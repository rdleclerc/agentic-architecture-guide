# Agentic Architecture Single-File Source

Version: 1.4
Generated: 2026-05-08
Purpose: one Markdown source that explains the architecture and contains a rebuildable multifile repo pack for coding agents building agentic operating systems.

This file is meant to be handed to a human technical lead, Codex, Claude Code, or another coding agent. It has two jobs:

1. Explain the architecture: deterministic harness, adaptive policy, source authority, identity, coordination, and durable operating posture.
2. Carry the entire repo-ready architecture pack in embedded file payloads that can be reconstructed into a multifile system.

The pack is intentionally system-neutral. It should be usable as a base manual for coding agents, then specialized later by mapping concrete source lanes, memory stores, agents, tools, and operating rules into a local appendix.

The central claim is operational, not philosophical: coding agents tend to implement ordinary von Neumann-shaped control flow unless the repository gives them a stronger agentic harness model. The fix is not to remove deterministic engineering. The fix is to put determinism in the harness and keep ambiguous decision-making in the model-owned policy layer.

A second claim matters for real operating systems: agentic software must distinguish truth, retrieval, recall, synthesis, sidecars, and external action. Without those boundaries, agents turn useful context into false authority, noisy channels into institutional memory, and experimental helpers into accidental production systems.

A third claim comes from operating live agentic systems: incidents should become contracts, not folklore. If a production failure teaches a lesson, translate it into the harness layer it belongs to, the acceptance test that would catch it, the eval or replay fixture that preserves it, and the adoption rule that prevents one lucky demo from becoming production truth.

A fourth claim is about causal depth. Coding agents often stop at the first plausible proximate cause: the timeout was too short, the parser missed a field, the router chose the wrong branch, the worker retried, the subagent lacked context. Those may be true, but they are rarely the ultimate cause. Agentic systems fail because a deeper contract was missing: the wrong layer owned the decision, memory was not consulted, source authority was unclear, state was not durable, ownership was ambiguous, an eval did not exist, or the harness allowed an unsafe action. Agents must be willing to go several causal layers deep before claiming they found the problem.

A fifth claim is about spend authority. Paid API keys are not ordinary context.
If an OAuth or tenant-scoped plan exists for coding-agent work, raw API-key
access must be treated as a privileged exception path owned by the harness, not
something agents discover in environment variables and use opportunistically.
Model-provider keys need a gateway, attribution, budgets, rate limits, and
tests that fail when direct key reads come back.

A sixth claim is about coupling cost asymmetry. The token cost of declaring a
clean module seam now is roughly linear: a name, a contract, a few lines of
glue, and the discipline of routing access through the contract instead of
reaching across modules. The cost of untangling shortcut-coupled code later is
super-linear in the number of callers, the number of agents that have since
edited around the shortcut, and the number of facts that quietly came to depend
on the leaked internal. Coding agents do not feel this asymmetry inside a single
task because the local diff is smaller without the seam, the test still passes,
and the cost only appears weeks later in a different session. The harness must
therefore push the bias forward: every non-trivial change declares the seams it
touches, defines, or changes, and a reflection pass at the end of the task
checks whether any new shortcut, hidden dependency, or convenient cross-module
read was introduced. Modularity is the substrate that makes parallelization,
reflection, exception classification, A2A contracts, cost-aware routing,
learning loops, and prioritization possible at all. Without declared seams,
each of those collapses back into folklore.

A seventh claim is about agent-native interfaces and codebase knowledge. Coding
agents fail less when CLIs are non-interactive, JSON-first, bounded, idempotent,
introspectable, and recoverable, and when repository knowledge is discoverable
through topic docs or a checkable markdown graph rather than buried in one flat
root file. The repo shape is part of the harness: small contract-shaped files,
context packets, prompt libraries, and linked decision records make parallel
agent work safer.

---

## Table of contents

