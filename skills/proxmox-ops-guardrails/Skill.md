Name: proxmox-ops-guardrails
Description: Safely automate Proxmox VE tasks such as VM and container inspection, backup, snapshot, permissions, and API-token workflows.

# Proxmox Ops Guardrails

## Use this skill for

- Proxmox VE automation, scripting, and operational runbooks
- VM, LXC, node, cluster, storage, and backup tasks
- API token setup, permission checks, and least-privilege access
- read-first inspection before any mutating action

## Default checks

1. Start read-only: inspect node, VMID, container ID, storage, and permissions first.
2. Use least-privileged API tokens with separated privileges unless the task truly needs more.
3. Verify token and role permissions before mutation.
4. Take a snapshot or backup before risky changes when the workflow supports it.
5. Confirm the exact target object before stop, delete, migrate, or restore operations.
6. Keep destructive operations explicit and one-target-at-a-time.
7. Prefer idempotent API or CLI calls over ad hoc shell sequences.

## Review workflow

For a Proxmox change:

1. Identify whether the task is read-only, reversible, or destructive.
2. Confirm the target node, VMID, or CTID.
3. Check permissions and token scope.
4. Add backup/snapshot/rollback steps if data or uptime is at risk.
5. Keep the command sequence minimal and deterministic.

## Output style

When using this skill, keep the response short and concrete:

- state the target and risk
- point to the relevant Proxmox object or API path
- propose the smallest safe operation sequence
