# `governed-delivery` Examples

These shapes label evidence tiers. They are not host-enforcement proof: no gate, oracle seal, sink isolation, or ledger persistence is proven by emitting files.

## Example 1

Input:

```text
Deliver this small feature to done unattended overnight under governance.
```

Expected output shape:

```markdown
## Gate sequence
- `intent` — named human; evidence tier: human decision; auto-release: no
- `spec` — spec owner; evidence tier: artifact; auto-release: no
- `plan` — plan owner; evidence tier: artifact; auto-release: yes if binding is deterministic
- `execution` — executor; evidence tier: runtime; auto-release: yes if packet/ledger checks pass
- `verification` — attester/host verifier; evidence tier: ranked (deterministic first)
- `acceptance` — named accepter; evidence tier: mixed, not self-report; auto-release: no
- `retro` — retro owner; evidence tier: artifact

## Oracle manifest
- authoritative: feature acceptance + invariant (owner, host_seal unmet/`unknown`)
- developer: unit tests the worker may add

## Envelope (task-declared limits — no universal retry count)
- budget, pause list, kill conditions, failure-signature limit, allowed sinks, accepter, strictness (L1–L6)

## Run note
- oracle_sealing: unknown · sink_isolation: unknown · budget_enforcement: unknown · durable_ledger_storage: unknown · human_decision_channel: unknown
- evidence: [] (nothing `met`)
- status: artifact-complete, not enforcement-proven
- GDR-1–GDR-6: unknown (not run)
```

No host enforcement is proven.

## Example 2

Input:

```text
Run this to done under governance overnight. There is no objective oracle.
```

Expected output shape (refusal — do not emit the contract set):

```markdown
## Refusal
- No objective oracle exists → route to `reflective-brief`; do not emit
  intent-record, oracle-manifest, task-packet, envelope, or acceptance-record.

## Evidence tier
- self-assessment that "done" occurred is not a releaser
- high-risk PASS would need a non-model channel; none is available

## Host enforcement
- not proven; nothing was emitted to wire
```

## Example 3

Input:

```text
Emit the preflight evidence checker for an overnight run that requires observed host preconditions.
```

Expected output shape (generated template + host wiring, not enforcement proof):

```markdown
## Deliverable
- checks/preflight.py emitted verbatim from the skill template (stdlib only)
- executable checks/run-preflight.sh supplies the JSON arguments; select its
  absolute pathname as PREFLIGHT, not the Python file or a command string
- run-note.json: five precondition keys (`unknown` default), spec_version,
  host_identity, evidence rows, status artifact-complete
- binding.json: spec_version, host_identity, required_preconditions,
  task-declared max_age_seconds, files (path → SHA256)

## Preflight gate (host-run)
- `python3 checks/preflight.py run-note.json binding.json` → `ready`, exit 0
  only for coherent fresh required evidence with unchanged bound inputs
- wrapper body: `#!/bin/sh` followed by
  `exec python3 checks/preflight.py run-note.json binding.json`
- missing/non-executable/nonzero preflight → exit 4 before agent work and
  before any downstream result release, including the initial-success path
- gate output is evidence; it never promotes the run to enforcement-proven

## Evidence boundary
- Each declared `met`, required or not, needs one matching evidence row:
  precondition, result
  `met`, spec_version, host_identity, UTC observed_at, command argv, principal
  (executor/actual checked role), exit_code 0 for the complete host probe
  (a nonzero denial alone is not a `met`), and artifacts with at least one
  raw-output artifact whose hash still matches
- `met` without evidence, `unknown`/`unmet` required controls, stale
  time/spec/host/oracle/artifact, duplicated or mismatched rows, malformed or
  boolean-as-number types → `hold`/`stale`, exit 4, never a passing claim
- All five note fields must be explicit (`unknown` is a value, not omission).
  Duplicate/conflicting control observations hold before filtering by result.
- Record/input/artifact sources must be regular files; malformed paths, FIFOs
  and devices hold without tracebacks or consuming an endless stream.
- File and artifact existence/hash checks are record-coherence evidence, never
  proof events happened or sealing holds continuously; prose cannot seal the
  checker, the binding, or the evidence
- Cancellation/lifecycle facts appear only when required; absence is
  `unknown`, not implicit kill assurance
```

## Example 4

Input:

```text
Our worker was denied by the sandbox. Can the checker call that an enforcement proof?
```

Expected output shape (role-correct denial handling):

```markdown
## Refusal
- No: a nonzero denial alone is not a `met`. A worker-authorized probe needs
  its same-profile positive control (the complete probe exits 0 where allowed)
  plus the exact expected denial at host observation time.
- Owner-authorized oracle edits are not adversarial worker evidence.
- Keep status artifact-complete until observed host rejection/receipt evidence
  exists under the right principal.

## Host enforcement
- not proven by the checker; the host owns the broker, the sandbox, and the
  integrity of the checker, binding, and evidence
```
