# Dormant-Item User-Directed Adoption — 2026-07-12

> **Status: decided (non-authoritative); user-directed adoption wave.** Records
> the batch adoption of the remaining feasible dormant roadmap items under an
> explicit, repeated user instruction ("do them all as possible"). Authority
> chain unchanged: `06-repo/AGENTS.md` and the invoked `SKILL.md` contracts
> govern; this `plans/` record is evidence, not an operating rule. If it and a
> governed surface disagree, the governed surface wins.

## Purpose

Close every dormant item that can be implemented **truthfully today**, using the
AGENTS.md §Harness-Policy allowance that an explicit user instruction may supply
approval while recurrence evidence is recorded `unknown`. No usage number,
recurrence count, or external signal was fabricated.

## Scope

- In scope (adopted): T2 zh-TW pack appendix; M6 README Orientation (EN + zh-TW);
  M4 ephemeral-source internalization stanza; M7 sensitive-evidence packet
  stanza; D4 record-hygiene validator; P12 DAG executor template; P13 multi-wave
  template; writer-critic deterministic companion guidance.
- Out of scope (cannot be truthful): **P6** (needs the 2026-10-11 date + solo
  invocation evidence from the usage log) and **E2** (destructive archive
  restructuring; needs a second independent complaint or a real navigation
  failure, and destructive-op review). Both remain deferred with their triggers.
- Also unchanged: the nine frozen core skills, the two-pack registry cardinality,
  routing (P7 already resolved no-core-integration), Standing Non-Goals.

## Acceptance Criteria

- Each adopted item lands at its named surface with a migrated ledger row and a
  conditional guard flipped from "absent" to "present + structural contract".
- `make all` stays green; the new D4 validator passes and is wired into CI.
- Recurrence stays labelled `unknown`; no fabricated evidence.

## Evidence Actually Checked

- Read this session: both cheatsheets, both READMEs, `workflow-acquisition.md`,
  `external-adoption-review.md`, both pack SKILL bodies, the Makefile, the three
  dormant guard test modules, and the managed-skill / flow-control / rethink
  ledgers.
- Executed: D4 validator (0 enforced today, 38 historical skipped, clean); D4
  focused tests (11 passed); full `make all` recorded in the session final report.
- Tier: implementations are prompt/template/validator artifacts; their utility
  beyond structural correctness is `[INFERENCE]` until real use, exactly as the
  packs' own utility claims remain until the 2026-10-11 review.

## Candidate Adoption Ledger

| ID | Item | Status | Surface | Guard | Re-open / retire trigger |
| --- | --- | --- | --- | --- | --- |
| T2 | zh-TW pack appendix | Adopted 2026-07-12 (user-directed) | `SKILL_TRIGGER_CHEATSHEET.zh-TW.md` §領域包 | `test_dormant_conditional_contracts.py` parity | EN appendix change → re-sync |
| M4 | Ephemeral-source internalization | Adopted 2026-07-12 (user-directed) | `workflow-acquisition.md` §2a | `test_dormant_conditional_contracts.py` | Unused across next internalizations → trim |
| M6 | README Orientation | Adopted 2026-07-12 (user-directed) | `README.md`, `README.zh-TW.md` | `test_dormant_conditional_contracts.py` | Duplicates library README → trim |
| M7 | Sensitive-evidence packet handling | Adopted 2026-07-12 (user-directed) | `external-adoption-review.md` §2a | `test_dormant_conditional_contracts.py` | Never exercised on real sensitive evidence → revisit |
| D4 | Record-hygiene validator | Adopted 2026-07-12 (user-directed) | `validate_record_hygiene.py` + Makefile | `test_validate_record_hygiene.py` | Convention drift → tighten checks |
| P12 | DAG executor template | Adopted 2026-07-12 (user-directed) | `flow-control-generator` | `test_dormant_item_watch.py`, `test_dormant_conditional_contracts.py` | Host DAG primitive → regenerate |
| P13 | Multi-wave template | Adopted 2026-07-12 (user-directed) | `flow-loop-harness` | same | Single-wave work → compose-first |
| WC | Writer-critic deterministic companion | Adopted 2026-07-12 (user-directed) | `flow-loop-harness` guidance | template-set pin | Deterministic verifier exists → prefer it |

## Decision

Adopt the eight items above as user-directed additions with recurrence
`unknown`. Keep P6 and E2 deferred. Migrate the dormancy guards to activation
guards so the anti-drift protection continues to hold in the adopted direction.

## Falsifiability

Wrong if any adopted surface is absent while its ledger row claims adoption; if a
guard still asserts the old "absent" invariant (contradiction → `make all` red);
if P6 or E2 were silently adopted here (they were not); or if `unknown` recurrence
is later cited as if it were observed demand. Retire an item's row to a trim note
if its named re-open trigger fires.
