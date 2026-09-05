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
- budget, pause list, kill conditions, failure-signature limit, allowed sinks, accepter

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
