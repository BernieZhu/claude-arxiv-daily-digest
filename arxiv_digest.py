#!/usr/bin/env python3
"""
arxiv_digest.py - Fetch and filter arXiv papers for a date range.

Usage:
    python3 arxiv_digest.py                      # yesterday
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
# Step 1: Fetch paper listings from arXiv
# ---------------------------------------------------------------------------

def _parse_papers_from_dl(dl_tag, category):
    """Extract papers from a <dl> tag. Returns list of paper dicts."""
    papers = []
    dts = dl_tag.find_all("dt")
    dds = dl_tag.find_all("dd")

    for dt_tag, dd_tag in zip(dts, dds):
        link = dt_tag.find("a", title="Abstract")
        if not link:
            continue
        href = link.get("href", "")
        id_match = re.search(r"(\d{4}\.\d{4,5}(?:v\d+)?)", href)
        if not id_match:
            continue
        paper_id = re.sub(r"v\d+$", "", id_match.group(1))

        title = ""
        title_div = dd_tag.find("div", class_="list-title")
        if title_div:
            desc = title_div.find("span", class_="descriptor")
            if desc:
                desc.decompose()
            title = title_div.get_text().strip()

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


def _date_from_arxiv_id(arxiv_id):
    """Derive YYYY-MM-DD from an arxiv ID like '2603.12345' → '2026-03-12'."""
    m = re.match(r"(\d{2})(\d{2})\.(\d{2})", arxiv_id)
    if m:
        yy, mm, dd = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return f"20{yy:02d}-{mm:02d}-{dd:02d}"
    return None


def _fetch_papers_by_date(category):
    """Fetch papers from pastweek listing, grouped by YYYY-MM-DD from arxiv ID.
    Returns {YYYY-MM-DD: [papers]}."""
    url = ARXIV_LIST_PASTWEEK_URL.format(category)
    print(f"  Fetching {url} ...")
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    date_papers = {}
    for dl_tag in soup.find_all("dl"):
        papers = _parse_papers_from_dl(dl_tag, category)
        for p in papers:
            date_key = _date_from_arxiv_id(p["id"])
            if date_key:
                date_papers.setdefault(date_key, []).append(p)

    return date_papers


def fetch_papers_for_dates(categories, target_dates):
    """Fetch and deduplicate papers across categories for target dates.
    Returns {date_str: [papers]}."""
    result = {d: {} for d in target_dates}

    for cat in categories:
        try:
            date_papers = _fetch_papers_by_date(cat)
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
        time.sleep(1)

    return {d: list(papers.values()) for d, papers in result.items()}


# ---------------------------------------------------------------------------
# Step 2: Keyword matching
# ---------------------------------------------------------------------------

def _normalize(text):
    """Normalize text for fuzzy matching: lowercase, strip hyphens/punctuation, collapse whitespace."""
    text = text.lower()
    text = re.sub(r"[-/]", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _make_keyword_pattern(keyword):
    """Build a regex pattern for fuzzy matching a keyword.
    Handles: plurals, optional hyphens/spaces, morphological variants."""
    normalized = _normalize(keyword)
    words = normalized.split()
    word_patterns = []
    for w in words:
        stem = re.sub(r"(ing|tion|ment|ed|er|est|ly|ise|ize|s|es)$", "", w)
        if len(stem) < 2:
            stem = w
        word_patterns.append(rf"{re.escape(stem)}\w*")
    return re.compile(r"[\s\-]?".join(word_patterns), re.IGNORECASE)


def _text_matches_keywords(text, keywords, acronym_expansions=None):
    """Check if text fuzzy-matches any keyword.
    Checks: substring, regex morphological variants, acronym expansions."""
    normalized = _normalize(text)
    expansions = acronym_expansions or {}
    for kw in keywords:
        if _normalize(kw) in normalized:
            return True
        if _make_keyword_pattern(kw).search(normalized):
            return True
        for expansion in expansions.get(kw.upper(), []):
            if _normalize(expansion) in normalized:
                return True
    return False


# ---------------------------------------------------------------------------
# Step 2b: Fetch metadata from abs pages (only for candidate papers)
# ---------------------------------------------------------------------------

def _parse_abs_page(soup):
    """Extract title, authors, abstract, categories from a parsed abs page."""
    result = {}

    title_tag = soup.find("h1", class_="title")
    if title_tag:
        desc = title_tag.find("span", class_="descriptor")
        if desc:
            desc.decompose()
        result["title"] = title_tag.get_text().strip()

    authors_div = soup.find("div", class_="authors")
    if authors_div:
        authors = [a.get_text().strip() for a in authors_div.find_all("a")]
        if not authors:
            desc = authors_div.find("span", class_="descriptor")
            if desc:
                desc.decompose()
            authors = [x.strip() for x in authors_div.get_text().split(",") if x.strip()]
        result["authors"] = authors

    abs_tag = soup.find("blockquote", class_="abstract")
    if abs_tag:
        desc = abs_tag.find("span", class_="descriptor")
        if desc:
            desc.decompose()
        result["abstract"] = abs_tag.get_text().strip()

    subj_td = soup.find("td", class_="tablecell subjects")
    if subj_td:
        result["categories"] = subj_td.get_text().strip()

    return result


def fetch_paper_metadata(papers):
    """Fetch full abstract, authors, and categories from arxiv abs pages.
    Only fetches for papers missing metadata. Modifies papers in-place."""
    for i, p in enumerate(papers):
        if p.get("abstract") and p.get("authors"):
            continue
        url = ARXIV_ABS_URL.format(p["id"])
        try:
            print(f"  [{i+1}/{len(papers)}] Fetching metadata for {p['id']}...")
            resp = requests.get(url, timeout=30)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            metadata = _parse_abs_page(soup)
            p.update(metadata)
        except Exception as e:
            print(f"    Error fetching metadata: {e}")
            if not p.get("abstract"):
                p["abstract"] = p.get("abstract_snippet", "")
        time.sleep(0.5)


# ---------------------------------------------------------------------------
# Step 2c: Claude verification for abstract-matched candidates
# ---------------------------------------------------------------------------

def _verify_with_claude(client, papers, keywords):
    """Send papers to Claude for semantic keyword verification.
    Returns list of papers that Claude confirms as relevant."""
    if not papers:
        return []

    matched = []
    matched_ids = set()
    batch_size = 30

    for batch_start in range(0, len(papers), batch_size):
        batch = papers[batch_start:batch_start + batch_size]
        paper_lines = []
        for i, p in enumerate(batch):
            abstract = p.get("abstract", p.get("abstract_snippet", ""))
            paper_lines.append(f"[{i}] Title: {p['title']}\nAbstract: {abstract}")

        prompt = f"""Filter these arXiv papers. Return ONLY indices of papers that are **directly relevant** to at least one keyword.

