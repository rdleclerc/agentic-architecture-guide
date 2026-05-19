# Agentic Coding for Agentic Systems

## Why coding agents default to von Neumann architecture, and how to give them the harness, memory, tools, and skills needed to build adaptive systems

Version: 1.2
Audience: human technical leads, coding agents, staff engineers, agent-platform teams
Recommended repo path: `docs/agentic-coding-for-agentic-systems.md`

---

## 0. Executive thesis

The near-term challenge is not simply “use AI to write code.” The challenge is using agentic coding systems such as Codex, Claude Code, Cursor-style agents, or other coding agents to build *agentic systems themselves*.

That creates a recursive architecture problem. The coding agent is itself an agent, but it has been trained and conditioned mostly on ordinary software: deterministic functions, fixed control flow, request handlers, workflow engines, regular expressions, database calls, API clients, tests, and front-end applications. Those patterns are correct for conventional software. They are often wrong when the thing being built is an adaptive agentic harness.

The failure mode is predictable:

```text
Human intent: Build an agent that can inspect context, choose tools, use memory, adapt its plan, and recover from surprises.

Coding-agent implementation: Add keyword routing, regex parsing, fixed orchestration, hardcoded branches, and a giant prompt.
```

The human thought they were asking for a system with an intelligent policy inside a controlled harness. The coding agent implemented a brittle deterministic workflow that only resembles an agent from the outside.

The correction is not “remove determinism.” The correction is:

```text
Deterministic harness. Adaptive policy.
```

Use deterministic code for schemas, permissions, budgets, checkpoints, idempotency, state, logs, tests, evals, human approval, and tool execution. Use model-owned adaptive behavior for ambiguous interpretation, context selection, tool choice, memory retrieval, task decomposition, plan revision, and synthesis.

A serious agentic system needs more than model calls. It needs a harness: context engine, tool registry, skill system, memory subsystem, source authority, identity resolution, durable execution, hooks, guardrails, traces, evals, and subagent boundaries. Coding agents must have that architecture in their context before they start editing. Otherwise they will fill the missing architecture with the idioms they know: conventional von Neumann control flow.

For systems that serve a real organization, project, or long-lived workflow, the harness also needs an operating model. The agent must know which sources are raw evidence, which stores are authoritative, which pages are synthesis, which indexes are retrieval-only, which helpers are sidecars, which workflows are experimental, and when human attention is too valuable to spend.

The strongest field lesson is that agentic failures rarely stay inside one layer. A stalled publish, runaway retry storm, false memory, or bad handoff usually crosses context, tools, state, model policy, budget, and human attention. Treat each incident as a request to improve the architecture: name the contract that was missing, preserve a replay or eval, and promote the fix only after evidence.

### 0.1 Simplicity and deletion are safety properties

Simplicity is not taste. In agentic systems it is a reliability, cost, and parallelism requirement.

Every new agent, guardrail, policy file, schema, queue, router, eval harness, dependency, prompt clause, and handoff creates hidden cost: more context to load, more state to keep consistent, more traces to inspect, more stale assumptions, more merge surfaces for parallel agents, more ways for the model to see the wrong abstraction, and more future tests to maintain. Humans and coding agents usually see the local benefit immediately and see the complexity cost only weeks later.

Use a deletion-first order before architecture work:

1. Make the requirement less wrong or less broad.
2. Delete unnecessary steps, parts, processes, states, and handoffs.
3. Prefer better context, tools, source authority, and feedback over behavior-policing machinery.
4. Simplify the remaining path.
5. Optimize or accelerate only after the simpler path is correct.
6. Automate last.

The threshold for complexity is therefore asymmetric: the benefit must be much greater than the cost you can see, because the hidden downstream cost is usually undercounted. A plan that spends one hour adding mechanisms should be willing to spend several hours asking what can be deleted, collapsed, or solved by giving the agent the right context and tools.

This matters for RCA. Coding agents often look dumb when the harness deprived them of decisive context, good tools, source authority, or feedback. In those cases, adding more guardrails to force behavior is a symptom patch. The simpler fix is to engineer the information state so a capable agent would naturally do the right thing.

---

## 1. The frame: using agentic coding to build agentic systems

A conventional program is usually designed as a known sequence of operations. Even when it has branches, queues, retries, and services, its core logic is deterministic: given a state, a set of inputs, and the same external responses, the next step is specified by code.

Agentic software is different. It contains a model-driven policy that can choose among possible next actions under uncertainty. It may decide to inspect a file, search memory, call a tool, ask a human, generate a plan, revise that plan, spawn a specialist subagent, or stop. The path is not fully known when the software is written.

This does not mean agentic software is “unstructured.” It means the structure moves. In ordinary software, the structure is mostly the control flow. In agentic software, the structure is the harness around the model:

```text
ordinary program:
  control flow is the main architecture

agentic system:
  harness is the architecture
  model policy is the adaptive decision-maker inside the harness
```

The coding-agent trap is that a coding model tends to convert “ambiguous adaptive policy” into “explicit branch logic.” It does this because most software examples it has seen are built that way, and because coding tasks often reward concrete implementation over architectural uncertainty.

That is why a repo building agents needs standing architectural instructions. A one-off prompt saying “make this agentic” is too weak. The coding agent needs a durable architectural contract that it reads before editing.

---

## 2. The von Neumann lens and why it distorts agent design

The von Neumann style of computing is stored-program computing: instructions and data live in memory, and the machine executes instructions step by step. Modern software has grown far beyond the original model, but the mental pattern remains: define the data, define the functions, define the control flow, run the procedure.

That lens is valuable. It gives us tests, reproducibility, observability, safety, and debuggability. The problem appears when it becomes the only lens.

When a coding agent sees a request like:

```text
The agent should understand whether the user is asking about a portfolio company, then retrieve the right memory, inspect recent notes, choose the right diligence workflow, and produce an investment memo.
```

it may implement:

```python
if "portfolio" in user_input.lower():
    run_portfolio_company_flow()
elif "diligence" in user_input.lower():
    run_diligence_flow()
elif "memo" in user_input.lower():
    run_memo_flow()
```

That is a deterministic intent router. It can be useful for a narrow command palette. It is not a general agentic interface. It will fail when the user says, “What changed in the Convex deal since our last IC call?” or “Show me why this company is starting to look like a vertical SaaS trap.”

The user expected semantic understanding, memory retrieval, tool choice, and judgment. The implementation supplied keyword matching.

This is the central translation error:

```text
Human workflow assumption:
  “The agent will understand the work and pull the right context.”

Coding-agent implementation assumption:
  “I should encode the workflow as explicit branches.”
```

Those are not the same architecture.

---

## 3. The jagged frontier: what will improve quickly and what will remain brittle

The “bitter lesson” says that general methods that scale with compute tend to win over hand-engineered methods in the long run. For agentic systems, that implies model reasoning, tool-use competence, multimodal perception, code generation, and long-horizon planning will likely continue improving as models scale and training improves.

But the near-term frontier is jagged. Some capabilities improve faster than others. Memory, context selection, provenance, long-running state, eval reliability, safety boundaries, and tool semantics are not solved just by making the context window larger or the model more intelligent.

The practical implication is:

```text
Do not hardcode brittle substitutes for capabilities that models will soon do better.
Do build durable harnesses for bottlenecks that raw model scaling does not automatically solve.
```

### 3.1 Capabilities likely to improve with frontier models

These are places where the system should avoid premature over-engineering with brittle hand rules:

