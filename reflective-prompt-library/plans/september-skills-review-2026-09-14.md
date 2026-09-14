# September Skills Review — agentflow surveys and all skill changes since 2026-09-03 — 2026-09-14

> **Status: decided (non-authoritative); review record with applied fixes.** User instruction: *"Review all about agfnow/agentflow and my own skills' changes recently. Fix everything you concern and plan more roadmaps."* Six read-only lenses reviewed the two agentflow records and every skill change since baseline `084852c^` (17 files, +621/−173) against a shared packet (`review-packet-september-skills-2026-09-14.md`, deleted after synthesis). Verdict AGREE WITH CHANGES 6/6; every fix below landed in this commit; the roadmap layer was reconciled. Authority chain unchanged: `06-repo/AGENTS.md` and the invoked `SKILL.md` contracts govern.

## Panel Consensus

- **Decision:** AGREE WITH CHANGES — 6/6 (AFSurveyLedger, AF82DeltaProbe, DupScan, ContradictionScan, PackDiffs, RoadmapGaps).
- **Headline:** the September adoptions are individually sound — every adopted sentence sits exactly once at its surface, no enforcement overclaim, no clean-room leak, every deferred trigger live — but two things were never checked between records: **same-day collisions on one skill** (the 2026-09-03 governable-autonomy survey and governed-delivery adoption each landed the same rule on `reflective-implement`, `reflective-review`, and `reflective-research`), and **the planning layer**, which carried zero September items and had its own staleness falsifiers fire unnoticed.

## Concern Ledger

