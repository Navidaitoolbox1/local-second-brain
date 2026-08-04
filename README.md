# Local Second Brain

A free, local-first, open-source alternative to Notion.

Capture, organize, and retrieve your knowledge using only local Markdown files — no subscriptions, no cloud lock-in, full privacy. Works with Obsidian and any LLM.

## ✨ Why Local Second Brain?

- **Complete Local System** — everything stored in plain Markdown files you own
- **Notion-style Workspace** — databases, projects, tasks, meeting notes, wiki
- **Interactive Dashboard** — a zero-dependency, offline HTML dashboard that reads your vault
- **AI-Ready** — agent prompts included; works with any LLM (cloud or fully local via Ollama)
- **Powerful Queries** — Obsidian + Dataview turn folders into databases
- **Version Controlled** — Git integration for backup and history
- **Cross-Platform** — Windows, macOS, and Linux

## 📁 Folder Structure

```
Local-Second-Brain/
├── 00_System_of_Record/       # Databases, projects, tasks, meetings, wiki, knowledge base
├── 01_AI/              # Agent prompts: custom agents, deep research, AI meeting notes
├── 02_Developer_Platform/     # CLI tools, webhooks, syncs, agent tools
├── 03_Connected_Workspace/    # Integration guides for external tools
├── 04_Business_Workflows/     # CRM, roadmaps, content pipelines
├── 05_Personal_Productivity/  # Personal OS: notes, tasks, goals, habits, reading lists
├── dashboard/                 # Interactive local dashboard (open index.html)
├── templates/                 # Ready-to-use note templates
└── docs/                      # Documentation
```

## 🛠️ Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/Navidaitoolbox1/local-second-brain.git
cd local-second-brain
```

### 2. Run setup

```bash
python setup.py .
```

(or `python setup.py ~/My-Vault` to create the structure elsewhere)

### 3. Open in Obsidian

1. Open Obsidian → **Open folder as vault**
2. Select this folder
3. Install recommended plugins (Dataview, Tasks, Templater)

### 4. Open the dashboard

![Dashboard preview](docs/dashboard-preview.png)

The dashboard is a single offline HTML file. **It must be run as a local file, not viewed on GitHub** (GitHub only shows the source, it does not execute HTML). To use it:

1. Download/clone the repo to your computer
2. Double-click `dashboard/index.html` so it opens in your browser (Chrome or Edge recommended for the folder picker)
3. Click **Open Vault Folder** and select this repository folder

The dashboard scans your Markdown files **locally** — tasks, projects, notes, and meetings with search, filters, and stats. No server, no network, nothing leaves your machine.

> Want a clickable link instead of a local file? Enable **GitHub Pages** (Settings → Pages → Deploy from branch → `main` / root). Then `https://<user>.github.io/<repo>/dashboard/` runs the dashboard over HTTPS with the full folder picker.

### 5. Start capturing

Drop ideas into `00_System_of_Record/Forms/Inbox.md`, then use the templates in [`templates/`](templates/) to create notes, tasks, and projects.

## 🤖 Using with AI Models

This system is designed to work with any LLM. Just copy a template and ask your model to fill it:

> "Use the Atomic Note template and turn this article into 3 atomic notes."

Ready-made prompts live in [docs/agent-prompts.md](docs/agent-prompts.md). For sensitive notes, use a local model — see [docs/free-llms.md](docs/free-llms.md).

## 📚 Documentation

- [Getting Started](docs/getting-started.md)
- [Obsidian Setup](docs/obsidian-setup.md)
- [Using AI Models](docs/free-llms.md)
- [Dataview Guide](docs/dataview-mastery.md)
- [Agent Prompts](docs/agent-prompts.md)

## 🧩 Recommended Tools

- **Obsidian** (core app)
- **Dataview** plugin
- **Tasks** plugin
- **Templater** plugin (needed for `{{date}}` placeholders in templates)
- **Obsidian Git** (backup)

## 📄 License

**PolyForm Noncommercial License 1.0.0** — free to use, modify, and share for any noncommercial purpose. Commercial use requires a separate license from the copyright holder. See [LICENSE](LICENSE) for full terms, or contact taheri.navid@gmail.com to discuss commercial use.

---

**Local Second Brain** — your workspace, organized locally and forever.
