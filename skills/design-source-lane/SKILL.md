---
name: design-source-lane
description: Use when adding or reviewing a source lane, source-authority rule, identity-resolution path, noisy-lane promotion policy, sidecar adoption state, or synthesis boundary.
---

# Design Source Lane

## Procedure

1. Identify the artifact role: raw source, structured truth, retrieval index, recall memory, synthesis artifact, candidate signal, sidecar, or outbound artifact.
2. Define raw capture and idempotency.
3. Define identity resolution: aliases, external IDs, merge evidence, and unmerge path.
4. Define claim categories and source authority by category.
5. Define freshness, staleness, and contradiction behavior.
6. Define promotion rules and review queues.
7. Define health checks and trace fields.
8. Define synthesis behavior without making synthesis authoritative by default.
9. Define attention behavior: silent, internal record, review queue, ask, notify, interrupt, or approval.
10. Add evals for conflict, stale evidence, bad identity merge, noisy-lane promotion, and accidental sidecar promotion.

## Output

Return a source-lane contract, affected artifact roles, identity policy, authority matrix, adoption state, attention policy, and eval cases.
