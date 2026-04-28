# Engineering Agentic Systems: Orientation for Codex, Claude Code, and Other Coding Agents

Version: 2.0

Purpose: this document is a standing architectural instruction for coding agents working on agentic systems. It exists because coding models often default to ordinary application architecture: fixed control flow, keyword routers, regex parsing, deterministic lookup tables, and brittle orchestration. Those patterns are useful inside the harness, but they are wrong when used as substitutes for the adaptive reasoning layer of an agentic system.

Place this file at:

```text
docs/agentic-systems-engineering.md
```

Then reference it from `AGENTS.md`, `CLAUDE.md`, and pull request templates.

---

## 1. Non-negotiable premise

This repository builds agentic systems.

Do not implement open-ended agent behavior as a brittle deterministic workflow unless the task is genuinely closed-form and tested as such.

The core rule is:

```text
Deterministic harness. Adaptive policy.
```

Use deterministic code for the harness:

- typed schemas
- validation
- permission checks
- human approval gates
- idempotency
- rate limits
- cost and step budgets
- persistence and checkpoints
- concurrency controls
- audit logs and traces
- tool execution boundaries
- memory APIs and memory provenance
- tests and eval harnesses
- safety and compliance policies

Use model-driven or agent-driven behavior for the policy:

- deciding which context is relevant
- deciding which tool to call next
- interpreting ambiguous user intent
- decomposing tasks when the path is not known in advance
- revising a plan after observations
- choosing when to ask a human
- synthesizing evidence from multiple sources
- recovering from failed tools or partial information
- deciding whether memory should be searched, written, or updated
- deciding when a reusable skill applies

A good agentic system is not “less deterministic.” It is deterministic in the places that must be reliable and adaptive in the places where the environment, task, or information path cannot be known ahead of time.

---

## 2. The failure mode this document prevents

Coding agents trained on conventional code often implement systems like this:

```text
user input -> regex/keyword router -> fixed branch -> fixed tool call -> fixed response
```

That is ordinary orchestration. It may be correct for a narrow workflow, but it is not an agentic harness.

Common bad substitutions:

| Intended agentic behavior | Brittle implementation to avoid |
|---|---|
| Interpret a user goal using available context | Regex or keyword matching over the prompt |
| Choose among tools based on task state | Hardcoded `if "calendar" in text` routing |
| Decide what to retrieve | Always dump all documents into the prompt |
| Maintain durable user/project knowledge | Append random facts to a text file without evidence or scope |
| Recover from tool failure | Catch all exceptions and silently continue |
| Ask for approval before a risky side effect | Execute write/delete/send immediately |
| Learn a reusable procedure | Add another special-case branch |
| Delegate to specialist behavior | Add one more giant prompt and tool list to the main agent |
| Evaluate quality | Check only that code compiles |

The correct implementation looks more like this:

```text
intake
-> authorize and normalize
-> assemble bounded context
-> discover relevant tools and skills
-> retrieve relevant memory
-> model decides next action
-> execute tool through deterministic harness
-> observe result
-> update state/checkpoint/trace
-> repeat until stop condition
-> validate result
-> ask human where required
-> persist selected memory
-> return answer/artifact
```

The model is not “magic.” The harness gives it the right affordances, context, memory, and constraints.

---

## 3. Vocabulary

Use these terms precisely.

### Deterministic workflow

A workflow is a predefined sequence or graph of steps. It is correct when the path is known in advance.

Examples:

- parse invoice -> validate fields -> create accounting record
- run formatter -> run tests -> open pull request
- collect structured inputs -> call fixed API -> render output

Workflows are good when correctness depends on predictable control flow.

### Augmented LLM

An augmented LLM is a model call with tools, retrieval, structured output, or memory. It may not own a long action loop.

Use this when one or a few model calls are enough and the task does not require extended autonomous exploration.

### Agent loop

An agent loop lets the model choose actions over time:

```text
observe -> think/plan -> act -> observe -> revise -> act -> stop
```

Use this when the next step depends on the result of the previous step and cannot be predetermined.

### Agentic harness

The harness is the runtime around the model. It is not the model itself.

It includes:

- context assembly
- tool registry and tool search
- skill discovery and skill loading
- memory search, promotion, and persistence
- model invocation
- tool execution
- permission checks
- state management
- durable checkpoints
- compaction
- retries
- hooks
- traces
- evals
- human checkpoints
- artifact persistence

Most production failures in agentic systems are harness failures, not model failures. A second class of failures comes from operating-model collapse: the system treats raw evidence, retrieval indexes, synthesis pages, sidecar outputs, candidate signals, and source-of-truth records as if they had the same authority.

### Skill

A skill is a reusable package of procedural knowledge for an agent. It usually contains a `SKILL.md` instruction file plus optional scripts, reference files, examples, templates, tests, or fixtures.

Skills are for reusable “how to do this kind of work here” knowledge. They are not just prompts.

### Tool

A tool is an affordance exposed to the agent so it can inspect or change the world. Tools must be typed, documented, permissioned, observable, and bounded.

A tool can read, search, compute, transform, write, approve, verify, or delegate.

### Memory

Memory is persisted information outside the immediate context window.

Context is what is currently in the model prompt. Memory is what can be retrieved, inspected, updated, or promoted across steps, sessions, users, projects, or agents.

Do not confuse memory with dumping more text into the prompt.

---

## 4. Component classification before coding

Before editing agent behavior, classify the component you are touching.

Use one primary category and any secondary categories that apply.

1. Deterministic workflow
2. Augmented LLM
3. Agent loop
4. Multi-agent or subagent system
5. Tool or tool registry
6. Skill
7. Memory subsystem
8. Source lane or source authority layer
9. Identity resolution layer
10. Context engine
11. Durable execution layer
12. Guardrail, permission, or human-review layer
13. Cross-agent coordination layer
14. Attention or notification policy
15. Adoption-state change
16. Evals and observability
17. Product/user interface around an agent

Then state:

