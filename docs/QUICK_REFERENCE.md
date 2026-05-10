# Quick reference for coding agents

Version: 1.5
Purpose: lossy distillation of the architecture pack. Rules only, no examples, no rationale. Use as cold-start companion to `AGENTS.md`. Load the deep doc only for the topic you are actually touching.

If your task touches **schemas, permissions, idempotency, budgets, checkpoints, source authority, identity resolution, tool execution, human approval, traces, or evals** — that is harness work. Use deterministic code.

If your task touches **ambiguous intent, context selection, tool choice, memory retrieval, task decomposition, plan revision, recovery, or synthesis** — that is policy work. Use the model.

---

## Eight doctrinal claims (non-negotiable)

1. **Deterministic harness, adaptive policy.** Determinism in the harness; ambiguous decisions in the model-owned policy layer with the right tools, memory, skills, and context.
2. **Simplicity before machinery.** Question requirements, delete unnecessary parts/processes, prefer better context/tools/source authority/feedback, simplify what remains, and automate last. Complexity must be worth much more than its visible cost.
3. **Source-of-truth role separation.** Truth, retrieval, recall, synthesis, sidecars, candidate signals, and external reports are different roles. Do not collapse them.
4. **Incidents become contracts.** Every production failure produces a harness change, an acceptance test, an eval/replay fixture, and an adoption rule.
5. **Causal depth.** Do not stop at the first true local explanation. Name the missing contract in memory, context, tool semantics, source authority, durable state, ownership, guardrails, or evals.
6. **Spend authority.** Paid API keys are gateway-owned exception paths, not ambient context. Attribution, budgets, rate limits, and tests that fail when direct key reads come back.
7. **Coupling cost asymmetry.** Declaring a seam now is linear; untangling later is super-linear in callers and editors. Bias forward: declare the seam now even when the local diff would be smaller without it.
8. **Agent-native interfaces.** CLIs, repo shape, local docs, skills, and file seams are model-facing surfaces. Design them for headless JSON, bounded output, dry-runs/idempotency, small cohesive files, and disjoint multi-agent write sets.

---


## Coding Agent Work Contract (every non-trivial coding task)

Before editing, fill or assemble `docs/coding-agent-work-contract.md` using `.agentic/coding_agent_work_contract_template.md` unless the task is tiny and deterministic. Minimum fields: Objective · In scope · Out of scope/stop conditions · Orientation evidence · Plan · Evidence required · Skipped evidence/gaps · Learning trail.

---

## Component classification (declare one before coding)

`deterministic workflow` · `augmented LLM` · `agent loop` · `multi-agent / subagent` · `tool` · `tool registry` · `skill` · `memory subsystem` · `source lane / authority layer` · `identity resolution layer` · `context engine` · `durable execution layer` · `guardrail / human-review layer` · `cross-agent coordination layer` · `attention / notification policy` · `adoption-state change` · `eval / observability layer` · `agent-native CLI or tool surface` · `repository structure / parallel-agent seam` · `learning-loop or feedback pipeline`

---

## Seam-declaration rule (every non-trivial change)

Before code:

1. **Modules touched** — what does this change read, write, or import?
2. **Interfaces depended on** — which contracts does this change consume?
3. **Interfaces defined or changed** — what does this introduce, modify, deprecate, or extend? What is public, what is intentionally private?
4. **Substitutability** — what changes if the implementation behind each interface is swapped (different store, model, transport, provider)? Many things in many places means the seam is wrong.

Six coupling smells (any of these = creating coupling):

- **God-object state bag** — function takes a `context`/`state`/`request` bag and reads ≥4 fields.
- **Reaching through internals** — `module.B._private` access from outside B.
- **Runtime type-switch on opaque payload** — `if event.kind == ...` chain growing branch by branch.
- **Hidden temporal dependency** — A must be called before B, encoded only in caller order.
- **"Just one more parameter" creep** — function accumulates 6+ optional parameters added by N agents.
- **Multi-module test instantiation** — unit test imports 4 modules to construct the system under test.

Detail: `docs/modularity-and-seams.md`. Anti-pattern 9.9. Field lesson 12.10.

---

## Reflection checklist (before declaring done)

1. **Simplicity/deletion** — requirement narrowed; unnecessary machinery deleted or avoided; context/tool/source-affordance alternative considered.
2. **Goal drift** — original goal restated; change still serves it; no quiet redefinition to "make the test pass."
3. **Coupling and seams** — none of the six smells; no boundary crossed; no parameter/branch/field that other modules now depend on by absence.
4. **Shortcuts** — no skipped step (validation, schema, idempotency, source-authority lookup, memory write, eval coverage, durable-state record).
5. **Hidden state** — no undocumented dependency on globals, env vars, file layout, time, process startup order.
6. **Failure modes** — every external dep has stated behavior under slow/unavailable/partial/garbage; nothing silently re-raises.
7. **Tests and evals** — no new behavior is true that no test exercises; no incident class reachable that no eval catches.
8. **Causal depth** — for fixes: proximate cause + ultimate contract both named; if only proximate addressed, remaining incident class named as gap.

