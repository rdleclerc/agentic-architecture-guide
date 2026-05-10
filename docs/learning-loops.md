# Learning loops and skill evolution

Version: 1.0
Audience: coding agents, operators, and architects of long-lived agentic systems.

Stable contracts are the substrate; learning loops are how the system gets better at using them. A system without learning loops handles each new task as if it were the first. Patterns that worked are not promoted into skills, patterns that failed are not deprecated, and the agent rediscovers the same answer every week.

---

## 1. Three kinds of learning loop

### 1.1 Within-task: reflection

The per-task self-critique pass. Catches shortcuts, drift, and coupling inside one task. Operates on the change, not on the system. See `docs/reflection-and-planning.md` and section 5.14.

### 1.2 Across-task: skill promotion

A pattern that has worked across N tasks is promoted from ad-hoc agent behavior into a documented skill (section 5.4) with a clear when-to-use rule. The threshold (N, the success criterion, the owner who approves) is part of the harness, not the agent's judgment.

```text
candidate skill   appears in K tasks; nobody has named it; success
                  criterion not yet defined.

drafted skill     named, documented, has a when-to-use rule, has at
                  least one eval. runs in shadow or candidate-write
                  mode.

canonical skill   eval-backed, owner-approved, used as the default
                  procedure for its task class.

deprecated skill  superseded or no longer relevant. removed from the
                  active registry but retained for replay.
```

Promotion follows the same adoption-state discipline as new tools, sidecars, and lanes (section 5.13).

### 1.3 System-level: external critique

A separate agent or human, on a different cadence than the working agents, reviews aggregate behavior:

```text
- which patterns are recurring across tasks?
- which failures are repeating?
- which contracts need to change?
- which skills are stale or contradicting newer evidence?
- which evals are missing for behaviors that have started to matter?
```

External critique operates on the system, not on any one task. It runs on a slower cadence (weekly, monthly) and produces findings that go to the same destinations as within-task reflection.

---

## 2. Closing the loop

The most common learning-loop failure is the loop that exists but is not closed. Closing the loop means the harness has a path from finding to action.

```text
finding                       destination
recurring pattern             candidate skill
recurring failure class       missing eval, contract change proposal
contract feels wrong          contract change proposal
ambiguous data subject        candidate signal for human review
duplicated effort             refactoring task or skill consolidation
stale skill                   deprecation candidate
silent degradation observed   exception-taxonomy contract change
                               (docs/exception-taxonomy.md)
```

A finding without a destination is a smell, not a feature. Loops that produce findings nobody acts on are journals, not learning.

---

## 3. Source authority for findings

Findings are claims. They follow the same source-authority and identity rules as any other claim (section 5.11):

```text
- candidate signal: someone or something noticed a pattern
- supported claim: the pattern has corroboration across N tasks
- promoted claim: the pattern has an owner and an action
- canonical: the pattern has been encoded in a contract or skill
```

A finding promoted to "canonical" without going through the candidate stage is a vibes-based change. Treat it as a smell.

---

## 4. Adoption state for new skills

A new skill follows the adoption-state ladder:

```text
reference_only -> shadow_mode -> candidate_write -> write_enabled -> canonical
```

Skill promotion to canonical requires:

```text
- evals passing on the skill's task class
- an owner who has reviewed the skill
- a rollback plan if the skill turns out to be wrong
- a deprecation path for the procedure(s) it supersedes
```

Promotion by acclamation (one good demo) is the same anti-pattern as accidental production promotion (section 9.8).

---

## 5. What learning loops are not

```text
- not chat summaries: a chat summary that nobody reads is not learning.
- not journals: a daily diary of agent activity is not learning.
- not fine-tuning a base model: that is a separate change that requires
   its own evals and adoption process. learning loops here operate on
   skills, contracts, and evals.
- not "we tried it and it worked": vibes are not promotion.
```

---

## 6. Common smells

```text
- weekly digest emails that nobody opens
- a "lessons learned" file that grows but is never referenced
- skills that have not changed in N months in a system that has
- evals that have not changed in N months in a system whose behavior has
- recurring incidents whose post-mortems do not feed any contract change
```

---

## 7. Cross-references

- Architecture: section 5.19 (Learning loops and skill evolution)
- Anti-pattern: section 9.13 (No learning loop)
- Field lesson: section 12.13 (Systems that don't learn get worse)
- Reflection: `docs/reflection-and-planning.md`
- Adoption state: section 5.13 and `docs/cross-agent-operating-model.md`
- Eval design: `docs/evals.md`
