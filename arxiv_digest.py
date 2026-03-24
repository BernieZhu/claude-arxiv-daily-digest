#!/usr/bin/env python3
"""
arxiv_digest.py - Fetch and filter arXiv papers for a date range.

Usage:
    python3 arxiv_digest.py                      # today
    python3 arxiv_digest.py --start 2026-03-24   # specific day
    python3 arxiv_digest.py --start 2026-03-20 --end 2026-03-24  # date range
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

try:
    import anthropic
except ImportError:
    anthropic = None

ARXIV_ABS_URL = "https://arxiv.org/abs/{}"
ARXIV_HTML_URL = "https://arxiv.org/html/{}"
ARXIV_LIST_NEW_URL = "https://arxiv.org/list/{}/new"
ARXIV_LIST_PASTWEEK_URL = "https://arxiv.org/list/{}/pastweek?show=2000"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "arxiv_config.json")


def load_config(path=None):
    with open(path or CONFIG_PATH) as f:
        return json.load(f)


def get_claude_client():
    if anthropic is None:
        print("Error: anthropic package required. Install with: pip install anthropic")
        sys.exit(1)
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Export it with: export ANTHROPIC_API_KEY=your-key-here")
        sys.exit(1)
    return anthropic.Anthropic(api_key=api_key)


# ---------------------------------------------------------------------------
# Step 1: Fetch papers from arxiv listing pages
# ---------------------------------------------------------------------------

def parse_date_from_h3(h3_text):
    """Parse a date string from an h3 heading like 'Tue, 24 Mar 2026 (showing ...)'."""
    m = re.search(r"(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{4})", h3_text)
    if m:
        return datetime.strptime(f"{m.group(1)} {m.group(2)} {m.group(3)}", "%d %b %Y").strftime("%Y-%m-%d")
    return None


def parse_papers_from_dl(dl_tag, category):
    """Extract papers from a <dl> tag. Returns list of paper dicts."""
    papers = []
    dts = dl_tag.find_all("dt")
    dds = dl_tag.find_all("dd")

    for dt_tag, dd_tag in zip(dts, dds):
        # Extract paper ID
        link = dt_tag.find("a", title="Abstract")
        if not link:
            continue
        href = link.get("href", "")
        id_match = re.search(r"(\d{4}\.\d{4,5}(?:v\d+)?)", href)
        if not id_match:
            continue
        paper_id = re.sub(r"v\d+$", "", id_match.group(1))

        # Extract title
        title = ""
        title_div = dd_tag.find("div", class_="list-title")
        if title_div:
            # Remove the "Title:" descriptor span
            desc = title_div.find("span", class_="descriptor")
            if desc:
                desc.decompose()
            title = title_div.get_text().strip()

        # Extract abstract snippet if present
        abstract_snippet = ""
        abs_p = dd_tag.find("p", class_="mathjax")
        if abs_p:
            abstract_snippet = abs_p.get_text().strip()

        papers.append({
            "id": paper_id,
            "title": title,
            "abstract_snippet": abstract_snippet,
            "category": category,
        })

    return papers


def fetch_papers_by_date(category):
    """Fetch papers from pastweek listing, grouped by date. Returns {date_str: [papers]}."""
    url = ARXIV_LIST_PASTWEEK_URL.format(category)
    print(f"  Fetching {url} ...")
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Structure: DL appears before its corresponding H3
    # Collect all DL and H3 in order
    tags = soup.find_all(["dl", "h3"])

    date_papers = {}
    pending_dl = None

    for tag in tags:
        if tag.name == "dl":
            pending_dl = tag
        elif tag.name == "h3" and pending_dl is not None:
            date_str = parse_date_from_h3(tag.get_text())
            if date_str:
                papers = parse_papers_from_dl(pending_dl, category)
                date_papers[date_str] = papers
            pending_dl = None

    return date_papers


def fetch_papers_for_dates(categories, target_dates):
    """Fetch and deduplicate papers across categories for target dates.
    Returns {date_str: [papers]}."""
    result = {d: {} for d in target_dates}  # date -> {paper_id: paper}

    for cat in categories:
        try:
            date_papers = fetch_papers_by_date(cat)
            for date_str in target_dates:
                if date_str in date_papers:
                    for p in date_papers[date_str]:
                        pid = p["id"]
                        if pid not in result[date_str]:
                            p["categories_found"] = [cat]
                            result[date_str][pid] = p
                        else:
                            result[date_str][pid]["categories_found"].append(cat)
        except Exception as e:
            print(f"  Error fetching {cat}: {e}")
        time.sleep(1)  # rate limit

    return {d: list(papers.values()) for d, papers in result.items()}


# ---------------------------------------------------------------------------
# Step 2: Filter papers by keywords (uses Claude for fuzzy matching)
# ---------------------------------------------------------------------------

def filter_papers_with_claude(client, papers, keywords):
    """Use Claude to fuzzy-match papers against keywords."""
    if not papers:
        return []

    paper_lines = []
    for i, p in enumerate(papers):
        line = f"[{i}] {p['title']}"
        if p.get("abstract_snippet"):
            line += f" | {p['abstract_snippet'][:200]}"
        paper_lines.append(line)

    prompt = f"""Filter these arXiv papers. Return ONLY indices whose title or snippet fuzzy-matches at least one keyword.

