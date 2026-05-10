## Agentic architecture review

Component classification:

- [ ] deterministic workflow
- [ ] augmented LLM call
- [ ] agent loop
- [ ] multi-agent/subagent system
- [ ] tool or tool registry
- [ ] skill
- [ ] memory subsystem
- [ ] source lane/source authority/identity layer
- [ ] context engine
- [ ] durable execution
- [ ] guardrail/permission/human review
- [ ] cross-agent coordination/adoption state
- [ ] attention or notification policy
- [ ] eval/observability
- [ ] agent-native CLI or tool surface
- [ ] repository structure / parallel-agent seam
- [ ] learning-loop or feedback pipeline

Model-owned decisions:

Deterministic harness responsibilities:

Source authority, identity, and truth/synthesis boundaries:

Guardrails and human approval gates:

Cross-agent ownership or adoption-state changes:

Attention/notification behavior:

Tests/evals added or updated:

Source-authority and package-integrity proof:

- [ ] Live multifile files are canonical.
- [ ] Single-file bundle contains no unique canonical content.
- [ ] Runtime-specific adapters contain no unique doctrine.
- [ ] Referenced docs/skills/eval fixtures exist and validate.

Acceptance proof:

- Commands/evals/reviews run:
- Evidence artifacts or links:
- Manual proof vs autonomous/system proof gaps:
- Known residual gaps accepted by integrator:
- Rollback or revert path:

Deletion-first simplicity check:

- Requirement narrowed or corrected:
- Parts/processes/guards/handoffs deleted or avoided:
- Context/tool/source-authority/feedback alternative considered:
- Smallest viable guardrail/change considered:
- Remaining complexity and why its benefit is much greater than hidden cost:

Agent Failure RCA, if this fixes agent behavior:

- What the agent saw:
- Human counterfactual: would a capable human likely fail with the same information/tools?
- Missing context/tool/source/memory/feedback/invariant:
- Replay/eval/contract that prevents recurrence:
