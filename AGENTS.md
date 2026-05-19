# AGENTS.md

This repository builds agentic operating systems. Read this whole file (it is short). For deeper detail, load only the doc(s) relevant to the task you are about to do — do not load everything by default.

For any non-trivial guide/code/prompt/tool/workflow change, load `docs/00-agentic-change-protocol.md` first. It is the compact working protocol; the larger docs are references, not default context dumps.

For any non-trivial coding task, first assemble or fill the Coding Agent Work Contract in `docs/coding-agent-work-contract.md` (template: `.agentic/coding_agent_work_contract_template.md`) unless the task is tiny and deterministic.

Source authority rule: the live multifile repo is canonical. `agentic_architecture_singlefile.md` is a generated distribution/recovery artifact and must not contain unique live doctrine. If bundle content is useful, materialize it as a live file or mark it archival/non-authoritative.

## Topic → file routing (lazy load)

Read the matching doc only when the listed task applies:

| If you are working on… | Load |
|---|---|
| Any non-trivial agentic-system change | `docs/00-agentic-change-protocol.md` |
| Non-trivial coding task / coding-agent work contract | `docs/coding-agent-work-contract.md` and `.agentic/coding_agent_work_contract_template.md` |
| Starting under tight context or needing a rule-only refresher | `docs/QUICK_REFERENCE.md` |
| Current guide version, canonicality, adapter status, or rollout state | `docs/version-and-adoption.md` |
| Agent errors, repeated mistakes, symptom patches, poor context/tools/feedback | `docs/agent-failure-rca.md` |
| Coding agents that build agent systems, when the compact protocol is insufficient | `docs/agentic-coding-for-agentic-systems.md` |
| End-to-end systems engineering for agents, when the compact protocol is insufficient | `docs/agentic-systems-engineering.md` |
| Choosing agentic patterns, agent-native CLIs, small-file repo shape, feedback loops | `docs/agentic-pattern-catalog.md` |
| Modularity, seams, file splitting, or parallel coding structure | `docs/modularity-and-seams.md` |
| Reflection, planning loops, or post-change critique | `docs/reflection-and-planning.md` |
| Retry/fallback/degraded-mode classification | `docs/exception-taxonomy.md` |
| Agent-to-agent message contracts | `docs/a2a-contracts.md` |
| Provider/model routing, spend, or fallback | `docs/cost-aware-routing.md` |
| Learning loops, feedback, skill evolution, or lesson promotion | `docs/learning-loops.md` |
| Queues, priority, preemption, or staleness | `docs/task-prioritization.md` |
| Source lanes, truth vs. retrieval/sidecars, candidate signals | `docs/source-authority-and-truth-lanes.md` |
| Multi-agent coordination, owner/integrator pattern, shared edits | `docs/cross-agent-operating-model.md` |
| Tools, tool registries, tool design, typed enforcement | `docs/tool-design.md` |
| Memory architecture, durability, retrieval boundaries | `docs/memory-architecture.md` |
| Context engines, context assembly, context budgets | `docs/context-engineering.md` |
| Durable execution, checkpoints, resumability | `docs/durable-execution.md` |
| Evals, observability, regression coverage | `docs/evals.md` |
| Skills, neutral packaging, or runtime adapters | `docs/skills.md` |
| Subagents and delegation | `docs/subagents.md` |

Do **not** load `agentic_architecture_singlefile.md` — it is a compiled human reference and will eat the context window.

Core rule: deterministic harness, adaptive policy.

High-agent-affordance default: architect OpenClaw, Type0, Gaia/Gaia Brain, Soho House, and shared agentic-media work so capable agents can inspect sources, use clear tools, apply concise skills, and exercise judgment. Before adding hard gates, hidden automation, routing layers, reviewer loops, or deterministic substitutes for judgment, first ask whether a better skill, typed tool, source lane, context packet, or feedback loop would preserve more agency with less machinery. If a coding agent chooses a lower-affordance design, it must explain why and get explicit approval.

