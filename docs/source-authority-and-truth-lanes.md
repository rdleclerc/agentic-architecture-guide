# Source Authority And Truth Lanes

Agentic systems become unreliable when every useful artifact is treated as memory. A durable operating system separates evidence, truth, retrieval, recall, synthesis, sidecars, candidate signals, and outbound artifacts.

## Artifact Roles

Use these roles explicitly:

- `raw_source`: original evidence such as messages, transcripts, documents, events, API rows, logs, tickets, or files.
- `structured_truth`: normalized entities, claims, relationships, commitments, states, and decisions with provenance.
- `retrieval_index`: vector or keyword search over source material. Retrieval is not authority.
- `recall_memory`: operator, session, or procedural continuity. Useful, but not automatically truth.
- `synthesis_artifact`: wiki page, memo, brief, dashboard, report, or summary for humans.
- `candidate_signal`: open question, contradiction, stale lane, possible alert, or review item.
- `sidecar`: helper system that improves workflow or hygiene without owning truth by default.
- `outbound_artifact`: message, report, email, notification, or external output.

## Source Lane Contract

Every source lane should define:

```yaml
lane_id: string
owner: person_or_team
raw_capture: path_or_table_or_api
idempotency_key: string
identity_resolution:
  external_ids: string[]
  aliases: string[]
  merge_policy: string
  unmerge_policy: string
claim_categories: string[]
authority_by_claim_category: object
freshness_policy: object
contradiction_policy: object
promotion_policy: object
health_check: command_or_query
synthesis_targets: string[]
external_sharing_policy: object
```

Do not wire a new corpus, channel, table, or sidecar directly into promoted answers without this contract.

## Authority Matrix

Authority is claim-specific. A chat message, signed document, CRM row, billing system, source transcript, code trace, and human approval may each win for different questions.

For each claim category, define which source can:

- establish the claim
- override an older claim
- corroborate but not override
- generate a candidate signal only
- be used only as retrieval context

## Identity First

Resolve identity before promoting claims. Track aliases, domains, external IDs, source handles, merge evidence, merge time, merge actor, and unmerge path.

If identity is uncertain, keep the result as a candidate signal or open question rather than creating durable truth.

## Synthesis Is Not Truth

Human-readable synthesis is valuable because it makes the system usable. It should cite source handles and claim IDs. It should not silently become the source of truth for future compilers.

If a generated page contains a mistake, fix the underlying claim or source lane when possible, then regenerate synthesis.

## Noisy Lanes

Some lanes contain brainstorming, jokes, speculation, or weak signals. These lanes can be valuable, but the default outputs should be digests, candidates, experiments, story ideas, roadmap ideas, or review queues. Promotion requires repeated evidence, credible sources, owner review, or clear operational relevance.

## Sidecar Adoption

A sidecar starts as reference-only or shadow-mode unless explicitly promoted. Promotion requires a contract, tests, health checks, traceability, rollback, and a scoped owner.
