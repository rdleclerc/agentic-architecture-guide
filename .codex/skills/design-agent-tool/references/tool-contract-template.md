# Tool Contract Template

Use this as the working contract before implementing an agent-facing tool.

```json
{
  "name": "verb_noun",
  "version": "v0",
  "model_description": "One or two sentences the model will see. Include when to use and the boundary.",
  "purpose": "What deterministic capability the tool provides.",
  "affordance_bought": "What this lets the agent perceive, verify, decide, or do.",
  "when_to_use": ["Concrete trigger"],
  "when_not_to_use": ["Near miss or unsafe case"],
  "input_schema": {
    "type": "object",
    "required": [],
    "properties": {}
  },
  "output_schema": {
    "type": "object",
    "required": [],
    "properties": {}
  },
  "side_effect_class": "none|read|write|external_write|destructive",
  "permission_level": "who/what may call this and against which target",
  "idempotency_policy": "required for writes/external/destructive; natural key or explicit key",
  "source_authority_role": "raw_evidence|memory_recall|model_synthesis|candidate_signal|outbound_artifact|not_source",
  "freshness_policy": "How timestamps, cache age, and stale results are represented",
  "privacy_security_policy": "Secrets/PII filtering, target allowlists, authz checks",
  "error_codes": [
    {"code": "INVALID_ARGUMENT", "meaning": "...", "agent_next_action": "..."}
  ],
  "trace_fields": ["tool_call_id", "actor", "target", "started_at", "duration_ms", "input_hash"],
  "examples": [
    {"input": {}, "output": {}, "why": "..."}
  ],
  "misuse_examples": [
    {"input": {}, "rejection": "...", "why": "..."}
  ],
  "eval_cases": [
    {"name": "happy path", "prompt": "...", "expected_tool_call": {}, "expected_result": "..."},
    {"name": "near miss", "prompt": "...", "expected_behavior": "do_not_call"}
  ]
}
```

For `write`, `external_write`, and `destructive` tools, also specify:

- dry-run behavior;
- approval requirement;
- rollback/undo strategy;
- duplicate-call behavior;
- audit log location;
- tenant/project boundary.