Keywords: {', '.join(keywords)}

Matching rules (MUST match):
1. Case-insensitive, morphological variants OK ('model' matches 'models', 'modeling')
2. Sub-word/token matches OK ('VLA' matches 'VLA-based', 'OpenVLA')
3. Acronym expansions MUST match: 'VLA' = 'Vision-Language-Action', so any paper mentioning 'Vision-Language-Action' matches 'VLA'
4. Multi-word keywords: match as coherent phrase ('world model' matches 'world models', 'world-model', 'world model-based')
5. A keyword match ANYWHERE in the title or abstract counts — even a single mention is enough if the keyword clearly appears

Rejection rules (MUST reject — these are STRICT):
- VLM (Vision-Language Model) is NOT VLA. VLN (Vision-Language Navigation) is NOT VLA. LLM is NOT VLA. Only 'VLA' or 'Vision-Language-Action' matches the keyword 'VLA'
- Generic 'model' does NOT match 'world model'. The word 'world' must appear near 'model'
- Papers about navigation, VLMs, LLMs, or general AI do NOT match unless they explicitly mention VLA/Vision-Language-Action or world model
- The exact keyword string or its direct expansion must actually appear in the text

Papers:
{chr(10).join(paper_lines)}

Respond with ONLY a JSON array. No explanation, no reasoning, no markdown fences.
Format: [{{"index": 0, "keyword": "matched keyword"}}]
If no papers match, respond with exactly: []"""

        print(f"  Asking Claude to verify batch {batch_start // batch_size + 1} ({len(batch)} papers)...")
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2048,
            system="You are a JSON-only filter. Output raw JSON arrays only. Never explain your reasoning. Never use markdown code fences.",
            messages=[{"role": "user", "content": prompt}],
        )

        text = response.content[0].text.strip()
        json_match = re.search(r"\[.*\]", text, re.DOTALL)
        if json_match:
            try:
                results = json.loads(json_match.group())
                for item in results:
                    if isinstance(item, dict):
                        idx = item.get("index", -1)
                        kw = item.get("keyword", "")
                    elif isinstance(item, int):
                        idx, kw = item, ""
                    else:
                        continue
                    if 0 <= idx < len(batch):
                        paper = batch[idx]
                        if paper["id"] not in matched_ids:
                            paper["matched_keyword"] = kw
                            matched.append(paper)
                            matched_ids.add(paper["id"])
                            print(f"    Matched [{idx}] \"{paper['title'][:60]}\" -> {kw}")
            except json.JSONDecodeError:
                print(f"  Warning: Could not parse filter response: {text[:200]}")
        else:
            print(f"  Warning: Could not parse filter response: {text[:200]}")

    return matched


# ---------------------------------------------------------------------------
# Step 2 combined: Filter pipeline (title → snippet → metadata → Claude)
# ---------------------------------------------------------------------------

def _claude_title_scan(client, papers, keywords):
    """Send papers with only titles to Claude for a quick relevance scan.
    Returns papers Claude thinks might be relevant (need full abstract check)."""
    if not papers:
        return []

    candidates = []
    batch_size = 100  # titles only, so we can send more per batch

    for batch_start in range(0, len(papers), batch_size):
        batch = papers[batch_start:batch_start + batch_size]
        title_lines = [f"[{i}] {p['title']}" for i, p in enumerate(batch)]

        prompt = f"""From these arXiv paper titles, identify which ones are LIKELY to be about any of these keywords (they may use the concept without the exact words):

