# Tool Design for Agentic Systems

A tool is an affordance exposed to the model. Do not treat tools as ordinary internal helper functions. Tools need semantic contracts because the model decides when and how to call them.

Every model-callable tool requires:

- name
- description for the model
- purpose
- when to use
- when not to use
- input schema
- output schema
- side-effect class
- permission level
- idempotency policy
- examples
- misuse examples
- failure modes
- trace fields
- eval cases

Bad tool designs are vague, overly broad, unsafe, or hard to recover from. A tool called `run(query: string)` is usually too broad. A tool called `search_company_memory(query, company_id, limit, freshness)` is usually better.

Side-effect classes:

- `none`: pure computation or formatting
- `read`: reads local or external state
- `write`: writes local workspace state
- `external_write`: sends or mutates external systems
- `destructive`: deletes, overwrites, spends money, changes permissions, or causes irreversible effects

Rules:

- External writes require idempotency keys.
- Destructive tools require human approval unless explicitly whitelisted.
- Tools return structured errors; they do not silently swallow failure.
- Tool outputs should be concise, typed, and traceable.
- Tool descriptions should explain boundaries and examples, not only parameters.

Use `.agentic/tool_catalog.yaml` as the source of truth.

## Source-Aware Tools

Tools that read evidence should declare source role and freshness. Tools that write or publish should declare authority, approval, idempotency, undo strategy, and whether the output is truth, synthesis, candidate signal, or outbound artifact.

A model-friendly tool description should say when not to use the tool. For example, a search index can retrieve evidence, but it should not be described as deciding which source wins. A report renderer can create synthesis, but it should not silently promote the report back into durable truth.
