# CLAUDE.md

Read AGENTS.md first. This repo builds agentic operating systems.

Use deterministic code for the harness: schemas, permissions, idempotency, state, checkpoints, compaction, source authority, identity resolution, tool execution, human approval, traces, and evals.

Use model-owned adaptive behavior for ambiguous intent, context gathering, memory retrieval, tool choice, plan revision, recovery, and synthesis.

Do not implement open-ended agent behavior as keyword routers, regex intent detection, hardcoded branches, or giant always-loaded prompts unless explicitly justified and tested.

Do not collapse source-of-truth stores, retrieval indexes, recall memory, human-readable synthesis, sidecars, and candidate signals into one vague memory layer. Name the role of each artifact.

For any agentic change, inspect relevant tools, skills, memory, source lanes, identity policy, context policy, coordination rules, durability, and evals before editing code.

Define done as observable system behavior. A manual one-off proof is not completion for autonomous behavior; record the system acceptance test, replay/eval evidence, and known gaps. Treat cost controls, provider fallback policy, and adoption state as safety-critical harness design.

Keep this file short. Put reusable procedures in skills. Put detailed architecture in docs/.