Keywords: {', '.join(keywords)}

Fuzzy matching: case-insensitive, morphological variants ('model' matches 'models'/'modeling'), sub-word matches ('VLA' matches 'VLA-based'/'OpenVLA'), semantic equivalents ('world model' matches 'model of the world'), abbreviation expansion.

Papers:
{chr(10).join(paper_lines)}

Return ONLY a JSON array of matching indices, e.g. [0, 3, 7]. Nothing else."""

    print(f"  Asking Claude to filter {len(papers)} papers...")
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text.strip()
    match = re.search(r"\[[\d\s,]*\]", text)
    if match:
        indices = json.loads(match.group())
        return [papers[i] for i in indices if 0 <= i < len(papers)]
    print(f"  Warning: Could not parse filter response: {text[:200]}")
    return []


# ---------------------------------------------------------------------------
# Step 3: Fetch paper details
# ---------------------------------------------------------------------------

def fetch_paper_details_direct(paper_id):
    """Fetch title, authors, abstract, categories from arxiv abs page."""
    url = ARXIV_ABS_URL.format(paper_id)
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    title = ""
    title_tag = soup.find("h1", class_="title")
    if title_tag:
        desc = title_tag.find("span", class_="descriptor")
        if desc:
            desc.decompose()
        title = title_tag.get_text().strip()

    authors = []
    authors_div = soup.find("div", class_="authors")
    if authors_div:
        for a in authors_div.find_all("a"):
            authors.append(a.get_text().strip())
        if not authors:
            desc = authors_div.find("span", class_="descriptor")
            if desc:
                desc.decompose()
            authors = [x.strip() for x in authors_div.get_text().split(",") if x.strip()]

    abstract = ""
    abs_tag = soup.find("blockquote", class_="abstract")
    if abs_tag:
        desc = abs_tag.find("span", class_="descriptor")
        if desc:
            desc.decompose()
        abstract = abs_tag.get_text().strip()

    categories = ""
    subj_td = soup.find("td", class_="tablecell subjects")
    if subj_td:
        categories = subj_td.get_text().strip()

    return {
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "categories": categories,
    }


def fetch_paper_details_abstract(client, paper_id):
    """Fetch HTML page and generate 2-3 sentence summary with Claude."""
    # Get metadata from abs page first
    details = fetch_paper_details_direct(paper_id)

    # Fetch full HTML
    url = ARXIV_HTML_URL.format(paper_id)
    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        body = soup.find("article") or soup.find("body")
        text_content = body.get_text()[:8000] if body else ""
    except Exception:
        # Fall back to abstract if HTML not available
        text_content = details.get("abstract", "")

    prompt = f"""Read this arXiv paper content and write a brief 2-3 sentence summary in your own words. Do NOT copy the abstract verbatim. Focus on the key contribution and methodology.

Title: {details['title']}

Content:
{text_content}

