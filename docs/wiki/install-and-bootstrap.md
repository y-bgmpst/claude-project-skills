# Install and Bootstrap

This repository is designed to be copied into `~/.claude/skills` on a new machine with a single command.

## Recommended install flow

```bash
./scripts/install_to_claude_home.sh
```

What it does:

- resolves the repository root
- chooses `${CLAUDE_HOME:-$HOME/.claude}/skills`
- copies each skill directory there
- refuses to overwrite an existing skill directory

## Bootstrap expectations

A new machine should end up with:

- the reusable skill pack installed locally
- the repo itself available as the source of truth
- the same layout used by Claude on that machine

## When to use manual install

Use manual install only if you need to copy a subset of skills.

Example:

```bash
./scripts/install_to_claude_home.sh skills/rust-security-guardrails skills/crusty-sort-guardrails
```

## Failure behavior

The installer intentionally fails fast if:

- the destination skill already exists
- the source path is not a directory
- the shell is missing required permissions

This is deliberate. The install path should not silently merge or replace skill definitions.
