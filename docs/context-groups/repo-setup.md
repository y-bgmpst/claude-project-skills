# Repo Setup

Use this group for repo layout, installation, validation, and PR workflow.

## Layout

- `skills/` holds one folder per skill
- `scripts/` holds deterministic helpers
- `docs/wiki/` holds longer documentation
- `docs/context-groups/` holds small routing files

## Local install

```bash
./scripts/install_to_claude_home.sh
```

That copies skills into `~/.claude/skills` unless `CLAUDE_HOME` is set.

## Validation

```bash
python3 scripts/validate_skill_repo.py
```

## PR flow

1. make a focused branch
2. update the touched skill files
3. run validation
4. open a PR to `main`
