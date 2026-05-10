# Exception taxonomy and graceful degradation

Version: 1.0
Audience: coding agents writing or auditing failure paths in agentic systems.

Durable execution and checkpointing answer "what happens if the process dies." Exception taxonomy answers a different question: "what does this code do when something it depends on misbehaves?" A coding agent that does not classify failure tends to write code where every failure becomes a re-raised exception that propagates upward and stops the lane. This is the right behavior for a small subset of failures and the wrong behavior for the rest.

---

## 1. Three exception classes

Every failure attaches to exactly one of these classes.

### 1.1 Recoverable

The operation can be retried with the same inputs and is expected to succeed within the configured retry budget.

Examples:
- Transient network error
- Rate-limited provider
- Optimistic-lock conflict
- Leader election handoff
- Temporary quota exhaustion that resets on a known cadence

Required behavior:
- Retry per policy (exponential backoff, jitter, max attempts).
- Surface the failure to the caller only on retry budget exhaustion.
- Log the retry path so operators can see what is happening.
- Do not poison durable state with intermediate failures.

### 1.2 Degraded

The operation cannot succeed fully, but a partial result is meaningful and the calling lane can continue.

Examples:
- Enrichment lookup unavailable but the core record is still valid
- One of three sources missing for a synthesis
- One of N parallel subtasks failed but the task tolerates it
- Expensive lane budget exhausted, cheaper lane used as fallback

Required behavior:
- Produce the partial result.
- Mark the missing pieces explicitly in the result type.
- Surface a structured signal (not a silent gap) to the next layer.
- Record what would have been there so audit and replay are possible.

### 1.3 Unrecoverable

The operation cannot succeed and a partial result would be wrong. The lane must stop and surface the failure.

Examples:
- Schema mismatch on durable input
- Source-authority disagreement that cannot be resolved by policy
- Identity collision (two distinct entities resolved to one)
- Irreversible side-effect failure detected after the side effect committed

Required behavior:
- Stop. Do not retry. Do not produce a degraded result.
- Write a structured failure record.
- Alert per attention policy (section 5.12).
- Make the failure visible to operators and to durable state.

---

## 2. Class attribution rules

Every retry policy, fallback, or degradation path attaches to one of the three classes explicitly. A retry without a class is a guess.

```python
# Bad
try:
    return call_external()
except Exception:
    return None

# Better
try:
    return call_external()
except TransientError:
    raise  # recoverable: retry policy will handle
except PartialResultError as e:
    return DegradedResult(value=e.partial, missing=e.missing)
except SchemaError:
    raise  # unrecoverable: do not retry, do not degrade
```

The bad version collapses three different failures into the same silent `None`. The caller has no way to distinguish "transient, retry me" from "the input was wrong, do not retry" from "the side effect committed and we lost the receipt."

---

## 3. Graceful degradation discipline

Graceful degradation means producing a *degraded* result *with a structured signal*, never silently. The signal is what allows the next layer to know whether it is reading complete or partial data.

```python
@dataclass
class DegradedResult:
    value: Any
    missing: list[str]            # which fields or sources are absent
    reasons: dict[str, str]       # per-missing-piece, why
    completeness: float           # 0.0 to 1.0
```

Silent degradation is more dangerous than unrecoverable failure because it produces a confidently wrong output downstream. A reviewer reading a degraded result without the signal cannot tell that something is missing.

---

## 4. Retry policy contract

Every retry attaches to:

```text
- the exception class it handles (always recoverable)
- a budget (max attempts, max total time, max cost)
- a backoff strategy (constant, exponential, fibonacci, with jitter)
- a circuit breaker (when to stop trying for a window)
- an audit surface (where retries are logged)
```

A retry policy that is not declared in code is a guess at runtime. Retry budgets that are not enforced lead to retry storms when a downstream is slow.

---

## 5. Common smells

```text
- bare except: catches everything, classifies nothing.
- silent return None on error: hides degradation as a missing value.
- unbounded retry loops: retry-storms a flaky downstream into outage.
- silent paid spillover: see docs/cost-aware-routing.md.
- "we'll add error handling later": the error handling is the contract.
```

---

## 6. Cross-references

- Architecture: section 5.16 (Exception taxonomy and graceful degradation)
- Anti-pattern: section 9.11 (Unclassified errors)
- Field lesson: section 12.11 (Errors are classes, not surprises)
- Routing and spillover: `docs/cost-aware-routing.md`
- Durable state and checkpoints: `docs/durable-execution.md`
