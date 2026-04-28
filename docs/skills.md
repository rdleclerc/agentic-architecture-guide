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
