---
name: heartbeat
description: >
  Use when the user asks to design, create, review, or modify heartbeats,
  recurring automations, scheduled tasks, cron-like wakeups, monitors,
  reminders, trigger rules, or agent auto-run loops. Treat heartbeat as Agent
  trigger design first: define the agent role, professional positioning,
  authority, evidence standard, context, stop/resume policy, and only then
  choose schedule/event/state-change mechanics. Also use for continuous-thread
  light loops, supervisor delegation, prompt slimming, trigger rewrite, and
  anti-bureaucratic heartbeat control. Apply Occam and entropy reduction:
  do not create or expand a loop unless it reduces beneficiary confusion,
  waiting, forgotten work, drift, verification burden, or recovery risk.
  Trigger on Chinese terms such as
  心跳、定时任务、自动化、定期推进、触发器、trigger、唤醒、监工、循环、暂停、恢复、改频、重建.
---

# Heartbeat

`heartbeat` designs Agent triggers. A timer is only one trigger source.

Use this skill when the user wants to create or change a heartbeat, recurring automation, scheduled task, monitor, reminder, cron job, or long-running Agent loop. The default assumption is:

> Design the Agent first; then decide when and how it wakes.

## Governing Principles

### Occam Preflight

Before designing or modifying a heartbeat, first ask whether the heartbeat should exist at all.
Prefer the least active mechanism that still reduces entropy for the beneficiary:

1. no recurring trigger; finish the work now
2. simple host reminder; no Agent loop
3. event or state-change trigger; no polling cadence
4. continuous-thread light loop; no cold-start rereads
5. one thin Agent prompt plus existing control contract
6. workflow-backed trigger only when phases, gates, artifacts, recovery, or reuse truly require it

Do not add a heartbeat, supervisor, dashboard, auditor, workflow, control file, or prompt rewrite just because progress is uncertain.
Add one only when it removes a specific uncertainty, wait state, forgotten handoff, verification gap, drift risk, or recovery risk.

### Beneficiary Entropy Reduction

Every heartbeat must name the beneficiary and the entropy it reduces.
The useful question is not "how often should this wake up?" but:

- Who is less confused, less blocked, less exposed to drift, or less burdened after this trigger runs?
- What context, decision, evidence, or recovery path becomes clearer?
- What noise, repeated check, unnecessary reread, or avoidable status output disappears?

If the loop mainly creates transcript volume, status theater, repeated request packets, duplicated governance text, or extra control objects,
pause or downgrade it until the entropy reduction is explicit.

### Causal Chain For Trigger Demand

Use this causal chain before choosing the Agent role or cadence:

```text
comparison advantage or survival pressure -> pain -> trigger need -> harness architecture -> wakeup mechanics
```

Here, comparison advantage means a beneficiary needs to show, preserve, or improve an advantage among peers.
Survival pressure means a beneficiary needs to stay safe, reliable, recoverable, compliant, or operational under environmental pressure.
The pain is the concrete friction created when that drive is blocked.
The trigger need is the smallest recurring or event-driven intervention that can reduce that pain.
Only after that should the harness architecture and wakeup mechanics be chosen.

## Coordination

- `MyWay` or another companion router can identify whether the user really means trigger / Agent design rather than a simple timer.
- `files-driven` or another governance layer should own project truth, write authority, gates, evidence, recovery, and whether trigger outputs may enter project facts.
- `skills-master` or another skill lifecycle process should own packaging, live asset routing, and distribution.
- `gstack` or another expert-review method is useful when professional viewpoints or adversarial questioning are needed before defining the Agent role.
- `Archon` or another workflow engine is useful when the trigger becomes a multi-stage workflow / harness contract with DAG nodes, loop gates, artifacts, isolation, adapters, recovery, and audit.

If the user explicitly asks to create, update, delete, list, or inspect a host automation, use the host automation tool when available. Do not replace a real automation operation with prose.