1. Natural-language understanding of user intent.
2. Tool choice under ordinary ambiguity.
3. Multi-step reasoning when observations change the plan.
4. Codebase exploration and synthesis.
5. Transforming loosely specified instructions into usable artifacts.
6. Detecting missing context and asking targeted questions.
7. Using examples to infer style, procedure, and local conventions.

For these, the harness should expose good tools and context, then let the model decide.

### 3.2 Capabilities that require explicit harness design

These are not reliably solved by “more model” alone:

1. What context gets loaded and what stays out.
2. How memories are written, scoped, retrieved, updated, contradicted, and retired.
3. Which tools exist, how they are described, and what side effects they can cause.
4. How skills are packaged, discovered, loaded, and tested.
5. How long-running tasks checkpoint and resume.
6. How side effects are made idempotent.
7. How risky actions require human review.
8. How traces and evals prove the agent is doing the right thing.
9. How subagents are isolated by role, tools, memory, and context.
10. How the system prevents context bloat and stale-memory poisoning.

This is the harness layer. It is the architecture the coding agent must be taught to build.

---

## 4. Context is not memory, and a larger context window is not a memory system

A common mistake is to treat the context window as a database. It is not. The context window is the temporary working set passed to the model for a specific inference. Memory is durable information outside that prompt that can be searched, inspected, updated, and governed.

Larger context windows help, but they do not eliminate context engineering. Long contexts can degrade because relevant information may be diluted, stale material can distract the model, and facts in the middle of long prompts may be used less reliably than facts at the beginning or end. Bigger windows can also create false confidence: “the information was in context” does not mean the model used it correctly.

Humans appear to have a different retrieval pattern. A small cue can bring a large hidden body of knowledge into awareness. We do not keep every relevant fact in immediate conscious attention. We carry a broad latent store and retrieve selectively. Agentic systems need an engineered analogue:

```text
broad memory surface area
+ fast retrieval
+ scoped context assembly
+ compaction
+ provenance
+ contradiction handling
+ just-in-time skill and tool loading
```

The agent should not see everything. It should see what it needs, know how to ask for more, and have tools to retrieve missing context.

---

## 5. The agentic harness

An agentic harness is the runtime that mediates between the model and the world. It provides affordances, constraints, state, memory, and observability.

A minimal serious harness has these layers:

```text
1. Intake and authorization
2. Context engine
3. Tool registry and tool search
4. Skill registry and skill loading
5. Memory subsystem
6. Source authority and identity resolution
7. Model policy loop
8. Tool execution sandbox
9. State, checkpointing, and replay
10. Hooks, guardrails, and human approval
11. Tracing, evals, and review
12. Attention policy and operating posture
13. Subagent or cross-agent orchestration when needed
```

### 5.1 Intake and authorization

This layer normalizes the user request and determines the allowed operating envelope.

It should answer:

```text
Who is asking?
What workspace, project, customer, or account is in scope?
What tools may be used?
What side effects are allowed?
What human approvals are required?
What cost, step, and time budgets apply?
What data boundaries apply?
```

The coding agent should not bury these policies inside scattered branches. They should be explicit harness configuration.

### 5.2 Context engine

The context engine decides what enters the model prompt.

It should assemble:

```text
system/developer instructions
repo rules
current user request
active plan/state
relevant retrieved memory
relevant files or snippets
available tool summaries
available skill summaries
recent observations
constraints and budgets
source ledger
```

It should not dump the whole repo, every prior conversation, every memory, every tool schema, and every skill body into the prompt. That produces context bloat.

A good context engine uses progressive disclosure:

```text
always loaded:
  short root instructions, current request, active state, high-priority constraints

loaded by retrieval:
  memories, documents, files, examples, prior episodes

loaded by need:
  full tool schemas, skill bodies, long references, large files

removed or compressed:
  stale messages, redundant observations, low-value intermediate work
```

The context engine should also produce a source ledger: a machine-readable list of what was included and why.

### 5.3 Tool registry and tool search

Tools are not just functions. They are the action surface of the agent.

Every tool needs a contract:

```yaml
name: memory_search
purpose: Retrieve relevant long-term memories by semantic query and filters.
when_to_use:
  - The task depends on prior user/project/company knowledge.
  - The current prompt refers to something not fully specified.
when_not_to_use:
  - The needed fact is already in the current context with clear provenance.
input_schema:
  query: string
  namespaces: string[]
  limit: integer
  freshness: optional string
output_schema:
  memories:
    - id: string
      text: string
      source: string
      confidence: number
      created_at: string
      updated_at: string
      superseded_by: optional string
side_effects: none
permission_level: read
failure_modes:
  - no relevant memory
  - conflicting memories
  - stale memory
observability:
  trace_fields: [query, namespaces, result_count, selected_ids]
```

Bad tool design produces bad agents. If the tools are vague, too broad, too slow, too dangerous, or poorly described, the model will misuse them. A deterministic API meant for a human programmer is often not a good agent tool. Agent tools need semantic affordances and clear usage boundaries.

### 5.4 Skill registry and skill loading

A skill is reusable procedural knowledge. It is not merely a prompt. A strong skill package contains:

```text
SKILL.md
examples/
scripts/
templates/
fixtures/
tests/
references/
```

Skills are for “how this kind of task is done here.” Examples:

```text
openclaw-agentic-tool-designer
write-memory-schema
build-context-policy
create-eval-dataset
review-agentic-architecture
run-investment-memo-workflow
```

A skill should have a small metadata surface that is visible before loading the full skill:

```yaml
name: openclaw-agentic-tool-designer
description: Use when adding or modifying a tool exposed to an agent.
triggers:
  - tool contract
  - agent affordance
  - side-effecting action
  - schema for model tool use
loads:
  - SKILL.md
  - examples/tool_contract.yaml
  - tests/tool_contract_eval.md
```

This lets the model discover that a skill exists without polluting the prompt with every skill body.

### 5.5 Memory subsystem

Memory must be designed as a governed subsystem, not an append-only note dump.

Use at least four memory types:

```text
working memory:
  current task state, plan, open questions, active artifacts

episodic memory:
  prior actions, conversations, decisions, traces, outcomes

semantic memory:
  durable facts about users, projects, companies, markets, codebase, policies

procedural memory:
  reusable methods, preferences, workflows, skills, instructions
```

Memory writes should usually be candidates before they become durable truth:

```yaml
id: mem_candidate_123
claim: "Project Alpha uses Postgres for durable agent checkpoints."
scope: [repo:alpha, subsystem:agent_runtime]
evidence:
  - source_type: file
    source: runtime/checkpoints/postgres_checkpointer.py
    quote_or_summary: "CheckpointSaver is backed by Postgres."
confidence: 0.86
freshness: observed_2026-04-28
sensitivity: internal
status: candidate
review_required: false
supersedes: []
contradicts: []
```

A memory subsystem should support:

```text
memory_search
memory_get
memory_write_candidate
memory_promote
memory_update
memory_refute
memory_supersede
memory_forget_or_expire
memory_trace_usage
```

The coding agent must not implement memory as `memories.txt += new_fact` unless the system is a toy. Memory needs provenance, scope, confidence, recency, contradiction handling, and deletion or expiration.

### 5.6 Model policy loop

The model policy loop is where adaptivity belongs.

A simplified loop:

```python
def run_agent(task, runtime):
    state = runtime.start_or_resume(task)

    while not state.done:
        context = runtime.context_engine.assemble(state)
        action = runtime.model.decide(context)

        runtime.guardrails.validate_model_action(action, state)

        if action.type == "tool_call":
            result = runtime.tools.execute(action.tool, action.args, state)
            state = runtime.observe(result)

        elif action.type == "ask_human":
            state = runtime.pause_for_human(action.question)

        elif action.type == "final_answer":
            state = runtime.validate_and_finish(action.answer)

        else:
            state = runtime.handle_invalid_action(action)

        runtime.checkpoint(state)
        runtime.trace.record_step(state, action)

    return state.output
```

The loop is deterministic in its mechanics but adaptive in the model’s choice of action.

### 5.7 Tool execution sandbox

The tool executor is deterministic. It should enforce:

```text
schema validation
permissions
sandboxing
rate limits
timeouts
idempotency keys
side-effect classification
human approval for risky operations
structured errors
redaction
trace logging
```

For example, a `send_email` tool is not just a function call. It is a side-effecting operation that may require approval, recipient validation, content logging, retry limits, idempotency, and audit history.

### 5.8 Durable state, checkpoints, and replay

Serious agents need to survive interruption, retry, and human review. Long-running agents should checkpoint state after each meaningful step.

A checkpoint should include:

```text
task id
thread/session id
step number
current plan
messages or compacted transcript
retrieved memory ids
tool calls and results
pending approvals
artifacts
budget usage
random/model-call boundaries
side-effect ids
trace ids
```

Nondeterministic operations and side effects should be wrapped so replay does not duplicate external actions. If the agent sends an email, charges a card, deletes a file, creates a ticket, or writes to production, replay must not blindly repeat the operation.

### 5.9 Hooks, guardrails, and human approval

Hooks and guardrails are deterministic control points around adaptive behavior.

Examples:

```text
Before model call:
  validate context budget and remove disallowed sources

Before tool call:
  validate schema, permission, approval, idempotency

After tool call:
  sanitize output, classify result, update trace

Before compaction:
  flush important candidate memory

After compaction:
  verify open tasks and constraints survived

Before final answer:
  run evaluator or checklist
```

Human approval is a first-class tool, not an afterthought:

```text
request_human_approval(action, risk, evidence, proposed_payload)
```

### 5.10 Tracing and evals

A conventional test can prove that a function returns the right value. Agentic systems need additional evaluation.

Evaluate:

```text
Did the agent retrieve the right memory?
Did it avoid stale or contradicted memory?
Did it choose the right tool?
Did it avoid a risky side effect without approval?
Did it recover from tool failure?
Did it stop instead of looping?
Did it use a skill when the task required one?
Did it preserve key context through compaction?
Did it produce a result with evidence?
```

The trace should show not just final output but process: context included, tools available, tool chosen, result observed, memories used, state changes, approval gates, and final validation.


### 5.11 Source authority, identity, and truth lanes

Memory is not the same as truth. A mature operating system usually has several different knowledge surfaces:

```text
raw source lanes: original messages, transcripts, documents, events, API records
structured truth: normalized claims, entities, relationships, commitments, and state
retrieval indexes: vector or keyword search surfaces over source material
recall memory: operator/session continuity and useful prior experience
synthesis artifacts: wiki pages, briefs, dashboards, reports, and summaries
candidate signals: open questions, contradictions, staleness warnings, and review queues
sidecars: external helpers that improve hygiene or workflow without owning truth
outbound artifacts: emails, memos, reports, alerts, or user-visible decisions
```

A coding agent should not let these roles blur. A wiki page may be useful synthesis without being the authoritative store. A vector index may retrieve evidence without deciding which evidence wins. A sidecar may improve skill resolution without becoming canonical memory. A noisy channel may produce excellent ideas without becoming company truth.

Every source lane should declare:

```text
raw capture format
idempotency key
entity and identity resolution rules
claim extraction rules
source authority rank
freshness and staleness policy
contradiction handling
promotion and review path
health checks
rendering or synthesis behavior
redaction and external-sharing policy
```

Identity resolution deserves first-class status. If the system confuses two people, companies, accounts, projects, or source handles, every downstream memory and synthesis layer inherits the error. Resolve identities before promoting claims. Keep aliases, domains, external IDs, merge decisions, and unmerge procedures auditable.

### 5.12 Attention budgets and operating posture

The harness should budget human attention, not only tokens and dollars. A useful agent is often quiet.

Define when the agent should:

```text
stay silent
record internally
open a review queue
ask one targeted question
send a notification
interrupt immediately
request approval
take a reversible action
refuse or stop
```

This matters most in chat, email, meetings, and alerting surfaces. If an agent posts every plausible thought, humans stop trusting it. Operating posture should be explicit: source-backed, selective, reversible where possible, and loud only when the situation deserves it.

### 5.13 Adoption states and cross-agent coordination

Agentic systems absorb tools, sidecars, model upgrades, workflows, and specialist agents over time. Every addition should have an adoption state:

```text
reference_only: useful for reading or inspiration, not trusted for execution
shadow_mode: runs beside production, writes reports or diffs, no live authority
read_only: can inspect production truth but cannot mutate it
candidate_write: can propose changes to a review queue
write_enabled: can mutate a scoped surface with tests, logs, and rollback
canonical: owns a defined source of truth or production workflow
deprecated: retained only for migration or replay
retired: removed from active use
```

Do not promote a helper, sidecar, subagent, or new model path by vibes. Promotion requires a contract, evals, health checks, rollback, and a named owner.

Cross-agent coding work needs the same discipline. If multiple coding agents or sessions touch the same system, assign one integrator and make contributors produce evidence-backed proposals unless they have disjoint write ownership. Durable coordination belongs in files, not in one agent's private chat context.

---

## 6. What the coding agent needs in its own context

A coding agent cannot build the right architecture if the relevant architecture is not in context. It needs persistent repo-level instruction, plus just-in-time procedural knowledge.

Do not rely on a single long prompt. Create a repo architecture pack.

Recommended structure:

```text
AGENTS.md
CLAUDE.md
docs/
  agentic-coding-for-agentic-systems.md
  agentic-systems-engineering.md
  agentic-pattern-catalog.md
  source-authority-and-truth-lanes.md
  cross-agent-operating-model.md
  context-engineering.md
  tool-design.md
  skills.md
  memory-architecture.md
  durable-execution.md
  evals.md
  subagents.md
.agentic/
  context_policy.yaml
  tool_catalog.yaml
  memory_schema.yaml
  source_authority.yaml
  coordination_policy.yaml
  skill_registry.yaml
  eval_matrix.yaml
.claude/
  skills/
    openclaw-agentic-tool-designer/SKILL.md
    design-agent-memory/SKILL.md
    design-context-engine/SKILL.md
    build-agent-eval/SKILL.md
    review-agentic-architecture/SKILL.md
.github/
  pull_request_template.md
tests/
  agentic/
    tool_choice_cases.yaml
    memory_retrieval_cases.yaml
    context_compaction_cases.yaml
    guardrail_cases.yaml
    recovery_cases.yaml
```

`AGENTS.md` and `CLAUDE.md` should be short. They should point to the deeper documents rather than trying to include everything. Treat root instructions as an index and operating contract, not as the repository's only memory. Durable design knowledge belongs in topic docs, ADRs, prompt libraries, eval fixtures, or a checkable markdown knowledge graph.

### 6.1 Context packets, prompt libraries, and repo shape for coding agents

For nontrivial agentic changes, create or assemble a small task context packet before editing:

