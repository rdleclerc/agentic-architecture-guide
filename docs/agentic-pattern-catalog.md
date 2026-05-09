# Agentic Pattern Catalog

Use this catalog when a coding agent is about to add, refactor, or review agent behavior. The goal is not to add every pattern everywhere. The goal is to choose the smallest pattern that preserves this guide's core contract:

```text
Deterministic harness. Adaptive policy.
```

The pattern is the *shape of the harness*. It must still have typed contracts, traces, budgets, permission gates, source-authority boundaries, and evals.

## 1. Pattern-selection matrix

| Pattern | Use when | Harness contract | Avoid / failure mode |
|---|---|---|---|
| Prompt chaining | A task is naturally staged and each stage has a checkable artifact. | Stage schema, acceptance check per stage, trace link from input to output. | Long opaque chains where stage outputs are not validated. |
| Routing | Inputs should go to different models, tools, skills, queues, or policies. | Typed route set, route confidence/reason, safe default, eval cases, trace. | Brittle keyword routers for open-ended intent. Routing is good when semantic, typed, observed, and tested. |
| Parallelization | Independent subtasks can run without sharing mutable state. | Disjoint ownership, merge protocol, per-slice tests, conflict handling, synthesis step. | Two agents editing the same file/contract without an integrator. |
| Reflection / evaluator-optimizer | Output quality depends on critique and revision. | Explicit rubric, separate critique artifact, max iterations, stop condition, verification tool. | Infinite self-critique or self-approval without external tests/evidence. |
| Tool use / function calling | The agent needs to sense, calculate, mutate, or verify beyond text generation. | Tool catalog entry, input/output schema, permission, idempotency, examples, structured errors. | Broad `run(query)` tools, hidden side effects, unbounded output. |
| Planning | The path cannot be known upfront, but progress needs control. | Plan artifact, checkpoints, replan triggers, budget, status transitions, done criteria. | Treating an initial plan as binding after observations invalidate it. |
| Multi-agent collaboration | Separate roles need different context, tools, memory, policy, or parallel ownership. | Owner/integrator, A2A contract, disjoint write sets, handoff evidence, final synthesis. | Role-play swarms where every agent has the same context and no unique affordance. |
| Memory management | Useful knowledge must survive beyond one inference/run. | Candidate/promote/refute/supersede states, scope, evidence, freshness, privacy. | Append-only notes, stale memory as truth, context-window-as-database. |
| Learning / adaptation | Production traces reveal recurring model, harness, or context failures. | Trace + feedback store, triage lane, eval fixture, guarded rollout, rollback. | Agents rewriting their own policy directly from one anecdote. |
| MCP / tool interop | External tools need discovery and typed execution across runtimes. | Namespaces, schema loading on demand, permission mapping, versioning, trace correlation. | Loading every schema into context or trusting remote tools as policy. |
| Goal setting / monitoring | Long-running work needs measurable progress and stopping. | Goal, milestones, status, budget, checkpoint, stop/escalate rules. | Vague goals like “make it better” with no observable acceptance test. |
| Exception handling / recovery | Tools, providers, or subagents can fail partially. | Error taxonomy, retryability, compensating action, degraded mode, escalation. | Swallowing failures or pretending partial success is complete. |
| Human-in/on-the-loop | Risk, taste, authority, spend, or irreversibility requires review. | Approval payload, risk class, timeout behavior, audit receipt, resume checkpoint. | Asking humans for every minor decision; bypassing approval on retries. |
| RAG / knowledge retrieval | The agent needs external evidence or long-tail domain context. | Source role, freshness, citation/evidence ids, conflict handling, retrieval evals. | Treating retrieved snippets or summaries as source of truth. |
| A2A / inter-agent communication | One agent delegates or requests a result from another. | Request schema, response schema, ownership, allowed tools, evidence requirements, timeout. | Natural-language handoffs with no contract or state reconciliation. |
| Resource-aware optimization | Model/tool choice must balance latency, cost, quality, quotas, and risk. | Routing policy, budgets, attribution, fallback rules, quality thresholds, trace. | Silent paid fallback or provider spillover. Cost-aware routing is good only when explicit and approved. |
| Reasoning techniques | Hard problems need decomposition, symbolic checks, self-consistency, or program-aided reasoning. | Technique chosen deliberately, budgeted, private scratchpad policy, external verification. | Exposing hidden chain-of-thought or using extra reasoning as a substitute for tests. |
| Guardrails / safety | The agent can harm users, data, money, policy, or production systems. | Deterministic checks, allow/deny policy, approval gate, refusal/escalation path, safety evals. | Prompt-only warnings for irreversible actions. |
| Evaluation / monitoring | Behavior must improve or remain stable over time. | Offline evals, online traces, feedback labels, regression fixtures, dashboards/alerts. | One successful demo promoted to production truth. |
| Prioritization | Multiple tasks, alerts, traces, or leads compete for attention. | Scoring fields, queue state, aging/priority policy, owner, audit trail. | “Most recent wins” or notification storms. |
| Exploration / discovery | The system should look for opportunities, unknowns, or anomalies. | Sandbox lane, curiosity budget, source labels, promotion rules, review queue. | Letting exploratory hypotheses contaminate truth or production action. |

