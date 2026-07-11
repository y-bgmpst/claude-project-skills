Name: web-app-security-guardrails
Description: Review or implement web apps with a security-first posture, especially Next.js and other full-stack apps that use route handlers, server actions, forms, and auth.

# Web App Security Guardrails

## Use this skill for

- full-stack web app changes
- route handlers, server actions, forms, and auth checks
- input validation, output encoding, and session handling
- security reviews for client/server boundaries

## Default checks

1. Re-check authorization inside every server action and route handler.
2. Never rely on a page-level auth check to protect downstream mutations.
3. Validate and normalize untrusted input on the server.
4. Keep secrets server-side and avoid leaking internal headers or tokens.
5. Encode or escape data before rendering it back to users.
6. Treat requests, headers, and form payloads as hostile until verified.
7. Add tests for auth, validation, and dangerous edge cases.

## Next.js-specific reminders

- Re-verify auth inside Server Actions.
- Protect Route Handlers explicitly.
- Prefer framework-provided unauthorized/redirect flows where they fit.
- Keep internal headers and other framework plumbing out of app logic.

## Review workflow

For a web app change:

1. Identify the trust boundary.
2. Trace the request from UI to server mutation.
3. Check auth, validation, and data encoding at each hop.
4. Confirm no secret or internal-only detail leaks to the client.
5. Keep the smallest fix that closes the risk.

## Output style

When using this skill, keep the response short and concrete:

- state the risk
- point to the route, action, or component
- propose the smallest safe fix
