# Agentic Architecture Guide

Reusable architecture guide for coding agents and humans building agentic operating systems.

Core principles:

> Deterministic harness. Adaptive policy. Simplicity before machinery.

Use deterministic code for schemas, permissions, budgets, idempotency, checkpoints, source authority, identity resolution, tool execution, human approval, traces, and evals. Use model-owned adaptive behavior for ambiguous context gathering, tool choice, memory retrieval, plan revision, recovery, and synthesis.

Simplicity is a first-class design constraint: question requirements, delete unnecessary parts/processes, prefer better context/tools/source authority/feedback over behavior-policing guardrails, simplify what remains, then optimize/accelerate/automate last. Complexity has hidden downstream cost, so it must be worth much more than its visible cost.

## What is in this repo

- `AGENTS.md`, `docs/`, `.agentic/`, and `skills/` — canonical agent-facing source.
- `CLAUDE.md`, `.claude/skills/`, and `.codex/skills/` — adapter entrypoints. They must not contain unique doctrine that is absent from the canonical neutral source.
- `agentic_architecture_singlefile.md` — generated/legacy human handoff reference. It must not contain unique canonical content.
- `build_agentic_architecture_singlefile.py` — rebuilds the generated single-file handoff from the canonical live files.
- `rebuild_agentic_architecture.py` — legacy recovery helper for rebuilding a split pack from a historical single-file bundle; it is not the normal authoring path.
- `scripts/` and `tests/` — lightweight validation/eval checks that keep the guide operational instead of purely aspirational.
- `docs/` — detailed architecture docs for tools, memory, context, evals, source authority, subagents, durable execution, and cross-agent operating model.
- `.agentic/` — starter YAML policies/catalogs/schemas.
- `skills/` — starter skills for designing tools, memory, context engines, source lanes, and evals.

## Use on a new computer

```bash
git clone git@github.com:rdleclerc/agentic-architecture-guide.git
cd agentic-architecture-guide
```

Then point local agent instructions at `AGENTS.md`. For non-trivial changes, load `docs/00-agentic-change-protocol.md` first and only then load the specific topic doc you need.

## Source authority

The live multifile repo is canonical. The single-file bundle is a generated distribution/recovery artifact and should validate against the live files before it is shared. If a file exists only in the bundle, either materialize it in the live repo or mark it explicitly archival/non-authoritative.

Do not let adapter paths become owners of doctrine. Claude, Codex, local CLIs, MCP servers, and other runtimes should adapt the neutral guide rather than fork it.

## Validate and regenerate generated artifacts

```bash
python3 build_agentic_architecture_singlefile.py
python3 scripts/validate_agentic_pack.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

Use `python3 build_agentic_architecture_singlefile.py --check` in CI or review to prove the generated single-file handoff is current.

## Legacy single-file recovery

```bash
python3 rebuild_agentic_architecture.py agentic_architecture_singlefile.md ./agentic_architecture_pack
```

Use `--overwrite` to replace existing generated files. Do not use this as the normal edit flow unless you are intentionally recovering from the legacy single-file bundle.

## Field lessons through v1.5

- Define done as observable system behavior, not manual proof.
- Convert incidents into contracts, fixtures, replays, evals, or operating rules.
- Treat backpressure, cost controls, provider fallback, and human attention as harness responsibilities.
- Reconcile natural-language claims with actual state transitions or side-effect receipts.
- Keep thesis/future-state documents separate from current operating truth.
- Promote sidecars, model paths, source lanes, and workflows through explicit adoption states.
- Design agent-native CLIs and repo seams as model-facing interfaces.
- Prefer small, cohesive, contract-shaped files for parallel agent work.
- Put simplicity/deletion before machinery; complexity must justify its hidden cost.
