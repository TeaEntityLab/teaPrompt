---
name: governed-delivery
description: Use when a task must be delivered end-to-end under governance — an autonomous or unattended delivery run that needs a gate sequence, an oracle manifest, a task packet, failure-signature exits, decorrelated verification, an evidence ledger, and a named acceptance record. It emits a host-run delivery contract set; it does not enforce it. For effect authority use agent-governance-scaffold; for loop or flow scripts use flow-loop-harness or flow-control-generator.
license: MIT
compatibility: Emits static delivery contracts (Markdown and YAML templates) for a POSIX host with a headless agent CLI; the host owns oracle sealing, sink isolation, budget enforcement, durable ledgers, and the human decision channel — TeaPrompt runs none of them.
metadata:
  risk_level: high
  human_review_required: true
  external_io: false
  context_load: medium
---

# Governed Delivery

**Type:** Domain-pack skill (delivery-contract generation) — registered in the TeaPrompt source repo's domain-pack registry (`plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS`), not one of the nine frozen core workflow skills, and not selected by `reflective-dispatch` route rows; the host harness may invoke it directly. Companion to `agent-governance-scaffold` (effect authority), `flow-loop-harness` (iteration), and `flow-control-generator` (topology), which own those concerns, not the delivery lifecycle.

## Purpose

Turn a governed end-to-end delivery request into a small host-run contract set: a seven-gate sequence, an oracle manifest, a task packet, failure-signature exits, a verification plan, an evidence ledger, an autonomy envelope, and a named acceptance record. Direct answer: unattended delivery cannot be trusted without human intent sign-off and host containment; intent drift and context rot are bounded, not solved. TeaPrompt stays on the methodology side of the methodology-vs-operationalization boundary (source repo: `plans/external-adoption-case-studies-2026-06-20.md`): the emitted files are operational artifacts awaiting host wiring. Sealing, isolation, budgets, ledgers, and the human decision channel are the host's to run — TeaPrompt operates none of that runtime.

## Module Contract

Trigger:

- The user asks to "deliver end-to-end with gates", "autonomous delivery", "unattended delivery run", "governed pipeline to done", or "run this to done under governance".
- A delivery needs a gate sequence, an oracle manifest, a task packet, failure-signature exits, decorrelated verification, an evidence ledger, and a named acceptance record before any unattended run.
- Plain "pipeline", "plan", "deliver", or "automate" without explicit governed end-to-end intent still follows the nine core routes.

Methods:

- Gate mapping: instantiate the seven-gate sequence; size thickness to risk (Gate 2.0); never auto-release `intent` or `acceptance`.
- Packet-first: emit a task packet (spec version, State Ledger, oracle manifest, relevant files). Gates read the packet and the ledgers, not the transcript. A missing acceptance criterion stops the run until the packet is repaired.
- Oracle split: list every acceptance, invariant, and security check with class (authoritative or developer), owner, host sealing precondition, and change protocol. Authoritative oracles are read-only in-run; developer tests may be added. Prompt text cannot seal an oracle — the host must.
- Failure signatures: record failing oracle, error class, and touched surface. After a correction, a repeated signature exits by rollback to the last verified ledger state, a strategy change, or escalation — never an identical retry. Limits are task-declared in the envelope.
- Decorrelated verification: declare channels (deterministic check, runtime evidence, external primary source, independent model, self-assessment) and whether they are independent. A high-risk PASS needs at least one non-model channel.
- Evidence ledger: each entry names the claim, the source, the attester, the freshness kind, and the date checked. A tool result is evidence; the agent's summary of it is not.
- Envelope: before unattended work, record pre-approved budget, per-action pause list, kill conditions, failure-signature limit, allowed sinks, and named accepter. A run outside the envelope stops. Unresolved high-impact irreversible assumptions are Human Review triggers.
- Acceptance: a named accepter closes the delivery against the oracle manifest and product evidence; execution success alone never closes it.
- Minimality: size gate thickness to risk; remove ceremony that defends no named invariant.
- Compatibility: name tool, framework, model, or repository versions the guidance assumes; a workflow skill needs a paired with/without check.

Output:

- The nine contract templates the task needs, written where the user chooses (delete unused objects).
- A filled gate-sequence table: every gate names a releaser and an evidence tier.
- A run note listing host preconditions as met, unmet, or `unknown`, plus the status literal `artifact-complete` or `enforcement-proven`. `artifact-complete` ≠ `enforcement-proven`; the latter requires observed host evidence.

Never:

- Never claim TeaPrompt enforces a gate, seals an oracle, isolates a sink, or persists a ledger; the contract set is host-run and enforcement is a host precondition.
- Never let the executing agent edit the oracle manifest, the verification plan, the acceptance record, or the envelope; those are constitutional paths changed only out-of-band by a different owner.
- Never auto-release a gate on model self-report; a gate releases on deterministic evidence, an attester's receipt, or a named human decision.
- Never use a universal retry or iteration count; budgets and failure-signature limits are task-declared in the envelope.
- Never treat the transcript as the source of record; every gate reads the task packet and the ledgers.
- Never route this pack from `reflective-dispatch` or present it as a tenth core workflow skill; it is host-invoked.

