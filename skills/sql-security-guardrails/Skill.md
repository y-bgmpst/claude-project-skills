Name: sql-security-guardrails
Description: Review or implement SQL work with a security-first posture: parameterized queries, least privilege, safe migrations, and transaction-aware data changes.

# SQL Security Guardrails

## Use this skill for

- SQL queries, ORM query builders, and database migrations
- schema changes, rollbacks, and seed data
- SQL used in web apps, scripts, or automation
- security reviews for database access patterns

## Default checks

1. Use prepared statements or bound parameters for every user-controlled value.
2. Never build SQL by string concatenation.
3. Keep database credentials and roles least-privileged.
4. Wrap related writes in a transaction; use savepoints when partial rollback matters.
5. Enable and verify foreign-key enforcement and other safety toggles required by the engine.
6. Sanitize logs and avoid printing secrets, full connection strings, or raw tokens.
7. Treat migrations as sequential, idempotent, and reversible where possible.

## Review workflow

For a SQL-sensitive change:

1. Identify the database engine and trust boundary.
2. Trace every query that touches user input.
3. Confirm parameter binding is used end-to-end.
4. Check transaction boundaries, rollback behavior, and migration ordering.
5. Check permissions, role scope, and connection handling.
6. Keep the fix minimal and engine-appropriate.

## Output style

When using this skill, keep the response short and concrete:

- state the risk
- point to the exact query or migration path
- propose the smallest safe fix