For multi-Agent heartbeats, do not add a new control layer by default. First try direct peer handoff:

```text
target + why_now + work_batch + write_scope + evidence_refs + validation + stop_or_recovery
```

If the existing Agents can hand off with that packet and the target Agent can safely wake, work, verify, and back off, do not create a supervisor,
shared control file, workflow, dashboard, or new prompt regime.

Handoff payloads are replace-only, not append-only. A heartbeat prompt may contain at most one `current_handoff`. When that handoff is completed,
blocked, or routed onward, the Agent must remove it or restore the base prompt. Durable evidence, logs, receipts, and decisions belong in artifacts,
project files, or the target thread output, not in the automation prompt.

Recipient-owned prompt rule: the target Agent owns its role mission, default behavior, authority, boundaries, and result-return rules. A different
Agent may only add, replace, or clear the target's single `current_handoff`; it must not rewrite the target's base prompt into a handoff-only prompt.
Use the host automation API when available, preserving the existing base prompt and changing only `current_handoff`, status, and cadence. Directly
editing `automation.toml` is allowed only to repair a broken automation file; after repair, validate that the file parses, the target thread still
matches, and the target's role baseline markers are still present.

Result handoff comes before cleanup. If a run produces failures, fixes, evidence gaps, owner decisions, downstream tasks, or facts that another
Agent must consume, the Agent must first wake the right target with a minimal `current_handoff`, verify that the handoff was written, and only then
clean its own prompt / cadence. If there is no actionable downstream result, it may clean itself and stay quiet. Cleanup without routing actionable
results is a broken handoff, even when the run itself completed.

Return scheduling comes before self-backoff. A frontline, validator, E2E, or worker Agent that completes, blocks, or exhausts a `work_batch` must
send the owner / dispatcher a compact scheduling result before lowering its own cadence, unless the owner already has an equivalent handoff or the
Agent explicitly emits `no_owner_scheduling_needed` with evidence. This result can be combined with the normal handoff, but it must tell the owner:
completed state, evidence refs, remaining blocker, recommended next batch, and whether the Agent should stay active, back off, or wait. Self-backoff
without this owner scheduling signal is a broken handoff even when no direct fix task exists.

Self-prove comes before escalation. A frontline Agent must exhaust safe local proof before handing a blocker to Owner: search accepted refs and
existing public-safe artifacts, run non-live preflight / validator commands that are inside its write and privacy boundary, attach the command or
absence proof, and keep working if the next action is still repo-local. Escalate only when the next step crosses safety, privacy, live / SSH / secret,
release / showcase, real-data, write-scope, authority, or evidence-conflict boundaries.

Post-audit is the default for safe work. Do not use audit as a pre-approval gate when issues can be caught by self-review, Subagents, validators, E2E,
receipts, rollback paths, or owner review after the work batch. Frontline Agents should push implementation, tests, and evidence forward in parallel,
then route the audit findings and fixes; pre-gate only for safety, privacy, live / release, real-data, irreversible writes, write-scope conflict, or
material evidence contradiction.

New issue intake is part of the scheduling result. If development, audit, E2E, validation, or runtime recovery exposes a new bug, missing prerequisite,
broken harness behavior, unclear requirement, or follow-up task, the executing Agent must propose it as an intake candidate instead of burying it in
the final answer. The candidate should be compact: symptom, evidence, affected lane, proposed owner, whether it can run in parallel, and the smallest
validation / stop condition. The owner / dispatcher must either merge it into the next executable backlog batch, route it to the right Agent, reject it
with a reason, or mark the single missing evidence path. A newly discovered issue that is not triaged is a broken handoff.

Only when repeated handoffs fail for a structural reason should you use an existing shared control contract. Avoid putting the full governance model into every automation prompt. Prefer:

```text
shared files-driven control contract + thin role prompts
```

The shared contract states the minimum authority and stop rules needed to prevent recurring failure. It should not become a new project truth source,
status board, or approval layer. Each heartbeat prompt should mostly state the Agent's local role and the direct handoff rule.

