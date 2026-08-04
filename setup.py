#!/usr/bin/env python3
"""
Local Second Brain - Setup Script
Creates the full folder structure for your Second Brain vault.
"""

import os
import sys
from pathlib import Path

FOLDERS = [
    # System of Record
    "00_System_of_Record/Databases",
    "00_System_of_Record/Meeting_Notes",
    "00_System_of_Record/Version_Control",
    "00_System_of_Record/Wiki",
    "00_System_of_Record/Projects",
    "00_System_of_Record/Docs",
    "00_System_of_Record/Tasks",
    "00_System_of_Record/Forms",
    "00_System_of_Record/Knowledge_Base/Atomic_Notes",
    "00_System_of_Record/Knowledge_Base/Library",

    # AI Agents
    "01_AI_Agents/Custom_Agents",
    "01_AI_Agents/Research_Agents",
    "01_AI_Agents/Meeting_Summarizers",
    "01_AI_Agents/Prompt_Library",

    # Developer Tools
    "02_Developer_Tools/Scripts",
    "02_Developer_Tools/Webhooks",
    "02_Developer_Tools/Sync_Tools",

    # Integrations
    "03_Integrations/Telegram",
    "03_Integrations/Twitter",
    "03_Integrations/Email",
    "03_Integrations/Calendar",
    "03_Integrations/Other",

    # Workflows
    "04_Workflows/CRM",
    "04_Workflows/Roadmaps",
    "04_Workflows/Content_Creation",
    "04_Workflows/Personal_Projects",

    # Personal Productivity
    "05_Personal_Productivity/Notes/Daily",
    "05_Personal_Productivity/Notes/Weekly",
    "05_Personal_Productivity/Goals",
    "05_Personal_Productivity/Habits",
    "05_Personal_Productivity/Reading",
    "05_Personal_Productivity/Travel",
    "05_Personal_Productivity/Health",
]

def create_structure(base_path: Path):
    print(f"Creating Local Second Brain structure in: {base_path}\n")

    for folder in FOLDERS:
        path = base_path / folder
        path.mkdir(parents=True, exist_ok=True)
        (path / ".gitkeep").touch(exist_ok=True)
        print(f"  ✓ {folder}")

    print("\n✅ Local Second Brain structure created successfully!")
    print("Open this folder as an Obsidian vault to begin.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = Path(sys.argv[1]).expanduser().resolve()
    else:
        target = Path.cwd() / "Local-Second-Brain"

    create_structure(target)