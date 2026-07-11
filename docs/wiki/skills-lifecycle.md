# Skill Lifecycle

This section describes the full lifecycle of a skill in this repository.

## 1. Design the skill

Start from one concrete use case.

Ask:

- What should trigger the skill?
- What is the exact job to be done?
- What belongs in the skill body versus a script?
- What is the smallest useful surface?

A good skill is narrow enough to trigger reliably and broad enough to be reused.

## 2. Author `Skill.md`

`Skill.md` is the actual behavior contract.

It should answer:

- when to use the skill
- what default checks matter
- what workflow to follow
- what failure modes to watch for
- how concise the final response should be

If the skill grows too large, move detail into a reference file instead of bloating the main skill body.

## 3. Validate

Before merging changes:

- run the repo validator
- check that skill names and metadata match
- verify the install helper still copies the right directories

## 4. Install locally

The local install flow is intentionally simple:

- copy the skill directory into `~/.claude/skills`
- avoid overwriting an existing directory
- keep the copy layout identical to the repo layout

## 5. Review and merge

All changes should go through PRs to `main`.

Use the PR template to capture:

- summary
- touched skills
- validation
- notes or follow-up work

## Updating an existing skill

When changing an existing skill:

1. keep the name stable unless you explicitly want a new skill
2. update the skill body with the Claude-specific wording
3. run validation
4. confirm the install helper still behaves correctly
