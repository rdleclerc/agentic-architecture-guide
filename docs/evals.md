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
- deletion/simplification discipline before adding machinery

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

- **Simplicity/deletion evals:** when a plan proposes new guardrails, routers, subagents, workflows, queues, schemas, dependencies, or automation, the agent should first identify deletion candidates and context/tool/source-affordance alternatives; negative cases should reject machinery whose benefit is only marginally larger than visible cost.
- **Routing evals:** ambiguous user goals should choose the right semantic route, record confidence/reason, and use a safe default when uncertain; negative cases should reject keyword-only routing.
- **Fallback evals:** provider/tool fallback should be denied unless explicitly budgeted, approved, attributed, traceable, and replay-safe.
- **CLI affordance evals:** agent-facing CLIs should run headlessly, emit JSON, bound output, expose dry-run/idempotency, return actionable errors, and support introspection.
- **Parallel-slice evals:** multi-agent coding work should have disjoint write sets, small contract-shaped files, per-slice tests, and integrator-owned shared contracts.
- **Reflection evals:** self-critique should find harness/policy boundary violations, but readiness must depend on external tests/evals/traces rather than self-judgment.
- **Learning-loop evals:** production feedback should become trace labels, fixtures, rules, or review queues before it changes prompts, memory, routing, or tool policy.

## Lightweight package validation

The guide should dogfood this doctrine with a small executable harness, not a ceremonial framework. Use the deterministic validator whenever the package, docs, bundle, skills, or eval matrix changes:

```bash
python3 scripts/validate_agentic_pack.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

The validator checks source-authority/package integrity:

- referenced guide docs exist;
- bundled payload metadata is valid;
- bundled payloads match live files when the live file exists;
- bundled docs are materialized as live docs rather than hidden only in the single-file artifact;
- skill registry paths resolve;
- eval cases have required fields and behavior-category coverage;
- behavior fixtures exist for simplicity/deletion, CLI affordance, parallel slicing, source-authority conflict, and side-effect approval.

Non-theatre standard: do not silence validator failures to make the run green. If a failure is expected during a multi-agent pass, record the exact failing contract and the owner who must close it. The default ready-for-merge state is that this command passes, or that the final integrator explicitly accepts the named residual gap.
