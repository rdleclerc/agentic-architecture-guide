# Version and Adoption State

This file records the current canonicality and rollout posture of the guide. It is intentionally small; version metadata should prevent ambiguity, not become governance theatre.

## Current version

**Current local version: v1.5**
**Date:** 2026-05-09
**Canonical source:** live multifile repository

`agentic_architecture_singlefile.md` is a generated distribution/recovery artifact. It should validate against live files before sharing and must not contain unique canonical doctrine.

## Adoption state by area

| Area | Status | Notes |
|---|---|---|
| Deterministic harness / adaptive policy | canonical | Core doctrine. |
| Simplicity / deletion-first design | canonical | Complexity requires benefit much greater than hidden cost. |
| Source authority and truth/synthesis boundaries | canonical | Treat raw source, structured truth, retrieval, recall, synthesis, sidecars, candidate signals, and outbound artifacts as distinct roles. |
| Agent-native CLI/tool-surface guidance | canonical | CLI surfaces are model-facing APIs. |
| Repository seams and small-file guidance | canonical | Split at stable contracts; avoid multi-responsibility mega-files. |
| Embedded single-file bundle | generated adapter | Distribution/recovery only; not an editing source. |
| Neutral `skills/` package | canonical | Runtime-specific skill paths are adapters. |
| Claude/Codex skill adapters | adapter | Must not contain unique doctrine absent from `skills/`. |
| Lightweight package validator/eval checks | canonical baseline | Intended to catch drift, not replace real project-specific evals. |
| Deep reference docs | reference | Load only when the topic applies. |

## Promotion rule

New doctrine becomes canonical only when it has:

1. a clear source-authority location in the live multifile repo,
2. a deletion-first justification,
3. either a validator/eval/fixture or an explicit reason why a static check is sufficient,
4. no unique copy hidden in a runtime-specific adapter, and
5. a rollback/deprecation path if it later proves wrong.
