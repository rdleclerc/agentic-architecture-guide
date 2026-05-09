# Evals for Agentic Systems

Agentic evals test behavior, not only syntax.

Evaluate:

- tool choice
- memory retrieval
- memory write quality
- context compaction
- skill use
- human approval gates
- side-effect safety
- failure recovery
- stop conditions
- final answer quality and evidence

Use positive and negative cases. A negative case proves the agent does not call a risky tool, does not use stale memory, does not bypass approval, or does not fall back to keyword routing.

When a real incident exists, make it the fixture. Sanitize logs or traces if needed, but preserve the causal shape: inputs, context, tool calls, state, side effects, failures, and expected recovery. Synthetic cases are useful after the incident replay exists; they should not replace it.

For prompt, skill, workflow, or agent-behavior changes intended to alter live behavior, require a live-safe end-to-end run, replay, shadow run, or forensics-backed verification. If not run, mark the layer as a known gap rather than calling the change done.

A useful eval trace captures:

- context items included
- tool summaries shown
- skill summaries shown
- memory ids retrieved
- action chosen
- tool args
- tool result
- state diff
- approval status
- checkpoint id
- evaluator result

## Operating-System Evals

Add evals for source conflict handling, stale evidence, identity resolution, bad merge prevention, synthesis-not-truth boundaries, noisy-lane promotion, attention-budget behavior, adoption-state promotion, backpressure behavior, paid-fallback denial, claim/state reconciliation, and manual-proof-vs-autonomous-proof acceptance.

A good eval asks whether the system chose the right authority and posture, not only whether it called the right tool.

## Pattern and Coding-Agent Evals

Add eval cases for the agentic patterns that commonly regress in coding-agent work:

- **Routing evals:** ambiguous user goals should choose the right semantic route, record confidence/reason, and use a safe default when uncertain; negative cases should reject keyword-only routing.
- **Fallback evals:** provider/tool fallback should be denied unless explicitly budgeted, approved, attributed, traceable, and replay-safe.
- **CLI affordance evals:** agent-facing CLIs should run headlessly, emit JSON, bound output, expose dry-run/idempotency, return actionable errors, and support introspection.
- **Parallel-slice evals:** multi-agent coding work should have disjoint write sets, small contract-shaped files, per-slice tests, and integrator-owned shared contracts.
- **Reflection evals:** self-critique should find harness/policy boundary violations, but readiness must depend on external tests/evals/traces rather than self-judgment.
- **Learning-loop evals:** production feedback should become trace labels, fixtures, rules, or review queues before it changes prompts, memory, routing, or tool policy.
