# claude-arxiv-daily-digest

A configurable daily arXiv paper tracker powered by [Claude Cowork](https://claude.com/product/cowork). Set your categories, keywords, and preferred mode — Claude fetches, filters, and summarizes the latest papers into a clean markdown digest every morning.

![Daily](https://img.shields.io/badge/schedule-daily-blue)
![Cowork](https://img.shields.io/badge/powered%20by-Claude%20Cowork-orange)
![arXiv](https://img.shields.io/badge/source-arXiv.org-b31b1b)

## Quick Start

### Prerequisites

- [Claude Desktop](https://claude.ai/download) (macOS or Windows)
- A paid Claude plan (Pro, Max, Team, or Enterprise) with Cowork enabled

### 1. Clone and set up

```bash
git clone https://github.com/BernieZhu/claude-arxiv-daily-digest.git

# Create the working directory and copy the config
mkdir -p ~/Documents/arxiv-daily-digest
cp claude-arxiv-daily-digest/arxiv_config.json ~/Documents/arxiv-daily-digest/
```

### 2. Edit the config

Open `~/Documents/arxiv-daily-digest/arxiv_config.json` and set your `categories`, `keywords`, and `mode`:

| Mode | What You Get |
|------|--------------|
| `direct` | The original abstract as-is — fast and precise |
| `abstract` | A brief 2–3 sentence AI-generated summary — richer context |

All settings are self-documented in the config file itself (look for `_`-prefixed keys).

### 3. Create the scheduled task in Cowork

1. Open Claude Desktop → click **Scheduled** in the left sidebar
2. Click **+ New task**
3. Fill in:
   - **Name:** `ArXiv Daily Digest`
   - **Prompt:** Copy the contents of [`COWORK_TASK_PROMPT.md`](./COWORK_TASK_PROMPT.md) (it's only 6 lines)
   - **Model:** Claude Opus 4.6 or Sonnet 4.6
   - **Folder:** `~/Documents/arxiv-daily-digest`
   - **Frequency:** Daily
4. Click **Save**

### 4. Test it

Click into the task and hit **Run Now**. Check `~/Documents/arxiv-daily-digest/` for your first digest.

## How It Works

```
┌─────────────────┐     ┌──────────────┐     ┌─────────────────┐
│  arxiv_config    │────▶│ Claude Cowork │────▶│ arxiv_digest_   │
│  .json           │     │ (scheduled)   │     │ 202X-XX-XX.md   │
└─────────────────┘     └──────┬───────┘     └─────────────────┘
                               │
                     ┌─────────┴─────────┐
                     │  arxiv.org/list/   │
                     │  {category}/new    │
                     └───────────────────┘
```

1. **Cowork reads** your `arxiv_config.json` — which contains *both* your settings and the execution instructions
2. **Scans** each category's new submissions on arXiv
3. **Filters** papers by your keywords
4. **Fetches** details using your chosen mode (direct abstract or full-page summary)
5. **Outputs** a dated markdown file to your local machine

### Design: Self-Describing Config

The config file contains an `instructions` object with every step Claude should follow. This means:

- **The Cowork prompt is permanent** — it just says "read the config and follow its instructions"
- **All changes happen in one file** — edit `arxiv_config.json` to change categories, keywords, mode, output format, or even the execution steps themselves
- **No prompt/config sync issues** — the config *is* the source of truth

```
arxiv_config.json
├── mode, categories, keywords      ← what to fetch
├── output, author_display          ← how to format
└── instructions                    ← how to execute (step_1 through step_7)
        │
        ▼
COWORK_TASK_PROMPT.md
└── "Read arxiv_config.json and follow its instructions."
    (never needs editing)
```

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
├── COWORK_TASK_PROMPT.md     # Minimal prompt — just reads the config
└── examples/
    └── arxiv_digest_example.md   # Sample output
```

## Contributing

Contributions welcome! Some ideas:

- Additional output formats (HTML, PDF, RSS)
- Slack/email notification integration via Cowork connectors
- Weekly rollup summaries
- Citation count integration
- New instruction steps (e.g., `step_8_notify` for Slack alerts)

## License

[MIT](./LICENSE)

---

Built with [Claude Cowork](https://claude.com/product/cowork) · Papers from [arXiv.org](https://arxiv.org)
