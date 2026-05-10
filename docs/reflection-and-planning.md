# Reflection and planning

Version: 1.0
Audience: coding agents working on agentic systems, plus human reviewers who set acceptance bars.

Plan-then-execute and reflection are the two primitives that make every other harness pattern work in practice. Without them, modularity, exception classification, A2A contracts, cost routing, learning loops, and prioritization all collapse back to folklore at the first time pressure.

---

## 1. Plan as a first-class artifact

The plan is written before action, referenced during action, and compared against at the end. It is not a chat-summary "I'm going to do X"; it is a structured artifact in the change record.

```text
1. Goal
   One sentence. What does the world look like after this change that it
   does not look like now? Stated as observable system behavior, not as
   "the test passes."

2. Acceptance proof
   How will we know the goal was met? What is the acceptance test in system
   terms? What manual-proof gaps will remain after implementation?

3. Component classification
   Which kind of component is being added or changed (workflow, augmented
   LLM, agent loop, subagent, tool, skill, memory, source lane, identity,
   context, durable execution, guardrail, coordination, attention, adoption,
   eval).

4. Simplicity/deletion pass
   Requirement narrowed or corrected, unnecessary parts removed or avoided,
   context/tool/source-authority/feedback alternative considered, and why any
   remaining complexity is worth much more than its hidden cost.

5. Seam declaration
   Modules touched, interfaces depended on, interfaces defined or changed,
   substitutability. See docs/modularity-and-seams.md.

6. Failure-mode budget
   Which exception classes are in scope (recoverable, degraded, unrecoverable)?
   What partial-result or degraded-result behavior is acceptable? See
   docs/exception-taxonomy.md.

7. Routing decision
   Which lane runs this work and why. Degraded or fallback lane if any.
   See docs/cost-aware-routing.md.

8. Out of scope
   What deliberately is not being done, and why? This list catches the
   scope creep that would otherwise drift the goal.
```

A plan that does not have all eight sections is a draft, not a plan.

---

## 2. Goal drift and where to catch it

Goal drift is the failure mode where an agent that started with "make the system survive a malformed payload" quietly redefines the goal to "make this one test pass" once it gets into the weeds. The user-visible symptom looks like the original task, but the underlying contract was never fixed.

Catch drift at three points:

```text
- before each tool call:   does this action serve the original goal stated
                            in the plan?
- before declaring done:   does the result match the acceptance proof?
- inside reflection:       did the change end up serving the goal stated
                            in the plan, or a quietly redefined version
                            of it?
```

If the goal genuinely needs to change mid-task, change the plan explicitly and record why. A change in goal that is not recorded becomes folklore; the next agent inherits a goal it did not see written down.

---

## 3. Reflection: the per-task self-critique loop

Reflection runs after the agent has produced a candidate result and before the result is declared done. It is a structured checklist, not a free-form summary.

### 3.1 The checklist

```text
1. Simplicity/deletion
   What did I delete, collapse, or avoid before adding machinery? Did I consider
   a context/tool/source-authority/feedback fix before adding guardrails or new
   layers?

2. Goal drift
   What was the original goal? Did the implementation drift toward
   "make the local test pass" or "make the immediate symptom go away"?
   Restate the original goal and confirm the change still serves it.

3. Coupling and seams
   Did this change introduce any of the six coupling smells (god-object
   bag, reaching through internals, runtime type-switch, hidden temporal
   dependency, parameter creep, multi-module test)? Did this change reach
   across a module boundary that previously had a seam? Did this change
   add a parameter, branch, or field that another module now depends on
   by absence rather than by contract?

4. Shortcuts
   Where did the change skip a step that the architecture says should
   exist (input validation, schema check, idempotency, source-authority
   lookup, memory write, eval coverage, durable-state record)?

5. Hidden state
   Does the change rely on global state, environment variables, file
   system layout, time-of-day, or process startup order in ways that
   are not documented in the contract?

6. Failure modes
   What happens when each external dependency this change calls is
   slow, unavailable, returns a partial result, or returns garbage?
   Which of those are handled and which are silently re-raised as the
   fall-through path?

7. Tests and evals
   What new behavior is now true that no test exercises? What incident
   class is now reachable that no eval would catch?

8. Causal depth
   If this is a fix, what proximate cause did it address, and what
   ultimate contract did it change? If only the proximate cause was
   addressed, what class of incident is still reachable?
```

### 3.2 What "done" means

Reflection is not done when the agent has answers; it is done when the answers are written down in the change record and the agent has either fixed the items it found or named them as explicit gaps.

```text
hidden gap > known gap
```

Hidden gaps are worse than known gaps because the next agent inherits them without warning.

### 3.3 Reflection is not eval

Evals run from a fixture and grade behavior against expected output. Reflection runs against the architecture and grades the *change* against the contract.

| | Eval | Reflection |
|---|---|---|
| Input | Fixture or replay | The change diff and plan |
| Grades | Behavior | Architecture compliance |
| Cadence | Continuous, automated | Per-task, before "done" |
| Catches | Wrong output | Shortcuts, coupling, drift, hidden state |

Both are required. Neither replaces the other.

---

## 4. Anti-patterns

```text
- "I'll reflect later"          : reflection that is not done before
                                   declaring done is reflection that
                                   does not exist.
- "the test passes, so it's    : the test is a proxy. The plan's
   done"                          acceptance proof is the standard.
- "I'll write the plan after"  : the plan exists to constrain action.
                                   A retroactive plan does not.
- "no scope creep here"         : every change has scope creep
                                   pressure; the out-of-scope list
                                   exists to make resisting it cheap.
```

---

## 5. Cross-references

- Architecture: sections 5.14 (Reflection), 5.15 (Plan-then-execute), 12.1 (Define done as system behavior)
- Anti-pattern: section 9.10 (Skipping reflection)
- Modularity: `docs/modularity-and-seams.md`
- Exceptions: `docs/exception-taxonomy.md`
- Cost routing: `docs/cost-aware-routing.md`
- Eval design: `docs/evals.md`
