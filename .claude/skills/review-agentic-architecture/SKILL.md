---
name: review-agentic-architecture
description: Use before merging changes to agent loops, tools, memory, context, skills, subagents, guardrails, or evals.
---

# Review Agentic Architecture

## Checklist

- Is the component correctly classified?
- Are model-owned decisions separated from harness-owned responsibilities?
- Are ambiguous decisions handled by adaptive policy rather than brittle regex or keyword routing?
- Are tools typed, permissioned, observable, and tested?
- Is memory scoped, evidenced, and contradiction-aware?
- Is context assembled by policy rather than dumping everything?
- Are risky side effects gated by approval and idempotency?
- Are checkpoints and replay behavior safe?
- Are evals included for positive and negative cases?

## Output

Return pass/fail with required changes.
