# Agentic Architecture Guide

Reusable architecture guide for coding agents and humans building agentic operating systems.

Core principle:

> Deterministic harness. Adaptive policy.

Use deterministic code for schemas, permissions, budgets, idempotency, checkpoints, source authority, identity resolution, tool execution, human approval, traces, and evals. Use model-owned adaptive behavior for ambiguous context gathering, tool choice, memory retrieval, plan revision, recovery, and synthesis.

## What is in this repo

- `AGENTS.md`, `docs/`, and `.agentic/` — canonical agent-facing source.
- `agentic_architecture_singlefile.md` — generated/legacy human handoff reference. Do not treat it as the agent editing source.
- `rebuild_agentic_architecture.py` — legacy recovery helper for rebuilding a split pack from a historical single-file bundle; it is not the normal authoring path.
- `AGENTS.md` / `CLAUDE.md` — short always-loaded instructions for coding agents.
- `docs/` — detailed architecture docs for tools, memory, context, evals, source authority, subagents, durable execution, and cross-agent operating model.
- `.agentic/` — starter YAML policies/catalogs/schemas.
- `.claude/skills/` — starter skills for designing tools, memory, context engines, source lanes, and evals.

## Use on a new computer

```bash
git clone git@github.com:rdleclerc/agentic-architecture-guide.git
cd agentic-architecture-guide
```

Then point local agent instructions at `AGENTS.md`. For non-trivial changes, load `docs/00-agentic-change-protocol.md` first and only then load the specific topic doc you need.

## Legacy single-file recovery

```bash
python3 rebuild_agentic_architecture.py agentic_architecture_singlefile.md ./agentic_architecture_pack
```

Use `--overwrite` to replace existing generated files. Do not use this as the normal edit flow unless you are intentionally recovering from the legacy single-file bundle.

## Field lessons added in v1.3

- Define done as observable system behavior, not manual proof.
- Convert incidents into contracts, fixtures, replays, evals, or operating rules.
- Treat backpressure, cost controls, provider fallback, and human attention as harness responsibilities.
- Reconcile natural-language claims with actual state transitions or side-effect receipts.
- Keep thesis/future-state documents separate from current operating truth.
- Promote sidecars, model paths, source lanes, and workflows through explicit adoption states.