If a heartbeat targets the same continuing conversation each time, treat that thread as live working context. Do not force the Agent to reread its own latest final answer, replay the rollout, or reload the full project truth on every tick just to prove continuity. Use external files and thread reads as exception handling: new user instruction, new owner verdict, gate change, context break, boundary risk, repeated no-op, or admission / release decision.

## Multi-Tool Adaptation

`heartbeat` is a native skill directory: one source folder with one `SKILL.md`. Keep that folder as the only editable source and expose it to each host through symlinks or project-local projections.

Default user-level discovery paths:

- OpenAI Codex: `~/.agents/skills/heartbeat`
- Claude Code: `~/.claude/skills/heartbeat`
- Google Antigravity: `~/.gemini/antigravity/skills/heartbeat`

Default project-level discovery paths:

- OpenAI Codex: `<project>/.agents/skills/heartbeat`
- Claude Code: `<project>/.claude/skills/heartbeat`
- Google Antigravity: `<project>/.agents/skills/heartbeat`

Use `scripts/link_skill.py` for link and status checks when this repository is available:

```bash
python3 scripts/link_skill.py . --status
python3 scripts/link_skill.py .
python3 scripts/link_skill.py . --project-root /path/to/project --status
```

Rules:

- Do not copy `SKILL.md` into multiple editable host directories.
- If this folder already lives in a host's native path, treat that as the source and do not create a self-link.
- If a project wants local behavior, clone or vendor the skill under `<project>/.agents/skills/heartbeat`, then link other project host paths to it.
- If a host caches skills, verify in a fresh session before claiming live discovery.
- If a workflow engine, command pack, MCP server, or plugin is involved, adapt to that external surface instead of flattening it into this skill.

## Core Model

Think in this order:

```text
beneficiary pain -> entropy reduction target -> trigger need -> target Agent -> outcome contract -> context mode -> authority -> evidence -> output -> next trigger policy
```

For repeatable Agent work, the practical object is often not a prompt but a harness:

```text
trigger need -> workflow run -> node harness -> outcome gate -> artifact chain -> authority gate -> resume / rewrite / stop
```

Agent management is not HR for models. Foundation-model ability is often similar across Agents; the meaningful differences come from harness design: context, tools, skills, hooks, model choice, sandbox, artifact contract, trigger source, evidence gate, adapter, and recovery policy.

Default philosophy:

```text
capability plane: mostly flat
coordination plane: minimally explicit
```

Do not create hierarchy because one Agent is "smarter", and do not create hierarchy just because coordination feels uncertain. Prefer peer handoff plus
local responsibility. Add hierarchy only when there is a real authority dispute, acceptance decision, write-scope conflict, release risk, or repeated
handoff failure that cannot be solved by a smaller packet.

## Continuous-Thread Light Loops

Not every heartbeat is a fresh-context job. Many host automations wake the same target thread repeatedly. In that mode, continuity is already provided by the conversation, so the harness should optimize for low-noise progress rather than ritual rereading.

Pick a context mode before writing the prompt:

- `continuous_thread`: same target thread, previous turns remain active context.
- `fresh_context`: each run starts from a clean context and must load state from files, artifacts, or upstream outputs.
- `external_workflow_state`: a workflow engine or durable state store is the main continuity mechanism.

Rules for `continuous_thread` heartbeats:

- Default to inheriting the previous turn. If no new user instruction, owner verdict, gate change, or external artifact arrived, continue the previous `work_batch`, agree with the prior proposal, or return `DONT_NOTIFY`.
- Do not read the Agent's own latest final answer or replay its rollout on every tick. That is cold-start behavior in a warm thread.
- Read other threads only when the current action depends on their new final output, verdict, evidence, or blocker.
- Refresh project truth only when the run is about to change authority level, enter implementation / runtime / release admission, adjudicate new evidence, or recover from drift.
- Heavy audit should be event-driven: context break, gate change, boundary violation, repeated no-op, repeated shallow packets, failed validation, or explicit human request.

