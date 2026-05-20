---
name: openclaw-agentic-tool-designer
description: >-
  Use when adding, modifying, reviewing, or debugging any OpenClaw-facing agent tool or tool-like interface: OpenClaw tools, MCP tools, function-calling schemas, agent-facing CLIs/scripts, source readers, memory APIs, write/publish actions, or workflow commands. Use for Type0, Gaia/Gaia Brain, Soho House, OpenClaw, or agentic-media work whenever a tool interface could be ambiguous, contradictory, overbroad, unsafe, hard for agents to call, or when a coding agent proposes deterministic gates instead of better agent affordances.
---

# OpenClaw Agentic Tool Designer

A tool is an **agent affordance**, not merely a helper function. Design it so a capable agent can perceive the right state, choose the tool at the right time, call it correctly, recover from errors, and leave an auditable trace.

## First principle

Prefer high-agent-affordance architecture: better source access, typed tools, concise skills, feedback loops, and raw-evidence lanes before adding brittle orchestration, hidden automation, hard gates, or deterministic substitutes for agent judgment.

If you believe a lower-affordance pattern is correct, explain why and get explicit approval before implementing it.

## Use this procedure

1. **Name the affordance.** State what this lets the agent see, decide, verify, or do that it could not do before.
2. **Delete first.** Ask whether the requirement can be removed, simplified, handled by an existing tool, or expressed as a skill/source lane instead.
3. **Choose the right primitive.** Use the decision table below before writing code.
4. **Write a tool contract.** Include purpose, use/non-use, schemas, side effects, idempotency, errors, traces, and evals.
5. **Design for the model caller.** Tool and parameter descriptions are UX copy for the model. Include examples and misuse examples.
6. **Separate evidence from synthesis.** Raw source output, memory recall, model synthesis, candidate signal, and outbound artifact must be labeled differently.
7. **Make failure recoverable.** Return structured error codes, human-readable cause, and the next safe action. Do not swallow failures.
8. **Test tool choice and misuse.** Add evals where the agent should call the tool, should not call it, passes bad args, lacks permission, or faces conflicting tools.

## Choose skill vs tool vs source lane vs harness

| Need | Prefer | Why |
|---|---|---|
| Repeatable judgment/process with flexible execution | Skill | Teaches the agent how to work without reducing agency. |
| Model-callable read/write/action with stable schema | Tool | Gives the agent a typed affordance and traceable side effects. |
| Evidence capture/retrieval/truth boundary | Source lane | Keeps raw evidence, freshness, and authority explicit. |
| Prevent invalid state, enforce permissions, validate writes | Deterministic harness | Machines should own invariants, idempotency, authz, and side-effect gates. |
| Editorial/taste judgment, source chasing, synthesis | Agent with skills/tools | Do not bury ambiguous judgment in deterministic gates by default. |

## Required tool contract

Before implementation, produce a contract. Use `references/tool-contract-template.md` for the expanded template.

Minimum fields:

- `name`
- `model_description`
- `purpose`
- `affordance_bought`
- `when_to_use`
- `when_not_to_use`
- `input_schema`
- `output_schema`
- `side_effect_class`: `none`, `read`, `write`, `external_write`, or `destructive`
- `permission_level`
- `idempotency_policy`
- `source_authority_role`
- `error_codes`
- `trace_fields`
- `examples`
- `misuse_examples`
- `eval_cases`

Run `scripts/lint_tool_contract.py <contract.json>` when you have a JSON contract.

## Agent-facing CLI requirements

If the tool is a CLI command agents will call:

- Non-interactive by default or provide `--no-input`/`--yes` with safe behavior.
- Stable `--json` output for data; diagnostics on stderr.
- Documented exit codes and structured errors.
- Bounded reads: `--limit`, filters, cursors, truncation metadata.
- Safe writes: `--dry-run`, idempotency key/natural key, explicit target, undo/rollback note.
- Target clarity: local vs prod, tenant/project, and actor/principal visible in output.
- Introspection: `--help` plus an agent-readable command/tool manifest when broad.

## Common failure patterns

See `references/interface-failure-patterns.md` for examples. Watch especially for:

- contradictory flags or defaults;
- one mega-tool with mode strings instead of orthogonal tools;
- tool names that describe implementation, not user/model intent;
- write tools without idempotency;
- errors that say what failed but not how the agent should recover;
- raw evidence mixed with model summaries;
- tools that quietly make editorial decisions while pretending to be validators.

## Type0 / Gaia / Soho examples

- **Type0 source chase:** a tweet/article/media reader should return raw artifacts, source role, freshness, receipt IDs, and gaps. It should not decide whether Sonny accepts the story.
- **Gaia / Gaia Brain memory:** a memory tool should distinguish raw source, remembered claim, synthesis, contradiction, and confidence. Writes need provenance and idempotency.
- **Soho House bookmarks:** a bookmark-intake tool should expose original URL/text/media, classification candidate, and source gaps. It should not bury the trail behind a single score.

## Output format

Return:

1. `Tool or non-tool decision` — keep/delete/skill/tool/source-lane/harness.
2. `Tool contract` — with the required fields above.
3. `Implementation notes` — smallest viable surface and where validation lives.
4. `Tests/evals` — tool-choice, schema, permission, side-effect, source-authority, and misuse cases.
5. `Approval needed` — any lower-affordance design, external write, destructive action, or live side effect.

## When composing with Skill Creator

If a new or changed OpenClaw skill introduces scripts, CLIs, MCP tools, function-calling schemas, source lanes, memory APIs, or side effects, invoke this tool-design procedure before shipping the skill. If you are creating or improving the OpenClaw skill itself, use `openclaw-agentic-skill-creator` for the draft → eval → improve lifecycle.