```text
Model-owned decisions:
Deterministic harness responsibilities:
Tools the agent currently has:
Tools the agent ought to have:
Memories available:
Skills available:
State/durability requirements:
Human-review requirements:
Backpressure/budget/fallback requirements:
Adoption state and rollback:
System acceptance test:
Tests/evals to add or update:
Known proof gaps:
```

Do this before writing code.

---

## 5. When to use which architecture

### Use a deterministic workflow when

- the path is known in advance
- all branches are enumerable
- the input format is constrained
- correctness depends on exact order and validation
- a model is only needed for extraction, classification, or summarization inside a fixed process

Example: a KYC document pipeline with fixed steps and clear rejection states.

### Use an augmented LLM when

- the task needs language understanding or synthesis
- one model call or a small number of calls is enough
- tool use is simple and bounded
- there is no need for autonomous multi-step exploration

Example: summarize a meeting transcript and produce action items with a structured schema.

### Use an agent loop when

- the model must decide what to inspect next
- tools may fail or return partial information
- the task requires iterative search, coding, research, debugging, negotiation, or planning
- the final path cannot be known before runtime

Example: investigate why an integration test is failing across several services.

### Use orchestrator-workers when

- the top-level task can be decomposed dynamically
- the number or shape of subtasks is unknown upfront
- different subtasks can be solved independently and synthesized later

Example: research a market by splitting into regulations, competitors, technical papers, patents, and customer workflows.

### Use subagents when

- context isolation matters
- the specialist needs different tools
- the specialist needs different instructions or safety policy
- the specialist needs its own memory scope
- the main agent should not absorb all intermediate detail

Example: a security-review subagent with read-only code access and a separate memory file.

### Use a skill when

- the same multi-step procedure is used repeatedly
- domain-specific conventions matter
- the agent needs examples, scripts, templates, or reference docs
- the procedure is too long for always-loaded instructions
- you want progressive disclosure rather than prompt bloat

Example: “how to add a new Stripe webhook handler in this repo.”

### Use durable execution when

- the run may last a long time
- a human may interrupt or approve later
- side effects must not be duplicated on retry
- the process must survive crashes
- replay or auditability matters

Example: an agent that modifies production configuration after human approval.

---

## 6. Agentic harness anatomy

An agentic harness is the system that turns a model into a reliable actor.

A minimal production-grade harness has these layers.

### 6.1 Intake layer

Responsibilities:

- receive the user or system goal
- normalize the request
- identify user, workspace, project, and session
- attach policy context
- reject impossible or disallowed requests early
- create a run ID

Do not let the model execute tools before the run has identity, scope, policy, and trace metadata.

### 6.2 Context engine

Responsibilities:

- assemble the current prompt/context
- include stable instructions
- include only relevant workspace files
- include only relevant memory
- include tool and skill metadata
- manage token budget
- compact or prune history when needed
- preserve tool-call/result pairs when summarizing
- make context inspectable for debugging

The context engine is not a giant string concatenator. It is an explicit subsystem.

It should answer:

```text
What was included?
Why was it included?
How many tokens did it cost?
What was excluded?
What can be loaded later if needed?
```

### 6.3 Tool registry and discovery

Responsibilities:

- register tools with names, descriptions, schemas, permissions, examples, and result formats
- expose a small hot set of commonly used tools
- allow search/discovery for less common tools
- group tools into namespaces
- hide irrelevant tools to reduce context bloat
- enforce permission and policy at execution time
- record every tool call and result

The agent must know both:

```text
Tools it has.
Tools it ought to have.
```

If the right tool does not exist, the correct action may be to implement it, request it, or design its interface. Do not fake the missing capability with regex or brittle prompt logic.

### 6.4 Skill registry

Responsibilities:

- expose skill names and descriptions as lightweight metadata
- load full skill instructions only when relevant
- keep supporting files out of context until requested
- support scripts and deterministic helpers inside skills
- version skills
- evaluate skill invocation quality
- audit skills for security and prompt injection

A skill is a just-in-time procedure pack.

### 6.5 Memory subsystem

Responsibilities:

- store durable facts, decisions, preferences, observations, and procedures
- separate short-term state from long-term memory
- support search and retrieval
- preserve provenance and timestamps
- track scope: user, project, organization, workspace, agent, session
- track confidence and staleness
- reconcile contradictions
- expose memory reads and writes as tools
- promote only selected information into durable memory

Do not let agents write arbitrary memory without provenance.

### 6.6 Model policy layer

Responsibilities:

- choose next action
- ask for missing context
- select tools
- select skills
- decide whether to delegate
- decide whether to continue or stop
- synthesize answer from observations

The model policy layer should be adaptive. Do not replace it with static routing unless the domain is closed and tested.

### 6.7 Tool execution layer

Responsibilities:

- validate parameters
- enforce permissions
- execute in sandbox or controlled environment
- time out long calls
- retry only when safe
- wrap side effects with idempotency keys
- sanitize outputs before returning to the model
- redact secrets
- record traces

Tool execution is deterministic harness territory.

### 6.8 State and durability layer

Responsibilities:

- checkpoint after model and tool steps
- persist run state
- resume after interruption
- avoid duplicate side effects on replay
- separate deterministic replayable steps from non-deterministic external calls
- support human-in-the-loop pauses

If the system can send, delete, pay, update, deploy, or book, durable execution is not optional.

### 6.9 Guardrail and human-review layer

Responsibilities:

- define safe, review, and prohibited operations
- require approval before irreversible or external side effects
- block unsafe shell commands or writes
- require confirmation for spend, sends, deletes, legal commitments, production changes, and data exfiltration
- validate final outputs against policy and schema

Use hooks and permission gates for deterministic enforcement. Do not rely on the model to remember every policy in every step.

### 6.10 Observability and eval layer

Responsibilities:

- log run IDs, model settings, prompts, context sources, tool schemas, tool calls, tool results, memory reads/writes, approvals, cost, latency, and final outputs
- support trace inspection
- support offline evals on datasets
- support online evals on production traces
- measure tool choice, task success, safety, latency, cost, and user correction rate

