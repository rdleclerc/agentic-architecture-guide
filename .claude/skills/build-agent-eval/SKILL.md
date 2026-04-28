---
name: build-agent-eval
description: Use when adding tests or evals for agentic behavior.
---

# Build Agent Eval

## Procedure

1. Identify the behavior being tested.
2. Create positive and negative cases.
3. Test process, not only final answer.
4. Capture tool choice, memory retrieval, context use, approval gates, recovery, and stop conditions.
5. Add cheap tests for CI and heavier tests for release or nightly runs.
6. Ensure failures are traceable.

## Output

Return eval cases, expected traces, and pass/fail criteria.
