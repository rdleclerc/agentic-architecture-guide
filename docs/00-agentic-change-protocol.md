# Agentic Change Protocol

Use this compact protocol before loading the larger reference docs. The goal is to make agentic changes safer without turning every task into a governance project.

## 1. Classify the change

Name the primary component you are changing: workflow, agent loop, multi-agent system, tool, skill, memory, source lane, identity, context, durable execution, guardrail, coordination, attention policy, adoption state, eval/observability, CLI/tool surface, repo seam, or feedback loop.

If more than one applies, pick one primary component and list the secondary ones. Do not expand scope just because many categories are adjacent.

## 2. Basic Spine First for product/rewrite/agentic-system work

This is a brake, not more machinery. Before adding architecture, abstractions, agents, contracts, routers, monitors, or eval frameworks for product/rewrite/agentic-system work, state the minimum user-visible product spine and its proof:

- **Minimum spine:** the shortest real user/input-to-result path that must work.
- **Canonical proof:** the single command, acceptance test, or live-safe check that proves that spine.
- **Current result:** `pass`, `fail`, or `not available`.
- **If fail/not available:** the task may only fix/create that spine check, or explicitly label itself a non-readiness spike.
- **Brake:** core spine gaps are blockers, not named residual risks, unless the user explicitly accepts the spike boundary.

For Type0, the default spine is: real feed/tip/wire input → normalized signal → admission decision → lane/story assignment → story processing → fact-check/publish/reject guard → traceable result.

## 3. Run the deletion-first simplicity pass

Simplicity is a safety property for agentic systems. Every new part creates coordination cost, context cost, stale-state risk, eval surface area, ownership ambiguity, and future merge conflict risk. These costs are usually hidden until a later agent touches the system.

Before adding a new agent, schema, router, policy layer, eval harness, guardrail, workflow, dependency, or automation, answer in this order:

1. **Make the requirement less wrong.** Is the requirement stale, over-broad, based on a one-off incident, or asking for the wrong layer to own the behavior?
2. **Delete.** What step, part, handoff, queue, policy, file, prompt clause, or process can be removed instead of improved?
3. **Prefer affordance over coercion.** Could the agent behave correctly if it had better context, a clearer tool, source authority, feedback, or an inspectable state transition?
4. **Simplify.** Can the remaining design be expressed as a smaller contract, fewer states, fewer files, fewer roles, or a narrower public seam?
5. **Optimize or accelerate.** Only speed up the path after the simpler path is correct.
6. **Automate last.** Do not automate a workflow, policy, or workaround that should have been deleted.

A complexity addition is justified only when its expected benefit is much greater than its visible cost. “Slightly better than the cost we can see” is not enough because the hidden cost is usually the larger part.

## 4. If a guardrail remains, choose the smallest useful one

Prefer the smallest deterministic guardrail that prevents a named failure class.

Before adding a new agent, schema, router, eval harness, policy layer, or CI gate, answer:

- What failure does this prevent?
- Has that failure happened, or is it high-risk enough to justify the hidden cost?
- Why would better context, tools, source authority, feedback, or a smaller contract not prevent it?
- Is there a smaller check, template, test, or acceptance line that would prevent it?
- What maintenance burden and future coordination burden does the new machinery create?

If the benefit is not clearly larger than the hidden cost, write the simpler rule and defer the machinery until a real failure demands it.

## 5. Separate harness from policy

Deterministic harness owns schemas, permissions, idempotency, budgets, checkpoints, memory APIs, source authority, identity resolution, context assembly, tool execution, approval gates, traces, and evals.

Model policy owns ambiguity, context gathering, tool choice, memory retrieval, task decomposition, plan revision, recovery, and synthesis.

Do not bury harness responsibilities inside prompts. Do not replace adaptive behavior with brittle keywords unless the behavior is genuinely deterministic and tested.

## 6. Run Agent Failure RCA when relevant

If the change fixes an agent mistake, repeated agent error, multi-agent confusion, context/tool/memory issue, or symptom patch risk, load `docs/agent-failure-rca.md` and answer the human counterfactual before coding.

The default stance is: agents often fail because the system withheld context, tools, feedback, source clarity, or authority that a capable human would have had. Fix the missing affordance before adding behavior-policing machinery.

## 7. Define filesystem topology as an executable contract

For code changes, name the package/module destination before editing. If the repo has a topology, dependency-map, or import-boundary test, include it in the acceptance rubric. If a non-trivial change would add code in a root/convenience layer and no executable guard exists, add the smallest useful guard first. Prose-only hierarchy guidance is not a control.

## 8. Define done as evidence

Before implementation, write a small acceptance rubric:

- expected system behavior
- files/components in scope and out of scope
- user approval or side-effect boundaries
- commands/tests/evals/reviews to run, including repo topology/dependency gates when code files are added or moved
- deletion/simplification pass result
- manual proof vs autonomous/system proof gap
- rollback/adoption state when relevant

For small changes, a few bullets are enough. For contained Tier 1 coding work, the Coding Agent Work Contract can be the plan artifact. For larger or riskier work, use a dedicated plan only when it reduces risk more than it adds process, and extend the work contract rather than duplicating it.

## 9. Final acceptance

Before calling work done, try to disprove readiness:

- Did the implementation drift from the plan?
- Did it add complexity without preventing a named failure?
- Did it skip a simpler context/tool/source-authority fix?
- Did new/moved code respect the repo topology and run the executable topology/dependency guard?
- Are source/truth/memory/context/tool boundaries still clear?
- Are untested layers named honestly?
- If this fixes agent behavior, does the RCA identify the missing invariant or affordance?

Report known gaps explicitly instead of letting "tests pass" stand in for system proof.
