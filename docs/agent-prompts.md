# Agent Prompts for Local Second Brain

Ready-to-use prompts. Store your own variants in `01_AI/Custom_Agents/`.

## Atomic Note Creator

> You are an expert at creating atomic notes.
> Take the following content and turn it into one clear atomic note with:
> - A clear title
> - One main idea
> - Links to related concepts as `[[wikilinks]]`
> - Proper YAML frontmatter matching this template: (paste `templates/atomic-note.md`)

## Meeting Summarizer

> Summarize this meeting transcript using the template below.
> Extract: agenda, key notes, decisions, and action items as `- [ ]` checkboxes with owners.
> Template: (paste `templates/meeting-notes.md`)

## Deep Research Agent

> Research the following topic and produce 3–5 atomic notes plus one index note that links them all together.
> Cite sources inline. Use the atomic note template for each note.

## Weekly Review Assistant

> Here are my open tasks and this week's daily notes.
> 1. Flag overdue tasks.
> 2. Suggest what to move from the Inbox to Tasks or Projects.
> 3. Draft next week's top 3 priorities.
