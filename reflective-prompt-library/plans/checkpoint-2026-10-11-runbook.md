# Checkpoint Runbook — 2026-10-11 (P6 / T2 / F4 / roadmap self-review)

> **Status: operator runbook (non-authoritative).** Step-by-step procedure for
> the only date-gated checkpoint on record, aggregating the agenda from the
> [whole-project roadmap](whole-project-roadmap-2026-07-11.md) §Horizon 2 with
> the decision procedures scattered across the owning records. It restates
> gates with pointers and adds none. If a step and its owning record disagree,
> the record wins. Draft specs for every agenda item live in the
> [dormant-work spec book](dormant-work-specs-2026-07-11.md).
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
| 3 | EN appendix stable? | `git log --since=2026-07-11 -- reflective-prompt-library/skills/SKILL_TRIGGER_CHEATSHEET.md` — appendix section untouched since 2026-07-11? | T2 |
| 4 | Demotion evaluation on record? | [flow-pack-demotion-evaluation-2026-07-11.md](flow-pack-demotion-evaluation-2026-07-11.md) exists, verdict "not fired" | F4 duty |
| 5 | Watch-table rows re-checked? | [flow-control roadmap §F4](flow-control-roadmap-2026-07-11.md) — re-verify each of the six watch rows against its named source | F1 re-run decision |
| 6 | Trigger drift sweep green? | `make all` from repository root — `test_dormant_item_watch.py` and conditionals passing means no *watched* surface drifted; it never proves no trigger fired in the world | Roadmap self-review |
| 7 | Decision Index vs roadmap diff | Any [PROJECT_KNOWLEDGE.md](../PROJECT_KNOWLEDGE.md) Decision Index entry since 2026-07-11 that touches a queue item? | Roadmap self-review |

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

Owning gate: [pack record §Required Changes 6](flow-control-pack-panel-record-2026-07-11.md).

- Check 3 says **stable** → T2 qualifies as due: translate the EN appendix
  (ready draft in the [T2 spec](dormant-work-specs-2026-07-11.md)), land it with
  cheatsheet parity tests green — the pre-written conditional contract in
  `test_dormant_conditional_contracts.py` enforces the structural parity the
  moment pack names appear in the zh-TW file.
- Check 3 says **edited since 2026-07-11** → the stability clock restarts; name
  the next check date in the outcome record.

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

## Outcome record contract (`plans/checkpoint-2026-10-11-outcome.md`)

Required sections — the conditional guard in
`tests/test_checkpoint_2026_10_11.py` checks these the moment the file exists:

1. `## P6 outcome` — branch taken (closed / re-opened / unknown-extended),
   counts, next checkpoint date.
2. `## T2 decision` — stable→landed, or clock restarted with date.
3. `## F4 re-check` — per-row table: unchanged / fired + follow-up opened.
4. `## Roadmap self-review` — falsifiers walked, queue items with fired
   triggers, artifacts marked stale.
5. `## Ledger and index updates` — the Decision Index entry text added to
   PROJECT_KNOWLEDGE.md and any ledger rows opened elsewhere.

Post-checkpoint duties (same session): Decision Index entry; regenerate
`index.json` if docs changed; `make all` green from the repository root; if any
trigger fired, its re-litigation record opened with a Candidate Adoption Ledger
(queue discipline: a fired trigger authorizes re-litigation, not adoption).

## Falsifiability (this runbook)

Wrong or stale if: the checkpoint runs and any step here contradicts an owning
record (record wins; fix the runbook); the outcome contract is satisfied but the
deadman still fires (guard bug — fix the test, not the record); or a new agenda
item lands in the roadmap's Horizon 2 without a section here.