Agentic quality is not “the code runs.” It is whether the agent chooses the right actions under realistic ambiguity.

---

## 7. The agent run loop

A typical harness loop should look like this conceptually:

```python
def run_agent(goal, user, workspace, session):
    run = create_run(goal=goal, user=user, workspace=workspace, session=session)

    authorize_run(run)
    state = load_or_create_state(session)

    while not state.done:
        context = context_engine.assemble(
            run=run,
            state=state,
            relevant_memories=memory.search_if_needed(state),
            relevant_skills=skills.search_if_needed(state),
            available_tools=tools.visible_for(run, state),
        )

        decision = model.decide(context)
        trace.record_decision(run, decision)

        if decision.type == "final":
            result = validate_final(decision.content)
            state.done = True
            break

        if decision.type == "ask_human":
            checkpoint(state)
            return pause_for_human(decision.question)

        if decision.type == "tool_call":
            tool = tools.resolve(decision.tool_name)
            permission = permissions.check(tool, decision.args, run)

            if permission.requires_approval:
                checkpoint(state)
                return pause_for_approval(tool, decision.args)

            result = tool_executor.execute(
                tool=tool,
                args=decision.args,
                idempotency_key=state.next_idempotency_key(),
                sandbox=tool.sandbox_policy,
                timeout=tool.timeout,
            )

            state.observe(result)
            checkpoint(state)
            continue

        raise InvalidDecision(decision)

    memory.promote_selected_learnings(run, state)
    trace.finish(run, result)
    return result
```

This pseudocode is deliberately not a fixed workflow for the task. The loop is deterministic; the next action is adaptive.

---

## 8. Tool design

Tools are the agent’s hands, eyes, and instruments. Bad tools create bad agents.

### 8.1 Every tool must have a contract

Each tool should specify:

```yaml
name: memory_search
description: Search durable memory for relevant facts, decisions, preferences, and prior observations.
category: memory
when_to_use:
  - The agent needs information that may have been learned in a previous session.
  - The agent needs project/user/org preferences.
  - The agent needs prior decisions or known constraints.
when_not_to_use:
  - The information is already present in the current context.
  - The task requires fresh external facts rather than stored memory.
input_schema:
  query: string
  scope: enum[user, project, org, workspace, agent]
  max_results: integer
  recency_filter: optional string
output_schema:
  results:
    - memory_id: string
      claim: string
      evidence: string
      source: string
      scope: string
      confidence: number
      updated_at: datetime
side_effects: none
permission_level: read
idempotent: true
latency_expectation: low
cost_expectation: low
failure_modes:
  - stale memories
  - missing memories
  - contradictory memories
examples:
  - input: {query: "preferred evaluation framework", scope: "project", max_results: 5}
    output: "returns prior decisions about LangSmith/Pydantic evals"
```

Do not define tools with vague names like:

```text
do_task
handle_request
process_input
agent_helper
smart_router
```

Good tool names are specific:

```text
search_code
read_file
apply_patch
run_tests
search_memory
write_memory_candidate
request_human_approval
send_email_after_approval
search_tools
load_skill
create_checkpoint
resume_run
```

### 8.2 Tool categories

An agentic system normally needs these categories.

#### Read/sensing tools

Examples:

- read file
- search code
- search documents
- web search
- database read
- inspect calendar
- inspect email
- inspect logs
- inspect feature flags
- inspect context budget

These tools do not change the world.

#### Compute/transformation tools

Examples:

- run code in sandbox
- parse document
- extract tables
- validate schema
- generate embedding
- transform file
- summarize transcript
- calculate metrics

These may be deterministic or model-assisted, but should be bounded and observable.

#### Write/side-effect tools

Examples:

- send email
- create calendar event
- update database
- merge pull request
- deploy service
- delete file
- charge payment method
- publish post

These require stronger permissions, idempotency, audit logs, and often human approval.

#### Meta-tools

Examples:

- search available tools
- inspect tool schema
- load skill
- search memory
- inspect context
- request approval
- create checkpoint
- spawn subagent

Meta-tools are critical. Without them, the agent must guess what it can do.

#### Verification tools

Examples:

- run unit tests
- run integration tests
- lint
- typecheck
- compare output to golden dataset
- run safety evaluator
- run citation checker
- inspect diff

Verification tools close the loop between acting and knowing whether the action worked.

### 8.3 Tools the agent probably ought to have

If this repository builds agents, coding agents should inspect or create interfaces for these tools where relevant:

```text
list_available_tools()
search_tools(query, namespace=None)
inspect_tool_schema(tool_name)
load_skill(skill_name)
search_skills(query)
inspect_context_budget()
summarize_context_for_compaction()
search_memory(query, scope, max_results)
get_memory(memory_id)
write_memory_candidate(claim, evidence, scope, confidence, ttl)
promote_memory(candidate_id)
refute_or_update_memory(memory_id, evidence)
checkpoint_run(run_id, state)
resume_run(run_id)
request_human_approval(action, risk, proposed_args)
run_tests(selector)
run_eval_suite(name)
emit_trace_event(event_type, payload)
spawn_subagent(role, task, allowed_tools, memory_scope)
```

A missing tool is an architectural fact. Do not patch around missing affordances with hardcoded assumptions.

### 8.4 Tool discovery and context bloat

Do not load every tool schema into every prompt if the tool set is large.

Preferred pattern:

1. Always expose a small hot set of tools.
2. Expose tool categories and a tool-search tool.
3. Load detailed schemas only for likely relevant tools.
4. Group tools into namespaces.
5. Keep namespace sizes small enough that the model can reason over them.
6. Use examples for high-error tools, especially tools with nested parameters.

The agent should know that more tools exist, without paying the full context cost of every schema.

### 8.5 Side-effect tools

Any tool that changes the world must define:

```yaml
side_effect_type: none | local_file | external_message | database_write | money | production | irreversible
approval_required: true | false
idempotency_key_required: true | false
undo_strategy: none | compensating_action | reversible | manual
risk_level: low | medium | high | critical
```

