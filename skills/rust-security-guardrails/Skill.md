Name: rust-security-guardrails
Description: Review or implement Rust code that touches filesystem paths, process execution, SQLite, concurrency, serialization, or unsafe code, and keep the change safe by default.

# Rust Security Guardrails

## Use this skill for

- Rust code that reads, writes, deletes, or renames files
- database code, especially SQLite
- spawned processes, shells, or external tools
- concurrency, channels, threads, locks, shared state
- serialization/deserialization, JSONL, config, and path handling
- any `unsafe` block or FFI boundary

## Default checks

1. Prefer safe Rust over `unsafe`.
2. Keep mutations explicit, small, and reversible where possible.
3. Never assume paths are trusted; canonicalize or sanitize before use.
4. Treat deserialization as untrusted input.
5. Serialize DB writes through one owner thread or transaction path.
6. Bound queues, thread counts, and file reads.
7. Preserve user data unless the task explicitly requires a destructive action.

## Review workflow

For a security-sensitive Rust change:

1. Identify the trust boundary and attacker-controlled inputs.
2. Trace where data enters the filesystem, DB, network, or process boundary.
3. Check for panics, unwraps, unchecked indexing, and overflow assumptions.
4. Check for TOCTOU risks between validation and mutation.
5. Check for partial-failure cleanup and rollback behavior.
6. Confirm the code remains deterministic under concurrency.

## High-risk patterns

- `unwrap()` / `expect()` on external input paths
- unbounded channels, recursion, or file collection
- `Command::new(...)` with shell interpolation
- `unsafe` without a narrow safety comment and local proof
- deleting or overwriting files before a fresh precondition check
- concurrent writes to the same SQLite connection

## Output style

When using this skill, keep the response short and concrete:

- state the risk
- point to the exact code path
- propose the smallest safe fix
