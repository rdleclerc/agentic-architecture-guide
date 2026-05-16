# Interface Failure Patterns

Use these as anti-pattern checks when reviewing a proposed tool.

## Contradictory interface

Symptoms:
- two flags imply opposite behavior;
- default target is production but examples imply dry-run;
- enum values overlap semantically;
- output field names change between success and error.

Fix:
- remove one path;
- make target explicit;
- reject ambiguous combinations before side effects;
- return one stable schema with `status` and structured `error`.

## Mega-tool with hidden modes

Symptoms:
- `run(action="search|write|delete|publish", payload={...})`;
- unrelated permissions in one schema;
- agent must remember which fields matter for each mode.

Fix:
- split read/write/destructive tools;
- keep a shared internal helper if needed;
- expose small model-facing surfaces.

## Fake validator that makes judgments

Symptoms:
- tool says it validates but actually decides accept/reject/promote;
- editorial/taste logic hidden behind scores;
- no transcript or source evidence for the decision.

Fix:
- validator enforces hard invariants only;
- agent/editor owns ambiguous judgment;
- raw source and synthesis remain separate.

## Unrecoverable errors

Symptoms:
- stack traces or `failed` with no code;
- agent retries blindly;
- missing permission/target/resource information.

Fix:
- structured `error.code`;
- safe `agent_next_action`;
- no secrets or internal stack traces in model-facing output.

## Missing idempotency

Symptoms:
- retry sends duplicate email, publishes twice, charges twice, or writes duplicate memory;
- no natural key or request key;
- output lacks durable resource ID.

Fix:
- require idempotency key or natural key;
- return existing resource on duplicate;
- log actor, input hash, and target.

## Source authority collapse

Symptoms:
- fetched text, memory recall, LLM summary, and candidate signal share one `content` field;
- timestamps/freshness missing;
- model-generated text is treated as evidence.

Fix:
- label each artifact role;
- include freshness/provenance;
- prevent model synthesis from being promoted to raw evidence.
