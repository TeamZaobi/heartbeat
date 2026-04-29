# Heartbeat Skill

`heartbeat` is a portable Agent skill for designing heartbeats, scheduled tasks, recurring automations, monitors, and long-running Agent loops.

The central idea is simple:

```text
Design the Agent first; then decide when and how it wakes.
```

A heartbeat is a trigger. A timer is only one trigger source. Good heartbeat design defines the Agent role, professional positioning, authority, evidence standard, context payload, stop/resume policy, artifact chain, and recovery path before choosing cron, schedule, webhook, state change, or human wakeup mechanics.

## What This Skill Adds

- Agent role cards before cron expressions
- Trigger contracts with authority, evidence, and next-run policy
- Workflow-backed trigger design for DAGs, loops, approvals, artifacts, isolation, adapters, and recovery
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
- workflow-backed Agent orchestration

Chinese trigger terms include: `心跳`, `定时任务`, `自动化`, `定期推进`, `触发器`, `trigger`, `唤醒`, `监工`, `循环`, `暂停`, `恢复`, `改频`, `重建`.

## Installation

This repository is a skill package. The root `SKILL.md` is the skill entrypoint.

For a local skill root, clone or copy this repository as a folder named `heartbeat`:

```bash
git clone https://github.com/TeamZaobi/heartbeat.git ~/.agents/skills/heartbeat
```

For Claude Code-style project skills, place it under:

```text
.claude/skills/heartbeat/
```

For any other Agent host, install it wherever that host expects a skill directory containing `SKILL.md`.

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
trigger -> target Agent -> context payload -> authority -> evidence -> output -> next trigger policy
```

For repeatable Agent work, lower it into a harness:

```text
trigger -> workflow run -> node harness -> artifact chain -> authority gate -> resume / rewrite / stop
```

## Examples

- [Agent role card](examples/agent-role-card.yaml)
- [Trigger contract](examples/trigger-contract.yaml)
- [Workflow-backed trigger](examples/workflow-backed-trigger.yaml)

## License

MIT
