# Claude Project Skills Wiki

This wiki documents how the repository is structured, how skills are maintained, how validation works, and how to ship changes safely.

## Quick navigation

- [Architecture](architecture.md)
- [Skill lifecycle](skills-lifecycle.md)
- [Install and bootstrap](install-and-bootstrap.md)
- [Validation and CI](validation-and-ci.md)
- [Security and trust model](security-and-trust-model.md)
- [Release and versioning](release-and-versioning.md)
- [Contributing](contributing.md)

## Purpose

This repository is the source of truth for reusable Claude skills that can be installed into `~/.claude/skills` on any machine.

The repository deliberately keeps the runtime surface small:

- skill metadata lives in `skills/<skill-name>/Skill.md`
- repeatable operations live in `scripts/`
- human-facing docs live in `docs/wiki/`

## Current skills

- `rust-security-guardrails`
- `crusty-sort-guardrails`
- `crusty-dlp-guardrails`

## Reading order

If you are new to the repo, read in this order:

1. `architecture.md`
2. `skills-lifecycle.md`
3. `install-and-bootstrap.md`
4. `validation-and-ci.md`
5. `security-and-trust-model.md`
6. `release-and-versioning.md`
7. `contributing.md`
