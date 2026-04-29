# Outcome-Oriented Harness

This reference translates "correct outcome definition" into heartbeat and Agent harness design.

The goal is to prevent an Agent loop from optimizing for visible activity, short-term metrics, or internal self-evaluation when the real target is durable value for a beneficiary.

## Core Principles

1. Redefine success.
   Move from surface completion toward sustained usefulness, maintainability, evidence, and downstream acceptance.

2. Balance visible and foundation work.
   A good loop values both immediate delivery and invisible groundwork: state cleanup, tests, recovery, durable docs, context handoff, data quality, and future-Agent readability.

3. Anchor validation in beneficiaries.
   Prefer real users, downstream systems, validators, third-party checks, production telemetry, or explicit owner verdicts over model self-assessment alone.

## Harness Components

### 1. Reward Shape And Success Criteria

In most Agent systems, reward shaping is not model training. It is the scoring and gating surface around the model: rubrics, validators, acceptance checks, dashboards, state transitions, and trigger policies.

Use an explicit outcome contract:

```yaml
outcome_contract:
  beneficiary: downstream_system
  success_definition:
    visible_delivery: "the requested change is implemented and documented"
    foundation_contribution: "tests, state refs, and rollback path make future runs safer"
    long_term_value: "the system becomes easier to operate and extend"
  reward_shape:
    short_term_completion_weight: 0.2
    long_term_value_weight: 0.4
    sustainability_weight: 0.2
    external_validation_weight: 0.2
    delayed_reward_refs:
      - post_release_feedback
      - downstream_acceptance
  validation_oracles:
    - validator_or_test
    - owner_verdict
    - downstream_acceptance
```

The weights are examples. The important point is that the harness does not let a single easy metric define success.

### 2. Guardrails

Guardrails should block outcome drift, not only unsafe text.

Required checks:

- no unverified plan may be presented as delivery
- no dashboard status may become project truth by itself
- no single KPI may override maintainability, recovery, or beneficiary value
- no loop may keep running without a stop condition, recheck condition, or evidence delta
- no hidden debt may be buried under a positive status summary

Dynamic strictness:

- Discovery can permit more foundation work and uncertainty.
- Execution should require evidence and artifact updates.
- Release or acceptance should require external validation, owner verdict, or downstream signoff.

### 3. Feedback Loop

A heartbeat should learn from delayed signals.

Useful feedback sources:

- direct user feedback
- downstream system acceptance or rejection
- test and validator results
- production incidents or support tickets
- delayed adoption, maintenance, or rollback data
- third-party objective metrics

Feed the result into:

- memory or state records
- trigger cadence
- next prompt or workflow node
- reward rubric
- guardrail strictness
- owner escalation policy

If delayed feedback contradicts an earlier "success", the next run should reopen the outcome contract instead of preserving the old verdict.

### 4. Self-Reflection

Reflection is useful only when it is tied to the outcome contract.

Minimum reflection questions:

```text
Did this run create durable value for the beneficiary?
Did visible progress hide missing foundation work?
Did the run trade maintainability or recovery for short-term completion?
Which external or delayed signal could falsify this success claim?
What should the next trigger change: cadence, prompt, target, gate, or stop policy?
```

Reflection output should become a patch, state update, or trigger adjustment when it identifies a real drift. It should not remain free-floating commentary.

### 5. Multi-Agent Orchestration

In multi-Agent systems, outcome alignment is a system property.

Require each Agent to report:

- visible delivery
- foundation contribution
- beneficiary affected
- evidence produced
- debt created or reduced
- validation oracle still missing

The supervisor or project-owner Agent should maintain an outcome view across lanes:

```yaml
outcome_health:
  visible_progress:
  foundation_progress:
  beneficiary_signal:
  external_validation:
  debt_trend:
  reorchestration_needed: true | false
```

If visible progress rises while beneficiary signal, external validation, or foundation health weakens, the supervisor should re-orchestrate: slow down, split the lane, add validation, change the prompt, or escalate.

## Anti-Gaming Rules

Watch for:

- beautiful plans with no execution path
- "all green" dashboards without artifact refs
- short-loop churn presented as progress
- metric success that increases future maintenance cost
- self-review replacing external validation
- foundation work used as an excuse for never delivering visible value
- delayed feedback ignored because the original run already closed

## Minimal Output

When a user asks for outcome-oriented heartbeat design, return:

1. `outcome_contract`
2. `guardrails`
3. `validation_oracles`
4. `feedback_loop`
5. `reflection_questions`
6. `orchestration_policy` when multiple Agents are involved
