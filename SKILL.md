---
name: heartbeat
description: >
  Use when the user asks to design, create, review, or modify heartbeats,
  recurring automations, scheduled tasks, cron-like wakeups, monitors,
  reminders, trigger rules, or agent auto-run loops. Treat heartbeat as Agent
  trigger design first: define the agent role, professional positioning,
  authority, evidence standard, context, stop/resume policy, and only then
  choose schedule/event/state-change mechanics. Trigger on Chinese terms such
  as 心跳、定时任务、自动化、定期推进、触发器、trigger、唤醒、监工、循环、暂停、恢复、改频、重建.
---

# Heartbeat

`heartbeat` designs Agent triggers. A timer is only one trigger source.

Use this skill when the user wants to create or change a heartbeat, recurring automation, scheduled task, monitor, reminder, cron job, or long-running Agent loop. The default assumption is:

> Design the Agent first; then decide when and how it wakes.

## Coordination

- `MyWay` or another companion router can identify whether the user really means trigger / Agent design rather than a simple timer.
- `files-driven` or another governance layer should own project truth, write authority, gates, evidence, recovery, and whether trigger outputs may enter project facts.
- `skills-master` or another skill lifecycle process should own packaging, live asset routing, and distribution.
- `gstack` or another expert-review method is useful when professional viewpoints or adversarial questioning are needed before defining the Agent role.
- `Archon` or another workflow engine is useful when the trigger becomes a multi-stage workflow / harness contract with DAG nodes, loop gates, artifacts, isolation, adapters, recovery, and audit.

If the user explicitly asks to create, update, delete, list, or inspect a host automation, use the host automation tool when available. Do not replace a real automation operation with prose.

For multi-Agent heartbeats, avoid putting the full governance model into every automation prompt. Prefer:

```text
shared files-driven control contract + thin role prompts
```

The shared contract states who commands whom, which context each Agent must inherit, what output package each Agent emits, and when a trigger may pause, resume, change frequency, or escalate. Each heartbeat prompt should mostly point to that contract and state the Agent's local role.

## Core Model

Think in this order:

```text
trigger -> target Agent -> context payload -> authority -> evidence -> output -> next trigger policy
```

For repeatable Agent work, the practical object is often not a prompt but a harness:

```text
trigger -> workflow run -> node harness -> artifact chain -> authority gate -> resume / rewrite / stop
```

Agent management is not HR for models. Foundation-model ability is often similar across Agents; the meaningful differences come from harness design: context, tools, skills, hooks, model choice, sandbox, artifact contract, trigger source, evidence gate, adapter, and recovery policy.

Default philosophy:

```text
capability plane: mostly flat
control plane: explicitly layered
```

Do not create hierarchy because one Agent is "smarter". Create hierarchy because one harness owns planning, one owns execution, one owns projection, one owns professional challenge, and one owns acceptance / recovery.

Trigger sources:

- `schedule`: fixed cadence such as every 20 minutes or hourly.
- `event`: new message, CI result, file change, issue, PR, job completion.
- `state_change`: project status changed, blocker opened, gate passed, deadline entered.
- `human`: user request, owner verdict, explicit resume / pause command.
- `recovery`: missed run, crashed process, deleted automation, stale session, lock expiry.

Trigger actions:

- `loop`: run again at the next cadence.
- `backoff`: slow down after no change or repeated no-op.
- `pause`: stop future runs without deleting the trigger.
- `resume`: restart after prompt, context, or authority has been corrected.
- `rewrite`: modify prompt, payload, target, cadence, or handoff route.
- `split`: separate one broad trigger into specialized Agents.
- `escalate`: route to owner, project lead, professional reviewer, or human.

## Agent Role Card

Before writing a cron expression or automation prompt, define:

```yaml
agent:
  task_role: developer | dashboard | supervisor | validator | reminder | monitor
  method_role: observer | hypothesizer | challenger | executor | adjudicator | projector
  professional_positioning:
    domain: product | engineering | runtime_reliability | security | clinical_research | data_governance | release
    evidence_standard: what counts as proof for this profession
    blindspot_watch: what this profession is expected to catch
  project_scope: capability_scope | project_scope | runtime_scope
  reads: []
  writes: []
  forbidden_writes: []
  authority:
    can_do: []
    must_escalate: []
  output_contract: HEARTBEAT_OK | DONT_NOTIFY | status_card | decision_packet | patch | verification_report
```

