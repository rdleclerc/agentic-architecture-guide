# Context Engineering for Agentic Systems

The context engine decides what enters the model prompt. Larger context windows do not remove the need for selection, compression, and provenance.

The context engine should assemble:

- root instructions
- current user request
- active task state
- constraints and budgets
- relevant retrieved memory
- relevant files or snippets
- available tool summaries
- available skill summaries
- recent observations
- source ledger

Progressive disclosure:

- Always load short root instructions, current task, active state, and safety constraints.
- Retrieve memories, files, examples, and prior episodes by relevance.
- Load full tool schemas and full skill bodies only when activated.
- Compact stale or redundant history while preserving goals, constraints, decisions, open questions, evidence, pending approvals, and artifacts.

Acceptance criteria:

- Context assembly has one primary code path.
- Each included context item has source, reason, priority, and token estimate.
- Compaction is tested.
- The agent has tools to request more context instead of receiving everything upfront.

Use `.agentic/context_policy.yaml` as the source of truth.

## Source Ledger Requirements

The context engine should include a source ledger for every run. The ledger should identify which source records, memories, synthesis artifacts, tool schemas, skills, and files were loaded; why they were loaded; their freshness; and whether they are authoritative, retrieval-only, recall, synthesis, or candidate material.

Compaction must preserve source handles, identity decisions, unresolved contradictions, approval constraints, and attention policy. A short summary that loses those identifiers is not safe context.
