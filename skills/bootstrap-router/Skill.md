Name: bootstrap-router
Description: Route Claude work to the smallest relevant context group in this repo, so prompts stay token-lean and only the needed instructions are loaded.

# Bootstrap Router

Use this skill first when working in the Claude Project Skills repo or when you need to choose the smallest useful context block before editing or summarizing.

## Default order

1. Read `docs/context-groups/README.md`.
2. Pick exactly one matching context group.
3. Load a second group only if the task clearly spans two areas.
4. Keep the final answer short and grounded in the selected files.

## Routing rules

- Repo structure, install, validation, PRs -> `repo-setup.md`
- Adding or editing skills -> `skill-authoring.md`
- Safety, overwrites, trust model -> `safety.md`
- Releases, tags, drafts -> `release.md`
- Common task suggestions for end users -> `common-tasks.md`

## Output style

When using this skill, answer with:

- the chosen context group
- the smallest relevant next step
- any missing file if the repo does not yet contain the needed context
