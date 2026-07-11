# Project Bootstrap

This file is the generic starting point for a new repo.

## Minimal workflow

1. Read `claude.md`.
2. Read `docs/context-groups/index.md`.
3. Pick one narrow context group.
4. Make the smallest useful change.
5. Validate before merging.

## Repo conventions

- keep docs token-lean
- keep mutation paths explicit
- keep helper scripts deterministic
- prefer versioned files over chat memory

## When to expand context

Only load another file when the first one does not fully answer the task.