Escalation:

- Unclear intent → `reflective-brief`.
- No-code workflow spec → `reflective-spec-plan`.
- Side effects on credentials, permissions, privacy, billing, production, or destructive ops → `reflective-risk` before first run.
- Effect authority, capability tokens, broker receipts → `agent-governance-scaffold`.
- Iteration loops → `flow-loop-harness`.
- Fixed topology → `flow-control-generator`.
- Whether the delivery run should exist at all → `reflective-minimality`.

## Delivery Gate Sequence

| Gate | Release condition | Who releases | Evidence tier | Auto-release allowed |
| --- | --- | --- | --- | --- |
| `intent` | Named human signs the intent-record; unknowns have owners | named human | human decision | no |
| `spec` | Versioned spec plus oracle manifest; no `stale` dependents | spec owner | artifact | no |
| `plan` | Plan items bound to the current spec version | plan owner | artifact | yes if binding is deterministic |
| `execution` | Work follows the task packet; ledger current | executor | runtime | yes if packet and ledger checks pass |
| `verification` | Verification-plan channels met | attester / host verifier | ranked; deterministic first | yes for deterministic; no for model-only |
| `acceptance` | Named accepter closes against oracles and product evidence | named accepter | mixed; not self-report | no |
| `retro` | Gate retro recorded; policy change kept off activation | retro owner | artifact | yes if the retro record parses |

Auto-release is never allowed for `intent` and `acceptance`. A mid-task spec change bumps the spec version and marks every dependent plan item and ledger entry `stale` before work continues.

## Autonomy Envelope

This pack adds no new lettered ladder: autonomy is expressed through the existing strictness ladder (`L1`–`L6`) and Gate 2.0 thickness. Cross-ref `flow-loop-harness` Human Review Boundary for loops and `agent-governance-scaffold` Gate 2.0 for effect severity. Envelope fields: pre-approved budget, per-action pause list, kill conditions, failure-signature limit (task-declared), allowed sinks, named accepter. A run outside the envelope stops. Thickness scales with risk; higher strictness still cannot auto-release `intent` or `acceptance`.

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

## Delivery Invariants

- Closing execution is not closing acceptance.
- An approval signature is not evidence that an oracle held.
- Self-report is not attestation.
- Artifact presence is not enforcement.
- The transcript is not the record.
- Passing developer tests is not passing the oracle.
- A stale spec cannot release a gate.

## Host Preconditions

The host must supply: oracle sealing (write protection, protected branch, or CI ownership); sink isolation (sandbox, egress control, credential brokering); budget enforcement; durable ledger storage; a human decision channel. TeaPrompt runs none of these. Name each precondition met, unmet, or `unknown` in the run note — do not infer enforcement from files on disk.

## Adversarial Refuters

Host-run checks. A refuter that has not been run is `unknown`, never passed.

- **GDR-1** Executor attempt to edit an authoritative oracle must fail.
- **GDR-2** An instruction embedded in a tool result must not reach any sink.
- **GDR-3** A repeated failure signature must exit, not retry.
- **GDR-4** Losing the transcript must not lose state (packet rebuild from artifacts).
- **GDR-5** Self-report-only evidence must not release a gate.
- **GDR-6** A mid-run spec change must mark dependent items `stale` and re-plan.

## Verification

1. Parse check: every emitted YAML/Markdown template parses. Parseability is not schema validation unless the host declares a dialect and runs it.
2. Structural check: every gate names a releaser and an evidence tier; auto-release is recorded as no for `intent` and `acceptance`.
3. Refuter list exists (GDR-1–GDR-6); each unused check stays `unknown`.
4. Run note uses the status literals `artifact-complete` ≠ `enforcement-proven`. Do not claim the delivery is governed from static files.

## Demotion Triggers

- Contract drift → regenerate from this skill rather than patching a drifted copy.
- Zero recurrence by the next checkpoint, or a host absorbs the pattern → pack-level demotion folds back into `plans/governed-delivery-adoption-2026-09-03.md`.

## Examples

Companion examples live in the installed `<skills-root>/examples/governed-delivery.examples.md` tree when examples are co-installed. They show expected input/output shapes and evidence-tier labels; they are not end-to-end host enforcement proof.

## Prompt Sources

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill is self-contained; the operative rules above are inlined and attributed to their source lens.*

- `plans/governed-delivery-adoption-2026-09-03.md`
- `plans/governable-autonomy-survey-2026-09-03.md`
- `04-agent/runtime-trust-boundary.md`
- `04-agent/artifact-promotion.md`
- `04-agent/workflow-recipes.md`
- `plans/external-adoption-case-studies-2026-06-20.md`
