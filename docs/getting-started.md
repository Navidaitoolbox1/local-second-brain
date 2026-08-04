# Getting Started with Local Second Brain

Welcome to your fully local, free, open-source alternative to Notion.

## Quick Start

1. Clone this repository
2. Run `python setup.py .` to fill in the folder structure (or `python setup.py ~/My-Vault` for a custom location)
3. Open the root folder in Obsidian ("Open folder as vault")
4. Start capturing ideas in `00_System_of_Record/Forms/Inbox.md`
5. Open `dashboard/index.html` in your browser for the interactive dashboard

## Folder Map

| Folder | Purpose |
|---|---|
| `00_System_of_Record/` | Databases, projects, tasks, meeting notes, wiki, knowledge base |
| `01_AI/` | Agent prompts: custom agents, deep research, AI meeting notes |
| `02_Developer_Platform/` | CLI tools, webhooks, syncs, agent tools |
| `03_Connected_Workspace/` | Integration guides for external tools |
| `04_Business_Workflows/` | CRM, roadmaps, content pipelines |
| `05_Personal_Productivity/` | Personal OS: notes, tasks, goals, habits, reading lists |

## Recommended Obsidian Plugins

- **Dataview** — query your notes like a database
- **Tasks** — task management with due dates
- **Templater** — required for the `{{date}}` placeholders in `templates/`
- **Obsidian Git** — automatic backup (optional)