Default to approval for:

- sending external messages
- deleting or overwriting data
- spending money
- production changes
- user-visible publication
- legal commitments
- permission changes
- data export

### 8.6 Tool result design

Tool outputs should be concise, structured, and evidence-preserving.

Bad result:

```text
Success.
```

Better result:

```json
{
  "status": "success",
  "changed_files": ["src/agent/tools.py"],
  "summary": "Added memory_search tool with typed schema.",
  "warnings": [],
  "trace_id": "run_abc123:tool_004"
}
```

Bad search result:

```text
Lots of text pasted from documents...
```

Better search result:

```json
{
  "results": [
    {
      "source_id": "doc_17",
      "title": "Tool Design Guide",
      "section": "Permissioning",
      "snippet": "External sends require approval...",
      "score": 0.87,
      "updated_at": "2026-03-12"
    }
  ]
}
```

Keep evidence addressable. Do not force the model to parse giant blobs.

---

## 9. Skills

Skills are how agents acquire reusable procedural knowledge without bloating the always-loaded prompt.

A skill is appropriate when the agent needs to know “how we do this kind of thing here.”

### 9.1 Skill anatomy

A typical skill directory:

```text
.skills/
  add-agent-tool/
    SKILL.md
    examples.md
    tool_contract_template.yaml
    scripts/
      validate_tool_schema.py
    evals/
      cases.yaml
```

`SKILL.md` should be short enough to load into context when needed. Large details should be split into supporting files.

### 9.2 `SKILL.md` template

```md
---
name: add-agent-tool
description: Use when adding, modifying, or reviewing a tool exposed to an agent. Covers tool contracts, schemas, permissions, result formats, tracing, and evals.
---

# Add Agent Tool Skill

## When to use

Use this skill when the task involves adding or changing an agent tool, MCP tool, function tool, plugin tool, or tool wrapper.

Do not use this skill for ordinary internal helper functions that are not exposed to agents.

## Goal

Add a tool that is easy for an agent to discover, safe to execute, typed, observable, and testable.

## Procedure

1. Identify the user-facing capability the agent needs.
2. Decide whether this should be a tool, skill, memory operation, deterministic workflow, or subagent.
3. Write the tool contract before implementation.
4. Define input and output schemas.
5. Define permission level and side-effect class.
6. Add idempotency if the tool has side effects.
7. Add tracing and structured errors.
8. Add examples for ambiguous parameters.
9. Add tests for validation, permissions, failure modes, and result shape.
10. Add or update evals for tool selection.

## Tool contract checklist

- name is specific and verb-oriented
- description says when to use and when not to use
- input schema is narrow and typed
- output schema is structured
- side effects are explicit
- permission gate exists
- idempotency is defined where needed
- timeout is defined
- errors are structured
- examples cover common and edge cases
- traces include run ID and tool call ID

## Common failures

- vague tool name
- broad stringly typed parameters
- silent exception handling
- returning unstructured text blobs
- no permission gate for side effects
- no eval showing that the agent chooses this tool correctly
```

### 9.3 Skill design rules

1. Put always-needed rules in `AGENTS.md` or `CLAUDE.md`.
2. Put reusable procedures in skills.
3. Put long reference material in supporting files.
4. Put deterministic repetitive operations in scripts.
5. Keep skill descriptions highly specific, because models use descriptions to decide when to load skills.
6. Include negative triggers: when not to use the skill.
7. Include expected outputs.
8. Include validation steps.
9. Include examples.
10. Add eval cases showing that the skill is invoked appropriately.

### 9.4 Skill security

Skills are powerful because they influence agent behavior and may include executable code.

Security requirements:

- audit skills before installation
- treat third-party skills as untrusted until reviewed
- forbid skills from embedding secrets
- require approval before skill scripts perform side effects
- version skills
- track which skill version was active in each run
- test whether a malicious document can trick the model into loading or following the wrong skill

---

## 10. Memory architecture

Memory is not a magic global scratchpad. It is a structured persistence layer for useful information.

### 10.1 Separate context from memory

Context:

- current model input
- limited by context window
- assembled for this turn or run
- should be inspectable
- should be pruned or compacted

Memory:

- persisted outside the current prompt
- retrieved only when relevant
- scoped and permissioned
- has provenance
- may become stale
- may conflict with newer evidence

Never solve memory by dumping all prior conversations into the prompt.

### 10.2 Memory types

#### Working memory

Temporary state inside the current run or session.

Examples:

- current plan
- completed steps
- unresolved questions
- current tool results
- scratchpad summaries

Working memory may be checkpointed but is not necessarily durable long-term knowledge.

#### Episodic memory

Records of events or runs.

Examples:

- “On 2026-04-28, the deployment failed because the migration was missing.”
- “The user rejected proposal A and preferred proposal B.”
- “The agent used tool X and got error Y.”

Episodic memory is useful for audit and later retrieval.

#### Semantic memory

Durable facts, preferences, definitions, and decisions.

Examples:

- “This project uses Pydantic AI for typed agent tools.”
- “Production deploys require two approvals.”
- “The user prefers market maps with source-graded evidence.”

Semantic memory should include source, scope, and confidence.

#### Procedural memory

Reusable know-how.

Examples:

- skills
- runbooks
- templates
- code scripts
- onboarding docs

Procedural memory often belongs in skills rather than a freeform memory file.

### 10.3 Memory scopes

Every memory write must specify scope.

Common scopes:

```text
user
organization
project
workspace
agent
session
run
```

Examples:

- User preference: user scope
- Repo architecture rule: project/workspace scope
- Temporary investigation state: session/run scope
- Specialist agent learning: agent scope
- Company policy: organization scope

Do not write user-specific preferences into global project memory.

### 10.4 Memory write contract

Every durable memory candidate should include:

