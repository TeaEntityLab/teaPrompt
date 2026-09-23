# Flow-Pack Usage Log

> **Status: living evidence ledger (non-authoritative).** Manual invocation log
> for every registered domain pack (`DOMAIN_PACK_SKILLS`: five since 2026-09-23;
> scope widened 2026-09-14 so the `governed-delivery` recurrence checkpoint reads
> the same ledger), established 2026-07-11 per
> [necessity record N11](governance-necessity-panel-record-2026-07-11.md) and
> T3/F2 of the [whole-project plan](whole-project-plan-2026-07-11.md). TeaPrompt
> has no telemetry; this log is the only evidence feeding the 2026-10-11 P6
> merge re-litigation and the zero-invocation demotion trigger. Append-only;
> absence of entries is recorded `unknown`-vs-zero honestly: an empty log means
> "no invocation was *recorded*", and the 2026-10-11 review must weigh whether
> unlogged use is plausible before treating it as zero.

## Convention

One row per real invocation (not stub/rig runs, not tests of the templates
themselves):

| Date | Skill | Host / context | Task shape | Outcome + evidence pointer |
| --- | --- | --- | --- | --- |

- "Real invocation" = the skill's contract was used to generate a script for an
  actual task, whether or not the script then ran to completion.
- Rig verification runs during pack maintenance do not count; note them below
  the table only when they change a template.
- Anyone (human or agent) touching the packs appends here in the same change.

## Entries

| Date | Skill | Host / context | Task shape | Outcome + evidence pointer |
| --- | --- | --- | --- | --- |
| — | — | — | — | Zero-state recorded 2026-07-11: no real invocation on record since pack adoption (2026-07-11). |
| — | `agent-governance-scaffold` | — | — | Zero-state recorded 2026-09-14: no real invocation on record since pack adoption (2026-07-17). |
| — | `governed-delivery` | — | — | Zero-state recorded 2026-09-14: no real invocation on record since pack adoption (2026-09-03); the 2026-10-11 checkpoint reads this row — absence stays `unknown`, and demotion is a policy consequence of missing evidence. |
| 2026-09-23 | `verification-map-generator` | omp task agents | Four-product verification-map generation (wsgiLite.js, fpGo, fpEs, fpRust) | Adopted same-day: pattern generated VERIFY.md + features/ + locked spec on four products; fresh-agent arms classified product regression, doc drift, spec-oracle error correctly; evidence in `plans/pstack-survey-2026-09-22.md`. |
| 2026-09-23 | `verification-map-generator` | teaPrompt self-application (dogfooding) | Verification map for this repo's own gate suite | Generated `VERIFY.md` + `features/` (4 areas: test suite, validators, route evals, registry cardinality) + locked `acceptance.yaml` at repo root; fresh-agent sweep + seeded-bug classification run same-day; evidence in commit and sweep report. |

## Template maintenance (not invocations)

- 2026-09-05 — skill-verification pass changed templates in both flow packs
  (`flow-control-generator` D1–D7: quorum counting, merged-result gates, plan
  parsing, worker-id sanitizing, upstream-dependency consumption; `flow-loop-harness`
  FLH-1–FLH-10: progress detection, writer-critic sole-ACCEPT verdict and
  deterministic floor, backlog preflights) — rig-tier stub runs only
  ([record](skill-verification-panel-2026-09-05.md)). Recorded 2026-09-14; the
  convention's same-change note was missed at the time.

## Review checkpoints

- 2026-10-11 — P6 merge re-litigation consumes this table
  ([pack record §Required Changes 6](flow-control-pack-panel-record-2026-07-11.md));
  zero recorded solo invocations for either skill re-opens the merge question.
- Host-native demotion trigger evaluations cite this log for the
  zero-recurrence branch
  ([first evaluation, not fired](flow-pack-demotion-evaluation-2026-07-11.md)).
- 2026-10-11 — `governed-delivery` recurrence checkpoint consumes the
  `governed-delivery` row ([GD adoption §Demotion Triggers](governed-delivery-adoption-2026-09-03.md),
  [runbook Agenda item 7](checkpoint-2026-10-11-runbook.md)).
