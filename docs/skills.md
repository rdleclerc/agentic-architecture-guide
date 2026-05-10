# Skills for Agentic Systems

A skill is reusable procedural knowledge for a class of agentic-system work. It usually contains `SKILL.md` plus optional examples, scripts, templates, fixtures, references, or tests.

Use a skill when the task is a repeatable way of doing work, not merely a one-off branch or another long root-prompt instruction.

## Canonical skill source

The canonical, agent-neutral skill source is:

```text
skills/<skill-name>/SKILL.md
```

Adapter-specific directories are compatibility surfaces, not sources of truth:

```text
.claude/skills/<skill-name>/SKILL.md -> ../../../skills/<skill-name>/SKILL.md
.codex/skills/<skill-name>/SKILL.md  -> ../../../skills/<skill-name>/SKILL.md
```

Edit `skills/<skill-name>/SKILL.md` first. Refresh adapter symlinks or generated copies from that canonical source. Do not make one-off edits inside `.claude/skills/` or `.codex/skills/`; doing so creates tool-specific drift.

If an environment cannot preserve symlinks, adapter copies may be generated, but they remain derived artifacts and must be validated against the canonical `skills/` tree.

## Skill package structure

```text
skills/<skill-name>/
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
- when not to use, when ambiguity is likely
- prerequisites
- procedure
- output contract
- examples or misuse examples, when useful
- eval or review checklist

Keep root instructions short. Put detailed procedures in skills so they load only when relevant. Keep each `SKILL.md` concise enough for agent context; move bulky examples, fixtures, and reference material into optional subdirectories.

## Initial skills in this pack

- `design-agent-tool`
- `design-agent-memory`
- `design-source-lane`
- `design-context-engine`
- `build-agent-eval`
- `review-agentic-architecture`

## Skills for operating systems

Skills should package procedures that prevent architectural drift: designing source lanes, reviewing identity resolution, creating eval cases, writing source-authority policies, and auditing adoption-state changes.

Prefer a skill when the repo needs a repeatable way to do a class of work. Prefer a deterministic script or eval when consistency matters more than judgment. Prefer deleting or simplifying the process when the skill would only preserve unnecessary complexity.
