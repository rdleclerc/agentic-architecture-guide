---
name: openclaw-agentic-skill-creator
description: Create, modify, evaluate, or optimize OpenClaw-targeted agentic skills and skill-like workflows. Use when Codex, Claude, or another coding agent is asked to turn an OpenClaw/Gaia/Type0/Soho/agentic-media workflow into a skill, improve an OpenClaw skill, run eval-driven OpenClaw skill iteration, benchmark an OpenClaw skill, or tune an OpenClaw skill description. Do not use as the general portable skill creator; use `uber-skill-creator` for general SKILL.md skills when it is installed.
---

# OpenClaw Agentic Skill Creator

Create and improve skills for OpenClaw, Gaia/Gaia Brain, Type0, Soho House, and shared agentic-media work. This skill is the OpenClaw-specific counterpart to `uber-skill-creator`: use this when the skill depends on OpenClaw runtime behavior, tenant/workspace policy, live source lanes, agent affordance, local proof conventions, or live-safe OpenClaw parity receipts. Use `uber-skill-creator` for portable SKILL.md work that should run across Codex, Claude, and compatible agents without OpenClaw-specific assumptions.

Keep provenance visible when adapting public skill-creator methods, but do not copy proprietary or leaked code. Translate runtime examples into the current executor; do not assume Claude-specific subprocesses, slash commands, browser viewers, or OpenClaw tools unless this runtime exposes them and the user approved that path.

## OpenClaw Production Contract

Before creating or expanding a skill, run the smallest useful non-skill check. A direct answer, source note, typed tool, source-lane contract, deterministic script, or workflow affordance may be better. Promote to a skill only when repeated agent behavior, discovery, source-lane use, or reusable judgment guidance is the real need.

For production, library, governed, Slack-visible, side-effecting, tenant-sensitive, or cross-agent skills, capture the compact contract before adding release machinery:

- owned recurring job and expected OpenClaw agent behavior;
- should-trigger, should-not-trigger, and near-neighbor prompts;
- tenant, workspace, channel, account, project, and actor boundaries;
- required source lanes, tools, memory/context packets, permissions, and live-data access;
- scripts, assets, references, and deterministic checks that carry real behavior;
- trigger evals, output evals, live-safe OpenClaw proof receipts, owner, review cadence, maturity tier, and rollback/idempotency rule;
- source-authority boundary, identity-resolution behavior, synthesis boundary, side-effect boundary, budget/fallback policy, and attention/notification behavior.

Use maturity tiers to select gates, not ceremony: `Scaffold` gets quick validation; `Production` adds trigger/output evals; `Library` adds packaging/runtime checks and route-confusion coverage; `Governed` adds owner review, regression history, live-safe proof, and explicit acceptance evidence.

Any usage or drift loop must be metadata-only and local-first by default. Acceptable telemetry is skill name/version, event type, source/client, command name without arguments, outcome, failure type, and timestamp. Do not store raw prompts, Slack messages, transcripts, private files, model outputs, command arguments, or reviewer notes as telemetry.

## Affordance And Proof Rules

Preserve high agent affordance. Help agents inspect sources, choose clear tools, apply judgment, recover from gaps, and leave traces. Do not encode brittle gates, hidden routing layers, semantic judges, or deterministic substitutes for judgment unless the user explicitly approves the lower-affordance design.

If the skill introduces or changes scripts, CLIs, MCP tools, function-calling schemas, source readers, memory APIs, write/publish actions, or side effects, use `openclaw-agentic-tool-designer` before implementation and include the resulting tool contract or summary in the skill/eval package.

For behavior that an OpenClaw agent is supposed to perform, prove the workflow before readiness claims:

1. Run a fresh self-subagent or runtime-native executor with the intended context, tools, source lanes, skills, recovery instructions, and no hidden rationale.
2. If it fails, improve affordances: context packet, skill wording, tool descriptions, source access, task frame, recovery instructions, or audit trail. Do not patch with private harness state.
3. Run the same workflow with a real OpenClaw agent using only normal OpenClaw scaffold plus the successful context/skill/tool profile.
4. Preserve receipts: self-subagent result, OpenClaw `sessionKey`/`sessionId` or transcript path, tool outputs, source artifacts, eval outputs, and any redactions.

If live proof is unsafe or unavailable, label the gap. Do not present local validation or synthetic evals as OpenClaw parity proof.

## Creation Workflow

