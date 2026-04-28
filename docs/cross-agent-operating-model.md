# Cross-Agent Operating Model

This document is for repositories where multiple coding agents, research agents, sidecars, or background workflows may work on the same system.

## Core Rule

Do not let independent agents act like separate contractors on the same shared files, runtime config, truth store, or roadmap.

Use one explicit integrator for shared work. Contributors produce evidence-backed proposals unless they are assigned a disjoint write set.

## Roles

`integrator` owns the final design choice, shared-file edits, ownership plan, final verification, and handoff.

`contributor` researches, tests, proposes, and writes notes. A contributor does not edit shared implementation, config, runtime, or source-of-truth files unless the integrator grants scoped ownership.

## Required Artifacts

For coordinated work, prefer a task folder with:

```text
brief.md
constraints.md
proposal-<session-name>.md
integration-plan.md
verification.md
```

The integration plan should name the integrator, write sets, adoption states, checks to run, and unresolved risks.

## Adoption States

Track sidecars, model paths, source lanes, workflows, and specialist agents as:

```text
reference_only
shadow_mode
read_only
candidate_write
write_enabled
canonical
deprecated
retired
```

Do not let a successful demo or one good run change adoption state implicitly.

## Wisdom Intake

When importing lessons from another multi-agent system, do not copy its local nouns into this manual. Translate each lesson into a generic principle, then into a contract that can be reviewed or tested:

1. What failed or worked?
2. Which architectural layer was involved?
3. Is the lesson about source authority, identity, memory, tools, context, coordination, attention, adoption, durability, or evals?
4. What contract, test, replay, eval, or operating rule would prevent the failure or preserve the success?
5. What adoption state, rollback path, or owner changes because of the lesson?
6. Does the principle belong in the generic manual or only in a local system appendix?

This keeps the manual reusable while still allowing it to absorb field wisdom. A lesson is fully absorbed only when future agents can find it before acting and when a relevant eval, checklist, or gate would catch the old failure shape.

## Handoff Requirements

A final handoff should state:

- role and ownership
- changed files or artifacts
- source lanes or truth stores affected
- adoption-state changes
- tests and evals run
- unresolved risks
- follow-up owner or review queue
