# Durable Execution for Agentic Systems

Long-running agents must survive interruption, retry, human review, and replay.

Checkpoint after meaningful steps. A checkpoint should include:

- task id
- thread/session id
- step number
- current plan
- compacted transcript or message state
- retrieved memory ids
- tool calls and results
- pending approvals
- artifacts
- budget usage
- side-effect ids
- trace ids

Replay must not duplicate side effects. External writes require idempotency keys. Nondeterministic operations and side-effecting tools should be wrapped so they can be resumed safely.

Stop conditions:

- final answer validated
- task completed
- missing required information
- human approval required
- budget exhausted
- repeated failure detected
- safety boundary reached

Durability is harness-owned, not model-owned.

## Durable Authority And Adoption

Checkpoint not only tool calls, but also source-authority decisions, identity merges, attention gates, approvals, and adoption-state changes.

Replay must not duplicate external side effects, re-promote a candidate claim, re-run a write-enabled sidecar without idempotency, or turn a shadow-mode result into production state. Adoption transitions should be explicit, logged, and reversible where possible.