```text
task-context/
  00_goal.md              # observable outcome and user intent
  01_constraints.md       # permissions, budgets, source authority, adoption state
  02_relevant_files.md    # files/symbols with why they matter
  03_commands.md          # tests, evals, local run commands, known flakes
  04_acceptance.md        # system acceptance test and proof layers
  05_risks.md             # side effects, privacy/security, fallback/rollback
```

The packet is not a second giant prompt. It is a scoped working set that can be handed to the main agent, a subagent, or an integrator without forcing them to rediscover the whole codebase. Keep it addressable and update it when the plan changes.

Agentic repos should also carry prompt and procedure assets as code:

```text
prompts/ or .agentic/prompts/
  <agent_or_skill>/<purpose>.md
  rubrics/<eval_name>.md
  examples/<case_name>.md
```

A prompt library should have owners, versions, intended models, eval links, and known failure modes. Do not bury long-lived prompt behavior in an always-loaded root file or inline string unless the prompt is genuinely trivial.

Finally, shape code for parallel coding agents. Prefer small, contract-shaped slices where deterministic harness, model policy, prompts, tool schemas, eval fixtures, tests, and side-effect adapters are separable. Split at stable contracts rather than arbitrary line counts. For active hand-edited code, 150-250 lines should trigger a split review; 300+ lines is a strong smell; 500+ lines requires an explicit exception such as generated code, declarative data/config, a cohesive algorithm with tight invariants, a stable adapter/vendor boundary, or an intentional fixture/golden file. Parallel work needs disjoint write sets, per-slice tests, and a named integrator for shared contracts.

For agent-native modules, separate the jobs that old service files often combine: implementation, conceptual map, dependency surface, and behavioral truth/tests. Put local rules in module-level `AGENTS.md` or README files, export only through `public_api.py` / `public-api.ts` / package index surfaces, co-locate tests and eval fixtures, and generate or check dependency maps. Prefer one-agent-task-per-file when a behavior can be changed, tested, and reasoned about independently. This is not one-helper-per-file; it is one independently changeable unit per edit surface.

`AGENTS.md` can point to a `lat.md/`-style markdown knowledge graph or ordinary topic docs. The important property is that architecture decisions, business rules, test specs, and code references are discoverable, linked, and checkable instead of buried in one flat file. Prose is not enough: reinforce the shape with lint rules, generators, dependency checks, review agents, and CI so agents do not drift back to human-centered mega-files.


### 6.2 Minimal AGENTS.md

```md
# AGENTS.md

This repository builds agentic systems. Before editing agent logic, read:

- docs/agentic-coding-for-agentic-systems.md
- docs/agentic-systems-engineering.md
- docs/agentic-pattern-catalog.md
- docs/tool-design.md
- docs/memory-architecture.md
- docs/context-engineering.md

Core rule: deterministic harness, adaptive policy.

Do not replace open-ended agent behavior with brittle keyword routing, regex parsing, lookup tables, or fixed orchestration unless the task is genuinely deterministic and tested as such. Typed routing/fallback are allowed only when explicit, budgeted, traceable, eval-covered, and approved for their cost/risk class.

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
13. attention or notification policy
14. adoption-state change
15. eval/observability layer

In the final summary, state:

- model-owned decisions
- deterministic harness responsibilities
- tools available and tools missing
- memory behavior
- source authority and identity behavior
- context behavior
- skills used or added
- guardrails and approvals
- adoption state, rollback, and backpressure/fallback behavior
- acceptance proof, known gaps, and tests/evals added
```

### 6.3 Minimal CLAUDE.md

```md
# CLAUDE.md

This repo builds agentic systems. Read AGENTS.md first.

Use deterministic code for the harness: schemas, permissions, idempotency, state, checkpoints, compaction, tool execution, human approval, traces, and evals.

Use model-owned adaptive behavior for ambiguous intent, context gathering, memory retrieval, tool choice, plan revision, and synthesis.

Do not implement open-ended agent behavior as keyword routers, regex intent detection, hardcoded branches, or fixed workflows unless explicitly justified and tested.

For any agentic change, inspect the relevant tools, skills, memory, source authority, identity policy, context policy, durability, cost/fallback policy, adoption state, and evals before editing code.

Define done as observable system behavior, not a manual one-off proof.
```

### 6.4 Pull request template

```md
## Agentic architecture review

Component classification:

Model-owned decisions:

Deterministic harness responsibilities:

Tools added/changed:

Tools the agent ought to have but does not yet have:

Skills added/changed:

Memory read/write behavior:

Context assembly behavior:

Durability/checkpoint/replay behavior:

Guardrails and human approval gates:

Evals/tests added:

Known failure modes:

Why this is not brittle deterministic orchestration:
```

---

## 7. Detailed build plan for the architecture pack

This section is written as a handoff to coding agents.

### Phase 0: Install the architecture contract

Objective: make the repo self-orienting for coding agents.

Deliverables:

```text
AGENTS.md
CLAUDE.md
docs/agentic-coding-for-agentic-systems.md
docs/agentic-systems-engineering.md
docs/tool-design.md
docs/memory-architecture.md
docs/context-engineering.md
docs/skills.md
docs/durable-execution.md
docs/evals.md
.github/pull_request_template.md
```

Acceptance criteria:

```text
- A coding agent opening the repo sees that this is an agentic system.
- The root files are concise enough to stay in context.
- Deeper docs exist for tools, memory, context, skills, durability, and evals.
- PRs require an agentic architecture review.
```

Coding-agent task:

```text
Create the repo architecture pack. Keep AGENTS.md and CLAUDE.md short. Put long-form guidance in docs/. Add a PR template that requires the agentic architecture review fields.
```

### Phase 1: Inventory the existing system

Objective: find where the code currently substitutes deterministic branches for adaptive agent behavior.

Deliverables:

```text
docs/current-agentic-inventory.md
```

Inventory schema:

```md
# Current agentic inventory

## Entry points

## Agent loops

## Deterministic workflows

## Tool registry

## Tool execution permissions

## Skills or procedural instructions

## Memory stores

## Source lanes and authority rules

## Identity resolution and merge/unmerge paths

## Context assembly path

## Attention and notification policy

## Adoption states for sidecars, model paths, and workflows

## Cross-agent coordination rules

## Checkpointing/durability

## Hooks/guardrails

## Evals/tests

## Brittle orchestration risks

## Missing affordances
```

Acceptance criteria:

```text
- Every agent entry point is listed.
- Every tool surface is listed.
- Every memory surface is listed.
- Context assembly is documented.
- At least five brittle orchestration risks are identified, or the document states why fewer exist.
```

Coding-agent task:

```text
Inspect the repo before editing behavior. Produce docs/current-agentic-inventory.md. Highlight keyword routers, regex intent detection, giant prompts, unbounded loops, unsafe tools, missing memory provenance, missing compaction, and missing evals.
```

### Phase 2: Build or refactor the context engine

Objective: make context assembly explicit, inspectable, bounded, and testable.

Deliverables:

```text
.agentic/context_policy.yaml
src/agentic/context_engine.*
tests/agentic/context_compaction_cases.*
```

Context policy example:

```yaml
budget:
  max_context_tokens: 120000
  reserved_for_response: 8000
  reserved_for_tool_results: 20000
always_include:
  - root_instructions
  - current_user_request
  - active_task_state
  - safety_policy
include_by_retrieval:
  - semantic_memory
  - episodic_memory
  - relevant_files
  - prior_artifacts
include_by_activation:
  - full_tool_schema
  - full_skill_body
  - long_reference_docs
compaction:
  trigger_at_context_fraction: 0.75
  preserve:
    - user_goal
    - constraints
    - open_questions
    - decisions
    - evidence
    - pending_tool_results
    - pending_approvals
source_ledger_required: true
```