Keep prompts thin:

```text
role mission + exception-based read policy + output package + permissions + pause/resume rules
```

Put shared governance, command chain, and stop rules in a control contract, not in every automation prompt. If control-plane edits become more active than actual lane delivery, pause control expansion and return to the work lane.

Supervisor delegation should avoid "monitor hoarding":

- Frontline Agents should usually have pre-signoff preparation authority: gather refs, draft acceptance maps, propose PRD patches, run validators, prepare rollback paths, request read-only expert challenge, and assemble an admission packet.
- Supervisors or owner Agents should reserve hard decisions: open a new write surface, sign / reject / defer, resolve authority disputes, modify subordinate triggers, or escalate to a human.
- After two same-level request packets with no new hard blocker, the supervisor must sign, reject, or name the single missing evidence path. It should not ask for another packet at the same layer.
- Owner Agents are delivery drivers, not inboxes. On every result or blocker they must scan the plan for other runnable lanes, dispatch a sufficiently large safe batch, and verify the target trigger / thread exists and was updated. They may wait only after naming the blocking lane, proving no independent lane can move, and giving the resume condition.

Prompt governance learned from live runs:

- A heartbeat prompt is not a backlog, status log, retrospective, or project memory. It should contain the role, authority, stop rules, read policy, and at most one `current_handoff`.
- The base role mission is not disposable. Prompt rewrites that only change a handoff, status, cadence, or evidence refs must preserve the first role / mission paragraph unless the user explicitly changes that role. Losing phrases that define success posture, such as owner responsibility for delivery quality and speed or a worker's mandate to push implementation with Subagents, is a prompt regression.
- Cross-Agent handoff is not cross-Agent prompt ownership. If an Agent cannot preserve the target's role baseline while writing a handoff, it must send the owner a compact handoff packet instead of editing the target automation.
- If the target is a continuing thread, prefer a short delta such as "continue the prior accepted batch with this new evidence" over replaying project truth, prior finals, or long governance text.
- Update prompts only when authority, route, cadence, evidence standard, stop condition, or current handoff changes. Do not edit prompts just to restate good practice.
- When a work lane is clear, the owner should authorize a full `work_batch` or `deep_push`: implementation, self-review, targeted Subagents / sidecars, validator or E2E, fixes, evidence, and result handoff in one run.
- Do not split work into approval packets when audit, testing, and reflection can happen inside the execution batch. Reserve gates for irreversible writes, privacy / security / live / release risk, real-data risk, write-scope conflict, authority conflict, or evidence contradiction.
- If a worker escalates a small blocker without a self-prove packet, the right owner action is usually to return it as an executable self-prove handoff, not to ask for human approval.
- Treat new bugs, missing prerequisites, and harness failures found during execution as backlog intake, not as optional commentary. The executing Agent proposes; the owner absorbs, routes, rejects, or names the one evidence gap.
- Treat "one lane blocked" as a scheduling event, not as a project stop. The owner must either open another safe lane, wake a recovery owner, or document why all lanes are genuinely blocked.
- If prompt cleanup would erase the only active task before another Agent has received it, cleanup is wrong. Route the result first, then clean.

Subagents and sidecars should increase depth without adding bureaucracy:

- Use Subagents only when the host policy and trigger contract allow it, and when the work can be parallelized or professionally challenged without blocking the next local step.
- Prefer concrete sidecar jobs: disjoint implementation slice, read-only architecture / product / risk challenge, validator / E2E run, evidence audit, or targeted root-cause review.
- A Subagent request must name role, scope, allowed writes, expected artifact or finding, validation, and stop condition. Do not pass the whole project history when a delta plus evidence refs is enough.
- Frontline Agents may call Subagents for self-audit, tests, and bounded fixes inside their authorized work batch. Owner Agents may call Subagents for multi-expert challenge before signing, rejecting, or narrowing the single evidence path.
- Subagents do not decide by vote. Their findings are consumed by the responsible Agent, which must either fix, sign, reject, or hand off a concrete next task.
- If Subagents produce actionable results, those results follow the same rule: result handoff comes before cleanup.

