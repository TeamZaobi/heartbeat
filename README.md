# Heartbeat Skill

`heartbeat` is a portable Agent skill for designing heartbeats, scheduled tasks, recurring automations, monitors, and long-running Agent loops.

The central idea is simple:

```text
Prove the beneficiary entropy reduction first; design the Agent second; decide when and how it wakes last.
```

A heartbeat is a trigger. A timer is only one trigger source. Good heartbeat design first checks whether any recurring trigger is needed, then defines the beneficiary pain, entropy reduction target, Agent role, professional positioning, authority, evidence standard, context payload, stop/resume policy, artifact chain, and recovery path before choosing cron, schedule, webhook, state change, or human wakeup mechanics.

## What This Skill Adds

- Occam preflight before creating or expanding loops
- Beneficiary entropy reduction as the reason a heartbeat exists
- Causal-chain design: comparison advantage or survival pressure -> pain -> trigger need -> harness architecture -> wakeup mechanics
- Agent role cards before cron expressions
- Trigger contracts with authority, evidence, and next-run policy
- Workflow-backed trigger design for DAGs, loops, approvals, artifacts, isolation, adapters, and recovery
- Outcome-oriented harness design: success criteria, visible and foundation work, guardrails, feedback loops, and beneficiary validation
- Continuous-thread light-loop design: inherit active thread context, avoid cold-start rereads, keep prompts thin, and trigger heavy audit only on real change
- Multi-Agent governance patterns for frontline Agents, project-owner Agents, dashboard/projection Agents, validators, and reviewers
- Stop rules for pause, resume, backoff, prompt rewrite, escalation, and deletion authority
- Harness topology guidance: model capability can be mostly flat, while control planes should be explicitly layered

## When To Use It

Use this skill when a user asks to design, create, review, or modify:

- heartbeats
- recurring automations
- scheduled tasks
- cron-like wakeups
- monitors
- reminders that involve Agent work
- trigger rules
- Agent auto-run loops
- supervisor / project-owner / dashboard Agent cycles
- continuous-thread heartbeats that should continue the last work batch instead of replaying history
- workflow-backed Agent orchestration

Chinese trigger terms include: `心跳`, `定时任务`, `自动化`, `定期推进`, `触发器`, `trigger`, `唤醒`, `监工`, `循环`, `暂停`, `恢复`, `改频`, `重建`.

## Installation

This repository is a skill package. The root `SKILL.md` is the skill entrypoint.

For OpenAI Codex-style user skills, clone this repository as the canonical local source:

```bash
git clone https://github.com/TeamZaobi/heartbeat.git ~/.agents/skills/heartbeat
```

Then check how it is exposed to supported tools:

```bash
python3 ~/.agents/skills/heartbeat/scripts/link_skill.py ~/.agents/skills/heartbeat --status
```

Link the same source into Claude Code and Antigravity user-level discovery paths:

```bash
python3 ~/.agents/skills/heartbeat/scripts/link_skill.py ~/.agents/skills/heartbeat
```

This keeps one editable source and creates symlinks where the host expects them.

## Multi-Tool Support

`heartbeat` is a native skill directory: one folder with one `SKILL.md`. Do not maintain separate editable copies for different hosts. Use links or generated projections.

Supported default user paths:

| Host | User-level path | Mode |
| --- | --- | --- |
| OpenAI Codex | `~/.agents/skills/heartbeat` | native source |
| Claude Code | `~/.claude/skills/heartbeat` | symlink to source |
| Google Antigravity | `~/.gemini/antigravity/skills/heartbeat` | symlink to source |

Project-level paths:

| Host | Project-level path | Mode |
| --- | --- | --- |
| OpenAI Codex | `<project>/.agents/skills/heartbeat` | native project source |
| Claude Code | `<project>/.claude/skills/heartbeat` | symlink to project source |
| Google Antigravity | `<project>/.agents/skills/heartbeat` | native project source |

For project-local setup, keep the canonical project copy under `.agents/skills/heartbeat`, then link Claude Code to it:

```bash
git clone https://github.com/TeamZaobi/heartbeat.git .agents/skills/heartbeat
python3 .agents/skills/heartbeat/scripts/link_skill.py .agents/skills/heartbeat --project-root .
python3 .agents/skills/heartbeat/scripts/link_skill.py .agents/skills/heartbeat --project-root . --status
```

If a host caches skill discovery, open a fresh session after linking.

See [multi-tool adaptation](references/multi-tool-adaptation.md) for the source-of-truth model, refresh rules, and smoke checks.

## Optional Integrations

The skill is standalone. It can also cooperate with adjacent method layers:

- A companion router such as `MyWay` can decide whether the user means a simple reminder or Agent trigger design.
- A governance layer such as `files-driven` can decide whether trigger output enters project truth, write authority, workflow contracts, recovery, or audit.
- A skill lifecycle layer such as `skills-master` can handle packaging, live asset routing, upstream sync, and distribution.
- A workflow engine such as `Archon` can be used when the trigger should compile into a DAG / loop / approval / artifact-backed workflow.
- An expert-review method such as `gstack` can be used when professional viewpoints or adversarial questioning are needed.

If these tools are not installed, apply the same responsibilities manually in your host environment.

## Core Model

```text
beneficiary pain -> entropy reduction target -> trigger need -> target Agent -> context mode -> authority -> evidence -> output -> next trigger policy
```

For repeatable Agent work, lower it into a harness:

```text
trigger -> workflow run -> node harness -> artifact chain -> authority gate -> resume / rewrite / stop
```

## Examples

- [Agent role card](examples/agent-role-card.yaml)
- [Trigger contract](examples/trigger-contract.yaml)
- [Outcome contract](examples/outcome-contract.yaml)
- [Workflow-backed trigger](examples/workflow-backed-trigger.yaml)

## Method References

- [Outcome-oriented harness](references/outcome-oriented-harness.md)
- [Continuous-thread light loops](references/continuous-thread-light-loops.md)
- [Multi-tool adaptation](references/multi-tool-adaptation.md)

## License

MIT
