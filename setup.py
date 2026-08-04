#!/usr/bin/env python3
"""
Local Second Brain - Free Local Alternative to Notion
Setup script - creates the full local workspace structure
"""

import sys
from pathlib import Path

FOLDERS = [
    "00_System_of_Record/Databases",
    "00_System_of_Record/Meeting_Notes",
    "00_System_of_Record/Version_Control",
    "00_System_of_Record/Wiki",
    "00_System_of_Record/Projects",
    "00_System_of_Record/Docs",
    "00_System_of_Record/Tasks",
    "00_System_of_Record/Forms",
    "00_System_of_Record/Knowledge_Base",
    "01_AI/Custom_Agents",
    "01_AI/External_Agents",
    "01_AI/Enterprise_Search",
    "01_AI/AI_Meeting_Notes",
    "01_AI/Deep_Research",
    "01_AI/Autofill",
    "01_AI/AI_Connectors",
    "01_AI/Mobile_Agents",
    "02_Developer_Platform/CLI_Tools",
    "02_Developer_Platform/Webhooks",
    "02_Developer_Platform/Syncs",
    "02_Developer_Platform/Agent_Tools",
    "02_Developer_Platform/Developer_Portal",
    "03_Connected_Workspace",
    "04_Business_Workflows",
    "05_Personal_Productivity/Personal_OS",
    "05_Personal_Productivity/Notes",
    "05_Personal_Productivity/Tasks",
    "05_Personal_Productivity/Goals",
    "05_Personal_Productivity/Reading_Lists",
    "05_Personal_Productivity/Travel_Planning",
    "05_Personal_Productivity/Habit_Tracking",
    "05_Personal_Productivity/Side_Projects",
    "05_Personal_Productivity/Life_Admin",
    "dashboard",
    "docs",
    "templates",
]

def create_structure(base_path: Path):
    print(f"Creating Local Second Brain structure in: {base_path}\n")
    for folder in FOLDERS:
        path = base_path / folder
        path.mkdir(parents=True, exist_ok=True)
        (path / ".gitkeep").touch(exist_ok=True)
        print(f"  ✓ {folder}")
    print("\n✅ Local Second Brain structure created successfully!")

if __name__ == "__main__":
    target = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path.cwd() / "Local-Second-Brain"
    create_structure(target)
