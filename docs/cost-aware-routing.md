# Cost-aware routing

Version: 1.0
Audience: coding agents and operators of agentic systems with multiple model lanes or paid providers.

Attention budgets cover human attention. Spend authority covers paid API keys. Cost-aware routing covers the runtime decision: given a task, which lane runs it.

---

## 1. Lanes

A long-lived agentic system typically has at least three lanes available.

```text
default lane    cheaper, faster, broadly capable. Used for the bulk of
                routine work. Token cost per task is low; capability
                ceiling is moderate.

escalated lane  more expensive, more capable on hard tasks, often slower.
                Used when task difficulty, evidence sensitivity, or
                consequence severity justifies the cost.

degraded lane   cheapest, possibly local, possibly cached. Used when the
                default lane is unavailable or budget is exhausted, and
                when a degraded result is acceptable. See
                docs/exception-taxonomy.md.
```

Real systems often have more lanes (a coding-specific lane, a vision lane, a long-context lane), but the routing doctrine is the same.

---

## 2. The routing decision

Lane choice combines several inputs. None of them is sufficient alone.

```text
- task difficulty
   does the default lane handle this class reliably in evals? if no, the
   escalated lane is justified by capability, not by intuition.

- evidence sensitivity
   data subject (founder, customer, employee, public), jurisdiction,
   confidentiality tier. some lanes may be doctrinally barred from
   handling some classes of evidence regardless of difficulty.

- consequence
   is this a draft for review, a durable claim, or an irreversible side
   effect? higher-consequence work bears more cost.

- budget state
   rolling spend, per-lane budget, per-tenant budget. routing must
   refuse to escalate when the budget is exhausted, not silently
   pretend the budget does not exist.

- lane health
   current error rate, current latency, current rate-limit posture of
   each lane. unhealthy lanes are routed away from, not retried into.

- explicit overrides
   the operator or doctrine has said "this task class always uses the
   escalated lane regardless of difficulty." overrides are recorded
   with rationale; they do not become folklore.
```

The routing decision is recorded with the task. A routing decision that is not recorded cannot be audited and cannot be evaluated.

---

## 3. Spillover policy is part of routing

When the default lane fails, the choice between "escalate to a more expensive lane," "degrade to a cheaper lane," and "stop" is a doctrine decision, not an emergent behavior.

```text
silent paid spillover is a bug.
silent retry past budget is a bug.
silent degradation that produces a confidently wrong output is a bug.
```

Each spillover path attaches to:

```text
- the exception class it responds to (recoverable, degraded, unrecoverable)
- the destination lane and why
- the budget impact and per-task cost cap
- the audit record so spend is attributable
```

---

## 4. Three failure modes

```text
1. Silent escalation
   every task goes to the escalated lane because the default lane felt
   unreliable in one bad demo. cost leaks accumulate without anyone
   owning the choice.

2. Silent fallback
   the default lane fails, the harness silently routes to a paid
   fallback, and no one realizes the burn rate has changed until the
   bill arrives.

3. Wrong-axis routing
   lane choice keys off task length, prompt-token count, or whatever
   was easiest to measure, instead of off the actual axis (difficulty,
   sensitivity, consequence).
```

The fix in all three is the same: explicit doctrine, recorded decisions, audited spillover.

---

## 5. Audit and attribution

Every paid call attaches to:

```text
- the originating task or session id
- the lane chosen and why
- the input token count and the output token count
- the cost (provider-reported and internally tracked)
- the budget bucket the cost was charged to
```

Calls without attribution should fail closed at the gateway. "Anonymous" paid calls are the most reliable predictor of next month's bill surprise.

---

## 6. Eval coverage

Routing behavior is evaluable.

```text
- given a task class, does the harness pick the configured lane?
- given a budget-exhausted state, does the harness refuse to escalate?
- given a lane outage, does the harness degrade or stop per doctrine?
- given a sensitive evidence class, does the harness refuse barred
  lanes?
```

A routing rule with no eval is a rule that will quietly drift.

---

## 7. Common smells

```text
- routing logic spread across N call sites instead of in a registry.
- retry counters that escalate to a paid lane after some attempts
  without doctrine.
- "we'll worry about cost later."
- per-call provider switches in handler code rather than in routing.
- hardcoded model strings in agent prompts.
```

---

## 8. Cross-references

- Architecture: section 5.18 (Cost-aware routing doctrine)
- Field lesson: section 12.12 (Cost asymmetry is a routing input)
- Spend authority claim: executive thesis claim 5
- Exception taxonomy: `docs/exception-taxonomy.md`
- Adoption state for new lanes: section 5.13 and `docs/cross-agent-operating-model.md`
