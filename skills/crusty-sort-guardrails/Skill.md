Name: crusty-sort-guardrails
Description: Make safe changes in crusty-sort, especially around schema migrations, scanning, hashing, duplicate detection, reconciliation, organizing files, and SQLite-backed metadata flows.

# crusty-sort Guardrails

## Use this skill for

- changes in the `crusty-sort` repo
- schema migrations and SQLite access
- filesystem scanning, hashing, and media probing
- duplicate grouping, similarity search, and review flows
- organizer operations, path sanitization, and rollback behavior

## Defaults

1. Keep user media safe by default.
2. Never delete or overwrite files unless the task explicitly requires it.
3. Serialize SQLite writes in one place.
4. Bound concurrency and queues.
5. Prefer incremental, reversible changes.
6. Add tests for new DB or filesystem behavior.

## Repository-specific checks

- Migrations must be sequential and idempotent.
- Scan jobs should not touch SQLite from worker threads.
- Stale-file reconciliation must not remove files outside the scanned root.
- Exact duplicate actions require a fresh byte-hash precondition immediately before mutation.
- Near-duplicate results are for review, not automatic replacement.

## Output style

When using this skill, keep the response compact:

- state the relevant risk or invariant
- point to the file or subsystem
- propose the smallest safe change
