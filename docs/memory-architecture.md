# Memory Architecture for Agentic Systems

Context is what the model sees now. Memory is durable information outside the immediate prompt that can be searched, inspected, updated, promoted, contradicted, or expired.

Use four memory types:

- working memory: current task state, plan, open questions, active artifacts
- episodic memory: prior actions, conversations, decisions, traces, outcomes
- semantic memory: durable facts about users, projects, companies, codebase, and policies
- procedural memory: reusable methods, workflows, skills, and instructions

Memory is not an append-only text file. Every durable memory should have scope, evidence, confidence, recency, sensitivity, and status.

Minimum memory tools:

- `memory_search`
- `memory_get`
- `memory_write_candidate`
- `memory_promote`
- `memory_update`
- `memory_refute`
- `memory_supersede`
- `memory_forget_or_expire`
- `memory_trace_usage`

Policy:

- The agent can search memory when prior context is likely relevant.
- The agent can propose memory writes.
- Promotion requires evidence and policy approval.
- Contradicted memories must not be silently overwritten.
- Sensitive memory has stricter review and deletion rules.
- Final outputs relying on memory should be traceable to memory ids.

Use `.agentic/memory_schema.yaml` as the source of truth.

## Truth Boundaries

Memory is not automatically the source of truth. Separate durable recall, semantic memory, structured truth, retrieval indexes, source records, synthesis artifacts, and candidate signals.

When a memory is used to answer a high-stakes question, the system should expose its source authority and freshness. If memory conflicts with live primary evidence, prefer the policy-defined authority path and mark the conflict rather than overwriting silently.
