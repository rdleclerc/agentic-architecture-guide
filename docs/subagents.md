# Subagents

Use subagents for isolation, specialization, or context control. Do not add multiple agents just to imitate an org chart.

Add a subagent when at least one is true:

- It needs different tools.
- It needs different instructions.
- It needs separate memory scope.
- It needs a separate context window.
- It benefits from parallel exploration.
- The main agent should stay in control while delegating bounded work.
- Human approval or compliance policy differs by role.

Every subagent needs:

- name
- purpose
- allowed tools
- forbidden tools
- memory scope
- context policy
- return contract
- eval cases

## Subagents Versus Independent Coding Agents

A subagent is part of one run and returns to a parent controller. Independent coding agents or sessions require a separate coordination protocol: one integrator, contributor proposals, file ownership, and one final verification owner.

Do not let multiple agents mutate the same source-of-truth files, runtime config, or generated artifacts without an explicit ownership plan.
