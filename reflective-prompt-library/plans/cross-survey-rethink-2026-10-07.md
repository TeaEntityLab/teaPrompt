# Cross-Survey ReThink — Unimplemented Candidates Worth Reopening (2026-10-07)

> **Status:** Decided — RTH-1 adopted in place under user direction 2026-10-07 (`Modify you want and commit`); RTH-2/RTH-3 rejected. `06-repo/AGENTS.md` and the invoked skill contracts remain authoritative.

## Purpose

User instruction: "Rethink all known surveyed features in plans in parallel. Try to find out something we don't implement yet and worthy it."

This record re-examines the deferred/held/record-only candidate ledgers across the `plans/` corpus (81 ledger-bearing documents, ~45 surveys) against the installed surface as of 2026-10-07 — post the five domain-pack admissions (`headless-agent-cli-contract`, `arm-blinded-eval-harness`, `acceptance-join-validator`, `golden-benchmark-runner`, `router-trace-linter`, commits `8f610df`/`dfa1789`).

## Method


1. Enumerated all `Candidate Adoption Ledger` tables and extracted every row whose disposition is not `Adopted`/`Rejected` (deferred, held, record-only, study-only, partial).
2. Cross-checked each surviving candidate against current installed surfaces — including the five packs admitted 2026-10-06, which post-date most ledgers.
3. Applied each candidate's own recorded reopen trigger as the test, not a re-derived judgment.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Reopen trigger / falsifier |
| --- | --- | --- | --- | --- |
| RTH-1 | Eval measurement-discipline repair: `golden-benchmark-runner` + `arm-blinded-eval-harness` must name noise floor, failure categorization, and selection-vs-final separation | Adopted in place 2026-10-07 (user direction) | ECT-2 / RRSI-5 / ECT-4 / RRSI-11 reopen triggers now satisfied by the existence of owned eval harnesses; zero grep hits for the diagnostic vocabulary in `skills/`; TASK-005 n=1/mixed-arm confound | Adoption requires explicit user direction (bare rethink carries no adoption direction, DS-1) |
| RTH-2 | Tenth core skill for eval discipline | Rejected | In-place repair of the two existing packs is the named smallest shape; core frozen at nine | — |
| RTH-3 | Import RRSI annealed-budget / critic-leakage / numeric-threshold machinery | Rejected | Benchmark-integrity machinery for evolve-measured loops; wrong substrate | — |

## The Finding

**One candidate class now has a fired reopen condition that did not exist when the ledgers were written: measurement diagnostic discipline for eval harnesses (ECT-2 / RRSI-5 / RRSI-11 / ECT-4).**

- **ECT-2** (`coordinate-codex-tasks-eval-survey-2026-09-30`): reopen = "a named local eval run mistakes noise, grader error, harness failure, or task impossibility for product improvement; consider the smallest in-place repair."
- **RRSI-5** (`rrsi-survey-2026-09-30`): same trigger — "a named local eval mistakes noise for improvement; smallest in-place repair at that harness surface."
- **ECT-4 / RRSI-11**: untouched-final separation — reopen = "a named eval-driven optimization needs a reportable final-gain claim."

When these were written (2026-09-30) TeaPrompt had no owned eval harness at all — they were Record-only/Adjacent because there was no harness surface to repair. On 2026-10-06 we admitted two: `arm-blinded-eval-harness` and `golden-benchmark-runner`. TASK-005's own honesty record shows why the gap is real: n=1 arms, mixed models, mixed guidance, scorer not arm-blinded at extraction — the harnesses run comparisons but have **no noise-floor preflight, no stall/failure categorization, and no selection-vs-final-test separation contract**. The orchestration exists; the measurement discipline the surveys named is missing. Grep confirms: zero hits for `noise floor|held-out|stall categor|within-noise|headroom` across `skills/`.

This is the "smallest in-place repair" the triggers named: tighten `golden-benchmark-runner` (or the shared Methods text) so a run report must name (a) the noise floor basis — repeated-baseline or documented single-run caveat, (b) failure categorization — a delta is not attributable to the treatment until noise / grader error / harness failure / task impossibility are ruled out, (c) selection-vs-report separation — the score that selected a winner is not a reportable final gain. Same repair class as AF-2/EP-6 wording fixes: a contract that would otherwise permit exactly the failure it exists to prevent (a user mistaking an n=1 delta for improvement — which we just narrowly avoided only by manual honesty disclosure).

## Other Surviving Candidates — Why Not Them

| Candidate | Verdict 2026-10-07 | Reason |
| --- | --- | --- |
| 3XA-1 reviewed-batch hash binding | Not fired | Reopen = "documented local reviewed-vs-shipped asset drift". Session drift observed (index.json staleness, survey commit reset) is process drift, not reviewed-vs-shipped *asset* drift of the class the trigger names. Borderline — worth watching. |
| 3XA-2 cold-reader handoff | Not fired | No local handoff failure where next action was unrecoverable. |
| AEAT-4 acceptance-oracle join | Partially advanced | `acceptance-join-validator` now joins REQ/AC → evidence — but the held item is the *independent* oracle join on a named product. Still needs a named product + explicit authorization. Not this repair. |
| AH-3/AH-14 kill-point benchmark | Not fired | Requires an owned runtime to test; `golden-benchmark-runner` is a doc-scorer harness, not a kill-point/crash-window rig. |
| CCSP4 integrity digest | Not fired | Still needs explicit domain-pack approval + enforcing host. |
| CR-1/CR-2 knowledge staleness | Not fired | No recorded decision-vs-code-drift incident class it names; the supersession convention already handles doc drift. |
| PS-C1/PS2-3 feature-map drift | Not fired | Needs a named product repo; `verification-map-generator` already carries event-driven maintenance contract. |
| GW-9 flow-pack lint tier | Not fired | Date-gated for the 2026-10-11 checkpoint runbook, not a gap. |
| OO-3 bounded delta re-review | Weak | `Recorded`, not a verified gap; loop caps already bound retries. |
| SH1 symlink install distribution | Not fired | Zero observed stale-copy failures from manual install. |

## Rejected Shapes

- **A tenth core skill for eval discipline** — rejected: the gap is inside two packs that already exist; in-place repair is the named shape, and core stays frozen at nine.
- **Importing RRSI's annealed-budget / critic-leakage machinery** — rejected: benchmark-integrity machinery for evolve-measured loops; TeaPrompt's harnesses score docs, not mutate-and-select populations.
- **Numeric thresholds (z=2, δ)** — rejected: prompt-layer contract states the *requirement* (name the noise basis), not a tuned constant; that's the RRSI-5 "per-instance tuned constant" distinction.

## Evidence vs Inference

Observed: the two new packs contain no noise-floor/stall/final-separation text (grep, 2026-10-07); the ledgers' reopen triggers quote above; TASK-005's n=1/mixed-arms confound is recorded in `local://runtime-skill-planning-evidence-2026-10-06.json` and this session's summary. [INFERENCE] That the repair is "in-place in golden-benchmark-runner + arm-blinded-eval-harness Methods/Output" rather than a new surface — smallest satisfying the trigger.

## Falsifiability

This recommendation is wrong if: (a) a grep of either pack shows the diagnostic already stated; (b) a local eval report already commits a noise-for-improvement misreading and was caught by the existing contract text (showing it suffices); (c) the admission record shows the packs were designed never to emit comparative claims (then the repair is cosmetic).
