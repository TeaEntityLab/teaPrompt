---
name: governed-delivery
description: Use when a task must be delivered end-to-end under governance — an autonomous or unattended delivery run that needs a gate sequence, an oracle manifest, a task packet, failure-signature exits, decorrelated verification, an evidence ledger, and a named acceptance record. It emits a host-run delivery contract set; it does not enforce it. For effect authority use agent-governance-scaffold; for loop or flow scripts use flow-loop-harness or flow-control-generator.
license: MIT
compatibility: Emits delivery contracts (Markdown/YAML) and an optional stdlib-only Python 3.7+ record checker for a POSIX host with a headless agent CLI; the host owns sealing, sink isolation, budgets, durable ledgers, and human decisions — TeaPrompt runs none of them.
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
- Envelope: before unattended work, record pre-approved budget, per-action pause list, kill conditions, failure-signature limit, allowed sinks, named accepter, and strictness level. A run outside the envelope stops. Unresolved high-impact irreversible assumptions are Human Review triggers.
- Acceptance: a named accepter closes the delivery against the oracle manifest and product evidence; execution success alone never closes it.
- Minimality: size gate thickness to risk; remove ceremony that defends no named invariant.
- Compatibility: name tool, framework, model, or repository versions the guidance assumes; a workflow skill needs a paired with/without check.

Output:

- A run note listing host preconditions as met, unmet, or `unknown`, plus the status literal `artifact-complete` or `enforcement-proven`. `artifact-complete` ≠ `enforcement-proven`; the latter requires observed host evidence. The emitted run note keeps the five existing precondition keys and their `unknown` default; the JSON note is the same mapping serialized for the checker, not a second authority surface.
- Optionally, the `checks/preflight.py` record-coherence checker and, for flow-pack integration, its executable `checks/run-preflight.sh` wrapper (see the Preflight evidence checker template). The host selects the wrapper pathname only when required; empty preserves an attended example without claimed runtime enforcement. The host protects both files, the binding, and the evidence; prose cannot seal them.

Never:

- Never claim TeaPrompt enforces a gate, seals an oracle, isolates a sink, or persists a ledger; the contract set is host-run and enforcement is a host precondition.
- Never let the executing agent edit the oracle manifest, the verification plan, the acceptance record, or the envelope; those are constitutional paths changed only out-of-band by a different owner.
- Never auto-release a gate on model self-report; a gate releases on deterministic evidence, an attester's receipt, or a named human decision.
- Never use a universal retry or iteration count; budgets and failure-signature limits are task-declared in the envelope.
- Never treat the transcript as the source of record; every gate reads the task packet and the ledgers.
- Never accept or promote `enforcement-proven` on the preflight checker's output alone: it validates record coherence at a point in time, not that events happened, that sealing holds continuously, or that delivery is accepted. File and artifact existence/hash checks are record-coherence evidence, never proof an event occurred or sealing holds continuously.
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
| `execution` | Work follows the task packet; ledger current | executor | runtime | yes if the deterministic packet-binding and ledger-currency checks pass; no when packet-adherence rests on agent self-report |
| `verification` | Verification-plan channels met | attester / host verifier | ranked; deterministic first | yes for deterministic; no for model-only |
| `acceptance` | Named accepter closes against oracles and product evidence | named accepter | mixed; not self-report | no |
| `retro` | Gate retro recorded; policy change kept off activation | retro owner | artifact | yes if the retro record parses |

Auto-release is never allowed for `intent` and `acceptance`. A mid-task spec change bumps the spec version and marks every spec_version-keyed artifact — plan items, ledger entries, the oracle manifest, the task packet, and the acceptance record — `stale`; the oracle manifest is re-validated and the affected slice re-planned before work continues. Auto-release keys off whether the release condition is a deterministic check, not off the evidence tier.

## Autonomy Envelope

This pack adds no new lettered ladder: autonomy is expressed through the existing strictness ladder (`L1`–`L6`) and Gate 2.0 thickness. Cross-ref `flow-loop-harness` Human Review Boundary for loops and `agent-governance-scaffold` Gate 2.0 for effect severity. Envelope fields: pre-approved budget, per-action pause list, kill conditions, failure-signature limit (task-declared), allowed sinks, named accepter, strictness (L1–L6). A run outside the envelope stops. Thickness scales with risk; higher strictness still cannot auto-release a gate.

## Contract Set