Projection and audit loops should stay quiet by default:

- Dashboard Agents project accepted truth and owner verdicts. If there is no new truth, verdict, or user-relevant blocker, they should return `DONT_NOTIFY`.
- Harness auditor Agents should normally be paused or low-frequency. Wake them for review, drift, boundary risk, repeated no-op, wrong signature, or trigger rewrite.

## Outcome-Oriented Harness

Every non-trivial heartbeat needs a definition of the right outcome before it needs a cadence. Do not optimize the Agent for quick visible activity, short transcripts, or internal KPI completion when the real job is durable value for a beneficiary.

Use three principles:

1. Redefine success: prefer sustained value, maintainability, evidence, and downstream usefulness over short-term surface completion.
2. Balance visible and foundation work: reward both immediate deliverables and invisible groundwork such as test scaffolds, state cleanup, durable docs, recovery paths, and context handoff.
3. Anchor validation in beneficiaries: use real users, downstream systems, external checks, validators, or production feedback rather than model self-assessment alone.

Define an `outcome_contract` for any trigger that can change project state or guide other Agents:

```yaml
outcome_contract:
  beneficiary: user | downstream_system | project_owner | operator | future_agent
  entropy_reduction:
    pain_source: comparison_advantage | survival_pressure | both
    reduced_confusion:
    reduced_waiting:
    reduced_repeated_work:
    reduced_drift_or_recovery_risk:
    no_new_noise_rule:
  success_definition:
    visible_delivery:
    foundation_contribution:
    long_term_value:
  reward_shape:
    short_term_completion_weight:
    long_term_value_weight:
    sustainability_weight:
    external_validation_weight:
    delayed_reward_refs: []
  anti_gaming_guardrails:
    - no_metric_theater
    - no_unverified_plan_as_delivery
    - no_shortcut_that_damages_recovery_or_maintainability
  validation_oracles:
    - user_feedback
    - downstream_acceptance
    - validator_or_test
    - third_party_metric
  reflection_questions:
    - Which beneficiary entropy did this run reduce?
    - Did this run create durable value for the beneficiary?
    - Did it trade long-term reliability for short-term visible progress?
    - What invisible foundation work should be protected or continued?
  feedback_loop:
    immediate_signal:
    delayed_signal:
    memory_or_state_update:
    next_trigger_adjustment:
```

Treat reward shaping as harness scoring unless you are actually training a model. For most Agent systems, this means rubrics, validators, owner verdicts, dashboards, state transitions, and trigger policies.

Outcome guardrails:

- Block plans that look complete but have no execution path, evidence path, rollback path, or beneficiary validation.
- Block triggers whose beneficiary pain, entropy reduction target, or causal chain is unclear.
- Penalize specification gaming: inflated status, shallow dashboard progress, fabricated completion, hidden debt, or passing one metric while harming the system.
- Allow protected iteration for foundation work when the long-term benefit is explicit and the trigger has a recheck condition.
- Tighten validation during execution and release phases; allow more exploration only when the trigger is explicitly in discovery mode.

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
  outcome_contract_ref:
  context_policy:
    mode: continuous_thread | fresh_context | external_workflow_state
    inherit_previous_turn: true
    read_self_history: false
    read_policy:
      default: inherit_context
      read_project_truth_when:
        - gate_changed
        - authority_level_changes
        - entering_implementation_runtime_or_release_admission
        - context_discontinuity
    no_change_response: continue_previous | DONT_NOTIFY | suppress
    heavy_refresh_triggers:
      - explicit_human_request
      - boundary_violation
      - repeated_noop
      - repeated_shallow_packets
      - failed_validation
  batch_mode: single_step | work_batch | deep_push
  isolation:
    worktree: optional | required | forbidden
    sandbox:
  permissions:
    observe: true
    write_draft: false
    write_truth: false
    pause_self: true
    modify_others: handoff_only | false
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
- A frontline Agent may modify another Agent's prompt, schedule, or status only for a bounded handoff, and only with `target`, `why_now`,
  `work_batch`, `write_scope`, `evidence_refs`, `validation`, and `stop_or_recovery`. It must not change the target thread, cwd, model,
  execution environment, write authority, role baseline, default behavior, boundary rules, result-return rules, or delete the target trigger.
  Prefer the platform automation update tool; raw file edits are repair-only and must be followed by parser validation and baseline-marker checks.