Keywords: {', '.join(keywords)}
Keyword expansions: VLA = Vision-Language-Action, world model = learned environment simulator/predictor

Return indices of papers whose title suggests they MIGHT discuss these topics.
Be moderately inclusive — if a title hints at the topic, include it. We will verify with full abstracts later.

Titles:
{chr(10).join(title_lines)}

Respond with ONLY a JSON array of integers, e.g. [0, 3, 7]. If none match, respond with: []"""

        print(f"  Claude title scan batch {batch_start // batch_size + 1} ({len(batch)} titles)...")
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2048,
            system="You are a JSON-only filter. Output raw JSON arrays only. Never explain your reasoning.",
            messages=[{"role": "user", "content": prompt}],
        )

        text = response.content[0].text.strip()
        json_match = re.search(r"\[[\d\s,]*\]", text)
        if json_match:
            try:
                indices = json.loads(json_match.group())
                for idx in indices:
                    if 0 <= idx < len(batch):
                        candidates.append(batch[idx])
                        print(f"    Flagged [{idx}] \"{batch[idx]['title'][:70]}\"")
            except json.JSONDecodeError:
                print(f"  Warning: Could not parse title scan response: {text[:200]}")

    return candidates


def filter_papers(client, papers, keywords, acronym_expansions=None):
    """Four-tier filtering pipeline:
    1. Title keyword match (free) → accepted immediately
    2. Snippet keyword match → fetch abstract → Claude verification
    3. Remaining papers → Claude title scan → fetch abstract → keyword check on full abstract
    4. No match → skipped
    Returns filtered papers with full metadata."""
    title_matched = []
    snippet_candidates = []
    remaining = []

    for p in papers:
        if _text_matches_keywords(p.get("title", ""), keywords, acronym_expansions):
            title_matched.append(p)
        elif _text_matches_keywords(p.get("abstract_snippet", ""), keywords, acronym_expansions):
            snippet_candidates.append(p)
        else:
            remaining.append(p)

    print(f"  {len(title_matched)} papers matched by title")
    print(f"  {len(snippet_candidates)} papers have keyword in snippet (need verification)")
    print(f"  {len(remaining)} papers need title scan")

    # Tier 3: Claude scans remaining titles for potential relevance
    title_scan_candidates = _claude_title_scan(client, remaining, keywords)
    if title_scan_candidates:
        print(f"  {len(title_scan_candidates)} papers flagged by Claude title scan, fetching abstracts...")
        fetch_paper_metadata(title_scan_candidates)
        # Check full abstracts for keyword matches
        abstract_confirmed = []
        for p in title_scan_candidates:
            abstract = p.get("abstract", p.get("abstract_snippet", ""))
            if _text_matches_keywords(abstract, keywords, acronym_expansions):
                abstract_confirmed.append(p)
                print(f"    Confirmed: \"{p['title'][:60]}\" (keyword in abstract)")
        if abstract_confirmed:
            print(f"  {len(abstract_confirmed)} confirmed by full abstract keyword check")
    else:
        abstract_confirmed = []

    # Fetch metadata for title-matched + snippet candidates
    all_candidates = title_matched + snippet_candidates
    if all_candidates:
        print(f"  Fetching metadata for {len(all_candidates)} candidate papers...")
        fetch_paper_metadata(all_candidates)

    # Claude verifies only the snippet-matched papers (title-matched are already accepted)
    claude_verified = _verify_with_claude(client, snippet_candidates, keywords)

    # Combine and deduplicate
    seen = set()
    filtered = []
    for p in title_matched + claude_verified + abstract_confirmed:
        if p["id"] not in seen:
            seen.add(p["id"])
            filtered.append(p)

    return filtered


# ---------------------------------------------------------------------------
# Abstract mode: generate summaries with Claude
# ---------------------------------------------------------------------------

def _summarize_paper(client, paper):
    """Fetch HTML page and generate 2-3 sentence summary with Claude."""
    url = ARXIV_HTML_URL.format(paper["id"])
    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        body = soup.find("article") or soup.find("body")
        text_content = body.get_text()[:8000] if body else ""
    except Exception:
        text_content = paper.get("abstract", "")

    prompt = f"""Read this arXiv paper content and write a brief 2-3 sentence summary in your own words. Do NOT copy the abstract verbatim. Focus on the key contribution and methodology.