Acceptance criteria:

```text
- Context assembly has one primary code path.
- Each included context item has source, reason, priority, and token estimate.
- Long skills and long tool docs are not always loaded.
- Compaction preserves goals, constraints, open tasks, and evidence.
- Tests prove important information survives compaction.
```

Coding-agent task:

```text
Implement a context engine with progressive disclosure. Do not dump all memory, tools, skills, or files into the prompt. Add a source ledger. Add tests for context budgeting and compaction survival.
```

### Phase 3: Build the tool registry and tool contracts

Objective: make tools discoverable, typed, permissioned, and observable.

Deliverables:

```text
.agentic/tool_catalog.yaml
src/agentic/tools/registry.*
src/agentic/tools/executor.*
docs/tool-design.md
tests/agentic/tool_contract_cases.*
tests/agentic/tool_choice_cases.*
```

Required tool contract fields:

```yaml
name: string
description_for_model: string
purpose: string
when_to_use: string[]
when_not_to_use: string[]
input_schema: object
output_schema: object
side_effects: none | read | write | external_write | destructive
permission_level: public | workspace | sensitive | approval_required
idempotency_required: boolean
examples: object[]
failure_modes: string[]
observability:
  trace_fields: string[]
evals:
  tool_choice_cases: string[]
  misuse_cases: string[]
```

Core tools most agentic systems should consider:

```text
context_inspect
context_request_more
skill_search
skill_load
tool_search
tool_inspect
memory_search
memory_get
memory_write_candidate
memory_promote
memory_refute
checkpoint_get
checkpoint_save
request_human_approval
artifact_read
artifact_write
run_eval
emit_trace
spawn_subagent
```

Acceptance criteria:

```text
- Every tool has schema, side-effect class, permission class, and examples.
- Side-effecting tools require idempotency keys.
- Risky tools require human approval.
- Tool execution emits structured traces.
- Tool-choice evals cover correct use and misuse.
```

Coding-agent task:

```text
Create or refactor the tool registry. Convert implicit helper functions into explicit agent tools only when the model should be able to call them. Add tool contracts and tool-choice evals. Do not expose broad unsafe tools without permissions and approval gates.
```

### Phase 4: Build the skill system

Objective: package procedural knowledge so the agent can load the right competence just in time.

Deliverables:

```text
.agentic/skill_registry.yaml
skills/openclaw-agentic-tool-designer/SKILL.md
skills/design-agent-memory/SKILL.md
skills/design-source-lane/SKILL.md
skills/design-context-engine/SKILL.md
skills/build-agent-eval/SKILL.md
skills/review-agentic-architecture/SKILL.md
.claude/skills/*/SKILL.md and .codex/skills/*/SKILL.md adapter links or generated copies
docs/skills.md
```

Skill structure:

```text
skill-name/
  SKILL.md
  examples/
  scripts/
  templates/
  tests/
  references/
```

`SKILL.md` template:

```md
---
name: openclaw-agentic-tool-designer
description: Use when adding, modifying, or reviewing a tool exposed to an agent.
---

# OpenClaw Agentic Tool Designer

## When to use

Use this skill when the change affects a model-callable tool, tool registry, tool schema, tool permission, or tool-result format.

## Procedure

1. Identify whether the model should call this directly.
2. Define when to use and when not to use.
3. Define input and output schemas.
4. Classify side effects and permissions.
5. Add idempotency if the tool writes externally.
6. Add examples and misuse cases.
7. Add tool-choice evals.
8. Add trace fields.

## Output

Return a tool contract and list of tests/evals to add.
```

Acceptance criteria:

```text
- Skills are discoverable by name and description.
- Full skill bodies are loaded only when relevant.
- Skills include examples and test guidance.
- Coding agents are instructed to create a skill instead of another hardcoded branch when the problem is reusable procedural knowledge.
```

Coding-agent task:

```text
Add the initial skill library. Make skills procedural and testable. Do not duplicate long instructions in AGENTS.md or CLAUDE.md; load detailed procedures through skills or docs.
```

### Phase 5: Build the memory subsystem

Objective: separate durable memory from context and make memory safe, scoped, retrievable, and reviewable.

Deliverables:

```text
.agentic/memory_schema.yaml
src/agentic/memory/store.*
src/agentic/memory/retrieval.*
src/agentic/memory/promotion.*
src/agentic/memory/contradictions.*
docs/memory-architecture.md
tests/agentic/memory_retrieval_cases.*
tests/agentic/memory_write_cases.*
```

Memory schema example:

```yaml
memory:
  id: string
  type: working | episodic | semantic | procedural
  scope:
    user_id: optional string
    org_id: optional string
    repo: optional string
    project: optional string
    entity: optional string
  claim: string
  evidence:
    - source_type: file | message | tool_result | human_review | external_doc
      source_ref: string
      summary: string
  confidence: number
  sensitivity: public | internal | confidential | restricted
  status: candidate | promoted | superseded | refuted | expired
  created_at: datetime
  updated_at: datetime
  expires_at: optional datetime
  supersedes: string[]
  contradicted_by: string[]
  retrieval_tags: string[]
```

Memory policy:

```text
- The agent may search memory when prior context is likely relevant.
- The agent may propose memory writes.
- Promotion can be automatic only for low-risk, high-evidence claims.
- Sensitive, strategic, or user-preference memories require stricter policy.
- Contradicted memories must not be silently overwritten.
- Memory used in final outputs must be traceable.
```

Acceptance criteria:

```text
- Memory is not an append-only text file.
- Memory retrieval supports namespaces/scopes.
- Memory writes capture evidence and confidence.
- Stale or contradicted memories are handled explicitly.
- Tests cover relevant retrieval, stale retrieval, contradiction, and promotion.
```

Coding-agent task:

```text
Implement memory as a governed subsystem. Add memory tools. Do not write directly to arbitrary notes files from agent policy code. Add retrieval and write evals.
```


### Phase 5A: Build source authority and identity contracts

Objective: make source truth, retrieval, synthesis, sidecars, and candidate signals explicit.

Deliverables:

```text
docs/source-authority-and-truth-lanes.md
.agentic/source_authority.yaml
src/agentic/source_lanes/*
src/agentic/identity/*
tests/agentic/source_authority_cases.*
tests/agentic/identity_resolution_cases.*
```

Acceptance criteria:

```text
- Every source lane declares raw capture, idempotency, entity linking, claim extraction, freshness, authority, contradictions, health checks, and promotion rules.
- Identity resolution is auditable and supports aliases, external ids, merge evidence, and unmerge procedures.
- Synthesis artifacts are marked as synthesis, not truth.
- Retrieval indexes retrieve evidence but do not become authority.
- Noisy idea lanes produce candidates, digests, or review queues rather than promoted claims by default.
```

Coding-agent task:

```text
Add source-lane and identity contracts before wiring a new corpus, channel, sidecar, or synthesis surface into agent answers. Add evals for conflicts, stale evidence, bad merges, and promotion mistakes.
```

### Phase 6: Refactor the agent loop

Objective: separate adaptive model decisions from deterministic harness mechanics.

Deliverables:

```text
src/agentic/runtime/agent_loop.*
src/agentic/runtime/state.*
src/agentic/runtime/actions.*
src/agentic/runtime/stop_conditions.*
tests/agentic/agent_loop_cases.*
```

