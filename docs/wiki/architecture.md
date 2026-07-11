# Architecture

The repository is organized around a simple rule: the skill definition is the product.

## Top-level layout

- `skills/` — versioned skill packages
- `scripts/` — deterministic helpers for install and validation
- `.github/workflows/` — CI checks for pull requests and mainline pushes
- `.github/pull_request_template.md` — required PR checklist
- `docs/wiki/` — long-form documentation

## Skill package shape

Each skill is a self-contained directory:

```text
skills/<skill-name>/
└── Skill.md
```

Optional resources can be added later if they are genuinely needed, but the default posture should stay minimal.

## Data flow

1. A user or project selects a skill.
2. Claude reads `Skill.md` first.
3. If a task is repetitive or brittle, move the repeatable part into `scripts/`.
4. Validate the repo before opening a PR.

## Design goals

- token-lean skill definitions
- predictable install behavior
- easy PR review
- no hidden runtime dependencies
- no ambiguity about the source of truth

## What should stay out of the repo

- ad hoc one-off notes
- duplicate instructions copied into many skills
- large generated artifacts
- non-deterministic helper logic unless it is clearly justified