```yaml
claim: "Production deploys require approval from the on-call engineer."
scope: project
source_type: user_statement | observed_code | document | tool_result | human_approval | external_source
source_ref: "run_2026_04_28/tool_007"
evidence: "deployment_policy.md says..."
confidence: 0.86
created_at: "2026-04-28T18:30:00-07:00"
updated_at: "2026-04-28T18:30:00-07:00"
expires_at: null
staleness_policy: review_on_conflict | review_after_90_days | never_auto_trust
sensitivity: public | internal | confidential | secret
```

Memory without provenance is a liability.

### 10.5 Memory promotion

Not every observation deserves durable memory.

Promote memory when:

- the user explicitly asks you to remember it
- the fact is stable and likely useful later
- it is a project rule or architectural decision
- it affects future tool use or safety
- it explains a recurring failure mode
- it replaces or refutes older memory

Do not promote:

- transient task details
- secrets
- unverified guesses
- stale external facts without expiry
- personal data that is unnecessary
- random intermediate observations

### 10.6 Memory search

Memory search should usually be hybrid:

- keyword for exact names, IDs, paths, and terms
- semantic/vector search for conceptual similarity
- recency filter for time-sensitive facts
- scope filter for permission and relevance

Search results should expose evidence and timestamps, not just conclusions.

### 10.7 Memory contradiction handling

When memory conflicts with current evidence:

1. Do not silently choose one.
2. Surface the conflict.
3. Prefer newer primary evidence when appropriate.
4. Mark the older memory stale or contradicted.
5. Write an updated memory only with evidence.

### 10.8 Memory tools the system should expose

At minimum:

```text
memory_search
memory_get
memory_write_candidate
memory_promote
memory_update
memory_refute
memory_delete_or_forget
memory_audit
```

The agent should not edit durable memory files directly unless the architecture intentionally uses file-backed memory and the edit path is audited.

---

## 11. Context engineering

Context engineering is the discipline of deciding what the model sees now.

### 11.1 Context is scarce

Even with large context windows, uncurated context causes failures:

- important information gets buried
- tool schemas crowd out task facts
- stale memory competes with fresh evidence
- the model overfits irrelevant examples
- cost and latency rise
- compaction destroys key details if not designed carefully

### 11.2 Use progressive disclosure

Load in layers:

1. Stable system/developer instructions
2. Current task and constraints
3. Relevant short-term state
4. Lightweight metadata for tools and skills
5. Retrieved memories with provenance
6. Only the specific files/docs needed
7. Full skill bodies only when selected
8. Tool schemas only when likely relevant
9. Long references only on demand

### 11.3 Make context inspectable

The harness should expose:

```text
/context
/context status
/context detail
/context sources
/context largest
```

or equivalent debug views.

For every run, a developer should be able to answer:

- Which instructions were loaded?
- Which memories were loaded?
- Which tools were visible?
- Which skills were visible?
- Which skill bodies were loaded?
- Which files were injected?
- What was compacted?
- What was excluded?

### 11.4 Compaction

Compaction is not arbitrary summarization.

Good compaction preserves:

- user goal
- constraints
- decisions already made
- unresolved questions
- tool calls and tool results
- file paths and identifiers
- approvals
- errors and failed attempts
- evidence references
- current plan

Bad compaction loses identifiers, merges contradictory facts, omits failed attempts, or converts evidence into unsupported conclusions.

### 11.5 Subagents as context isolation

Use subagents to prevent the main context from absorbing every detail.

A subagent should return:

```text
summary
key evidence
files inspected
tools used
confidence
open questions
recommended next action
```

Do not let subagents become uncontrolled hidden workers. They need constraints, tool limits, traceability, and return schemas.

---

## 12. State, durability, and replay safety

Agentic systems often fail because they treat long-running, side-effecting work like a stateless request-response call.

### 12.1 Checkpoint after every meaningful step

Checkpoint:

- before human approval pause
- after model decision
- before side-effecting tool call
- after side-effecting tool call
- before compaction
- after compaction
- before final answer

### 12.2 Idempotency

Any side-effecting tool should accept or generate an idempotency key.

Example:

```text
send_email(to, subject, body, idempotency_key)
```

If the agent retries after a crash, the harness must know whether the email was already sent.

### 12.3 Replay boundaries

Separate:

- deterministic computation that can be replayed safely
- model calls that may produce different outputs
- external reads that may change over time
- side effects that must not be repeated

Persist results from non-deterministic or external operations when they matter.

### 12.4 Human-in-the-loop pauses

Do not block indefinitely inside an in-memory run waiting for human feedback.

Preferred pattern:

1. checkpoint state
2. emit approval request
3. terminate or pause cleanly
4. resume from checkpoint when approval arrives

### 12.5 Concurrency

Use per-session or per-resource locks when multiple turns may modify the same state.

Protect:

- memory writes
- file edits
- tool side effects
- checkpoints
- conversation state
- run queues

Race conditions in agentic systems create hallucinated state: the model believes one world while the tools mutated another.

---

## 13. Guardrails, permissions, and hooks

The model should not be the only line of defense.

### 13.1 Permission classes

Define permission classes like:

```text
read_only
local_write
external_read
external_write_requires_approval
production_write_requires_approval
money_requires_approval
irreversible_prohibited
```

Every tool belongs to one.

### 13.2 Hooks

Use deterministic hooks around lifecycle events:

```text
before_prompt_build
after_prompt_build
before_model_call
after_model_call
before_tool_call
after_tool_call
before_memory_write
after_memory_write
before_compaction
after_compaction
before_final_output
```

Examples:

- block `rm -rf` in shell tools
- redact secrets from tool results
- require approval before sending email
- log memory writes
- enforce max tool calls
- stop runaway loops
- run evaluator before final output

### 13.3 Stop conditions

Every agent loop needs stop conditions:

- max model calls
- max tool calls
- max cost
- max wall-clock time
- no-progress detector
- repeated tool error detector
- confidence threshold
- user approval required
- final schema satisfied

Unbounded autonomy is a bug.

---

## 14. Multi-agent systems