Professional positioning matters most on concrete problems. A clinical research Agent, runtime reliability Agent, product Agent, security Agent, and release Agent should not use the same evidence standard.

## Trigger Contract

Define the trigger as a small contract:

```yaml
trigger:
  id:
  target_agent:
  source: schedule | event | state_change | human | recovery
  cadence:
  workflow_ref:
  node_ref:
  target_thread:
  source_threads: []
  payload:
    truth_refs: []
    artifact_refs: []
    last_run_state:
    resume_token:
  batch_mode: single_step | work_batch | deep_push
  isolation:
    worktree: optional | required | forbidden
    sandbox:
  permissions:
    observe: true
    write_draft: false
    write_truth: false
    pause_self: true
    modify_others: false
    modify_subordinate_schedule: false
    delete_self: false
  next_policy:
    if_no_change: suppress_or_backoff
    if_progress: continue
    if_blocked: route_to_owner_agent
    if_repeated_noise: pause
    if_stage_changed: rewrite_prompt_or_schedule
```

Default deletion rule:

- Worker / Dashboard / monitor Agents must not delete their own heartbeat.
- They may pause themselves when stop conditions are met.
- A supervisor or project-owner Agent may modify subordinate prompt, schedule, and status when it emits a `harness_action` with reason, scope, expected effect, and restore / recheck condition.
- Deletion is reserved for an explicit human/admin maintenance action unless the current platform has a stricter contract.

Frequency is a scheduling decision, not a project-truth decision. A Dashboard or projection trigger may be reduced to hourly when the visible state is unlikely to change; a development or owner-verdict trigger may stay high-frequency during fast-changing or blocked phases. Frequency does not define work depth: a 3-minute wakeup can still request a substantial `work_batch`.

## Workflow-Backed Triggers

Use a workflow-backed trigger when the work has phases, gates, repeated loops, multiple reviewers, recovery needs, or must be reusable across projects. Archon is the strongest current reference pattern for this: encode the development process as a workflow, let AI fill in intelligence at selected nodes, and keep phases, gates, artifacts, and isolation deterministic.

Translate heartbeat design into workflow objects:

| Heartbeat concept | Workflow-backed shape |
| --- | --- |
| `target_agent` | workflow node with a scoped prompt / command / deterministic script |
| `trigger source` | workflow invocation, resume condition, event adapter, or schedule |
| `loop` | bounded loop with completion signal, max iterations, and preferably deterministic check |
| `human / owner gate` | approval node or owner-verdict gate |
| `stop condition` | intentional cancel / pause with reason, not silent failure |
| `evidence` | artifact chain, structured output, test log, validator result, or review packet |
| `multi-Agent debate` | parallel review nodes followed by synthesis and owner verdict |
| `context policy` | fresh context for long loops, shared context only when memory of attempts matters |
| `isolation` | worktree / sandbox / per-node tool permissions |
| `adapter` | CLI, Web, IM, GitHub, or webhook ingress; never project truth by itself |

Design rules:

1. Prefer deterministic nodes for validation, tests, file checks, branch checks, and cancel conditions.
2. Use AI nodes where judgment is needed: planning, implementation, review, synthesis, professional challenge, and explanation.
3. Long loops should read and write progress from files or artifacts. Do not rely on conversational memory as the only state.
4. A fresh-context loop must carry enough state through files, upstream node output, or artifact refs to continue safely.
5. Every loop needs a hard bound and a stop reason. A completion tag alone is weaker than a deterministic gate such as tests, validators, or schema checks.
6. Parallel reviewers do not decide by vote. They produce findings; a synthesis / owner-verdict node decides scope, evidence sufficiency, and next action.
7. Platform adapters trigger or report workflows. They do not own acceptance, truth, or write authority.

## Supervisor Plan Control

When an Agent is responsible for other Agents, it must be designed as a planner and dispatcher, not just a reviewer. Require a `plan_control` package before it issues directives:

```yaml
plan_control:
  lane_queue: []
  dependency_map: []
  current_focus:
  batch_policy: single_step | work_batch | deep_push
  gate_map: []
  evidence_debt: []
  tool_routing: []
  dashboard_policy:
```