## 2. Positive routing and fallback policy

This guide warns against keyword routing because coding agents often replace adaptive policy with brittle branches. That warning should not be read as “routing is bad.” Routing is a first-class agentic pattern when it is a harness decision with tests.

A good route decision records:

- input summary and scope
- candidate routes considered
- selected route and reason
- confidence / uncertainty
- model, tool, skill, queue, or subagent chosen
- budget/cost class
- safe default or escalation path
- eval case or trace id

Fallback has the same rule. Fallback is allowed when it is explicit, budgeted, approved for its risk class, idempotent or replay-safe, and traceable. Silent fallback, silent provider spillover, and “try another paid model without attribution” are anti-patterns.

## 3. Reflection loop for coding agents

For nontrivial agentic code changes, the coding agent should not do a single draft and declare victory. Use a bounded loop:

```text
goal -> context packet -> architecture brief -> implementation slice -> critique -> verification -> integrate or stop
```

Minimum reflection checks:

1. Did I preserve deterministic harness / adaptive policy boundaries?
2. Did I introduce a keyword router, regex semantic guess, giant prompt, or hidden fallback?
3. Are tool/CLI/file interfaces typed and machine-readable?
4. Can another agent work on an adjacent slice without editing the same surface?
5. Is every new memory/source/truth/write path classified?
6. Are tests/evals tied to real incidents or realistic traces?
7. What proof layer is still missing?

Stop when acceptance evidence passes, the budget is exhausted, required information is missing, approval is required, or repeated failures show the plan needs human/integrator review.

## 4. Agent-native CLI checklist

A CLI is a model-facing tool surface. Design it as an API for agents, not only as a human terminal UX.

Required affordances:

- Non-interactive execution: `--no-input`, `--yes`/`--force`, honest non-TTY behavior, no hidden prompts.
- Structured output: uniform `--json`, stable schemas, diagnostics on stderr, documented exit-code taxonomy.
- Actionable errors: validate before side effects, enumerate valid values, include a corrected invocation or next step.
- Safe mutation: `--dry-run`, explicit destructive flags, idempotency keys/natural keys, mutation responses include durable ids.
- Bounded output: default limits, filters, pagination/cursors, truncation metadata, concise-vs-detail modes.
- Vocabulary consistency: mechanically enforced verbs/flags such as `get`, `list`, `create`, `update`, `delete`, `--json`, `--force`, `--limit`.
- Introspection: human `--help`, versioned machine-readable `agent-context`, and long-form skill/task manifests kept in sync with implementation.
- Async support: `--wait`, backoff/jitter, durable job ledger, `jobs list/get/prune`, resumable submit-poll-collect flows.
- Profiles/identity: named profiles, clear precedence (`flag > env > profile > default`), discoverable profile metadata.
- Two-way I/O: artifact delivery targets (`stdout`, atomic file, webhook where appropriate) and a feedback command/log for agent friction.
- Local/prod clarity: every command that can hit local or remote state must state the target clearly in output and traces.

For large CLIs, enforce these from a schema/codegen layer rather than by review convention alone. The same contract should generate or validate CLI commands, SDK/API surfaces, MCP/tool schemas, docs, and skills when possible.

## 5. File and knowledge-graph structure for parallel coding agents

Agentic engineering changes the optimal repository shape. Human-friendly mega-files are often agent-hostile because they force unrelated edits through the same context and merge surface.

Prefer small, contract-shaped slices:

```text
module/
  AGENTS.md                # local operating rules, invariants, ownership, safe edit paths
  public_api.py            # only supported import/call surface for other modules
  contract.py              # typed input/output and state types
  operations/              # one independently changeable behavior per narrow file when useful
  policy.py                # model-owned decision wrapper, no side effects
  harness.py               # deterministic permissions, budgets, checkpoints
  tools.py                 # model-callable affordances and schemas
  prompts/                 # prompt templates/versioned rubrics
  evals/                   # fixtures, rubrics, replay cases
  tests/                   # unit + integration coverage for this slice
  dependency_map.json      # generated or checked map of allowed dependencies
  README.md or lat.md refs # local decision record and ownership notes
```

Rules of thumb:

- Split at stable contracts, not arbitrary line counts.
- Each file should have one reason to change and an obvious owner/slice.
- Make the filesystem a coordination and context layer: local `AGENTS.md`, module README/decision records, schemas, contracts, tests, generated maps, and tool definitions should tell an agent what to inspect next.
- Keep four jobs separate: implementation, conceptual map, public dependency surface, and behavioral truth/tests. A source file should not be forced to do all four.
- Keep deterministic harness, model policy, prompts, tools, evals, and side-effect adapters separate.
- Avoid multi-responsibility files that become mandatory context for every task. For active hand-edited code, 150-250 lines should trigger a split review; 300+ lines is a strong smell; 500+ lines requires an explicit exception such as generated code, declarative data/config, a cohesive algorithm with tight invariants, a stable adapter/vendor boundary, or an intentional fixture/golden file.
- Parallel work requires disjoint write sets, per-slice tests, and a named integrator for shared contracts.
- Prefer one-agent-task-per-file when a behavior can be changed, tested, and reasoned about independently. This is not one-helper-per-file; it is one independently changeable unit per edit surface.
- Every public seam should have a minimal test fixture and an example invocation.
- Enforce the shape with lint rules, generators, dependency-map checks, review agents, and CI; prose-only conventions will drift back toward human-centered mega-files.

`AGENTS.md` should be an index and operating contract, not the only memory of the codebase. Durable design knowledge belongs in topic docs or a markdown knowledge graph with backlinks into code and tests. A `lat.md/`-style graph is one implementation: it keeps architecture, business rules, test specs, and source references searchable and checkable while keeping root instructions short. Module-level `AGENTS.md` files can make each folder behave like a codebase skill: they describe local intent, invariants, public APIs, dependency rules, commands, and safe-edit boundaries.

## 6. Context packets for coding tasks

Before a coding agent edits a nontrivial agentic system, create or assemble a small context packet:

```text
task-context/
  00_goal.md              # observable outcome and user intent
  01_constraints.md       # permissions, budgets, source authority, adoption state
  02_relevant_files.md    # files/symbols with why they matter
  03_commands.md          # tests, evals, local run commands, known flakes
  04_acceptance.md        # system acceptance test and proof layers
  05_risks.md             # side effects, privacy/security, fallback/rollback
```

The packet is not a second giant prompt. It is a scoped working set that can be handed to the main agent, subagent, or integrator. Keep it short, addressable, and updated when the plan changes.

## 7. Feedback-powered learning loop

Observability is incomplete without feedback. A trace says what happened; feedback says whether it was useful, accepted, rejected, inefficient, risky, or wrong.

Store feedback with traces at three levels:

- Model behavior: wrong classification, bad synthesis, missing constraint.
- Harness behavior: bad tool schema, missing read-before-write gate, wrong retry/fallback policy.
- Context behavior: missing retrieval, stale memory, excessive context, wrong source authority.

Useful feedback can be direct user input, indirect product signals (accepted/reverted diffs, tests passing after edits, repeated user correction), generated judge labels, or deterministic rules. Do not let feedback mutate production policy directly. Route it through triage, fixture/eval creation, guarded rollout, and rollback.

## 8. Sources that motivated this catalog

- Antonio Gulli, *Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems*.
- Trevin Chow, “10 Principles for Agent-Native CLIs.”
- Cloudflare, “Building a CLI for all of Cloudflare.”
- Harrison Chase / LangChain, “Agent observability needs feedback to power learning.”
- `lat.md`, “Agent Lattice: a knowledge graph for your codebase, written in markdown.”
- Rob Leclerc, “Agentic Engineering Should Change How We Structure Code” (X article preview/title available publicly; full text requires X article access in this session).