Return ONLY the 2-3 sentence summary."""

    print(f"    Summarizing {paper_id}...")
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )
    details["summary"] = response.content[0].text.strip()
    return details


def fetch_all_details(client, papers, mode):
    """Fetch full details for all filtered papers."""
    detailed = []
    for i, p in enumerate(papers):
        print(f"  [{i+1}/{len(papers)}] Fetching {p['id']}...")
        try:
            if mode == "abstract" and client:
                d = fetch_paper_details_abstract(client, p["id"])
            else:
                d = fetch_paper_details_direct(p["id"])
            d["id"] = p["id"]
            d["categories_found"] = p.get("categories_found", [])
            detailed.append(d)
        except Exception as e:
            print(f"    Error: {e}")
        time.sleep(1)
    return detailed


# ---------------------------------------------------------------------------
# Step 4: Format authors
# ---------------------------------------------------------------------------

def format_authors(authors, config):
    """Format author list per config author_display settings."""
    if isinstance(authors, str):
        authors = [a.strip() for a in authors.split(",") if a.strip()]
    if not authors:
        return "Unknown"

    display = config.get("author_display", {})
    max_first = display.get("max_first", 3)
    max_last = display.get("max_last", 2)
    sep = display.get("separator", ", ")
    ellipsis = display.get("ellipsis", "...")

    if len(authors) <= max_first + max_last:
        return sep.join(authors)

    return sep.join(authors[:max_first]) + sep + ellipsis + sep + sep.join(authors[-max_last:])


# ---------------------------------------------------------------------------
# Steps 5-6: Generate markdown
# ---------------------------------------------------------------------------

def generate_markdown(papers, date_str, config, mode):
    """Generate the markdown file content."""
    lines = [
        f"# arXiv Daily Digest — {date_str}",
        "",
        f"**Mode:** {mode}",
        f"**Categories:** {', '.join(config['categories'])}",
        f"**Keywords:** {', '.join(config['keywords'])}",
        f"**Papers found:** {len(papers)}",
        "",
        "---",
        "",
    ]

    for i, p in enumerate(papers, 1):
        title = p.get("title", "Unknown Title")
        pid = p["id"]
        authors = format_authors(p.get("authors", []), config)
        cats = p.get("categories", ", ".join(p.get("categories_found", [])))

        lines.append(f"## {i}. {title}")
        lines.append("")
        lines.append(f"**Authors:** {authors}")
        lines.append(f"**arXiv:** [{pid}](https://arxiv.org/abs/{pid})")
        lines.append(f"**Categories:** {cats}")
        lines.append("")

        if mode == "abstract" and "summary" in p:
            lines.append(p["summary"])
        else:
            lines.append(p.get("abstract", "No abstract available."))

        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Step 7: Report
# ---------------------------------------------------------------------------

def print_report(papers, output_path, total_fetched, date_str):
    print(f"\n{'='*60}")
    print(f"  Date: {date_str}")
    print(f"  Papers fetched: {total_fetched}")
    print(f"  Papers matched: {len(papers)}")
    print(f"  Output: {output_path}")
    if papers:
        print(f"\n  Top {min(5, len(papers))} titles:")
        for i, p in enumerate(papers[:5], 1):
            print(f"    {i}. {p.get('title', '?')[:80]}")
    print(f"{'='*60}\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_date(date_str, papers_for_date, config, mode, client):
    """Process a single date: filter, fetch details, generate markdown."""
    papers = papers_for_date
    total_fetched = len(papers)
    print(f"\n--- {date_str}: {total_fetched} papers found ---")

    if not papers:
        print("  No papers, skipping.")
        return

    # Step 2: Filter
    print("Step 2: Filtering by keywords...")
    filtered = filter_papers_with_claude(client, papers, config["keywords"])
    print(f"  {len(filtered)} papers match keywords")

    if not filtered:
        print("  No matches, skipping.")
        return

    # Cap output to max_papers_per_day
    max_papers = config.get("max_papers_per_day", 100)
    if len(filtered) > max_papers:
        print(f"  Capping output to {max_papers} papers (from {len(filtered)})")
        filtered = filtered[:max_papers]

    # Step 3: Fetch details
    print(f"Step 3: Fetching details (mode={mode})...")
    detailed = fetch_all_details(client, filtered, mode)

    # Steps 4-6: Generate markdown
    print("Steps 4-6: Generating markdown...")
    markdown = generate_markdown(detailed, date_str, config, mode)

    output_folder = os.path.join(SCRIPT_DIR, config["output"].get("output_folder", "markdown"))
    os.makedirs(output_folder, exist_ok=True)

    dt = datetime.strptime(date_str, "%Y-%m-%d")
    filename = (
        config["output"].get("filename_template", "arxiv_digest_{YYYY}-{MM}-{DD}.md")
        .replace("{YYYY}", dt.strftime("%Y"))
        .replace("{MM}", dt.strftime("%m"))
        .replace("{DD}", dt.strftime("%d"))
    )
    output_path = os.path.join(output_folder, filename)

    with open(output_path, "w") as f:
        f.write(markdown)

    # Step 7
    print_report(detailed, output_path, total_fetched, date_str)


def main():
    parser = argparse.ArgumentParser(description="arXiv Daily Digest (Python)")
    parser.add_argument("--start", default=datetime.now().strftime("%Y-%m-%d"), help="Start date (YYYY-MM-DD), defaults to today")
    parser.add_argument("--end", help="End date (YYYY-MM-DD), defaults to start")
    parser.add_argument("--config", help="Path to config file")
    args = parser.parse_args()

    config = load_config(args.config)
    mode = config.get("mode", "direct")
    end_date = args.end or args.start

    try:
        start_dt = datetime.strptime(args.start, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Error: Dates must be YYYY-MM-DD format")
        sys.exit(1)

    if end_dt < start_dt:
        print("Error: End date must be >= start date")
        sys.exit(1)

    client = get_claude_client()

    # Build list of target dates
    target_dates = []
    cur = start_dt
    while cur <= end_dt:
        target_dates.append(cur.strftime("%Y-%m-%d"))
        cur += timedelta(days=1)

    print(f"arXiv Daily Digest (Python)")
    print(f"  Dates: {target_dates[0]} to {target_dates[-1]} ({len(target_dates)} days)")
    print(f"  Mode: {mode}")
    print(f"  Categories: {', '.join(config['categories'])}")
    print(f"  Keywords: {', '.join(config['keywords'])}")

    # Step 1: Fetch all papers, grouped by date, across categories
    print("\nStep 1: Fetching papers from arXiv...")
    all_date_papers = fetch_papers_for_dates(config["categories"], target_dates)

    # Process each date
    for date_str in target_dates:
        papers = all_date_papers.get(date_str, [])
        process_date(date_str, papers, config, mode, client)

    print("\nDone!")


if __name__ == "__main__":
    main()
