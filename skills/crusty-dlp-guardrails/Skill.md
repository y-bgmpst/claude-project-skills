Name: crusty-dlp-guardrails
Description: Make safe, token-lean changes in crusty-dlp / yt-dlp tui around downloads, bridge routing, context groups, and file safety.

# crusty-dlp Guardrails

## Use this skill for

- changes in the `crusty-dlp` repo
- yt-dlp tui workflows and local-first media handling
- bridge routing, Claude/Codex coordination, and token-saving context
- download/extraction paths, metadata handling, and path sanitization
- tests around regressions, parsing, and safe file operations

## Defaults

1. Prefer local-first workflows.
2. Never overwrite or delete media without an explicit apply step.
3. Keep bridge/tooling optional; CLI workflows must still work.
4. Bound downloads, parsing, and file scans.
5. Sanitize every path derived from remote metadata.
6. Add tests for parsing, extraction, and file safety.

## Repository-specific checks

- Bridge helpers should degrade cleanly when no live bridge is available.
- Context groups should stay token-lean and repo-scoped.
- Download/output paths must be validated before use.
- Any mutating action should support a dry run or equivalent preview.
- Prefer deterministic, inspectable transforms over implicit behavior.

## Output style

When using this skill, keep the response compact:

- state the risk or invariant
- point to the relevant command or file
- propose the smallest safe change
