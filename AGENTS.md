# AGENTS.md

This repository builds agentic operating systems. Read this whole file (it is short). For deeper detail, load only the doc(s) relevant to the task you are about to do — do not load everything by default.

## Topic → file routing (lazy load)

Read the matching doc only when the listed task applies:

| If you are working on… | Load |
|---|---|
| Coding agents that build agent systems | `docs/agentic-coding-for-agentic-systems.md` |
| End-to-end systems engineering for agents | `docs/agentic-systems-engineering.md` |
| Source lanes, truth vs. retrieval/sidecars, candidate signals | `docs/source-authority-and-truth-lanes.md` |
| Multi-agent coordination, owner/integrator pattern, shared edits | `docs/cross-agent-operating-model.md` |
| Tools, tool registries, tool design, typed enforcement | `docs/tool-design.md` |
| Memory architecture, durability, retrieval boundaries | `docs/memory-architecture.md` |
| Context engines, context assembly, context budgets | `docs/context-engineering.md` |
| Durable execution, checkpoints, resumability | `docs/durable-execution.md` |
| Evals, observability, regression coverage | `docs/evals.md` |
| Skills (design, registration, invocation) | `docs/skills.md` |
| Subagents and delegation | `docs/subagents.md` |

Do **not** load `agentic_architecture_singlefile.md` — it is a compiled human reference and will eat the context window.

Core rule: deterministic harness, adaptive policy.

Use deterministic code for schemas, permissions, idempotency, budgets, checkpoints, memory APIs, source authority, identity resolution, context assembly, tool execution, human approval, traces, and evals.

Use model-owned adaptive behavior for ambiguous intent, context gathering, tool choice, memory retrieval, task decomposition, plan revision, recovery, and synthesis.

Second rule: truth, retrieval, recall, synthesis, sidecars, candidate signals, and external reports are different architectural roles. Do not let a convenient artifact become a source of truth by accident.

Do not replace open-ended agent behavior with brittle keyword routing, regex parsing, lookup tables, or fixed orchestration unless the task is genuinely deterministic and tested as such.

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

For source lanes, define raw capture, identity linking, claim extraction, freshness, authority, contradiction handling, health checks, and promotion rules before wiring the lane into agent answers.

For multi-agent work, ensure one explicit owner or integrator controls shared-file edits and final verification. Contributors should return evidence-backed proposals unless given a disjoint write set.

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
- adoption state and rollback plan
- acceptance proof, manual-proof gaps, and tests/evals added
