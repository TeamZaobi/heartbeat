# Continuous-Thread Light Loops

Some heartbeats wake the same target conversation over and over. That is different from a cron job that starts a fresh process or a workflow node that starts with clean context.

In a continuing thread, the Agent already has the previous turn in active context. The harness should use that continuity instead of rebuilding it through rollout replay, self-history reads, or full project-truth reloads on every tick.

## Context Modes

Choose one context mode explicitly:

```yaml
context_policy:
  mode: continuous_thread
  inherit_previous_turn: true
  read_self_history: false
  no_change_response: continue_previous
```

- `continuous_thread`: the target thread is the working state.
- `fresh_context`: the run must load state from files, artifacts, or upstream output.
- `external_workflow_state`: a workflow engine or durable state store owns continuity.

Do not mix these modes accidentally. A continuous thread does not need cold-start proof every run; a fresh-context workflow cannot rely on hidden conversational memory.

## Light Read Policy

For `continuous_thread`, default to this read policy:

```yaml
read_policy:
  default: inherit_context
  read_peer_thread_when:
    - peer_final_changed
    - owner_verdict_changed
    - new_blocker_or_evidence
  read_project_truth_when:
    - gate_changed
    - authority_level_changes
    - entering_implementation_runtime_or_release_admission
    - context_discontinuity
  heavy_refresh_when:
    - explicit_human_request
    - boundary_violation
    - repeated_noop
    - repeated_shallow_packets
    - failed_validation
```

If none of these signals exists, the Agent can answer with one of:

- `continue_previous`
- `agree_with_previous_proposal`
- `continue_work_batch`
- `DONT_NOTIFY`

## Prompt Shape

Keep automation prompts short:

```text
role mission
exception-based read policy
output package
permissions and forbidden actions
pause / resume / rewrite conditions
```

Move shared rules into a control contract. The prompt should point to the contract instead of duplicating it.

Useful split:

- Shared control contract: command chain, authority map, stop rules, escalation, evidence standards.
- Frontline prompt: current lane, allowed preparation work, output package.
- Owner prompt: plan control, verdict, directive, trigger rewrite authority.
- Dashboard prompt: projection only, `DONT_NOTIFY` by default.
- Auditor prompt: paused or low-frequency, wakes for drift, no-op, boundary risk, wrong verdict, or explicit review.

## Delegation Model

A supervisor should not turn every decision into an approval ticket.

Frontline Agents can usually do pre-signoff preparation:

- gather and resolve refs
- draft acceptance maps
- propose PRD or contract patches
- run validators and diff checks
- prepare rollback paths
- request read-only expert challenge
- assemble an admission packet

Owner or supervisor Agents should reserve hard authority:

- open a new write surface
- sign, reject, defer, or escalate
- modify subordinate trigger prompt, cadence, or status
- resolve boundary disputes
- admit implementation, runtime, release, or production-data work

After two same-level request packets with no new hard blocker, the owner must do one of:

1. sign the next scope
2. reject the route with a return gate
3. name the single missing evidence path

Asking for another packet at the same layer is harness churn, not progress.

## Control-Plane Anti-Bureaucracy

The control plane exists to create delivery, evidence, and better decisions. It is failing when it becomes busier than the work.

Watch for:

- prompts grow every run while lane output stays shallow
- Agents reread their own history instead of continuing
- dashboards report every no-op
- auditors become permanent managers
- owner Agents keep asking for decision packets instead of deciding

Countermeasures:

- lower frequency for projection and audit
- keep development / owner loops in `work_batch` mode
- pause control-file expansion when it outpaces implementation or evidence work
- route no-change runs to `DONT_NOTIFY`
- make heavy audit event-driven instead of cadence-driven

## Minimal Contract

```yaml
continuous_thread_loop:
  context_policy:
    mode: continuous_thread
    inherit_previous_turn: true
    read_self_history: false
  default_action:
    if_no_new_signal: continue_previous
    if_no_user_visible_change: DONT_NOTIFY
  heavy_refresh_triggers:
    - context_discontinuity
    - gate_changed
    - boundary_violation
    - repeated_noop
    - repeated_shallow_packets
    - entering_implementation_runtime_or_release_admission
  supervisor_policy:
    frontline_pre_signoff_authority: true
    owner_decides_after_repeated_same_level_packets: true
  prompt_policy:
    shared_rules_live_in_control_contract: true
    automation_prompts_are_thin: true
```
