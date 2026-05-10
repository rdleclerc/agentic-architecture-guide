# Task prioritization and queue discipline

Version: 1.0
Audience: coding agents and operators of agentic systems with many concurrent lanes.

Attention budgets decide when humans should be interrupted. Cost-aware routing decides which lane runs a task. Prioritization decides which task runs next when several are ready and they cannot all run at once.

---

## 1. Why this is not optional

A long-lived agentic system runs many concurrent lanes: scheduled cron tasks, ingest workers, claim compilers, retrieval surfaces, conversation surfaces, review queues, alerts. Without discipline, the order is first-come-first-served by accident, and the failure mode is that an urgent task waits behind a long-running batch because no one declared which mattered more.

The harness owns the rule, not the agent. A coding agent that picks the next task by feel will reliably pick the easiest one; this is a known bias, not a moral failing. A scheduler with no declared rule will silently drift toward whatever the easiest implementation produces.

---

## 2. Required inputs per task

Every task in a queue carries five declared inputs.

```text
- urgency
   does the task have a deadline? what is the cost of late completion
   (none, soft, hard, irreversible)?

- importance
   does completion change a downstream state that other tasks depend on?
   does failure block other lanes?

- preemptability
   can the task be paused and resumed without loss? if yes, it can yield
   to a higher-priority task; if no, starting it commits the lane.

- cost
   how expensive is this task in the lane it would run in? a cheap
   urgent task should not wait behind an expensive non-urgent one.

- staleness
   does the task lose value if delayed (a daily digest is useless once
   the day is over) or does it accumulate value (a backlog cleanup gets
   more valuable the older it is)?
```

A task without these inputs is a guess. The harness should refuse to enqueue a task that does not declare them; defaults are fine, but they are declared defaults.

---

## 3. The queue rule

The simplest defensible rule:

```text
1. Run preemption-immune tasks (an irreversible side effect already
   committed, a durable-state migration in progress) to completion
   regardless of priority.

2. Among ready tasks, prefer higher importance. Among equally important
   tasks, prefer higher urgency. Among equally urgent tasks, prefer
   cheaper.

3. Allow explicit overrides recorded with rationale. An override that is
   not recorded becomes folklore; record it.

4. If the queue is consistently saturated, the lane is under-resourced
   or the upstream is producing too fast. Surface that as a signal,
   not as silent task drops.
```

More sophisticated rules exist (weighted fair queueing, EDF, deadline-monotonic, priority inheritance for shared-resource cases). The right rule depends on the lane, but the discipline is the same: declared inputs, declared rule, recorded overrides, no silent drops.

---

## 4. Staleness and value decay

Some tasks lose value if delayed. A digest scheduled for 8am loses most of its value if it runs at 3pm. The queue rule has to know this, or the digest will run after every batch ahead of it has finished.

```text
staleness behavior      example
hard window             daily 8am digest; expires at 9am.
soft decay              freshness check on a market signal; value halves
                         every hour.
appreciation            backlog cleanup; value grows with age.
none                    long-running compilation; value flat.
```

Tasks with hard windows that miss the window should not silently run late. They should be recorded as missed and either rescheduled with new urgency or dropped with a signal.

---

## 5. Backpressure

If a queue is consistently saturated, something is wrong upstream. The harness should:

```text
- surface the saturation as a signal (not as silent drops)
- expose queue depth and oldest-task age in observability
- refuse new enqueues past a configured ceiling, with a structured
  rejection (degraded class, see docs/exception-taxonomy.md)
- escalate to a human if saturation persists past a threshold
```

A queue that grows unboundedly is a bug, not a feature. The right response is operator visibility, not silent task suppression.

---

## 6. Auditing override decisions

Every override (priority bump, queue jump, manual deferral) is recorded with:

```text
- who or what made the override
- when
- which task was affected
- the rationale
```

An override without a record becomes folklore the first time anyone questions why a task ran in the order it did.

---

## 7. Common smells

```text
- new lane added with no declared priority inputs.
- "this just runs every hour" with no declared staleness.
- queues that grow without alerting.
- urgent tasks routinely missing their windows but no signal raised.
- overrides made by humans that are not recorded.
- prioritization implemented inside a single agent's prompt instead of
  in the harness.
```

---

## 8. Cross-references

- Architecture: section 5.20 (Task prioritization and queue discipline)
- Anti-pattern: section 9.14 (FCFS task scheduling)
- Field lesson: section 12.14 (Priority is not optional)
- Attention budgets: section 5.12
- Exception taxonomy and backpressure: `docs/exception-taxonomy.md`