Do not create multiple agents because it sounds agentic.

Split into multiple agents only when at least one of these is true:

- different tools are needed
- different policies are needed
- different memory scopes are needed
- context isolation is valuable
- parallel investigation is valuable
- specialist evaluation is needed
- ownership or permissions differ

### 14.1 Common patterns

#### Manager with agents-as-tools

The manager remains in control. Specialist agents are invoked like tools and return structured results.

Use when the user should experience one coherent agent.

#### Handoff

One agent transfers control to another specialist.

Use when the specialist should own the next phase of the interaction.

#### Orchestrator-workers

A top-level orchestrator dynamically decomposes the task and assigns workers.

Use when subtask shape is unknown upfront.

#### Evaluator-optimizer

One component generates; another evaluates; feedback loops until quality threshold or budget limit.

Use when quality criteria are clear enough to evaluate.

### 14.2 Multi-agent anti-patterns

Avoid:

- many agents with identical tools and prompts
- agents chatting without structured outputs
- no shared run state
- no trace linking subagent work to parent run
- no budget per agent
- no clear authority for final answer
- hidden side effects from child agents

---

## 15. Evals and observability

Agentic code is not done when unit tests pass.

### 15.1 Required eval dimensions

For agentic changes, add or update evals for:

- task success
- correct tool choice
- correct skill invocation
- correct memory retrieval
- correct source authority under conflict
- correct identity resolution before promotion
- correct silence, notification, or interruption behavior
- refusal or approval behavior for risky actions
- loop termination
- recovery from tool failure
- context budget behavior
- final answer faithfulness to evidence
- latency and cost

### 15.2 Offline evals

Use curated datasets before deployment.

Example cases:

```yaml
- name: chooses_memory_before_answering_project_preference
  input: "Use our usual deployment process"
  expected_behavior:
    - calls memory_search with project scope
    - loads deploy-process skill
    - does not invent process

- name: asks_approval_before_external_send
  input: "Email the investor update to the board"
  expected_behavior:
    - drafts email
    - requests human approval
    - does not send before approval

- name: no_regex_router_for_open_goal
  input: "Figure out why signup conversion dropped"
  expected_behavior:
    - decomposes investigation
    - searches metrics/logs/docs as needed
    - does not route solely from keyword "signup"
```

### 15.3 Online evals

Log production traces and review:

- incorrect tool calls
- missing tool calls
- skill overuse
- skill underuse
- memory staleness
- repeated loops
- approval bypass attempts
- user corrections
- high-cost runs

### 15.4 Traces

A useful trace includes:

```text
run_id
session_id
user/workspace/project
model and settings
instructions loaded
tools visible
tool schemas versions
skills visible
skills loaded
memories retrieved
model decisions
tool calls/results
approvals requested/granted/denied
checkpoints
compactions
final output
cost/latency/errors
```

Without traces, agentic debugging becomes folklore.

---

## 16. Anti-pattern catalogue

### 16.1 Keyword router for open-ended intent

Bad:

```python
if "calendar" in user_input:
    return create_calendar_event(user_input)
elif "email" in user_input:
    return send_email(user_input)
```

Better:

- expose calendar and email tools with schemas
- let the model choose tools inside a bounded policy
- require approval for sends/creates
- evaluate tool choice on realistic examples

A keyword router is acceptable only when the domain is closed and the classification is explicitly tested.

### 16.2 Regex as semantic understanding

Regex is fine for parsing known formats. It is not a substitute for understanding ambiguous user goals.

Good regex use:

- parse ISO dates
- extract IDs with known format
- validate schema fields

Bad regex use:

- decide user intent in an open-ended agent
- infer risk level from a few words
- detect all possible tool needs

### 16.3 Global context dump

Bad:

```text
Put all docs, all tools, all memories, and all prior messages into every prompt.
```

Better:

- progressive disclosure
- tool search
- memory search
- skill metadata first, full skill later
- compaction with evidence preservation

### 16.4 Silent fallback

Bad:

```python
try:
    return call_tool(args)
except Exception:
    return "Done"
```

Better:

- structured error
- retry only when safe
- expose failure to model
- ask human or choose alternate tool
- trace the failure

### 16.5 Fake memory

Bad:

```text
Append every user utterance to MEMORY.md.
```

Better:

- candidate memory writes
- evidence
- scope
- confidence
- promotion rule
- contradiction handling

### 16.6 Unbounded loop

Bad:

```python
while True:
    decision = model(...)
    execute(decision)
```

Better:

- max steps
- max cost
- no-progress detector
- stop schema
- error threshold
- human checkpoint

### 16.7 Tool blob output

Bad:

- returning 20,000 words of unstructured search results
- returning raw logs without filtering
- returning secrets

Better:

- structured results
- snippets
- source refs
- pagination
- filters
- redaction

### 16.8 Multi-agent theater

Bad:

- create five agents with different names but same tools and instructions
- let them debate without grounding or tool use

Better:

- split only for tool, policy, memory, context, or ownership reasons
- structured subagent outputs
- parent trace links

---

## 17. Repository files to maintain

Recommended structure:

```text
AGENTS.md
CLAUDE.md
docs/
  agentic-systems-engineering.md
  tool-design.md
  memory-architecture.md
  evals.md
  context-engineering.md
  durable-execution.md
.skills/
  add-agent-tool/
    SKILL.md
    examples.md
    scripts/
  add-agent-memory/
    SKILL.md
  build-agent-eval/
    SKILL.md
agent_runtime/
  context_engine.py
  tools.py
  tool_registry.py
  skills.py
  memory.py
  permissions.py
  checkpoints.py
  traces.py
  evals.py
tests/
  agentic/
    test_tool_choice.py
    test_memory.py
    test_permissions.py
    test_stop_conditions.py
    test_context_budget.py
```

Actual names may vary. The architecture should not.

---

## 18. `AGENTS.md` root instruction

Use a concise root instruction and point to the long doc.

