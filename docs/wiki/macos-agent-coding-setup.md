# macOS Agent Coding Setup

This guide gives a practical starting point for common agent-coding environments on macOS.

## Core rule

Use one repo bootstrap file (`claude.md` or `project.md`) plus one narrow context group. Do not keep large instructions in chat if they can live in versioned files.

## Recommended environments

### Claude

- open the repo
- read `claude.md`
- then read `docs/context-groups/index.md`
- load only the one matching context group

### VS Code

- keep the repo open in a workspace
- use the project bootstrap file as the first reference
- keep task-specific instructions in the repo, not in ad hoc chat notes
- when a change is token-sensitive, point the assistant at the smallest matching context file first

### Cursor

- start from `project.md`
- use the same context-group routing rule
- keep any reusable prompt fragments in the repo so they can be shared across sessions

### Zed

- prefer a repository-local bootstrap file and one context index
- keep long instructions in files that can be loaded on demand
- separate safety and release guidance from day-to-day task guidance

### Other agentic editors

The same pattern applies:

1. one tiny repo bootstrap file
2. one context index
3. one matching context block
4. no extra prompt baggage

## Token-saving habits

- read only one small file first
- use the repo wiki for longer explanations
- avoid copying the same workflow into multiple places
- split content by task, not by feature list

## Suggested baseline workflow

1. Open the repo.
2. Read `claude.md` or `project.md`.
3. Read `docs/context-groups/index.md`.
4. Select one matching group.
5. Make the change.
6. Validate.
7. Open a PR.
