# Cross-Survey ReThink — Unimplemented Candidates Worth Reopening (2026-10-07)

> **Status:** Decided — RTH-1 adopted in place under user direction 2026-10-07 (`Modify you want and commit`); RTH-2/RTH-3 rejected. `06-repo/AGENTS.md` and the invoked skill contracts remain authoritative.

## Purpose

User instruction: "Rethink all known surveyed features in plans in parallel. Try to find out something we don't implement yet and worthy it."

The original review reported 81 ledger-bearing documents and roughly 45 surveys in the `plans/` corpus; that historical count is not a fresh inventory for this follow-up. It compared deferred/held/record-only candidates against the installed surface after the five domain-pack admissions (`headless-agent-cli-contract`, `arm-blinded-eval-harness`, `acceptance-join-validator`, `golden-benchmark-runner`, `router-trace-linter`, commits `8f610df`/`dfa1789`).

## Method


1. Enumerated all `Candidate Adoption Ledger` tables and extracted every row whose disposition is not `Adopted`/`Rejected` (deferred, held, record-only, study-only, partial).
2. Cross-checked each surviving candidate against current installed surfaces — including the five packs admitted 2026-10-06, which post-date most ledgers.
3. Compared candidates with their recorded reopen triggers, separately from explicit user authorization. RTH-1 was adopted under user direction before a named misreading event was demonstrated.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Reopen trigger / falsifier |
| --- | --- | --- | --- | --- |
| RTH-1 | Eval measurement-discipline repair: `golden-benchmark-runner` + `arm-blinded-eval-harness` name noise floor, failure categorization, and selection-vs-final separation | Adopted in place 2026-10-07 (user direction) | Owned comparison-harness surfaces now exist (repair precondition); TASK-005 disclosed n=1/mixed-arm confounds, not a completed noise-for-improvement misreading. Adoption was prophylactic under explicit user direction, not proof that ECT-2/RRSI-5/ECT-4/RRSI-11 triggers fired. | Bare rethink carries no adoption direction (DS-1); retain the original event-based triggers, without inventing recurrence. |
| RTH-2 | Tenth core skill for eval discipline | Rejected | In-place repair of the two existing packs is the named smallest shape; core frozen at nine | — |
| RTH-3 | Import RRSI annealed-budget / critic-leakage / numeric-threshold machinery | Rejected | Benchmark-integrity machinery for evolve-measured loops; wrong substrate | — |

## The Finding

**The admitted comparison packs provided an in-place repair surface, not evidence that the event-based reopen conditions had fired.**

- **ECT-2** (`coordinate-codex-tasks-eval-survey-2026-09-30`): reopen = "a named local eval run mistakes noise, grader error, harness failure, or task impossibility for product improvement; consider the smallest in-place repair."
- **RRSI-5** (`rrsi-survey-2026-09-30`): same trigger — "a named local eval mistakes noise for improvement; smallest in-place repair at that harness surface."
- **ECT-4 / RRSI-11**: untouched-final separation — reopen = "a named eval-driven optimization needs a reportable final-gain claim."

The two comparison domain packs were admitted 2026-10-06. TASK-005 disclosed n=1 arms, mixed models/guidance, and non-blinded extraction; those honest limits are a near-miss avoided, not a recorded misattribution. The pre-adoption review identified missing explicit noise-floor, failure-categorization, and selection-vs-final requirements in these packs. Its broad zero-hit scan is not current evidence and is not used here to claim absence across all skills.

Under explicit user direction on 2026-10-07, RTH-1 tightened the existing packs instead of adding a surface. The live golden runner now states measurement preflight in Methods 8 and the corresponding Never clauses; the blinded harness states the attribution/final-evaluation limits and carries `noise_floor_basis`, `failure_categorization`, and `selection_vs_final` in CONFIG and the run note. This is preventive contract maintenance, not an observed skill-effect or final-gain result.

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

Observed: the live contracts now contain noise-floor, failure-categorization, and selection-vs-final requirements; the event-based trigger texts are quoted above; TASK-005's mixed-model/single-run confounds remain disclosed in its ticket and receipts. The pre-adoption gap is historical, not the current state. [INFERENCE] In-place repair was the smallest useful preventive shape under explicit user direction; harness existence alone neither fires the original triggers nor supplies recurrence evidence.

## Falsifiability

The original gap claim would be wrong if the exact pre-adoption pack revisions already carried all three obligations; post-adoption text does not refute a historical gap. The preventive-shape judgment is wrong if a concrete run shows the requirements unnecessary or insufficient. A claim that a reopen trigger fired needs the named misreading or reportable-final-gain event that the original ledger specified; none is established by admitting a harness or by TASK-005's honest confound disclosure.

## Latest-survey refresh (2026-10-08)

User direction: “fix all and review the skills or docs to update by newest
surveys; rethink in parallel,” then “until nothing to do.” This permits
bounded repairs to existing surfaces, not a new core skill, pack, owned
runtime, provider campaign, commit, or push.

Three read-only slices reviewed evidence/provenance, workflow composition,
and eval governance. Main integrated the findings; reviewer agreement is
advisory, not independent experimental evidence or approval by majority.
The inputs were the dated Semantica, System Prompts Leaks, Diagram Design,
Matt Pocock delta, pstack/Matt–Lauren, and retained Agentflow/Firstmate
records, not a fresh upstream re-survey.

