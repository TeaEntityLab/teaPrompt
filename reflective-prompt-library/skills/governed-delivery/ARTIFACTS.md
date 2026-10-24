# `governed-delivery` Artifacts

Portable sibling to [SKILL.md](SKILL.md) in this directory. Read its Module Contract, gate sequence, invariants, host preconditions, verification and demotion rules before emitting these objects. The sections below are the normative contract templates, not a second implementation or evidence of host enforcement.

## Contract Set

Emit only what the task needs. Each object is a static contract; the host wires enforcement.

### intent-record

Purpose: freeze the signed goal, owned unknowns, and irreversible assumptions before any later gate.

```yaml
intent_id: ""
goal: ""
out_of_scope: []
unknowns: [{item: "", owner: ""}]
irreversible_assumptions: [{item: "", human_review: required}]
signed_by: ""
status: unsigned
```

Invariant: unsigned intent cannot release `intent`; tacit gaps stay visible as owned unknowns.

### oracle-manifest

Purpose: name every acceptance, invariant, and security oracle with class, owner, seal, and change protocol.

```yaml
spec_version: ""
oracles:
  - name: ""
    class: authoritative  # or developer
    owner: ""
    host_seal: write_protection  # or protected_branch | ci_ownership | none
    change_protocol: out_of_band
```

Invariant: the executing agent does not edit this file; a developer test is not an authoritative oracle.

### task-packet

Purpose: the source of record for work — spec version, State Ledger, oracle manifest, files — never the transcript.

```yaml
spec_version: ""
state_ledger_ref: ""
oracle_manifest_ref: ""
files: []
missing_acceptance: stop_and_repair
```

Invariant: if an acceptance criterion is missing from the packet, stop and repair the packet.

### failure-log

Purpose: record failure signatures so a repeat after correction exits instead of retrying.

```yaml
entries:
  - oracle: ""
    error_class: ""
    surface: ""
    after_correction: false
    exit: rollback  # or strategy_change | escalate
```

Invariant: a repeated signature is not an identical retry; budgets stay task-declared.

### verification-plan

Purpose: declare channels and independence so a high-risk PASS cannot rest on self-assessment.

```yaml
channels:
  - kind: deterministic  # or runtime | external_primary | independent_model | self_assessment
    independent: true
high_risk_pass_requires_non_model: true
compatibility_bounds: {tools: "", models: "", repos: ""}
```

Invariant: model judgment may block or warn; it never solely passes a high-risk claim.

### evidence-ledger

Purpose: rank attested evidence with freshness; keep claim, source, and attester distinct.

```yaml
entries:
  - claim: ""
    source: ""
    attester: ""
    freshness_kind: recheck_date  # or tracking_event | immutable_pin
    date_checked: ""
```

Invariant: the agent's summary is not the attester; unrun freshness is `unknown`.

### acceptance-record

Purpose: a named accepter closes delivery against the oracle manifest and product evidence.

```yaml
spec_version: ""
accepter: ""
oracle_manifest_ref: ""
product_evidence_refs: []
closed: false
```

Invariant: execution success alone never closes this record.

### envelope

Purpose: bound the unattended run before it starts.

```yaml
budget: ""
pause_actions: []
kill_conditions: []
failure_signature_limit: task_declared
allowed_sinks: []  # secrets, memory_or_skill_promotion, permissions, deployment, outbound, money
accepter: ""
strictness: L2  # L1–L6
```

Invariant: a run outside this envelope stops; no universal retry count lives here.

### gate-retro

Purpose: record which gates fired, which were bypassed, and which caught nothing.

```yaml
gates:
  - name: intent  # spec | plan | execution | verification | acceptance | retro
    fired: false
    bypassed: false
    caught_nothing: false
policy_change: separate_from_activation
```

Invariant: policy change stays separate from policy activation; feed the retro into change, then activate out-of-band.