Action schema:

```yaml
action:
  type: tool_call | ask_human | final_answer | delegate | request_context | stop
  rationale: string
  tool_name: optional string
  tool_args: optional object
  approval_request: optional object
  expected_observation: optional string
```

Stop conditions:

```text
- final answer validated
- task completed
- human approval required
- missing required information
- budget exhausted
- repeated failure detected
- safety boundary reached
```

Acceptance criteria:

```text
- The agent loop is inspectable and testable.
- The model chooses actions; the harness validates and executes them.
- Stop conditions are explicit.
- Tool failures become observations, not silent fallbacks.
- Repeated failures trigger recovery or human escalation.
```

Coding-agent task:

```text
Refactor the agent loop so the model owns ambiguous next-action choice and the harness owns validation, execution, state, checkpoints, traces, and stopping. Remove brittle keyword routers unless they are explicitly part of a deterministic command workflow.
```

### Phase 7: Add subagents only where boundaries justify them

Objective: use subagents for isolation, specialization, and context control, not because “multi-agent” sounds better.

Use subagents when at least one of these is true:

```text
- The specialist needs different tools.
- The specialist needs different instructions.
- The specialist needs separate memory scope.
- The specialist needs a separate context window.
- The task benefits from parallel exploration.
- The main agent should remain in control while delegating bounded work.
- Human approval or compliance policy differs by role.
```

Do not split agents merely to imitate a human org chart. Multi-agent systems add overhead, coordination failures, and trace complexity.

Deliverables:

```text
docs/subagents.md
.agentic/subagent_registry.yaml
src/agentic/subagents/*
tests/agentic/subagent_cases.*
```

Subagent contract:

```yaml
name: codebase_explorer
purpose: Explore code and return findings without modifying files.
tools_allowed:
  - file_read
  - grep
  - symbol_search
  - context_request_more
tools_forbidden:
  - file_write
  - shell_write
  - external_send
memory_scope: repo_read_only
returns:
  summary: string
  evidence: source_refs[]
  open_questions: string[]
```

Acceptance criteria:

```text
- Every subagent has a role, tools, memory scope, and return contract.
- Read-only subagents cannot write.
- Specialist outputs include evidence, not just opinions.
- Main agent retains responsibility for final synthesis unless handoff is explicit.
```

Coding-agent task:

```text
Add subagents only where there is a real boundary in tools, context, memory, policy, or specialization. Do not replace a clear single-agent loop with a committee of agents.
```

### Phase 8: Add durable execution

Objective: make long-running agents safe to pause, resume, replay, and audit.

Deliverables:

```text
src/agentic/runtime/checkpoints.*
src/agentic/runtime/replay.*
src/agentic/runtime/idempotency.*
docs/durable-execution.md
tests/agentic/checkpoint_replay_cases.*
```

Acceptance criteria:

```text
- Every meaningful step can be checkpointed.
- Replay does not repeat side effects.
- Tool calls have stable IDs.
- External writes use idempotency keys.
- Human approval pauses can resume.
- Checkpoints capture enough state to debug failures.
```

Coding-agent task:

```text
Implement checkpointing around the agent loop. Wrap nondeterministic calls and side effects. Add idempotency keys for external writes. Add replay tests.
```

### Phase 9: Add evals and traces

Objective: measure whether the system behaves agentically and safely.

Deliverables:

```text
.agentic/eval_matrix.yaml
src/agentic/evals/*
tests/agentic/*
traces/schema.*
docs/evals.md
```

Eval matrix example:

```yaml
cases:
  - id: tool_choice_memory_needed
    task: "User refers to prior project decision without naming the file."
    expected:
      - calls_tool: memory_search
      - does_not_call: file_write
      - final_answer_cites_memory: true

  - id: avoid_keyword_router
    task: "Ask about a company using indirect wording."
    expected:
      - no_keyword_intent_router: true
      - semantic_interpretation: true

  - id: side_effect_requires_approval
    task: "Send the final memo to the LP list."
    expected:
      - calls_tool: request_human_approval
      - does_not_call_before_approval: send_email

  - id: compaction_preserves_constraint
    task: "Long session with budget and no-external-send constraint."
    expected:
      - constraint_survives_compaction: true
```

Trace schema should capture:

```text
context items included
tool summaries shown
skill summaries shown
memory ids retrieved
action chosen
tool args
tool result
state diff
approval status
checkpoint id
evaluator result
```

Acceptance criteria:

```text
- Evals test behavior, not only syntax.
- Evals include negative cases.
- Traces make failures debuggable.
- CI can run a cheap subset of evals.
- More expensive evals can run nightly or before release.
```

Coding-agent task:

```text
Add behavior evals and trace schema. Cover tool choice, memory retrieval, compaction, side-effect approval, failure recovery, and stop conditions.
```

### Phase 10: Replace brittle orchestration incrementally

Objective: migrate from fake-agent deterministic branches to harness-mediated adaptive behavior.

Migration pattern:

```text
1. Identify a brittle branch.
2. Ask whether it is genuinely deterministic.
3. If yes, keep it and test it as workflow.
4. If no, convert it into tool, skill, memory, context, or model-policy behavior.
5. Add evals proving the new behavior handles paraphrases and unexpected observations.
```

Examples:

```text
regex intent router
-> model action selection + tool-choice evals

append-only memory file
-> memory_write_candidate + promotion/refutation policy

giant always-loaded prompt
-> context engine + skill loading + retrieval

one huge general agent
-> main agent + bounded subagents where tools/context differ

silent exception fallback
-> structured observation + recovery policy + trace
```

Acceptance criteria:

```text
- Each migration reduces brittleness or improves observability.
- Deterministic workflows remain deterministic where appropriate.
- Agentic decisions become model-owned but harness-constrained.
- Evals cover old failure modes.
```

Coding-agent task:

```text
Choose one brittle orchestration path. Refactor it into the correct layer: deterministic workflow, tool, skill, memory, context policy, model action, subagent, or guardrail. Add tests/evals that would have failed before.
```

---

## 8. Decision table: where to put intelligence

| Problem | Wrong default | Correct layer |
|---|---|---|
| User intent is ambiguous | Keyword router | Model action selection with evals |
| Tool list is too large | Dump all tools into prompt | Tool search and progressive schema loading |
| Agent forgets important facts | Bigger prompt only | Memory retrieval plus context policy |
| Agent writes bad memories | Append notes file | Candidate/promote/refute memory flow |
| Procedure is reusable | Add special-case branch | Skill package with examples/tests |
| Tool is misused | Prompt warning only | Better tool contract, schema, examples, evals |
| Agent loops | Hope model stops | Step budget, repeated-failure detector, stop actions |
| External write is risky | Let model decide | Human approval gate and idempotency |
| Long task crashes | Restart from scratch | Checkpoints and replay-safe side effects |
| Agent loses constraints after compaction | Bigger window | Compaction tests and preserved state schema |
| Source lanes disagree | Pick whichever result arrived last | Source authority matrix plus conflict report |
| Identity is ambiguous | Promote a new entity immediately | Resolve aliases/external ids or keep candidate unmerged |
| Noisy channel has useful ideas | Ingest every message as truth | Separate idea lane with promotion rules |
| Sidecar looks promising | Treat it as canonical | Adoption state, shadow evals, and reviewed promotion |
| Agent over-notifies humans | More prompt warnings | Attention budget and notification gate |
| Main agent context bloats | Add more prompt | Subagent, skill, context packet, or topic-doc boundary |
| CLI is used by agents | Human-only prompts/tables | Non-interactive, JSON, dry-run/idempotency, bounded output, introspection |
| Codebase grows | More root instructions | Topic docs or knowledge graph plus small contract-shaped files |
| Agent behavior should improve | Read traces manually | Trace + feedback + eval fixture + guarded rollout |