Skill/tool creation rule: use `skills/openclaw-skill-creator` when creating or improving OpenClaw-targeted skills. Use `uber-skill-creator` for general portable SKILL.md skills when it is installed; otherwise use the current runtime's general skill creator. Use `skills/design-agent-tool` before implementing or reviewing OpenClaw tools, MCP tools, function-calling schemas, agent-facing CLIs/scripts, source readers, memory APIs, write/publish actions, or tool-like workflow commands.

Second rule: simplicity/deletion before machinery. Complexity has hidden downstream cost. Before adding an agent, schema, router, policy layer, eval harness, guardrail, workflow, dependency, or automation, run the deletion-first order:

1. Make the requirement less wrong or less broad.
2. Delete unnecessary steps, parts, policies, queues, and handoffs.
3. Prefer better context, tools, source authority, and feedback over behavioral control machinery.
4. Simplify the remaining path.
5. Optimize, accelerate, or automate only after the simpler system is correct.

Because agents and humans systematically underprice coordination, maintenance, context bloat, stale state, eval surface area, and future merge conflicts, the expected benefit of new complexity must be much greater than its visible cost, not merely slightly higher.

Complexity rule: prefer the smallest deterministic guardrail that prevents a named failure class. Do not add machinery because a plan feels complete; add it only when a simpler context/tool/source fix would not prevent the failure.

Use deterministic code for schemas, permissions, idempotency, budgets, checkpoints, memory APIs, source authority, identity resolution, context assembly, tool execution, human approval, traces, and evals.

Use model-owned adaptive behavior for ambiguous intent, context gathering, tool choice, memory retrieval, task decomposition, plan revision, recovery, and synthesis.

Third rule: truth, retrieval, recall, synthesis, sidecars, candidate signals, and external reports are different architectural roles. Do not let a convenient artifact become a source of truth by accident.

Do not replace open-ended agent behavior with brittle keyword routing, regex parsing, lookup tables, or fixed orchestration unless the task is genuinely deterministic and tested as such. Typed routing and fallback are valid harness patterns only when they are explicit, budgeted, traceable, eval-covered, and approved for their cost/risk class.

Before coding, classify the component as one of:

1. deterministic workflow
2. augmented LLM
3. agent loop
4. multi-agent/subagent system
5. tool or tool registry
6. skill
7. memory subsystem
8. source lane or source authority layer
9. identity resolution layer
10. context engine
11. durable execution layer
12. guardrail or human-review layer
13. cross-agent coordination layer
14. attention or notification policy
15. adoption-state change
16. eval/observability layer
17. agent-native CLI or tool surface
18. repository structure / parallel-agent seam
19. learning-loop or feedback pipeline

For source lanes, define raw capture, identity linking, claim extraction, freshness, authority, contradiction handling, health checks, and promotion rules before wiring the lane into agent answers.

For multi-agent work, ensure one explicit owner or integrator controls shared-file edits and final verification. Contributors should return evidence-backed proposals unless given a disjoint write set.

For agent failures or suspected symptom patches, run an Agent Failure RCA before implementing. Ask what the agent actually saw, what tools/memory/source lanes/feedback it had, whether a capable human would likely fail with the same information state, and what lowest-layer invariant or affordance would prevent recurrence.

Define done in system terms, not personal activity terms. For autonomous behavior, state the acceptance test before implementation, distinguish manual proof from system/autonomous proof, and list untested layers as explicit gaps.

For live or long-running systems, convert incidents into enforceable contracts. Backpressure, budgets, caller attribution, adoption state, rollback, and human attention are harness concerns, not prompt vibes. Never add silent paid fallbacks, silent provider spillover, or production promotion from one good demo.

In the final summary, state:

- component classification
- model-owned decisions
- deterministic harness responsibilities
- tools available and tools missing
- memory behavior
- source authority and truth/synthesis boundaries
- identity resolution behavior
- context behavior
- skills used or added
- guardrails and approvals
- cross-agent ownership or adoption-state changes
- attention/notification behavior
- backpressure, budget, and fallback behavior
- deletion/simplification pass result, including parts or requirements removed
- cost/complexity tradeoff and why any remaining complexity is worth its hidden cost
- Agent Failure RCA / human-counterfactual result when relevant
- adoption state and rollback plan
- acceptance proof, manual-proof gaps, and tests/evals added