Hidden gaps are worse than known gaps.

Detail: `docs/reflection-and-planning.md`. Anti-pattern 9.10.

---

## Plan as artifact (before action)

Goal · Acceptance proof · Coding Agent Work Contract when non-trivial · Component classification · Simplicity/deletion pass · Seam declaration · Failure-mode budget · Routing decision · Out of scope.

Goal-drift checks: before each tool call, before declaring done, inside reflection. If goal genuinely changes mid-task, change the plan explicitly.

Detail: `docs/reflection-and-planning.md`.

---

## Three exception classes (every retry/fallback/degradation attaches to one)

- **Recoverable** — retry per policy; surface only on budget exhaustion; do not poison durable state.
- **Degraded** — produce partial result; mark missing pieces; surface a structured signal (never silent); record what would have been there.
- **Unrecoverable** — stop; do not retry; do not degrade; write structured failure record; alert per attention policy.

A retry without a class is a guess. Silent degradation is a bug. Silent paid spillover is a bug. Silent retry past budget is a bug.

Detail: `docs/exception-taxonomy.md`. Anti-pattern 9.11. Field lesson 12.11.

---

## A2A message contracts (every agent-to-agent message type)

Schema · Direction (request/reply/broadcast/signal/event) · Idempotency (key, hash, dedup window, or documented at-least-once handler) · Versioning (additive vs migration) · Authority (sender + receiver, registry-enforced) · Failure attribution (per exception class, both sides) · Audit surface.

Payloads typed as `dict`/`any` are folklore. A2A traffic with no audit surface is invisible.

Detail: `docs/a2a-contracts.md`. Anti-pattern 9.12.

---

## Cost-aware routing (every paid call attributable, every spillover doctrinal)

Routing inputs: task difficulty · evidence sensitivity · consequence · budget state · lane health · explicit overrides.

Lanes: default (cheap, broad) · escalated (expensive, capable) · degraded (cheapest or stop).

Spillover policy is part of routing, not emergent. Each spillover path attaches to: exception class · destination lane · budget impact · audit record.

Three failure modes: silent escalation · silent fallback · wrong-axis routing. All recover by recording the doctrine decision and auditing the spend.

Detail: `docs/cost-aware-routing.md`. Field lesson 12.12.

---

## Learning loops (every finding has a destination)

- **Within-task**: reflection (above).
- **Across-task**: skill promotion. Pattern works across N tasks → drafted skill (eval, when-to-use) → canonical (owner, rollback). Promotion follows adoption state: `reference_only` → `shadow_mode` → `candidate_write` → `write_enabled` → `canonical` → `deprecated`.
- **System-level**: external critique on slower cadence. Findings → candidate skill / contract change / missing eval / candidate signal / deprecation.

A finding without a destination is a smell. A loop nobody acts on is a journal, not learning.

Detail: `docs/learning-loops.md`. Anti-pattern 9.13. Field lesson 12.13.

---

## Task prioritization (every queued task declares five inputs)

Urgency (none/soft/hard/irreversible) · importance (blocks other lanes?) · preemptability · cost · staleness (hard window / soft decay / appreciation / none).

Queue rule: preemption-immune tasks run to completion · among ready tasks prefer importance, then urgency, then cheaper · overrides recorded with rationale · saturation surfaces as signal, never silent drops.

The harness owns the rule, not the agent.

Detail: `docs/task-prioritization.md`. Anti-pattern 9.14. Field lesson 12.14.

---

## Anti-patterns (never these)

- **9.1 Regex pretending to be intelligence** — ambiguous routing in if/elif/regex.
- **9.2 Giant prompt as architecture** — every rule, memory, tool, transcript stuffed into the system prompt.
- **9.3 Memory as append-only notes** — write summaries to a file with no schema or promotion path.
- **9.4 Tools without semantic affordances** — `run(query: string) → result`.
- **9.5 Multi-agent theater** — committee of agents per task instead of single-agent-first.
- **9.6 Source-of-truth collapse** — wiki, vector index, source DB, sidecar, chat all treated as one memory.
- **9.7 Noisy-lane contamination** — brainstorming or speculation promoted into project truth without review.
- **9.8 Accidental production promotion** — sidecar passes one demo and becomes canonical.
- **9.9 Convenient coupling** — reaching across module boundaries because "it is right there."
- **9.10 Skipping reflection** — declaring done without the §5.14 checklist.
- **9.11 Unclassified errors** — bare except, silent None, retry without class.
- **9.12 Implicit A2A folklore** — pair of agents that work via a hardcoded script with no contract.
- **9.13 No learning loop** — recurring findings with no destination.
- **9.14 FCFS task scheduling** — first-come-first-served by accident, no declared priority rule.