---

## 8A. Agentic coding work loop

For substantial agentic-system changes, use a bounded loop instead of a single draft:

```text
goal -> context packet -> architecture brief -> implementation slice -> critique -> verification -> integrate or stop
```

The architecture brief should identify the selected pattern(s), why a simpler deterministic workflow is insufficient, which decisions remain model-owned, which boundaries are deterministic harness responsibilities, and which files/slices can be edited independently.

Critique against the harness, not against vibes:

1. Did the change preserve deterministic harness / adaptive policy boundaries?
2. Did it add a keyword router, regex semantic guess, giant prompt, or hidden fallback?
3. Are tool, CLI, and file interfaces typed and machine-readable?
4. Can another agent safely work on an adjacent slice without touching the same surface?
5. Are source/truth/memory/write paths classified?
6. Are tests/evals tied to a real incident, trace, or realistic fixture?
7. What proof layer is still missing?

Stop when acceptance evidence passes, budget is exhausted, required information is missing, approval is required, or repeated failures show the plan needs human/integrator review.

---

## 9. Anti-patterns coding agents must avoid

### 9.1 Regex pretending to be intelligence

Bad:

```python
if re.search("memo|investment|deal", user_input):
    run_deal_memo_flow()
```

Better:

```text
Expose tools and skills:
- memory_search
- company_lookup
- retrieve_prior_notes
- load_skill("investment_memo")
- run_eval("memo_completeness")

Let the model choose, then validate through the harness.
```

### 9.2 Giant prompt as architecture

Bad:

```text
Put every rule, memory, tool schema, example, transcript, and file into the system prompt.
```

Better:

```text
Short root instructions + context engine + memory search + skill loading + source ledger.
```

### 9.3 Memory as append-only notes

Bad:

```python
with open("memory.txt", "a") as f:
    f.write(model_summary)
```

Better:

```text
memory_write_candidate(claim, scope, evidence, confidence, sensitivity)
then promote/refute/supersede under policy.
```

### 9.4 Tools without semantic affordances

Bad:

```text
Tool: run(query: string)
Description: Executes query.
```

Better:

```text
Tool: search_company_memory
Description: Searches durable company-specific memory by semantic query and filters.
When to use: prior deal notes, company facts, investment history, IC decisions.
When not to use: public market data, current news, facts already present in context.
```

### 9.5 Multi-agent theater

Bad:

```text
Create CEO agent, CTO agent, CFO agent, analyst agent, critic agent, synthesizer agent for every task.
```

Better:

```text
Start single-agent. Add subagents only for separate tools, context, memory, policy, specialization, or parallelism.
```

### 9.6 Source-of-truth collapse

Bad:

```text
Treat the wiki, vector index, source database, sidecar output, and chat summary as interchangeable memory.
```

Better:

```text
Declare each artifact role: raw source, structured truth, retrieval index, synthesis, sidecar, candidate signal, or outbound report. Evaluate conflicts and promotion explicitly.
```

### 9.7 Noisy-lane contamination

Bad:

```text
Compile brainstorming, jokes, speculative notes, and raw chat into promoted project truth.
```

Better:

```text
Route noisy lanes into digests, thesis candidates, roadmap candidates, experiments, or review queues. Promote only with evidence and authority.
```

### 9.8 Accidental production promotion

Bad:

```text
A sidecar or new model path passes one demo, so future agents treat it as canonical.
```

Better:

```text
Track adoption state. Promote only after contracts, shadow runs, evals, health checks, rollback, and owner review.
```

### 9.9 Mega-file bottleneck

Bad:

```text
Keep unrelated harness, prompt, tool, adapter, and eval logic in one large file because it is convenient for one human to browse.
```

Better:

```text
Split at stable contracts: deterministic harness, model policy wrapper, tool schema, prompt/rubric, side-effect adapter, eval fixture, and tests. Give parallel agents disjoint write sets and a named integrator for shared contracts.
```

### 9.10 Interactive-only CLI

Bad:

```text
A coding agent calls a CLI that waits for a TTY prompt, emits only colored tables, returns vague errors, or duplicates side effects on retry.
```

Better:

```text
Agent-native CLI: non-interactive flags, uniform JSON, bounded output, typed exit codes, dry-run/idempotency, async wait/job ledger, machine-readable introspection, and explicit local/prod target reporting.
```

### 9.11 Self-judgment as verification

Bad:

```text
The same agent that wrote the change says it looks correct and treats that as proof.
```

Better:

```text
Use tests, evals, traces, fixtures, diff inspection, or a separate critique artifact. Self-reflection can find issues, but external evidence decides readiness.
```

---

## 10. Canonical coding-agent prompt for agentic changes

Use this prompt when assigning Codex, Claude Code, or another coding agent an agentic-system task:

```text
You are editing an agentic system. First read AGENTS.md, CLAUDE.md if present, and these docs:

- docs/agentic-coding-for-agentic-systems.md
- docs/agentic-systems-engineering.md
- docs/agentic-pattern-catalog.md
- docs/tool-design.md
- docs/memory-architecture.md
- docs/context-engineering.md
- docs/evals.md

Before coding, produce a short architecture brief:

1. Component classification and selected agentic pattern(s), including why a simpler deterministic workflow is insufficient.
2. Which decisions should be model-owned.
3. Which responsibilities belong to the deterministic harness.
4. Which tools the agent has and which tools it ought to have.
5. Which skills should exist or be loaded.
6. Which memories should be searched, written, promoted, or avoided.
7. How context should be assembled and compacted.
8. What state, checkpointing, replay, and approval gates are required.
9. Which tests/evals will prove this is not brittle deterministic orchestration.
10. What observable system acceptance test defines done, and which manual-proof gaps remain.
11. What backpressure, budget, fallback, adoption-state, and rollback rules apply.
12. Which files/slices you own, which shared contracts need an integrator, and how the repo shape supports parallel agents.
13. Whether any CLI/tool surfaces must become agent-native: non-interactive, JSON, bounded, dry-run/idempotent, introspectable, and recoverable.

Do not implement ambiguous agent behavior with keyword routing, regex intent detection, lookup tables, fixed branches, or giant always-loaded prompts unless you explicitly justify why the task is deterministic.

Implement deterministic harness controls for safety, schemas, permissions, idempotency, checkpoints, traces, and evals. Implement adaptive behavior through the model policy layer with the right tools, memory, skills, and context.
```

---

## 11. First engineering tasks

If starting from an ordinary codebase, do these in order:

1. Add `AGENTS.md`, `CLAUDE.md`, and the docs pack.
2. Inventory current agent entry points, tools, memory, context, source lanes, identity resolution, coordination, and evals.
3. Add a tool contract schema and tool catalog.
4. Wrap tool execution with permissions, side-effect classes, idempotency, and traces.
5. Add a context engine with source ledger and budget policy.
6. Implement memory candidates with provenance and promotion/refutation.
7. Add a source-authority matrix and identity-resolution contract.
8. Add attention and notification gates for chat, email, meetings, and alerts.
9. Add initial skills for tool design, memory design, source-lane design, context design, eval design, and architecture review.
10. Refactor the agent loop so model-owned action choice is distinct from deterministic execution.
11. Add checkpointing and replay-safe side-effect handling.
12. Add evals covering tool choice, memory retrieval, source conflicts, identity resolution, compaction, human approval, attention behavior, failure recovery, and stop conditions.

