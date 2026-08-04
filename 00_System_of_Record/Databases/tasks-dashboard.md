---
type: dashboard
tags: [dashboard, dataview]
---

# 📊 Tasks Dashboard (Obsidian + Dataview)

Requires the **Dataview** plugin. These queries read the same frontmatter the HTML dashboard uses.

## ⚠️ Overdue & open tasks
```dataview
TABLE priority, due, project
FROM "05_Personal_Productivity/Tasks"
WHERE type = "task" AND status != "Done"
SORT due ASC
```

## 🚀 Active projects
```dataview
TABLE status, deadline
FROM "00_System_of_Record/Projects"
WHERE type = "project" AND status = "Active"
SORT deadline ASC
```

## 📝 Recently created notes
```dataview
TABLE created, domain
FROM "00_System_of_Record/Knowledge_Base"
WHERE type = "note"
SORT created DESC
LIMIT 15
```

## 👥 Recent meetings
```dataview
TABLE date, participants
FROM "00_System_of_Record/Meeting_Notes"
WHERE type = "meeting"
SORT date DESC
LIMIT 10
```
