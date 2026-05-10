# Modularity and seam design

Version: 1.0
Audience: coding agents and human reviewers working on agentic systems.

This document is the detailed contract for the modularity claim in the executive thesis and for the "Modularity, parallelization, and seam design" section of the architecture pack. Read it before beginning any non-trivial change. Re-read it during reflection.

---

## 1. Why this exists

Coding agents systematically under-modularize. The reward signal inside one task does not include the costs that land in the next task. Tokens spent declaring a clean module seam are visible inside the task; the cost of *not* declaring the seam is invisible inside the task and lands later, in a different session, on a different agent.

```text
declare a seam now:           cost ~ linear (one contract + a few lines of glue)
untangle a shortcut later:    cost ~ super-linear (callers x editors x dependent facts)
```

Humans hold this asymmetry in working memory because they have lived through it. Coding agents do not. The harness has to install the bias.

---

## 2. The seam-declaration rule

Every non-trivial change brief answers five questions before code is written. These belong in the architecture brief alongside component classification and harness/policy split.

```text
1. Modules touched
   Which modules does this change read, write, or import?

2. Interfaces depended on
   Which contracts (function signatures, schemas, message types, tool contracts,
   memory APIs, source-authority lookups) does this change consume?

3. Interfaces defined or changed
   Which contracts does this change introduce, modify, deprecate, or extend?
   For each, what is the public surface and what is intentionally private?

4. Filesystem/package destination
   Which package owns this change, and which repo-local topology/dependency gate
   proves future agents cannot add the same behavior to a convenience/root layer?

5. Substitutability
   What would have to change if the implementation behind each interface were
   swapped (different store, different model, different transport, different
   provider)? If the answer is "many things in many places," the seam is in the
   wrong place.
```

A coding agent that cannot answer these has not understood the change yet.

---

## 3. The six coupling smells

Any of these in a diff is creating coupling. The harness should catch them at review time, not at incident time.

### 3.1 God-object state bag

A new function takes a `context`, `state`, `request`, or similarly named bag and reads four or more fields from it. The function does not depend on the bag; it depends on the four fields.

```python
# Bad
def render(context):
    return f"{context.user.name}: {context.last_event.kind} at {context.now} ({context.locale})"

# Better
def render(name: str, event_kind: str, when: datetime, locale: str) -> str:
    return f"{name}: {event_kind} at {when} ({locale})"
```

The bad version couples `render` to the entire `context` shape. The better version depends on four typed values and is independently callable from anywhere those values are available.

### 3.2 Reaching through a module to read internals

Module A imports module B and accesses `B._internal_thing` or a field that is conventionally private. The author justifies it as "it is right there." This is the most reliable predictor of expensive future untangling.

```python
# Bad
from b import _config_dict
host = _config_dict["host"]

# Better
from b import get_endpoint
ep = get_endpoint()
host = ep.host
```

If module B's storage shape changes, the bad version forces a coordinated edit in every caller that reached through. The better version isolates the change to module B.

### 3.3 Runtime type-switch on opaque payload

A function receives an opaque payload and switches on a `kind`, `type`, or `event_name` field, dispatching to N branches. Each branch knows about the others by absence. Each new branch is a coupling event.

```python
# Bad
def handle(event):
    if event["kind"] == "create":
        ...
    elif event["kind"] == "update":
        ...
    elif event["kind"] == "delete":
        ...

# Better
HANDLERS: dict[str, Callable] = {}
def register(kind):
    def deco(fn): HANDLERS[kind] = fn; return fn
    return deco

@register("create")
def _on_create(event): ...

@register("update")
def _on_update(event): ...

def handle(event):
    return HANDLERS[event["kind"]](event)
```

The better version makes each handler independently addressable. Adding a new event kind does not require editing the dispatcher.

### 3.4 Hidden temporal dependency

Function A must be called before function B, but the requirement is encoded only in the order they appear in the calling code.

