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
- .agent/policies/capability-token.json (flat capability token + host policy
  binding: allowed_effects [read,write], forbidden_effects [network_send])
- .agent/approval/slack-gate.yaml (named approval: owner, approver, rationale)
- cumulative-effect-budget.yaml keyed on principal x purpose x authorization_id
  x resource_domain (NOT session); max_external_recipients: 0; reset_requires:
  new_out_of_band_authorization
- effect-receipt.contract.json (issued_by: broker; broker-owned receipt store;
  host-specific integrity evidence; before_hash/after_state)
- acceptance-contract.yaml (L0 parse gate; L5 named human decision for Slack)
- run-<cli>.sh wrapper stub + emitted-file manifest (host must route effects
  through the broker — never direct tool calls)
## Gates
- file write: thin (idempotent, small blast radius, machine evidence)
- Slack send: thick (external, must-approve) -> approval gate + broker receipt
## Host preconditions (scaffold cannot enforce)
- broker intercepts all side effects, writes receipts to a worker-nonwritable
  store, and issues integrity evidence; a direct Slack/tool call bypassing the
  broker is a governance failure
- policy engine denies network_send without signed approval from slack-gate.yaml;
  budget enforcer tracks both the lease key and principal x resource_domain
  aggregate across sessions and authorization rotations
## Residual risk if unwired
- the agent can still send Slack if the host calls the Slack tool on model output
  without broker/policy hooks
## Verification
- all contract templates parse; generated run-<cli>.sh is bash -n clean; budget
  contract is lease-keyed and cross-authorization-capped; handover maps emitted
  objects to invariants and labels the result artifact-complete, not
  enforcement-proven; no claim that Slack sends are blocked until host evidence exists
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
- constitutional_paths list (.agent/policies/**, .agent/hooks/**, .agent/approval/**,
  .agent/evidence-schema/**, .agent/verifiers/**)
- constitutional_verifiers vs task_mutable_tests split (worker may add unit tests;
  cannot weaken tests/acceptance/locked/**)
- worker_writable_exclusions deny writes to policies, hooks, approval, evidence-schema,
  verifiers, and locked acceptance tests; the host runtime owns enforcement
- policy_activation object: change != activation; new authorization_epoch;
  usable_by_existing_leases: false
- mutation_suite.yaml (host-run adversarial spec): worker_weakens_acceptance_test,
  worker_changes_rule_then_executes -> the host must reject these pre-effect with
  worker-immutable evidence once wired; this skill only emits the spec
## Verification
- verify the emitted constitutional_paths, policy_activation, and worker-writable
  exclusions appear and parse; handover maps objects to invariants and labels the
  result artifact-complete, not enforcement-proven; runtime enforcement remains an
  unproven host precondition
## Escalation
- policy/permission changes -> reflective-risk + Human Review
```

## Example 3

Input:

```text
Emit a first governance scaffold for a CLI worker that can edit files, but keep it generic across host CLIs.
```

Expected output shape:

```markdown
## Deliverable (canonical `.agent/` tree)
- .agent/policies/capability-token.json
- .agent/broker/effect-receipt.contract.json
- .agent/acceptance/acceptance-contract.yaml
- .agent/INVARIANTS.md
- .agent/HANDOVER.md
- run-<cli>.sh
- <cli>-bounded-worker.md
## INVARIANTS.md excerpt
| emitted_object | invariant(s) | host_enforcer | evidence_now | unwired_obligation |
| --- | --- | --- | --- | --- |
| effect_receipt | #1, #3, #4 | broker | template parses | broker-owned issuance and integrity evidence |
| run-<cli>.sh | #1, #12 | host broker/policy wrapper | bash -n clean | prevent direct_<cli>_exec_via_hook bypass |
## HANDOVER.md status
- **Governance status:** artifact-complete, not enforcement-proven
- Named unwired bypass: direct_<cli>_exec_via_hook until the host broker intercepts the CLI
- Conditional artifacts omitted: conformance_suite, mutation_suite, approver_canary — add only when a host runner exists
## Host matrix
- Keep `<cli>` generic: agy, agent(cursor-cli), Devin, OpenCode, OMP, Claude, Codex, or another headless host may supply the concrete command.
```

