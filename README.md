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
| `direct` | The original abstract as-is — fast and precise, saving tokens |
| `abstract` | A brief 2–3 sentence AI-generated summary — richer context |

### 3. Run it

Three options — pick whichever fits your workflow:

---

#### Option 1: Automate with GitHub Actions

Best for fully automated daily digests WITHOUT a local machine.

**Setup:**

1. Go to your repo on GitHub → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
   - **Name:** `ANTHROPIC_API_KEY`
   - **Secret:** your Anthropic API key
3. Go to **Settings** → **Actions** → **General** → scroll to **Workflow permissions** → select **Read and write permissions** → Save
4. That's it — the workflow runs daily at 9:00 AM PDT and commits results to `markdown/`

You can also trigger it manually from the **Actions** tab → **Daily arXiv Digest** → **Run workflow**.  

It uses Claude Sonnet 4.6 API and typically costs under $0.10 per day in `direct` mode.

---

#### Option 2: Schedule daily with Claude Cowork

Best for hands-free daily digests on your local machine.

Why not use the [Claude Code schedule tasks on the web](https://code.claude.com/docs/en/web-scheduled-tasks)? Because arXiv is not directly accessible from Claude Code's remote agent environment.

**Prerequisites:**

- A paid Claude plan with Cowork enabled
- [Claude Desktop](https://claude.ai/download)

**Setup:**

1. Open Claude Desktop → cowork tab → click **Scheduled** in the left sidebar
2. Click **+ New task**
3. Fill in:
   - **Name:** `ArXiv Daily Digest`
   - **Prompt:** Copy the contents of [`COWORK_TASK_PROMPT.md`](./COWORK_TASK_PROMPT.md) (it's only 6 lines)
   - **Model:** Claude Opus 4.6 or Sonnet 4.6
   - **Folder:** path to this cloned repo
   - **Frequency:** Daily 09:00 AM
4. Click **Save**

---

#### Option 3: Run manually with the Python script

Best for backfills, date ranges, or running from a server/cron job.

**Installation:**

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your-key-here
```

**Usage:**

```bash
# Yesterday's digest (default)
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

- **arXiv publishes new papers ~8:00 PM ET, Sunday through Thursday.** Schedule your task for the following morning to catch everything.
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
├── requirements.txt          # Python dependencies
├── .github/workflows/
│   └── daily_digest.yml      # GitHub Actions workflow
└── markdown/                 # Output digests go here
```

## License

[MIT](./LICENSE)

---

Built with [Claude Cowork](https://claude.com/product/cowork) & [Claude API](https://console.anthropic.com/) · Papers from [arXiv.org](https://arxiv.org)