Emit only what the task needs. Read the selected sections of the co-installed
[ARTIFACTS.md](ARTIFACTS.md#contract-set) before emission; they contain the
normative YAML bodies and field purposes. Install this complete skill directory,
not `SKILL.md` alone. Each object is a static contract; the host wires enforcement.

| Object | Invariant |
| --- | --- |
| [intent-record](ARTIFACTS.md#intent-record) | Unsigned intent cannot release `intent`; tacit gaps stay visible as owned unknowns. |
| [oracle-manifest](ARTIFACTS.md#oracle-manifest) | The executing agent does not edit this file; a developer test is not an authoritative oracle. |
| [task-packet](ARTIFACTS.md#task-packet) | If an acceptance criterion is missing from the packet, stop and repair the packet. |
| [failure-log](ARTIFACTS.md#failure-log) | A repeated signature is not an identical retry; budgets stay task-declared. |
| [verification-plan](ARTIFACTS.md#verification-plan) | Model judgment may block or warn; it never solely passes a high-risk claim. |
| [evidence-ledger](ARTIFACTS.md#evidence-ledger) | The agent's summary is not the attester; unrun freshness is `unknown`. |
| [acceptance-record](ARTIFACTS.md#acceptance-record) | Execution success alone never closes this record. |
| [envelope](ARTIFACTS.md#envelope) | A run outside this envelope stops; no universal retry count lives here. |
| [gate-retro](ARTIFACTS.md#gate-retro) | Policy change stays separate from policy activation; feed the retro into change, then activate out-of-band. |

## Delivery Invariants

- Closing execution is not closing acceptance.
- An approval signature is not evidence that an oracle held.
- Self-report is not attestation.
- Artifact presence is not enforcement.
- The transcript is not the record.
- Passing developer tests is not passing the oracle.
- A stale spec cannot release a gate.

## Host Preconditions

The host must supply: oracle sealing (write protection, protected branch, or CI ownership); sink isolation (sandbox, egress control, credential brokering); budget enforcement; durable ledger storage; a human decision channel. TeaPrompt runs none of these. Name each precondition met, unmet, or `unknown` in the run note — do not infer enforcement from files on disk. A run note that omits a named precondition is incomplete, not passing; a filled block is an output, not enforcement.

Probe discipline (observed 2026-10-06 dry run, macOS seatbelt): a denial receipt needs byte-level verification — hash protected files before and after the attempt, and show the target unchanged; a nonzero probe exit alone does not distinguish enforcement from launch failure. Egress denials must use IP-literal connects (`/dev/tcp/1.1.1.1/443`, `nc`), not hostname lookups — DNS failure (`curl` exit 6) is ambiguous between sandbox denial and missing resolver plumbing. Record the verifying harness's exit code as `exit_code` (the denied syscall's EPERM is the observed result, not the probe's); consolidate all attempts for one control into a single evidence row with multiple `artifacts` — a second row for the same precondition holds as duplicate. Oracle-integrity probes should cover the full alteration surface: direct write, rename-replace, symlink swap, chmod-then-write, and descendant-process writes (inheritance observed, not assumed). Bound inputs can change between gate calls: run the selected gate again after work before release — a mutation landing in that window is caught only by the post-work check (TOCTOU). Malformed or environment-incomplete invocations (prompt-as-flag swallowed, headless permission denial) are recorded as discarded receipts, never as arm results in a comparison denominator.

```yaml
oracle_sealing: unknown           # met | unmet | unknown
sink_isolation: unknown
budget_enforcement: unknown
durable_ledger_storage: unknown
human_decision_channel: unknown
evidence: []                      # one entry per `met`: what was observed, where
status: artifact-complete         # enforcement-proven only with observed host evidence
```

The JSON run note is the same five-key mapping serialized for the checker, plus `spec_version`, `host_identity`, per-`met` evidence rows, and the `artifact-complete` status. `unknown` is the only default for every precondition.

## Adversarial Refuters

Host-run checks. A refuter that has not been run is `unknown`, never passed.

- **GDR-1** Executor attempt to edit an authoritative oracle must fail.
- **GDR-2** An instruction embedded in a tool result must not reach any sink.
- **GDR-3** A repeated failure signature must exit or escalate, not retry identically. Signature = task identity + error class (a prompt-hash is a minimal proxy; record which reading was implemented); a distinct-signature task must still proceed within budget.
- **GDR-4** Losing the transcript must not lose state (packet rebuild from artifacts).
- **GDR-5** Self-report-only evidence must not release a gate.
- **GDR-6** A mid-run spec change must mark every spec_version-keyed artifact (plan items, ledger entries, oracle manifest, task packet, acceptance record) `stale` and re-plan; any downstream artifact left at the prior spec_version is a refuter failure.

## Preflight Evidence Checker (generated template, host-run)

When a task requires observed host preconditions, read the co-installed [TEMPLATES.md](TEMPLATES.md) and emit `checks/preflight.py` from its normative template. CLI: `python3 checks/preflight.py run-note.json binding.json`. For flow packs, select its executable wrapper as `PREFLIGHT`; selecting the Python file directly supplies no JSON arguments and correctly holds with exit `4`. The checker is stdlib-only and single-pass: it reads the JSON records, resolves relative paths against the task-root working directory, and exits `0` only for coherent fresh required evidence with unchanged bound inputs; otherwise it exits `4`. It emits one disposition line (`ready`, `hold`, or `stale`) plus JSON detail. A missing/non-executable/failing selected gate stops dispatch or result release with exit `4`; its output never promotes a run to `enforcement-proven`.

The checker does not invoke agent CLIs, execute arbitrary probe commands, change permissions, mutate records, seal anything, or implement lifecycle. It validates record coherence only: declared types (including boolean-as-number ambiguity), unique known control keys, no duplicate required or evidence rows, per-`met` evidence rows bound to the current spec/host, fresh observations within the binding's task-declared `max_age_seconds` (no universal fallback), matching file hashes for immutable task inputs/oracles/verifier, and at least one raw-output artifact per required `met`. An `exit_code` of `0` on the complete host probe is required; a nonzero denial alone is not a `met`. Missing, malformed, `unknown`/`unmet`, duplicated, mismatched, or stale bindings return `hold` or `stale` with exit `4`, never a passing claim. Cancellation and run-lifecycle facts appear only when the host requires them; their absence is `unknown`, never implicit kill assurance. A worker-authorized probe needs its same-profile positive control and exact expected denial at host observation time; owner-authorized oracle edits are not adversarial worker evidence. The host owns and protects the checker, the binding, and the evidence; prose cannot seal them.

The serialized note must explicitly contain all five precondition fields; `unknown` is the generated value, not an omission waiver. Index evidence by precondition before result validation: duplicate or conflicting control rows hold, including a non-`met` row accompanying a `met` claim. Every declared `met`, required or not, needs coherent evidence. JSON records, bound inputs and raw artifacts must be regular files; malformed paths, FIFOs and devices hold rather than traceback or consume a stream. Open-descriptor checks do not authenticate paths, seal against later changes or supply arbitrary-filesystem time/resource guarantees.

## Verification

1. Parse check: every emitted YAML/Markdown template parses. Parseability is not schema validation unless the host declares a dialect and runs it.
2. Structural check: every gate names a releaser and an evidence tier; auto-release is recorded as no for `intent` and `acceptance`.
3. Refuter list exists (GDR-1–GDR-6); each unused check stays `unknown`.
4. Run note uses the status literals `artifact-complete` ≠ `enforcement-proven`. Do not claim the delivery is governed from static files. Handover/status generation keeps the same boundary: a generated note is a record for the host to check, never a sealed or enforced result.

## Demotion Triggers

- Contract drift → regenerate from this skill rather than patching a drifted copy.
- Zero recurrence by the next checkpoint, or a host absorbs the pattern → pack-level demotion folds back into `plans/governed-delivery-adoption-2026-09-03.md`. Recurrence evidence is host-supplied (a prompt library cannot observe host invocations); when no invocation evidence reaches the checkpoint, recurrence stays `unknown` — and a skipped or unrecorded checkpoint triggers demotion as a policy consequence of missing evidence, not as an observed zero.
- Redundancy-in-use → if the pack is never invoked independently of `agent-governance-scaffold`, or the shared host-precondition / `artifact-complete` / constitutional-path machinery diverges between the two packs, fold the delivery lifecycle into a shared reference and retire the duplicated boilerplate rather than maintaining two copies.

## Examples

Companion examples live in the installed `<skills-root>/examples/governed-delivery.examples.md` tree when examples are co-installed. They show expected input/output shapes and evidence-tier labels; they are not end-to-end host enforcement proof.

## Prompt Sources

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill directory is self-contained, including its co-installed `ARTIFACTS.md` and `TEMPLATES.md`; the operative rules above govern both references.*

- `plans/governed-delivery-adoption-2026-09-03.md`
- `plans/governable-autonomy-survey-2026-09-03.md`
- `04-agent/runtime-trust-boundary.md`
- `04-agent/artifact-promotion.md`
- `04-agent/workflow-recipes.md`
- `plans/external-adoption-case-studies-2026-06-20.md`
