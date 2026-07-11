# Security and Trust Model

This repository distributes executable guidance. The main risks are not classic application vulnerabilities; they are incorrect instructions, stale metadata, and unsafe helper behavior.

## Trust boundaries

- The skill text is trusted by Claude after it is selected.
- Helper scripts are trusted to modify the local machine only in the narrow way they describe.
- CI is trusted to prevent obvious structural mistakes from reaching `main`.

## Security goals

- avoid overwriting existing local skills
- keep helpers deterministic
- avoid hidden network behavior in install or validation flows
- make metadata changes reviewable in PRs
- keep permissions narrow and explicit

## Threats to watch

### 1. Skill drift

A `Skill.md` file can drift away from the rest of the repo documentation.

Mitigation:

- keep a validator in the repo
- review the skill and its surrounding docs together

### 2. Unsafe installers

An install script can accidentally overwrite local work.

Mitigation:

- fail if the target already exists
- keep copying explicit
- avoid clever merge logic

### 3. Implicit scope creep

A skill can become too broad and start triggering in unrelated contexts.

Mitigation:

- keep descriptions narrow
- keep skill bodies short
- split unrelated behaviors into separate skills

### 4. Hidden mutation

A skill or helper can make changes that are not obvious from the repo layout.

Mitigation:

- prefer visible scripts and explicit paths
- document all mutation entry points in this wiki

## Safe change checklist

Before merging a change that affects installation or skill behavior:

- confirm the destination path is correct
- confirm no existing skill directory will be overwritten
- confirm the repo validator still passes
- confirm the PR description names every touched skill
