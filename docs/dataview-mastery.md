# Dataview Mastery

Example queries that work with this vault's actual folder structure and the frontmatter fields used in `templates/`.

## All tasks that are not done

```dataview
TABLE due, priority, project
FROM "05_Personal_Productivity/Tasks"
WHERE type = "task" AND status != "Done"
SORT due ASC
```

## Active projects

```dataview
TABLE status, deadline
FROM "00_System_of_Record/Projects"
WHERE type = "project" AND status = "Active"
SORT deadline ASC
```

## Recent notes in the knowledge base

```dataview
TABLE created, domain
FROM "00_System_of_Record/Knowledge_Base"
WHERE type = "note"
SORT created DESC
LIMIT 20
```

## Meetings from the last 30 days

```dataview
TABLE date, participants
FROM "00_System_of_Record/Meeting_Notes"
WHERE type = "meeting" AND date >= date(today) - dur(30 days)
SORT date DESC
```