| Finding / candidate | Disposition and destination | Evidence / verification |
| --- | --- | --- |
| SL-1: RTH-1 state and trigger overclaim | Corrected this record and its project-knowledge pointer; pre-adoption gaps are historical, adoption remains user-directed preventive maintenance. | Live comparison contracts carry the requirements; admitting a harness is not the event named by the original triggers. |
| SL-2 / SL-5 / SL-6: malformed CONFIG, candidate escape, incomplete hold validation | Repaired the blinded harness before copying/scoring; relative/absolute/symlink escape and invalid hold receipts refuse with exit 4. Launch failure/timeout retain execution-error evidence, not product-failure scores. | Regression reproduction originally had 25 failures; standalone emitted-program negatives now refuse without dispatch or traceback. |
| SL-3 / SL-4: misleading hashes and nonexistent invocation log | Clean cutover to `final_state_hashes`; caller owns pre-dispatch clone equality. Audit the emitted `scores.jsonl` stdout/stderr, retained in full so early labels cannot disappear under truncation. | The full-output regression failed before the fix; standalone stdout/stderr controls retain 2,509 characters and expose the early label to the caller audit. |
| SL-7 / SL-8 / SL-9: golden determinism, treatment construction, denominator | Normalize only `observed_at`, retain original receipts, predeclare exact treatment artifact/composition, and define the task-pair denominator. Updated live skill and examples. | Two local `cat` calls produce a timestamp-only difference; normalization accepts it but rejects a changed score. This is stub mechanics, not model utility. |
| AUD-2: summarized invalidations | Extend `reflective-handoff-retro` Continuation Packet and the context-handoff lens; preserve withdrawn support and affected decisions/steps, with an illustrative example. | Actual rendered example preserves “A retracted; D affected” and the held dependent publish step. No graph store or runtime invalidation engine added. |
| AUD-1: scope of integrity claims | Refine runtime-trust-boundary and the review checklist: name covered fields/encoding; authenticity/completeness need separate evidence only when those stronger claims are made. | The Semantica counterexamples motivate the distinction. A narrow field-integrity claim does not require a universal tail anchor. |
| SR-01: file-loaded argv transport | Keep array-form exec and `shell=False`; publish an executable illustration, not a generic shell recipe or unprobed `--` separator. Correct the implication that file loading bypasses argv limits. | Local stub received quotes, shell-looking substitutions, CRLF, Unicode, and trailing newlines as one exact argv value; no shell side effects. Provider flag acceptance and length caps remain unprobed. |
| SR-02: fallback completeness and layered verification | Refine the existing creative-spec acceptance/validation/fallback fields in English and zh-TW; static/no-JS/reduced-motion states retain meaningful content, and structural checks are not rendered-preview proof. | Actual Markdown rendering exposes both obligations. No upstream style system, geometry verifier, or animation implementation imported. |
| AUD-6: survey receipt/count corrections | Correct System Prompts Leaks symlink-entry wording and retain the unverified exact delta-membership boundary; name Semantica's initial unmatched cases 2/5/8 from the retained receipt. | No new upstream execution or rewritten behavioral expectation; case 5's missing inner stderr stays explicit. |

### Dissent and no-change rulings

- **Strongest objection:** some prompt refinements precede a reproduced local
  consumer misreading. Decision: explicit user direction permits completing
  existing handoff/audit/fallback obligations; it does not establish recurrence
  or fire the external ledgers' event-based triggers.
- **SR-03 declined:** creative output already starts with goal/audience/message;
  no local layout-first failure justifies a new semantic-pattern selector.
- **SR-04 narrowed:** preserve named continuation state and invalidations, not
  a separate ledger of every dropped or merged piece of irrelevant raw context.
- AUD-3/AUD-4 remain covered by research freshness/count discipline and scaffold
  provenance; chief-of-staff tactical/strategic composition and memory
  revalidation remain covered. No parallel duplicate workflow added.
- Geometry/export tooling, strategic always-on ceremony, clock/pass-horizon
  constants, lease/wake/merge authority, RRSI machinery, and a tenth core skill
  remain outside the demonstrated gap or host-owned. Their recorded reopen
  triggers stand; missing local evidence is unknown, not zero demand.

### Consumer evidence and limits

The standalone smoke matched 15/15 checks: clean planted repair outcomes,
malformed/config/path/hold refusals, scorer launch/timeout receipts,
full-output label visibility, published argv transport, timestamp normalization,
actual Markdown rendering, and installed-skill resolution. Timeout-branch
smoke shortened the constant to 0.1 seconds; it did not measure the production
300-second ceiling. The four affected installed skill paths resolve to the
canonical repository files.

The [final report](../../review/final-report.md#latest-survey-skills-and-docs-refresh-2026-10-08)
records integration closure. Registry remains nine core plus ten packs.
Synthetic fixtures and rendered docs do not establish model adherence, host
isolation, statistical blinding, source authentication, log completeness,
comparative efficacy, or operational animation behavior. Historical proposal
scaffolds remain admission evidence, explicitly non-current; no compatibility
alias or executable shim is retained.

