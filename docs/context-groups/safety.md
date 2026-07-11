# Safety

Use this group when the task could mutate local files, overwrite work, or broaden tool access.

## Defaults

- refuse silent overwrites
- fail fast on ambiguous paths
- keep installation explicit
- keep helpers deterministic
- prefer reviewable changes over hidden automation

## Checklist

- Is the target path exact?
- Can the change be reversed?
- Does the script avoid overwriting existing files?
- Does the repo still make it obvious what changed?

## Practical rule

If the task needs more than one risky step, stop and ask or split the work into smaller operations.