```python
# Bad
session.attach()
session.send(msg)  # silently fails if attach was not called first

# Better
def send(attached_session: AttachedSession, msg: Message):
    ...

attached = session.attach()
send(attached, msg)
```

The better version makes the dependency a type. `send` cannot be called without an attached session because the function signature refuses to accept anything else.

### 3.5 "Just one more parameter" creep

A function gains its sixth, seventh, eighth optional parameter, each added by a different agent in a different session for a different caller.

```python
# Bad
def fetch(url, timeout=None, retries=None, cache=None, follow_redirects=None,
          user_agent=None, headers=None, dry_run=None, trace_id=None):
    ...
```

Either the function is doing several jobs (split it) or the parameters belong on a typed config object that includes only the fields each caller needs.

```python
# Better
@dataclass
class FetchOptions:
    timeout: float = 30.0
    retries: int = 3
    cache: CachePolicy = CachePolicy.DEFAULT

def fetch(url: str, options: FetchOptions = FetchOptions()) -> Response:
    ...
```

### 3.6 Test that requires more than one module to instantiate

A unit test imports four modules to construct the system under test. The test is honest about the coupling: there is no seam between those modules. Fix the seam, not the test.

If the only way to test `analyzer` is to construct a `repository`, a `cache`, and a `client`, then `analyzer` is implicitly coupled to all three. A seam between `analyzer` and the others (an interface, a fake, a typed input) makes the test simple and the coupling explicit.

---

## 4. Parallelization as the diagnostic

A codebase where two agents collide on shared files every session has a seam problem, not a coordination problem. The right fix is not better merge tooling; it is to find which interface is missing and declare it.

```text
symptom                                   diagnosis
two agents keep editing the same file     surface needs a seam between their work
agent edit lands and breaks unrelated     module exposed an internal that other
  callers it had no reason to know         callers reached through
adding a new lane requires touching N     N call sites are all reading the same
  call sites                                internal directly instead of through
                                            a contract
removing a feature touches more files     the feature was never encapsulated; it
  than adding it did                        leaked into N modules during build
agents repeatedly re-derive the same      there is no contract for the result;
  result in different shapes                 it is being recomputed inline
                                             every time
```

If the system cannot be worked on in parallel without folklore-level coordination, the seams are wrong.

---

## 5. What this document is not

This is not a license to invent abstractions for hypothetical future requirements. The bias is toward declaring seams *for the modules this change actually touches*, not toward speculative interface design.

```text
Three similar lines is better than a premature abstraction that picks the
wrong axis. The cost asymmetry argument applies to seams that turn out to
matter; the canonical signal that a seam matters is that more than one
caller needs the contract or more than one agent will edit on either side
of it.
```

When in doubt: prefer a small, named function with the right signature over an inlined snippet, but defer abstract base classes, plugin systems, and configurable strategies until the second or third caller appears.

---

## 6. Reflection ties this to the per-task loop

The reflection checklist (`docs/reflection-and-planning.md`) explicitly asks:

```text
- Did this change introduce any of the six coupling smells?
- Did this change reach across a module boundary that previously had a seam?
- Did this change add a parameter, branch, or field that another module
  now depends on by absence rather than by contract?
- Did this change add or move code without a repo-local topology/dependency gate
  proving the intended package seam?
- If a future task had to swap the implementation behind any interface
  this change touches, what would have to change with it?
```

A reflection pass that cannot answer "no" to the first three and bound the answer to the fourth is not done.

---

## 7. Cross-references

- Architecture: section 3 (Modularity, parallelization, and seam design)
- Anti-pattern: section 9.9 (Convenient coupling)
- Field lesson: section 12.10 (Modularity is a runtime property)
- Reflection: section 5.14 and `docs/reflection-and-planning.md`
- Parallel work and integrator/contributor roles: section 5.13 and `docs/cross-agent-operating-model.md`
