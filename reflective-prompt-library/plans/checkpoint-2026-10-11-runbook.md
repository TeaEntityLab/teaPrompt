# Checkpoint Runbook — 2026-10-11 (P6 / T2 / F4 / roadmap self-review)

> **Status: operator runbook (non-authoritative).** Step-by-step procedure for
> the only date-gated checkpoint on record, aggregating the agenda from the
> [whole-project roadmap](whole-project-roadmap-2026-07-11.md) §Horizon 2 with
> the decision procedures scattered across the owning records. It restates
> gates with pointers and adds none. If a step and its owning record disagree,
> the record wins. Specs or disposition/owning-record pointers for the agenda
> live in the [dormant-work spec book](dormant-work-specs-2026-07-11.md).
>
> **Output contract:** the checkpoint session MUST produce
> `plans/checkpoint-2026-10-11-outcome.md` (required sections below). The
> deadman guard in `plans/tests/test_checkpoint_2026_10_11.py` fails the suite
> once the date has passed with no outcome record — the roadmap's
> "checkpoint passes undocumented" falsifier, mechanized. Write the outcome
> record in the same session as the review.

## Pre-checkpoint evidence checklist (run first, before any discussion)

| # | Check | Command / source | Feeds |
| --- | --- | --- | --- |
| 1 | Usage log current? | [flow-pack-usage-log.md](flow-pack-usage-log.md) — count rows per skill in §Entries | P6 |
| 2 | Unlogged use plausible? | `git log --since=2026-07-11 -- reflective-prompt-library/skills/flow-control-generator reflective-prompt-library/skills/flow-loop-harness` + scan session/retro records for pack mentions | P6 (unknown-vs-zero weighing) |
| 3 | EN stability and EN/zh-TW parity? | Review EN appendix history since 2026-07-11; compare both current appendices with `DOMAIN_PACK_SKILLS` (one bullet per registered pack plus dispatch). T2 landed 2026-07-12; this is re-verification, not re-adoption. | T2 |
| 4 | Demotion evaluation on record? | [flow-pack-demotion-evaluation-2026-07-11.md](flow-pack-demotion-evaluation-2026-07-11.md) exists, verdict "not fired" | F4 duty |
| 5 | Watch-table rows re-checked? | [flow-control roadmap §F4](flow-control-roadmap-2026-07-11.md) — re-verify each of the six watch rows against its named source | F1 re-run decision |
| 6 | Trigger drift sweep green? | `make all` from repository root — `test_dormant_item_watch.py` and conditionals passing means no *watched* surface drifted; it never proves no trigger fired in the world | Roadmap self-review |
| 7 | Decision Index vs roadmap diff | Any [PROJECT_KNOWLEDGE.md](../PROJECT_KNOWLEDGE.md) Decision Index entry since 2026-07-11 that touches a queue item? | Roadmap self-review |
| 8 | `governed-delivery` invocation evidence? | Scan session/retro records, host logs, and `git log --since=2026-09-03` for any host-supplied run of the pack; absence stays `unknown`, never zero | Agenda item 7 |
| 9 | GD↔AGS shared blocks diverged? | Diff the Host Preconditions, `artifact-complete` status, and constitutional-path text of `governed-delivery` against `agent-governance-scaffold` | Agenda item 7 |
| 10 | Flow-pack char counts | Whole-file length of `flow-control-generator` and `flow-loop-harness` as `lint_skills.py` measures it (20k warning; 19,952 and 19,927 on 2026-09-14 — superseded by 19,890 and 19,997 on 2026-10-01) | Agenda item 6 |
| 11 | G9/AS9 trigger evidence? | [G9 adoption ledger](agent-governance-scaffold-adoption-2026-07-17.md), [AS9](all-skills-panel-record-2026-07-18.md), session evidence of governance-vocabulary misroute/discoverability failure | Agenda item 8 |

## Agenda item 1 — P6 / N11: pack merge re-litigation

Owning gate: [necessity record N11](governance-necessity-panel-record-2026-07-11.md);
[pack record §Required Changes 6](flow-control-pack-panel-record-2026-07-11.md).

Decision tree (evidence from checks 1–2):

1. **Both skills ≥1 recorded solo invocation** → merge question stays closed.
   Record the counts; set the next evidence checkpoint (+3 months default).
