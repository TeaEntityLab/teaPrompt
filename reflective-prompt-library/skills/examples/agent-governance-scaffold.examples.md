# `agent-governance-scaffold` Examples

## Example 1

Input:

```text
Our agent can write files and send Slack messages on its own. Add governance so it can't send messages without approval, and so small edits don't add up to a big unreviewed change.
```

Expected output shape:

```markdown
## Authority split
- Proposal=model; Authorization=policy+human (Slack=must-approve, external);
  Effect=broker; Acceptance=verifier + human sign-off on sends
## Deliverable (scaffolding — host runs it)
- .agent/policies/authority-policy.json (AuthorityPolicy + capability token:
  allowed_effects [read,write], forbidden_effects [network_send])
- .agent/approval/slack-gate.yaml (named approval: owner, approver, rationale)
- cumulative-effect-budget.yaml keyed on principal x purpose x authorization_id
  x resource_domain (NOT session); max_external_recipients: 0; reset_requires:
  new_out_of_band_authorization
- effect-receipt.schema.json (issued_by: broker; before_hash/after_state)
## Gates
- file write: thin (idempotent, small blast radius, machine evidence)
- Slack send: thick (external, must-approve) -> approval gate + broker receipt
## Host preconditions (scaffold cannot enforce)
- broker computes receipts; policy engine denies network_send without approval
## Verification
- all objects parse; run-<cli>.sh bash -n clean; budget is lease-keyed
## Escalation
- network_send + approval -> reflective-risk + Human Review before wiring live
```

## Example 2

Input:

```text
Stop our worker agent from quietly relaxing its own tests or policy files to make a task pass.
```

Expected output shape:

```markdown
## Concept
- Entrenchment: control-plane edits need a different owner + out-of-band activation
## Deliverable
- constitutional_paths list (.agent/policies, .agent/verifiers, .agent/approval)
- constitutional_verifiers vs task_mutable_tests split (worker may add unit tests;
  cannot weaken tests/acceptance/locked/**)
- policy_activation object: change != activation; new authorization_epoch;
  usable_by_existing_leases: false
- mutation_suite: worker_weakens_acceptance_test, worker_changes_rule_then_executes
  -> must be rejected pre-effect with worker-immutable evidence
## Verification
- confirm verifiers/policies excluded from worker writable set (host precondition)
## Escalation
- policy/permission changes -> reflective-risk + Human Review
```
