# Using Free LLMs with Local Notion

You can use any free LLM (Claude, ChatGPT free, Gemini, DeepSeek, local models via Ollama, etc.) to help you:

- Atomize ideas into notes
- Generate Dataview queries
- Summarize meetings into `00_System_of_Record/Meeting_Notes/`
- Draft project plans from a rough goal

## Workflow

1. Copy a template from `templates/`
2. Paste it into the LLM along with your raw content
3. Ask the model to fill the template (keep the YAML frontmatter intact)
4. Save the result into the matching folder

Example prompt:

> "Use this Atomic Note template and turn the following article into 3 atomic notes. Keep the YAML frontmatter and fill every field."

## Privacy Note

For sensitive notes, prefer a **local model** (e.g. via Ollama or LM Studio) so your data never leaves your machine — that is the whole point of Local Notion.
