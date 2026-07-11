# Contributing

This repo is designed for low-friction, high-clarity changes.

## Contribution rules

- keep each PR focused on a single theme
- update `Skill.md` and any helper files together
- run validation before opening a PR
- describe any install or workflow impact in the PR body
- prefer small, reviewable diffs

## Suggested PR structure

Use this shape:

- summary
- skills touched
- validation
- notes

That matches the repository template and makes review faster.

## Good change types

- add a new skill
- tighten a skill description
- split a broad skill into two smaller ones
- improve install or validation tooling
- improve documentation

## Avoid

- mixing unrelated skill changes in one PR
- adding large generated content without a reason
- silently changing skill names
- introducing a helper that overwrites local directories

## If you are adding a new skill

Before merging, confirm:

- the skill name is short and stable
- the description is specific enough to trigger correctly
- the skill body mentions the right workflows and boundaries
- the repository wiki describes where it fits
