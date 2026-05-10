# Coding Agent Work Contract

Audience: coding agents and human operators working in any project.

Use this contract before a **non-trivial coding task**. It makes coding agents more reliable by forcing the smallest useful loop:

```text
intent → orientation → bounded plan → surgical patch → evidence → learning trail
```

This is a project-agnostic template. Project-specific repos may add stricter rules, but they should not weaken this contract.

## When to use it

Use for tasks that touch any of these:

- code, tests, prompts, skills, workflows, runtime config, automation, tools, schemas, or docs that guide agents;
- shared repos or machine-level config;
- external side effects, secrets, user data, browser/UI, email, social, DBs, queues, provider calls, long-running agents, or deployment paths;
- any change where “tests pass” would not by itself prove the system is safe.

For tiny deterministic edits, use the minimal inline version below. Do not turn typo fixes into a governance project.

## Contract fields

### 1. Objective

State the concrete user-visible outcome in one or two sentences.

Good:

> Add a small validator that rejects missing evidence rows in coding-agent task contracts.

Bad:

> Improve reliability.

### 1A. Basic Spine First for product/rewrite/agentic-system work

Before adding architecture, abstractions, agents, contracts, routers, monitors, or eval frameworks, name:

- minimum user-visible product spine;
- single canonical command, acceptance test, or live-safe check that proves it;
- current result: `pass`, `fail`, or `not available`;
- if `fail` or `not available`, whether this task only fixes/creates that spine check or is explicitly a non-readiness spike.

Core spine gaps are blockers, not residual risks, unless the user explicitly accepts the spike boundary. For Type0, default to: real feed/tip/wire input → normalized signal → admission decision → lane/story assignment → story processing → fact-check/publish/reject guard → traceable result.

### 2. Scope and non-scope

Name exactly what may change and what may not change.

Include:

- files/components in scope;
- files/components out of scope;
- protected files;
- side-effect boundaries;
- whether commit/push/deploy/send/writeback is allowed.

### 3. Assumptions and ambiguities

List assumptions. If an assumption would change the implementation materially, stop and ask.

### 4. Orientation before edits

Before patching, cite evidence that you found the right layer:

- repo/project rules read;
- active claims or ownership checked, where applicable;
- existing implementation or similar pattern inspected;
- tests/evals/fixtures located or gap named;
- source-of-truth docs identified;
- duplicate implementation path rejected or explained.

### 5. Plan with evidence targets

Each step should have a proof target.

```text
1. Add template → evidence: file exists, links resolve.
2. Add validator → evidence: focused unit tests pass.
3. Update docs → evidence: source authority and gaps recorded.
```

### 6. Patch discipline

Default rules:

- smallest change that satisfies the contract;
- no speculative features;
- no adjacent refactor or formatting sweep;
- match existing style;
- delete/simplify before adding;
- every changed line should trace to objective or evidence;
- optional validators/frameworks/automation wait until a real failure proves need.

### 7. Evidence matrix

Before claiming done, fill this matrix. If a layer is skipped, say why and whether it is a gap.

| Layer | Required when | Evidence |
|---|---|---|
| Basic product spine | product/rewrite/agentic-system work | spine name, canonical proof, current pass/fail/not available result |
| Unit/regression | deterministic code logic changed | command/result or n/a reason |
| Integration | cross-module/service/runtime behavior changed | command/result or n/a reason |
| Eval/golden/replay | LLM judgment, prompt, skill, classifier, agent behavior changed | eval/replay/rubric or explicit gap |
| Browser/e2e | user-visible web/UI changed | URL/screenshot/console result or n/a |
| Security/privacy | secrets/auth/user data/outbound side effects involved | scan/review result or n/a |
| Topology/dependency | new/moved code files or package seams | gate command/result or n/a |
| Real-world fixture | bug/failure/judgment claim exists | source case or gap |
| Source/authority | durable claim, memory, source lane, or external source used | source handles |

### 8. Stop conditions

Stop and ask before proceeding if:

- protected files need edits not explicitly authorized;
- external side effects are needed;
- required evidence cannot be gathered;
- the basic product spine is failing/not available and scope is drifting into architecture instead of fixing the spine check or declaring a spike;
- scope expands materially;
- privacy/secret boundary is unclear;
- tests/evals reveal a different root cause;
- multiple agents/claims overlap on the same files;
- implementation requires runtime automation or new services not in scope.

### 9. Review lane

For medium/high-risk work, run at least one review pass before done:

- architecture/source-authority review;
- hidden-complexity/simplifier review;
- security/privacy review;
- dead-code/orphan review;
- agent-advocate/human-counterfactual review.

Use deterministic tests first. LLM reviewers do not replace tests or human approval.

### 10. Learning trail

Route outcomes:

| Finding | Destination |
|---|---|
| recurring successful workflow | skill candidate |
| recurring failure class | eval fixture / quality gate |
| missing context | source doc / context policy |
| confusing tool surface | tool/API/CLI improvement deep dive |
| useful but unapproved durable lesson | memory candidate |
| stale or bloated instruction | simplify/delete proposal |

## Minimal inline version

```text
Work contract:
Objective:
Basic spine first (if product/rewrite/agentic-system):
In scope:
Out of scope / stop conditions:
Orientation evidence:
Plan:
Evidence required:
Skipped evidence/gaps:
Learning trail:
```

## Relationship to other guide docs

- Use `docs/00-agentic-change-protocol.md` for the broader agentic-system change protocol.
- Use `docs/context-engineering.md` when context loading/compaction is part of the change.
- Use `docs/learning-loops.md` when findings should become skills, evals, or contract changes.
- Use `docs/evals.md` when agent behavior, prompts, or judgment require eval coverage.
- Use this contract as the concrete task-start artifact that ties those docs to one coding task.

## Relationship to Uber planning

Do not create duplicate planning bureaucracy.

- Tier 0 / tiny deterministic work: inline note is enough.
- Tier 1 / contained non-trivial coding: this work contract is usually the plan artifact.
- Tier 2/3 / high-risk, agentic-system, runtime, prompt/skill, cross-repo, deletion/refactor, or ambiguous architecture work: `uberplan` may extend this contract into a full plan contract, but should reuse the same objective, scope, evidence, and stop-condition fields instead of creating an unrelated second plan.
