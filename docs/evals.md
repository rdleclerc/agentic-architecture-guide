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