---
- **Category index in bootstrap.** Loading a multi-section reference doc (one section per lane/integration/tool) as bootstrap. Bootstrap pays the cost on every turn and the runtime silently truncates. Split into per-member sub-docs; replace the original with a thin index; let the retriever surface the right sub-doc by query. Detail: `docs/context-engineering.md` and `docs/agentic-coding-for-agentic-systems.md` § 5.2.1.

## Field lessons (operational consequences)

- **12.1 Define done as system behavior** — manual one-off proof is debugging evidence, not completion.
- **12.2 Incidents become contracts, not folklore** — every incident becomes a harness layer, an acceptance test, and an eval.
- **12.3 Proximate causes are not ultimate causes** — go deep enough to name the missing contract.
- **12.4 Backpressure and cost are harness responsibilities** — silent paid fallback is unreviewed side effect.
- **12.5 Claims must reconcile with state** — if claim and state disagree, both are evidence; reconcile, do not arbitrarily prefer.
- **12.6 Keep thesis, current state, and truth separate** — a roadmap is not truth and a synthesis is not truth.
- **12.7 Promote through adoption states** — sidecars, models, workflows promoted via shadow → candidate → canonical with evals, health, rollback, owner.
- **12.8 Human attention is a scarce system resource** — quiet by default; loud only when situation deserves it.
- **12.9 The coding agent is part of the operating system** — its edits, logs, claims, summaries are operating-system memory.
- **12.10 Modularity is a runtime property** — parallel collisions are seam problems, not coordination problems.
- **12.11 Errors are classes, not surprises** — every failure attaches to recoverable / degraded / unrecoverable.
- **12.12 Cost asymmetry is a routing input, not an afterthought** — cost is rarely a runtime emergency, almost always doctrine drift.
- **12.13 Systems that don't learn get worse** — stability is the default state of contracts; improvement is not.
- **12.14 Priority is not optional** — FCFS is the default that emerges when no one declares the rule.

---

## Dependency awareness (every non-trivial change)

Six patterns, ordered cheapest to strongest — pick by failure mode, not aesthetic:

1. **Seam declaration before code** — universal floor. Modules touched · interfaces depended on · interfaces defined or changed · substitutability.
2. **Source ledger on context assembly** — each context item carries source + reason + freshness.
3. **Reverse-lookup retriever** — given a path/symbol you're about to change, what already depends on it? Most underused; usually one script.
4. **Adoption-state tracking** — per-consumer state (legacy / migrating / migrated / deprecated). Forces migrations out of one agent's head into the schema.
5. **Static analysis in CI** — broken-link / stale-reference checks for shared paths, links, names.
6. **Replay tests** — record a real session, re-run after refactor; only for high-blast-radius components.

Anti-pattern: **blind local edit** — agent edits a file as if it were standalone, ships, discovers downstream breakage later. Fix with the cheapest pattern that would have caught the specific failure shape.

Detail: `docs/agentic-coding-for-agentic-systems.md` § 5.21. Adjacent: `docs/modularity-and-seams.md` (seams), `docs/context-engineering.md` (source ledger), `docs/cross-agent-operating-model.md` (adoption state).

---

## Pointers to deep docs

For the topic you are actually touching:

| Topic | Doc |
|---|---|
| Tools | `docs/tool-design.md` |
| Memory | `docs/memory-architecture.md` |
| Context engineering | `docs/context-engineering.md` |
| Skills | `docs/skills.md` |
| Subagents | `docs/subagents.md` |
| Durable execution | `docs/durable-execution.md` |
| Evals | `docs/evals.md` |
| Source authority and truth lanes | `docs/source-authority-and-truth-lanes.md` |
| Cross-agent coordination | `docs/cross-agent-operating-model.md` |
| Modularity and seams | `docs/modularity-and-seams.md` |
| Reflection and planning | `docs/reflection-and-planning.md` |
| Exception taxonomy | `docs/exception-taxonomy.md` |
| A2A contracts | `docs/a2a-contracts.md` |
| Cost-aware routing | `docs/cost-aware-routing.md` |
| Learning loops | `docs/learning-loops.md` |
| Task prioritization | `docs/task-prioritization.md` |

For the full architecture, the executive thesis, all anti-patterns with worked examples, all field lessons with rationale, the canonical coding-agent prompt, the first-engineering-tasks ordering, and the multifile rebuild scaffolding: `docs/agentic-coding-for-agentic-systems.md` and `docs/agentic-systems-engineering.md`.

For the full single-file source: `AGENTIC_ARCHITECTURE.md` (top-level).

---

## Final summary requirements

A non-trivial change ends with the agent stating: component classification · model-owned vs harness responsibilities · tools / skills / memory / source authority / identity / context behavior · guardrails and approvals · cross-agent ownership · attention behavior · backpressure/budget/fallback · adoption state and rollback · causal ladder for fixes · acceptance proof and gaps · plan and goal · seam declaration · exception classes · A2A contract changes · routing and cost · prioritization inputs · learning destination · reflection checklist results.

Hidden gaps are worse than known gaps. State the gaps explicitly.