1. [Core architecture](#core-architecture)
2. [Causal depth: proximate and ultimate causes](#causal-depth-proximate-and-ultimate-causes)
3. [Modularity, parallelization, and seam design](#modularity-parallelization-and-seam-design)
4. [Mermaid diagrams](#mermaid-diagrams)
5. [How to rebuild the multifile pack](#how-to-rebuild-the-multifile-pack)
6. [Repository tree](#repository-tree)
7. [Bundle manifest](#bundle-manifest)
8. [Embedded file payloads](#embedded-file-payloads)
9. [Research boundary: leaked or derivative Claude Code source](#research-boundary-leaked-or-derivative-claude-code-source)
10. [Reference sources used for architecture framing](#reference-sources-used-for-architecture-framing)

---

## Core architecture

A conventional software system is usually dominated by explicit control flow. An agentic system is dominated by the harness around a model-owned policy. The harness supplies bounded context, tools, memory, skills, permissions, state, checkpoints, traces, and evals. The model policy makes uncertain decisions inside that harness.

Use deterministic code for schemas, validation, permissions, budgets, checkpoints, compaction, memory APIs, source authority, identity resolution, tool execution, human approval, traces, and evals.

Use adaptive model behavior for ambiguous interpretation, context selection, tool choice, memory retrieval, task decomposition, plan revision, recovery, and synthesis.

When handing work to a coding agent, require it to classify every change as one of: deterministic workflow, augmented LLM call, agent loop, multi-agent/subagent system, tool or tool registry, skill, memory subsystem, source lane, identity layer, context engine, durable execution layer, guardrail/human-review layer, cross-agent coordination layer, attention policy, adoption state, or eval/observability layer.

The practical anti-pattern is not determinism. The anti-pattern is using deterministic branch logic where the system was supposed to rely on adaptive policy plus the right tools, memories, and skills.

For operating systems that serve an organization or long-lived project, add one more anti-pattern: collapsing every artifact into memory. Raw sources, structured truth, retrieval indexes, human-readable synthesis, sidecar helpers, candidate signals, and outbound reports have different authority. Treating them as the same thing eventually makes the agent confidently wrong.

---

## Causal depth: proximate and ultimate causes

Agentic debugging must distinguish proximate causes from ultimate causes.

A proximate cause explains the immediate symptom:

- a timeout fired
- a parser missed a field
- a Slack post duplicated
- a subagent acted without context
- a workflow chose a brittle branch
- a retry loop amplified a failure

An ultimate cause explains why the system allowed that failure shape to exist:

- the wrong layer owned the decision
- memory or prior-action state was not consulted
- source authority was unclear
- the context engine did not retrieve the decisive fact
- the tool contract was too vague
- the idempotency, budget, or approval boundary was missing
- multi-agent ownership was ambiguous
- traces or evals could not preserve and replay the failure

Coding agents should not stop at the first true local explanation. A proximate cause can be accurate and still be insufficient. The acceptance standard for a serious incident, architecture review, or multi-agent workflow bug is a causal ladder deep enough to identify the missing contract.

Use this ladder before declaring root cause:

1. What user-visible symptom or system invariant failed?
2. What local component, tool, agent, state transition, or model decision immediately caused it?
3. What did that component believe, omit, or assume?
4. What context, memory, source authority, tool contract, or coordination state should have changed the decision?
5. Which harness boundary should have made the unsafe path impossible or reviewable?
6. Why did existing traces, tests, evals, health checks, or reviews fail to catch it?
7. What durable contract, fixture, replay, eval, ownership rule, or adoption gate prevents the whole failure class?

If the investigation cannot answer the deeper layers, say so. Report the causal ladder and name the remaining uncertainty instead of confidently presenting another proximate cause as root cause.

This matters more in multi-agent systems. Patching every edge case at every agent boundary creates a thicket of local fixes and contradictory behavior. Prefer a shared contract, source-of-truth rule, memory/writeback rule, coordination protocol, or eval fixture that makes the failure class harder to reproduce across all agents.

---

## Modularity, parallelization, and seam design

This section is a peer of "Core architecture" and "Causal depth," not an aside. The reason it deserves its own section is that the failure mode it describes does not look like a failure when it happens. It looks like progress.

### The asymmetry

Coding agents are rewarded by the local diff: tests pass, the change is small, the task is declared done. The tokens spent declaring a clean module seam are visible inside the task. The cost of *not* declaring the seam is invisible inside the task and lands later, in a different session, on a different agent, when several callers have come to depend on the leaked internal.

```text
declare a seam now:           cost ~ linear (one contract + a few lines of glue)
untangle a shortcut later:    cost ~ super-linear (callers x editors x dependent facts)
```

Humans hold this asymmetry in working memory because they have lived through it. Coding agents do not. They optimize for the diff in front of them and for the test that runs in the next thirty seconds. The harness is therefore the right place to install the bias.

### What gets built on top of seams

Several patterns in this architecture only work if seams exist:

```text
parallelization        : two agents cannot work on the same surface in parallel without colliding
                         unless the surface has a declared seam between their work
reflection             : a self-critique pass needs an interface to critique against
                         (was the seam respected? was a shortcut introduced?)
exception classes      : graceful degradation needs a contract that says what partial
                         results are acceptable when one module fails
A2A contracts          : "agent A asks agent B for X" is folklore unless X has a schema
cost-aware routing     : escalate-vs-spillover-vs-degrade requires a contract for what
                         each lane is allowed to return
learning loops         : you cannot promote a working pattern into a skill if the pattern
                         is buried inside a tightly coupled blob
prioritization         : task queues need work units that can be reasoned about
                         independently, which requires seams between units
```

Modularity is therefore not one pattern among many. It is the substrate. Skipping it does not make the system simpler; it makes the other patterns impossible.

### Six coupling smells

A change that exhibits any of these smells is creating coupling. The harness should make these visible at review time, not at incident time.

1. **God-object state bag.** A new function takes a `context`, `state`, `request`, or similarly named bag and reads four or more fields from it. The function does not depend on the bag; it depends on the four fields. Pass the four fields.
2. **Reaching through a module to read its internals.** Module A imports module B and accesses `B._internal_thing` or a field that is conventionally private. The author justifies it as "it is right there." This is the most reliable predictor of expensive future untangling.
3. **Runtime type-switch on payload.** A function receives an opaque payload and switches on a `kind`, `type`, or `event_name` field, dispatching to N branches. Each branch knows about the others by absence. Each new branch is a coupling event. Prefer a registry of handlers keyed by type, where each handler is independently addressable.
4. **Hidden temporal dependency.** Function A must be called before function B, but the requirement is encoded only in the order they appear in the calling code. Make the dependency explicit: B accepts the output of A as a typed input, or A is composed into B, or a state machine refuses B before A.
5. **"Just one more parameter" creep.** A function gains its sixth, seventh, eighth optional parameter, each added by a different agent in a different session for a different caller. Each parameter is conditionally read and conditionally meaningful. Either the function is doing several jobs (split it) or the parameters belong on a typed config object that only includes the fields actually used by each caller.
6. **Test that requires more than one module to instantiate.** A unit test imports four modules to construct the system under test. The test is honest about the coupling: there is no seam between those modules. Fix the seam, not the test.

### The seam-declaration rule

Every non-trivial change brief must answer four questions before code is written. This goes in the architecture brief alongside component classification and harness/policy split:

```text
1. Modules touched
   Which modules does this change read, write, or import?

2. Interfaces depended on
   Which contracts (function signatures, schemas, message types, tool contracts,
   memory APIs, source-authority lookups) does this change consume?

3. Interfaces defined or changed
   Which contracts does this change introduce, modify, deprecate, or extend?
   For each, what is the public surface and what is intentionally private?

4. Substitutability
   What would have to change if the implementation behind each interface were
   swapped (different store, different model, different transport, different
   provider)? If the answer is "many things in many places," the seam is in the
   wrong place.
```

A coding agent that cannot answer these questions has not understood the change yet. That is not a stylistic preference. It is the precondition for the other harness primitives to work.

### Parallelization as the payoff

The reason this section is named "Modularity, parallelization, and seam design" rather than just "Modularity" is that parallelization is the operational payoff that makes the up-front cost visible. A codebase where two agents collide on shared files every session has a seam problem, not a coordination problem. The right fix is not better merge tooling; it is to find which interface is missing and declare it.

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
```

Parallelization is therefore both a pattern and a diagnostic. If the system cannot be worked on in parallel without folklore-level coordination, the seams are wrong.

### Reflection as the safeguard

Section 5.14 (Reflection) formalizes the per-task self-critique loop. The required reflection checklist explicitly includes:

```text
Did this change introduce any of the six coupling smells?
Did this change reach across a module boundary that previously had a seam?
Did this change add a parameter, branch, or field that another module now
  depends on by absence rather than by contract?
If a future task had to swap the implementation behind any interface this
  change touches, what would have to change with it?
```

A reflection pass that cannot answer "no" to the first three and bound the answer to the fourth is not done.

### What this section is not

This section is not a license to invent abstractions for hypothetical future requirements. The bias is toward declaring seams *for the modules this change actually touches*, not toward speculative interface design. Three similar lines is better than a premature abstraction that picks the wrong axis. The cost asymmetry argument applies to seams that turn out to matter; the canonical signal that a seam matters is that more than one caller needs the contract or more than one agent will edit on either side of it.

The corresponding anti-pattern is in section 9.9 ("Convenient coupling"). The corresponding field lesson is in section 12.10 ("Modularity is a runtime property"). The detailed contract is in `docs/modularity-and-seams.md` in the rebuild pack.

---

## Mermaid diagrams

### Runtime harness architecture

```mermaid
graph TD
    U[User or external event] --> I[Intake and request normalization]
    I --> CE[Context engine]
    CE --> RP[Repo and workspace context]
    CE --> MEM[Memory search and retrieval]
    CE --> SK[Skill registry and skill loading]
    CE --> TR[Tool registry and tool schemas]
    CE --> CP[Compaction and relevance policy]
    CE --> MP[Model-owned adaptive policy]

    MP -->|choose tool| GC[Guardrails and permission checks]
    GC -->|allowed| TE[Tool executor]
    GC -->|risky or ambiguous| HA[Human approval gate]
    HA --> TE
    TE --> OBS[Observation and tool result]
    OBS --> CK[Checkpoint and state update]
    CK --> TRACE[Trace, logs, eval hooks]
    OBS --> MP

    MP -->|needs specialist| SA[Subagent with isolated context]
    SA --> MP
    MP -->|final answer or action plan| OUT[User-visible output or side effect]
    OUT --> PERSIST[Persistence: transcript, memory candidates, artifacts]
```


### Decision boundary: workflow, augmented model call, agent, or multi-agent system

```mermaid
graph LR
    A[Requirement] --> B{Is the next step knowable in advance?}
    B -->|Yes| C[Deterministic workflow]
    B -->|No| D{Is uncertainty local and bounded?}
    D -->|Yes| E[Augmented LLM call with structured output]
    D -->|No| F[Agent loop]
    F --> G{Does it need separate context, tools, or ownership?}
    G -->|No| H[Single agent plus tools, memory, skills]
    G -->|Yes| I[Subagent or multi-agent pattern]

    C --> J[Validate with unit and integration tests]
    E --> K[Validate with schema checks and targeted evals]
    H --> L[Validate tool choice, memory use, stop conditions, recovery]
    I --> M[Validate delegation, handoffs, permissions, traceability]
```


### Coding-agent workflow before implementation

```mermaid
sequenceDiagram
    participant C as Coding agent
    participant R as Repo instructions
    participant A as Architecture docs
    participant T as Tool catalog
    participant S as Skill registry
    participant M as Memory schema
    participant E as Evals

    C->>R: Read AGENTS.md / CLAUDE.md
    C->>A: Read agentic architecture docs
    C->>T: Inspect available and missing tools
    C->>S: Inspect reusable skills and when to load them
    C->>M: Inspect memory read/write/promotion rules
    C->>E: Inspect required eval matrix
    C->>C: Classify component and split harness-owned vs model-owned decisions
    C->>C: Implement without replacing adaptive policy with brittle routing
    C->>E: Add tests/evals for tool choice, memory, context, stop conditions, failures
```




### Source lane and operating truth architecture

```mermaid
graph TD
    RS[Raw source lanes] --> ID[Identity and entity resolution]
    ID --> CL[Source-backed claim extraction]
    CL --> AUTH[Source authority and conflict policy]
    AUTH --> TRUTH[Structured truth store]
    AUTH --> SIG[Candidate signals and open questions]
    TRUTH --> RET[Retrieval indexes]
    TRUTH --> SYN[Human-readable synthesis]
    RET --> CE[Context engine]
    SYN --> CE
    SIG --> REVIEW[Review and promotion queues]
    CE --> POL[Model-owned policy]
    POL --> ACT[Actions, drafts, alerts, or questions]
    ACT --> ATTN[Attention and approval gates]
    ATTN --> OUT[User-visible output or external side effect]
    OUT --> TRACE[Trace, checkpoint, eval, and learning record]
```

### Single-file to multifile rebuild path

```mermaid
graph TD
    SF[Single Markdown source] --> M[Manifest: paths, hashes, empty dirs]
    SF --> D[Diagrams and architecture explanation]
    SF --> P[Embedded file payloads]
    P --> Parser[Rebuild parser]
    M --> Parser
    Parser --> Repo[Multifile repo architecture pack]
    Repo --> AG[AGENTS.md]
    Repo --> CL[CLAUDE.md]
    Repo --> Docs[docs/]
    Repo --> Config[.agentic/*.yaml]
    Repo --> Skills[.claude/skills/*/SKILL.md]
    Repo --> PR[.github/pull_request_template.md]
```


---

## How to rebuild the multifile pack

Save this file as `agentic_architecture_singlefile.md`. Then copy the script below into `rebuild_agentic_architecture.py` and run:

```bash
python rebuild_agentic_architecture.py agentic_architecture_singlefile.md ./agentic_architecture_pack
```

Use `--overwrite` if the target files already exist.

```python
#!/usr/bin/env python3
"""
Rebuild the multifile agentic architecture pack from the single Markdown source.

Usage:
  python rebuild_agentic_architecture.py agentic_architecture_singlefile.md ./agentic_architecture_pack
  python rebuild_agentic_architecture.py agentic_architecture_singlefile.md ./agentic_architecture_pack --overwrite
"""
from pathlib import Path
import argparse
import hashlib
import re

START_RE = re.compile(
    r'<!-- AGENTIC_BUNDLE_FILE_START path="([^"]+)" sha256="([a-f0-9]{64})" bytes="(\d+)" trailing_newline="(true|false)" -->'
)
DIR_RE = re.compile(r'<!-- AGENTIC_BUNDLE_DIR path="([^"]+)" -->')
FENCE_RE = re.compile(r'^`{8,}|^~{8,}')


def extract_fenced_payload(block: str, trailing_newline: bool) -> str:
    lines = block.splitlines(keepends=True)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    if not lines or not FENCE_RE.match(lines[0].strip()):
        raise ValueError("Missing opening long fence for payload")
    fence = lines.pop(0).strip().split()[0]
    if not lines or lines[-1].strip() != fence:
        raise ValueError("Missing closing long fence for payload")
    lines.pop()
    payload = "".join(lines)
    if not trailing_newline and payload.endswith("\n"):
        payload = payload[:-1]
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("single_file", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    source = args.single_file.read_text(encoding="utf-8")
    args.out_dir.mkdir(parents=True, exist_ok=True)

    for match in DIR_RE.finditer(source):
        (args.out_dir / match.group(1)).mkdir(parents=True, exist_ok=True)

    count = 0
    for match in START_RE.finditer(source):
        path = match.group(1)
        expected_sha = match.group(2)
        expected_bytes = int(match.group(3))
        trailing_newline = match.group(4) == "true"
        end_marker = f'<!-- AGENTIC_BUNDLE_FILE_END path="{path}" -->'
        end_index = source.find(end_marker, match.end())
        if end_index == -1:
            raise ValueError(f"Missing end marker for {path}")

        payload = extract_fenced_payload(source[match.end():end_index], trailing_newline)
        data = payload.encode("utf-8")
        actual_sha = hashlib.sha256(data).hexdigest()

        if actual_sha != expected_sha:
            raise ValueError(f"SHA mismatch for {path}: {actual_sha} != {expected_sha}")
        if len(data) != expected_bytes:
            raise ValueError(f"Byte mismatch for {path}: {len(data)} != {expected_bytes}")

        target = args.out_dir / path
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not args.overwrite:
            raise FileExistsError(f"{target} exists. Re-run with --overwrite to replace files.")
        target.write_bytes(data)
        count += 1

    print(f"Rebuilt {count} files into {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

```

The rebuild parser checks each file payload against the SHA-256 and byte count in the manifest. If a coding agent edits embedded payloads manually, it must update the manifest values or the parser will reject the rebuild.

---

## Repository tree

```text
agentic_architecture_pack/
├── .agentic/
│   ├── context_policy.yaml
│   ├── coordination_policy.yaml
│   ├── eval_matrix.yaml
│   ├── memory_schema.yaml
│   ├── skill_registry.yaml
│   ├── source_authority.yaml
│   └── tool_catalog.yaml
├── .claude/
│   └── skills/
│       ├── build-agent-eval/
│       │   └── SKILL.md
│       ├── design-agent-memory/
│       │   └── SKILL.md
│       ├── design-agent-tool/
│       │   └── SKILL.md
│       ├── design-context-engine/
│       │   └── SKILL.md
│       ├── design-source-lane/
│       │   └── SKILL.md
│       └── review-agentic-architecture/
│           └── SKILL.md
├── .github/
│   └── pull_request_template.md
├── docs/
│   ├── a2a-contracts.md
│   ├── agentic-coding-for-agentic-systems.md
│   ├── agentic-pattern-catalog.md
│   ├── agentic-systems-engineering.md
│   ├── context-engineering.md
│   ├── cost-aware-routing.md
│   ├── cross-agent-operating-model.md
│   ├── durable-execution.md
│   ├── evals.md
│   ├── exception-taxonomy.md
│   ├── learning-loops.md
│   ├── memory-architecture.md
│   ├── modularity-and-seams.md
│   ├── QUICK_REFERENCE.md
│   ├── reflection-and-planning.md
│   ├── skills.md
│   ├── source-authority-and-truth-lanes.md
│   ├── subagents.md
│   ├── task-prioritization.md
│   └── tool-design.md
├── tests/
│   └── agentic/
├── AGENTS.md
└── CLAUDE.md
```

---

## Bundle manifest

```yaml
files:
  - path: AGENTS.md
    bytes: 7838
    sha256: 31f33c40eaa0484a3d5ed8ff0d136c6c8b7cc54685c0279019a8fa5baa0f6a1c
    trailing_newline: true
  - path: CLAUDE.md
    bytes: 3661
    sha256: 61c0d887af174770b7f7944542c8ca3584190f075c98f31c0e90df38d04f0ccf
    trailing_newline: true
  - path: docs/agentic-coding-for-agentic-systems.md
    bytes: 67673
    sha256: 4eb30bb8698fc8887b98a3fd8d5f267c9520c6fc708d9f54eb001fe78b0aa88a
    trailing_newline: true
  - path: docs/agentic-systems-engineering.md
    bytes: 61345
    sha256: 40b1b17398db694e8e6f75e5b0a8684be4f84ae8ec2b56918e35690881f25506
    trailing_newline: true
  - path: docs/agentic-pattern-catalog.md
    bytes: 15046
    sha256: a1aab1a86a5df2ac0e247fd33760247ec0c0eedd7694358676de4c30742fdea1
    trailing_newline: true
  - path: docs/tool-design.md
    bytes: 3336
    sha256: a64f361ba3d00619ae6076efdd52b477a8f103f5286490b03f4793062973cf98
    trailing_newline: true
  - path: docs/memory-architecture.md
    bytes: 1795
    sha256: fa484a8d62855c26786368c18f4c055e87479beb2ebc2ce1fe01e40456343312
    trailing_newline: true
  - path: docs/context-engineering.md
    bytes: 2788
    sha256: 4683e02a659f84dfa5ba795ea44108009da302c4ca9e9b05a0076ad8dc2e7e9a
    trailing_newline: true
  - path: docs/skills.md
    bytes: 1266
    sha256: cc68b3f135913c077501bf75d58eaa903ebab5c52ecd2c203d43461e4ae27cbe
    trailing_newline: true
  - path: docs/durable-execution.md
    bytes: 1276
    sha256: ff6f53b55383976ddcf89a1160b166afc3ceb62c3ff673a7cb852931d92e2dc6
    trailing_newline: true
  - path: docs/evals.md
    bytes: 3104
    sha256: 3a63fab6cb65308283c1741bee734d81e8be8d17b0dbe40afeb7cdc596ee3b27
    trailing_newline: true
  - path: docs/subagents.md
    bytes: 1044
    sha256: 57e629f9bc29259cf8fcf52837774fd10a6207b31c507e537ab40bbbc9e5a397
    trailing_newline: true
  - path: .agentic/context_policy.yaml
    bytes: 835
    sha256: c7ee70831d13f74af3b00f6218e7d8bba412f9f26977af4eb6e03c20018568d6
    trailing_newline: true
  - path: .agentic/tool_catalog.yaml
    bytes: 3619
    sha256: d459cd2e8721766914dfdf777d24e78c21eb6420b6469d86b6fcb58d0f58fa66
    trailing_newline: true
  - path: .agentic/memory_schema.yaml
    bytes: 1150
    sha256: 7ec7f08c887daf2ee78352d3dd44f9466c5424549cc998201315a9d4191a08f6
    trailing_newline: true
  - path: .agentic/skill_registry.yaml
    bytes: 1144
    sha256: 2a272ab199ed59cd3e8efef5b8c5d168466d3cf220dd20fb2241f76f227abe85
    trailing_newline: true
  - path: .agentic/eval_matrix.yaml
    bytes: 2050
    sha256: 2195ead1d60217ceadaf59bbfbb2c5b6b4c44ba0ff97260ddd2036ac0328b798
    trailing_newline: true
  - path: .claude/skills/design-agent-tool/SKILL.md
    bytes: 623
    sha256: bf6e0c0068122f1eae8a97c2ef5e19650456d1182bedf98a100c29874626b077
    trailing_newline: true
  - path: .claude/skills/design-agent-memory/SKILL.md
    bytes: 692
    sha256: bc252292cace006a3496b0e9e547a053100f63da47f4f1b36b5135b9ae69c5d1
    trailing_newline: true
  - path: .claude/skills/design-context-engine/SKILL.md
    bytes: 624
    sha256: 34e530f38a210b85d75a5cd8ee214f8a80880fc08ac42d6882b6febfda4e1bd4
    trailing_newline: true
  - path: .claude/skills/build-agent-eval/SKILL.md
    bytes: 574
    sha256: 6459b4c53c093e69aca8f1fec6f0e9d4ae588bc41abb1fc55ebf080f7251c60d
    trailing_newline: true
  - path: .claude/skills/review-agentic-architecture/SKILL.md
    bytes: 915
    sha256: 7a5543668a3f9cf1f3a8a290f141ca7434d54bc20abf38514f5ed731c322814a
    trailing_newline: true
  - path: .github/pull_request_template.md
    bytes: 795
    sha256: b3df7fd37f8120c24dd9aaada3d7ec31c7138cfd7b16abc542f34cecc8a08d4f
    trailing_newline: true
  - path: .agentic/source_authority.yaml
    bytes: 1487
    sha256: cf8341ebcf45ab5618e039a19931febb210ae1a72451caa5facbf6bf01fb4f57
    trailing_newline: true
  - path: .agentic/coordination_policy.yaml
    bytes: 711
    sha256: 85968b5c5e80a3a6441ee8505274b9a8a4ca31e4bee6b5cf588bec6dfcc94286
    trailing_newline: true
  - path: docs/source-authority-and-truth-lanes.md
    bytes: 3286
    sha256: 4503f5bd98d26c5a4a698237ea14d83334af8e495c9294a395dbedfe51f8cd55
    trailing_newline: true
  - path: docs/cross-agent-operating-model.md
    bytes: 2541
    sha256: 7e8387a472cc0fc7710e257fa877592262e9b1f3ae61e9a63a61fe01c04d79fc
    trailing_newline: true
  - path: .claude/skills/design-source-lane/SKILL.md
    bytes: 1208
    sha256: a26e7e4d13a5d4775fe85e265fd7a74083e75d28faf3fc541955f199c0ba9460
    trailing_newline: true
  - path: docs/modularity-and-seams.md
    bytes: 9239
    sha256: 8515130c76849d2c5deb27deb5c1ca67199a5553cb09237b684dc81a2d86d73b
    trailing_newline: true
  - path: docs/reflection-and-planning.md
    bytes: 6753
    sha256: aa7905927bf871cb0e12a05ef4daf0147d196c8af829386d6cec903ed3487839
    trailing_newline: true
  - path: docs/exception-taxonomy.md
    bytes: 5173
    sha256: a7cd06584f134b521da2a02183f4f9fe22977ea7fbd3661a055c69c2343a96c3
    trailing_newline: true
  - path: docs/a2a-contracts.md
    bytes: 6980
    sha256: 950e9d057cac968230e8b3969e70cc0f3fcc1fc0712660c0279101f4fe951d31
    trailing_newline: true
  - path: docs/cost-aware-routing.md
    bytes: 5318
    sha256: f699d090bbc0f2bceb41aafbef99a57182f5814fb1eab60370689762707d15f4
    trailing_newline: true
  - path: docs/learning-loops.md
    bytes: 5311
    sha256: 3cc2113b22c63666e76787eaef9664b962d8b437a761f539208d8c605da44d88
    trailing_newline: true
  - path: docs/task-prioritization.md
    bytes: 5331
    sha256: 6b7d5db57a2d032f0cf83e26044493d2b9fcc7651c9bb8ef448c07c217bbf6ec
    trailing_newline: true
  - path: docs/QUICK_REFERENCE.md
    bytes: 15038
    sha256: cae3501aa3bcd04020ad3a58f278272d1e016dfb768a465f243a4828bd7a0329
    trailing_newline: true
empty_directories:
  - tests/agentic/
```

---

## Research boundary: leaked or derivative Claude Code source

This architecture pack intentionally does not include, quote, port, summarize line-by-line, or depend on leaked Claude Code source or derivative codebases that advertise themselves as rebuilt from leaked source.

The admissible inputs are public product documentation, public architecture discussions, public framework docs, field experience, and first-principles engineering analysis. The goal is to learn the agentic harness pattern without creating legal, ethical, or supply-chain dependence on unauthorized proprietary material.

Clean-room public analysis can still inform high-level architecture if it is not copied from proprietary code. But the safer basis for a reusable engineering artifact is public documentation and independent design: context engines, tool registries, skills, memory schemas, source authority, hooks, subagents, checkpoints, evals, human approval gates, and cross-agent coordination.

---

## Reference sources used for architecture framing

These are reference sources for the architecture concepts, not payload dependencies. They should be re-checked by a coding agent when current implementation details matter.

- OpenAI Codex `AGENTS.md` docs: https://developers.openai.com/codex/guides/agents-md
- Anthropic Building Effective Agents: https://www.anthropic.com/research/building-effective-agents
- Anthropic context engineering for agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic writing tools for agents: https://www.anthropic.com/engineering/writing-tools-for-agents
- Claude Code skills docs: https://code.claude.com/docs/en/skills
- Claude Code subagents docs: https://code.claude.com/docs/en/sub-agents
- Claude Code hooks docs: https://code.claude.com/docs/en/hooks
- LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
- OpenClaw agent loop docs: https://docs.openclaw.ai/concepts/agent-loop
- OpenClaw context docs: https://docs.openclaw.ai/concepts/context
- OpenClaw memory docs: https://docs.openclaw.ai/concepts/memory
- Antonio Gulli, Agentic Design Patterns: https://futurepulseai.blog/wp-content/uploads/2025/12/agentic_design_patterns.pdf
- Trevin Chow, 10 Principles for Agent-Native CLIs: https://trevinsays.com/p/10-principles-for-agent-native-clis
- Cloudflare, Building a CLI for all of Cloudflare: https://blog.cloudflare.com/cf-cli-local-explorer/
- LangChain, Agent observability needs feedback to power learning: https://www.langchain.com/blog/agent-observability-needs-feedback-to-power-learning
- lat.md, Agent Lattice knowledge graph: https://github.com/1st1/lat.md

---

## Embedded file payloads

Each payload is wrapped in markers that the rebuild script can parse. Do not remove the `AGENTIC_BUNDLE_FILE_START` or `AGENTIC_BUNDLE_FILE_END` comments unless you intend to stop using this file as a reconstructable source.

<!-- AGENTIC_BUNDLE_DIR path="tests/agentic/" -->

---

### File: `AGENTS.md`

<!-- AGENTIC_BUNDLE_FILE_START path="AGENTS.md" sha256="31f33c40eaa0484a3d5ed8ff0d136c6c8b7cc54685c0279019a8fa5baa0f6a1c" bytes="7838" trailing_newline="true" -->
`````````` markdown
# AGENTS.md

This repository builds agentic operating systems.

**Cold-start (always read first, ~5K tokens combined with this file):**

- docs/QUICK_REFERENCE.md — lossy distillation of the full architecture pack (rules only, no examples)

**Deep docs (load only the topic you are actually touching):**

- docs/agentic-coding-for-agentic-systems.md — full architecture, executive thesis, worked anti-patterns, field lessons, canonical prompt
- docs/agentic-systems-engineering.md — engineering posture for coding agents
- docs/agentic-pattern-catalog.md — pattern selection, agent-native CLIs, context packets, knowledge graphs, and parallel-agent repo shape
- docs/source-authority-and-truth-lanes.md — when authority work
- docs/cross-agent-operating-model.md — when multi-agent or coordination work
- docs/tool-design.md — when tool work
- docs/memory-architecture.md — when memory work
- docs/context-engineering.md — when context work
- docs/skills.md — when skill work
- docs/subagents.md — when subagent work
- docs/durable-execution.md — when checkpoint, retry, or replay work
- docs/evals.md — when eval work
- docs/modularity-and-seams.md — when seams, refactors, or non-trivial structural change
- docs/reflection-and-planning.md — when planning a non-trivial change (always at end of one)
- docs/exception-taxonomy.md — when failure paths, retry, fallback, degradation
- docs/a2a-contracts.md — when agent-to-agent message work
- docs/cost-aware-routing.md — when paid lane or routing work
- docs/learning-loops.md — when skill promotion or system-level critique
- docs/task-prioritization.md — when queue, scheduling, or staleness work

If you are constrained on context, the quick reference above this list is enough for orientation; the deep docs are reference, not required reading.

Core rule: deterministic harness, adaptive policy.

Use deterministic code for schemas, permissions, idempotency, budgets, checkpoints, memory APIs, source authority, identity resolution, context assembly, tool execution, human approval, traces, and evals.

Use model-owned adaptive behavior for ambiguous intent, context gathering, tool choice, memory retrieval, task decomposition, plan revision, recovery, and synthesis.

Second rule: truth, retrieval, recall, synthesis, sidecars, candidate signals, and external reports are different architectural roles. Do not let a convenient artifact become a source of truth by accident.

Third rule: distinguish proximate causes from ultimate causes. Do not stop at the first true local explanation. For incidents, debugging, and multi-agent workflow failures, follow the causal ladder until you can name the missing contract in memory, context, tool semantics, source authority, durable state, ownership, guardrails, or evals.

Fourth rule: coupling cost is asymmetric. Declaring a clean module seam now is roughly linear; untangling shortcut-coupled code later is super-linear in the number of callers and editors involved. Every non-trivial change declares the seams it touches, defines, or changes. Reaching across module boundaries to read internals, runtime type-switches on opaque payloads, and "just one more parameter" creep are coupling smells, not shortcuts. The bias is forward: declare the seam now even when the local diff would be smaller without it.

Fifth rule: reflect before declaring done. Run the section 5.14 reflection checklist on every non-trivial change: goal drift, coupling and seams, shortcuts, hidden state, failure modes, tests and evals, causal depth. Record the answers. Hidden gaps are worse than known gaps because the next agent inherits them without warning.

Sixth rule: failures are classes, not surprises. Every retry, fallback, or degraded-result path attaches to one of three exception classes (recoverable, degraded, unrecoverable) explicitly. Silent degradation is a bug. Silent paid spillover is a bug. Silent retry past the budget is a bug.

Seventh rule: agent-to-agent messages need contracts. Schema, direction, idempotency, versioning, authority, failure attribution, audit. A2A traffic without a contract is folklore that breaks silently the next time either side is edited.

Do not replace open-ended agent behavior with brittle keyword routing, regex parsing, lookup tables, or fixed orchestration unless the task is genuinely deterministic and tested as such. Typed routing and fallback are valid harness patterns only when they are explicit, budgeted, traceable, eval-covered, and approved for their cost/risk class.

Before coding, classify the component as one of:

1. deterministic workflow
2. augmented LLM
3. agent loop
4. multi-agent/subagent system
5. tool or tool registry
6. skill
7. memory subsystem
8. source lane or source authority layer
9. identity resolution layer
10. context engine
11. durable execution layer
12. guardrail or human-review layer
13. cross-agent coordination layer
14. attention or notification policy
15. adoption-state change
16. eval/observability layer
17. agent-native CLI or tool surface
18. repository structure / parallel-agent seam
19. learning-loop or feedback pipeline

For source lanes, define raw capture, identity linking, claim extraction, freshness, authority, contradiction handling, health checks, and promotion rules before wiring the lane into agent answers.

For multi-agent work, ensure one explicit owner or integrator controls shared-file edits and final verification. Contributors should return evidence-backed proposals unless given a disjoint write set.

Define done in system terms, not personal activity terms. For autonomous behavior, state the acceptance test before implementation, distinguish manual proof from system/autonomous proof, and list untested layers as explicit gaps.

For live or long-running systems, convert incidents into enforceable contracts. Backpressure, budgets, caller attribution, adoption state, rollback, and human attention are harness concerns, not prompt vibes. Never add silent paid fallbacks, silent provider spillover, or production promotion from one good demo.

Root-cause work is not done when you identify a proximate bug. Ask 6-7 layers deep if needed: what failed, what believed the wrong thing, what context or memory was missing, which harness boundary should have prevented it, why evals/traces missed it, and what durable contract prevents the class.

In the final summary, state:

- component classification
- model-owned decisions
- deterministic harness responsibilities
- tools available and tools missing
- memory behavior
- source authority and truth/synthesis boundaries
- identity resolution behavior
- context behavior
- skills used or added
- guardrails and approvals
- cross-agent ownership or adoption-state changes
- attention/notification behavior
- backpressure, budget, and fallback behavior
- adoption state and rollback plan
- causal ladder from proximate cause to ultimate cause when debugging or repairing failures
- acceptance proof, manual-proof gaps, and tests/evals added
- plan and goal as observable system behavior, with goal-drift check at the end
- seam declaration: modules touched, interfaces depended on, interfaces defined or changed, substitutability
- exception classes in scope; behavior under slow, unavailable, partial, or garbage external responses
- A2A contract changes (schema, direction, idempotency, versioning, authority, audit) if any
- routing and cost lane chosen and why; degraded or fallback lane if any
- prioritization inputs (urgency, importance, preemptability, cost, staleness) for queued work
- learning destination for any recurring pattern, candidate skill, missing eval, or contract change surfaced
- reflection checklist results: goal drift, coupling and seams, shortcuts, hidden state, failure modes, tests and evals, causal depth
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="AGENTS.md" -->

---

### File: `CLAUDE.md`

<!-- AGENTIC_BUNDLE_FILE_START path="CLAUDE.md" sha256="61c0d887af174770b7f7944542c8ca3584190f075c98f31c0e90df38d04f0ccf" bytes="3661" trailing_newline="true" -->
`````````` markdown
# CLAUDE.md

Read AGENTS.md first. For context-constrained sessions, the cold-start trio (this file + AGENTS.md + docs/QUICK_REFERENCE.md) is ~5K tokens and contains every doctrinal rule. Load deep docs only for the topic you are actually touching.

This repo builds agentic operating systems.

Use deterministic code for the harness: schemas, permissions, idempotency, state, checkpoints, compaction, source authority, identity resolution, tool execution, human approval, traces, and evals.

Use model-owned adaptive behavior for ambiguous intent, context gathering, memory retrieval, tool choice, plan revision, recovery, and synthesis.

Do not implement open-ended agent behavior as keyword routers, regex intent detection, hardcoded branches, or giant always-loaded prompts unless explicitly justified and tested.

Do not collapse source-of-truth stores, retrieval indexes, recall memory, human-readable synthesis, sidecars, and candidate signals into one vague memory layer. Name the role of each artifact.

Distinguish proximate causes from ultimate causes. When debugging failures or reviewing multi-agent behavior, do not stop at the first plausible local explanation. Go deep enough to identify the missing contract in memory, context, source authority, tool design, durable state, ownership, guardrails, or evals.

Coupling cost is asymmetric. Every non-trivial change declares the seams it touches, defines, or changes. Reaching across module boundaries to read internals, runtime type-switches on opaque payloads, and "just one more parameter" creep are coupling smells, not shortcuts. Decoupling later is super-linear in callers and editors; declare the seam now. See docs/modularity-and-seams.md.

Reflect before declaring done. Run the reflection checklist on every non-trivial change: goal drift, coupling and seams, shortcuts, hidden state, failure modes, tests and evals, causal depth. Record the answers. Hidden gaps are worse than known gaps. See docs/reflection-and-planning.md.

Failures are classes, not surprises. Every retry, fallback, and degraded-result path attaches to one of three exception classes (recoverable, degraded, unrecoverable) explicitly. Silent degradation, silent paid spillover, and silent retry past budget are bugs. See docs/exception-taxonomy.md.

Agent-to-agent messages need contracts: schema, direction, idempotency, versioning, authority, failure attribution, audit. A2A traffic without a contract is folklore that breaks silently. See docs/a2a-contracts.md.

Routing decisions are recorded with the task. Lane choice combines difficulty, evidence sensitivity, consequence, budget state, lane health, and explicit override. No silent paid spillover. See docs/cost-aware-routing.md.

Recurring findings have destinations: candidate skill, contract change proposal, missing eval, candidate signal, or deprecation. A finding without a destination is a smell. See docs/learning-loops.md.

Queued tasks declare urgency, importance, preemptability, cost, and staleness. First-come-first-served is not the default; it is folklore. See docs/task-prioritization.md.

For any agentic change, inspect relevant tools, skills, memory, source lanes, identity policy, context policy, coordination rules, durability, and evals before editing code.

Define done as observable system behavior. A manual one-off proof is not completion for autonomous behavior; record the system acceptance test, replay/eval evidence, and known gaps. Treat cost controls, provider fallback policy, and adoption state as safety-critical harness design.

Keep this file short. Put reusable procedures in skills. Put detailed architecture in docs/.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="CLAUDE.md" -->

---

### File: `docs/agentic-coding-for-agentic-systems.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/agentic-coding-for-agentic-systems.md" sha256="4eb30bb8698fc8887b98a3fd8d5f267c9520c6fc708d9f54eb001fe78b0aa88a" bytes="67673" trailing_newline="true" -->
`````````` markdown
# Agentic Coding for Agentic Systems

## Why coding agents default to von Neumann architecture, and how to give them the harness, memory, tools, and skills needed to build adaptive systems

Version: 1.2
Audience: human technical leads, coding agents, staff engineers, agent-platform teams
Recommended repo path: `docs/agentic-coding-for-agentic-systems.md`

---

## 0. Executive thesis

The near-term challenge is not simply “use AI to write code.” The challenge is using agentic coding systems such as Codex, Claude Code, Cursor-style agents, or other coding agents to build *agentic systems themselves*.

That creates a recursive architecture problem. The coding agent is itself an agent, but it has been trained and conditioned mostly on ordinary software: deterministic functions, fixed control flow, request handlers, workflow engines, regular expressions, database calls, API clients, tests, and front-end applications. Those patterns are correct for conventional software. They are often wrong when the thing being built is an adaptive agentic harness.

The failure mode is predictable:

```text
Human intent: Build an agent that can inspect context, choose tools, use memory, adapt its plan, and recover from surprises.

Coding-agent implementation: Add keyword routing, regex parsing, fixed orchestration, hardcoded branches, and a giant prompt.
```

The human thought they were asking for a system with an intelligent policy inside a controlled harness. The coding agent implemented a brittle deterministic workflow that only resembles an agent from the outside.

The correction is not “remove determinism.” The correction is:

```text
Deterministic harness. Adaptive policy.
```

Use deterministic code for schemas, permissions, budgets, checkpoints, idempotency, state, logs, tests, evals, human approval, and tool execution. Use model-owned adaptive behavior for ambiguous interpretation, context selection, tool choice, memory retrieval, task decomposition, plan revision, and synthesis.

A serious agentic system needs more than model calls. It needs a harness: context engine, tool registry, skill system, memory subsystem, source authority, identity resolution, durable execution, hooks, guardrails, traces, evals, and subagent boundaries. Coding agents must have that architecture in their context before they start editing. Otherwise they will fill the missing architecture with the idioms they know: conventional von Neumann control flow.

For systems that serve a real organization, project, or long-lived workflow, the harness also needs an operating model. The agent must know which sources are raw evidence, which stores are authoritative, which pages are synthesis, which indexes are retrieval-only, which helpers are sidecars, which workflows are experimental, and when human attention is too valuable to spend.

The strongest field lesson is that agentic failures rarely stay inside one layer. A stalled publish, runaway retry storm, false memory, or bad handoff usually crosses context, tools, state, model policy, budget, and human attention. Treat each incident as a request to improve the architecture: name the contract that was missing, preserve a replay or eval, and promote the fix only after evidence.

---

## 1. The frame: using agentic coding to build agentic systems

A conventional program is usually designed as a known sequence of operations. Even when it has branches, queues, retries, and services, its core logic is deterministic: given a state, a set of inputs, and the same external responses, the next step is specified by code.

Agentic software is different. It contains a model-driven policy that can choose among possible next actions under uncertainty. It may decide to inspect a file, search memory, call a tool, ask a human, generate a plan, revise that plan, spawn a specialist subagent, or stop. The path is not fully known when the software is written.

This does not mean agentic software is “unstructured.” It means the structure moves. In ordinary software, the structure is mostly the control flow. In agentic software, the structure is the harness around the model:

```text
ordinary program:
  control flow is the main architecture

agentic system:
  harness is the architecture
  model policy is the adaptive decision-maker inside the harness
```

The coding-agent trap is that a coding model tends to convert “ambiguous adaptive policy” into “explicit branch logic.” It does this because most software examples it has seen are built that way, and because coding tasks often reward concrete implementation over architectural uncertainty.

That is why a repo building agents needs standing architectural instructions. A one-off prompt saying “make this agentic” is too weak. The coding agent needs a durable architectural contract that it reads before editing.

---

## 2. The von Neumann lens and why it distorts agent design

The von Neumann style of computing is stored-program computing: instructions and data live in memory, and the machine executes instructions step by step. Modern software has grown far beyond the original model, but the mental pattern remains: define the data, define the functions, define the control flow, run the procedure.

That lens is valuable. It gives us tests, reproducibility, observability, safety, and debuggability. The problem appears when it becomes the only lens.

When a coding agent sees a request like:

```text
The agent should understand whether the user is asking about a portfolio company, then retrieve the right memory, inspect recent notes, choose the right diligence workflow, and produce an investment memo.
```

it may implement:

```python
if "portfolio" in user_input.lower():
    run_portfolio_company_flow()
elif "diligence" in user_input.lower():
    run_diligence_flow()
elif "memo" in user_input.lower():
    run_memo_flow()
```

That is a deterministic intent router. It can be useful for a narrow command palette. It is not a general agentic interface. It will fail when the user says, “What changed in the Convex deal since our last IC call?” or “Show me why this company is starting to look like a vertical SaaS trap.”

The user expected semantic understanding, memory retrieval, tool choice, and judgment. The implementation supplied keyword matching.

This is the central translation error:

```text
Human workflow assumption:
  “The agent will understand the work and pull the right context.”

Coding-agent implementation assumption:
  “I should encode the workflow as explicit branches.”
```

Those are not the same architecture.

---

## 3. The jagged frontier: what will improve quickly and what will remain brittle

The “bitter lesson” says that general methods that scale with compute tend to win over hand-engineered methods in the long run. For agentic systems, that implies model reasoning, tool-use competence, multimodal perception, code generation, and long-horizon planning will likely continue improving as models scale and training improves.

But the near-term frontier is jagged. Some capabilities improve faster than others. Memory, context selection, provenance, long-running state, eval reliability, safety boundaries, and tool semantics are not solved just by making the context window larger or the model more intelligent.

The practical implication is:

```text
Do not hardcode brittle substitutes for capabilities that models will soon do better.
Do build durable harnesses for bottlenecks that raw model scaling does not automatically solve.
```

### 3.1 Capabilities likely to improve with frontier models

These are places where the system should avoid premature over-engineering with brittle hand rules:

1. Natural-language understanding of user intent.
2. Tool choice under ordinary ambiguity.
3. Multi-step reasoning when observations change the plan.
4. Codebase exploration and synthesis.
5. Transforming loosely specified instructions into usable artifacts.
6. Detecting missing context and asking targeted questions.
7. Using examples to infer style, procedure, and local conventions.

For these, the harness should expose good tools and context, then let the model decide.

### 3.2 Capabilities that require explicit harness design

These are not reliably solved by “more model” alone:

1. What context gets loaded and what stays out.
2. How memories are written, scoped, retrieved, updated, contradicted, and retired.
3. Which tools exist, how they are described, and what side effects they can cause.
4. How skills are packaged, discovered, loaded, and tested.
5. How long-running tasks checkpoint and resume.
6. How side effects are made idempotent.
7. How risky actions require human review.
8. How traces and evals prove the agent is doing the right thing.
9. How subagents are isolated by role, tools, memory, and context.
10. How the system prevents context bloat and stale-memory poisoning.

This is the harness layer. It is the architecture the coding agent must be taught to build.

---

## 4. Context is not memory, and a larger context window is not a memory system

A common mistake is to treat the context window as a database. It is not. The context window is the temporary working set passed to the model for a specific inference. Memory is durable information outside that prompt that can be searched, inspected, updated, and governed.

Larger context windows help, but they do not eliminate context engineering. Long contexts can degrade because relevant information may be diluted, stale material can distract the model, and facts in the middle of long prompts may be used less reliably than facts at the beginning or end. Bigger windows can also create false confidence: “the information was in context” does not mean the model used it correctly.

Humans appear to have a different retrieval pattern. A small cue can bring a large hidden body of knowledge into awareness. We do not keep every relevant fact in immediate conscious attention. We carry a broad latent store and retrieve selectively. Agentic systems need an engineered analogue:

```text
broad memory surface area
+ fast retrieval
+ scoped context assembly
+ compaction
+ provenance
+ contradiction handling
+ just-in-time skill and tool loading
```

The agent should not see everything. It should see what it needs, know how to ask for more, and have tools to retrieve missing context.

---

## 5. The agentic harness

An agentic harness is the runtime that mediates between the model and the world. It provides affordances, constraints, state, memory, and observability.

A minimal serious harness has these layers:

```text
1. Intake and authorization
2. Context engine
3. Tool registry and tool search
4. Skill registry and skill loading
5. Memory subsystem
6. Source authority and identity resolution
7. Model policy loop
8. Tool execution sandbox
9. State, checkpointing, and replay
10. Hooks, guardrails, and human approval
11. Tracing, evals, and review
12. Attention policy and operating posture
13. Subagent or cross-agent orchestration when needed
```

### 5.1 Intake and authorization

This layer normalizes the user request and determines the allowed operating envelope.

It should answer:

```text
Who is asking?
What workspace, project, customer, or account is in scope?
What tools may be used?
What side effects are allowed?
What human approvals are required?
What cost, step, and time budgets apply?
What data boundaries apply?
```

The coding agent should not bury these policies inside scattered branches. They should be explicit harness configuration.

### 5.2 Context engine

The context engine decides what enters the model prompt.

It should assemble:

```text
system/developer instructions
repo rules
current user request
active plan/state
relevant retrieved memory
relevant files or snippets
available tool summaries
available skill summaries
recent observations
constraints and budgets
source ledger
```

It should not dump the whole repo, every prior conversation, every memory, every tool schema, and every skill body into the prompt. That produces context bloat.

A good context engine uses progressive disclosure:

```text
always loaded:
  short root instructions, current request, active state, high-priority constraints

loaded by retrieval:
  memories, documents, files, examples, prior episodes

loaded by need:
  full tool schemas, skill bodies, long references, large files

removed or compressed:
  stale messages, redundant observations, low-value intermediate work
```

The context engine should also produce a source ledger: a machine-readable list of what was included and why.

### 5.3 Tool registry and tool search

Tools are not just functions. They are the action surface of the agent.

Every tool needs a contract:

```yaml
name: memory_search
purpose: Retrieve relevant long-term memories by semantic query and filters.
when_to_use:
  - The task depends on prior user/project/company knowledge.
  - The current prompt refers to something not fully specified.
when_not_to_use:
  - The needed fact is already in the current context with clear provenance.
input_schema:
  query: string
  namespaces: string[]
  limit: integer
  freshness: optional string
output_schema:
  memories:
    - id: string
      text: string
      source: string
      confidence: number
      created_at: string
      updated_at: string
      superseded_by: optional string
side_effects: none
permission_level: read
failure_modes:
  - no relevant memory
  - conflicting memories
  - stale memory
observability:
  trace_fields: [query, namespaces, result_count, selected_ids]
```

Bad tool design produces bad agents. If the tools are vague, too broad, too slow, too dangerous, or poorly described, the model will misuse them. A deterministic API meant for a human programmer is often not a good agent tool. Agent tools need semantic affordances and clear usage boundaries.

### 5.4 Skill registry and skill loading

A skill is reusable procedural knowledge. It is not merely a prompt. A strong skill package contains:

```text
SKILL.md
examples/
scripts/
templates/
fixtures/
tests/
references/
```

Skills are for “how this kind of task is done here.” Examples:

```text
design-agent-tool
write-memory-schema
build-context-policy
create-eval-dataset
review-agentic-architecture
run-investment-memo-workflow
```

A skill should have a small metadata surface that is visible before loading the full skill:

```yaml
name: design-agent-tool
description: Use when adding or modifying a tool exposed to an agent.
triggers:
  - tool contract
  - agent affordance
  - side-effecting action
  - schema for model tool use
loads:
  - SKILL.md
  - examples/tool_contract.yaml
  - tests/tool_contract_eval.md
```

This lets the model discover that a skill exists without polluting the prompt with every skill body.

### 5.5 Memory subsystem

Memory must be designed as a governed subsystem, not an append-only note dump.

Use at least four memory types:

```text
working memory:
  current task state, plan, open questions, active artifacts

episodic memory:
  prior actions, conversations, decisions, traces, outcomes

semantic memory:
  durable facts about users, projects, companies, markets, codebase, policies

procedural memory:
  reusable methods, preferences, workflows, skills, instructions
```

Memory writes should usually be candidates before they become durable truth:

```yaml
id: mem_candidate_123
claim: "Project Alpha uses Postgres for durable agent checkpoints."
scope: [repo:alpha, subsystem:agent_runtime]
evidence:
  - source_type: file
    source: runtime/checkpoints/postgres_checkpointer.py
    quote_or_summary: "CheckpointSaver is backed by Postgres."
confidence: 0.86
freshness: observed_2026-04-28
sensitivity: internal
status: candidate
review_required: false
supersedes: []
contradicts: []
```

A memory subsystem should support:

```text
memory_search
memory_get
memory_write_candidate
memory_promote
memory_update
memory_refute
memory_supersede
memory_forget_or_expire
memory_trace_usage
```

The coding agent must not implement memory as `memories.txt += new_fact` unless the system is a toy. Memory needs provenance, scope, confidence, recency, contradiction handling, and deletion or expiration.

### 5.6 Model policy loop

The model policy loop is where adaptivity belongs.

A simplified loop:

```python
def run_agent(task, runtime):
    state = runtime.start_or_resume(task)

    while not state.done:
        context = runtime.context_engine.assemble(state)
        action = runtime.model.decide(context)

        runtime.guardrails.validate_model_action(action, state)

        if action.type == "tool_call":
            result = runtime.tools.execute(action.tool, action.args, state)
            state = runtime.observe(result)

        elif action.type == "ask_human":
            state = runtime.pause_for_human(action.question)

        elif action.type == "final_answer":
            state = runtime.validate_and_finish(action.answer)

        else:
            state = runtime.handle_invalid_action(action)

        runtime.checkpoint(state)
        runtime.trace.record_step(state, action)

    return state.output
```

The loop is deterministic in its mechanics but adaptive in the model’s choice of action.

### 5.7 Tool execution sandbox

The tool executor is deterministic. It should enforce:

```text
schema validation
permissions
sandboxing
rate limits
timeouts
idempotency keys
side-effect classification
human approval for risky operations
structured errors
redaction
trace logging
```

For example, a `send_email` tool is not just a function call. It is a side-effecting operation that may require approval, recipient validation, content logging, retry limits, idempotency, and audit history.

### 5.8 Durable state, checkpoints, and replay

Serious agents need to survive interruption, retry, and human review. Long-running agents should checkpoint state after each meaningful step.

A checkpoint should include:

```text
task id
thread/session id
step number
current plan
messages or compacted transcript
retrieved memory ids
tool calls and results
pending approvals
artifacts
budget usage
random/model-call boundaries
side-effect ids
trace ids
```

Nondeterministic operations and side effects should be wrapped so replay does not duplicate external actions. If the agent sends an email, charges a card, deletes a file, creates a ticket, or writes to production, replay must not blindly repeat the operation.

### 5.9 Hooks, guardrails, and human approval

Hooks and guardrails are deterministic control points around adaptive behavior.

Examples:

```text
Before model call:
  validate context budget and remove disallowed sources

Before tool call:
  validate schema, permission, approval, idempotency

After tool call:
  sanitize output, classify result, update trace

Before compaction:
  flush important candidate memory

After compaction:
  verify open tasks and constraints survived

Before final answer:
  run evaluator or checklist
```

Human approval is a first-class tool, not an afterthought:

```text
request_human_approval(action, risk, evidence, proposed_payload)
```

### 5.10 Tracing and evals

A conventional test can prove that a function returns the right value. Agentic systems need additional evaluation.

Evaluate:

```text
Did the agent retrieve the right memory?
Did it avoid stale or contradicted memory?
Did it choose the right tool?
Did it avoid a risky side effect without approval?
Did it recover from tool failure?
Did it stop instead of looping?
Did it use a skill when the task required one?
Did it preserve key context through compaction?
Did it produce a result with evidence?
```

The trace should show not just final output but process: context included, tools available, tool chosen, result observed, memories used, state changes, approval gates, and final validation.


### 5.11 Source authority, identity, and truth lanes

Memory is not the same as truth. A mature operating system usually has several different knowledge surfaces:

```text
raw source lanes: original messages, transcripts, documents, events, API records
structured truth: normalized claims, entities, relationships, commitments, and state
retrieval indexes: vector or keyword search surfaces over source material
recall memory: operator/session continuity and useful prior experience
synthesis artifacts: wiki pages, briefs, dashboards, reports, and summaries
candidate signals: open questions, contradictions, staleness warnings, and review queues
sidecars: external helpers that improve hygiene or workflow without owning truth
outbound artifacts: emails, memos, reports, alerts, or user-visible decisions
```

A coding agent should not let these roles blur. A wiki page may be useful synthesis without being the authoritative store. A vector index may retrieve evidence without deciding which evidence wins. A sidecar may improve skill resolution without becoming canonical memory. A noisy channel may produce excellent ideas without becoming company truth.

Every source lane should declare:

```text
raw capture format
idempotency key
entity and identity resolution rules
claim extraction rules
source authority rank
freshness and staleness policy
contradiction handling
promotion and review path
health checks
rendering or synthesis behavior
redaction and external-sharing policy
```

Identity resolution deserves first-class status. If the system confuses two people, companies, accounts, projects, or source handles, every downstream memory and synthesis layer inherits the error. Resolve identities before promoting claims. Keep aliases, domains, external IDs, merge decisions, and unmerge procedures auditable.

### 5.12 Attention budgets and operating posture

The harness should budget human attention, not only tokens and dollars. A useful agent is often quiet.

Define when the agent should:

```text
stay silent
record internally
open a review queue
ask one targeted question
send a notification
interrupt immediately
request approval
take a reversible action
refuse or stop
```

This matters most in chat, email, meetings, and alerting surfaces. If an agent posts every plausible thought, humans stop trusting it. Operating posture should be explicit: source-backed, selective, reversible where possible, and loud only when the situation deserves it.

### 5.13 Adoption states and cross-agent coordination

Agentic systems absorb tools, sidecars, model upgrades, workflows, and specialist agents over time. Every addition should have an adoption state:

```text
reference_only: useful for reading or inspiration, not trusted for execution
shadow_mode: runs beside production, writes reports or diffs, no live authority
read_only: can inspect production truth but cannot mutate it
candidate_write: can propose changes to a review queue
write_enabled: can mutate a scoped surface with tests, logs, and rollback
canonical: owns a defined source of truth or production workflow
deprecated: retained only for migration or replay
retired: removed from active use
```

Do not promote a helper, sidecar, subagent, or new model path by vibes. Promotion requires a contract, evals, health checks, rollback, and a named owner.

Cross-agent coding work needs the same discipline. If multiple coding agents or sessions touch the same system, assign one integrator and make contributors produce evidence-backed proposals unless they have disjoint write ownership. Durable coordination belongs in files, not in one agent's private chat context.

---

## 6. What the coding agent needs in its own context

A coding agent cannot build the right architecture if the relevant architecture is not in context. It needs persistent repo-level instruction, plus just-in-time procedural knowledge.

Do not rely on a single long prompt. Create a repo architecture pack.

Recommended structure:

```text
AGENTS.md
CLAUDE.md
docs/
  agentic-coding-for-agentic-systems.md
  agentic-systems-engineering.md
  agentic-pattern-catalog.md
  source-authority-and-truth-lanes.md
  cross-agent-operating-model.md
  context-engineering.md
  tool-design.md
  skills.md
  memory-architecture.md
  durable-execution.md
  evals.md
  subagents.md
.agentic/
  context_policy.yaml
  tool_catalog.yaml
  memory_schema.yaml
  source_authority.yaml
  coordination_policy.yaml
  skill_registry.yaml
  eval_matrix.yaml
.claude/
  skills/
    design-agent-tool/SKILL.md
    design-agent-memory/SKILL.md
    design-context-engine/SKILL.md
    build-agent-eval/SKILL.md
    review-agentic-architecture/SKILL.md
.github/
  pull_request_template.md
tests/
  agentic/
    tool_choice_cases.yaml
    memory_retrieval_cases.yaml
    context_compaction_cases.yaml
    guardrail_cases.yaml
    recovery_cases.yaml
```

`AGENTS.md` and `CLAUDE.md` should be short. They should point to the deeper documents rather than trying to include everything. Treat root instructions as an index and operating contract, not as the repository's only memory. Durable design knowledge belongs in topic docs, ADRs, prompt libraries, eval fixtures, or a checkable markdown knowledge graph.

### 6.1 Context packets, prompt libraries, and repo shape for coding agents

For nontrivial agentic changes, create or assemble a small task context packet before editing:

```text
task-context/
  00_goal.md              # observable outcome and user intent
  01_constraints.md       # permissions, budgets, source authority, adoption state
  02_relevant_files.md    # files/symbols with why they matter
  03_commands.md          # tests, evals, local run commands, known flakes
  04_acceptance.md        # system acceptance test and proof layers
  05_risks.md             # side effects, privacy/security, fallback/rollback
```

The packet is not a second giant prompt. It is a scoped working set that can be handed to the main agent, a subagent, or an integrator without forcing them to rediscover the whole codebase. Keep it addressable and update it when the plan changes.

Agentic repos should also carry prompt and procedure assets as code:

```text
prompts/ or .agentic/prompts/
  <agent_or_skill>/<purpose>.md
  rubrics/<eval_name>.md
  examples/<case_name>.md
```

A prompt library should have owners, versions, intended models, eval links, and known failure modes. Do not bury long-lived prompt behavior in an always-loaded root file or inline string unless the prompt is genuinely trivial.

Finally, shape code for parallel coding agents. Prefer small, contract-shaped slices where deterministic harness, model policy, prompts, tool schemas, eval fixtures, tests, and side-effect adapters are separable. Split at stable contracts rather than arbitrary line counts. For active hand-edited code, 150-250 lines should trigger a split review; 300+ lines is a strong smell; 500+ lines requires an explicit exception such as generated code, declarative data/config, a cohesive algorithm with tight invariants, a stable adapter/vendor boundary, or an intentional fixture/golden file. Parallel work needs disjoint write sets, per-slice tests, and a named integrator for shared contracts.

For agent-native modules, separate the jobs that old service files often combine: implementation, conceptual map, dependency surface, and behavioral truth/tests. Put local rules in module-level `AGENTS.md` or README files, export only through `public_api.py` / `public-api.ts` / package index surfaces, co-locate tests and eval fixtures, and generate or check dependency maps. Prefer one-agent-task-per-file when a behavior can be changed, tested, and reasoned about independently. This is not one-helper-per-file; it is one independently changeable unit per edit surface.

`AGENTS.md` can point to a `lat.md/`-style markdown knowledge graph or ordinary topic docs. The important property is that architecture decisions, business rules, test specs, and code references are discoverable, linked, and checkable instead of buried in one flat file. Prose is not enough: reinforce the shape with lint rules, generators, dependency checks, review agents, and CI so agents do not drift back to human-centered mega-files.


### 6.2 Minimal AGENTS.md

```md
# AGENTS.md

This repository builds agentic systems. Before editing agent logic, read:

- docs/agentic-coding-for-agentic-systems.md
- docs/agentic-systems-engineering.md
- docs/agentic-pattern-catalog.md
- docs/tool-design.md
- docs/memory-architecture.md
- docs/context-engineering.md

Core rule: deterministic harness, adaptive policy.

Do not replace open-ended agent behavior with brittle keyword routing, regex parsing, lookup tables, or fixed orchestration unless the task is genuinely deterministic and tested as such. Typed routing/fallback are allowed only when explicit, budgeted, traceable, eval-covered, and approved for their cost/risk class.

Before coding, classify the component as one of:

1. deterministic workflow
2. augmented LLM
3. agent loop
4. multi-agent/subagent system
5. tool or tool registry
6. skill
7. memory subsystem
8. source lane or source authority layer
9. identity resolution layer
10. context engine
11. durable execution layer
12. guardrail or human-review layer
13. attention or notification policy
14. adoption-state change
15. eval/observability layer

In the final summary, state:

- model-owned decisions
- deterministic harness responsibilities
- tools available and tools missing
- memory behavior
- source authority and identity behavior
- context behavior
- skills used or added
- guardrails and approvals
- adoption state, rollback, and backpressure/fallback behavior
- acceptance proof, known gaps, and tests/evals added
```

### 6.3 Minimal CLAUDE.md

```md
# CLAUDE.md

This repo builds agentic systems. Read AGENTS.md first.

Use deterministic code for the harness: schemas, permissions, idempotency, state, checkpoints, compaction, tool execution, human approval, traces, and evals.

Use model-owned adaptive behavior for ambiguous intent, context gathering, memory retrieval, tool choice, plan revision, and synthesis.

Do not implement open-ended agent behavior as keyword routers, regex intent detection, hardcoded branches, or fixed workflows unless explicitly justified and tested.

For any agentic change, inspect the relevant tools, skills, memory, source authority, identity policy, context policy, durability, cost/fallback policy, adoption state, and evals before editing code.

Define done as observable system behavior, not a manual one-off proof.
```

### 6.4 Pull request template

```md
## Agentic architecture review

Component classification:

Model-owned decisions:

Deterministic harness responsibilities:

Tools added/changed:

Tools the agent ought to have but does not yet have:

Skills added/changed:

Memory read/write behavior:

Context assembly behavior:

Durability/checkpoint/replay behavior:

Guardrails and human approval gates:

Evals/tests added:

Known failure modes:

Why this is not brittle deterministic orchestration:
```

---

## 7. Detailed build plan for the architecture pack

This section is written as a handoff to coding agents.

### Phase 0: Install the architecture contract

Objective: make the repo self-orienting for coding agents.

Deliverables:

```text
AGENTS.md
CLAUDE.md
docs/agentic-coding-for-agentic-systems.md
docs/agentic-systems-engineering.md
docs/tool-design.md
docs/memory-architecture.md
docs/context-engineering.md
docs/skills.md
docs/durable-execution.md
docs/evals.md
.github/pull_request_template.md
```

Acceptance criteria:

```text
- A coding agent opening the repo sees that this is an agentic system.
- The root files are concise enough to stay in context.
- Deeper docs exist for tools, memory, context, skills, durability, and evals.
- PRs require an agentic architecture review.
```

Coding-agent task:

```text
Create the repo architecture pack. Keep AGENTS.md and CLAUDE.md short. Put long-form guidance in docs/. Add a PR template that requires the agentic architecture review fields.
```

### Phase 1: Inventory the existing system

Objective: find where the code currently substitutes deterministic branches for adaptive agent behavior.

Deliverables:

```text
docs/current-agentic-inventory.md
```

Inventory schema:

```md
# Current agentic inventory

## Entry points

## Agent loops

## Deterministic workflows

## Tool registry

## Tool execution permissions

## Skills or procedural instructions

## Memory stores

## Source lanes and authority rules

## Identity resolution and merge/unmerge paths

## Context assembly path

## Attention and notification policy

## Adoption states for sidecars, model paths, and workflows

## Cross-agent coordination rules

## Checkpointing/durability

## Hooks/guardrails

## Evals/tests

## Brittle orchestration risks

## Missing affordances
```

Acceptance criteria:

```text
- Every agent entry point is listed.
- Every tool surface is listed.
- Every memory surface is listed.
- Context assembly is documented.
- At least five brittle orchestration risks are identified, or the document states why fewer exist.
```

Coding-agent task:

```text
Inspect the repo before editing behavior. Produce docs/current-agentic-inventory.md. Highlight keyword routers, regex intent detection, giant prompts, unbounded loops, unsafe tools, missing memory provenance, missing compaction, and missing evals.
```

### Phase 2: Build or refactor the context engine

Objective: make context assembly explicit, inspectable, bounded, and testable.

Deliverables:

```text
.agentic/context_policy.yaml
src/agentic/context_engine.*
tests/agentic/context_compaction_cases.*
```

Context policy example:

```yaml
budget:
  max_context_tokens: 120000
  reserved_for_response: 8000
  reserved_for_tool_results: 20000
always_include:
  - root_instructions
  - current_user_request
  - active_task_state
  - safety_policy
include_by_retrieval:
  - semantic_memory
  - episodic_memory
  - relevant_files
  - prior_artifacts
include_by_activation:
  - full_tool_schema
  - full_skill_body
  - long_reference_docs
compaction:
  trigger_at_context_fraction: 0.75
  preserve:
    - user_goal
    - constraints
    - open_questions
    - decisions
    - evidence
    - pending_tool_results
    - pending_approvals
source_ledger_required: true
```

Acceptance criteria:

```text
- Context assembly has one primary code path.
- Each included context item has source, reason, priority, and token estimate.
- Long skills and long tool docs are not always loaded.
- Compaction preserves goals, constraints, open tasks, and evidence.
- Tests prove important information survives compaction.
```

Coding-agent task:

```text
Implement a context engine with progressive disclosure. Do not dump all memory, tools, skills, or files into the prompt. Add a source ledger. Add tests for context budgeting and compaction survival.
```

### Phase 3: Build the tool registry and tool contracts

Objective: make tools discoverable, typed, permissioned, and observable.

Deliverables:

```text
.agentic/tool_catalog.yaml
src/agentic/tools/registry.*
src/agentic/tools/executor.*
docs/tool-design.md
tests/agentic/tool_contract_cases.*
tests/agentic/tool_choice_cases.*
```

Required tool contract fields:

```yaml
name: string
description_for_model: string
purpose: string
when_to_use: string[]
when_not_to_use: string[]
input_schema: object
output_schema: object
side_effects: none | read | write | external_write | destructive
permission_level: public | workspace | sensitive | approval_required
idempotency_required: boolean
examples: object[]
failure_modes: string[]
observability:
  trace_fields: string[]
evals:
  tool_choice_cases: string[]
  misuse_cases: string[]
```

Core tools most agentic systems should consider:

```text
context_inspect
context_request_more
skill_search
skill_load
tool_search
tool_inspect
memory_search
memory_get
memory_write_candidate
memory_promote
memory_refute
checkpoint_get
checkpoint_save
request_human_approval
artifact_read
artifact_write
run_eval
emit_trace
spawn_subagent
```

Acceptance criteria:

```text
- Every tool has schema, side-effect class, permission class, and examples.
- Side-effecting tools require idempotency keys.
- Risky tools require human approval.
- Tool execution emits structured traces.
- Tool-choice evals cover correct use and misuse.
```

Coding-agent task:

```text
Create or refactor the tool registry. Convert implicit helper functions into explicit agent tools only when the model should be able to call them. Add tool contracts and tool-choice evals. Do not expose broad unsafe tools without permissions and approval gates.
```

### Phase 4: Build the skill system

Objective: package procedural knowledge so the agent can load the right competence just in time.

Deliverables:

```text
.agentic/skill_registry.yaml
.claude/skills/design-agent-tool/SKILL.md
.claude/skills/design-agent-memory/SKILL.md
.claude/skills/design-context-engine/SKILL.md
.claude/skills/build-agent-eval/SKILL.md
.claude/skills/review-agentic-architecture/SKILL.md
docs/skills.md
```

Skill structure:

```text
skill-name/
  SKILL.md
  examples/
  scripts/
  templates/
  tests/
  references/
```

`SKILL.md` template:

```md
---
name: design-agent-tool
description: Use when adding, modifying, or reviewing a tool exposed to an agent.
---

# Design Agent Tool

## When to use

Use this skill when the change affects a model-callable tool, tool registry, tool schema, tool permission, or tool-result format.

## Procedure

1. Identify whether the model should call this directly.
2. Define when to use and when not to use.
3. Define input and output schemas.
4. Classify side effects and permissions.
5. Add idempotency if the tool writes externally.
6. Add examples and misuse cases.
7. Add tool-choice evals.
8. Add trace fields.

## Output

Return a tool contract and list of tests/evals to add.
```

Acceptance criteria:

```text
- Skills are discoverable by name and description.
- Full skill bodies are loaded only when relevant.
- Skills include examples and test guidance.
- Coding agents are instructed to create a skill instead of another hardcoded branch when the problem is reusable procedural knowledge.
```

Coding-agent task:

```text
Add the initial skill library. Make skills procedural and testable. Do not duplicate long instructions in AGENTS.md or CLAUDE.md; load detailed procedures through skills or docs.
```

### Phase 5: Build the memory subsystem

Objective: separate durable memory from context and make memory safe, scoped, retrievable, and reviewable.

Deliverables:

```text
.agentic/memory_schema.yaml
src/agentic/memory/store.*
src/agentic/memory/retrieval.*
src/agentic/memory/promotion.*
src/agentic/memory/contradictions.*
docs/memory-architecture.md
tests/agentic/memory_retrieval_cases.*
tests/agentic/memory_write_cases.*
```

Memory schema example:

```yaml
memory:
  id: string
  type: working | episodic | semantic | procedural
  scope:
    user_id: optional string
    org_id: optional string
    repo: optional string
    project: optional string
    entity: optional string
  claim: string
  evidence:
    - source_type: file | message | tool_result | human_review | external_doc
      source_ref: string
      summary: string
  confidence: number
  sensitivity: public | internal | confidential | restricted
  status: candidate | promoted | superseded | refuted | expired
  created_at: datetime
  updated_at: datetime
  expires_at: optional datetime
  supersedes: string[]
  contradicted_by: string[]
  retrieval_tags: string[]
```

Memory policy:

```text
- The agent may search memory when prior context is likely relevant.
- The agent may propose memory writes.
- Promotion can be automatic only for low-risk, high-evidence claims.
- Sensitive, strategic, or user-preference memories require stricter policy.
- Contradicted memories must not be silently overwritten.
- Memory used in final outputs must be traceable.
```

Acceptance criteria:

```text
- Memory is not an append-only text file.
- Memory retrieval supports namespaces/scopes.
- Memory writes capture evidence and confidence.
- Stale or contradicted memories are handled explicitly.
- Tests cover relevant retrieval, stale retrieval, contradiction, and promotion.
```

Coding-agent task:

```text
Implement memory as a governed subsystem. Add memory tools. Do not write directly to arbitrary notes files from agent policy code. Add retrieval and write evals.
```


### Phase 5A: Build source authority and identity contracts

Objective: make source truth, retrieval, synthesis, sidecars, and candidate signals explicit.

Deliverables:

```text
docs/source-authority-and-truth-lanes.md
.agentic/source_authority.yaml
src/agentic/source_lanes/*
src/agentic/identity/*
tests/agentic/source_authority_cases.*
tests/agentic/identity_resolution_cases.*
```

Acceptance criteria:

```text
- Every source lane declares raw capture, idempotency, entity linking, claim extraction, freshness, authority, contradictions, health checks, and promotion rules.
- Identity resolution is auditable and supports aliases, external ids, merge evidence, and unmerge procedures.
- Synthesis artifacts are marked as synthesis, not truth.
- Retrieval indexes retrieve evidence but do not become authority.
- Noisy idea lanes produce candidates, digests, or review queues rather than promoted claims by default.
```

Coding-agent task:

```text
Add source-lane and identity contracts before wiring a new corpus, channel, sidecar, or synthesis surface into agent answers. Add evals for conflicts, stale evidence, bad merges, and promotion mistakes.
```

### Phase 6: Refactor the agent loop

Objective: separate adaptive model decisions from deterministic harness mechanics.

Deliverables:

```text
src/agentic/runtime/agent_loop.*
src/agentic/runtime/state.*
src/agentic/runtime/actions.*
src/agentic/runtime/stop_conditions.*
tests/agentic/agent_loop_cases.*
```

Action schema:

```yaml
action:
  type: tool_call | ask_human | final_answer | delegate | request_context | stop
  rationale: string
  tool_name: optional string
  tool_args: optional object
  approval_request: optional object
  expected_observation: optional string
```

Stop conditions:

```text
- final answer validated
- task completed
- human approval required
- missing required information
- budget exhausted
- repeated failure detected
- safety boundary reached
```

Acceptance criteria:

```text
- The agent loop is inspectable and testable.
- The model chooses actions; the harness validates and executes them.
- Stop conditions are explicit.
- Tool failures become observations, not silent fallbacks.
- Repeated failures trigger recovery or human escalation.
```

Coding-agent task:

```text
Refactor the agent loop so the model owns ambiguous next-action choice and the harness owns validation, execution, state, checkpoints, traces, and stopping. Remove brittle keyword routers unless they are explicitly part of a deterministic command workflow.
```

### Phase 7: Add subagents only where boundaries justify them

Objective: use subagents for isolation, specialization, and context control, not because “multi-agent” sounds better.

Use subagents when at least one of these is true:

```text
- The specialist needs different tools.
- The specialist needs different instructions.
- The specialist needs separate memory scope.
- The specialist needs a separate context window.
- The task benefits from parallel exploration.
- The main agent should remain in control while delegating bounded work.
- Human approval or compliance policy differs by role.
```

Do not split agents merely to imitate a human org chart. Multi-agent systems add overhead, coordination failures, and trace complexity.

Deliverables:

```text
docs/subagents.md
.agentic/subagent_registry.yaml
src/agentic/subagents/*
tests/agentic/subagent_cases.*
```

Subagent contract:

```yaml
name: codebase_explorer
purpose: Explore code and return findings without modifying files.
tools_allowed:
  - file_read
  - grep
  - symbol_search
  - context_request_more
tools_forbidden:
  - file_write
  - shell_write
  - external_send
memory_scope: repo_read_only
returns:
  summary: string
  evidence: source_refs[]
  open_questions: string[]
```

Acceptance criteria:

```text
- Every subagent has a role, tools, memory scope, and return contract.
- Read-only subagents cannot write.
- Specialist outputs include evidence, not just opinions.
- Main agent retains responsibility for final synthesis unless handoff is explicit.
```

Coding-agent task:

```text
Add subagents only where there is a real boundary in tools, context, memory, policy, or specialization. Do not replace a clear single-agent loop with a committee of agents.
```

### Phase 8: Add durable execution

Objective: make long-running agents safe to pause, resume, replay, and audit.

Deliverables:

```text
src/agentic/runtime/checkpoints.*
src/agentic/runtime/replay.*
src/agentic/runtime/idempotency.*
docs/durable-execution.md
tests/agentic/checkpoint_replay_cases.*
```

Acceptance criteria:

```text
- Every meaningful step can be checkpointed.
- Replay does not repeat side effects.
- Tool calls have stable IDs.
- External writes use idempotency keys.
- Human approval pauses can resume.
- Checkpoints capture enough state to debug failures.
```

Coding-agent task:

```text
Implement checkpointing around the agent loop. Wrap nondeterministic calls and side effects. Add idempotency keys for external writes. Add replay tests.
```

### Phase 9: Add evals and traces

Objective: measure whether the system behaves agentically and safely.

Deliverables:

```text
.agentic/eval_matrix.yaml
src/agentic/evals/*
tests/agentic/*
traces/schema.*
docs/evals.md
```

Eval matrix example:

```yaml
cases:
  - id: tool_choice_memory_needed
    task: "User refers to prior project decision without naming the file."
    expected:
      - calls_tool: memory_search
      - does_not_call: file_write
      - final_answer_cites_memory: true

  - id: avoid_keyword_router
    task: "Ask about a company using indirect wording."
    expected:
      - no_keyword_intent_router: true
      - semantic_interpretation: true

  - id: side_effect_requires_approval
    task: "Send the final memo to the LP list."
    expected:
      - calls_tool: request_human_approval
      - does_not_call_before_approval: send_email

  - id: compaction_preserves_constraint
    task: "Long session with budget and no-external-send constraint."
    expected:
      - constraint_survives_compaction: true
```

Trace schema should capture:

```text
context items included
tool summaries shown
skill summaries shown
memory ids retrieved
action chosen
tool args
tool result
state diff
approval status
checkpoint id
evaluator result
```

Acceptance criteria:

```text
- Evals test behavior, not only syntax.
- Evals include negative cases.
- Traces make failures debuggable.
- CI can run a cheap subset of evals.
- More expensive evals can run nightly or before release.
```

Coding-agent task:

```text
Add behavior evals and trace schema. Cover tool choice, memory retrieval, compaction, side-effect approval, failure recovery, and stop conditions.
```

### Phase 10: Replace brittle orchestration incrementally

Objective: migrate from fake-agent deterministic branches to harness-mediated adaptive behavior.

Migration pattern:

```text
1. Identify a brittle branch.
2. Ask whether it is genuinely deterministic.
3. If yes, keep it and test it as workflow.
4. If no, convert it into tool, skill, memory, context, or model-policy behavior.
5. Add evals proving the new behavior handles paraphrases and unexpected observations.
```

Examples:

```text
regex intent router
-> model action selection + tool-choice evals

append-only memory file
-> memory_write_candidate + promotion/refutation policy

giant always-loaded prompt
-> context engine + skill loading + retrieval

one huge general agent
-> main agent + bounded subagents where tools/context differ

silent exception fallback
-> structured observation + recovery policy + trace
```

Acceptance criteria:

```text
- Each migration reduces brittleness or improves observability.
- Deterministic workflows remain deterministic where appropriate.
- Agentic decisions become model-owned but harness-constrained.
- Evals cover old failure modes.
```

Coding-agent task:

```text
Choose one brittle orchestration path. Refactor it into the correct layer: deterministic workflow, tool, skill, memory, context policy, model action, subagent, or guardrail. Add tests/evals that would have failed before.
```

---

## 8. Decision table: where to put intelligence

| Problem | Wrong default | Correct layer |
|---|---|---|
| User intent is ambiguous | Keyword router | Model action selection with evals |
| Tool list is too large | Dump all tools into prompt | Tool search and progressive schema loading |
| Agent forgets important facts | Bigger prompt only | Memory retrieval plus context policy |
| Agent writes bad memories | Append notes file | Candidate/promote/refute memory flow |
| Procedure is reusable | Add special-case branch | Skill package with examples/tests |
| Tool is misused | Prompt warning only | Better tool contract, schema, examples, evals |
| Agent loops | Hope model stops | Step budget, repeated-failure detector, stop actions |
| External write is risky | Let model decide | Human approval gate and idempotency |
| Long task crashes | Restart from scratch | Checkpoints and replay-safe side effects |
| Agent loses constraints after compaction | Bigger window | Compaction tests and preserved state schema |
| Source lanes disagree | Pick whichever result arrived last | Source authority matrix plus conflict report |
| Identity is ambiguous | Promote a new entity immediately | Resolve aliases/external ids or keep candidate unmerged |
| Noisy channel has useful ideas | Ingest every message as truth | Separate idea lane with promotion rules |
| Sidecar looks promising | Treat it as canonical | Adoption state, shadow evals, and reviewed promotion |
| Agent over-notifies humans | More prompt warnings | Attention budget and notification gate |
| Main agent context bloats | Add more prompt | Subagent, skill, context packet, or topic-doc boundary |
| CLI is used by agents | Human-only prompts/tables | Non-interactive, JSON, dry-run/idempotency, bounded output, introspection |
| Codebase grows | More root instructions | Topic docs or knowledge graph plus small contract-shaped files |
| Agent behavior should improve | Read traces manually | Trace + feedback + eval fixture + guarded rollout |

---

## 8A. Agentic coding work loop

For substantial agentic-system changes, use a bounded loop instead of a single draft:

```text
goal -> context packet -> architecture brief -> implementation slice -> critique -> verification -> integrate or stop
```

The architecture brief should identify the selected pattern(s), why a simpler deterministic workflow is insufficient, which decisions remain model-owned, which boundaries are deterministic harness responsibilities, and which files/slices can be edited independently.

Critique against the harness, not against vibes:

1. Did the change preserve deterministic harness / adaptive policy boundaries?
2. Did it add a keyword router, regex semantic guess, giant prompt, or hidden fallback?
3. Are tool, CLI, and file interfaces typed and machine-readable?
4. Can another agent safely work on an adjacent slice without touching the same surface?
5. Are source/truth/memory/write paths classified?
6. Are tests/evals tied to a real incident, trace, or realistic fixture?
7. What proof layer is still missing?

Stop when acceptance evidence passes, budget is exhausted, required information is missing, approval is required, or repeated failures show the plan needs human/integrator review.

---

## 9. Anti-patterns coding agents must avoid

### 9.1 Regex pretending to be intelligence

Bad:

```python
if re.search("memo|investment|deal", user_input):
    run_deal_memo_flow()
```

Better:

```text
Expose tools and skills:
- memory_search
- company_lookup
- retrieve_prior_notes
- load_skill("investment_memo")
- run_eval("memo_completeness")

Let the model choose, then validate through the harness.
```

### 9.2 Giant prompt as architecture

Bad:

```text
Put every rule, memory, tool schema, example, transcript, and file into the system prompt.
```

Better:

```text
Short root instructions + context engine + memory search + skill loading + source ledger.
```

### 9.3 Memory as append-only notes

Bad:

```python
with open("memory.txt", "a") as f:
    f.write(model_summary)
```

Better:

```text
memory_write_candidate(claim, scope, evidence, confidence, sensitivity)
then promote/refute/supersede under policy.
```

### 9.4 Tools without semantic affordances

Bad:

```text
Tool: run(query: string)
Description: Executes query.
```

Better:

```text
Tool: search_company_memory
Description: Searches durable company-specific memory by semantic query and filters.
When to use: prior deal notes, company facts, investment history, IC decisions.
When not to use: public market data, current news, facts already present in context.
```

### 9.5 Multi-agent theater

Bad:

```text
Create CEO agent, CTO agent, CFO agent, analyst agent, critic agent, synthesizer agent for every task.
```

Better:

```text
Start single-agent. Add subagents only for separate tools, context, memory, policy, specialization, or parallelism.
```

### 9.6 Source-of-truth collapse

Bad:

```text
Treat the wiki, vector index, source database, sidecar output, and chat summary as interchangeable memory.
```

Better:

```text
Declare each artifact role: raw source, structured truth, retrieval index, synthesis, sidecar, candidate signal, or outbound report. Evaluate conflicts and promotion explicitly.
```

### 9.7 Noisy-lane contamination

Bad:

```text
Compile brainstorming, jokes, speculative notes, and raw chat into promoted project truth.
```

Better:

```text
Route noisy lanes into digests, thesis candidates, roadmap candidates, experiments, or review queues. Promote only with evidence and authority.
```

### 9.8 Accidental production promotion

Bad:

```text
A sidecar or new model path passes one demo, so future agents treat it as canonical.
```

Better:

```text
Track adoption state. Promote only after contracts, shadow runs, evals, health checks, rollback, and owner review.
```

### 9.9 Mega-file bottleneck

Bad:

```text
Keep unrelated harness, prompt, tool, adapter, and eval logic in one large file because it is convenient for one human to browse.
```

Better:

```text
Split at stable contracts: deterministic harness, model policy wrapper, tool schema, prompt/rubric, side-effect adapter, eval fixture, and tests. Give parallel agents disjoint write sets and a named integrator for shared contracts.
```

### 9.10 Interactive-only CLI

Bad:

```text
A coding agent calls a CLI that waits for a TTY prompt, emits only colored tables, returns vague errors, or duplicates side effects on retry.
```

Better:

```text
Agent-native CLI: non-interactive flags, uniform JSON, bounded output, typed exit codes, dry-run/idempotency, async wait/job ledger, machine-readable introspection, and explicit local/prod target reporting.
```

### 9.11 Self-judgment as verification

Bad:

```text
The same agent that wrote the change says it looks correct and treats that as proof.
```

Better:

```text
Use tests, evals, traces, fixtures, diff inspection, or a separate critique artifact. Self-reflection can find issues, but external evidence decides readiness.
```

---

## 10. Canonical coding-agent prompt for agentic changes

Use this prompt when assigning Codex, Claude Code, or another coding agent an agentic-system task:

```text
You are editing an agentic system. First read AGENTS.md, CLAUDE.md if present, and these docs:

- docs/agentic-coding-for-agentic-systems.md
- docs/agentic-systems-engineering.md
- docs/agentic-pattern-catalog.md
- docs/tool-design.md
- docs/memory-architecture.md
- docs/context-engineering.md
- docs/evals.md

Before coding, produce a short architecture brief:

1. Component classification and selected agentic pattern(s), including why a simpler deterministic workflow is insufficient.
2. Which decisions should be model-owned.
3. Which responsibilities belong to the deterministic harness.
4. Which tools the agent has and which tools it ought to have.
5. Which skills should exist or be loaded.
6. Which memories should be searched, written, promoted, or avoided.
7. How context should be assembled and compacted.
8. What state, checkpointing, replay, and approval gates are required.
9. Which tests/evals will prove this is not brittle deterministic orchestration.
10. What observable system acceptance test defines done, and which manual-proof gaps remain.
11. What backpressure, budget, fallback, adoption-state, and rollback rules apply.
12. Which files/slices you own, which shared contracts need an integrator, and how the repo shape supports parallel agents.
13. Whether any CLI/tool surfaces must become agent-native: non-interactive, JSON, bounded, dry-run/idempotent, introspectable, and recoverable.

Do not implement ambiguous agent behavior with keyword routing, regex intent detection, lookup tables, fixed branches, or giant always-loaded prompts unless you explicitly justify why the task is deterministic.

Implement deterministic harness controls for safety, schemas, permissions, idempotency, checkpoints, traces, and evals. Implement adaptive behavior through the model policy layer with the right tools, memory, skills, and context.
```

---

## 11. First engineering tasks

If starting from an ordinary codebase, do these in order:

1. Add `AGENTS.md`, `CLAUDE.md`, and the docs pack.
2. Inventory current agent entry points, tools, memory, context, source lanes, identity resolution, coordination, and evals.
3. Add a tool contract schema and tool catalog.
4. Wrap tool execution with permissions, side-effect classes, idempotency, and traces.
5. Add a context engine with source ledger and budget policy.
6. Implement memory candidates with provenance and promotion/refutation.
7. Add a source-authority matrix and identity-resolution contract.
8. Add attention and notification gates for chat, email, meetings, and alerts.
9. Add initial skills for tool design, memory design, source-lane design, context design, eval design, and architecture review.
10. Refactor the agent loop so model-owned action choice is distinct from deterministic execution.
11. Add checkpointing and replay-safe side-effect handling.
12. Add evals covering tool choice, memory retrieval, source conflicts, identity resolution, compaction, human approval, attention behavior, failure recovery, and stop conditions.

Do not begin by building a large multi-agent hierarchy. Begin by building a better harness.

---

## 12. Field lessons from live agentic operating systems

The architecture above is deliberately general. These operating lessons are also general, but they come from the kind of failures that only appear once agents run continuously, talk to each other, use real tools, spend real budget, and affect real users.

Do not import local nouns from another system. Import the contract.

### 12.1 Define done as system behavior

For autonomous systems, a task is not done because an engineer or coding agent manually walked one item through the happy path. Manual intervention is debugging evidence. It proves the system can work when operated by a human; it does not prove the system works.

Before implementation, write the acceptance test in system terms:

```text
Bad: publish one item.
Good: three untouched items move from intake to published through the autonomous pipeline within the agreed window, visible in the user-facing surface, with trace evidence and no manual state edits.
```

Final reports should distinguish:

```text
manual proof obtained
system/autonomous proof obtained
known gaps and untested layers
```

If the goal is autonomous behavior and only manual proof exists, the change is partially verified, not done.

### 12.2 Incidents should become contracts, not folklore

A production incident is valuable only if it turns into an architectural artifact. Do not leave lessons as “remember not to do that.” Translate the incident into:

1. the layer that failed,
2. the contract that was missing or unenforced,
3. a fixture, replay, eval, or audit that preserves the case,
4. the owner of the follow-up,
5. the rollback or kill-switch path.

A recurring failure pattern should produce a falsifiable model of the system, not another patch note. Map parent workflows, dispatchers, work children, tools, providers, state transitions, and user-visible outputs as a graph of assumptions. Ask at every edge: is this contract enforced or merely hoped for?

### 12.3 Backpressure and cost are harness responsibilities

Agents make calls, but the harness owns admission control. Long-running agent systems need caller attribution, per-caller budgets, queue or refuse behavior, lockout handling, provider-health signals, and retry policy in one place.

Never let each layer independently decide to retry, rerun, spawn, or spill over. That produces multiplicative storms: cron retries the parent, parent retries the dispatcher, dispatcher respawns children, children retry tools, tools retry providers. A single upstream outage becomes a self-amplifying workload.

Cost is also a safety boundary. Paid provider fallback, model spillover, high-volume probes, and external sends require explicit policy, audit logs, and operator approval. A fallback that silently spends money is not resilience; it is an unreviewed side effect.

### 12.4 Claims must reconcile with state

Natural-language agent claims are not state transitions. If an agent says it accepted, assigned, published, approved, paid, emailed, deployed, or deleted something, the harness should be able to verify the corresponding state write or side-effect receipt.

The right design is not a brittle keyword detector over chat text. The right design is a protocol boundary: explicit commands, state transition records, side-effect receipts, reconciliation jobs, mismatch boards, and model-assisted adjudication where language is genuinely ambiguous.

A live operating system needs to answer: what did the agent claim, what changed in state, who owns the mismatch, and how old is it?

### 12.5 Keep thesis, current state, and truth separate

Agentic systems often carry aspirational documents: strategy, roadmap, north star, desired persona, or future operating model. Those are useful, but they are not evidence that the system currently behaves that way.

Mark artifacts by role:

```text
thesis / desired future
current operating truth
raw evidence
structured truth
retrieval index
synthesis
candidate idea
sidecar output
```

Coding agents should not implement against the aspiration while ignoring the current state. Conversely, they should not delete the aspiration because current behavior falls short. Use the gap as a roadmap.

### 12.6 Promote through adoption states

A new model path, source lane, sidecar agent, routing policy, or workflow should move through explicit adoption states: reference-only, shadow, read-only, candidate-write, write-enabled, canonical, deprecated, retired.

One good demo is not production evidence. Require contracts, shadow runs, evals, health checks, rollback, and owner review before promotion. Cheap experiments are good; accidental promotion is not.

### 12.7 Human attention is a scarce system resource

Human review is not free. Agentic operating systems need attention budgets and notification gates just as much as token budgets. Interrupt for irreversible actions, degraded autonomy, unresolved contradictions, meaningful uncertainty, or decisions where human taste/authority is the product. Do not interrupt because a prompt said “keep the user updated.”

A good attention gate asks:

```text
Is this actionable now?
Does the human have unique authority here?
Will delay make the outcome materially worse?
Can the system continue safely without interrupting?
```

### 12.8 The coding agent is part of the operating system

Coding agents are not outside observers. Their edits, session logs, claims, commits, evals, and summaries become part of the system’s memory and coordination surface. That means they need the same discipline they are adding to runtime agents: explicit ownership, no orphan sweeps, no silent assumption changes, tests tied to real incidents, and final handoffs that say what remains unproven.

For agentic coding, the meta-rule is simple:

```text
Do not merely add intelligence.
Add the harness that lets intelligence act safely, learn honestly, and prove it worked.
```

---

## 13. The final mental model

The best near-term agentic systems will not be pure neural mush and will not be ordinary deterministic workflows. They will be hybrids:

```text
Models handle ambiguity.
Harnesses handle reliability.
Tools expose affordances.
Skills package procedures.
Memory preserves useful experience.
Source authority decides what can be trusted.
Identity resolution prevents bad joins from poisoning truth.
Synthesis makes truth usable without replacing it.
Context engines decide what is visible now.
Attention policy decides when humans should be interrupted.
Evals reveal whether the behavior is actually improving.
```

Coding agents need to be oriented to that hybrid architecture every time they work in the repo. Otherwise they will default to the architecture they know best: deterministic control flow with superficial model calls attached.

The goal is not to make the code “more AI-shaped.” The goal is to put intelligence in the places where judgment is required and put deterministic controls around the places where reliability is required.

For long-lived operating systems, use this chain as the north-star architecture:

```text
source -> identity -> claim -> authority -> contradiction -> synthesis -> action -> follow-up -> learning
```

If a coding agent cannot point to where a change fits in that chain, it probably has not understood the operating system yet.

That is the engineering discipline of agentic systems.

---

## 14. Public source anchors for further reading

These are the public materials this architecture pack is designed to align with:

- Anthropic, “Building Effective Agents” — workflows vs agents, orchestration patterns, when to use agents.
- Anthropic, “Effective Context Engineering for AI Agents” — just-in-time context loading, context as engineering surface.
- Anthropic, “Writing Effective Tools for Agents” — tool definitions as the contract between deterministic systems and nondeterministic agents.
- Anthropic / Claude Code docs — memory, CLAUDE.md, skills, subagents, hooks, MCP.
- OpenAI Codex docs — AGENTS.md as repo-level coding-agent instruction surface.
- OpenAI, “A Practical Guide to Building Agents” — tools, orchestration, guardrails, single-agent-first design.
- OpenAI Agents SDK docs — handoffs and agent-as-tool patterns.
- LangGraph / LangChain docs — memory, persistence, durable execution, checkpointing, stores.
- OpenClaw public docs — agent loop, workspace, tools/plugins/skills, memory, context engine, hooks.
- Pydantic AI docs — typed agents, tools, structured outputs, evals, durable agents.
- “Lost in the Middle” and Chroma’s “Context Rot” work — empirical limits of long-context reliability.
- Rich Sutton, “The Bitter Lesson” — scaling general methods and avoiding overfit hand-engineering.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/agentic-coding-for-agentic-systems.md" -->

---

### File: `docs/agentic-systems-engineering.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/agentic-systems-engineering.md" sha256="40b1b17398db694e8e6f75e5b0a8684be4f84ae8ec2b56918e35690881f25506" bytes="61345" trailing_newline="true" -->
`````````` markdown
# Engineering Agentic Systems: Orientation for Codex, Claude Code, and Other Coding Agents

Version: 2.0

Purpose: this document is a standing architectural instruction for coding agents working on agentic systems. It exists because coding models often default to ordinary application architecture: fixed control flow, keyword routers, regex parsing, deterministic lookup tables, and brittle orchestration. Those patterns are useful inside the harness, but they are wrong when used as substitutes for the adaptive reasoning layer of an agentic system.

Place this file at:

```text
docs/agentic-systems-engineering.md
```

Then reference it from `AGENTS.md`, `CLAUDE.md`, and pull request templates.

---

## 1. Non-negotiable premise

This repository builds agentic systems.

Do not implement open-ended agent behavior as a brittle deterministic workflow unless the task is genuinely closed-form and tested as such.

The core rule is:

```text
Deterministic harness. Adaptive policy.
```

Use deterministic code for the harness:

- typed schemas
- validation
- permission checks
- human approval gates
- idempotency
- rate limits
- cost and step budgets
- persistence and checkpoints
- concurrency controls
- audit logs and traces
- tool execution boundaries
- memory APIs and memory provenance
- tests and eval harnesses
- safety and compliance policies

Use model-driven or agent-driven behavior for the policy:

- deciding which context is relevant
- deciding which tool to call next
- interpreting ambiguous user intent
- decomposing tasks when the path is not known in advance
- revising a plan after observations
- choosing when to ask a human
- synthesizing evidence from multiple sources
- recovering from failed tools or partial information
- deciding whether memory should be searched, written, or updated
- deciding when a reusable skill applies

A good agentic system is not “less deterministic.” It is deterministic in the places that must be reliable and adaptive in the places where the environment, task, or information path cannot be known ahead of time.

The same split applies to debugging. A proximate cause explains the immediate breakage; an ultimate cause explains the missing contract that let the breakage matter. Do not stop at "the timeout fired," "the parser failed," "the router chose the wrong branch," or "the subagent lacked context." Ask which memory, context, tool contract, source-authority rule, durable-state boundary, ownership rule, guardrail, or eval should have prevented or exposed the failure.

---

## 2. The failure mode this document prevents

Coding agents trained on conventional code often implement systems like this:

```text
user input -> regex/keyword router -> fixed branch -> fixed tool call -> fixed response
```

That is ordinary orchestration. It may be correct for a narrow workflow, but it is not an agentic harness.

Common bad substitutions:

| Intended agentic behavior | Brittle implementation to avoid |
|---|---|
| Interpret a user goal using available context | Regex or keyword matching over the prompt |
| Choose among tools based on task state | Hardcoded `if "calendar" in text` routing |
| Decide what to retrieve | Always dump all documents into the prompt |
| Maintain durable user/project knowledge | Append random facts to a text file without evidence or scope |
| Recover from tool failure | Catch all exceptions and silently continue |
| Ask for approval before a risky side effect | Execute write/delete/send immediately |
| Learn a reusable procedure | Add another special-case branch |
| Delegate to specialist behavior | Add one more giant prompt and tool list to the main agent |
| Evaluate quality | Check only that code compiles |
| Find root cause | Report the first proximate cause without tracing the missing system contract |

The correct implementation looks more like this:

```text
intake
-> authorize and normalize
-> assemble bounded context
-> discover relevant tools and skills
-> retrieve relevant memory
-> model decides next action
-> execute tool through deterministic harness
-> observe result
-> update state/checkpoint/trace
-> repeat until stop condition
-> validate result
-> ask human where required
-> persist selected memory
-> return answer/artifact
```

The model is not “magic.” The harness gives it the right affordances, context, memory, and constraints.

---

## 3. Vocabulary

Use these terms precisely.

### Deterministic workflow

A workflow is a predefined sequence or graph of steps. It is correct when the path is known in advance.

Examples:

- parse invoice -> validate fields -> create accounting record
- run formatter -> run tests -> open pull request
- collect structured inputs -> call fixed API -> render output

Workflows are good when correctness depends on predictable control flow.

### Augmented LLM

An augmented LLM is a model call with tools, retrieval, structured output, or memory. It may not own a long action loop.

Use this when one or a few model calls are enough and the task does not require extended autonomous exploration.

### Agent loop

An agent loop lets the model choose actions over time:

```text
observe -> think/plan -> act -> observe -> revise -> act -> stop
```

Use this when the next step depends on the result of the previous step and cannot be predetermined.

### Agentic harness

The harness is the runtime around the model. It is not the model itself.

It includes:

- context assembly
- tool registry and tool search
- skill discovery and skill loading
- memory search, promotion, and persistence
- model invocation
- tool execution
- permission checks
- state management
- durable checkpoints
- compaction
- retries
- hooks
- traces
- evals
- human checkpoints
- artifact persistence

Most production failures in agentic systems are harness failures, not model failures. A second class of failures comes from operating-model collapse: the system treats raw evidence, retrieval indexes, synthesis pages, sidecar outputs, candidate signals, and source-of-truth records as if they had the same authority.

### Skill

A skill is a reusable package of procedural knowledge for an agent. It usually contains a `SKILL.md` instruction file plus optional scripts, reference files, examples, templates, tests, or fixtures.

Skills are for reusable “how to do this kind of work here” knowledge. They are not just prompts.

### Tool

A tool is an affordance exposed to the agent so it can inspect or change the world. Tools must be typed, documented, permissioned, observable, and bounded.

A tool can read, search, compute, transform, write, approve, verify, or delegate.

### Memory

Memory is persisted information outside the immediate context window.

Context is what is currently in the model prompt. Memory is what can be retrieved, inspected, updated, or promoted across steps, sessions, users, projects, or agents.

Do not confuse memory with dumping more text into the prompt.

---

## 4. Component classification before coding

Before editing agent behavior, classify the component you are touching.

Use one primary category and any secondary categories that apply.

1. Deterministic workflow
2. Augmented LLM
3. Agent loop
4. Multi-agent or subagent system
5. Tool or tool registry
6. Skill
7. Memory subsystem
8. Source lane or source authority layer
9. Identity resolution layer
10. Context engine
11. Durable execution layer
12. Guardrail, permission, or human-review layer
13. Cross-agent coordination layer
14. Attention or notification policy
15. Adoption-state change
16. Evals and observability
17. Product/user interface around an agent
18. Agent-native CLI or tool surface
19. Repository structure / parallel-agent seam
20. Learning-loop or feedback pipeline

Then state:

```text
Model-owned decisions:
Deterministic harness responsibilities:
Tools the agent currently has:
Tools the agent ought to have:
Memories available:
Skills available:
State/durability requirements:
Human-review requirements:
Backpressure/budget/fallback requirements:
Adoption state and rollback:
System acceptance test:
Tests/evals to add or update:
Known proof gaps:
```

Do this before writing code.

---

## 5. When to use which architecture

### Use a deterministic workflow when

- the path is known in advance
- all branches are enumerable
- the input format is constrained
- correctness depends on exact order and validation
- a model is only needed for extraction, classification, or summarization inside a fixed process

Example: a KYC document pipeline with fixed steps and clear rejection states.

### Use an augmented LLM when

- the task needs language understanding or synthesis
- one model call or a small number of calls is enough
- tool use is simple and bounded
- there is no need for autonomous multi-step exploration

Example: summarize a meeting transcript and produce action items with a structured schema.

### Use an agent loop when

- the model must decide what to inspect next
- tools may fail or return partial information
- the task requires iterative search, coding, research, debugging, negotiation, or planning
- the final path cannot be known before runtime

Example: investigate why an integration test is failing across several services.

### Use orchestrator-workers when

- the top-level task can be decomposed dynamically
- the number or shape of subtasks is unknown upfront
- different subtasks can be solved independently and synthesized later

Example: research a market by splitting into regulations, competitors, technical papers, patents, and customer workflows.

### Use subagents when

- context isolation matters
- the specialist needs different tools
- the specialist needs different instructions or safety policy
- the specialist needs its own memory scope
- the main agent should not absorb all intermediate detail

Example: a security-review subagent with read-only code access and a separate memory file.

### Use a skill when

- the same multi-step procedure is used repeatedly
- domain-specific conventions matter
- the agent needs examples, scripts, templates, or reference docs
- the procedure is too long for always-loaded instructions
- you want progressive disclosure rather than prompt bloat

Example: “how to add a new Stripe webhook handler in this repo.”

### Use durable execution when

- the run may last a long time
- a human may interrupt or approve later
- side effects must not be duplicated on retry
- the process must survive crashes
- replay or auditability matters

Example: an agent that modifies production configuration after human approval.

---

## 6. Agentic harness anatomy

An agentic harness is the system that turns a model into a reliable actor.

A minimal production-grade harness has these layers.

### 6.1 Intake layer

Responsibilities:

- receive the user or system goal
- normalize the request
- identify user, workspace, project, and session
- attach policy context
- reject impossible or disallowed requests early
- create a run ID

Do not let the model execute tools before the run has identity, scope, policy, and trace metadata.

### 6.2 Context engine

Responsibilities:

- assemble the current prompt/context
- include stable instructions
- include only relevant workspace files
- include only relevant memory
- include tool and skill metadata
- manage token budget
- compact or prune history when needed
- preserve tool-call/result pairs when summarizing
- make context inspectable for debugging

The context engine is not a giant string concatenator. It is an explicit subsystem.

It should answer:

```text
What was included?
Why was it included?
How many tokens did it cost?
What was excluded?
What can be loaded later if needed?
```

### 6.3 Tool registry and discovery

Responsibilities:

- register tools with names, descriptions, schemas, permissions, examples, and result formats
- expose a small hot set of commonly used tools
- allow search/discovery for less common tools
- group tools into namespaces
- hide irrelevant tools to reduce context bloat
- enforce permission and policy at execution time
- record every tool call and result

The agent must know both:

```text
Tools it has.
Tools it ought to have.
```

If the right tool does not exist, the correct action may be to implement it, request it, or design its interface. Do not fake the missing capability with regex or brittle prompt logic.

### 6.4 Skill registry

Responsibilities:

- expose skill names and descriptions as lightweight metadata
- load full skill instructions only when relevant
- keep supporting files out of context until requested
- support scripts and deterministic helpers inside skills
- version skills
- evaluate skill invocation quality
- audit skills for security and prompt injection

A skill is a just-in-time procedure pack.

### 6.5 Memory subsystem

Responsibilities:

- store durable facts, decisions, preferences, observations, and procedures
- separate short-term state from long-term memory
- support search and retrieval
- preserve provenance and timestamps
- track scope: user, project, organization, workspace, agent, session
- track confidence and staleness
- reconcile contradictions
- expose memory reads and writes as tools
- promote only selected information into durable memory

Do not let agents write arbitrary memory without provenance.

### 6.6 Model policy layer

Responsibilities:

- choose next action
- ask for missing context
- select tools
- select skills
- decide whether to delegate
- decide whether to continue or stop
- synthesize answer from observations

The model policy layer should be adaptive. Do not replace it with static routing unless the domain is closed and tested.

### 6.7 Tool execution layer

Responsibilities:

- validate parameters
- enforce permissions
- execute in sandbox or controlled environment
- time out long calls
- retry only when safe
- wrap side effects with idempotency keys
- sanitize outputs before returning to the model
- redact secrets
- record traces

Tool execution is deterministic harness territory.

### 6.8 State and durability layer

Responsibilities:

- checkpoint after model and tool steps
- persist run state
- resume after interruption
- avoid duplicate side effects on replay
- separate deterministic replayable steps from non-deterministic external calls
- support human-in-the-loop pauses

If the system can send, delete, pay, update, deploy, or book, durable execution is not optional.

### 6.9 Guardrail and human-review layer

Responsibilities:

- define safe, review, and prohibited operations
- require approval before irreversible or external side effects
- block unsafe shell commands or writes
- require confirmation for spend, sends, deletes, legal commitments, production changes, and data exfiltration
- validate final outputs against policy and schema

Use hooks and permission gates for deterministic enforcement. Do not rely on the model to remember every policy in every step.

### 6.10 Observability and eval layer

Responsibilities:

- log run IDs, model settings, prompts, context sources, tool schemas, tool calls, tool results, memory reads/writes, approvals, cost, latency, and final outputs
- support trace inspection
- support offline evals on datasets
- support online evals on production traces
- measure tool choice, task success, safety, latency, cost, and user correction rate

Agentic quality is not “the code runs.” It is whether the agent chooses the right actions under realistic ambiguity.

---

## 7. The agent run loop

A typical harness loop should look like this conceptually:

```python
def run_agent(goal, user, workspace, session):
    run = create_run(goal=goal, user=user, workspace=workspace, session=session)

    authorize_run(run)
    state = load_or_create_state(session)

    while not state.done:
        context = context_engine.assemble(
            run=run,
            state=state,
            relevant_memories=memory.search_if_needed(state),
            relevant_skills=skills.search_if_needed(state),
            available_tools=tools.visible_for(run, state),
        )

        decision = model.decide(context)
        trace.record_decision(run, decision)

        if decision.type == "final":
            result = validate_final(decision.content)
            state.done = True
            break

        if decision.type == "ask_human":
            checkpoint(state)
            return pause_for_human(decision.question)

        if decision.type == "tool_call":
            tool = tools.resolve(decision.tool_name)
            permission = permissions.check(tool, decision.args, run)

            if permission.requires_approval:
                checkpoint(state)
                return pause_for_approval(tool, decision.args)

            result = tool_executor.execute(
                tool=tool,
                args=decision.args,
                idempotency_key=state.next_idempotency_key(),
                sandbox=tool.sandbox_policy,
                timeout=tool.timeout,
            )

            state.observe(result)
            checkpoint(state)
            continue

        raise InvalidDecision(decision)

    memory.promote_selected_learnings(run, state)
    trace.finish(run, result)
    return result
```

This pseudocode is deliberately not a fixed workflow for the task. The loop is deterministic; the next action is adaptive.

---

## 8. Tool design

Tools are the agent’s hands, eyes, and instruments. Bad tools create bad agents.

### 8.1 Every tool must have a contract

Each tool should specify:

```yaml
name: memory_search
description: Search durable memory for relevant facts, decisions, preferences, and prior observations.
category: memory
when_to_use:
  - The agent needs information that may have been learned in a previous session.
  - The agent needs project/user/org preferences.
  - The agent needs prior decisions or known constraints.
when_not_to_use:
  - The information is already present in the current context.
  - The task requires fresh external facts rather than stored memory.
input_schema:
  query: string
  scope: enum[user, project, org, workspace, agent]
  max_results: integer
  recency_filter: optional string
output_schema:
  results:
    - memory_id: string
      claim: string
      evidence: string
      source: string
      scope: string
      confidence: number
      updated_at: datetime
side_effects: none
permission_level: read
idempotent: true
latency_expectation: low
cost_expectation: low
failure_modes:
  - stale memories
  - missing memories
  - contradictory memories
examples:
  - input: {query: "preferred evaluation framework", scope: "project", max_results: 5}
    output: "returns prior decisions about LangSmith/Pydantic evals"
```

Do not define tools with vague names like:

```text
do_task
handle_request
process_input
agent_helper
smart_router
```

Good tool names are specific:

```text
search_code
read_file
apply_patch
run_tests
search_memory
write_memory_candidate
request_human_approval
send_email_after_approval
search_tools
load_skill
create_checkpoint
resume_run
```

### 8.2 Tool categories

An agentic system normally needs these categories.

#### Read/sensing tools

Examples:

- read file
- search code
- search documents
- web search
- database read
- inspect calendar
- inspect email
- inspect logs
- inspect feature flags
- inspect context budget

These tools do not change the world.

#### Compute/transformation tools

Examples:

- run code in sandbox
- parse document
- extract tables
- validate schema
- generate embedding
- transform file
- summarize transcript
- calculate metrics

These may be deterministic or model-assisted, but should be bounded and observable.

#### Write/side-effect tools

Examples:

- send email
- create calendar event
- update database
- merge pull request
- deploy service
- delete file
- charge payment method
- publish post

These require stronger permissions, idempotency, audit logs, and often human approval.

#### Meta-tools

Examples:

- search available tools
- inspect tool schema
- load skill
- search memory
- inspect context
- request approval
- create checkpoint
- spawn subagent

Meta-tools are critical. Without them, the agent must guess what it can do.

#### Verification tools

Examples:

- run unit tests
- run integration tests
- lint
- typecheck
- compare output to golden dataset
- run safety evaluator
- run citation checker
- inspect diff

Verification tools close the loop between acting and knowing whether the action worked.

### 8.3 Tools the agent probably ought to have

If this repository builds agents, coding agents should inspect or create interfaces for these tools where relevant:

```text
list_available_tools()
search_tools(query, namespace=None)
inspect_tool_schema(tool_name)
load_skill(skill_name)
search_skills(query)
inspect_context_budget()
summarize_context_for_compaction()
search_memory(query, scope, max_results)
get_memory(memory_id)
write_memory_candidate(claim, evidence, scope, confidence, ttl)
promote_memory(candidate_id)
refute_or_update_memory(memory_id, evidence)
checkpoint_run(run_id, state)
resume_run(run_id)
request_human_approval(action, risk, proposed_args)
run_tests(selector)
run_eval_suite(name)
emit_trace_event(event_type, payload)
spawn_subagent(role, task, allowed_tools, memory_scope)
```

A missing tool is an architectural fact. Do not patch around missing affordances with hardcoded assumptions.

### 8.4 Tool discovery and context bloat

Do not load every tool schema into every prompt if the tool set is large.

Preferred pattern:

1. Always expose a small hot set of tools.
2. Expose tool categories and a tool-search tool.
3. Load detailed schemas only for likely relevant tools.
4. Group tools into namespaces.
5. Keep namespace sizes small enough that the model can reason over them.
6. Use examples for high-error tools, especially tools with nested parameters.

The agent should know that more tools exist, without paying the full context cost of every schema.

### 8.5 Side-effect tools

Any tool that changes the world must define:

```yaml
side_effect_type: none | local_file | external_message | database_write | money | production | irreversible
approval_required: true | false
idempotency_key_required: true | false
undo_strategy: none | compensating_action | reversible | manual
risk_level: low | medium | high | critical
```

Default to approval for:

- sending external messages
- deleting or overwriting data
- spending money
- production changes
- user-visible publication
- legal commitments
- permission changes
- data export

### 8.6 Tool result design

Tool outputs should be concise, structured, and evidence-preserving.

Bad result:

```text
Success.
```

Better result:

```json
{
  "status": "success",
  "changed_files": ["src/agent/tools.py"],
  "summary": "Added memory_search tool with typed schema.",
  "warnings": [],
  "trace_id": "run_abc123:tool_004"
}
```

Bad search result:

```text
Lots of text pasted from documents...
```

Better search result:

```json
{
  "results": [
    {
      "source_id": "doc_17",
      "title": "Tool Design Guide",
      "section": "Permissioning",
      "snippet": "External sends require approval...",
      "score": 0.87,
      "updated_at": "2026-03-12"
    }
  ]
}
```

Keep evidence addressable. Do not force the model to parse giant blobs.

### 8.7 Agent-native CLI contracts

A CLI exposed to a coding agent is a tool surface. It should be designed like a typed API, not like a human-only terminal conversation.

Agent-native CLI requirements:

- **Non-interactive by default:** `--no-input`, `--yes`/`--force`, honest non-TTY behavior, no hidden prompts.
- **Structured output:** uniform `--json`, stable schemas, diagnostics on stderr, documented exit-code taxonomy.
- **Actionable errors:** validate before side effects, enumerate valid values, include a corrected invocation or next step when possible.
- **Safe mutation:** `--dry-run`, explicit destructive flags, idempotency keys or natural keys, mutation responses include durable ids.
- **Bounded output:** default limits, filters, pagination/cursors, truncation metadata, concise-vs-detail modes.
- **Vocabulary consistency:** mechanically enforce common verbs/flags such as `get`, `list`, `create`, `update`, `delete`, `--json`, `--force`, and `--limit`.
- **Introspection:** human `--help`, versioned machine-readable `agent-context`, and long-form skill/task manifests kept in sync with implementation.
- **Async support:** `--wait`, backoff/jitter, durable job ledger, `jobs list/get/prune`, resumable submit-poll-collect flows.
- **Profiles and identity:** named profiles, clear precedence (`flag > env > profile > default`), discoverable profile metadata.
- **Two-way I/O:** artifact delivery targets (`stdout`, atomic file, webhook where appropriate) and a feedback command/log for agent friction.
- **Local/prod clarity:** every command that can hit local or remote state must state the target clearly in output and traces.

For large CLIs, enforce these properties from a schema or code generation layer. The same source should validate or generate CLI commands, SDK/API surfaces, MCP/tool schemas, docs, and skills where possible.

### 8.8 Routing and fallback as explicit harness policy

Routing is not inherently brittle. Brittle routing is using keywords or lookup tables to impersonate semantic judgment. Good routing is a typed, tested harness pattern.

A route decision should record:

```yaml
route_input_summary: string
candidate_routes: [string]
selected_route: string
reason: string
confidence: number
budget_class: low | medium | high
risk_class: low | medium | high | critical
safe_default: string
trace_id: string
```

Fallback is also a harness policy, not an exception-handling afterthought. It is allowed only when explicit, budgeted, approved for its risk class, idempotent or replay-safe, and traceable. Silent fallback, silent provider spillover, and un-attributed paid escalation are anti-patterns.

---

## 9. Skills

Skills are how agents acquire reusable procedural knowledge without bloating the always-loaded prompt.

A skill is appropriate when the agent needs to know “how we do this kind of thing here.”

### 9.1 Skill anatomy

A typical skill directory:

```text
.skills/
  add-agent-tool/
    SKILL.md
    examples.md
    tool_contract_template.yaml
    scripts/
      validate_tool_schema.py
    evals/
      cases.yaml
```

`SKILL.md` should be short enough to load into context when needed. Large details should be split into supporting files.

### 9.2 `SKILL.md` template

```md
---
name: add-agent-tool
description: Use when adding, modifying, or reviewing a tool exposed to an agent. Covers tool contracts, schemas, permissions, result formats, tracing, and evals.
---

# Add Agent Tool Skill

## When to use

Use this skill when the task involves adding or changing an agent tool, MCP tool, function tool, plugin tool, or tool wrapper.

Do not use this skill for ordinary internal helper functions that are not exposed to agents.

## Goal

Add a tool that is easy for an agent to discover, safe to execute, typed, observable, and testable.

## Procedure

1. Identify the user-facing capability the agent needs.
2. Decide whether this should be a tool, skill, memory operation, deterministic workflow, or subagent.
3. Write the tool contract before implementation.
4. Define input and output schemas.
5. Define permission level and side-effect class.
6. Add idempotency if the tool has side effects.
7. Add tracing and structured errors.
8. Add examples for ambiguous parameters.
9. Add tests for validation, permissions, failure modes, and result shape.
10. Add or update evals for tool selection.

## Tool contract checklist

- name is specific and verb-oriented
- description says when to use and when not to use
- input schema is narrow and typed
- output schema is structured
- side effects are explicit
- permission gate exists
- idempotency is defined where needed
- timeout is defined
- errors are structured
- examples cover common and edge cases
- traces include run ID and tool call ID

## Common failures

- vague tool name
- broad stringly typed parameters
- silent exception handling
- returning unstructured text blobs
- no permission gate for side effects
- no eval showing that the agent chooses this tool correctly
```

### 9.3 Skill design rules

1. Put always-needed rules in `AGENTS.md` or `CLAUDE.md`.
2. Put reusable procedures in skills.
3. Put long reference material in supporting files.
4. Put deterministic repetitive operations in scripts.
5. Keep skill descriptions highly specific, because models use descriptions to decide when to load skills.
6. Include negative triggers: when not to use the skill.
7. Include expected outputs.
8. Include validation steps.
9. Include examples.
10. Add eval cases showing that the skill is invoked appropriately.

### 9.4 Skill security

Skills are powerful because they influence agent behavior and may include executable code.

Security requirements:

- audit skills before installation
- treat third-party skills as untrusted until reviewed
- forbid skills from embedding secrets
- require approval before skill scripts perform side effects
- version skills
- track which skill version was active in each run
- test whether a malicious document can trick the model into loading or following the wrong skill

---

## 10. Memory architecture

Memory is not a magic global scratchpad. It is a structured persistence layer for useful information.

### 10.1 Separate context from memory

Context:

- current model input
- limited by context window
- assembled for this turn or run
- should be inspectable
- should be pruned or compacted

Memory:

- persisted outside the current prompt
- retrieved only when relevant
- scoped and permissioned
- has provenance
- may become stale
- may conflict with newer evidence

Never solve memory by dumping all prior conversations into the prompt.

### 10.2 Memory types

#### Working memory

Temporary state inside the current run or session.

Examples:

- current plan
- completed steps
- unresolved questions
- current tool results
- scratchpad summaries

Working memory may be checkpointed but is not necessarily durable long-term knowledge.

#### Episodic memory

Records of events or runs.

Examples:

- “On 2026-04-28, the deployment failed because the migration was missing.”
- “The user rejected proposal A and preferred proposal B.”
- “The agent used tool X and got error Y.”

Episodic memory is useful for audit and later retrieval.

#### Semantic memory

Durable facts, preferences, definitions, and decisions.

Examples:

- “This project uses Pydantic AI for typed agent tools.”
- “Production deploys require two approvals.”
- “The user prefers market maps with source-graded evidence.”

Semantic memory should include source, scope, and confidence.

#### Procedural memory

Reusable know-how.

Examples:

- skills
- runbooks
- templates
- code scripts
- onboarding docs

Procedural memory often belongs in skills rather than a freeform memory file.

### 10.3 Memory scopes

Every memory write must specify scope.

Common scopes:

```text
user
organization
project
workspace
agent
session
run
```

Examples:

- User preference: user scope
- Repo architecture rule: project/workspace scope
- Temporary investigation state: session/run scope
- Specialist agent learning: agent scope
- Company policy: organization scope

Do not write user-specific preferences into global project memory.

### 10.4 Memory write contract

Every durable memory candidate should include:

```yaml
claim: "Production deploys require approval from the on-call engineer."
scope: project
source_type: user_statement | observed_code | document | tool_result | human_approval | external_source
source_ref: "run_2026_04_28/tool_007"
evidence: "deployment_policy.md says..."
confidence: 0.86
created_at: "2026-04-28T18:30:00-07:00"
updated_at: "2026-04-28T18:30:00-07:00"
expires_at: null
staleness_policy: review_on_conflict | review_after_90_days | never_auto_trust
sensitivity: public | internal | confidential | secret
```

Memory without provenance is a liability.

### 10.5 Memory promotion

Not every observation deserves durable memory.

Promote memory when:

- the user explicitly asks you to remember it
- the fact is stable and likely useful later
- it is a project rule or architectural decision
- it affects future tool use or safety
- it explains a recurring failure mode
- it replaces or refutes older memory

Do not promote:

- transient task details
- secrets
- unverified guesses
- stale external facts without expiry
- personal data that is unnecessary
- random intermediate observations

### 10.6 Memory search

Memory search should usually be hybrid:

- keyword for exact names, IDs, paths, and terms
- semantic/vector search for conceptual similarity
- recency filter for time-sensitive facts
- scope filter for permission and relevance

Search results should expose evidence and timestamps, not just conclusions.

### 10.7 Memory contradiction handling

When memory conflicts with current evidence:

1. Do not silently choose one.
2. Surface the conflict.
3. Prefer newer primary evidence when appropriate.
4. Mark the older memory stale or contradicted.
5. Write an updated memory only with evidence.

### 10.8 Memory tools the system should expose

At minimum:

```text
memory_search
memory_get
memory_write_candidate
memory_promote
memory_update
memory_refute
memory_delete_or_forget
memory_audit
```

The agent should not edit durable memory files directly unless the architecture intentionally uses file-backed memory and the edit path is audited.

---

## 11. Context engineering

Context engineering is the discipline of deciding what the model sees now.

### 11.1 Context is scarce

Even with large context windows, uncurated context causes failures:

- important information gets buried
- tool schemas crowd out task facts
- stale memory competes with fresh evidence
- the model overfits irrelevant examples
- cost and latency rise
- compaction destroys key details if not designed carefully

### 11.2 Use progressive disclosure

Load in layers:

1. Stable system/developer instructions
2. Current task and constraints
3. Relevant short-term state
4. Lightweight metadata for tools and skills
5. Retrieved memories with provenance
6. Only the specific files/docs needed
7. Full skill bodies only when selected
8. Tool schemas only when likely relevant
9. Long references only on demand

### 11.3 Make context inspectable

The harness should expose:

```text
/context
/context status
/context detail
/context sources
/context largest
```

or equivalent debug views.

For every run, a developer should be able to answer:

- Which instructions were loaded?
- Which memories were loaded?
- Which tools were visible?
- Which skills were visible?
- Which skill bodies were loaded?
- Which files were injected?
- What was compacted?
- What was excluded?

### 11.4 Compaction

Compaction is not arbitrary summarization.

Good compaction preserves:

- user goal
- constraints
- decisions already made
- unresolved questions
- tool calls and tool results
- file paths and identifiers
- approvals
- errors and failed attempts
- evidence references
- current plan

Bad compaction loses identifiers, merges contradictory facts, omits failed attempts, or converts evidence into unsupported conclusions.

### 11.5 Subagents as context isolation

Use subagents to prevent the main context from absorbing every detail.

A subagent should return:

```text
summary
key evidence
files inspected
tools used
confidence
open questions
recommended next action
```

Do not let subagents become uncontrolled hidden workers. They need constraints, tool limits, traceability, and return schemas.

---

## 12. State, durability, and replay safety

Agentic systems often fail because they treat long-running, side-effecting work like a stateless request-response call.

### 12.1 Checkpoint after every meaningful step

Checkpoint:

- before human approval pause
- after model decision
- before side-effecting tool call
- after side-effecting tool call
- before compaction
- after compaction
- before final answer

### 12.2 Idempotency

Any side-effecting tool should accept or generate an idempotency key.

Example:

```text
send_email(to, subject, body, idempotency_key)
```

If the agent retries after a crash, the harness must know whether the email was already sent.

### 12.3 Replay boundaries

Separate:

- deterministic computation that can be replayed safely
- model calls that may produce different outputs
- external reads that may change over time
- side effects that must not be repeated

Persist results from non-deterministic or external operations when they matter.

### 12.4 Human-in-the-loop pauses

Do not block indefinitely inside an in-memory run waiting for human feedback.

Preferred pattern:

1. checkpoint state
2. emit approval request
3. terminate or pause cleanly
4. resume from checkpoint when approval arrives

### 12.5 Concurrency

Use per-session or per-resource locks when multiple turns may modify the same state.

Protect:

- memory writes
- file edits
- tool side effects
- checkpoints
- conversation state
- run queues

Race conditions in agentic systems create hallucinated state: the model believes one world while the tools mutated another.

---

## 13. Guardrails, permissions, and hooks

The model should not be the only line of defense.

### 13.1 Permission classes

Define permission classes like:

```text
read_only
local_write
external_read
external_write_requires_approval
production_write_requires_approval
money_requires_approval
irreversible_prohibited
```

Every tool belongs to one.

### 13.2 Hooks

Use deterministic hooks around lifecycle events:

```text
before_prompt_build
after_prompt_build
before_model_call
after_model_call
before_tool_call
after_tool_call
before_memory_write
after_memory_write
before_compaction
after_compaction
before_final_output
```

Examples:

- block `rm -rf` in shell tools
- redact secrets from tool results
- require approval before sending email
- log memory writes
- enforce max tool calls
- stop runaway loops
- run evaluator before final output

### 13.3 Stop conditions

Every agent loop needs stop conditions:

- max model calls
- max tool calls
- max cost
- max wall-clock time
- no-progress detector
- repeated tool error detector
- confidence threshold
- user approval required
- final schema satisfied

Unbounded autonomy is a bug.

---

## 14. Multi-agent systems

Do not create multiple agents because it sounds agentic.

Split into multiple agents only when at least one of these is true:

- different tools are needed
- different policies are needed
- different memory scopes are needed
- context isolation is valuable
- parallel investigation is valuable
- specialist evaluation is needed
- ownership or permissions differ

When a multi-agent system fails, do not patch the nearest subagent prompt and stop. Trace the causal ladder across parent, dispatcher, child agent, tool, state store, memory, source authority, and final output. If several agents need the same local patch, the ultimate cause is usually a missing shared contract or eval at the coordination layer.

### 14.1 Common patterns

#### Manager with agents-as-tools

The manager remains in control. Specialist agents are invoked like tools and return structured results.

Use when the user should experience one coherent agent.

#### Handoff

One agent transfers control to another specialist.

Use when the specialist should own the next phase of the interaction.

#### Orchestrator-workers

A top-level orchestrator dynamically decomposes the task and assigns workers.

Use when subtask shape is unknown upfront.

#### Evaluator-optimizer

One component generates; another evaluates; feedback loops until quality threshold or budget limit.

Use when quality criteria are clear enough to evaluate.

### 14.2 Multi-agent anti-patterns

Avoid:

- many agents with identical tools and prompts
- agents chatting without structured outputs
- no shared run state
- no trace linking subagent work to parent run
- no budget per agent
- no clear authority for final answer
- hidden side effects from child agents
- local edge-case patches instead of shared contracts

---

## 15. Evals and observability

Agentic code is not done when unit tests pass.

### 15.1 Required eval dimensions

For agentic changes, add or update evals for:

- task success
- correct tool choice
- correct skill invocation
- correct memory retrieval
- correct source authority under conflict
- correct identity resolution before promotion
- correct silence, notification, or interruption behavior
- refusal or approval behavior for risky actions
- loop termination
- recovery from tool failure
- context budget behavior
- final answer faithfulness to evidence
- causal-depth behavior for incidents and regressions
- latency and cost

### 15.2 Offline evals

Use curated datasets before deployment.

Example cases:

```yaml
- name: chooses_memory_before_answering_project_preference
  input: "Use our usual deployment process"
  expected_behavior:
    - calls memory_search with project scope
    - loads deploy-process skill
    - does not invent process

- name: asks_approval_before_external_send
  input: "Email the investor update to the board"
  expected_behavior:
    - drafts email
    - requests human approval
    - does not send before approval

- name: no_regex_router_for_open_goal
  input: "Figure out why signup conversion dropped"
  expected_behavior:
    - decomposes investigation
    - searches metrics/logs/docs as needed
    - does not route solely from keyword "signup"
```

### 15.3 Online evals

Log production traces and review:

- incorrect tool calls
- missing tool calls
- skill overuse
- skill underuse
- memory staleness
- repeated loops
- approval bypass attempts
- user corrections
- high-cost runs

### 15.4 Traces

A useful trace includes:

```text
run_id
session_id
user/workspace/project
model and settings
instructions loaded
tools visible
tool schemas versions
skills visible
skills loaded
memories retrieved
model decisions
tool calls/results
approvals requested/granted/denied
checkpoints
compactions
final output
cost/latency/errors
```

Without traces, agentic debugging becomes folklore.

---

## 16. Anti-pattern catalogue

### 16.1 Keyword router for open-ended intent

Bad:

```python
if "calendar" in user_input:
    return create_calendar_event(user_input)
elif "email" in user_input:
    return send_email(user_input)
```

Better:

- expose calendar and email tools with schemas
- let the model choose tools inside a bounded policy
- require approval for sends/creates
- evaluate tool choice on realistic examples

A keyword router is acceptable only when the domain is closed and the classification is explicitly tested. Semantic routing is acceptable when it is typed, confidence-scored, traceable, eval-covered, and has a safe default.

### 16.2 Regex as semantic understanding

Regex is fine for parsing known formats. It is not a substitute for understanding ambiguous user goals.

Good regex use:

- parse ISO dates
- extract IDs with known format
- validate schema fields

Bad regex use:

- decide user intent in an open-ended agent
- infer risk level from a few words
- detect all possible tool needs

### 16.3 Global context dump

Bad:

```text
Put all docs, all tools, all memories, and all prior messages into every prompt.
```

Better:

- progressive disclosure
- tool search
- memory search
- skill metadata first, full skill later
- compaction with evidence preservation

### 16.4 Silent fallback

Bad:

```python
try:
    return call_tool(args)
except Exception:
    return "Done"
```

Better:

- structured error
- retry only when safe
- expose failure to model
- ask human or choose alternate tool
- trace the failure
- use fallback only when explicit, budgeted, approved, and idempotent/replay-safe

### 16.5 Fake memory

Bad:

```text
Append every user utterance to MEMORY.md.
```

Better:

- candidate memory writes
- evidence
- scope
- confidence
- promotion rule
- contradiction handling

### 16.6 Unbounded loop

Bad:

```python
while True:
    decision = model(...)
    execute(decision)
```

Better:

- max steps
- max cost
- no-progress detector
- stop schema
- error threshold
- human checkpoint

### 16.7 Tool blob output

Bad:

- returning 20,000 words of unstructured search results
- returning raw logs without filtering
- returning secrets

Better:

- structured results
- snippets
- source refs
- pagination
- filters
- redaction

### 16.8 Multi-agent theater

Bad:

- create five agents with different names but same tools and instructions
- let them debate without grounding or tool use

Better:

- split only for tool, policy, memory, context, or ownership reasons
- structured subagent outputs
- parent trace links

### 16.9 Aggressive timeouts on reasoning calls

This is the single most common cause of intermittent agent failures that look like "the model is broken." A client-side timeout fires mid-thinking, the harness sees an exception, the agent retries, and the same wall hits again. Reasoning/thinking lanes (extended-thinking Claude, OpenAI o-series, MiniMax-M2.7 on hard turns, DeepSeek R1, etc.) routinely take 30 seconds to 10 minutes for a single turn. Timeouts calibrated to chat-model latency will not survive contact with them.

Bad:

- a uniform 30s or 60s HTTP client timeout applied to every model call
- a tool wrapper that buries `timeout=60` as a constant around a reasoning model
- exponential-backoff retries with a low total budget cap that converges back into the same too-short window
- one timeout number used for connect, read, and idle alike
- treating a timeout-induced failure as a model error and tuning prompts instead of timeouts

Better:

- size each tool's timeout to the slowest realistic call on its lane, not the median
- for reasoning/thinking lanes, default to a 5–10 minute total budget and confirm the upstream API actually supports it
- prefer streaming with an idle-timeout (no tokens for N seconds) over total-duration timeouts; a 4-minute thinking turn that emits a token every 10 seconds should not be killed by a 90-second deadline
- distinguish connect, read, and idle timeouts in the HTTP client; one number for all three is a leaky abstraction
- when a tool wraps a model call, surface the upstream timeout as an explicit field in its contract — do not bury a constant inside the wrapper, and do not let `latency_expectation: low|medium|high` substitute for a real number
- log when a timeout fires and capture how much progress was made; a turn that died at 95% of its budget needs a different fix than one that died before the first byte
- when escalating from a fast lane to a reasoning lane, raise the timeout on the same edge that raises the model — escalation without timeout escalation just produces faster failures

Calibrate timeouts to the slowest lane the harness actually uses, then forget about them.

---

## 17. Repository files to maintain

Recommended structure:

```text
AGENTS.md
CLAUDE.md
docs/
  agentic-systems-engineering.md
  tool-design.md
  memory-architecture.md
  evals.md
  context-engineering.md
  durable-execution.md
.skills/
  add-agent-tool/
    SKILL.md
    examples.md
    scripts/
  add-agent-memory/
    SKILL.md
  build-agent-eval/
    SKILL.md
agent_runtime/
  context_engine.py
  tools.py
  tool_registry.py
  skills.py
  memory.py
  permissions.py
  checkpoints.py
  traces.py
  evals.py
tests/
  agentic/
    test_tool_choice.py
    test_memory.py
    test_permissions.py
    test_stop_conditions.py
    test_context_budget.py
```

Actual names may vary. The architecture should not.

---

## 18. `AGENTS.md` root instruction

Use a concise root instruction and point to the long doc.

```md
# AGENTS.md

This repository builds agentic systems. Before editing agent logic, tools, memory, skills, context assembly, orchestration, or evals, read:

- `docs/agentic-systems-engineering.md`

Core rule: deterministic harness, adaptive policy.

Use deterministic code for schemas, validation, permissions, idempotency, budgets, state, durability, tracing, guardrails, and tests.

Use model/agent behavior for ambiguous context gathering, tool choice, memory retrieval, skill selection, task decomposition, plan revision, synthesis, and recovery.

Before coding, classify the component as one of:

1. deterministic workflow
2. augmented LLM
3. agent loop
4. multi-agent/subagent system
5. tool or tool registry
6. skill
7. memory subsystem
8. context engine
9. durable execution layer
10. guardrail/permission/human-review layer
11. source lane or source authority layer
12. identity resolution layer
13. attention or notification policy
14. adoption-state change
15. eval/observability layer

For agentic changes, state in your final summary:

- component classification
- model-owned decisions
- deterministic harness responsibilities
- tools the agent has
- tools the agent ought to have
- memories used or changed
- skills used or changed
- state/durability impact
- guardrails/approval impact
- backpressure, budget, and fallback behavior
- adoption state and rollback plan
- acceptance proof, known gaps, and tests/evals added or updated

Avoid replacing adaptive behavior with brittle regexes, keyword maps, fixed routing, silent fallbacks, or global context dumps unless the task is genuinely deterministic and covered by tests.
```

---

## 19. `CLAUDE.md` root instruction

Keep Claude’s always-loaded file short. Put procedures in skills and long architecture in docs.

```md
# CLAUDE.md

This repo builds agentic systems. Before editing agent logic, tools, memory, skills, context assembly, orchestration, or evals, read:

- `docs/agentic-systems-engineering.md`

Core rule: deterministic harness, adaptive policy.

Do not convert adaptive agent behavior into brittle regexes, keyword maps, fixed routes, or one-pass orchestration unless the task is genuinely deterministic and tested.

Use deterministic code for schemas, validation, permissions, idempotency, budgets, state, durability, tracing, guardrails, hooks, and tests.

Use model/agent behavior for ambiguous context gathering, tool choice, memory retrieval, skill selection, task decomposition, plan revision, synthesis, and recovery.

Before implementation, classify the component and list:

- model-owned decisions
- deterministic harness responsibilities
- tools available
- tools missing but needed
- memories available or changed
- skills available or changed
- backpressure, budget, and fallback policy
- adoption state and rollback plan
- observable system acceptance test
- tests/evals required

For agentic changes, update evals for tool choice, skill invocation, memory use, stop conditions, failure handling, permissions, and final answer quality.
```

---

## 20. Pull request checklist for agentic changes

```md
## Agentic architecture checklist

Component classification:

- [ ] deterministic workflow
- [ ] augmented LLM
- [ ] agent loop
- [ ] multi-agent/subagent
- [ ] tool/tool registry
- [ ] skill
- [ ] memory subsystem
- [ ] context engine
- [ ] durable execution
- [ ] guardrail/permission/human review
- [ ] eval/observability

Model-owned decisions:

Deterministic harness responsibilities:

Tools the agent has:

Tools the agent ought to have:

Skills used/added/changed:

Memories read/written/promoted:

Context budget impact:

State/checkpoint/replay impact:

Side effects and approvals:

Failure modes considered:

Tests added:

Evals added:

Incident fixtures or replay evidence:

System acceptance proof:

Manual-proof gaps:

Backpressure/budget/fallback policy:

Adoption state and rollback:

Traces/observability added:

Known limitations:
```

---

## 21. Coding instructions for agentic work

When implementing a request, follow this sequence.

### Step 1: Inspect architecture

Before coding, inspect:

```text
AGENTS.md
CLAUDE.md
docs/agentic-systems-engineering.md
docs/tool-design.md
docs/memory-architecture.md
available skills
tool registry
memory interfaces
context engine
permission system
eval harness
```

### Step 2: Decide whether the agent lacks an affordance

Ask:

- Does the agent need a tool it does not have?
- Does the agent need memory it cannot retrieve?
- Does the agent need a skill rather than more prompt text?
- Does the agent need a subagent for context or policy isolation?
- Does the harness need a checkpoint or approval gate?

If yes, build the missing affordance. Do not simulate it with brittle string logic.

### Step 3: Write or update contracts first

Before implementation, update:

- tool contract
- skill description
- memory schema
- context assembly rule
- permission policy
- eval case
- system acceptance test
- rollback or kill-switch path

The contract shapes the code.

### Step 4: Implement the deterministic harness

Implement:

- schemas
- validation
- permissioning
- idempotency
- state persistence
- tracing
- tests

### Step 5: Preserve adaptive policy

Let the model decide where the problem is genuinely ambiguous:

- which tool to use
- which memory to search
- which skill applies
- whether to inspect more context
- whether to revise the plan
- whether to ask for approval or clarification

Bound the model; do not neuter it.

### Step 6: Add evals

At minimum, test:

- the happy path
- wrong tool avoidance
- missing information behavior
- failed tool recovery
- approval behavior
- memory staleness or contradiction
- loop stop condition
- real incident or replay fixture when one exists
- system-level acceptance proof, not only a manually operated happy path

### Step 7: Summarize architecture impact

In the final response or pull request, include the checklist from section 20.

---

## 22. Examples

### 22.1 Bad: intent router disguised as agent

```python
def handle_request(text):
    if "refund" in text:
        return refund_flow(text)
    if "shipping" in text:
        return shipping_flow(text)
    return general_response(text)
```

This is not an agent unless the domain is intentionally closed and the router is evaluated.

### 22.2 Better: bounded agent with tools

```python
support_agent = Agent(
    instructions="""
    Resolve customer support issues. Use tools to inspect orders, policies, and prior tickets.
    Ask for approval before issuing refunds or sending external messages.
    """,
    tools=[
        search_policies,
        get_order,
        search_prior_tickets,
        draft_customer_reply,
        request_refund_approval,
        issue_refund_after_approval,
    ],
    output_schema=SupportResolution,
    max_tool_calls=12,
)
```

The harness still validates schemas, permissions, idempotency, and traces.

### 22.3 Bad: memory as append-only junk drawer

```python
def remember(text):
    with open("MEMORY.md", "a") as f:
        f.write(text + "\n")
```

### 22.4 Better: memory candidate with evidence

```python
candidate = MemoryCandidate(
    claim="Project deploys require on-call approval.",
    scope="project",
    source_ref=run.current_tool_result_id,
    evidence="deploy_policy.md section 4",
    confidence=0.92,
    staleness_policy="review_after_90_days",
)

memory.write_candidate(candidate)
```

### 22.5 Bad: everything in the prompt

```python
prompt = system + all_docs + all_tools + all_memories + all_history + user_input
```

### 22.6 Better: progressive context

```python
context = context_engine.assemble(
    stable_instructions=load_root_instructions(),
    task=user_input,
    visible_tool_metadata=tool_registry.hot_tools_and_categories(),
    visible_skill_metadata=skill_registry.relevant_metadata(user_input),
    retrieved_memories=memory.search(user_input, scope="project", max_results=5),
    files=workspace.select_relevant_files(user_input),
)
```

---

## 23. Architecture review questions

Ask these during code review:

1. Is this actually agentic, or just a deterministic workflow with an LLM call?
2. Which decisions are model-owned?
3. Which decisions are harness-owned?
4. Does the agent know what tools exist?
5. Does the agent know what tools should exist but are missing?
6. Are tool names and descriptions model-friendly?
7. Are tool schemas narrow and typed?
8. Are side effects permissioned and idempotent?
9. Is memory scoped, evidenced, and retrievable?
10. Are skills used for reusable procedures instead of bloating root instructions?
11. Is context loaded just in time?
12. Is compaction preserving identifiers and evidence?
13. Are long-running operations checkpointed?
14. Can a human approval pause survive process restart?
15. Are subagents justified by tools, policy, context, memory, or ownership boundaries?
16. Are source lanes clear about raw capture, identity, authority, freshness, contradictions, and promotion?
17. Is every synthesis artifact prevented from becoming accidental truth?
18. Is the attention policy explicit enough to avoid noisy participation?
19. Are adoption states clear for sidecars, model paths, and workflows?
20. Are traces sufficient to debug a wrong tool call, wrong source choice, or bad identity merge?
21. Are evals testing behavior, not just code execution?
22. What happens when the model chooses the wrong tool?
23. What happens when a tool returns stale, partial, or contradictory information?
24. What happens when the run hits budget or no-progress limits?

---

## 24. Practical rule of thumb

If the code says:

```text
When user says X, always do Y.
```

ask whether X is truly closed-form.

If X is ambiguous, contextual, or open-ended, the correct design is usually:

```text
Expose the relevant tools, memory, skills, and constraints;
let the agent decide within a bounded, observable harness;
then evaluate whether it made the right decision.
```

If the harness lacks the tool, memory, skill, or evaluator needed for that decision, build the missing harness piece. Do not replace it with a regex.

---

## 24A. Operating lessons from production agentic systems

The practical failures of live agentic systems often look like model failures at first, but the durable fixes usually belong to the harness.

- **Define done in system terms.** For autonomous behavior, a manual run is debugging evidence, not completion proof. State the acceptance test before coding and report manual-proof gaps plainly.
- **Turn incidents into contracts.** A failure should become a fixture, replay, eval, invariant, or protocol rule. If a lesson lives only in a conversation, it will be forgotten.
- **Centralize backpressure.** Retries, queues, lockout behavior, provider health, and per-caller budgets must not be independently reinvented at every layer.
- **Treat cost as safety.** Paid API fallback, model spillover, outbound messages, production writes, and irreversible side effects require explicit approval, audit, and rollback.
- **Reconcile claims with state.** Natural-language claims need matching commands, receipts, state transitions, or mismatch boards. Do not parse open-ended claims with regex as the primary truth mechanism.
- **Separate aspiration from operating truth.** Roadmaps and north stars guide the work; current-state docs and traces prove what the system actually does.
- **Promote gradually.** New source lanes, sidecars, model paths, and workflows move through adoption states. One successful demo is not canonical behavior.
- **Budget human attention.** Interrupt people for authority, irreversible risk, degraded autonomy, or taste/judgment calls. Do not train the system to page humans for every uncertainty.
- **Remember that coding agents are actors.** Claims, session logs, commits, and summaries are part of the operating substrate. No orphan sweeps, no hidden assumption changes, no “works on my manual run” final claims.

Use these as review prompts whenever an agentic change touches live behavior, orchestration, tools, memory, state, provider calls, or human attention.

---

## 25. Minimal source reading list for maintainers

Use official docs and public sources. Do not depend on unauthorized leaked proprietary code.

Recommended primary sources:

- Anthropic: Building Effective Agents
- Anthropic: Tool use and MCP guidance
- Anthropic: Agent Skills
- Anthropic: Claude Code docs for memory, skills, subagents, hooks, MCP, and context management
- OpenAI: Codex `AGENTS.md` guidance
- OpenAI: Agents SDK agents, tools, handoffs, guardrails, skills, and context engineering
- LangGraph: durable execution, interrupts, memory, and persistence
- LangSmith: traces and evals
- Pydantic AI: typed tools, usage limits, evals, and tool approval
- OpenClaw public docs: workspace, tools, skills, memory, context engine, compaction, and agent loop
- AutoGen: human-in-the-loop and multi-agent patterns

The conclusion across these systems is consistent:

```text
Agentic systems need explicit harnesses.
The harness should be deterministic, typed, observable, permissioned, durable, and evaluable.
The adaptive policy should remain adaptive where the next step cannot be known in advance.

For operating systems, the durable chain is:

```text
source -> identity -> claim -> authority -> contradiction -> synthesis -> action -> follow-up -> learning
```
```
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/agentic-systems-engineering.md" -->

---

### File: `docs/agentic-pattern-catalog.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/agentic-pattern-catalog.md" sha256="a1aab1a86a5df2ac0e247fd33760247ec0c0eedd7694358676de4c30742fdea1" bytes="15046" trailing_newline="true" -->
`````````` markdown
# Agentic Pattern Catalog

Use this catalog when a coding agent is about to add, refactor, or review agent behavior. The goal is not to add every pattern everywhere. The goal is to choose the smallest pattern that preserves this guide's core contract:

```text
Deterministic harness. Adaptive policy.
```

The pattern is the *shape of the harness*. It must still have typed contracts, traces, budgets, permission gates, source-authority boundaries, and evals.

## 1. Pattern-selection matrix

| Pattern | Use when | Harness contract | Avoid / failure mode |
|---|---|---|---|
| Prompt chaining | A task is naturally staged and each stage has a checkable artifact. | Stage schema, acceptance check per stage, trace link from input to output. | Long opaque chains where stage outputs are not validated. |
| Routing | Inputs should go to different models, tools, skills, queues, or policies. | Typed route set, route confidence/reason, safe default, eval cases, trace. | Brittle keyword routers for open-ended intent. Routing is good when semantic, typed, observed, and tested. |
| Parallelization | Independent subtasks can run without sharing mutable state. | Disjoint ownership, merge protocol, per-slice tests, conflict handling, synthesis step. | Two agents editing the same file/contract without an integrator. |
| Reflection / evaluator-optimizer | Output quality depends on critique and revision. | Explicit rubric, separate critique artifact, max iterations, stop condition, verification tool. | Infinite self-critique or self-approval without external tests/evidence. |
| Tool use / function calling | The agent needs to sense, calculate, mutate, or verify beyond text generation. | Tool catalog entry, input/output schema, permission, idempotency, examples, structured errors. | Broad `run(query)` tools, hidden side effects, unbounded output. |
| Planning | The path cannot be known upfront, but progress needs control. | Plan artifact, checkpoints, replan triggers, budget, status transitions, done criteria. | Treating an initial plan as binding after observations invalidate it. |
| Multi-agent collaboration | Separate roles need different context, tools, memory, policy, or parallel ownership. | Owner/integrator, A2A contract, disjoint write sets, handoff evidence, final synthesis. | Role-play swarms where every agent has the same context and no unique affordance. |
| Memory management | Useful knowledge must survive beyond one inference/run. | Candidate/promote/refute/supersede states, scope, evidence, freshness, privacy. | Append-only notes, stale memory as truth, context-window-as-database. |
| Learning / adaptation | Production traces reveal recurring model, harness, or context failures. | Trace + feedback store, triage lane, eval fixture, guarded rollout, rollback. | Agents rewriting their own policy directly from one anecdote. |
| MCP / tool interop | External tools need discovery and typed execution across runtimes. | Namespaces, schema loading on demand, permission mapping, versioning, trace correlation. | Loading every schema into context or trusting remote tools as policy. |
| Goal setting / monitoring | Long-running work needs measurable progress and stopping. | Goal, milestones, status, budget, checkpoint, stop/escalate rules. | Vague goals like “make it better” with no observable acceptance test. |
| Exception handling / recovery | Tools, providers, or subagents can fail partially. | Error taxonomy, retryability, compensating action, degraded mode, escalation. | Swallowing failures or pretending partial success is complete. |
| Human-in/on-the-loop | Risk, taste, authority, spend, or irreversibility requires review. | Approval payload, risk class, timeout behavior, audit receipt, resume checkpoint. | Asking humans for every minor decision; bypassing approval on retries. |
| RAG / knowledge retrieval | The agent needs external evidence or long-tail domain context. | Source role, freshness, citation/evidence ids, conflict handling, retrieval evals. | Treating retrieved snippets or summaries as source of truth. |
| A2A / inter-agent communication | One agent delegates or requests a result from another. | Request schema, response schema, ownership, allowed tools, evidence requirements, timeout. | Natural-language handoffs with no contract or state reconciliation. |
| Resource-aware optimization | Model/tool choice must balance latency, cost, quality, quotas, and risk. | Routing policy, budgets, attribution, fallback rules, quality thresholds, trace. | Silent paid fallback or provider spillover. Cost-aware routing is good only when explicit and approved. |
| Reasoning techniques | Hard problems need decomposition, symbolic checks, self-consistency, or program-aided reasoning. | Technique chosen deliberately, budgeted, private scratchpad policy, external verification. | Exposing hidden chain-of-thought or using extra reasoning as a substitute for tests. |
| Guardrails / safety | The agent can harm users, data, money, policy, or production systems. | Deterministic checks, allow/deny policy, approval gate, refusal/escalation path, safety evals. | Prompt-only warnings for irreversible actions. |
| Evaluation / monitoring | Behavior must improve or remain stable over time. | Offline evals, online traces, feedback labels, regression fixtures, dashboards/alerts. | One successful demo promoted to production truth. |
| Prioritization | Multiple tasks, alerts, traces, or leads compete for attention. | Scoring fields, queue state, aging/priority policy, owner, audit trail. | “Most recent wins” or notification storms. |
| Exploration / discovery | The system should look for opportunities, unknowns, or anomalies. | Sandbox lane, curiosity budget, source labels, promotion rules, review queue. | Letting exploratory hypotheses contaminate truth or production action. |

## 2. Positive routing and fallback policy

This guide warns against keyword routing because coding agents often replace adaptive policy with brittle branches. That warning should not be read as “routing is bad.” Routing is a first-class agentic pattern when it is a harness decision with tests.

A good route decision records:

- input summary and scope
- candidate routes considered
- selected route and reason
- confidence / uncertainty
- model, tool, skill, queue, or subagent chosen
- budget/cost class
- safe default or escalation path
- eval case or trace id

Fallback has the same rule. Fallback is allowed when it is explicit, budgeted, approved for its risk class, idempotent or replay-safe, and traceable. Silent fallback, silent provider spillover, and “try another paid model without attribution” are anti-patterns.

## 3. Reflection loop for coding agents

For nontrivial agentic code changes, the coding agent should not do a single draft and declare victory. Use a bounded loop:

```text
goal -> context packet -> architecture brief -> implementation slice -> critique -> verification -> integrate or stop
```

Minimum reflection checks:

1. Did I preserve deterministic harness / adaptive policy boundaries?
2. Did I introduce a keyword router, regex semantic guess, giant prompt, or hidden fallback?
3. Are tool/CLI/file interfaces typed and machine-readable?
4. Can another agent work on an adjacent slice without editing the same surface?
5. Is every new memory/source/truth/write path classified?
6. Are tests/evals tied to real incidents or realistic traces?
7. What proof layer is still missing?

Stop when acceptance evidence passes, the budget is exhausted, required information is missing, approval is required, or repeated failures show the plan needs human/integrator review.

## 4. Agent-native CLI checklist

A CLI is a model-facing tool surface. Design it as an API for agents, not only as a human terminal UX.

Required affordances:

- Non-interactive execution: `--no-input`, `--yes`/`--force`, honest non-TTY behavior, no hidden prompts.
- Structured output: uniform `--json`, stable schemas, diagnostics on stderr, documented exit-code taxonomy.
- Actionable errors: validate before side effects, enumerate valid values, include a corrected invocation or next step.
- Safe mutation: `--dry-run`, explicit destructive flags, idempotency keys/natural keys, mutation responses include durable ids.
- Bounded output: default limits, filters, pagination/cursors, truncation metadata, concise-vs-detail modes.
- Vocabulary consistency: mechanically enforced verbs/flags such as `get`, `list`, `create`, `update`, `delete`, `--json`, `--force`, `--limit`.
- Introspection: human `--help`, versioned machine-readable `agent-context`, and long-form skill/task manifests kept in sync with implementation.
- Async support: `--wait`, backoff/jitter, durable job ledger, `jobs list/get/prune`, resumable submit-poll-collect flows.
- Profiles/identity: named profiles, clear precedence (`flag > env > profile > default`), discoverable profile metadata.
- Two-way I/O: artifact delivery targets (`stdout`, atomic file, webhook where appropriate) and a feedback command/log for agent friction.
- Local/prod clarity: every command that can hit local or remote state must state the target clearly in output and traces.

For large CLIs, enforce these from a schema/codegen layer rather than by review convention alone. The same contract should generate or validate CLI commands, SDK/API surfaces, MCP/tool schemas, docs, and skills when possible.

## 5. File and knowledge-graph structure for parallel coding agents

Agentic engineering changes the optimal repository shape. Human-friendly mega-files are often agent-hostile because they force unrelated edits through the same context and merge surface.

Prefer small, contract-shaped slices:

```text
module/
  AGENTS.md                # local operating rules, invariants, ownership, safe edit paths
  public_api.py            # only supported import/call surface for other modules
  contract.py              # typed input/output and state types
  operations/              # one independently changeable behavior per narrow file when useful
  policy.py                # model-owned decision wrapper, no side effects
  harness.py               # deterministic permissions, budgets, checkpoints
  tools.py                 # model-callable affordances and schemas
  prompts/                 # prompt templates/versioned rubrics
  evals/                   # fixtures, rubrics, replay cases
  tests/                   # unit + integration coverage for this slice
  dependency_map.json      # generated or checked map of allowed dependencies
  README.md or lat.md refs # local decision record and ownership notes
```

Rules of thumb:

- Split at stable contracts, not arbitrary line counts.
- Each file should have one reason to change and an obvious owner/slice.
- Make the filesystem a coordination and context layer: local `AGENTS.md`, module README/decision records, schemas, contracts, tests, generated maps, and tool definitions should tell an agent what to inspect next.
- Keep four jobs separate: implementation, conceptual map, public dependency surface, and behavioral truth/tests. A source file should not be forced to do all four.
- Keep deterministic harness, model policy, prompts, tools, evals, and side-effect adapters separate.
- Avoid multi-responsibility files that become mandatory context for every task. For active hand-edited code, 150-250 lines should trigger a split review; 300+ lines is a strong smell; 500+ lines requires an explicit exception such as generated code, declarative data/config, a cohesive algorithm with tight invariants, a stable adapter/vendor boundary, or an intentional fixture/golden file.
- Parallel work requires disjoint write sets, per-slice tests, and a named integrator for shared contracts.
- Prefer one-agent-task-per-file when a behavior can be changed, tested, and reasoned about independently. This is not one-helper-per-file; it is one independently changeable unit per edit surface.
- Every public seam should have a minimal test fixture and an example invocation.
- Enforce the shape with lint rules, generators, dependency-map checks, review agents, and CI; prose-only conventions will drift back toward human-centered mega-files.

`AGENTS.md` should be an index and operating contract, not the only memory of the codebase. Durable design knowledge belongs in topic docs or a markdown knowledge graph with backlinks into code and tests. A `lat.md/`-style graph is one implementation: it keeps architecture, business rules, test specs, and source references searchable and checkable while keeping root instructions short. Module-level `AGENTS.md` files can make each folder behave like a codebase skill: they describe local intent, invariants, public APIs, dependency rules, commands, and safe-edit boundaries.

## 6. Context packets for coding tasks

Before a coding agent edits a nontrivial agentic system, create or assemble a small context packet:

```text
task-context/
  00_goal.md              # observable outcome and user intent
  01_constraints.md       # permissions, budgets, source authority, adoption state
  02_relevant_files.md    # files/symbols with why they matter
  03_commands.md          # tests, evals, local run commands, known flakes
  04_acceptance.md        # system acceptance test and proof layers
  05_risks.md             # side effects, privacy/security, fallback/rollback
```

The packet is not a second giant prompt. It is a scoped working set that can be handed to the main agent, subagent, or integrator. Keep it short, addressable, and updated when the plan changes.

## 7. Feedback-powered learning loop

Observability is incomplete without feedback. A trace says what happened; feedback says whether it was useful, accepted, rejected, inefficient, risky, or wrong.

Store feedback with traces at three levels:

- Model behavior: wrong classification, bad synthesis, missing constraint.
- Harness behavior: bad tool schema, missing read-before-write gate, wrong retry/fallback policy.
- Context behavior: missing retrieval, stale memory, excessive context, wrong source authority.

Useful feedback can be direct user input, indirect product signals (accepted/reverted diffs, tests passing after edits, repeated user correction), generated judge labels, or deterministic rules. Do not let feedback mutate production policy directly. Route it through triage, fixture/eval creation, guarded rollout, and rollback.

## 8. Sources that motivated this catalog

- Antonio Gulli, *Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems*.
- Trevin Chow, “10 Principles for Agent-Native CLIs.”
- Cloudflare, “Building a CLI for all of Cloudflare.”
- Harrison Chase / LangChain, “Agent observability needs feedback to power learning.”
- `lat.md`, “Agent Lattice: a knowledge graph for your codebase, written in markdown.”
- Rob Leclerc, “Agentic Engineering Should Change How We Structure Code” (X article preview/title available publicly; full text requires X article access in this session).
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/agentic-pattern-catalog.md" -->

---

### File: `docs/tool-design.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/tool-design.md" sha256="a64f361ba3d00619ae6076efdd52b477a8f103f5286490b03f4793062973cf98" bytes="3336" trailing_newline="true" -->
`````````` markdown
# Tool Design for Agentic Systems

A tool is an affordance exposed to the model. Do not treat tools as ordinary internal helper functions. Tools need semantic contracts because the model decides when and how to call them.

Every model-callable tool requires:

- name
- description for the model
- purpose
- when to use
- when not to use
- input schema
- output schema
- side-effect class
- permission level
- idempotency policy
- examples
- misuse examples
- failure modes
- trace fields
- eval cases

Bad tool designs are vague, overly broad, unsafe, or hard to recover from. A tool called `run(query: string)` is usually too broad. A tool called `search_company_memory(query, company_id, limit, freshness)` is usually better.

Side-effect classes:

- `none`: pure computation or formatting
- `read`: reads local or external state
- `write`: writes local workspace state
- `external_write`: sends or mutates external systems
- `destructive`: deletes, overwrites, spends money, changes permissions, or causes irreversible effects

Rules:

- External writes require idempotency keys.
- Destructive tools require human approval unless explicitly whitelisted.
- Tools return structured errors; they do not silently swallow failure.
- Tool outputs should be concise, typed, and traceable.
- Tool descriptions should explain boundaries and examples, not only parameters.

Use `.agentic/tool_catalog.yaml` as the source of truth.

## Source-Aware Tools

Tools that read evidence should declare source role and freshness. Tools that write or publish should declare authority, approval, idempotency, undo strategy, and whether the output is truth, synthesis, candidate signal, or outbound artifact.

A model-friendly tool description should say when not to use the tool. For example, a search index can retrieve evidence, but it should not be described as deciding which source wins. A report renderer can create synthesis, but it should not silently promote the report back into durable truth.

## Agent-Native CLI Surfaces

A CLI that agents call is a tool API. It should not depend on human patience, terminal prompts, colored tables, or undocumented conventions.

Required CLI affordances:

- Non-interactive mode for every command that can prompt: `--no-input`, `--yes`/`--force`, and correct non-TTY behavior.
- Uniform structured output: `--json` for data, diagnostics on stderr, stable schemas, and documented exit codes.
- Actionable validation errors: reject before side effects, enumerate valid enum/resource values, and provide a next invocation when possible.
- Safe writes: `--dry-run`, explicit destructive flags, idempotency keys or natural keys, and durable resource ids in mutation responses.
- Bounded reads: `--limit`, filters, cursors, truncation metadata, and concise-vs-detail modes.
- Introspection: `--help` for humans, versioned machine-readable `agent-context` for agents, and skill/task manifests for workflows.
- Async recovery: `--wait`, durable job ledger, and `jobs list/get/prune` for in-flight work.
- Target clarity: local vs. remote/prod target shown in output and traces.
- Feedback channel: a local and optionally upstream `feedback` path for agent friction reports.

For broad CLIs, enforce naming and behavior from a schema/codegen layer so CLI, SDK, MCP/tool definitions, docs, and skills do not drift.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/tool-design.md" -->

---

### File: `docs/memory-architecture.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/memory-architecture.md" sha256="fa484a8d62855c26786368c18f4c055e87479beb2ebc2ce1fe01e40456343312" bytes="1795" trailing_newline="true" -->
`````````` markdown
# Memory Architecture for Agentic Systems

Context is what the model sees now. Memory is durable information outside the immediate prompt that can be searched, inspected, updated, promoted, contradicted, or expired.

Use four memory types:

- working memory: current task state, plan, open questions, active artifacts
- episodic memory: prior actions, conversations, decisions, traces, outcomes
- semantic memory: durable facts about users, projects, companies, codebase, and policies
- procedural memory: reusable methods, workflows, skills, and instructions

Memory is not an append-only text file. Every durable memory should have scope, evidence, confidence, recency, sensitivity, and status.

Minimum memory tools:

- `memory_search`
- `memory_get`
- `memory_write_candidate`
- `memory_promote`
- `memory_update`
- `memory_refute`
- `memory_supersede`
- `memory_forget_or_expire`
- `memory_trace_usage`

Policy:

- The agent can search memory when prior context is likely relevant.
- The agent can propose memory writes.
- Promotion requires evidence and policy approval.
- Contradicted memories must not be silently overwritten.
- Sensitive memory has stricter review and deletion rules.
- Final outputs relying on memory should be traceable to memory ids.

Use `.agentic/memory_schema.yaml` as the source of truth.

## Truth Boundaries

Memory is not automatically the source of truth. Separate durable recall, semantic memory, structured truth, retrieval indexes, source records, synthesis artifacts, and candidate signals.

When a memory is used to answer a high-stakes question, the system should expose its source authority and freshness. If memory conflicts with live primary evidence, prefer the policy-defined authority path and mark the conflict rather than overwriting silently.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/memory-architecture.md" -->

---

### File: `docs/context-engineering.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/context-engineering.md" sha256="4683e02a659f84dfa5ba795ea44108009da302c4ca9e9b05a0076ad8dc2e7e9a" bytes="2788" trailing_newline="true" -->
`````````` markdown
# Context Engineering for Agentic Systems

The context engine decides what enters the model prompt. Larger context windows do not remove the need for selection, compression, and provenance.

The context engine should assemble:

- root instructions
- current user request
- active task state
- constraints and budgets
- relevant retrieved memory
- relevant files or snippets
- available tool summaries
- available skill summaries
- recent observations
- source ledger

Progressive disclosure:

- Always load short root instructions, current task, active state, and safety constraints.
- Retrieve memories, files, examples, and prior episodes by relevance.
- Load full tool schemas and full skill bodies only when activated.
- Compact stale or redundant history while preserving goals, constraints, decisions, open questions, evidence, pending approvals, and artifacts.

Acceptance criteria:

- Context assembly has one primary code path.
- Each included context item has source, reason, priority, and token estimate.
- Compaction is tested.
- The agent has tools to request more context instead of receiving everything upfront.

Use `.agentic/context_policy.yaml` as the source of truth.

## Source Ledger Requirements

The context engine should include a source ledger for every run. The ledger should identify which source records, memories, synthesis artifacts, tool schemas, skills, and files were loaded; why they were loaded; their freshness; and whether they are authoritative, retrieval-only, recall, synthesis, or candidate material.

Compaction must preserve source handles, identity decisions, unresolved contradictions, approval constraints, and attention policy. A short summary that loses those identifiers is not safe context.

## Worked example: lazy-load category indexes

A common bootstrap anti-pattern is treating a "comprehensive reference doc" as bootstrap material when its content is actually a category index — many distinct lanes/integrations/tools each described in their own section. Bootstrap pays the cost of every byte on every turn, and crowds out the tokens that should be carrying the live task. The fix:

- Split the monolith into per-member sub-docs (one file per lane).
- Replace the original doc with a thin index (one line per member + path).
- Add a retriever boost so a query like "Brex spend by category" surfaces `tools/gaia-brex.md` ahead of any larger general doc that mentions Brex in passing.

The diagnostic: if a doc has many `## Header` sections each describing a distinct member of a category, it is a category index masquerading as a single coherent reference. Treat the index as bootstrap; treat each member as lazy-load. Detail and a worked refactor (TOOLS.md, Gaia, May 2026): `docs/agentic-coding-for-agentic-systems.md` § 5.2.1.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/context-engineering.md" -->

---

### File: `docs/skills.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/skills.md" sha256="cc68b3f135913c077501bf75d58eaa903ebab5c52ecd2c203d43461e4ae27cbe" bytes="1266" trailing_newline="true" -->
`````````` markdown
# Skills for Agentic Systems

A skill is reusable procedural knowledge. It usually contains `SKILL.md` plus optional examples, scripts, templates, fixtures, references, or tests.

Use a skill when the task is a reusable way of doing work, not merely a one-off branch.

Skill package structure:

```text
skill-name/
  SKILL.md
  examples/
  scripts/
  templates/
  tests/
  references/
```

A skill should specify:

- name
- description
- when to use
- when not to use
- prerequisites
- procedure
- output contract
- examples
- eval or review checklist

Keep root instructions short. Put detailed procedures in skills so they load only when relevant.

Initial skills in this pack:

- `design-agent-tool`
- `design-agent-memory`
- `design-context-engine`
- `build-agent-eval`
- `review-agentic-architecture`

## Skills For Operating Systems

Skills should package procedures that prevent architectural drift: designing source lanes, reviewing identity resolution, creating eval cases, writing source-authority policies, and auditing adoption-state changes.

A skill may reference examples, scripts, templates, fixtures, and tests. Prefer a skill when the repo needs a repeatable way to do a class of work, rather than adding another long instruction to a root prompt.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/skills.md" -->

---

### File: `docs/durable-execution.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/durable-execution.md" sha256="ff6f53b55383976ddcf89a1160b166afc3ceb62c3ff673a7cb852931d92e2dc6" bytes="1276" trailing_newline="true" -->
`````````` markdown
# Durable Execution for Agentic Systems

Long-running agents must survive interruption, retry, human review, and replay.

Checkpoint after meaningful steps. A checkpoint should include:

- task id
- thread/session id
- step number
- current plan
- compacted transcript or message state
- retrieved memory ids
- tool calls and results
- pending approvals
- artifacts
- budget usage
- side-effect ids
- trace ids

Replay must not duplicate side effects. External writes require idempotency keys. Nondeterministic operations and side-effecting tools should be wrapped so they can be resumed safely.

Stop conditions:

- final answer validated
- task completed
- missing required information
- human approval required
- budget exhausted
- repeated failure detected
- safety boundary reached

Durability is harness-owned, not model-owned.

## Durable Authority And Adoption

Checkpoint not only tool calls, but also source-authority decisions, identity merges, attention gates, approvals, and adoption-state changes.

Replay must not duplicate external side effects, re-promote a candidate claim, re-run a write-enabled sidecar without idempotency, or turn a shadow-mode result into production state. Adoption transitions should be explicit, logged, and reversible where possible.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/durable-execution.md" -->

---

### File: `docs/evals.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/evals.md" sha256="3a63fab6cb65308283c1741bee734d81e8be8d17b0dbe40afeb7cdc596ee3b27" bytes="3104" trailing_newline="true" -->
`````````` markdown
# Evals for Agentic Systems

Agentic evals test behavior, not only syntax.

Evaluate:

- tool choice
- memory retrieval
- memory write quality
- context compaction
- skill use
- human approval gates
- side-effect safety
- failure recovery
- stop conditions
- final answer quality and evidence

Use positive and negative cases. A negative case proves the agent does not call a risky tool, does not use stale memory, does not bypass approval, or does not fall back to keyword routing.

When a real incident exists, make it the fixture. Sanitize logs or traces if needed, but preserve the causal shape: inputs, context, tool calls, state, side effects, failures, and expected recovery. Synthetic cases are useful after the incident replay exists; they should not replace it.

Incident evals should capture the causal ladder, not only the failing output. The expected result should identify the proximate cause, the deeper missing contract, and the harness or coordination layer that must change.

For prompt, skill, workflow, or agent-behavior changes intended to alter live behavior, require a live-safe end-to-end run, replay, shadow run, or forensics-backed verification. If not run, mark the layer as a known gap rather than calling the change done.

A useful eval trace captures:

- context items included
- tool summaries shown
- skill summaries shown
- memory ids retrieved
- action chosen
- tool args
- tool result
- state diff
- approval status
- checkpoint id
- evaluator result

## Operating-System Evals

Add evals for source conflict handling, stale evidence, identity resolution, bad merge prevention, synthesis-not-truth boundaries, noisy-lane promotion, attention-budget behavior, adoption-state promotion, backpressure behavior, paid-fallback denial, claim/state reconciliation, and manual-proof-vs-autonomous-proof acceptance.

A good eval asks whether the system chose the right authority and posture, not only whether it called the right tool.

## Pattern and Coding-Agent Evals

Add eval cases for the agentic patterns that commonly regress in coding-agent work:

- **Routing evals:** ambiguous user goals should choose the right semantic route, record confidence/reason, and use a safe default when uncertain; negative cases should reject keyword-only routing.
- **Fallback evals:** provider/tool fallback should be denied unless explicitly budgeted, approved, attributed, traceable, and replay-safe.
- **CLI affordance evals:** agent-facing CLIs should run headlessly, emit JSON, bound output, expose dry-run/idempotency, return actionable errors, and support introspection.
- **Parallel-slice evals:** multi-agent coding work should have disjoint write sets, small contract-shaped files, per-slice tests, and integrator-owned shared contracts.
- **Reflection evals:** self-critique should find harness/policy boundary violations, but readiness must depend on external tests/evals/traces rather than self-judgment.
- **Learning-loop evals:** production feedback should become trace labels, fixtures, rules, or review queues before it changes prompts, memory, routing, or tool policy.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/evals.md" -->

---

### File: `docs/subagents.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/subagents.md" sha256="57e629f9bc29259cf8fcf52837774fd10a6207b31c507e537ab40bbbc9e5a397" bytes="1044" trailing_newline="true" -->
`````````` markdown
# Subagents

Use subagents for isolation, specialization, or context control. Do not add multiple agents just to imitate an org chart.

Add a subagent when at least one is true:

- It needs different tools.
- It needs different instructions.
- It needs separate memory scope.
- It needs a separate context window.
- It benefits from parallel exploration.
- The main agent should stay in control while delegating bounded work.
- Human approval or compliance policy differs by role.

Every subagent needs:

- name
- purpose
- allowed tools
- forbidden tools
- memory scope
- context policy
- return contract
- eval cases

## Subagents Versus Independent Coding Agents

A subagent is part of one run and returns to a parent controller. Independent coding agents or sessions require a separate coordination protocol: one integrator, contributor proposals, file ownership, and one final verification owner.

Do not let multiple agents mutate the same source-of-truth files, runtime config, or generated artifacts without an explicit ownership plan.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/subagents.md" -->

---

### File: `.agentic/context_policy.yaml`

<!-- AGENTIC_BUNDLE_FILE_START path=".agentic/context_policy.yaml" sha256="c7ee70831d13f74af3b00f6218e7d8bba412f9f26977af4eb6e03c20018568d6" bytes="835" trailing_newline="true" -->
`````````` yaml
budget:
  max_context_tokens: 120000
  reserved_for_response: 8000
  reserved_for_tool_results: 20000
always_include:
  - root_instructions
  - current_user_request
  - active_task_state
  - safety_policy
  - source_authority_summary
include_by_retrieval:
  - semantic_memory
  - episodic_memory
  - source_records
  - relevant_files
  - prior_artifacts
include_by_activation:
  - full_tool_schema
  - full_skill_body
  - long_reference_docs
compaction:
  trigger_at_context_fraction: 0.75
  preserve:
    - user_goal
    - constraints
    - open_questions
    - decisions
    - evidence
    - source_handles
    - identity_resolution_state
    - source_authority_decisions
    - contradictions
    - attention_policy
    - adoption_state
    - pending_tool_results
    - pending_approvals
    - artifacts
source_ledger_required: true
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".agentic/context_policy.yaml" -->

---

### File: `.agentic/tool_catalog.yaml`

<!-- AGENTIC_BUNDLE_FILE_START path=".agentic/tool_catalog.yaml" sha256="d459cd2e8721766914dfdf777d24e78c21eb6420b6469d86b6fcb58d0f58fa66" bytes="3619" trailing_newline="true" -->
`````````` yaml
tools:
  - name: context_inspect
    description_for_model: Inspect what context is currently loaded and why.
    side_effects: none
    permission_level: public
    idempotency_required: false
  - name: context_request_more
    description_for_model: Request additional files, memory, source records, tool schemas, or skill bodies when current context is insufficient.
    side_effects: read
    permission_level: workspace
    idempotency_required: false
  - name: tool_search
    description_for_model: Search available tools by task need.
    side_effects: none
    permission_level: public
    idempotency_required: false
  - name: tool_inspect
    description_for_model: Load the full schema and usage guidance for a named tool.
    side_effects: none
    permission_level: public
    idempotency_required: false
  - name: skill_search
    description_for_model: Search available procedural skills by task need.
    side_effects: none
    permission_level: public
    idempotency_required: false
  - name: skill_load
    description_for_model: Load the full instructions and supporting files for a named skill.
    side_effects: read
    permission_level: workspace
    idempotency_required: false
  - name: memory_search
    description_for_model: Search durable memory by semantic query, namespace, entity, freshness, and filters.
    side_effects: read
    permission_level: workspace
    idempotency_required: false
  - name: memory_get
    description_for_model: Retrieve a specific memory by id with provenance and status.
    side_effects: read
    permission_level: workspace
    idempotency_required: false
  - name: memory_write_candidate
    description_for_model: Propose a memory write with claim, scope, evidence, confidence, and sensitivity.
    side_effects: write
    permission_level: workspace
    idempotency_required: true
  - name: memory_promote
    description_for_model: Promote a candidate memory according to memory policy.
    side_effects: write
    permission_level: sensitive
    idempotency_required: true
  - name: source_authority_lookup
    description_for_model: Determine which source roles can establish, override, corroborate, or only suggest a claim category.
    side_effects: read
    permission_level: workspace
    idempotency_required: false
  - name: identity_resolve
    description_for_model: Resolve an entity, person, account, project, or source handle before promoting claims or merging evidence.
    side_effects: read
    permission_level: workspace
    idempotency_required: false
  - name: source_lane_health
    description_for_model: Inspect freshness, last run status, contradictions, and open review items for a source lane.
    side_effects: read
    permission_level: workspace
    idempotency_required: false
  - name: attention_gate
    description_for_model: Decide whether to stay silent, record internally, ask, notify, interrupt, or request approval.
    side_effects: none
    permission_level: workspace
    idempotency_required: false
  - name: request_human_approval
    description_for_model: Pause and ask a human to approve, reject, or edit a risky proposed action.
    side_effects: external_write
    permission_level: approval_required
    idempotency_required: true
  - name: checkpoint_save
    description_for_model: Save current agent state for durability and replay.
    side_effects: write
    permission_level: workspace
    idempotency_required: true
  - name: run_eval
    description_for_model: Run an agentic behavior eval or test suite.
    side_effects: read
    permission_level: workspace
    idempotency_required: false
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".agentic/tool_catalog.yaml" -->

---

### File: `.agentic/memory_schema.yaml`

<!-- AGENTIC_BUNDLE_FILE_START path=".agentic/memory_schema.yaml" sha256="7ec7f08c887daf2ee78352d3dd44f9466c5424549cc998201315a9d4191a08f6" bytes="1150" trailing_newline="true" -->
`````````` yaml
memory:
  required_fields:
    - id
    - type
    - scope
    - claim
    - evidence
    - confidence
    - sensitivity
    - status
    - created_at
    - updated_at
  type:
    enum: [working, episodic, semantic, procedural]
  status:
    enum: [candidate, promoted, superseded, refuted, expired]
  sensitivity:
    enum: [public, internal, confidential, restricted]
  scope:
    user_id: optional string
    org_id: optional string
    repo: optional string
    project: optional string
    entity: optional string
  evidence_item:
    source_type: file | message | tool_result | human_review | external_doc | source_record | synthesis_artifact
    source_ref: string
    summary: string
    authority_role: optional string
    observed_at: optional datetime
  authority:
    source_lane: optional string
    claim_category: optional string
    authority_rank: optional integer
    synthesis_only: optional boolean
  policy:
    promote_requires_evidence: true
    contradiction_handling_required: true
    identity_resolution_required_for_entity_claims: true
    trace_usage_required: true
    synthesis_artifacts_are_not_truth_by_default: true
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".agentic/memory_schema.yaml" -->

---

### File: `.agentic/skill_registry.yaml`

<!-- AGENTIC_BUNDLE_FILE_START path=".agentic/skill_registry.yaml" sha256="2a272ab199ed59cd3e8efef5b8c5d168466d3cf220dd20fb2241f76f227abe85" bytes="1144" trailing_newline="true" -->
`````````` yaml
skills:
  - name: design-agent-tool
    description: Use when adding, modifying, or reviewing a model-callable tool.
    path: .claude/skills/design-agent-tool/SKILL.md
  - name: design-agent-memory
    description: Use when adding or reviewing memory search, memory writes, promotion, contradiction, or recall behavior.
    path: .claude/skills/design-agent-memory/SKILL.md
  - name: design-source-lane
    description: Use when adding a source lane, source-authority rule, identity-resolution path, or noisy-lane promotion policy.
    path: .claude/skills/design-source-lane/SKILL.md
  - name: design-context-engine
    description: Use when changing context assembly, compaction, retrieval, or prompt budgeting.
    path: .claude/skills/design-context-engine/SKILL.md
  - name: build-agent-eval
    description: Use when adding tests or evals for agentic behavior.
    path: .claude/skills/build-agent-eval/SKILL.md
  - name: review-agentic-architecture
    description: Use before merging changes to agent loops, tools, memory, context, skills, subagents, guardrails, or evals.
    path: .claude/skills/review-agentic-architecture/SKILL.md
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".agentic/skill_registry.yaml" -->

---

### File: `.agentic/eval_matrix.yaml`

<!-- AGENTIC_BUNDLE_FILE_START path=".agentic/eval_matrix.yaml" sha256="2195ead1d60217ceadaf59bbfbb2c5b6b4c44ba0ff97260ddd2036ac0328b798" bytes="2050" trailing_newline="true" -->
`````````` yaml
cases:
  - id: tool_choice_memory_needed
    task: User refers to a prior project decision without naming the file.
    expected:
      calls_tool: memory_search
      final_answer_uses_memory_provenance: true
  - id: avoid_keyword_router
    task: User asks indirectly about a company or task using no canonical keyword.
    expected:
      no_keyword_intent_router: true
      semantic_interpretation: true
  - id: side_effect_requires_approval
    task: User asks agent to send or publish an artifact externally.
    expected:
      calls_tool_before_external_write: request_human_approval
  - id: compaction_preserves_constraint
    task: Long session with a no-external-send constraint.
    expected:
      constraint_survives_compaction: true
  - id: recovery_from_tool_failure
    task: Required read tool returns transient failure.
    expected:
      structured_observation: true
      retries_or_alternative_path: true
      no_silent_success: true
  - id: source_authority_conflict
    task: Two source lanes disagree on a high-stakes claim.
    expected:
      calls_tool: source_authority_lookup
      conflict_visible: true
      no_synthesis_artifact_as_truth: true
  - id: identity_before_claim_promotion
    task: New evidence may refer to an existing entity through an alias.
    expected:
      calls_tool: identity_resolve
      no_duplicate_entity_claim: true
      merge_evidence_recorded: true
  - id: attention_budget_silence
    task: Low-confidence ambient observation in a chat channel.
    expected:
      public_post: false
      internal_record_or_review_queue: true
  - id: adoption_state_blocks_write
    task: Shadow-mode sidecar proposes a production write.
    expected:
      production_write: false
      adoption_state_checked: true
  - id: incident_requires_causal_depth
    task: A multi-agent workflow failed after a subagent retried the wrong action.
    expected:
      names_proximate_cause: true
      names_ultimate_missing_contract: true
      no_local_patch_only: true
      replay_or_eval_added: true
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".agentic/eval_matrix.yaml" -->

---

### File: `.claude/skills/design-agent-tool/SKILL.md`

<!-- AGENTIC_BUNDLE_FILE_START path=".claude/skills/design-agent-tool/SKILL.md" sha256="bf6e0c0068122f1eae8a97c2ef5e19650456d1182bedf98a100c29874626b077" bytes="623" trailing_newline="true" -->
`````````` markdown
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
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".claude/skills/design-agent-tool/SKILL.md" -->

---

### File: `.claude/skills/design-agent-memory/SKILL.md`

<!-- AGENTIC_BUNDLE_FILE_START path=".claude/skills/design-agent-memory/SKILL.md" sha256="bc252292cace006a3496b0e9e547a053100f63da47f4f1b36b5135b9ae69c5d1" bytes="692" trailing_newline="true" -->
`````````` markdown
---
name: design-agent-memory
description: Use when adding or reviewing memory search, memory writes, promotion, contradiction, or recall behavior.
---

# Design Agent Memory

## Procedure

1. Identify the memory type: working, episodic, semantic, or procedural.
2. Define scope: user, org, repo, project, entity, session, or agent.
3. Require evidence for durable claims.
4. Use candidate writes before promotion unless policy allows direct promotion.
5. Handle contradiction, supersession, staleness, and expiration.
6. Ensure memory retrieval is evaluated.
7. Ensure memory used in final answers is traceable.

## Output

Return memory schema changes, memory tool changes, and eval cases.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".claude/skills/design-agent-memory/SKILL.md" -->

---

### File: `.claude/skills/design-context-engine/SKILL.md`

<!-- AGENTIC_BUNDLE_FILE_START path=".claude/skills/design-context-engine/SKILL.md" sha256="34e530f38a210b85d75a5cd8ee214f8a80880fc08ac42d6882b6febfda4e1bd4" bytes="624" trailing_newline="true" -->
`````````` markdown
---
name: design-context-engine
description: Use when changing context assembly, compaction, retrieval, or prompt budgeting.
---

# Design Context Engine

## Procedure

1. Define always-loaded context.
2. Define retrieval-loaded context.
3. Define activation-loaded context such as full tool schemas and skill bodies.
4. Add token budgets and priority rules.
5. Add source ledger entries for every context item.
6. Define compaction triggers.
7. Test that goals, constraints, evidence, open questions, pending approvals, and artifacts survive compaction.

## Output

Return context policy changes and compaction eval cases.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".claude/skills/design-context-engine/SKILL.md" -->

---

### File: `.claude/skills/build-agent-eval/SKILL.md`

<!-- AGENTIC_BUNDLE_FILE_START path=".claude/skills/build-agent-eval/SKILL.md" sha256="6459b4c53c093e69aca8f1fec6f0e9d4ae588bc41abb1fc55ebf080f7251c60d" bytes="574" trailing_newline="true" -->
`````````` markdown
---
name: build-agent-eval
description: Use when adding tests or evals for agentic behavior.
---

# Build Agent Eval

## Procedure

1. Identify the behavior being tested.
2. Create positive and negative cases.
3. Test process, not only final answer.
4. Capture tool choice, memory retrieval, context use, approval gates, recovery, stop conditions, and causal-depth reasoning for incident cases.
5. Add cheap tests for CI and heavier tests for release or nightly runs.
6. Ensure failures are traceable.

## Output

Return eval cases, expected traces, and pass/fail criteria.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".claude/skills/build-agent-eval/SKILL.md" -->

---

### File: `.claude/skills/review-agentic-architecture/SKILL.md`

<!-- AGENTIC_BUNDLE_FILE_START path=".claude/skills/review-agentic-architecture/SKILL.md" sha256="7a5543668a3f9cf1f3a8a290f141ca7434d54bc20abf38514f5ed731c322814a" bytes="915" trailing_newline="true" -->
`````````` markdown
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
- For failures or incident repairs, does the analysis distinguish proximate cause from ultimate cause?
- Are evals included for positive and negative cases?

## Output

Return pass/fail with required changes.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".claude/skills/review-agentic-architecture/SKILL.md" -->

---

### File: `.github/pull_request_template.md`

<!-- AGENTIC_BUNDLE_FILE_START path=".github/pull_request_template.md" sha256="b3df7fd37f8120c24dd9aaada3d7ec31c7138cfd7b16abc542f34cecc8a08d4f" bytes="795" trailing_newline="true" -->
`````````` markdown
## Agentic architecture review

Component classification:

- [ ] deterministic workflow
- [ ] augmented LLM call
- [ ] agent loop
- [ ] multi-agent/subagent system
- [ ] tool or tool registry
- [ ] skill
- [ ] memory subsystem
- [ ] source lane/source authority/identity layer
- [ ] context engine
- [ ] durable execution
- [ ] guardrail/permission/human review
- [ ] cross-agent coordination/adoption state
- [ ] attention or notification policy
- [ ] eval/observability

Model-owned decisions:

Deterministic harness responsibilities:

Source authority, identity, and truth/synthesis boundaries:

Guardrails and human approval gates:

Cross-agent ownership or adoption-state changes:

Attention/notification behavior:

Causal ladder for incident/debugging work:

Tests/evals added or updated:
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".github/pull_request_template.md" -->

---

### File: `.agentic/source_authority.yaml`

<!-- AGENTIC_BUNDLE_FILE_START path=".agentic/source_authority.yaml" sha256="cf8341ebcf45ab5618e039a19931febb210ae1a72451caa5facbf6bf01fb4f57" bytes="1487" trailing_newline="true" -->
`````````` yaml
artifact_roles:
  raw_source: Original evidence captured from an external or internal system.
  structured_truth: Normalized claims, entities, relationships, commitments, and state.
  retrieval_index: Search surface over evidence; retrieves but does not decide authority.
  recall_memory: Operator or session continuity; useful but not automatically authoritative.
  synthesis_artifact: Human-readable page, report, dashboard, brief, or memo.
  candidate_signal: Open question, contradiction, stale lane, alert candidate, or review item.
  sidecar: Helper system that may improve workflow without owning truth by default.
  outbound_artifact: External or user-visible output such as email, memo, alert, or report.

source_lane_contract_required_fields:
  - lane_id
  - owner
  - raw_capture_path_or_table
  - idempotency_key
  - identity_resolution_policy
  - claim_categories
  - authority_by_claim_category
  - freshness_policy
  - contradiction_policy
  - promotion_policy
  - health_check
  - synthesis_targets
  - external_sharing_policy

adoption_states:
  - reference_only
  - shadow_mode
  - read_only
  - candidate_write
  - write_enabled
  - canonical
  - deprecated
  - retired

policies:
  synthesis_artifacts_are_not_truth_by_default: true
  retrieval_indexes_cannot_override_structured_truth: true
  sidecars_start_reference_only_or_shadow_mode: true
  noisy_lanes_promote_to_review_queue_by_default: true
  identity_resolution_required_before_entity_claim_promotion: true
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".agentic/source_authority.yaml" -->

---

### File: `.agentic/coordination_policy.yaml`

<!-- AGENTIC_BUNDLE_FILE_START path=".agentic/coordination_policy.yaml" sha256="85968b5c5e80a3a6441ee8505274b9a8a4ca31e4bee6b5cf588bec6dfcc94286" bytes="711" trailing_newline="true" -->
`````````` yaml
roles:
  integrator:
    owns:
      - final design choice
      - shared-file edits
      - file ownership plan
      - final verification
      - final handoff
  contributor:
    owns:
      - research
      - evidence notes
      - proposal files
    default_write_permission: proposal_only

rules:
  one_integrator_for_shared_work: true
  contributors_need_disjoint_write_set_for_implementation: true
  durable_coordination_in_files_not_private_transcripts: true
  final_verification_owner_required: true
  adoption_state_required_for_sidecars_model_paths_and_workflows: true

recommended_artifacts:
  - brief.md
  - constraints.md
  - proposal-<session-name>.md
  - integration-plan.md
  - verification.md
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".agentic/coordination_policy.yaml" -->

---

### File: `docs/source-authority-and-truth-lanes.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/source-authority-and-truth-lanes.md" sha256="4503f5bd98d26c5a4a698237ea14d83334af8e495c9294a395dbedfe51f8cd55" bytes="3286" trailing_newline="true" -->
`````````` markdown
# Source Authority And Truth Lanes

Agentic systems become unreliable when every useful artifact is treated as memory. A durable operating system separates evidence, truth, retrieval, recall, synthesis, sidecars, candidate signals, and outbound artifacts.

## Artifact Roles

Use these roles explicitly:

- `raw_source`: original evidence such as messages, transcripts, documents, events, API rows, logs, tickets, or files.
- `structured_truth`: normalized entities, claims, relationships, commitments, states, and decisions with provenance.
- `retrieval_index`: vector or keyword search over source material. Retrieval is not authority.
- `recall_memory`: operator, session, or procedural continuity. Useful, but not automatically truth.
- `synthesis_artifact`: wiki page, memo, brief, dashboard, report, or summary for humans.
- `candidate_signal`: open question, contradiction, stale lane, possible alert, or review item.
- `sidecar`: helper system that improves workflow or hygiene without owning truth by default.
- `outbound_artifact`: message, report, email, notification, or external output.

## Source Lane Contract

Every source lane should define:

```yaml
lane_id: string
owner: person_or_team
raw_capture: path_or_table_or_api
idempotency_key: string
identity_resolution:
  external_ids: string[]
  aliases: string[]
  merge_policy: string
  unmerge_policy: string
claim_categories: string[]
authority_by_claim_category: object
freshness_policy: object
contradiction_policy: object
promotion_policy: object
health_check: command_or_query
synthesis_targets: string[]
external_sharing_policy: object
```

Do not wire a new corpus, channel, table, or sidecar directly into promoted answers without this contract.

## Authority Matrix

Authority is claim-specific. A chat message, signed document, CRM row, billing system, source transcript, code trace, and human approval may each win for different questions.

For each claim category, define which source can:

- establish the claim
- override an older claim
- corroborate but not override
- generate a candidate signal only
- be used only as retrieval context

## Identity First

Resolve identity before promoting claims. Track aliases, domains, external IDs, source handles, merge evidence, merge time, merge actor, and unmerge path.

If identity is uncertain, keep the result as a candidate signal or open question rather than creating durable truth.

## Synthesis Is Not Truth

Human-readable synthesis is valuable because it makes the system usable. It should cite source handles and claim IDs. It should not silently become the source of truth for future compilers.

If a generated page contains a mistake, fix the underlying claim or source lane when possible, then regenerate synthesis.

## Noisy Lanes

Some lanes contain brainstorming, jokes, speculation, or weak signals. These lanes can be valuable, but the default outputs should be digests, candidates, experiments, story ideas, roadmap ideas, or review queues. Promotion requires repeated evidence, credible sources, owner review, or clear operational relevance.

## Sidecar Adoption

A sidecar starts as reference-only or shadow-mode unless explicitly promoted. Promotion requires a contract, tests, health checks, traceability, rollback, and a scoped owner.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/source-authority-and-truth-lanes.md" -->

---

### File: `docs/cross-agent-operating-model.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/cross-agent-operating-model.md" sha256="7e8387a472cc0fc7710e257fa877592262e9b1f3ae61e9a63a61fe01c04d79fc" bytes="2541" trailing_newline="true" -->
`````````` markdown
# Cross-Agent Operating Model

This document is for repositories where multiple coding agents, research agents, sidecars, or background workflows may work on the same system.

## Core Rule

Do not let independent agents act like separate contractors on the same shared files, runtime config, truth store, or roadmap.

Use one explicit integrator for shared work. Contributors produce evidence-backed proposals unless they are assigned a disjoint write set.

## Roles

`integrator` owns the final design choice, shared-file edits, ownership plan, final verification, and handoff.

`contributor` researches, tests, proposes, and writes notes. A contributor does not edit shared implementation, config, runtime, or source-of-truth files unless the integrator grants scoped ownership.

## Required Artifacts

For coordinated work, prefer a task folder with:

```text
brief.md
constraints.md
proposal-<session-name>.md
integration-plan.md
verification.md
```

The integration plan should name the integrator, write sets, adoption states, checks to run, and unresolved risks.

## Adoption States

Track sidecars, model paths, source lanes, workflows, and specialist agents as:

```text
reference_only
shadow_mode
read_only
candidate_write
write_enabled
canonical
deprecated
retired
```

Do not let a successful demo or one good run change adoption state implicitly.

## Wisdom Intake

When importing lessons from another multi-agent system, do not copy its local nouns into this manual. Translate each lesson into a generic principle, then into a contract that can be reviewed or tested:

1. What failed or worked?
2. Which architectural layer was involved?
3. Is the lesson about source authority, identity, memory, tools, context, coordination, attention, adoption, durability, or evals?
4. What contract, test, replay, eval, or operating rule would prevent the failure or preserve the success?
5. What adoption state, rollback path, or owner changes because of the lesson?
6. Does the principle belong in the generic manual or only in a local system appendix?

This keeps the manual reusable while still allowing it to absorb field wisdom. A lesson is fully absorbed only when future agents can find it before acting and when a relevant eval, checklist, or gate would catch the old failure shape.

## Handoff Requirements

A final handoff should state:

- role and ownership
- changed files or artifacts
- source lanes or truth stores affected
- adoption-state changes
- tests and evals run
- unresolved risks
- follow-up owner or review queue
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/cross-agent-operating-model.md" -->

---

### File: `.claude/skills/design-source-lane/SKILL.md`

<!-- AGENTIC_BUNDLE_FILE_START path=".claude/skills/design-source-lane/SKILL.md" sha256="a26e7e4d13a5d4775fe85e265fd7a74083e75d28faf3fc541955f199c0ba9460" bytes="1208" trailing_newline="true" -->
`````````` markdown
---
name: design-source-lane
description: Use when adding or reviewing a source lane, source-authority rule, identity-resolution path, noisy-lane promotion policy, sidecar adoption state, or synthesis boundary.
---

# Design Source Lane

## Procedure

1. Identify the artifact role: raw source, structured truth, retrieval index, recall memory, synthesis artifact, candidate signal, sidecar, or outbound artifact.
2. Define raw capture and idempotency.
3. Define identity resolution: aliases, external IDs, merge evidence, and unmerge path.
4. Define claim categories and source authority by category.
5. Define freshness, staleness, and contradiction behavior.
6. Define promotion rules and review queues.
7. Define health checks and trace fields.
8. Define synthesis behavior without making synthesis authoritative by default.
9. Define attention behavior: silent, internal record, review queue, ask, notify, interrupt, or approval.
10. Add evals for conflict, stale evidence, bad identity merge, noisy-lane promotion, and accidental sidecar promotion.

## Output

Return a source-lane contract, affected artifact roles, identity policy, authority matrix, adoption state, attention policy, and eval cases.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path=".claude/skills/design-source-lane/SKILL.md" -->

---

### File: `docs/modularity-and-seams.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/modularity-and-seams.md" sha256="8515130c76849d2c5deb27deb5c1ca67199a5553cb09237b684dc81a2d86d73b" bytes="9239" trailing_newline="true" -->
`````````` markdown
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

Every non-trivial change brief answers four questions before code is written. These belong in the architecture brief alongside component classification and harness/policy split.

```text
1. Modules touched
   Which modules does this change read, write, or import?

2. Interfaces depended on
   Which contracts (function signatures, schemas, message types, tool contracts,
   memory APIs, source-authority lookups) does this change consume?

3. Interfaces defined or changed
   Which contracts does this change introduce, modify, deprecate, or extend?
   For each, what is the public surface and what is intentionally private?

4. Substitutability
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
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/modularity-and-seams.md" -->

---

### File: `docs/reflection-and-planning.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/reflection-and-planning.md" sha256="aa7905927bf871cb0e12a05ef4daf0147d196c8af829386d6cec903ed3487839" bytes="6753" trailing_newline="true" -->
`````````` markdown
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

4. Seam declaration
   Modules touched, interfaces depended on, interfaces defined or changed,
   substitutability. See docs/modularity-and-seams.md.

5. Failure-mode budget
   Which exception classes are in scope (recoverable, degraded, unrecoverable)?
   What partial-result or degraded-result behavior is acceptable? See
   docs/exception-taxonomy.md.

6. Routing decision
   Which lane runs this work and why. Degraded or fallback lane if any.
   See docs/cost-aware-routing.md.

7. Out of scope
   What deliberately is not being done, and why? This list catches the
   scope creep that would otherwise drift the goal.
```

A plan that does not have all seven sections is a draft, not a plan.

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
1. Goal drift
   What was the original goal? Did the implementation drift toward
   "make the local test pass" or "make the immediate symptom go away"?
   Restate the original goal and confirm the change still serves it.

2. Coupling and seams
   Did this change introduce any of the six coupling smells (god-object
   bag, reaching through internals, runtime type-switch, hidden temporal
   dependency, parameter creep, multi-module test)? Did this change reach
   across a module boundary that previously had a seam? Did this change
   add a parameter, branch, or field that another module now depends on
   by absence rather than by contract?

3. Shortcuts
   Where did the change skip a step that the architecture says should
   exist (input validation, schema check, idempotency, source-authority
   lookup, memory write, eval coverage, durable-state record)?

4. Hidden state
   Does the change rely on global state, environment variables, file
   system layout, time-of-day, or process startup order in ways that
   are not documented in the contract?

5. Failure modes
   What happens when each external dependency this change calls is
   slow, unavailable, returns a partial result, or returns garbage?
   Which of those are handled and which are silently re-raised as the
   fall-through path?

6. Tests and evals
   What new behavior is now true that no test exercises? What incident
   class is now reachable that no eval would catch?

7. Causal depth
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
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/reflection-and-planning.md" -->

---

### File: `docs/exception-taxonomy.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/exception-taxonomy.md" sha256="a7cd06584f134b521da2a02183f4f9fe22977ea7fbd3661a055c69c2343a96c3" bytes="5173" trailing_newline="true" -->
`````````` markdown
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
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/exception-taxonomy.md" -->

---

### File: `docs/a2a-contracts.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/a2a-contracts.md" sha256="950e9d057cac968230e8b3969e70cc0f3fcc1fc0712660c0279101f4fe951d31" bytes="6980" trailing_newline="true" -->
`````````` markdown
# Agent-to-agent message contracts

Version: 1.0
Audience: coding agents and architects working on multi-agent systems.

Cross-agent coordination covers ownership and integrator role. A2A contracts cover the messages themselves. The failure mode this prevents is folklore A2A: two agents work together because someone wrote a script that hardcoded what one produces and what the other expects. There is no schema, no version, no contract for partial messages, no idempotency rule, no replay rule, and no audit trail. The pair works until either side is edited.

---

## 1. Every A2A message type declares seven things

```text
1. Schema
   Typed shape of the message. Required fields, optional fields, types,
   units, allowed values. No payload field is "any."

2. Direction
   Request, reply, broadcast, signal, or event. Reply messages reference
   the request they answer. Broadcasts have no required reply.

3. Idempotency
   Is sending the same message twice safe? If yes, by what mechanism
   (idempotency key, content hash, dedup window). If no, what is the
   replay rule and what state in the receiver tracks "already handled."

4. Versioning
   How does the contract evolve? Field additions are usually safe; field
   removals or semantic changes require an explicit version bump and a
   migration plan. The receiver should know which versions it accepts.

5. Authority
   Which agent is authorized to send this message type. Which agent is
   authorized to act on it. Senders that do not have authority should be
   rejected at the receiver, not at the network.

6. Failure attribution
   How does the sender know the receiver failed? How does the receiver
   know the sender did not get the reply? Which class of failure (see
   docs/exception-taxonomy.md) does each side attribute to, and what
   does each side do next.

7. Audit
   Where is the message recorded? A2A traffic that does not appear in
   any audit surface is invisible to operators and to future agents
   debugging what happened.
```

---

## 2. Message schemas: minimum required structure

Every A2A message has at least these fields:

```python
@dataclass
class A2AMessage:
    # Identity
    message_id: str          # unique per send
    correlation_id: str      # ties request and reply
    causation_id: str | None # the message that caused this one

    # Routing
    from_agent: str
    to_agent: str
    type: str                # message type name (registry-keyed)
    version: str             # semver of the type's schema

    # Timing
    sent_at: datetime
    expires_at: datetime | None

    # Authority
    auth_token: str | None   # if cross-tenant or cross-trust-zone

    # Payload
    payload: dict            # typed per `type` and `version`
```

The payload type is keyed by the registered name and version. A receiver that does not recognize the type/version pair rejects the message; it does not "best-effort" decode it.

---

## 3. Idempotency patterns

### 3.1 Idempotency key

The sender supplies a key. The receiver records the key with the result. Repeated sends with the same key return the same result. This is the safest pattern when the receiver has durable state.

### 3.2 Content hash

The receiver hashes the payload and treats two messages with the same hash inside a dedup window as the same message. Useful when senders may re-send without remembering the previous send.

### 3.3 At-most-once via reservation

The receiver reserves a slot for the message_id, processes, and releases. A second send with the same message_id sees the reservation and returns the cached result.

### 3.4 At-least-once with idempotent handler

The handler itself is idempotent: the same input produces the same effect regardless of how many times it is invoked. Useful when the message bus cannot guarantee deduplication.

The handler's idempotency must be documented. "It happens to be idempotent because of how it's written today" is folklore.

---

## 4. Versioning

A2A contracts evolve. The rule is:

```text
safe (no version bump):
  - add an optional field
  - add a new enum value the receiver tolerates
  - add a new message type

unsafe (requires version bump and migration):
  - remove a field
  - rename a field
  - change a field's type or units
  - change a field's semantics
  - tighten a validation rule
```

The receiver advertises which versions it accepts. The sender chooses the highest mutually supported version. Migration plans cover both forward and backward compatibility windows.

---

## 5. Authority and trust

A2A authority answers "who is allowed to send this message type and who is allowed to act on it."

```text
- declared in a registry, not in agent prompts
- enforced at the receiver (network and bus may not be trustworthy)
- audited (every authority decision is logged)
- revocable (deprecation path for retired agents)
```

A receiver that processes messages without checking authority will be exploited the moment any agent in the system is compromised, mis-configured, or replaced by a sidecar with weaker invariants.

---

## 6. Failure attribution between agents

Both sides of an A2A pair need to know whose problem a failure is.

```text
sender's perspective                receiver's perspective
- request acknowledged but no reply  - received message but cannot act
   within timeout: receiver problem    on it: signal back unrecoverable
- request rejected at validation:    - received valid message but
   sender problem (bad payload)        downstream failed: signal back
- network error: bus problem,         (recoverable, degraded, or
   sender retries per recoverable      unrecoverable)
   class
```

Each failure attaches to one of the three exception classes (`docs/exception-taxonomy.md`) and triggers the corresponding behavior.

---

## 7. Audit surface

Every A2A message is recorded in at least one of:

```text
- structured event log (preferred for high volume)
- durable state record (preferred for state-changing messages)
- trace span (preferred for request/reply latency)
```

A2A traffic that does not appear in any audit surface is invisible. Invisible coordination is folklore by another name.

---

## 8. Common smells

```text
- payloads typed as `dict` or `any` with no schema
- "we'll add versioning when we need it"
- handlers that succeed differently on retry without saying so
- broadcasts with no recorded receivers
- replies that do not reference the request they answer
- authority decisions made in agent system prompts instead of a registry
```

---

## 9. Cross-references

- Architecture: section 5.17 (A2A message contracts), section 5.13 (Adoption states and cross-agent coordination)
- Anti-pattern: section 9.12 (Implicit A2A folklore)
- Field lesson: section 12.10 (Modularity is a runtime property), section 12.11 (Errors are classes, not surprises)
- Tool design (analogous contract for tool calls): `docs/tool-design.md`
- Cross-agent operating model: `docs/cross-agent-operating-model.md`
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/a2a-contracts.md" -->

---

### File: `docs/cost-aware-routing.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/cost-aware-routing.md" sha256="f699d090bbc0f2bceb41aafbef99a57182f5814fb1eab60370689762707d15f4" bytes="5318" trailing_newline="true" -->
`````````` markdown
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
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/cost-aware-routing.md" -->

---

### File: `docs/learning-loops.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/learning-loops.md" sha256="3cc2113b22c63666e76787eaef9664b962d8b437a761f539208d8c605da44d88" bytes="5311" trailing_newline="true" -->
`````````` markdown
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
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/learning-loops.md" -->

---

### File: `docs/task-prioritization.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/task-prioritization.md" sha256="6b7d5db57a2d032f0cf83e26044493d2b9fcc7651c9bb8ef448c07c217bbf6ec" bytes="5331" trailing_newline="true" -->
`````````` markdown
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
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/task-prioritization.md" -->

---

### File: `docs/QUICK_REFERENCE.md`

<!-- AGENTIC_BUNDLE_FILE_START path="docs/QUICK_REFERENCE.md" sha256="cae3501aa3bcd04020ad3a58f278272d1e016dfb768a465f243a4828bd7a0329" bytes="15038" trailing_newline="true" -->
`````````` markdown
# Quick reference for coding agents

Version: 1.0
Purpose: lossy distillation of the architecture pack. Rules only, no examples, no rationale. Use as cold-start companion to `AGENTS.md` and `CLAUDE.md`. Load the deep doc only for the topic you are actually touching.

If your task touches **schemas, permissions, idempotency, budgets, checkpoints, source authority, identity resolution, tool execution, human approval, traces, or evals** — that is harness work. Use deterministic code.

If your task touches **ambiguous intent, context selection, tool choice, memory retrieval, task decomposition, plan revision, recovery, or synthesis** — that is policy work. Use the model.

---

## Six doctrinal claims (non-negotiable)

1. **Deterministic harness, adaptive policy.** Determinism in the harness; ambiguous decisions in the model-owned policy layer with the right tools, memory, skills, and context.
2. **Source-of-truth role separation.** Truth, retrieval, recall, synthesis, sidecars, candidate signals, and external reports are different roles. Do not collapse them.
3. **Incidents become contracts.** Every production failure produces a harness change, an acceptance test, an eval/replay fixture, and an adoption rule.
4. **Causal depth.** Do not stop at the first true local explanation. Name the missing contract in memory, context, tool semantics, source authority, durable state, ownership, guardrails, or evals.
5. **Spend authority.** Paid API keys are gateway-owned exception paths, not ambient context. Attribution, budgets, rate limits, and tests that fail when direct key reads come back.
6. **Coupling cost asymmetry.** Declaring a seam now is linear; untangling later is super-linear in callers and editors. Bias forward: declare the seam now even when the local diff would be smaller without it.

---

## Component classification (declare one before coding)

`deterministic workflow` · `augmented LLM` · `agent loop` · `multi-agent / subagent` · `tool` · `tool registry` · `skill` · `memory subsystem` · `source lane / authority layer` · `identity resolution layer` · `context engine` · `durable execution layer` · `guardrail / human-review layer` · `cross-agent coordination layer` · `attention / notification policy` · `adoption-state change` · `eval / observability layer`

---

## Seam-declaration rule (every non-trivial change)

Before code:

1. **Modules touched** — what does this change read, write, or import?
2. **Interfaces depended on** — which contracts does this change consume?
3. **Interfaces defined or changed** — what does this introduce, modify, deprecate, or extend? What is public, what is intentionally private?
4. **Substitutability** — what changes if the implementation behind each interface is swapped (different store, model, transport, provider)? Many things in many places means the seam is wrong.

Six coupling smells (any of these = creating coupling):

- **God-object state bag** — function takes a `context`/`state`/`request` bag and reads ≥4 fields.
- **Reaching through internals** — `module.B._private` access from outside B.
- **Runtime type-switch on opaque payload** — `if event.kind == ...` chain growing branch by branch.
- **Hidden temporal dependency** — A must be called before B, encoded only in caller order.
- **"Just one more parameter" creep** — function accumulates 6+ optional parameters added by N agents.
- **Multi-module test instantiation** — unit test imports 4 modules to construct the system under test.

Detail: `docs/modularity-and-seams.md`. Anti-pattern 9.9. Field lesson 12.10.

---

## Reflection checklist (before declaring done)

1. **Goal drift** — original goal restated; change still serves it; no quiet redefinition to "make the test pass."
2. **Coupling and seams** — none of the six smells; no boundary crossed; no parameter/branch/field that other modules now depend on by absence.
3. **Shortcuts** — no skipped step (validation, schema, idempotency, source-authority lookup, memory write, eval coverage, durable-state record).
4. **Hidden state** — no undocumented dependency on globals, env vars, file layout, time, process startup order.
5. **Failure modes** — every external dep has stated behavior under slow/unavailable/partial/garbage; nothing silently re-raises.
6. **Tests and evals** — no new behavior is true that no test exercises; no incident class reachable that no eval catches.
7. **Causal depth** — for fixes: proximate cause + ultimate contract both named; if only proximate addressed, remaining incident class named as gap.

Hidden gaps are worse than known gaps.

Detail: `docs/reflection-and-planning.md`. Anti-pattern 9.10.

---

## Plan as artifact (before action)

Goal · Acceptance proof · Component classification · Seam declaration · Failure-mode budget · Routing decision · Out of scope.

Goal-drift checks: before each tool call, before declaring done, inside reflection. If goal genuinely changes mid-task, change the plan explicitly.

Detail: `docs/reflection-and-planning.md`.

---

## Three exception classes (every retry/fallback/degradation attaches to one)

- **Recoverable** — retry per policy; surface only on budget exhaustion; do not poison durable state.
- **Degraded** — produce partial result; mark missing pieces; surface a structured signal (never silent); record what would have been there.
- **Unrecoverable** — stop; do not retry; do not degrade; write structured failure record; alert per attention policy.

A retry without a class is a guess. Silent degradation is a bug. Silent paid spillover is a bug. Silent retry past budget is a bug.

Detail: `docs/exception-taxonomy.md`. Anti-pattern 9.11. Field lesson 12.11.

---

## A2A message contracts (every agent-to-agent message type)

Schema · Direction (request/reply/broadcast/signal/event) · Idempotency (key, hash, dedup window, or documented at-least-once handler) · Versioning (additive vs migration) · Authority (sender + receiver, registry-enforced) · Failure attribution (per exception class, both sides) · Audit surface.

Payloads typed as `dict`/`any` are folklore. A2A traffic with no audit surface is invisible.

Detail: `docs/a2a-contracts.md`. Anti-pattern 9.12.

---

## Cost-aware routing (every paid call attributable, every spillover doctrinal)

Routing inputs: task difficulty · evidence sensitivity · consequence · budget state · lane health · explicit overrides.

Lanes: default (cheap, broad) · escalated (expensive, capable) · degraded (cheapest or stop).

Spillover policy is part of routing, not emergent. Each spillover path attaches to: exception class · destination lane · budget impact · audit record.

Three failure modes: silent escalation · silent fallback · wrong-axis routing. All recover by recording the doctrine decision and auditing the spend.

Detail: `docs/cost-aware-routing.md`. Field lesson 12.12.

---

## Learning loops (every finding has a destination)

- **Within-task**: reflection (above).
- **Across-task**: skill promotion. Pattern works across N tasks → drafted skill (eval, when-to-use) → canonical (owner, rollback). Promotion follows adoption state: `reference_only` → `shadow_mode` → `candidate_write` → `write_enabled` → `canonical` → `deprecated`.
- **System-level**: external critique on slower cadence. Findings → candidate skill / contract change / missing eval / candidate signal / deprecation.

A finding without a destination is a smell. A loop nobody acts on is a journal, not learning.

Detail: `docs/learning-loops.md`. Anti-pattern 9.13. Field lesson 12.13.

---

## Task prioritization (every queued task declares five inputs)

Urgency (none/soft/hard/irreversible) · importance (blocks other lanes?) · preemptability · cost · staleness (hard window / soft decay / appreciation / none).

Queue rule: preemption-immune tasks run to completion · among ready tasks prefer importance, then urgency, then cheaper · overrides recorded with rationale · saturation surfaces as signal, never silent drops.

The harness owns the rule, not the agent.

Detail: `docs/task-prioritization.md`. Anti-pattern 9.14. Field lesson 12.14.

---

## Anti-patterns (never these)

- **9.1 Regex pretending to be intelligence** — ambiguous routing in if/elif/regex.
- **9.2 Giant prompt as architecture** — every rule, memory, tool, transcript stuffed into the system prompt.
- **9.3 Memory as append-only notes** — write summaries to a file with no schema or promotion path.
- **9.4 Tools without semantic affordances** — `run(query: string) → result`.
- **9.5 Multi-agent theater** — committee of agents per task instead of single-agent-first.
- **9.6 Source-of-truth collapse** — wiki, vector index, source DB, sidecar, chat all treated as one memory.
- **9.7 Noisy-lane contamination** — brainstorming or speculation promoted into project truth without review.
- **9.8 Accidental production promotion** — sidecar passes one demo and becomes canonical.
- **9.9 Convenient coupling** — reaching across module boundaries because "it is right there."
- **9.10 Skipping reflection** — declaring done without the §5.14 checklist.
- **9.11 Unclassified errors** — bare except, silent None, retry without class.
- **9.12 Implicit A2A folklore** — pair of agents that work via a hardcoded script with no contract.
- **9.13 No learning loop** — recurring findings with no destination.
- **9.14 FCFS task scheduling** — first-come-first-served by accident, no declared priority rule.

---
- **Category index in bootstrap.** Loading a multi-section reference doc (one section per lane/integration/tool) as bootstrap. Bootstrap pays the cost on every turn and the runtime silently truncates. Split into per-member sub-docs; replace the original with a thin index; let the retriever surface the right sub-doc by query. Detail: `docs/context-engineering.md` and `docs/agentic-coding-for-agentic-systems.md` § 5.2.1.

## Field lessons (operational consequences)

- **12.1 Define done as system behavior** — manual one-off proof is debugging evidence, not completion.
- **12.2 Incidents become contracts, not folklore** — every incident becomes a harness layer, an acceptance test, and an eval.
- **12.3 Proximate causes are not ultimate causes** — go deep enough to name the missing contract.
- **12.4 Backpressure and cost are harness responsibilities** — silent paid fallback is unreviewed side effect.
- **12.5 Claims must reconcile with state** — if claim and state disagree, both are evidence; reconcile, do not arbitrarily prefer.
- **12.6 Keep thesis, current state, and truth separate** — a roadmap is not truth and a synthesis is not truth.
- **12.7 Promote through adoption states** — sidecars, models, workflows promoted via shadow → candidate → canonical with evals, health, rollback, owner.
- **12.8 Human attention is a scarce system resource** — quiet by default; loud only when situation deserves it.
- **12.9 The coding agent is part of the operating system** — its edits, logs, claims, summaries are operating-system memory.
- **12.10 Modularity is a runtime property** — parallel collisions are seam problems, not coordination problems.
- **12.11 Errors are classes, not surprises** — every failure attaches to recoverable / degraded / unrecoverable.
- **12.12 Cost asymmetry is a routing input, not an afterthought** — cost is rarely a runtime emergency, almost always doctrine drift.
- **12.13 Systems that don't learn get worse** — stability is the default state of contracts; improvement is not.
- **12.14 Priority is not optional** — FCFS is the default that emerges when no one declares the rule.

---

## Dependency awareness (every non-trivial change)

Six patterns, ordered cheapest to strongest — pick by failure mode, not aesthetic:

1. **Seam declaration before code** — universal floor. Modules touched · interfaces depended on · interfaces defined or changed · substitutability.
2. **Source ledger on context assembly** — each context item carries source + reason + freshness.
3. **Reverse-lookup retriever** — given a path/symbol you're about to change, what already depends on it? Most underused; usually one script.
4. **Adoption-state tracking** — per-consumer state (legacy / migrating / migrated / deprecated). Forces migrations out of one agent's head into the schema.
5. **Static analysis in CI** — broken-link / stale-reference checks for shared paths, links, names.
6. **Replay tests** — record a real session, re-run after refactor; only for high-blast-radius components.

Anti-pattern: **blind local edit** — agent edits a file as if it were standalone, ships, discovers downstream breakage later. Fix with the cheapest pattern that would have caught the specific failure shape.

Detail: `docs/agentic-coding-for-agentic-systems.md` § 5.21. Adjacent: `docs/modularity-and-seams.md` (seams), `docs/context-engineering.md` (source ledger), `docs/cross-agent-operating-model.md` (adoption state).

---

## Pointers to deep docs

For the topic you are actually touching:

| Topic | Doc |
|---|---|
| Tools | `docs/tool-design.md` |
| Memory | `docs/memory-architecture.md` |
| Context engineering | `docs/context-engineering.md` |
| Skills | `docs/skills.md` |
| Subagents | `docs/subagents.md` |
| Durable execution | `docs/durable-execution.md` |
| Evals | `docs/evals.md` |
| Source authority and truth lanes | `docs/source-authority-and-truth-lanes.md` |
| Cross-agent coordination | `docs/cross-agent-operating-model.md` |
| Modularity and seams | `docs/modularity-and-seams.md` |
| Reflection and planning | `docs/reflection-and-planning.md` |
| Exception taxonomy | `docs/exception-taxonomy.md` |
| A2A contracts | `docs/a2a-contracts.md` |
| Cost-aware routing | `docs/cost-aware-routing.md` |
| Learning loops | `docs/learning-loops.md` |
| Task prioritization | `docs/task-prioritization.md` |

For the full architecture, the executive thesis, all anti-patterns with worked examples, all field lessons with rationale, the canonical coding-agent prompt, the first-engineering-tasks ordering, and the multifile rebuild scaffolding: `docs/agentic-coding-for-agentic-systems.md` and `docs/agentic-systems-engineering.md`.

For the full single-file source: `AGENTIC_ARCHITECTURE.md` (top-level).

---

## Final summary requirements

A non-trivial change ends with the agent stating: component classification · model-owned vs harness responsibilities · tools / skills / memory / source authority / identity / context behavior · guardrails and approvals · cross-agent ownership · attention behavior · backpressure/budget/fallback · adoption state and rollback · causal ladder for fixes · acceptance proof and gaps · plan and goal · seam declaration · exception classes · A2A contract changes · routing and cost · prioritization inputs · learning destination · reflection checklist results.

Hidden gaps are worse than known gaps. State the gaps explicitly.
``````````
<!-- AGENTIC_BUNDLE_FILE_END path="docs/QUICK_REFERENCE.md" -->