2. **Either skill = 0 recorded invocations AND unlogged use implausible**
   (check 2 found no pack activity anywhere) → re-open the merge question as a
   review with a Candidate Adoption Ledger; the Minimality dissent
   (one merged skill) is the prior; the strongest counterargument on record is
   the packs' distinct `human_review_required` defaults — see the
   [P6 draft spec](dormant-work-specs-2026-07-11.md) for the merge-branch
   sketch. A fired trigger authorizes *re-litigation*, not silent merging.
3. **Zero recorded but unlogged use plausible** (check 2 found pack activity
   that nobody logged) → record `unknown` honestly (the usage-log convention
   requires weighing this before treating empty as zero); backfill the log from
   the found evidence; extend to the next checkpoint. `unknown` is never zero.

Whatever branch: outcome section in the outcome record + ledger row update in
the necessity record's N11 row is **not** edited (historical); the outcome
record carries the new state, and the Decision Index points at it.

## Agenda item 2 — pack utility claims re-verification

Owning gate: [pack record §Disagreements](flow-control-pack-panel-record-2026-07-11.md) —
utility claims above template correctness were labeled `[INFERENCE]` until this
review. With the usage evidence from item 1: either cite real invocations that
ground the claims, or keep the `[INFERENCE]` labels and say so in the outcome
record. Do not upgrade evidence tiers without evidence (N13 discipline).

## Agenda item 3 — T2: zh-TW pack-appendix parity

T2 was **adopted 2026-07-12** by explicit user direction:
[adoption record](dormant-items-user-directed-adoption-2026-07-12.md). The original
stability-gated draft is historical, not an instruction to re-land it.

- Check 3: record EN appendix changes and its stability interval; keep legitimate
  later pack admissions rather than reverting to the original two-flow-pack draft.
- Re-verify both appendices against the current `DOMAIN_PACK_SKILLS` registry,
  including the dispatch-still-routes bullet and the same pack order. The existing
  `test_dormant_conditional_contracts.py` parity contract is registry-relative.
- Record parity intact / drift repaired / unresolved, the evidence source, and
  any next stability review date. No new adoption or localization scope is granted.

## Agenda item 4 — T4/F1 residue: F4 watch-table re-check

The demotion evaluation itself is done (verdict: not fired, 2026-07-11). The
checkpoint duty reduces to re-checking the six
[F4 watch rows](flow-control-roadmap-2026-07-11.md): for each row, re-verify the
watched surface against its named source; any row that fires triggers its named
follow-up (F1 re-run, S1 conformance re-run, SKILL_INSTALLATION host-coverage
check, survey-note retirement). Record per-row: unchanged / fired+follow-up.

## Agenda item 5 — roadmap self-review

Owning gate: [plan §Falsifiability](whole-project-plan-2026-07-11.md) and
[roadmap §Falsifiability](whole-project-roadmap-2026-07-11.md).

- Walk the Horizon 3 queue: for each item, did its trigger fire since
  2026-07-11 (checks 6–7 + human judgment)? Fired-and-ignored = queue-discipline
  violation — open the re-litigation record now.
- Walk the staleness falsifiers of plan, roadmap, and
  [spec book](dormant-work-specs-2026-07-11.md): any hit → mark the artifact
  stale in the outcome record and schedule its revision.
- If this checkpoint session convenes a governance panel, that panel **is** the
  M5 event (managed-skill re-audit) — run the
  [M5 audit procedure](dormant-work-specs-2026-07-11.md) in the same session.

## Agenda item 6 — AS8 / R10: governance-pack size re-litigation

Owning gate: [all-skill panel AS8](all-skills-panel-record-2026-07-18.md)
(deferred 2026-07-18: shrink or demote if still oversized/low-recurrence), with
the R10 ledger in the
[governance adoption record](agent-governance-scaffold-adoption-2026-07-17.md).

- Re-measure: `python3 reflective-prompt-library/plans/lint_skills.py` — does
  `agent-governance-scaffold` still trip the length warning?
- **Still oversized** → weigh the pre-staged disclosure design in
  [skill-improvement plan WGS-GOV-1](skill-improvement-plan-2026-07-24.md)
  (SKILL.md keeps Module Contract + Four-Power Split + Gate 2.0 + artifact menu;
  object templates move to a co-installed `ARTIFACTS.md` behind a context
  pointer) against demotion; either path opens its own decision record.
