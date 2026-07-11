Name: file-organizer
Description: Intelligently organize files and folders by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks; use when a user wants to tame a messy Downloads/Documents tree or clean up project folders.

# File Organizer

This skill acts as your personal organization assistant, helping you maintain a clean, logical file structure across your computer without the mental overhead of constant manual organization.

## When to Use This Skill

- Your Downloads folder is a chaotic mess
- You can't find files because they're scattered everywhere
- You have duplicate files taking up space
- Your folder structure doesn't make sense anymore
- You want to establish better organization habits
- You're starting a new project and need a good structure
- You're cleaning up before archiving old projects

## What This Skill Does

1. **Analyzes Current Structure**: Reviews your folders and files to understand what you have
2. **Finds Duplicates**: Identifies duplicate files across your system
3. **Suggests Organization**: Proposes logical folder structures based on your content
4. **Automates Cleanup**: Moves, renames, and organizes files with your approval
5. **Maintains Context**: Makes smart decisions based on file types, dates, and content
6. **Reduces Clutter**: Identifies old files you probably don't need anymore

## How to Use

### From Your Home Directory

```bash
cd ~
```

Then run Claude and ask for help:

```text
Help me organize my Downloads folder
```

```text
Find duplicate files in my Documents folder
```

```text
Review my project directories and suggest improvements
```

## Instructions

When a user requests file organization help:

1. **Understand the Scope**
   - Which directory needs organization?
   - What's the main problem?
   - Any files or folders to avoid?
   - How aggressively to organize?

2. **Analyze Current State**
   - review the target directory
   - summarize file types, size distribution, and obvious issues

3. **Identify Organization Patterns**
   - group by type, purpose, or date

4. **Find Duplicates**
   - show all paths
   - display sizes and modification dates
   - always ask for confirmation before deleting

5. **Propose Organization Plan**
   - present a clear plan before making changes
   - list folders to create, files to move, files needing decisions

6. **Execute Organization**
   - after approval, organize systematically
   - always confirm before deleting anything
   - log all moves for potential undo
   - preserve original modification dates
   - handle filename conflicts gracefully

7. **Provide Summary and Maintenance Tips**
   - summarize what changed
   - suggest a simple maintenance routine