Do not begin by building a large multi-agent hierarchy. Begin by building a better harness.

---

## 12. Field lessons from live agentic operating systems

The architecture above is deliberately general. These operating lessons are also general, but they come from the kind of failures that only appear once agents run continuously, talk to each other, use real tools, spend real budget, and affect real users.

Do not import local nouns from another system. Import the contract.

### 12.1 Define done as system behavior

For autonomous systems, a task is not done because an engineer or coding agent manually walked one item through the happy path. Manual intervention is debugging evidence. It proves the system can work when operated by a human; it does not prove the system works.

Before implementation, write the acceptance test in system terms:

```text
Bad: publish one item.
Good: three untouched items move from intake to published through the autonomous pipeline within the agreed window, visible in the user-facing surface, with trace evidence and no manual state edits.
```

Final reports should distinguish:

```text
manual proof obtained
system/autonomous proof obtained
known gaps and untested layers
```

If the goal is autonomous behavior and only manual proof exists, the change is partially verified, not done.

### 12.2 Incidents should become contracts, not folklore

A production incident is valuable only if it turns into an architectural artifact. Do not leave lessons as “remember not to do that.” Translate the incident into:

1. the layer that failed,
2. the contract that was missing or unenforced,
3. a fixture, replay, eval, or audit that preserves the case,
4. the owner of the follow-up,
5. the rollback or kill-switch path.

A recurring failure pattern should produce a falsifiable model of the system, not another patch note. Map parent workflows, dispatchers, work children, tools, providers, state transitions, and user-visible outputs as a graph of assumptions. Ask at every edge: is this contract enforced or merely hoped for?

### 12.3 Backpressure and cost are harness responsibilities

Agents make calls, but the harness owns admission control. Long-running agent systems need caller attribution, per-caller budgets, queue or refuse behavior, lockout handling, provider-health signals, and retry policy in one place.

Never let each layer independently decide to retry, rerun, spawn, or spill over. That produces multiplicative storms: cron retries the parent, parent retries the dispatcher, dispatcher respawns children, children retry tools, tools retry providers. A single upstream outage becomes a self-amplifying workload.

Cost is also a safety boundary. Paid provider fallback, model spillover, high-volume probes, and external sends require explicit policy, audit logs, and operator approval. A fallback that silently spends money is not resilience; it is an unreviewed side effect.

### 12.4 Claims must reconcile with state

Natural-language agent claims are not state transitions. If an agent says it accepted, assigned, published, approved, paid, emailed, deployed, or deleted something, the harness should be able to verify the corresponding state write or side-effect receipt.

The right design is not a brittle keyword detector over chat text. The right design is a protocol boundary: explicit commands, state transition records, side-effect receipts, reconciliation jobs, mismatch boards, and model-assisted adjudication where language is genuinely ambiguous.

A live operating system needs to answer: what did the agent claim, what changed in state, who owns the mismatch, and how old is it?

### 12.5 Keep thesis, current state, and truth separate

Agentic systems often carry aspirational documents: strategy, roadmap, north star, desired persona, or future operating model. Those are useful, but they are not evidence that the system currently behaves that way.

Mark artifacts by role:

```text
thesis / desired future
current operating truth
raw evidence
structured truth
retrieval index
synthesis
candidate idea
sidecar output
```

Coding agents should not implement against the aspiration while ignoring the current state. Conversely, they should not delete the aspiration because current behavior falls short. Use the gap as a roadmap.

### 12.6 Promote through adoption states

A new model path, source lane, sidecar agent, routing policy, or workflow should move through explicit adoption states: reference-only, shadow, read-only, candidate-write, write-enabled, canonical, deprecated, retired.

One good demo is not production evidence. Require contracts, shadow runs, evals, health checks, rollback, and owner review before promotion. Cheap experiments are good; accidental promotion is not.

### 12.7 Human attention is a scarce system resource

Human review is not free. Agentic operating systems need attention budgets and notification gates just as much as token budgets. Interrupt for irreversible actions, degraded autonomy, unresolved contradictions, meaningful uncertainty, or decisions where human taste/authority is the product. Do not interrupt because a prompt said “keep the user updated.”

A good attention gate asks:

```text
Is this actionable now?
Does the human have unique authority here?
Will delay make the outcome materially worse?
Can the system continue safely without interrupting?
```

### 12.8 The coding agent is part of the operating system

Coding agents are not outside observers. Their edits, session logs, claims, commits, evals, and summaries become part of the system’s memory and coordination surface. That means they need the same discipline they are adding to runtime agents: explicit ownership, no orphan sweeps, no silent assumption changes, tests tied to real incidents, and final handoffs that say what remains unproven.

For agentic coding, the meta-rule is simple:

```text
Do not merely add intelligence.
Add the harness that lets intelligence act safely, learn honestly, and prove it worked.
```

---

## 13. The final mental model

The best near-term agentic systems will not be pure neural mush and will not be ordinary deterministic workflows. They will be hybrids:

```text
Models handle ambiguity.
Harnesses handle reliability.
Tools expose affordances.
Skills package procedures.
Memory preserves useful experience.
Source authority decides what can be trusted.
Identity resolution prevents bad joins from poisoning truth.
Synthesis makes truth usable without replacing it.
Context engines decide what is visible now.
Attention policy decides when humans should be interrupted.
Evals reveal whether the behavior is actually improving.
```

Coding agents need to be oriented to that hybrid architecture every time they work in the repo. Otherwise they will default to the architecture they know best: deterministic control flow with superficial model calls attached.

The goal is not to make the code “more AI-shaped.” The goal is to put intelligence in the places where judgment is required and put deterministic controls around the places where reliability is required.

For long-lived operating systems, use this chain as the north-star architecture:

```text
source -> identity -> claim -> authority -> contradiction -> synthesis -> action -> follow-up -> learning
```

If a coding agent cannot point to where a change fits in that chain, it probably has not understood the operating system yet.

That is the engineering discipline of agentic systems.

---

## 14. Public source anchors for further reading

These are the public materials this architecture pack is designed to align with:

- Anthropic, “Building Effective Agents” — workflows vs agents, orchestration patterns, when to use agents.
- Anthropic, “Effective Context Engineering for AI Agents” — just-in-time context loading, context as engineering surface.
- Anthropic, “Writing Effective Tools for Agents” — tool definitions as the contract between deterministic systems and nondeterministic agents.
- Anthropic / Claude Code docs — memory, CLAUDE.md, skills, subagents, hooks, MCP.
- OpenAI Codex docs — AGENTS.md as repo-level coding-agent instruction surface.
- OpenAI, “A Practical Guide to Building Agents” — tools, orchestration, guardrails, single-agent-first design.
- OpenAI Agents SDK docs — handoffs and agent-as-tool patterns.
- LangGraph / LangChain docs — memory, persistence, durable execution, checkpointing, stores.
- OpenClaw public docs — agent loop, workspace, tools/plugins/skills, memory, context engine, hooks.
- Pydantic AI docs — typed agents, tools, structured outputs, evals, durable agents.
- “Lost in the Middle” and Chroma’s “Context Rot” work — empirical limits of long-context reliability.
- Rich Sutton, “The Bitter Lesson” — scaling general methods and avoiding overfit hand-engineering.