1. **Classify and route.** If the request is portable, redirect to `uber-skill-creator`. If it is OpenClaw-specific, continue here.
2. **Capture intent from evidence first.** Mine the conversation, files, transcripts, source lanes, operator corrections, and observed tools before asking questions.
3. **Ask only material gaps.** Clarify trigger/non-trigger contexts, expected outputs, tenant/source/tool permissions, side effects, success criteria, and proof requirements.
4. **Draft the skill.** Keep trigger information in the frontmatter `description`. Keep the body procedural, concise, and OpenClaw-specific. Use imperative instructions, short rationale where it improves behavior, and references/scripts/assets only when they reduce active-context load or repeated work.
5. **Use progressive disclosure.** `SKILL.md` is active context; larger examples, schemas, and recipes belong in `references/`; deterministic repeatable work belongs in `scripts/`; reusable output inputs belong in `assets/`. For multi-variant skills, route to only the relevant reference.
6. **Validate shape.** Run the available quick validator and any package-specific lint/tests. Validation checks package integrity; it does not replace agentic proof.

## Eval-Driven Iteration

Use eval-driven iteration for production/library/governed skills, broadly installed skills, behavior-changing skills, or any skill whose correctness is not obvious from inspection.

1. **Draft realistic eval prompts.** Use real operator-style OpenClaw/Gaia/Type0/Soho/agentic-media tasks. Include should-trigger, should-not-trigger, near-neighbor, source-lane, side-effect, and tenant-boundary cases as relevant.
2. **Run with-skill and baseline together.** For a new skill, baseline is no skill. For an existing skill, baseline is the previous or snapshotted version. Use the current runtime's fresh subagent/executor; in OpenClaw, use the exposed session runner when available.
3. **Capture artifacts.** Store prompts, input files, outputs, transcripts, timing/token data when available, tool receipts, source handles, and eval metadata under an iteration workspace.
4. **Draft assertions while runs execute.** Objective checks should cover observable outputs, source-authority labels, forbidden side effects, receipt presence, and tenant/source boundaries. Keep subjective judgment for human review.
5. **Grade and aggregate.** Use scripts where checks are deterministic. Produce a benchmark summary and preserve qualitative notes; read transcripts, not only final outputs.
6. **Show the human the results.** Prefer the bundled `eval-viewer/generate_review.py` with `--static` in headless OpenClaw environments, or an equivalent static report when the viewer is unavailable.
7. **Iterate on affordance.** Improve context, wording, resources, examples, tool descriptions, or source-lane guidance. Avoid overfitting to a tiny prompt set or adding coercive rules where clearer affordances would work.
8. **Repeat until acceptable.** Expand the eval set before claiming broad coverage.

Convert missed triggers into trigger evals, bad outputs into output assertions, and script/tool errors into smoke tests or tool-contract fixes.

## Description Optimization

The frontmatter `description` is the primary trigger surface. After creating or materially changing a skill, tune it with held-out trigger evals:

1. Create 20 realistic queries: roughly half should trigger and half should not. Include messy operator phrasing, local project names, channel/source-lane/tool names, abbreviations, adjacent portable-skill requests, and near misses.
2. Review the eval set with the user when practical; weak trigger evals produce weak descriptions.
3. Keep a champion and challenger. Score the current description, revise from failures, then retest on held-out examples. Promote only when the challenger improves trigger precision/recall without weakening must-pass cases or stealing portable work from `uber-skill-creator`.
4. Report before/after descriptions, scores, failure modes, and remaining ambiguity.

If the current runtime has no approved trigger-eval executor, run the held-out cases manually with fresh context or runtime-supported subagents and record the observed trigger behavior.

## Packaging And Reporting

Package only when the current runtime and user need a `.skill` artifact. Otherwise, leave the skill in the repo and report the path, validation commands, proof receipts, and gaps.

Final reports for OpenClaw skills should state: component classification, model-owned decisions, deterministic harness responsibilities, tools available/missing, memory behavior, source-authority and truth/synthesis boundaries, identity behavior, context behavior, skills used or added, guardrails/approvals, ownership/adoption state, attention behavior, backpressure/budget/fallback behavior, deletion/simplification result, cost/complexity tradeoff, RCA/human-counterfactual if relevant, rollback plan, acceptance proof, manual-proof gaps, and tests/evals added.

## Reference Files

Read only what the task needs:

- `references/schemas.md` for eval, grading, and benchmark JSON shapes.
- `agents/grader.md` when grading assertions against outputs.
- `agents/analyzer.md` when interpreting benchmark patterns and hidden regressions.
- `agents/comparator.md` for blind A/B comparison when a rigorous version comparison is needed.