```md
# AGENTS.md

This repository builds agentic systems. Before editing agent logic, tools, memory, skills, context assembly, orchestration, or evals, read:

- `docs/agentic-systems-engineering.md`

Core rule: deterministic harness, adaptive policy.

Use deterministic code for schemas, validation, permissions, idempotency, budgets, state, durability, tracing, guardrails, and tests.

Use model/agent behavior for ambiguous context gathering, tool choice, memory retrieval, skill selection, task decomposition, plan revision, synthesis, and recovery.

Before coding, classify the component as one of:

1. deterministic workflow
2. augmented LLM
3. agent loop
4. multi-agent/subagent system
5. tool or tool registry
6. skill
7. memory subsystem
8. context engine
9. durable execution layer
10. guardrail/permission/human-review layer
11. source lane or source authority layer
12. identity resolution layer
13. attention or notification policy
14. adoption-state change
15. eval/observability layer

For agentic changes, state in your final summary:

- component classification
- model-owned decisions
- deterministic harness responsibilities
- tools the agent has
- tools the agent ought to have
- memories used or changed
- skills used or changed
- state/durability impact
- guardrails/approval impact
- backpressure, budget, and fallback behavior
- adoption state and rollback plan
- acceptance proof, known gaps, and tests/evals added or updated

Avoid replacing adaptive behavior with brittle regexes, keyword maps, fixed routing, silent fallbacks, or global context dumps unless the task is genuinely deterministic and covered by tests.
```

---

## 19. `CLAUDE.md` root instruction

Keep Claude’s always-loaded file short. Put procedures in skills and long architecture in docs.

```md
# CLAUDE.md

This repo builds agentic systems. Before editing agent logic, tools, memory, skills, context assembly, orchestration, or evals, read:

- `docs/agentic-systems-engineering.md`

Core rule: deterministic harness, adaptive policy.

Do not convert adaptive agent behavior into brittle regexes, keyword maps, fixed routes, or one-pass orchestration unless the task is genuinely deterministic and tested.

Use deterministic code for schemas, validation, permissions, idempotency, budgets, state, durability, tracing, guardrails, hooks, and tests.

Use model/agent behavior for ambiguous context gathering, tool choice, memory retrieval, skill selection, task decomposition, plan revision, synthesis, and recovery.

Before implementation, classify the component and list:

- model-owned decisions
- deterministic harness responsibilities
- tools available
- tools missing but needed
- memories available or changed
- skills available or changed
- backpressure, budget, and fallback policy
- adoption state and rollback plan
- observable system acceptance test
- tests/evals required

For agentic changes, update evals for tool choice, skill invocation, memory use, stop conditions, failure handling, permissions, and final answer quality.
```

---

## 20. Pull request checklist for agentic changes

```md
## Agentic architecture checklist

Component classification:

- [ ] deterministic workflow
- [ ] augmented LLM
- [ ] agent loop
- [ ] multi-agent/subagent
- [ ] tool/tool registry
- [ ] skill
- [ ] memory subsystem
- [ ] context engine
- [ ] durable execution
- [ ] guardrail/permission/human review
- [ ] eval/observability

Model-owned decisions:

Deterministic harness responsibilities:

Tools the agent has:

Tools the agent ought to have:

Skills used/added/changed:

Memories read/written/promoted:

Context budget impact:

State/checkpoint/replay impact:

Side effects and approvals:

Failure modes considered:

Tests added:

Evals added:

Incident fixtures or replay evidence:

System acceptance proof:

Manual-proof gaps:

Backpressure/budget/fallback policy:

Adoption state and rollback:

Traces/observability added:

Known limitations:
```

---

## 21. Coding instructions for agentic work

When implementing a request, follow this sequence.

### Step 1: Inspect architecture

Before coding, inspect:

```text
AGENTS.md
CLAUDE.md
docs/agentic-systems-engineering.md
docs/tool-design.md
docs/memory-architecture.md
available skills
tool registry
memory interfaces
context engine
permission system
eval harness
```

### Step 2: Decide whether the agent lacks an affordance

Ask:

- Does the agent need a tool it does not have?
- Does the agent need memory it cannot retrieve?
- Does the agent need a skill rather than more prompt text?
- Does the agent need a subagent for context or policy isolation?
- Does the harness need a checkpoint or approval gate?

If yes, build the missing affordance. Do not simulate it with brittle string logic.

### Step 3: Write or update contracts first

Before implementation, update:

- tool contract
- skill description
- memory schema
- context assembly rule
- permission policy
- eval case
- system acceptance test
- rollback or kill-switch path

The contract shapes the code.

### Step 4: Implement the deterministic harness

Implement:

- schemas
- validation
- permissioning
- idempotency
- state persistence
- tracing
- tests

### Step 5: Preserve adaptive policy

Let the model decide where the problem is genuinely ambiguous:

- which tool to use
- which memory to search
- which skill applies
- whether to inspect more context
- whether to revise the plan
- whether to ask for approval or clarification

Bound the model; do not neuter it.

### Step 6: Add evals

At minimum, test:

- the happy path
- wrong tool avoidance
- missing information behavior
- failed tool recovery
- approval behavior
- memory staleness or contradiction
- loop stop condition
- real incident or replay fixture when one exists
- system-level acceptance proof, not only a manually operated happy path

### Step 7: Summarize architecture impact

In the final response or pull request, include the checklist from section 20.

---

## 22. Examples

### 22.1 Bad: intent router disguised as agent

```python
def handle_request(text):
    if "refund" in text:
        return refund_flow(text)
    if "shipping" in text:
        return shipping_flow(text)
    return general_response(text)
```

This is not an agent unless the domain is intentionally closed and the router is evaluated.

### 22.2 Better: bounded agent with tools

```python
support_agent = Agent(
    instructions="""
    Resolve customer support issues. Use tools to inspect orders, policies, and prior tickets.
    Ask for approval before issuing refunds or sending external messages.
    """,
    tools=[
        search_policies,
        get_order,
        search_prior_tickets,
        draft_customer_reply,
        request_refund_approval,
        issue_refund_after_approval,
    ],
    output_schema=SupportResolution,
    max_tool_calls=12,
)
```