- **Within bounds or recurrence evidence changed** → record the measurement and
  the branch not taken; WGS-GOV-1's premise is falsified and its row closes.
- Outcome lands under `## Ledger and index updates` in the outcome record; the
  required-section contract below is unchanged.

## Agenda item 7 — `governed-delivery` recurrence checkpoint and GD↔AGS redundancy

Owning gate: [GD adoption §Demotion Triggers](governed-delivery-adoption-2026-09-03.md)
(date-gated to this checkpoint) and [GD review R5/R6](governed-delivery-review-2026-09-13.md).

1. **Host-supplied invocation evidence exists** (check 8) → recurrence recorded
   with its source; the pack stays; proceed to step 3.
2. **No evidence** → recurrence stays `unknown`; the adoption record's policy
   demotes: fold the gate sequence, contract set, and refuters into a reference
   section of the adoption record and remove only the `governed-delivery` pack
   from `DOMAIN_PACK_SKILLS`. Use its admission checklist and the canonical
   `PACK_SURFACES` manifest in `plans/validate_skill_examples.py` for the full
   unwind; preserve historical usage evidence and every other registered pack.
   Nothing here executes the demotion — the owning record governs.
   A skipped or unrecorded checkpoint demotes by the same policy.
3. **Redundancy-in-use** (check 9): if the pack never ran independently of
   `agent-governance-scaffold`, or the shared blocks diverged, open a
   consolidation record (shared reference; retire the duplicated boilerplate).
4. Decide the two deferred minimality items in the same sitting: A1/E1 anchor
   tightening and the flow-pack lint tier (agenda item 6 extension).
5. This session is a governance panel: the M5 managed-skill re-audit fires again
   (last run 2026-09-13).

## Agenda item 8 — G9 / AS9: governance-vocabulary checkpoint review

Owning duty: [G9 adoption ledger](agent-governance-scaffold-adoption-2026-07-17.md)
and [AS9](all-skills-panel-record-2026-07-18.md), with the
[field-use panel](agent-governance-scaffold-field-use-panel-2026-07-17.md) retaining
the 2026-10-11 proceed/hold/close review.

- Record whether the named misroute/discoverability trigger fired, with its source
  or an explicit no-recorded-event/`unknown` limit.
- Even absent a fire event, record **proceed / hold / close**, rationale, and the
  owning decision pointer. Do not silently carry the deferral past this checkpoint.
- Proceed is re-litigation, not tuning or adoption: G9's ≥3 fresh holdout groups
  and pre-tune observation under R8 still precede any router, quick-cue, or
  dispatch change. This runbook grants no new holdout or tuning authority.

## Outcome record contract (`plans/checkpoint-2026-10-11-outcome.md`)

Required sections — the conditional guard in
`tests/test_checkpoint_2026_10_11.py` checks these the moment the file exists:

1. `## P6 outcome` — branch taken (closed / re-opened / unknown-extended),
   counts, next checkpoint date.
2. `## T2 decision` — registry-wide parity result, EN stability interval and
   changes, evidence source, drift disposition, and any next review date; no re-landing.
3. `## F4 re-check` — per-row table: unchanged / fired + follow-up opened.
4. `## Roadmap self-review` — falsifiers walked, queue items with fired
   triggers, artifacts marked stale.
5. `## Ledger and index updates` — the Decision Index entry text added to
   PROJECT_KNOWLEDGE.md and any ledger rows opened elsewhere.
6. `## GD outcome` — branch taken (retained with evidence / demoted / consolidation
   opened), the invocation evidence or its absence as `unknown`, and the A1/E1 and
   lint-tier decisions.
7. `## G9 / AS9 outcome` — trigger fired / no recorded event / unknown, evidence
   pointer, proceed / hold / close, rationale, owning decision, and next action
   under the unchanged G9 gate (or closure reason).

Post-checkpoint duties (same session): Decision Index entry; regenerate
`index.json` if docs changed; `make all` green from the repository root; if any
trigger fired, its re-litigation record opened with a Candidate Adoption Ledger
(queue discipline: a fired trigger authorizes re-litigation, not adoption).

## Falsifiability (this runbook)

Wrong or stale if: the checkpoint runs and any step here contradicts an owning
record (record wins; fix the runbook); the outcome contract is satisfied but the
deadman still fires (guard bug — fix the test, not the record); or a new agenda
item lands in the roadmap's Horizon 2 without a section here.
