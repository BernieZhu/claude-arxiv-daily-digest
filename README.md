# claude-arxiv-daily-digest

A configurable daily arXiv paper tracker. Set your categories, keywords, and preferred mode — get the latest papers filtered and summarized into a clean markdown digest.

![Daily](https://img.shields.io/badge/schedule-daily-blue)
![Cowork](https://img.shields.io/badge/powered%20by-Claude%20Cowork-orange)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![arXiv](https://img.shields.io/badge/source-arXiv.org-b31b1b)

## Quick Start

### 1. Clone

```bash
git clone https://github.com/BernieZhu/claude-arxiv-daily-digest.git
cd claude-arxiv-daily-digest
```

### 2. Edit the config

Open `arxiv_config.json` and set your `categories`, `keywords`, and `mode`:

| Mode | What You Get |
|------|--------------|
| `direct` | The original abstract as-is — fast and precise |
| `abstract` | A brief 2–3 sentence AI-generated summary — richer context |

All settings are self-documented in the config file itself (look for `_`-prefixed keys).

### 3. Run it

Two options — pick whichever fits your workflow:

---

#### Option 1: Schedule daily with Claude Cowork

Best for hands-free daily digests on your local machine.

**Prerequisites:**

- [Claude Desktop](https://claude.ai/download) (macOS or Windows)
- A paid Claude plan (Pro, Max, Team, or Enterprise) with Cowork enabled

**Setup:**

1. Open Claude Desktop → click **Scheduled** in the left sidebar
2. Click **+ New task**
3. Fill in:
   - **Name:** `ArXiv Daily Digest`
   - **Prompt:** Copy the contents of [`COWORK_TASK_PROMPT.md`](./COWORK_TASK_PROMPT.md) (it's only 6 lines)
   - **Model:** Claude Opus 4.6 or Sonnet 4.6
   - **Folder:** path to this cloned repo
   - **Frequency:** Daily
4. Click **Save**

---

#### Option 2: Run manually with the Python script

Best for backfills, date ranges, or running from a server/cron job.

**Prerequisites:**

- Python 3.8+
- An [Anthropic API key](https://console.anthropic.com/)

**Installation:**

```bash
pip install requests beautifulsoup4 anthropic
export ANTHROPIC_API_KEY=your-key-here
```

**Usage:**

```bash
# Today's digest
python3 arxiv_digest.py

# Specific day
python3 arxiv_digest.py --start 2026-03-24

# Date range (one markdown file per day)
python3 arxiv_digest.py --start 2026-03-20 --end 2026-03-24
```

One markdown file per date is saved to the `markdown/` folder.

## Output Format

Each digest is a markdown file like `arxiv_digest_2017-06-12.md`:

```markdown
# arXiv Daily Digest — 2017-06-12

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.CL, cs.CV
**Keywords:** large language model, LLM, transformer, diffusion, ...
**Papers found:** 23

---

## 1. Attention Is All You Need

**Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar, ... , Llion Jones, Illia Polosukhin
**arXiv:** [1706.03762](https://arxiv.org/abs/1706.03762)
**Categories:** cs.CL, cs.LG

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks... We propose a new simple network architecture, the Transformer, based solely on attention mechanisms...

---
```

## Scheduling Tips

- **arXiv publishes new papers ~8:00 PM ET, Sunday through Thursday.** Schedule your task for the following morning (e.g., 7:00 AM local time) to catch everything.
- Your computer must be **awake** and Claude Desktop must be **open** for the task to run. Missed runs execute automatically on the next wake.
- The `abstract` mode uses more tokens than `direct` since it reads full HTML pages. If you're watching usage limits, start with `direct`.

## Repo Structure

```
claude-arxiv-daily-digest/
├── README.md                 # This file
├── LICENSE                   # MIT License
├── .gitignore                # Ignores output digests and OS files
├── arxiv_config.json         # Self-describing config (settings + instructions)
├── COWORK_TASK_PROMPT.md     # Minimal Cowork prompt
├── arxiv_digest.py           # Python script
└── markdown/                 # Output digests go here
```

## License

[MIT](./LICENSE)

---

Built with [Claude Cowork](https://claude.com/product/cowork) & [Claude API](https://console.anthropic.com/) · Papers from [arXiv.org](https://arxiv.org)
