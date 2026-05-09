# Agentic Change Protocol

Use this compact protocol before loading the larger reference docs. The goal is to make agentic changes safer without turning every task into a governance project.

## 1. Classify the change

Name the primary component you are changing: workflow, agent loop, multi-agent system, tool, skill, memory, source lane, identity, context, durable execution, guardrail, coordination, attention policy, adoption state, eval/observability, CLI/tool surface, repo seam, or feedback loop.

If more than one applies, pick one primary component and list the secondary ones. Do not expand scope just because many categories are adjacent.

## 2. Choose the smallest useful guardrail

Prefer the smallest deterministic guardrail that prevents a known or plausible failure class.

Before adding a new agent, schema, router, eval harness, policy layer, or CI gate, answer:

- What failure does this prevent?
- Has that failure happened, or is it high-risk enough to justify the cost?
- Is there a smaller check, template, test, or acceptance line that would prevent it?
- What maintenance burden does the new machinery create?

If the benefit is not clear, write the simpler rule and defer the machinery until a real failure demands it.

## 3. Separate harness from policy

Deterministic harness owns schemas, permissions, idempotency, budgets, checkpoints, memory APIs, source authority, identity resolution, context assembly, tool execution, approval gates, traces, and evals.

Model policy owns ambiguity, context gathering, tool choice, memory retrieval, task decomposition, plan revision, recovery, and synthesis.

Do not bury harness responsibilities inside prompts. Do not replace adaptive behavior with brittle keywords unless the behavior is genuinely deterministic and tested.

## 4. Run Agent Failure RCA when relevant

If the change fixes an agent mistake, repeated agent error, multi-agent confusion, context/tool/memory issue, or symptom patch risk, load `docs/agent-failure-rca.md` and answer the human counterfactual before coding.

The default stance is: agents often fail because the system withheld context, tools, feedback, source clarity, or authority that a capable human would have had.

## 5. Define done as evidence

Before implementation, write a small acceptance rubric:

- expected system behavior
- files/components in scope and out of scope
- user approval or side-effect boundaries
- commands/tests/evals/reviews to run
- manual proof vs autonomous/system proof gap
- rollback/adoption state when relevant

For small changes, a few bullets are enough. For larger changes, use a dedicated plan only when it reduces risk more than it adds process.

## 6. Final acceptance

Before calling work done, try to disprove readiness:

- Did the implementation drift from the plan?
- Did it add complexity without preventing a named failure?
- Are source/truth/memory/context/tool boundaries still clear?
- Are untested layers named honestly?
- If this fixes agent behavior, does the RCA identify the missing invariant or affordance?

Report known gaps explicitly instead of letting "tests pass" stand in for system proof.