Title: {paper['title']}

Content:
{text_content}

Return ONLY the 2-3 sentence summary."""

    print(f"    Summarizing {paper['id']}...")
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )
    paper["summary"] = response.content[0].text.strip()


def generate_summaries(client, papers):
    """Generate Claude summaries for all papers (abstract mode only)."""
    for i, p in enumerate(papers):
        print(f"  [{i+1}/{len(papers)}] Summarizing {p['id']}...")
        try:
            _summarize_paper(client, p)
        except Exception as e:
            print(f"    Error: {e}")
        time.sleep(1)


# ---------------------------------------------------------------------------
# Output: Format authors and generate markdown
# ---------------------------------------------------------------------------

def _format_authors(authors, config):
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
        authors = _format_authors(p.get("authors", []), config)
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
# Main pipeline
# ---------------------------------------------------------------------------

def _print_report(papers, output_path, total_fetched, date_str):
    print(f"\n{'='*60}")
    print(f"  Date: {date_str}")
    print(f"  Papers fetched: {total_fetched}")
    print(f"  Papers matched: {len(papers)}")
    print(f"  Output: {output_path}")
    print(f"{'='*60}\n")


def process_date(date_str, papers_for_date, config, mode, client):
    """Process a single date: filter, fetch details, generate markdown."""
    total_fetched = len(papers_for_date)
    print(f"\n--- {date_str}: {total_fetched} papers found ---")

    if not papers_for_date:
        print("  No papers, skipping.")
        return

    # Filter: title match → snippet match → Claude verify (fetches metadata for candidates only)
    print("Step 2: Filtering by keywords...")
    filtered = filter_papers(client, papers_for_date, config["keywords"],
                             config.get("acronym_expansions", {}))
    print(f"  {len(filtered)} papers match keywords")

    if not filtered:
        print("  No matches, skipping.")
        return

    max_papers = config.get("max_papers_per_day", 100)
    if len(filtered) > max_papers:
        print(f"  Capping output to {max_papers} papers (from {len(filtered)})")
        filtered = filtered[:max_papers]

    # In abstract mode, generate summaries
    if mode == "abstract":
        print("Step 3: Generating summaries...")
        generate_summaries(client, filtered)

    # Generate markdown
    print("Step 4: Generating markdown...")
    markdown = generate_markdown(filtered, date_str, config, mode)

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

    _print_report(filtered, output_path, total_fetched, date_str)


def main():
    parser = argparse.ArgumentParser(description="arXiv Daily Digest (Python)")
    parser.add_argument("--start", help="Start date (YYYY-MM-DD), defaults to yesterday (with weekend logic)")
    parser.add_argument("--end", help="End date (YYYY-MM-DD), defaults to start")
    parser.add_argument("--config", help="Path to config file")
    args = parser.parse_args()

    config = load_config(args.config)
    mode = config.get("mode", "direct")

    # arXiv publishes new papers ~8PM ET, Sunday through Thursday.
    # No new papers on Friday or Saturday.
    # When no date is specified:
    #   Friday    → skip (nothing to fetch)
    #   Saturday  → skip (nothing to fetch)
    #   Sunday    → fetch Friday and Saturday
    #   Other days → fetch yesterday
    if args.start is None:
        today = datetime.now()
        weekday = today.weekday()  # 0=Mon, 4=Fri, 5=Sat, 6=Sun
        if weekday == 4:  # Friday
            print("Today is Friday — arXiv has no new papers. Nothing to do.")
            sys.exit(0)
        elif weekday == 5:  # Saturday
            print("Today is Saturday — arXiv has no new papers. Nothing to do.")
            sys.exit(0)
        elif weekday == 6:  # Sunday
            args.start = (today - timedelta(days=2)).strftime("%Y-%m-%d")  # Friday
            args.end = args.end or (today - timedelta(days=1)).strftime("%Y-%m-%d")  # Saturday
        else:
            args.start = (today - timedelta(days=1)).strftime("%Y-%m-%d")
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

    print("\nStep 1: Fetching papers from arXiv...")
    all_date_papers = fetch_papers_for_dates(config["categories"], target_dates)

    for date_str in target_dates:
        papers = all_date_papers.get(date_str, [])
        process_date(date_str, papers, config, mode, client)

    print("\nDone!")


if __name__ == "__main__":
    main()