- A supervisor or project-owner Agent may modify prompt, schedule, and status when it emits a `harness_action` with reason, scope,
  expected effect, and restore / recheck condition.
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
4. A continuous-thread loop may inherit its own prior turns, but any cross-thread dependency, owner verdict, artifact, or project truth change should still be carried through files, upstream node output, or artifact refs.
5. A fresh-context loop must carry enough state through files, upstream node output, or artifact refs to continue safely.
6. Every loop needs a hard bound and a stop reason. A completion tag alone is weaker than a deterministic gate such as tests, validators, or schema checks.
7. Parallel reviewers do not decide by vote. They produce findings; a synthesis / owner-verdict node decides scope, evidence sufficiency, and next action.
8. Platform adapters trigger or report workflows. They do not own acceptance, truth, or write authority.

## Supervisor Plan Control

Only use this section when an Agent truly owns planning / acceptance authority for other Agents. Do not introduce `plan_control` just because a
handoff is needed. Most peer-to-peer Agent collaboration should use the direct handoff packet instead.

When an Agent is explicitly responsible for other Agents, it must be designed as a planner and dispatcher, not just a reviewer. Require a `plan_control` package before it issues directives:

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

1. Run Occam preflight: decide whether no trigger, a simple reminder, an event trigger, a light loop, or a workflow-backed trigger is the least active sufficient mechanism.
2. Name the beneficiary entropy reduction: what confusion, waiting, repeated work, drift, verification burden, or recovery risk should go down?
3. Trace the causal chain: comparison advantage or survival pressure -> pain -> trigger need -> harness architecture -> wakeup mechanics.
4. If it is an Agent trigger, write the Agent role card.
5. Choose trigger source: schedule, event, state change, human, or recovery.
6. Define context payload and memory boundary. Background trigger content must not silently become long-term memory or project truth.
7. Define authority and forbidden actions, especially write rights, pause/resume rights, and delete rights.
8. Define output contract. No-op runs should be suppressible.
9. Define the outcome contract: entropy reduction target, right outcome, visible delivery, foundation contribution, beneficiary oracle, anti-gaming guardrails, and feedback loop.
10. For multi-Agent systems, first define direct handoff. Add a shared control contract only after repeated handoff failure or an explicit authority conflict.
11. If the trigger has phases, retries, or reusable gates, lower it into a workflow-backed trigger contract.
12. Define evidence standard and escalation path.
13. Define verification: persisted config, target thread or workflow run, latest run, artifact chain, state transition, and rollback/resume path.

## Output Shapes

For design-only requests, return:

1. `agent_role_card`
2. `trigger_contract`
3. `outcome_contract`
4. `authority_and_stop_rules`
5. `direct_handoff_rule`; add `shared_control_contract` only when direct handoff is insufficient
6. `workflow_backed_trigger_contract` when a DAG / loop / approval / artifact chain is needed
7. `activation_or_verification_plan`

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

Continuous-thread three-Agent loop:

- Frontline and owner Agents run in their own continuing threads; they inherit prior context by default.
- The owner Agent sends enough authorization for a full `work_batch`, not only a request for another planning packet.
- The frontline Agent continues the prior batch when no new directive appears, while staying inside its pre-signoff authority.
- The Dashboard Agent suppresses output unless accepted truth, owner verdict, blocker, or user-relevant status changed.
- The harness auditor stays paused or low-frequency until drift, no-op, boundary risk, wrong signature, or explicit review.

