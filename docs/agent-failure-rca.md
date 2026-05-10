# Agent Failure RCA

Use this when an agent made an error, a plan fixes agent behavior, or a proposed patch may be treating symptoms instead of root cause.

## Core question

Would a capable human, given the same prompt, context, tools, memory, source ledger, feedback, and authority boundaries, likely have made the same error?

- If yes, the system likely withheld or distorted information/capability. Fix the missing affordance.
- If no, capture the model-policy failure in an eval/replay and add the smallest harness guard that catches it.

## Simplicity bias

Do not start by adding another policy, prompt clause, router branch, reviewer, or guardrail. First ask whether the agent would have done the right thing with cleaner context, a more obvious tool, a stronger source-authority lane, an inspectable state transition, or faster feedback. Delete symptom patches that only compensate for missing affordances.

A durable RCA should prefer the lowest-layer simplification that prevents the class: remove a confusing state, collapse an unnecessary handoff, replace a vague tool with a typed one, or expose the decisive context directly. Add behavioral control machinery only when the missing affordance is not enough.

## Checklist

1. What did the agent actually see?
2. What tools, memory, source lanes, and handoff packet were available?
3. What feedback, error, or recovery signal did it receive?
4. What context or capability would a capable human normally have?
5. Which source of truth, authority boundary, or identity rule was missing or unclear?
6. What invariant should have prevented or caught the mistake?
7. What is the lowest-layer durable fix?
8. What test, replay, trace, or eval proves the failure class is covered?

## Common root causes

- missing, stale, excessive, or conflicting context
- unclear task or admission policy
- bad tool affordance or vague tool description
- misleading, lossy, or unstructured tool output
- conflicting source authority or identity resolution
- missing memory/context retrieval or bad compaction
- weak feedback loop, observation, or recovery path
- subagent handoff or ownership ambiguity
- prompt/tool/state mismatch
- missing deterministic guard, eval, or replay
- bad incentives, stop condition, budget/backpressure, or escalation policy

## Anti-pattern

Do not patch only the visible symptom. If the RCA cannot name the missing invariant, affordance, or feedback loop, label the change a mitigation and do not treat it as a durable fix. Do not keep mitigations after the lower-layer simplification makes them unnecessary.
