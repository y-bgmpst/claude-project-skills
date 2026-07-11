Name: kubernetes-docker-ops-guardrails
Description: Safely handle Kubernetes and Docker tasks with read-first inspection, least-privilege RBAC, pinned images, and non-root container defaults.

# Kubernetes and Docker Ops Guardrails

## Use this skill for

- kubectl, manifests, namespaces, RBAC, rollouts, or cluster access
- Dockerfiles, images, Compose, builds, runtime hardening, or container debugging
- tasks that can mutate workloads, pods, deployments, volumes, or registry assets

## Default checks

1. Start read-only: confirm cluster, context, namespace, image, tag, and target object.
2. Prefer namespace-scoped Roles and RoleBindings over cluster-wide access unless cluster scope is required.
3. Keep kubectl mutations explicit: use apply, rollout status, and dry-run before live changes when possible.
4. Never delete, restart, scale, or replace workloads without an exact target and a rollback path.
5. For Docker, pin base images by version or digest; avoid latest.
6. Prefer multi-stage builds, minimal images, and non-root users.
7. Avoid privileged containers and broad host mounts unless the task clearly needs them.
8. Verify after mutation with the smallest check that proves success.

## Review workflow

For a container change:

1. Identify the target workload, image, or file.
2. Check the current context, namespace, or build stage.
3. Narrow permissions and inputs before mutating anything.
4. Apply the smallest change that fits the task.
5. Verify rollout, container health, or image output immediately after.

## Output style

When using this skill, keep the response short and concrete:

- state the target and risk
- name the exact namespace, deployment, image, or Dockerfile
- propose the smallest safe sequence
