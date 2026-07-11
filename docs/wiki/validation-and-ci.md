# Validation and CI

Validation is intentionally lightweight so that the repo stays easy to maintain.

## Local validation

Run:

```bash
python3 scripts/validate_skill_repo.py
```

The validator checks that each skill has:

- `Skill.md`
- matching skill names
- a non-empty description header

## CI validation

GitHub Actions runs the same check on:

- pull requests
- pushes to `main`

This gives two benefits:

- broken metadata is caught before merge
- changes stay safe to install across machines

## Validation philosophy

Validation should prove the repository is structurally correct, not exhaustively prove every skill is behaviorally perfect.

Behavior should be small, reviewable, and easy to inspect in a PR.

## What CI does not do

CI does not:

- install the skills into a real home directory
- run interactive Claude flows
- verify every possible downstream usage

Those are better handled by review, explicit testing, or follow-up automation if needed.
