# Dataview Mastery

## Example Queries

### All tasks that are not done
```dataview
TABLE due, project
FROM "05_Personal_Productivity/Tasks"
WHERE status != "Done"
SORT due ASC
```

### Notes by domain
```dataview
TABLE created, topics
FROM "01_Atomic_Notes"
SORT created DESC
```
