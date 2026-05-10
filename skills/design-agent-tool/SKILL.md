---
name: design-agent-tool
description: Use when adding, modifying, or reviewing a tool exposed to an agent.
---

# Design Agent Tool

## Procedure

1. Decide whether the model should call this tool directly.
2. Define the semantic purpose.
3. Define when to use and when not to use.
4. Define input and output schemas.
5. Classify side effects and permissions.
6. Add idempotency for writes and external side effects.
7. Add examples and misuse examples.
8. Define structured errors and failure modes.
9. Add trace fields.
10. Add tool-choice and misuse evals.

## Output

Return a tool contract and list of tests/evals.