Then the supervisor may emit:

- `agent_directive`: tells a frontline Agent what to work on next.
- `owner_verdict`: signs, rejects, defers, or escalates when evidence is sufficient.
- `harness_action`: changes subordinate trigger prompt, schedule, status, batch depth, or recovery path.

Stop rule: if a supervisor only comments on subordinate work but does not maintain `plan_control`, it is drifting into a passive reviewer role.

## Design Workflow

1. Decide whether this is a simple reminder or an Agent trigger.
2. If it is an Agent trigger, write the Agent role card first.
3. Choose trigger source: schedule, event, state change, human, or recovery.
4. Define context payload and memory boundary. Background trigger content must not silently become long-term memory or project truth.
5. Define authority and forbidden actions, especially write rights, pause/resume rights, and delete rights.
6. Define output contract. No-op runs should be suppressible.
7. For multi-Agent systems, define the shared control contract and keep prompts thin.
8. If the trigger has phases, retries, or reusable gates, lower it into a workflow-backed trigger contract.
9. Define evidence standard and escalation path.
10. Define verification: persisted config, target thread or workflow run, latest run, artifact chain, state transition, and rollback/resume path.

## Output Shapes

For design-only requests, return:

1. `agent_role_card`
2. `trigger_contract`
3. `authority_and_stop_rules`
4. `shared_control_contract` when multiple Agents collaborate
5. `workflow_backed_trigger_contract` when a DAG / loop / approval / artifact chain is needed
6. `activation_or_verification_plan`

For review requests, return:

1. `drift`
2. `missing_authority_or_evidence`
3. `overdesign`
4. `recommended_patch`

For implementation requests, edit the real trigger or automation source, then verify persistence and report the exact object changed.

## Common Patterns

Three-Agent governance:

- Frontline Agent: closest to the work, submits `frontline_default` and `owner_verdict_dossier`.
- Project Owner Agent: maintains `plan_control`, issues `agent_directive`, reviews evidence, signs / rejects / defers within authorization, and emits `harness_action` to adjust subordinate triggers.
- Dashboard Agent: reads project truth, frontline reports, `plan_control`, and owner verdicts; projects status for humans, never becomes truth source or signer.

Light / heavy loop:

- Light loop checks whether anything changed and returns `HEARTBEAT_OK` / `DONT_NOTIFY`.
- `work_batch` loop does meaningful development, landing, evidence construction, self-review, reflection, and handoff in one run.
- `deep_push` is reserved for explicit supervisor or human direction when the lane is clear enough for a longer push.
- Heavy review runs only on state change, blocker, new evidence, failed gate, repeated short reports, or explicit human trigger.

Progress heartbeat:

- Include `run_id`, `attempt`, `last_success_ref`, `current_step`, `blocker_ref`, and `resume_token` so retries do not repeat completed side effects.

Workflow-backed implementation heartbeat:

- Use schedule / event / human request only to start or resume a workflow run.
- Keep per-node prompts thin and scoped; put shared rules in the workflow contract and project control contract.
- Persist progress in an artifact directory or state file so fresh-context nodes can pick up the next unit of work.
- Use deterministic validation and cancel nodes to stop wasted downstream work when a precondition fails.
- Treat workflow UI / IM / GitHub comments as projections unless `files-driven` accepts their artifacts into project truth.

## Anti-Patterns

- Writing a cron schedule before defining the Agent role.
- Treating heartbeat as infinite autonomous development.
- Treating heartbeat frequency as a cap on single-run work depth.
- Making the supervisor a passive reviewer instead of the owner of `plan_control`.
- Using one broad prompt for every Agent.
- Duplicating the full governance model in every prompt instead of using a shared control contract plus thin role prompts.
- Letting no-op heartbeats pollute the main transcript or long-term memory.
- Letting Dashboard projection become project truth.
- Letting a subordinate Agent delete its own trigger.
- Treating missing readiness evidence as liveness failure.
- Treating professional review as generic "quality check" without naming the domain and evidence standard.
- Treating an external workflow README or dashboard as project authority before `files-driven` accepts the contract and artifacts.
- Using an unbounded loop or AI-only completion signal where a deterministic validator, test, schema, or cancel gate is available.