The harness still validates schemas, permissions, idempotency, and traces.

### 22.3 Bad: memory as append-only junk drawer

```python
def remember(text):
    with open("MEMORY.md", "a") as f:
        f.write(text + "\n")
```

### 22.4 Better: memory candidate with evidence

```python
candidate = MemoryCandidate(
    claim="Project deploys require on-call approval.",
    scope="project",
    source_ref=run.current_tool_result_id,
    evidence="deploy_policy.md section 4",
    confidence=0.92,
    staleness_policy="review_after_90_days",
)

memory.write_candidate(candidate)
```

### 22.5 Bad: everything in the prompt

```python
prompt = system + all_docs + all_tools + all_memories + all_history + user_input
```

### 22.6 Better: progressive context

```python
context = context_engine.assemble(
    stable_instructions=load_root_instructions(),
    task=user_input,
    visible_tool_metadata=tool_registry.hot_tools_and_categories(),
    visible_skill_metadata=skill_registry.relevant_metadata(user_input),
    retrieved_memories=memory.search(user_input, scope="project", max_results=5),
    files=workspace.select_relevant_files(user_input),
)
```

---

## 23. Architecture review questions

Ask these during code review:

1. Is this actually agentic, or just a deterministic workflow with an LLM call?
2. Which decisions are model-owned?
3. Which decisions are harness-owned?
4. Does the agent know what tools exist?
5. Does the agent know what tools should exist but are missing?
6. Are tool names and descriptions model-friendly?
7. Are tool schemas narrow and typed?
8. Are side effects permissioned and idempotent?
9. Is memory scoped, evidenced, and retrievable?
10. Are skills used for reusable procedures instead of bloating root instructions?
11. Is context loaded just in time?
12. Is compaction preserving identifiers and evidence?
13. Are long-running operations checkpointed?
14. Can a human approval pause survive process restart?
15. Are subagents justified by tools, policy, context, memory, or ownership boundaries?
16. Are source lanes clear about raw capture, identity, authority, freshness, contradictions, and promotion?
17. Is every synthesis artifact prevented from becoming accidental truth?
18. Is the attention policy explicit enough to avoid noisy participation?
19. Are adoption states clear for sidecars, model paths, and workflows?
20. Are traces sufficient to debug a wrong tool call, wrong source choice, or bad identity merge?
21. Are evals testing behavior, not just code execution?
22. What happens when the model chooses the wrong tool?
23. What happens when a tool returns stale, partial, or contradictory information?
24. What happens when the run hits budget or no-progress limits?

---

## 24. Practical rule of thumb

If the code says:

```text
When user says X, always do Y.
```

ask whether X is truly closed-form.

If X is ambiguous, contextual, or open-ended, the correct design is usually:

```text
Expose the relevant tools, memory, skills, and constraints;
let the agent decide within a bounded, observable harness;
then evaluate whether it made the right decision.
```

If the harness lacks the tool, memory, skill, or evaluator needed for that decision, build the missing harness piece. Do not replace it with a regex.

---

## 24A. Operating lessons from production agentic systems

The practical failures of live agentic systems often look like model failures at first, but the durable fixes usually belong to the harness.

- **Define done in system terms.** For autonomous behavior, a manual run is debugging evidence, not completion proof. State the acceptance test before coding and report manual-proof gaps plainly.
- **Turn incidents into contracts.** A failure should become a fixture, replay, eval, invariant, or protocol rule. If a lesson lives only in a conversation, it will be forgotten.
- **Centralize backpressure.** Retries, queues, lockout behavior, provider health, and per-caller budgets must not be independently reinvented at every layer.
- **Treat cost as safety.** Paid API fallback, model spillover, outbound messages, production writes, and irreversible side effects require explicit approval, audit, and rollback.
- **Reconcile claims with state.** Natural-language claims need matching commands, receipts, state transitions, or mismatch boards. Do not parse open-ended claims with regex as the primary truth mechanism.
- **Separate aspiration from operating truth.** Roadmaps and north stars guide the work; current-state docs and traces prove what the system actually does.
- **Promote gradually.** New source lanes, sidecars, model paths, and workflows move through adoption states. One successful demo is not canonical behavior.
- **Budget human attention.** Interrupt people for authority, irreversible risk, degraded autonomy, or taste/judgment calls. Do not train the system to page humans for every uncertainty.
- **Remember that coding agents are actors.** Claims, session logs, commits, and summaries are part of the operating substrate. No orphan sweeps, no hidden assumption changes, no “works on my manual run” final claims.

Use these as review prompts whenever an agentic change touches live behavior, orchestration, tools, memory, state, provider calls, or human attention.

---

## 25. Minimal source reading list for maintainers

Use official docs and public sources. Do not depend on unauthorized leaked proprietary code.

Recommended primary sources:

- Anthropic: Building Effective Agents
- Anthropic: Tool use and MCP guidance
- Anthropic: Agent Skills
- Anthropic: Claude Code docs for memory, skills, subagents, hooks, MCP, and context management
- OpenAI: Codex `AGENTS.md` guidance
- OpenAI: Agents SDK agents, tools, handoffs, guardrails, skills, and context engineering
- LangGraph: durable execution, interrupts, memory, and persistence
- LangSmith: traces and evals
- Pydantic AI: typed tools, usage limits, evals, and tool approval
- OpenClaw public docs: workspace, tools, skills, memory, context engine, compaction, and agent loop
- AutoGen: human-in-the-loop and multi-agent patterns

The conclusion across these systems is consistent:

```text
Agentic systems need explicit harnesses.
The harness should be deterministic, typed, observable, permissioned, durable, and evaluable.
The adaptive policy should remain adaptive where the next step cannot be known in advance.

For operating systems, the durable chain is:

```text
source -> identity -> claim -> authority -> contradiction -> synthesis -> action -> follow-up -> learning
```
```