| # | Concern | Lens | Disposition |
| --- | --- | --- | --- |
| C1 | `reflective-implement` stated the failure-signature exit twice (GA-4 + GD C2, adjacent paragraphs) | coordinator, DupScan, Contradiction | **Fixed** — one paragraph keeping every unique clause; GA pin and GD `ANCHORS` updated |
| C2 | `reflective-review` Evidence Tiers stated "model judgment never solely passes high-risk" twice (GA-5 + GD D1) | coordinator, DupScan, Contradiction | **Fixed** — merged bullet; both pins updated |
| C3 | `reflective-research` stated freshness kind twice (GA-6 + GD E1, adjacent bullets) | coordinator, DupScan | **Fixed** — merged bullet; both pins updated |
| C4 | `reflective-dispatch` Core Rules restated the Never prohibition on unperformed-verification claims | DupScan | **Fixed** — Core Rules line reduced to "Prefer evidence over confidence." |
| C5 | `reflective-minimality` Never restated the Safety Floor list | DupScan | **Fixed** — Never bullet now points at the Safety Floor, keeping its two unique items |
| C6 | `reflective-handoff-retro` said "not from the transcript" four times | coordinator, DupScan | **Fixed** — two unpinned trailing negations trimmed; the Never rule and the AF-19 check stay |
| C7 | Reviewer `Required Fixes` outside the reviewed criteria had no bridge to the AF-2 finding-is-not-authorization rule | Contradiction | **Fixed** — one clause on `reflective-review` Escalation |
| C8 | `stale` is normative on five skills and the pack; `unknown` on four; neither defined in GLOSSARY | Contradiction | **Fixed** — two GLOSSARY entries, phase-local pointers, operational tests |
| C9 | `agent-governance-scaffold.examples.md` still carried `authorization_epoch` after the AGS-5 rename | PackDiffs | **Fixed** |
| C10 | `flow-control-generator.examples.md` Example 2 omitted the mandatory `## Gates` output | PackDiffs | **Fixed** |
| C11 | 8.2 delta record overstated the ambiguous-request probe ("under every wording"; draft 1 was 0/1) | AF82DeltaProbe | **Fixed** — ledger row and prose now give 3 of 5 with the draft-1 exception |
| C12 | 8.2 delta vocabulary (`agf`, `not_performed`, `fast-lane`, `completion-record`, `skills-audit`, `skill-conflicts`) had no clean-room guard | AF82DeltaProbe | **Fixed** — `FOREIGN_TOKENS` extended; the 2026-09-05 guard is the single regex for every delta and its docstring says the record is sealed |
| C13 | EP-1 ledger row read as still deferred after its trigger fired | AFSurveyLedger | **Fixed** — row says the gate is settled |
| C14 | Planning layer: no roadmap/runbook/plan surface carried any September item; plan falsifiers (pack registry 2→4; adoption without queue entry) fired; the 2026-10-11 runbook did not know the `governed-delivery` demotion checkpoint bound to that date | RoadmapGaps | **Fixed** — see Roadmap Additions |
| C15 | Both flow packs within ~700–800 chars of the 20k lint warning; the next adoption breaks the guard | PackDiffs | **Roadmap** — Horizon 1 zero-sum rule now; Horizon 2 lint-tier decision (a policy call, not a unilateral change) |
| C16 | `reflective-implement` Workflow step 4 restates the `reflective-spec-plan` Decision Gate (six clauses) | DupScan | **Roadmap** — needs a cross-referencing-vs-self-contained policy decision; each skill's Prompt Sources line claims self-containment |
| C17 | Core↔pack and inter-pack copies (spec-plan B2/B3 ↔ pack; research ↔ pack; both flow packs' unattended boundary) | DupScan | **No change** — by-design self-containment of host-invoked packs; consolidation trigger already recorded (GD review R6) and now on the runbook |
| C18 | Ledger status vocabularies diverge across skills (`asserted` / `unverified` / `pending` / `open`) | Contradiction | **Roadmap** — trigger: a documented handoff confusion |
| C19 | No examples for orchestrator, router, DAG, writer-critic floor, multi-wave templates | PackDiffs | **Roadmap** — trigger: a host run or the lint-tier decision |
| C20 | `skill:line` citations in the 2026-09-05 record drifted +1..+5 (8 of 18 sampled); every invariant intact | AFSurveyLedger | **No change** — dated citations pin the reviewed state; sealed record |
| C21 | The 142 KB 2026-09-05 record | AFSurveyLedger | **No change** — sealed and fit; the 8.2 delta correctly opened its own record; further addenda would be creep |
| C22 | `reflective-research` states the volatile-claim `stale` downgrade as a rule (§High-Volatility Facts) and again as a bar clarification (§State Ledger) | DupScan | **No change** — the second is the RR-2 clarification that the rule does not lower the `verified` bar; different job |

## Roadmap Additions (planning layer reconciled)

- **`whole-project-roadmap-2026-07-11.md`** — Horizon 1: four standing duties (pack template dry-run; same-day adoption collision check; flow-pack size budget; next agentflow delta protocol). Horizon 2: `governed-delivery` recurrence checkpoint, GD↔AGS redundancy-in-use, flow-pack lint tier decision, A1/E1 tightening; M5 recorded as fired 2026-09-13. Horizon 3: an "Adopted 2026-09-03 → 2026-09-14" section and ten trigger-gated rows (I-1/A-5, GD-19, GD-16, TK-1, E-5, GA-13/XS-4, cross-core checklist, status vocabulary, pack examples, single-sentence reserves). Falsifiability: the fired falsifiers and their reconciliation.
- **`whole-project-plan-2026-07-11.md`** — pack count 2→4 with the registry as the count of truth; WS6 acceptance keyed to `DOMAIN_PACK_SKILLS`; fired-falsifier reconciliation note.
- **`checkpoint-2026-10-11-runbook.md`** — checks 8–10; Agenda item 7 (`governed-delivery` recurrence, GD↔AGS redundancy, A1/E1 and lint-tier decisions, M5 re-fire); outcome section `## GD outcome`, mirrored in the deadman guard.

## Evidence Actually Checked

- **Observed:** `git diff 084852c^ HEAD` over 17 skill files (coordinator, full read of the nine core diffs); six complete lens reviews (hub-delivered); every adopted agentflow sentence located once at its surface; probe-table arithmetic (21 runs) reproduced; both flow-pack char counts (19,320 / 19,178); GLOSSARY heading list; guard pins for every merged or trimmed sentence (`grep` over `plans/tests/*.py`); `make all` green before and after the fixes.
- **Author-claimed, not re-verified:** upstream test tallies in the 2026-09-05 record; the 21 probe outcomes beyond the coordinator-read `git status` observable.
- **[INFERENCE]:** merging same-rule sentences improves clarity per OG-1; no behavioral gain is claimed or measured.
- **Not done:** the deferred policy decisions (lint tier, cross-core referencing, status vocabulary) — routed to the checkpoint, not decided here.

## Falsifiability

This record is wrong if: a merged sentence is absent from its skill or a retired duplicate reappears while the guard passes; a fixed example or GLOSSARY entry is missing; a roadmap row named above is absent; the 2026-10-11 runbook loses Agenda item 7 or `## GD outcome`; or a future same-day adoption pair lands on one skill without the Horizon 1 collision check being recorded.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Six-lens review | done | 6/6 AGREE WITH CHANGES |
| Skill fixes C1–C7 | done | merged/trimmed sentences at named surfaces; guards updated |
| GLOSSARY, examples, record corrections C8–C13 | done | named surfaces |
| Planning layer C14 | done | roadmap, plan, runbook, deadman guard |
| Guard | done | `test_september_skills_review_record.py` |
| Full repository gate | verified | `make all` from repository root |