Low-entropy deep-push loop:

- The owner gives one clear batch: objective, write scope, evidence refs, validation, forbidden zones, and result handoff target.
- The frontline Agent pushes the batch as far as safely possible in one run, using Subagents / sidecars for parallel audit, tests, and root-cause challenge when useful.
- The run must end in one of four states: landed with evidence, blocked by one named evidence path, handed off to the correct next Agent, or paused with no actionable downstream work.
- The prompt should shrink after the batch: remove stale `current_handoff`, keep only base role rules, and leave durable facts in artifacts or project files.

Progress heartbeat:

- Include `run_id`, `attempt`, `last_success_ref`, `current_step`, `blocker_ref`, and `resume_token` so retries do not repeat completed side effects.

Workflow-backed implementation heartbeat:

- Use schedule / event / human request only to start or resume a workflow run.
- Keep per-node prompts thin and scoped; put shared rules in the workflow contract and project control contract.
- Persist progress in an artifact directory or state file so fresh-context nodes can pick up the next unit of work.
- Use deterministic validation and cancel nodes to stop wasted downstream work when a precondition fails.
- Treat workflow UI / IM / GitHub comments as projections unless `files-driven` accepts their artifacts into project truth.

Outcome-oriented heartbeat:

- Require each run to say what visible delivery and foundation contribution it is protecting.
- Use beneficiary validation or downstream acceptance as the strongest success signal.
- Feed delayed signals back into memory, state, scoring, or trigger policy rather than letting the loop repeat a stale definition of success.
- Escalate or rewrite the trigger when short-term activity is rising but beneficiary value, maintainability, or external validation is not.

## Anti-Patterns

- Creating a heartbeat when finishing now, setting a simple reminder, or using an existing event would reduce more entropy.
- Starting from cadence, platform, or automation UI before naming beneficiary pain.
- Writing a cron schedule before defining the Agent role.
- Treating heartbeat as infinite autonomous development.
- Treating a continuing target thread as a cold-start job on every tick.
- Treating heartbeat frequency as a cap on single-run work depth.
- Making the supervisor a passive reviewer instead of the owner of `plan_control`.
- Making the supervisor hoard every preparation decision, so frontline Agents only produce repeated request packets.
- Forcing frontline Agents to wait for supervisor approval when the approved work batch can absorb audit, tests, fixes, and reflection locally.
- Calling Subagents as a discussion ritual instead of assigning parallel implementation, targeted audit, validator, E2E, or root-cause work with a clear artifact.
- Adding `plan_control`, a shared contract, or a supervisor when direct peer handoff would solve the coordination problem.
- Using one broad prompt for every Agent.
- Duplicating the full governance model in every prompt instead of using a shared control contract plus thin role prompts.
- Expanding control documents and automation prompts faster than actual lane delivery.
- Letting `current_handoff` accumulate stale history, or clearing it before actionable results reach the next Agent.
- Adding a supervisor, auditor, dashboard, or workflow because of anxiety, without proving which entropy it reduces.
- Letting no-op heartbeats pollute the main transcript or long-term memory.
- Letting Dashboard projection become project truth.
- Letting a subordinate Agent delete its own trigger.
- Treating missing readiness evidence as liveness failure.
- Treating professional review as generic "quality check" without naming the domain and evidence standard.
- Treating an external workflow README or dashboard as project authority before `files-driven` accepts the contract and artifacts.
- Using an unbounded loop or AI-only completion signal where a deterministic validator, test, schema, or cancel gate is available.
- Optimizing for visible status, short transcripts, or single KPI success while damaging maintainability, recovery, or downstream usefulness.
- Treating model self-reflection as enough validation when beneficiary feedback, tests, external acceptance, or delayed outcome data are available.
