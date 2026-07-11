# Claude Project Skills

Reusable Claude skills adapted from the Codex skill pack.

## Skills

- `rust-security-guardrails`
- `crusty-sort-guardrails`
- `crusty-dlp-guardrails`
- `email-draft-polish`
- `meeting-notes-and-actions`
- `spreadsheet-formula-helper`
- `file-organizer`
- `bootstrap-router`

## Layout

Each skill lives under `skills/<skill-name>/` and contains:

- `Skill.md`
- optional supporting files when needed

## Token-lean routing

Start with `skills/bootstrap-router/Skill.md`, then load only the matching file from `docs/context-groups/`.

## Wiki

Start here: [docs/wiki/README.md](docs/wiki/README.md)

## Release drafts

- [v0.1.0 draft](docs/releases/0.1.0-draft.md)

## Install on a new machine

```bash
./scripts/install_to_claude_home.sh
```

The script copies the skill directories into `~/.claude/skills` unless `CLAUDE_HOME` is set.

## PR workflow

1. Create a branch.
2. Edit or add skill directories under `skills/`.
3. Run `python3 scripts/validate_skill_repo.py`.
4. Open a pull request to `main`.

GitHub Actions runs the same validation on pull requests and on pushes to `main`.
