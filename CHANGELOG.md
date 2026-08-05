# Changelog

All notable changes to Local Second Brain are documented here.

## v1.0.0

First public release. A free, local, open-source alternative to Notion, built on plain Markdown files.

### Added
- **Folder structure** created by `setup.py` (System of Record, AI, Developer Platform, Connected Workspace, Business Workflows, Personal Productivity).
- **Interactive dashboard** (`dashboard/index.html`), a single offline HTML file:
  - List views for Tasks, Projects, Notes, and Meetings with stats, overdue detection, search, filters, and sorting.
  - **Board**: a Todo / Doing / Done kanban with drag and drop that writes `status` back to the file.
  - **In-place editor**: click any item to edit it in a friendly form (title, status buttons, priority, due date, clean writing area). **＋ New** creates a task, project, note, or meeting from a template.
  - **Write / Preview** toggle with a small built-in, XSS-safe Markdown renderer.
  - **Drag and drop into a note** to attach images (copied to `attachments/`, or embedded inline without write access) or paste in text files.
  - **Reorganize by dragging** an item onto another view in the sidebar to move its file to that folder.
  - **PIN lock** and a **Settings** panel (PIN, default view, scan options), stored in the browser only.
  - Reads and writes local files via the File System Access API in Chrome and Edge; falls back to a read-only folder upload elsewhere. Nothing leaves your machine.
- **Templates** for atomic notes, tasks, projects, and meetings.
- **Docs**: getting started, Obsidian setup, using free LLMs, a Dataview guide, agent prompts, and a "Roadmap to master Claude" guide.
- **Starter content** so the dashboard shows real data on first open.

### License
- **PolyForm Noncommercial License 1.0.0**: free for any noncommercial use; commercial use requires a separate license from the copyright holder.
