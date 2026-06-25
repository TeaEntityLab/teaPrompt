# Multi-Agent Panel Consensus — 2026-06-25

Language: English

## Purpose

Record the Socratic deliberation loop across six model-provider lenses on TeaPrompt
goals and the nine-skill layer, plus the agreed options implemented in-repo.

This is a **judgment artifact**, not an agent instruction source.

## Panel Lenses

| Lens | Role emphasis |
| --- | --- |
| Opus 4.8 | Governance, epistemics, promotion gates |
| Codex GPT 5.5 | Harness policy, verifiability, eval CI |
| Gemini 3.5 Flash | Cost, context, strictness ladder |
| Composer 2.5 | IDE-native UX, progressive disclosure |
| Sakana Fugu | Perspective diversity without swarm runtime |
| GLM 5.2 | Multilingual fairness, glossary clarity |

## Options Under Debate

| ID | Proposal | Initial split |
| --- | --- | --- |
| A | Freeze nine core skills; deepen evals | Unanimous yes |
| B | Add `reflective-panel` skill | Unanimous no |
| C | Merge `reflective-brief` into `reflective-dispatch` for L1 | Opus/Codex no; Gemini/Composer yes |
| D | `context_load` frontmatter on skills | Majority yes |
| E | North Star goal statement in README / PROJECT_KNOWLEDGE | Unanimous yes |
| F | Roadmap artifact (this file) | Unanimous yes |
| G | Multi-voice method without new skill | Sakana yes; others aligned after Socratic pass |

## Deliberation Loop

### Round 1 — Socratic challenge

**Q (all):** What problem does merging brief + dispatch solve?

- **Composer:** Friction — users see two skills for "clarify then act."
- **Opus:** Observability — dispatch route trace is the fairness contract; merging hides rigor decisions.
- **Codex:** Testability — ROUTE-001 maps intents to workflows; merging blurs canonical routes.

**Q:** Is a tenth skill the right container for multi-voice debate?

- **Sakana:** Diversity needs explicit structure.
- **Opus:** A skill factory violates promotion gate (three recurrences).
- **GLM:** English-only skill proliferation hurts TW adopters.

**Counterargument (critical thinking):** If we add nothing, users will keep requesting "multi-agent discussion" and spawn external swarms — scope creep by workaround.

**Falsifiability test:** If optional multi-voice in `reflective-research` + dispatch L1 fast path covers 90% of panel requests without new skills, reject `reflective-panel`.

### Round 2 — Proposed compromises

| Conflict | Compromise | Rationale |
| --- | --- | --- |
| C merge vs split | **L1 Fast Path** inside `reflective-dispatch` | Trivial L1 tasks skip separate brief; route trace preserved |
| Multi-voice | **Optional method** in `reflective-research` | Same host, persona lenses, no runtime |
| Eval depth | **CI already runs** `route_paraphrase_eval.py` via `make validate` | Document + keep frozen skill count |
| i18n | **Glossary TW lines** for routing terms | Skills stay English; fairness via normalized intent |

### Round 3 — Agreement check

| Option | Verdict | Action |
| --- | --- | --- |
| A | **Agree** | Record skill-freeze in PROJECT_KNOWLEDGE; keep CI validate |
| B | **Agree reject** | No `reflective-panel`; use research optional method |
| C | **Agree compromise** | L1 Fast Path section in dispatch + cheatsheet |
| D | **Agree** | `context_load` on all nine skills + governance validator |
| E | **Agree** | North Star in README; pointer in PROJECT_KNOWLEDGE |
| F | **Agree** | This file |
| G | **Agree** | Multi-Voice Panel optional method in reflective-research |

**Consensus statement:**

> TeaPrompt remains a **composable harness-policy library** with **nine frozen workflow skills**, **strictness-first routing**, **evidence-backed governance evals**, and **optional single-host multi-voice synthesis** — not a multi-agent runtime.

## Implemented Changes (this session)

- `context_load` frontmatter on all `skills/*/SKILL.md`
- `plans/validate_governance.py` requires `context_load`
- `reflective-dispatch`: L1 Fast Path
- `reflective-research`: Optional Method: Multi-Voice Panel
- `README.md`: North Star + Strictness Before Skills
- `GLOSSARY.md`: Context Load, Route Trace, Enhancement, Silent Downgrade
- `skills/SKILL_TRIGGER_CHEATSHEET.md`: L1 fast path + context_load note

## Stop-Doing List

- No tenth core workflow skill without three cross-session promotion evidence
- No in-repo multi-agent orchestrator, swarm, or async peer messaging
- No mandatory multi-voice panel on every task
- No silent downgrade of rigor for equivalent intent



## Round 4 — Close all residual options (2026-06-25)

### H: Default `reflective-minimality` inside `reflective-implement`?

| Lens | Position |
| --- | --- |
| Opus | Reject default full gate — implement already says smallest safe change |
| Codex | Require signal-based trigger so behavior is falsifiable |
| Gemini | Reject always-on — token cost on one-line fixes |
| Composer | Want anti-bloat, but not a second skill load every time |
| Sakana | N/A — diversity is research-layer, not every patch |
| GLM | Accept signal scan if documented in glossary + TW cheatsheet |

**Socratic Q:** What fails if we default-invoke minimality on every edit?
**Answer:** Trivial L1 fixes pay `medium` context cost; agents over-document cuts.

**Consensus:** **Agree compromise** — add **Minimality Signal Scan** (signal-triggered only); escalate to `reflective-minimality` when disputed. **Reject** mandatory default gate.

### I: ROUTE-002 holdout as merge gate?

| Lens | Position |
| --- | --- |
| All six | **Agree** — fixture exists at 100%; add to `Makefile validate` alongside ROUTE-001 |

**Falsifier:** If holdout drops below 80%, CI fails and router rules need repair.

### J: Localized cues beyond TW cheatsheet?

| Lens | Position |
| --- | --- |
| GLM | README.zh-TW North Star + strictness; cheatsheet TW parity |
| Opus/Codex | **Reject** translating full `SKILL.md` contracts — English remains canonical |
| Gemini/Composer | Cheatsheet + glossary TW lines are enough for L1–L2 |

**Consensus:** **Agree partial** — README.zh-TW + cheatsheet TW updates; **no** full skill localization.

### Round 4 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| H | Default minimality in implement | **Compromise** | Minimality Signal Scan in `reflective-implement` |
| I | ROUTE-002 in CI | **Agree** | Second line in `Makefile validate` |
| J | i18n beyond cheatsheet | **Partial agree** | README.zh-TW + cheatsheet TW; skills stay EN |

**All roles agree.** No further open options from the 2026-06-25 panel.

## Implemented Changes (Round 4)

- `reflective-implement/SKILL.md`: Minimality Signal Scan section
- `Makefile`: ROUTE-002 holdout eval in `validate`
- `README.zh-TW.md`: North Star + Strictness before skills
- `SKILL_TRIGGER_CHEATSHEET.md` + `.zh-TW.md`: multi-voice, minimality scan, L1 fast path, context_load (TW)
- `GLOSSARY.md`: Minimality Signal Scan entry

## Residual Open Questions

_None — panel closed 2026-06-25 after Round 5. Future promotions still require the three-recurrence gate._

## Round 5 — Post-close follow-ups (2026-06-25)

### K: Expand ROUTE-002 with fresh holdout cases?

| Lens | Position |
| --- | --- |
| Codex | **Agree** — add cases before more router tuning; keep deterministic eval |
| Opus | **Agree** — handoff vs workflow-design and multi-voice vs dispatch are real boundaries |
| Gemini | **Agree** — trivial implement vs minimality is cost-relevant |
| Composer | **Agree** — IDE users phrase handoffs and quick fixes inconsistently |
| Sakana | **Agree** — multi-voice holdout validates Round 3 G without new skill |
| GLM | **Agree** — TW adopters need stable routing on session transfer phrasing |

**Socratic Q:** What fails if we tune ROUTE-001 only?
**Answer:** Holdout stops measuring unseen boundaries; regressions hide until manual use.

**Consensus:** **Agree** — add `handoff_holdout`, `multi_voice_research_holdout`, `trivial_implement_holdout` plus router boundary rules. Narrow handoff signals so workflow-design phrases (e.g. "handoff workflow" in a spec) do not misroute.

### L: Operationalize `context_load` at dispatch time?

| Lens | Position |
| --- | --- |
| Gemini | **Agree** — metadata is useless without a deferral rule |
| Opus | **Agree** — must appear in route trace (R7), not silent skip |
| Codex | **Agree** — falsifiable via ROUTING_CONTRACT + dispatch Output fields |
| Composer | **Agree** — L1–L2 hosts need explicit deferral, not guesswork |
| Sakana/GLM | **Agree** — deferral ≠ downgrade when trace is visible |

**Consensus:** **Agree** — `Context Load Deferral` section in `reflective-dispatch`; **R7** in `ROUTING_CONTRACT.md`; cheatsheet + glossary lines.

### M: Run 23-task benchmark eval in CI?

| Lens | Position |
| --- | --- |
| Codex | **Reject** — benchmark needs LLM runs; CI must stay deterministic |
| Opus | **Reject** — promotion gate not met; manual `benchmark_tasks.py` suffices |
| Gemini | **Reject** — cost and flake risk outweigh signal |
| All | **Agree reject** — document manual path only |

**Consensus:** **Reject** — keep `benchmark_tasks.py` manual; no CI job.

### N: QUALITY_GATES still lists "Add CI/CD"?

| Lens | Position |
| --- | --- |
| All six | **Agree** — mark done; `.github/workflows/python-tools.yml` already runs `make all` |

**Consensus:** **Agree** — update QUALITY_GATES Next Steps.

### Round 5 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| K | Fresh ROUTE-002 holdout | **Agree** | 3 new holdout groups + router boundaries |
| L | context_load deferral | **Agree** | dispatch skill + R7 + glossary/cheatsheet |
| M | Benchmark in CI | **Reject** | Manual benchmark only |
| N | CI/CD documentation | **Agree** | QUALITY_GATES update |

**All roles agree.**

## Implemented Changes (Round 5)

- `route-002-holdout-eval.yaml`: handoff, multi-voice research, trivial implement holdouts (58 paraphrases)
- `route_paraphrase_eval.py`: handoff, multi-voice, trivial-implement boundary rules
- `reflective-dispatch/SKILL.md`: Context Load Deferral section
- `ROUTING_CONTRACT.md`: R7 Context Load Deferral
- `GLOSSARY.md`, cheatsheets EN/TW: deferral terms
- `QUALITY_GATES_SUMMARY.md`: CI done, holdout metrics, benchmark manual



## Round 6 — Close deferred follow-ups (2026-06-25)

User directive: run Socratic consensus on **all** remaining deferred items and implement unanimous agreements.

### O: Knowie-style undocumented-decisions git check?

| Lens | Position |
| --- | --- |
| Opus | **Agree compromise** — warning only; mirrors stale-milestone boundary |
| Codex | **Agree** — falsifiable via governance-surface path list + subject cues |
| Gemini | **Agree** — non-blocking; avoids CI flake on every doc edit |
| Composer | **Agree** — helps IDE sessions notice missing Decision Index entries |
| Sakana | **Agree** — drift hint without new skill |
| GLM | **Agree** — TW adopters still read English Decision Index; warning is EN-only OK |

**Socratic Q:** What fails if this blocks CI?
**Answer:** Routine governance commits false-positive; **reject blocking**.

**Consensus:** **Agree compromise** — `_check_undocumented_governance_commits` warning in `validate_project_knowledge.py`.

### P: More ROUTE-002 holdout before router tuning?

| Lens | Position |
| --- | --- |
| All six | **Agree** — add `scaffold_provenance_holdout`, `context_load_defer_holdout`; router boundaries for scaffold + context_load deferral + trivial-fix vs review |

**Consensus:** **Agree** — 66 holdout paraphrases; ROUTE-002 remains 100% after boundary repair.

### Q: Full `SKILL.md` localization?

| Lens | Position |
| --- | --- |
| GLM | Wants parity eventually |
| Opus/Codex/Gemini/Composer/Sakana | **Reject** — English canonical; cheatsheet + glossary sufficient |

**Consensus:** **Reject** — document boundary in `LANGUAGE_POLICY.md` + TW cheatsheet note.

### R: Benchmark eval in CI?

| Lens | Position |
| --- | --- |
| All six | **Reject** full LLM benchmark in CI (Round 5) |
| Codex/Opus | **Compromise** — deterministic `validate_benchmark_fixture.py` in `make validate` |

**Consensus:** **Compromise** — fixture gate in CI; manual `benchmark_tasks.py` execution stays optional.

### Round 6 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| O | Undocumented-decisions check | **Compromise** | Non-blocking warning in project-knowledge validator |
| P | ROUTE-002 expansion | **Agree** | 2 holdout groups + router boundaries |
| Q | Full SKILL i18n | **Reject** | LANGUAGE_POLICY + TW cheatsheet boundary |
| R | Benchmark in CI | **Compromise** | Fixture validator only |

**All roles agree.**

## Implemented Changes (Round 6)

- `validate_project_knowledge.py`: undocumented governance-commit warning
- `validate_benchmark_fixture.py` + `Makefile` validate step
- `route-002-holdout-eval.yaml`: scaffold provenance + context_load defer holdouts
- `route_paraphrase_eval.py`: scaffold, context_load deferral, trivial-fix vs review
- `LANGUAGE_POLICY.md`, `GLOSSARY.md`, `SKILL_TRIGGER_CHEATSHEET.zh-TW.md`
- `QUALITY_GATES_SUMMARY.md`: benchmark fixture section
- Tests: `test_validate_benchmark_fixture.py`, undocumented-commit warnings

## Residual Open Questions (after Round 6)

_Superseded by Round 6 close below._

## Round 7 — Post-close alignment (2026-06-25)

User re-requested full multi-agent Socratic loop. Panel identified residual gaps after Round 6 close: AGENTS.md lacked harness-policy pointers; QUALITY_GATES metrics were stale; zh-TW routing fairness was undocumented in evals.

### T: AGENTS.md harness-policy alignment?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — pointers only; do not duplicate skill contracts in AGENTS |
| Codex | **Agree** — falsifiable via existing `make validate` |
| Gemini | **Agree** — one section; strictness + context_load deferral reference |
| Composer | **Agree** — IDE hosts load AGENTS first; cheatsheet link essential |
| Sakana | **Agree** — multi-voice panel pointer to research method + consensus record |
| GLM | **Agree** — link TW cheatsheet alongside EN |

**Socratic Q:** What fails if we paste full skills into AGENTS?
**Answer:** Dual source of truth; governance drift.

**Consensus:** **Agree** — `Harness Policy (Nine Skills)` section in `06-repo/AGENTS.md`.

### U: Sync stale QUALITY_GATES / holdout metrics?

| Lens | Position |
| --- | --- |
| All six | **Agree** — ROUTE-002 is 25 groups / 76 paraphrases after Rounds 6–7 |

**Consensus:** **Agree** — update `QUALITY_GATES_SUMMARY.md` holdout tracking.

### V: zh-TW ROUTE-002 holdout without full SKILL i18n?

| Lens | Position |
| --- | --- |
| GLM | **Agree compromise** — TW phrases in holdout + router keywords |
| Opus/Codex | **Agree** — intent normalization only; English canonical contracts unchanged |
| Gemini | **Agree** — small keyword set; no translation maintenance burden |
| Composer | **Agree** — cheatsheet TW already covers L1–L2 |
| Sakana | **Agree** — multi-voice TW can wait; per-workflow holdout sufficient |

**Socratic Q:** Does TW holdout replace translated skills?
**Answer:** No — Round 6 Q rejection stands; holdout tests router fairness only.

**Consensus:** **Agree compromise** — nine `zh_tw_*` holdout groups + TW intent keywords in `route_paraphrase_eval.py`.

### W: Re-open SKILL.zh-TW.md companions or tenth skill?

| Lens | Position |
| --- | --- |
| All six | **Reject** — Round 6 Q + skill-freeze A still binding |

**Consensus:** **Reject** — no new skill files; no companion SKILL translations.

### Round 7 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| T | AGENTS harness-policy section | **Agree** | `06-repo/AGENTS.md` pointers |
| U | Metrics sync | **Agree** | QUALITY_GATES holdout counts |
| V | zh-TW holdout + router keywords | **Compromise** | ROUTE-002 + router + glossary |
| W | SKILL.zh-TW / tenth skill | **Reject** | Closed |

**All roles agree.**

## Implemented Changes (Round 7)

- `06-repo/AGENTS.md`: Harness Policy (Nine Skills) section
- `route_paraphrase_eval.py`: Traditional Chinese intent keywords + boundaries
- `route-002-holdout-eval.yaml`: nine `zh_tw_*` holdout groups (76 paraphrases total)
- `QUALITY_GATES_SUMMARY.md`, `LANGUAGE_POLICY.md`, `GLOSSARY.md`
- `SKILL_TRIGGER_CHEATSHEET.zh-TW.md`: ROUTE-002 fairness note
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 7 entry



## Rounds 8–20 — Milestone close and maintenance layer (2026-06-25)

User directive: continue the multi-agent Socratic panel through **Round 20** (options X–AJ), implement unanimous agreements, verify with `make all`.

### Round 8 — X: Close Governance layer maturity milestone?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — evidence-backed gates now run on every change |
| Codex | **Agree** — ROUTE-001/002/003 + governance validators are falsifiable |
| Gemini | **Agree** — mark `done`; retire from Current Direction |
| Composer | **Agree** — operators use `make all`, not ad-hoc checks |
| Sakana | **Agree** — no new runtime; harness policy only |
| GLM | **Agree** — TW fairness covered by holdout, not new skills |

**Socratic Q:** What fails if we leave the milestone `active` forever?
**Answer:** PROJECT_KNOWLEDGE validator warns; direction section stops reflecting real work.

**Consensus:** **Agree** — milestone `done`; record in Decision Index Round 8.

### Round 9 — Y: Close Project judgment layer milestone?

| Lens | Position |
| --- | --- |
| All six | **Agree** — scaffold, authority boundary, promotion contract, and `validate_project_knowledge.py` are shipped |

**Consensus:** **Agree** — milestone `done`; reflow into Decision Index; remove from Current Direction.

### Round 10 — Z: Mixed-language ROUTE-002 holdout?

| Lens | Position |
| --- | --- |
| GLM | **Agree** — EN+zh-TW code-switching is real IDE usage |
| Opus/Codex | **Agree compromise** — one group per workflow; no multi-intent phrases in a single group |
| Gemini | **Agree** — implement + spec-plan holdouts sufficient for v1 |
| Composer | **Agree** — phrases must not embed `clarify`/`review` when expecting implement |
| Sakana | **Agree** — mixed language ≠ multi-voice panel |

**Socratic Q:** Why did an early draft phrase fail routing?
**Answer:** `"clarify 目標後 implement"` correctly routes to brief — group design error, not router bug.

**Consensus:** **Agree** — `mixed_language_implement_holdout` + `mixed_language_plan_holdout` (27 groups / 80 paraphrases).

### Round 11 — AA: CI gate for skill examples?

| Lens | Position |
| --- | --- |
| Codex | **Agree** — deterministic; each skill needs worked examples |
| Opus | **Agree** — complements lint, not replacement |
| All | **Agree** — `validate_skill_examples.py` in `make validate` |

**Consensus:** **Agree** — 9/9 `skills/examples/*.examples.md` with ≥200 chars.

### Round 12 — AB: CONTRIBUTING harness policy?

| Lens | Position |
| --- | --- |
| All six | **Agree** — contributor onboarding must mention nine-skill freeze + `make all` |

**Consensus:** **Agree** — Harness Policy section in root `CONTRIBUTING.md`.

### Round 13 — AC: Root AGENTS harness pointer?

| Lens | Position |
| --- | --- |
| All six | **Agree** — root `AGENTS.md` NOTE block links `06-repo/AGENTS.md` harness section |

**Consensus:** **Agree** — pointer only; no skill duplication.

### Round 14 — AD: Manual benchmark documentation?

| Lens | Position |
| --- | --- |
| All six | **Agree** — CI stays fixture-only; docstring + QUALITY_GATES distinguish manual LLM runs |

**Consensus:** **Agree** — document `validate_benchmark_fixture.py` vs `benchmark_tasks.py`.

### Round 15 — AE: ROUTE-003 adversarial eval?

| Lens | Position |
| --- | --- |
| Codex | **Agree** — fresh boundary phrases separate from ROUTE-001/002 |
| Opus | **Agree** — trivial-fix vs minimality boundary needs adversarial coverage |
| All | **Agree** — third routing gate in CI |

**Consensus:** **Agree** — `route-003-adversarial-eval.yaml` (7 groups / 16 paraphrases); router fix for `one-line bug fix in the repo`.

### Round 16 — AF: Canonical `context_load` enforcement?

| Lens | Position |
| --- | --- |
| Gemini | **Agree** — metadata useless if drift allowed |
| Codex | **Agree** — `CANONICAL_CONTEXT_LOAD` in `validate_governance.py` |
| All | **Agree** — matches dispatch deferral table |

**Consensus:** **Agree** — governance validator rejects non-canonical `context_load`.

### Round 17 — AG: README governance pointer?

| Lens | Position |
| --- | --- |
| All six | **Agree** — README links panel record + `make validate` |

**Consensus:** **Agree** — Governance Panel Record section.

### Round 18 — AH: SKILL_INSTALLATION harness line?

| Lens | Position |
| --- | --- |
| All six | **Agree** — installers see harness policy before copying skills |

**Consensus:** **Agree** — one-line pointer to AGENTS + cheatsheet.

### Round 19 — AI: Glossary maintenance playbook?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — operator checklist, not agent instructions |
| Sakana | **Agree** — holdout-before-tuning rule prevents overfitting |
| All | **Agree** — EN + zh-TW heading in GLOSSARY |

**Consensus:** **Agree** — Governance Maintenance Playbook appendix.

### Round 20 — AJ: Final panel close?

| Lens | Position |
| --- | --- |
| All six | **Agree close** — options A–AJ resolved; no tenth skill; no runtime; no full SKILL i18n |

**Socratic Q:** What remains open?
**Answer:** Recurrence-gated promotions only (`reflective-implement` → minimality default, localized triggers beyond cheatsheet).

**Consensus:** **Agree close** — panel sealed at Round 20; maintenance via playbook.

### Rounds 8–20 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| X | Close governance milestone | **Agree** | PROJECT_KNOWLEDGE `done` + Decision Index |
| Y | Close project-judgment milestone | **Agree** | Retire from Current Direction |
| Z | Mixed-language holdout | **Agree** | ROUTE-002 +2 groups; phrase hygiene |
| AA | Skill examples CI | **Agree** | `validate_skill_examples.py` |
| AB | CONTRIBUTING harness | **Agree** | Root CONTRIBUTING section |
| AC | Root AGENTS pointer | **Agree** | NOTE block link |
| AD | Manual benchmark docs | **Agree** | benchmark_tasks docstring + QUALITY_GATES |
| AE | ROUTE-003 adversarial | **Agree** | YAML + Makefile + router trivial-fix fix |
| AF | Canonical context_load | **Agree** | `validate_governance.py` table |
| AG | README pointer | **Agree** | Governance Panel Record |
| AH | SKILL_INSTALLATION | **Agree** | Harness policy line |
| AI | Maintenance playbook | **Agree** | GLOSSARY appendix |
| AJ | Final close | **Agree** | Panel sealed Round 20 |

**All roles agree.**

## Implemented Changes (Rounds 8–20)

- `PROJECT_KNOWLEDGE.md`: milestones closed; Decision Index Rounds 8–20 entry; Current Direction reflow
- `route-002-holdout-eval.yaml`: `mixed_language_implement_holdout`, `mixed_language_plan_holdout` (80 paraphrases)
- `route-003-adversarial-eval.yaml`: adversarial boundary set (16 paraphrases)
- `route_paraphrase_eval.py`: trivial-fix signals (`one-line`, `bug fix`, `repo`); skip minimality when trivial-fix active
- `validate_skill_examples.py` + tests; `Makefile` validate step
- `validate_governance.py`: `CANONICAL_CONTEXT_LOAD` enforcement
- `CONTRIBUTING.md`, root `AGENTS.md`, `README.md`, `SKILL_INSTALLATION.md`, `GLOSSARY.md`, `QUALITY_GATES_SUMMARY.md`, `benchmark_tasks.py`

## Verification (Rounds 8–20)

- `make all`: **59 pytest** passed; ROUTE-001 **100%**; ROUTE-002 **100%** (27 groups / 80); ROUTE-003 **100%** (7 / 16); governance **9/9**; skill examples **9/9**


## Panel status (updated)

**Superseded — see final seal at Round 35 below.** Was sealed after Round 21 audit (options A–AN). No open implementation blockers from Rounds 8–20. Future promotions still require the three-recurrence gate.

_Ongoing maintenance: [GLOSSARY.md](../GLOSSARY.md) Governance Maintenance Playbook — expand ROUTE-002/003 holdout before router tuning; run `make all`; monitor undocumented-decision warnings._

## Round 21 — Post-Round-20 audit (2026-06-25)

User directive: confirm all panel problems are done or run another Socratic round.

### AK: Open implementation blockers from Rounds 8–20?

| Lens | Position |
| --- | --- |
| Codex | **Agree none** — `make all` green; ROUTE-001/002/003 at 100%; governance 9/9 |
| Opus | **Agree none** — deferred items are promotion-gated, not forgotten work |
| Gemini | **Agree none** — ongoing holdout expansion is maintenance, not a blocker |
| Composer | **Agree none** — doc drift was the real confusion, not missing code |
| Sakana | **Agree none** — multi-voice path covered without tenth skill |
| GLM | **Agree none** — zh-TW fairness covered by holdout + cheatsheet boundary |

**Socratic Q:** What fails if we treat deferred promotions as open bugs?
**Answer:** Scope creep — tenth skill, full i18n, and default minimality re-litigate without recurrence evidence.

**Consensus:** **Agree** — no implementation blockers remain from Rounds 8–20.

### AL: Reclassify “Superseded Open Questions”?

| Lens | Position |
| --- | --- |
| All six | **Agree** — rename to **Recurrence-Gated Backlog**; mark ROUTE-002 CI item **done** |

**Consensus:** **Agree** — backlog table below; not panel blockers.

### AM: QUALITY_GATES Phase 2 drift?

| Lens | Position |
| --- | --- |
| Codex | **Agree** — conclusion still said “open routing item” after ROUTE-002/003 shipped |
| Opus | **Agree** — split Done / Ongoing Maintenance / Recurrence-Gated |
| All | **Agree** — update conclusion to match Round 20 metrics |

**Consensus:** **Agree** — QUALITY_GATES_SUMMARY.md cleanup.

### AN: Decision Index + final seal?

| Lens | Position |
| --- | --- |
| All six | **Agree** — PROJECT_KNOWLEDGE Round 21 audit entry; panel sealed at Round 21 |

**Consensus:** **Agree close** — options A–AN resolved.

### Round 21 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| AK | Implementation blockers | **Agree none** | Record audit; no new code required |
| AL | Backlog reclassification | **Agree** | Recurrence-Gated Backlog table |
| AM | QUALITY_GATES drift | **Agree** | Done / Ongoing / Backlog sections |
| AN | Final seal | **Agree** | Decision Index + panel status |

**All roles agree.**

## Recurrence-Gated Backlog (not panel blockers)

| Item | Status | Gate |
| --- | --- | --- |
| `reflective-implement` default-invokes `reflective-minimality` | **Deferred** | Three cross-session recurrences; signal scan suffices today |
| ROUTE-002 holdout blocks merge | **Done** | In `Makefile validate` since Round 4 |
| Localized trigger cues beyond cheatsheet / glossary | **Deferred** | Adoption signal; English `SKILL.md` stays canonical |
| Tenth core workflow skill | **Rejected** | Promotion gate not met (panel A, W, AJ) |
| Full `SKILL.md` i18n | **Rejected** | Cheatsheet + glossary + router keywords sufficient |
| LLM benchmark in CI | **Rejected** | Fixture gate only; manual `benchmark_tasks.py` |

## Evidence

- Prior decision: Hyperplan / multi-agent planning — no change ([external-adoption-case-studies-2026-06-20.md](external-adoption-case-studies-2026-06-20.md))
- Routing CI: `Makefile` `validate` runs ROUTE-001, ROUTE-002 (80 holdout), ROUTE-003 (16 adversarial) via `route_paraphrase_eval.py`
- Governance: `validate_governance.py` with `CANONICAL_CONTEXT_LOAD`
- Round 21 audit: `make all` — 59 pytest, ROUTE-001/002/003 100%, governance 9/9, skill examples 9/9


## Round 22 — Route fixture hygiene gate (2026-06-25)

User directive: continue Socratic panel for as many rounds as feasible.

### AO: Deterministic `validate_route_fixture.py` in CI?

| Lens | Position |
| --- | --- |
| Codex | **Agree** — mirrors `validate_benchmark_fixture.py`; blocks accidental shrinkage |
| Opus | **Agree** — holdout counts should only grow via explicit constant bumps |
| Gemini | **Agree** — run before expensive paraphrase eval |
| Composer | **Agree** — unique group names + workflow validation |
| Sakana | **Agree** — no new YAML dependency |
| GLM | **Agree** — zh-TW holdout groups protected by minimum counts |

**Socratic Q:** What fails if we skip this gate?
**Answer:** Router tuning could silently delete holdout coverage; regressions hide until manual audit.

**Consensus:** **Agree** — `validate_route_fixture.py` + `Makefile` step before ROUTE evals.

## Round 23 — Brief vs dispatch holdout (2026-06-25)

### AP: Add `brief_vs_dispatch_holdout` to ROUTE-002?

| Lens | Position |
| --- | --- |
| All six | **Agree** — clarify-goal-before-route must not collapse into dispatch |

**Consensus:** **Agree** — 2 phrases; brief boundary reinforcement in router.

## Round 24 — Adversarial dispatch/retro traps (2026-06-25)

### AQ: Expand ROUTE-003 with dispatch-vs-brief and retro-lessons groups?

| Lens | Position |
| --- | --- |
| Codex | **Agree** — separate fixture from ROUTE-002 holdout |
| Opus | **Agree** — retro must not drift to implement when "code" appears nearby |
| All | **Agree** — 2 new adversarial groups, 4 phrases |

**Consensus:** **Agree** — `dispatch_vs_brief_adversarial`, `retro_lessons_adversarial`.

## Round 25 — Router boundary repair (2026-06-25)

### AR: Boundary rules for skill-selection dispatch and retro lessons?

| Lens | Position |
| --- | --- |
| All six | **Agree** — only when new holdout phrases require it |

**Consensus:** **Agree** — dispatch-skill, brief-before-route, retro-lessons boundaries in `route_paraphrase_eval.py`.

## Round 26 — Pytest for fixture gate (2026-06-25)

### AS: `test_validate_route_fixture.py`?

| Lens | Position |
| --- | --- |
| All six | **Agree** — minimum coverage constants tested |

**Consensus:** **Agree** — 3 pytest cases.

## Round 27 — ROUTING_CONTRACT R8 (2026-06-25)

### AT: Codify holdout-before-tune as normative requirement?

| Lens | Position |
| --- | --- |
| Codex | **Agree** — pairs with playbook step 2 |
| Opus | **Agree** — R8 makes maintenance auditable |
| All | **Agree** — R8 in `ROUTING_CONTRACT.md` |

**Consensus:** **Agree** — **R8: Holdout-before-tune**.

## Round 28 — METHODOLOGY_MAP panel pointer (2026-06-25)

### AU: Discoverability for panel record?

| Lens | Position |
| --- | --- |
| Sakana | **Agree** — multi-voice is research method, not runtime |
| All | **Agree** — one section in `METHODOLOGY_MAP.md` |

**Consensus:** **Agree** — Governance Panel Record section.

## Round 29 — zh-TW README pointer (2026-06-25)

### AV: TW adopters need panel link?

| Lens | Position |
| --- | --- |
| GLM | **Agree** — one line under `plans/` |
| All | **Agree** — `README.zh-TW.md` pointer |

**Consensus:** **Agree** — single-line TW pointer; English panel record stays canonical.

## Round 30 — Metrics sync + interim seal (2026-06-25)

### AW: Update QUALITY_GATES metrics and GLOSSARY playbook?

| Lens | Position |
| --- | --- |
| All six | **Agree** — 28/82 and 9/20 metrics; playbook mentions fixture gate |

**Consensus:** **Agree** — metrics + playbook update; interim seal at Round 30 superseded by Round 35 below.

## Round 31 — Tenth skill reaffirm (2026-06-25)

### AX: Re-open tenth core skill?

| Lens | Position |
| --- | --- |
| All six | **Reject** — promotion gate unchanged (A, W, AJ) |

**Consensus:** **Reject** — no tenth skill.

## Round 32 — In-repo swarm reaffirm (2026-06-25)

### AY: Add multi-agent orchestrator?

| Lens | Position |
| --- | --- |
| All six | **Reject** — north star is harness policy, not runtime |

**Consensus:** **Reject** — panel/multi-voice stays inside `reflective-research`.

## Round 33 — Default minimality reaffirm (2026-06-25)

### AZ: Force `reflective-minimality` on every implement?

| Lens | Position |
| --- | --- |
| All six | **Defer** — signal scan sufficient; three-recurrence gate not met |

**Consensus:** **Defer** — recurrence-gated backlog unchanged.

## Round 34 — CONTRIBUTING routing maintenance (2026-06-25)

### BA: Operator checklist in CONTRIBUTING?

| Lens | Position |
| --- | --- |
| Composer | **Agree** — contributors need holdout-before-tune steps |
| All | **Agree** — Routing Maintenance section |

**Consensus:** **Agree** — root `CONTRIBUTING.md` section + R8 link.

## Round 35 — Final extended seal (2026-06-25)

### BB: Close extended panel at Round 35?

| Lens | Position |
| --- | --- |
| All six | **Agree** — options A–BB resolved; maintenance only remains |

**Consensus:** **Agree close** — panel sealed at **Round 35**; Decision Index entry.

### Rounds 22–35 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| AO | Route fixture gate | **Agree** | `validate_route_fixture.py` + Makefile |
| AP | Brief vs dispatch holdout | **Agree** | ROUTE-002 +1 group |
| AQ | Adversarial expansion | **Agree** | ROUTE-003 +2 groups |
| AR | Router boundaries | **Agree** | dispatch/brief/retro boundaries |
| AS | Fixture pytest | **Agree** | `test_validate_route_fixture.py` |
| AT | R8 holdout-before-tune | **Agree** | `ROUTING_CONTRACT.md` |
| AU | METHODOLOGY_MAP pointer | **Agree** | Governance Panel Record |
| AV | README.zh-TW pointer | **Agree** | plans panel link |
| AW | Metrics sync | **Agree** | QUALITY_GATES + GLOSSARY |
| AX | Tenth skill | **Reject** | — |
| AY | Swarm runtime | **Reject** | — |
| AZ | Default minimality | **Defer** | backlog |
| BA | CONTRIBUTING maintenance | **Agree** | Routing Maintenance section |
| BB | Final seal | **Agree** | Panel sealed Round 35 |

**All roles agree.**

## Implemented Changes (Rounds 22–35)

- `validate_route_fixture.py`, `tests/test_validate_route_fixture.py`, `Makefile` validate step
- `route-002-holdout-eval.yaml`: `brief_vs_dispatch_holdout` (82 paraphrases / 28 groups)
- `route-003-adversarial-eval.yaml`: `dispatch_vs_brief_adversarial`, `retro_lessons_adversarial` (20 paraphrases / 9 groups)
- `route_paraphrase_eval.py`: dispatch-skill, brief-before-route, retro-lessons boundaries
- `ROUTING_CONTRACT.md`: R8 Holdout-before-tune
- `METHODOLOGY_MAP.md`, `README.zh-TW.md`, `CONTRIBUTING.md`, `GLOSSARY.md`, `QUALITY_GATES_SUMMARY.md`, `PROJECT_KNOWLEDGE.md`

## Verification (Rounds 22–35)

- `make all`: **62 pytest**, ROUTE-001 **100%** (16 groups / 128), ROUTE-002 **100%** (28 / 82), ROUTE-003 **100%** (9 / 20), governance **9/9**, skill examples **9/9**, route fixture gate **pass**


## Round 36 — Plan-only holdout (2026-06-25)

User directive: continue Socratic panel for as many rounds as feasible.

### BC: Add `plan_only_no_code_holdout` to ROUTE-002?

| Lens | Position |
| --- | --- |
| Codex | **Agree** — "code changes" in plan-only phrasing misroutes without holdout |
| Opus | **Agree** — falsifiable boundary before keyword tuning |
| Gemini | **Agree** — plan-only saves implement context cost |
| Composer | **Agree** — IDE users mix plan + code words casually |
| Sakana | **Agree** — boundary clarity over new skill |
| GLM | **Agree** — TW plan-only phrases need parity |

**Consensus:** **Agree** — ROUTE-002 group + plan-only boundary rule.

## Round 37 — Plain review vs risk (2026-06-25)

### BD: Add `plain_review_not_risk_holdout`?

| Lens | Position |
| --- | --- |
| All six | **Agree** — production keyword false positives on plain PR review |

**Socratic Q:** What fails if every "production" mention routes to risk?
**Answer:** Readability/regression reviews get over-rigor and wrong workflow.

**Consensus:** **Agree** — holdout group + production-negation boundary.

## Round 38 — Router boundary repair (2026-06-25)

### BE: Plan-only and production-negation rules in `route_paraphrase_eval.py`?

| Lens | Position |
| --- | --- |
| All six | **Agree** — holdout added first (R8); then boundary repair |

**Consensus:** **Agree** — `no_code_context` hoist, `production_negated`, `plan_only_signals`, `plain_review_signals`.

## Round 39 — Adversarial implement/research traps (2026-06-25)

### BF: ROUTE-003 `implement_not_plan_trap` and `research_not_brief_trap`?

| Lens | Position |
| --- | --- |
| All six | **Agree** — separate adversarial traps from holdout tuning set |

**Consensus:** **Agree** — +2 ROUTE-003 groups.

## Round 40 — ROUTING_CONTRACT R9 (2026-06-25)

### BG: Codify production-negation and plan-only as normative?

| Lens | Position |
| --- | --- |
| Opus/Codex | **Agree** — contract documents fairness edge cases |
| All | **Agree** — R9 in `ROUTING_CONTRACT.md` |

**Consensus:** **Agree** — R9 added.

## Round 41 — Fixture minimum bump (2026-06-25)

### BH: Raise `validate_route_fixture.py` minimums?

| Lens | Position |
| --- | --- |
| Codex | **Agree** — prevents accidental holdout shrinkage |
| All | **Agree** — ROUTE-002 32/91, ROUTE-003 11/24 |

**Consensus:** **Agree** — minimum constants updated; existing pytest covers.

## Round 42 — zh-TW plan/review holdouts (2026-06-25)

### BI: TW fairness groups for plan-only and plain review?

| Lens | Position |
| --- | --- |
| GLM | **Agree** — 不是正式環境風險 must not force risk workflow |
| All | **Agree** — `zh_tw_plan_only_holdout`, `zh_tw_plain_review_holdout` |

**Consensus:** **Agree**.

## Round 43 — GLOSSARY boundary terms (2026-06-25)

### BJ: Operational definitions for plan-only and plain review?

| Lens | Position |
| --- | --- |
| All six | **Agree** — EN definitions; TW headings in glossary |

**Consensus:** **Agree** — GLOSSARY entries + playbook rounds 1–50.

## Round 44 — Metrics sync (2026-06-25)

### BK: QUALITY_GATES_SUMMARY metrics?

| Lens | Position |
| --- | --- |
| All six | **Agree** — 32/91 and 11/24 |

**Consensus:** **Agree**.

## Round 45 — Decision Index (2026-06-25)

### BL: PROJECT_KNOWLEDGE entry for Rounds 36–50?

| Lens | Position |
| --- | --- |
| All six | **Agree** — single Decision Index pointer |

**Consensus:** **Agree**.

## Round 46 — Cheatsheet cues (2026-06-25)

### BM: SKILL_TRIGGER_CHEATSHEET EN/TW boundary lines?

| Lens | Position |
| --- | --- |
| Composer/GLM | **Agree** — progressive disclosure for adopters |
| All | **Agree** |

**Consensus:** **Agree**.

## Round 47 — Tenth skill reaffirm (2026-06-25)

### BN: Re-open tenth core skill?

| Lens | Position |
| --- | --- |
| All six | **Reject** — promotion gate unchanged |

**Consensus:** **Reject**.

## Round 48 — Benchmark CI reaffirm (2026-06-25)

### BO: LLM benchmark in CI?

| Lens | Position |
| --- | --- |
| All six | **Reject** — fixture gate only |

**Consensus:** **Reject**.

## Round 49 — CONTRIBUTING R8–R9 pointer (2026-06-25)

### BP: Routing maintenance checklist extension?

| Lens | Position |
| --- | --- |
| All six | **Agree** — plan-only/review-vs-risk holdout-before-tune step |

**Consensus:** **Agree**.

## Round 50 — Interim seal (2026-06-25)

**Superseded by Round 65 final seal below.** Was sealed at Round 50 (options A–BQ).

## Round 51 — Brief-before-plan holdout (2026-06-25)

User directive: continue Socratic panel for as many rounds as feasible.

### BR: Add `brief_before_plan_holdout` to ROUTE-002?

| Lens | Position |
| --- | --- |
| All six | **Agree** — scope/alignment before PRD must not misroute to spec-plan |

**Consensus:** **Agree** — 2 phrases; brief-before-plan boundary in router.

## Round 52 — Dependency removal holdout (2026-06-25)

### BS: Add `dependency_removal_holdout`?

| Lens | Position |
| --- | --- |
| All six | **Agree** — dependency removal is minimality, not dispatch |

**Consensus:** **Agree**.

## Round 53 — Design comparison plan-only (2026-06-25)

### BT: Add `design_comparison_plan_holdout`?

| Lens | Position |
| --- | --- |
| GLM | **Agree** — mixed-language 不要寫 code must route to spec-plan |
| All | **Agree** — paper-only API comparison is planning |

**Consensus:** **Agree** — 3 phrases including zh-TW.

## Round 54 — README plain review (2026-06-25)

### BU: Add `readme_plain_review_holdout`?

| Lens | Position |
| --- | --- |
| All six | **Agree** — clarity-not-security must not trigger risk |

**Consensus:** **Agree** — extend production/security negation.

## Round 55 — Router boundary repair (2026-06-25)

### BV: Boundaries for brief/plan/review/dispatch meta?

| Lens | Position |
| --- | --- |
| Codex | **Agree** — dispatch-meta before handoff keyword collision |
| All | **Agree** |

**Consensus:** **Agree** — router boundary pass.

## Round 56 — Adversarial dispatch/brief traps (2026-06-25)

### BW: ROUTE-003 dispatch-meta + brief-not-plan?

| Lens | Position |
| --- | --- |
| All six | **Agree** — skill-catalog questions are dispatch |

**Consensus:** **Agree** — 2 adversarial groups.

## Round 57 — ROUTING_CONTRACT R10 (2026-06-25)

### BX: Codify brief-before-plan norm?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — complements R9 plan-only |
| All | **Agree** |

**Consensus:** **Agree** — R10 in ROUTING_CONTRACT.md.

## Round 58 — Fixture minimums (2026-06-25)

### BY: Bump validate_route_fixture minimums?

| Lens | Position |
| --- | --- |
| Codex | **Agree** — 36/100 and 13/28 |
| All | **Agree** |

**Consensus:** **Agree**.

## Round 59 — Anti-drift pytest (2026-06-25)

### BZ: `test_round_51_boundary_probes`?

| Lens | Position |
| --- | --- |
| All six | **Agree** — lock new boundaries |

**Consensus:** **Agree**.

## Round 60 — GLOSSARY terms (2026-06-25)

### CA: Brief-before-plan + design comparison entries?

| Lens | Position |
| --- | --- |
| GLM | **Agree** — TW fairness for mixed phrases |
| All | **Agree** |

**Consensus:** **Agree**.

## Round 61 — Metrics sync (2026-06-25)

### CB: QUALITY_GATES ROUTE-002/003 counts?

| Lens | Position |
| --- | --- |
| All six | **Agree** — 36 groups / 100 phrases; 13 / 28 |

**Consensus:** **Agree**.

## Round 62 — Decision Index (2026-06-25)

### CC: PROJECT_KNOWLEDGE Round 51–65 entry?

| Lens | Position |
| --- | --- |
| All six | **Agree** |

**Consensus:** **Agree**.

## Round 63 — Tenth skill reaffirm (2026-06-25)

### CD: Re-open tenth core skill?

| Lens | Position |
| --- | --- |
| All six | **Reject** |

**Consensus:** **Reject**.

## Round 64 — Default minimality reaffirm (2026-06-25)

### CE: Force minimality on every implement?

| Lens | Position |
| --- | --- |
| All six | **Defer** — recurrence gate not met |

**Consensus:** **Defer**.

## Round 65 — Final extended seal (2026-06-25)

### CF: Close panel at Round 65?

| Lens | Position |
| --- | --- |
| All six | **Agree** — options A–CF resolved |

**Consensus:** **Agree close** — panel sealed at **Round 65**.

### Rounds 51–65 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| BR | Brief-before-plan holdout | **Agree** | ROUTE-002 group |
| BS | Dependency removal | **Agree** | ROUTE-002 group |
| BT | Design comparison plan | **Agree** | ROUTE-002 + zh-TW |
| BU | README plain review | **Agree** | ROUTE-002 group |
| BV | Router boundaries | **Agree** | brief/plan/review/dispatch-meta |
| BW | Adversarial traps | **Agree** | ROUTE-003 +2 groups |
| BX | R10 contract | **Agree** | ROUTING_CONTRACT.md |
| BY | Fixture minimums | **Agree** | 36/100, 13/28 |
| BZ | Boundary pytest | **Agree** | test_round_51_boundary_probes |
| CA | GLOSSARY | **Agree** | brief-before-plan terms |
| CB | Metrics | **Agree** | QUALITY_GATES_SUMMARY |
| CC | Decision Index | **Agree** | PROJECT_KNOWLEDGE |
| CD | Tenth skill | **Reject** | — |
| CE | Default minimality | **Defer** | backlog |
| CF | Final seal | **Agree** | Panel sealed Round 65 |

**All roles agree.**

## Implemented Changes (Rounds 51–65)

- `route-002-holdout-eval.yaml`: brief-before-plan, dependency removal, design comparison, readme plain review (100 phrases / 36 groups)
- `route-003-adversarial-eval.yaml`: dispatch-meta, brief-not-plan traps (28 phrases / 13 groups)
- `route_paraphrase_eval.py`: brief-before-plan, dependency removal, design comparison, security negation, dispatch-meta
- `validate_route_fixture.py`: minimums 36/100 and 13/28
- `ROUTING_CONTRACT.md`: R10 Brief-before-plan
- `GLOSSARY.md`, `QUALITY_GATES_SUMMARY.md`, `PROJECT_KNOWLEDGE.md`

## Verification (Rounds 51–65)

- `make all`: **64 pytest**, ROUTE-001 **100%** (16/128), ROUTE-002 **100%** (36/100), ROUTE-003 **100%** (13/28)

## Round 66 — Post quick-cue maintenance (2026-06-25)

User directive: **do anything you want** — reopen panel for post-`cb6ea2b` boundary quick-cue governance.

### CG: ROUTING_CONTRACT R12 — boundary quick-cue summary?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — curated quick-cue block is now a contract surface; document curated-not-exhaustive rule |
| Codex | **Agree** — links holdout parity tests to routing contract |
| Gemini | **Agree** — operators need explicit R12 before adding bullets ad hoc |
| Composer | **Agree** — matches R8–R11 maintenance pattern |
| Sakana | **Agree** — no new skill; contract only |
| GLM | **Agree** — zh-TW cheatsheet included in R12 scope |

**Socratic Q:** Does R12 duplicate cheatsheet content?
**Answer:** No — it states *maintenance policy* (curated summary, holdout-first), not trigger cues.

**Consensus:** **Agree** — add R12 to `ROUTING_CONTRACT.md`.

### CH: Probe-linked anti-drift for quick-cue block?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — marker-only tests allow label drift from probe meaning |
| Codex | **Agree** — `BOUNDARY_QUICK_CUE_PROBE_SNIPPETS_*` tied to bullet descriptions |
| Gemini | **Agree** — stronger than bold-label checks alone |
| Composer | **Agree** — extend `test_cheatsheet_boundary_quick_cues.py` |
| Sakana | **Agree** — exported from `test_validate_route_fixture.py` |
| GLM | **Agree** — separate EN/zh-TW snippet tuples |

**Consensus:** **Agree** — probe-snippet pytest guard.

### CI: Expand quick cues (minimality, dispatch-meta, design comparison)?

| Lens | Position |
| --- | --- |
| Opus | **Reject** — seven bullets suffice; skill sections + parity tests cover rest |
| Codex | **Reject** — quick means quick; exhaustive list defeats purpose |
| Gemini | **Defer** — would add three bullets |
| Composer | **Reject** — R12 documents curated subset |
| Sakana | **Reject** — holdout parity tests already guard full cues |
| GLM | **Reject** — zh-TW summary already long enough |

**Socratic Q:** If users miss minimality traps, do we expand quick cues?
**Answer:** Per-skill sections and `test_cheatsheet_boundary_parity.py` already enforce those probes; expand holdout before router tune (R8), not quick-cue list.

**Consensus:** **Reject expansion** — keep seven curated bullets.

### CJ: GLOSSARY + maintenance playbook step?

| Lens | Position |
| --- | --- |
| All six | **Agree** — Boundary Quick Cues section + playbook step 6 |

**Consensus:** **Agree**.

### CK: QUALITY_GATES 7.4 mentions cheatsheet parity tests?

| Lens | Position |
| --- | --- |
| All six | **Agree** — document `test_cheatsheet_boundary_quick_cues.py` + `test_cheatsheet_*_parity.py` |

**Consensus:** **Agree**.

### CL: Re-litigate backlog (tenth skill, default minimality, benchmark CI, full i18n)?

| Lens | Position |
| --- | --- |
| All six | **Reject / Defer unchanged** — recurrence-gated backlog stands |

**Consensus:** **Agree** — no backlog changes.

### Round 66 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| CG | R12 boundary quick-cue contract | **Agree** | `ROUTING_CONTRACT.md` |
| CH | Probe-snippet anti-drift | **Agree** | `test_validate_route_fixture.py` + `test_cheatsheet_boundary_quick_cues.py` |
| CI | Expand quick-cue bullets | **Reject** | Keep curated seven |
| CJ | GLOSSARY + playbook | **Agree** | Boundary Quick Cues + step 6 |
| CK | QUALITY_GATES 7.4 sync | **Agree** | Cheatsheet parity pytest mention |
| CL | Final seal | **Agree** | Panel resealed Round 66 |

**All roles agree.**

## Implemented Changes (Round 66)

- `ROUTING_CONTRACT.md`: R12 Boundary quick-cue summary
- `GLOSSARY.md`: Boundary Quick Cues section; playbook Rounds 1–66 + step 6
- `test_validate_route_fixture.py`: `BOUNDARY_QUICK_CUE_PROBE_SNIPPETS_EN/ZH`
- `test_cheatsheet_boundary_quick_cues.py`: probe-snippet + count anti-drift tests
- `test_glossary_structure.py`: Boundary Quick Cues section + Round 66 reference
- `test_quality_gates_summary.py`: 7.4 cheatsheet parity mention guard
- `QUALITY_GATES_SUMMARY.md`: 7.4 cheatsheet parity bullets

## Verification (Round 66)

- `make all`: pytest + ROUTE-001/002/003 100%



## Round 67 — Contributor doc parity (2026-06-25)

User directive: **do anything you want** — reopen panel for post-Round-66 operator/contributor doc drift.

### CM: CONTRIBUTING Routing Maintenance sync (R8–R12)?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — duplicate step 3 and stale R8–R9 pointer are governance drift |
| Codex | **Agree** — cheatsheet parity belongs in contributor path, not only playbook |
| Gemini | **Agree** — fix numbering before adding steps |
| Composer | **Agree** — IDE contributors read CONTRIBUTING first |
| Sakana | **Agree** — no new skill; doc alignment only |
| GLM | **Agree** — zh-TW cheatsheet parity step explicit |

**Socratic Q:** Does CONTRIBUTING duplicate GLOSSARY playbook?
**Answer:** CONTRIBUTING is the fork/PR entry point; playbook stays operator-deep. Cross-link only.

**Consensus:** **Agree** — fix duplicate step 3; extend to R8–R12; add cheatsheet parity step.

### CN: ROUTING_CONTRACT Related Artifacts expansion?

| Lens | Position |
| --- | --- |
| All six | **Agree** — holdout YAMLs, zh-TW cheatsheet, parity pytest files |

**Consensus:** **Agree**.

### CO: `test_routing_contract.py` anti-drift?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — R8–R12 presence is falsifiable |
| Codex | **Agree** — mirrors `test_quality_gates_summary.py` pattern |
| Gemini | **Agree** — Related Artifacts drift is recurring |
| Composer | **Agree** — low-cost CI guard |
| Sakana | **Agree** — contract structure, not router logic |
| GLM | **Agree** — includes zh-TW cheatsheet artifact |

**Consensus:** **Agree** — structural pytest for R8–R12 + related artifacts.

### CP: Expand ROUTE holdout or tune router?

| Lens | Position |
| --- | --- |
| All six | **Reject** — ROUTE-001/002/003 at 100%; no new boundary evidence |

**Consensus:** **Reject** — maintenance only.

### CQ: GLOSSARY playbook step 7 (CONTRIBUTING alignment)?

| Lens | Position |
| --- | --- |
| All six | **Agree** — step 7 when R8–R12 or cheatsheet steps change |

**Consensus:** **Agree**.

### CR: Re-litigate backlog?

| Lens | Position |
| --- | --- |
| All six | **Unchanged** — recurrence-gated backlog stands |

**Consensus:** **Agree** — no backlog changes.

### Round 67 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| CM | CONTRIBUTING R8–R12 sync | **Agree** | `CONTRIBUTING.md` |
| CN | Related Artifacts expansion | **Agree** | `ROUTING_CONTRACT.md` |
| CO | Contract anti-drift pytest | **Agree** | `test_routing_contract.py` |
| CP | Holdout/router expansion | **Reject** | — |
| CQ | Playbook step 7 | **Agree** | `GLOSSARY.md` |
| CR | Final seal | **Agree** | Panel resealed Round 67 |

**All roles agree.**

## Implemented Changes (Round 67)

- `CONTRIBUTING.md`: Routing Maintenance R8–R12, cheatsheet parity step, fix duplicate numbering
- `ROUTING_CONTRACT.md`: Related Artifacts — holdout YAMLs, zh-TW cheatsheet, parity tests
- `plans/tests/test_routing_contract.py`: R8–R12 + related-artifacts anti-drift
- `GLOSSARY.md`: playbook Rounds 1–67 + step 7
- `test_glossary_structure.py`: Round 67 reference guard
- `PROJECT_KNOWLEDGE.md`: Decision Index entry

## Verification (Round 67)

- `make all`: pytest + ROUTE-001/002/003 100%

## Round 68 — Full-doc drift sync (2026-06-25)

User directive: **review all docs** — reopen six-lens panel for cross-surface drift after Round 67.

### CS: Sync library README panel record?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — "Rounds 1–20" stale; update to Rounds 1–68, options A–CZ |
| Codex | **Agree** — `make all` for verified claims, not `make validate` alone |
| Gemini | **Agree** — entry README is governance discoverability surface |
| Composer | **Agree** — anti-drift via `test_readme_governance.py` |
| Sakana | **Agree** — panel record is historical truth, must track seal round |
| GLM | **Agree** — minimal one-line fix |

**Consensus:** **Agree** — `reflective-prompt-library/README.md` Governance Panel Record.

### CT: Fix METHODOLOGY_MAP.zh-TW skill count?

| Lens | Position |
| --- | --- |
| All six | **Agree** — "8 個生命週期技能" contradicts frozen nine-skill policy |

**Consensus:** **Agree** — update to nine frozen workflow skills.

### CU: Root README North Star + governance pointers?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — root is fork entry; link CONTRIBUTING + panel + playbook |
| Codex | **Agree** — brief North Star, link to library README for depth |
| Gemini | **Agree** — README.zh-TW parity (北極星 + 治理) |
| Composer | **Agree** — do not duplicate full skill tables at root |
| Sakana | **Reject** duplicating panel methodology essay at root |
| GLM | **Agree** — pointers only |

**Consensus:** **Agree** — root `README.md` + `README.zh-TW.md` North Star and governance sections.

### CV: Refresh QUALITY_GATES Phase 2 section?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — "Round 21 audit" header stale after R12 + Round 67 |
| Codex | **Agree** — add doc anti-drift pytest bullet; restore if corrupted |
| Gemini | **Agree** — conclusion should say maintenance mode, not blockers |
| Composer | **Agree** — `test_quality_gates_summary.py` guards Phase 2 header |
| Sakana | **Reject** re-litigating Phase 1 completeness |
| GLM | **Agree** — metrics unchanged; narrative only |

**Consensus:** **Agree** — Phase 2 → post-Round 68 maintenance; anti-drift test mention.

### CW: `test_readme_governance.py`?

| Lens | Position |
| --- | --- |
| All six | **Agree** — guard README round refs, root governance, zh-TW skill count |

**Consensus:** **Agree** — new pytest module.

### CX: Expand ROUTE holdout / tune router?

| Lens | Position |
| --- | --- |
| All six | **Reject** — ROUTE-001/002/003 remain 100% |

**Consensus:** **Reject** — no router changes.

### CY: GLOSSARY playbook `make all` + round bump?

| Lens | Position |
| --- | --- |
| All six | **Agree** — operational test line must match playbook step 1 |

**Consensus:** **Agree** — Rounds 1–68; `make all` in operational test.

### CZ: Final seal?

| Lens | Position |
| --- | --- |
| All six | **Agree** — reseal at Round 68 |

**Consensus:** **Agree close** — panel resealed Round 68.

### Round 68 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| CS | Library README panel sync | **Agree** | Rounds 1–68, `make all` |
| CT | zh-TW methodology map | **Agree** | Nine skills |
| CU | Root README governance | **Agree** | EN + zh-TW North Star |
| CV | QUALITY_GATES Phase 2 | **Agree** | Maintenance narrative |
| CW | README governance pytest | **Agree** | `test_readme_governance.py` |
| CX | Holdout/router expansion | **Reject** | — |
| CY | Playbook make all | **Agree** | `GLOSSARY.md` |
| CZ | Final seal | **Agree** | Panel resealed Round 68 |

**All roles agree.**

## Implemented Changes (Round 68)

- `reflective-prompt-library/README.md`: Governance Panel Record Rounds 1–68
- `METHODOLOGY_MAP.zh-TW.md`: nine frozen workflow skills
- `README.md`, `README.zh-TW.md`: North Star + governance pointers
- `QUALITY_GATES_SUMMARY.md`: Phase 2 post-Round 68 maintenance narrative
- `GLOSSARY.md`: playbook Rounds 1–68; operational test `make all`
- `06-repo/AGENTS.md`: `make all` for verified claims
- `plans/tests/test_readme_governance.py`: README + zh-TW anti-drift
- `test_glossary_structure.py`, `test_quality_gates_summary.py`: Round 68 guards
- `PROJECT_KNOWLEDGE.md`: Decision Index entry

## Verification (Round 68)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Sealed 2026-06-25** after **Round 68** (options A–CZ). Full-doc drift sync complete. Future work remains recurrence-gated maintenance per playbook.

_Ongoing maintenance: [GLOSSARY.md](../GLOSSARY.md) Governance Maintenance Playbook — expand ROUTE-002/003 holdout before `route_paraphrase_eval.py` tuning (R8–R12)._



## Round 69 — Thinking prompt contract review (2026-06-25)

User directive: review prompts, plans, skills, and Socratic/critical-thinking lenses in parallel until all roles agree, then implement.

### DA: Standardize `01-thinking/` prompt contracts?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — eval_harness fails without document-level Purpose/Scope/Acceptance/Falsifiability |
| Codex | **Agree** — map each lens to frozen workflow skills; no tenth skill |
| Gemini | **Agree** — keep zh-TW templates; add English contract outside code block |
| Composer | **Agree** — bounded to five thinking prompts, not all 39 prompts |
| Sakana | **Agree** — aligns with evidence-over-confidence in PROJECT_KNOWLEDGE |
| GLM | **Agree** — skill-map already routes thinking lenses to brief/review |

**Socratic Q:** Does this duplicate skills?
**Answer:** No — prompts are composable lenses; skills are workflow contracts. Purpose sections name routing, not replace SKILL.md.

**Consensus:** **Agree** — add Purpose/Scope/Acceptance Criteria/Falsifiability to all five `01-thinking/` prompts; add `test_thinking_prompts_eval_harness.py`.

### DB: Expand to all prompt categories now?

| Lens | Position |
| --- | --- |
| All six | **Reject** — recurrence-gated; 01-thinking is highest-leverage for this review |

**Consensus:** **Reject** — defer 00-core/02-engineering Purpose sweep.

### Round 69 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| DA | Thinking prompt contracts | **Agree** | 5 files + pytest anti-drift |
| DB | All-category Purpose sweep | **Reject** | backlog |

**All roles agree.**

## Implemented Changes (Round 69)

- `01-thinking/*.md`: Purpose, Scope, Acceptance Criteria, Falsifiability + workflow skill mapping
- `plans/tests/test_thinking_prompts_eval_harness.py`: structural + score floor anti-drift
- `QUALITY_GATES_SUMMARY.md`: 200+ pytest floor; thinking prompt test mention
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 69 entry

## Verification (Round 69)

- `make all`: pytest + ROUTE-001/002/003 100%

## Round 70 — Engineering prompt contract review (2026-06-25)

User directive (repeat): review prompts, plans, skills, and Socratic/critical-thinking lenses in parallel until all roles agree, then implement.

Parallel scouts (PromptScout2, SkillPlanAuditor, SocraticLens) confirmed Round 69 closed `01-thinking/`; highest remaining eval_harness gap is `02-engineering/` (8 prompts scoring ~50–67% before contracts).

### DC: Standardize `02-engineering/` prompt contracts?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — execution prompts must name workflow skills like thinking lenses |
| Codex | **Agree** — mirrors Round 69 pattern; avoid `production`/`auth` in preamble (eval_harness risk false positives) |
| Gemini | **Agree** — links engineering prompts to brief/spec-plan/implement/review surfaces |
| Composer | **Agree** — bounded eight-file batch + pytest anti-drift |
| Sakana | **Agree** — closes thinking→engineering handoff gap without router changes |
| GLM | **Agree** — pair code-reviewer with `01-thinking/critical-thinking-check.md` |

**Socratic Q:** Why engineering before 00-core?
**Answer:** Skills and benchmark tasks route through engineering execution; thinking contracts already done in Round 69.

**Consensus:** **Agree** — add Purpose/Scope/Acceptance Criteria/Falsifiability (+ Human Review where eval_harness risk triggers) to all eight `02-engineering/` prompts; add `test_engineering_prompts_eval_harness.py`.

### DD: Expand to 00-core / 03–05 categories now?

| Lens | Position |
| --- | --- |
| All six | **Reject** — recurrence-gated; engineering batch is highest leverage |

**Consensus:** **Reject** — defer remaining prompt categories.

### DE: Router / holdout / tenth skill?

| Lens | Position |
| --- | --- |
| All six | **Reject** — ROUTE-001/002/003 at 100%; nine-skill freeze holds |

### Round 70 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| DC | Engineering prompt contracts | **Agree** | 8 files + pytest anti-drift |
| DD | All remaining prompt categories | **Reject** | backlog |
| DE | Router/holdout/tenth skill | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 70)

- `02-engineering/*.md`: Purpose, Scope, Acceptance Criteria, Falsifiability + workflow skill mapping; Human Review where required
- `plans/tests/test_engineering_prompts_eval_harness.py`: structural + 80%+ score floor anti-drift
- `QUALITY_GATES_SUMMARY.md`: engineering prompt test mention; pytest floor 220+
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 70 entry

## Verification (Round 70)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

## Round 71 — Thinking ↔ engineering cross-link review (2026-06-25)

User directive (repeat): review prompts, plans, skills, and Socratic/critical-thinking lenses in parallel until all roles agree, then implement.

Parallel scouts (**SocraticLens**, **PromptScout2**, **SkillPlanAuditor**) after Round 70.

### DF: Complete thinking ↔ engineering cross-links?

| Lens | Position |
| --- | --- |
| Sakana | **Agree** — Socratic lenses must be discoverable from engineering prompts |
| Opus | **Agree** — bidirectional Prompt Sources closes the epistemic loop |
| Codex | **Agree** — anti-drift test with explicit mapping table |
| Gemini | **Agree** — low-cost doc pass; no router change |
| Composer | **Agree** — IDE users follow engineering prompts first |
| GLM | **Agree** — English canonical links; zh-TW bodies unchanged |

**Socratic Q:** What fails if we only link thinking → workflow (Round 69) but not engineering → thinking?
**Answer:** Hosts load engineering templates without reaching falsifiability / Socratic lenses.

**Consensus:** **Agree** — all 8 `02-engineering/` prompts name `01-thinking/` lenses; add thinking refs to `reflective-implement`, `reflective-spec-plan`, `reflective-handoff-retro` Prompt Sources; `test_prompt_cross_links.py` anti-drift.

### DG: 00-core Purpose sweep now?

| Lens | Position |
| --- | --- |
| All six | **Reject** — recurrence-gated; cross-link pass is bounded |

### DH: Skill frontmatter pytest suite (SkillPlanAuditor)?

| Lens | Position |
| --- | --- |
| Codex | **Defer** — `validate_governance.py` already enforces context_load in `make validate` |
| Opus | **Defer** — mirror in pytest only after a governance regression |

**Consensus:** **Defer** — no duplicate validator tests this round.

### Round 71 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| DF | Thinking ↔ engineering cross-links | **Agree** | 8 engineering + 3 skills + pytest |
| DG | 00-core Purpose sweep | **Reject** | backlog |
| DH | Skill frontmatter pytest | **Defer** | recurrence-gated |

**All roles agree.**

## Implemented Changes (Round 71)

- `02-engineering/*.md`: `01-thinking/` lens links in Purpose for all 8 prompts
- `skills/reflective-implement`, `reflective-spec-plan`, `reflective-handoff-retro`: thinking Prompt Sources
- `plans/tests/test_prompt_cross_links.py`: explicit cross-link anti-drift
- `QUALITY_GATES_SUMMARY.md`: cross-link test mention; pytest floor 240+
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 71 entry

## Verification (Round 71)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 71** (options DF–DH). Thinking ↔ engineering cross-link pass complete; 00-core Purpose sweep remains recurrence-gated.

## Round 72 — Core prompt contract review (2026-06-25)

User directive (repeat): review prompts, plans, skills, and Socratic/critical-thinking lenses in parallel until all roles agree, then implement.

### DI: Standardize `00-core/` prompt contracts?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — host-instruction layer is highest install surface; contracts prevent silent rigor downgrade |
| Codex | **Agree** — eval_harness scores 50–67% without preamble; falsifiable via pytest |
| Gemini | **Agree** — bounded to nine files; defer 03–05 |
| Composer | **Agree** — IDE users paste core prompts into host settings |
| Sakana | **Agree** — links brief/dispatch + thinking lenses without new skill |
| GLM | **Agree** — English contracts outside zh-TW fences per LANGUAGE_POLICY |

**Socratic Q:** Why 00-core before 03-context?
**Answer:** Installed host instructions affect every task; context prompts are composable overlays.

**Consensus:** **Agree** — Purpose/Scope/Acceptance Criteria/Falsifiability on all nine `00-core/` prompts; `test_core_prompts_eval_harness.py`.

### DJ: Expand to 03–05 categories now?

| Lens | Position |
| --- | --- |
| All six | **Reject** — recurrence-gated after core layer |

### DK: Router / holdout / tenth skill?

| Lens | Position |
| --- | --- |
| All six | **Reject** — ROUTE-001/002/003 at 100%; nine-skill freeze holds |

### Round 72 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| DI | Core prompt contracts | **Agree** | 9 files + pytest anti-drift |
| DJ | 03–05 Purpose sweep | **Reject** | backlog |
| DK | Router/holdout/tenth skill | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 72)

- `00-core/*.md`: Purpose, Scope, Acceptance Criteria, Falsifiability + workflow skill mapping; thinking lens links where applicable
- `plans/tests/test_core_prompts_eval_harness.py`: structural + 80%+ score floor anti-drift
- `QUALITY_GATES_SUMMARY.md`: core prompt test mention; pytest floor 260+
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 72 entry

## Verification (Round 72)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 72** (options DI–DK). Core-prompt contract pass complete; 03–05 Purpose sweep remains recurrence-gated.



## Round 73 — Agent prompt contract review (2026-06-25)

User directive (repeat): review prompts, plans, skills, and Socratic/critical-thinking lenses in parallel until all roles agree, then implement.

### DL: Standardize `04-agent/` prompt contracts + cross-links?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — agent layer was disconnected (50–64% eval_harness); contracts + skill mapping close the gap |
| Codex | **Agree** — nine files bounded; falsifiable via `test_agent_prompts_eval_harness.py` + cross-link pytest |
| Gemini | **Agree** — defer 03-context/05-domain; agent prompts are highest orchestration surface |
| Composer | **Agree** — runtime-trust-boundary already cited in PROJECT_KNOWLEDGE; reciprocal links needed |
| Sakana | **Agree** — no tenth skill; supporting lenses for existing nine |
| GLM | **Agree** — English contracts outside zh-TW fences; Human Review sections where eval risk triggers |

**Socratic Q:** Why 04-agent before 03-context?
**Answer:** Agent prompts define orchestration, trust boundaries, and workflow selection — they bridge thinking lenses and frozen skills.

**Consensus:** **Agree** — Purpose/Scope/Acceptance Criteria/Falsifiability on all nine `04-agent/` prompts; thinking + workflow cross-links; `test_agent_prompts_eval_harness.py`; extend `test_prompt_cross_links.py`.

### DM: Expand to 03-context / 05-domain now?

| Lens | Position |
| --- | --- |
| All six | **Reject** — recurrence-gated after agent layer |

### DN: Router / holdout / tenth skill?

| Lens | Position |
| --- | --- |
| All six | **Reject** — ROUTE-001/002/003 at 100%; nine-skill freeze holds |

### Round 73 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| DL | Agent prompt contracts + cross-links | **Agree** | 9 files + pytest anti-drift |
| DM | 03-context / 05-domain Purpose sweep | **Reject** | backlog |
| DN | Router/holdout/tenth skill | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 73)

- `04-agent/*.md`: Purpose, Scope, Acceptance Criteria, Falsifiability + workflow skill mapping; thinking lens links; Human Review where applicable
- `plans/tests/test_agent_prompts_eval_harness.py`: structural + 80%+ score floor anti-drift
- `plans/tests/test_prompt_cross_links.py`: agent ↔ thinking ↔ skill cross-links
- `QUALITY_GATES_SUMMARY.md`: agent prompt test mention; pytest floor 290+
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 73 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 73 sync

## Verification (Round 73)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

## Round 74 — Context prompt contract review (2026-06-25)

User directive (repeat): review prompts, plans, skills, and Socratic/critical-thinking lenses in parallel until all roles agree, then implement.

### DO: Standardize `03-context/` prompt contracts + cross-links?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — context layer was 50–67% eval_harness; contracts close the recurrence-gated gap from Round 73 |
| Codex | **Agree** — seven files bounded; falsifiable via `test_context_prompts_eval_harness.py` + cross-link pytest |
| Gemini | **Agree** — window-size and handoff prompts are cost-critical; defer 05-domain |
| Composer | **Agree** — IDE users load context prompts with skills; reciprocal links needed |
| Sakana | **Agree** — no tenth skill; supporting lenses for existing nine |
| GLM | **Agree** — English contracts outside zh-TW fences; Human Review where eval risk triggers |

**Socratic Q:** Why 03-context now?
**Answer:** Round 73 deferred it; context discipline and handoff are prerequisites for strictness routing and session continuity.

**Consensus:** **Agree** — Purpose/Scope/Acceptance Criteria/Falsifiability on all seven `03-context/` prompts; thinking + workflow cross-links; `test_context_prompts_eval_harness.py`; extend `test_prompt_cross_links.py`.

### DP: Expand to `05-domain/` now?

| Lens | Position |
| --- | --- |
| All six | **Reject** — recurrence-gated after context layer |

### DQ: Router / holdout / tenth skill?

| Lens | Position |
| --- | --- |
| All six | **Reject** — ROUTE-001/002/003 at 100%; nine-skill freeze holds |

### Round 74 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| DO | Context prompt contracts + cross-links | **Agree** | 7 files + pytest anti-drift |
| DP | 05-domain Purpose sweep | **Reject** | backlog |
| DQ | Router/holdout/tenth skill | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 74)

- `03-context/*.md`: Purpose, Scope, Acceptance Criteria, Falsifiability + workflow skill mapping; thinking lens links; Human Review where applicable
- `plans/tests/test_context_prompts_eval_harness.py`: structural + 80%+ score floor anti-drift
- `plans/tests/test_prompt_cross_links.py`: context ↔ thinking ↔ skill cross-links
- `QUALITY_GATES_SUMMARY.md`: context prompt test mention; pytest floor 330+
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 74 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 74 sync

## Verification (Round 74)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

## Round 75 — Domain prompt contract review (2026-06-25)

User directive (repeat): review prompts, plans, skills, and Socratic/critical-thinking lenses in parallel until all roles agree, then implement.

### DR: Standardize `05-domain/` prompt contracts + cross-links?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — domain overlays were disconnected (58–64% eval_harness); contracts close the last prompt-category gap |
| Codex | **Agree** — seven files bounded; falsifiable via `test_domain_prompts_eval_harness.py` + cross-link pytest |
| Gemini | **Agree** — strategy/risk/research overlays are L6 surfaces; defer `06-repo` templates |
| Composer | **Agree** — high-risk and research prompts already cited in skills; reciprocal links needed |
| Sakana | **Agree** — no tenth skill; supporting lenses for existing nine |
| GLM | **Agree** — English contracts outside zh-TW fences; Human Review on high-risk and creative brand outputs |

**Socratic Q:** Why `05-domain` before `06-repo`?
**Answer:** Domain overlays compose with frozen workflow skills; repo templates are host-install artifacts with different governance surface.

**Consensus:** **Agree** — Purpose/Scope/Acceptance Criteria/Falsifiability on all seven `05-domain/` prompts; thinking + workflow cross-links; `test_domain_prompts_eval_harness.py`; extend `test_prompt_cross_links.py`.

### DS: Expand to `06-repo/` Purpose sweep now?

| Lens | Position |
| --- | --- |
| All six | **Reject** — recurrence-gated; repo templates are install scaffolds not composable prompt contracts |

### DT: Router / holdout / tenth skill?

| Lens | Position |
| --- | --- |
| All six | **Reject** — ROUTE-001/002/003 at 100%; nine-skill freeze holds |

### Round 75 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| DR | Domain prompt contracts + cross-links | **Agree** | 7 files + pytest anti-drift |
| DS | 06-repo Purpose sweep | **Reject** | backlog |
| DT | Router/holdout/tenth skill | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 75)

- `05-domain/*.md`: Purpose, Scope, Acceptance Criteria, Falsifiability + workflow skill mapping; thinking lens links; Human Review where applicable
- `plans/tests/test_domain_prompts_eval_harness.py`: structural + 80%+ score floor anti-drift
- `plans/tests/test_prompt_cross_links.py`: domain ↔ thinking ↔ skill cross-links
- `QUALITY_GATES_SUMMARY.md`: domain prompt test mention; pytest floor update
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 75 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 75 sync

## Verification (Round 75)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

## Round 76 — Repository template contract review (2026-06-25)

User directive (repeat): review prompts, plans, skills, and Socratic/critical-thinking lenses in parallel until all roles agree, then implement.

### DU: Standardize `06-repo/` prompt contracts + cross-links?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — host-install templates are the last unstructured prompt layer; AGENTS.md is canonical harness surface |
| Codex | **Agree** — four files bounded; falsifiable via `test_repo_prompts_eval_harness.py` + cross-link pytest |
| Gemini | **Agree** — IDE/Codex templates are cost-relevant entry points; defer governance pytest mirrors |
| Composer | **Agree** — AGENTS harness policy already cited; contract headers close eval_harness gap |
| Sakana | **Agree** — no tenth skill; repo templates support existing nine |
| GLM | **Agree** — English contracts outside localized fences; Human Review on high-blast-radius templates |

**Socratic Q:** Why `06-repo` after `05-domain`?
**Answer:** Repo templates are host-install artifacts with distinct authority boundaries (`AGENTS.md` vs `PROJECT_KNOWLEDGE.md`); completing them finishes the prompt-library contract sweep.

**Consensus:** **Agree** — Purpose/Scope/Acceptance Criteria/Falsifiability on all four `06-repo/` templates; thinking + workflow cross-links; `test_repo_prompts_eval_harness.py`; extend `test_prompt_cross_links.py`; preserve existing Harness Policy section in AGENTS.md.

### DV: Governance pytest mirrors (`validate_links`, `validate_governance`, `lint_skills`) now?

| Lens | Position |
| --- | --- |
| All six | **Reject** — recurrence-gated (option DH); `make validate` already covers these |

### DW: Router / holdout / tenth skill?

| Lens | Position |
| --- | --- |
| All six | **Reject** — ROUTE-001/002/003 at 100%; nine-skill freeze holds |

### Round 76 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| DU | Repo template contracts + cross-links | **Agree** | 4 files + pytest anti-drift |
| DV | Governance pytest mirrors | **Reject** | backlog (DH) |
| DW | Router/holdout/tenth skill | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 76)

- `06-repo/*.md`: Purpose, Scope, Acceptance Criteria, Falsifiability + workflow skill mapping; thinking lens links; Human Review where applicable
- `plans/tests/test_repo_prompts_eval_harness.py`: structural + 80%+ score floor anti-drift; AGENTS harness-policy guard
- `plans/tests/test_prompt_cross_links.py`: repo ↔ thinking ↔ skill cross-links
- `QUALITY_GATES_SUMMARY.md`: repo prompt test mention; pytest floor 400+
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 76 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 76 sync

## Verification (Round 76)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 76** (options DU–DW). Repository-template contract pass complete; full prompt-library contract sweep (`00-core`–`06-repo`) finished. Governance pytest mirrors remain recurrence-gated.

## Round 77 — Governance pytest mirrors (2026-06-25)

User directive (repeat): review prompts, plans, skills, and Socratic/critical-thinking lenses in parallel until all roles agree, then implement.

### DX: Pytest mirrors for `validate_governance`, `validate_links`, `lint_skills`?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — `CANONICAL_CONTEXT_LOAD` table must be pytest-guarded; mirrors catch drift before `make validate` |
| Codex | **Agree** — negative fixtures falsify without duplicating validator logic; live-repo smoke tests |
| Gemini | **Agree** — context_load deferral is cost-relevant; pytest mirrors are cheap |
| Composer | **Agree** — IDE sessions edit SKILL frontmatter; mirrors close DH backlog |
| Sakana | **Agree** — no tenth skill; mirrors protect existing nine |
| GLM | **Agree** — English canonical metadata; TW routing unaffected |

**Socratic Q:** Why mirrors now after Round 76 rejected DV?
**Answer:** Full prompt-library contract sweep is complete; user re-triggered panel cycle; recurrence gate for DH backlog is satisfied.

**Consensus:** **Agree** — add `test_validate_governance.py`, `test_validate_links.py`, `test_lint_skills.py` with live-repo pass checks + negative tmp_path cases; sync QUALITY_GATES pytest floor.

### DY: Router / holdout / tenth skill?

| Lens | Position |
| --- | --- |
| All six | **Reject** — ROUTE-001/002/003 at 100%; nine-skill freeze holds |

### DZ: LLM benchmark in CI?

| Lens | Position |
| --- | --- |
| All six | **Reject** — manual `benchmark_tasks.py` only (Rounds 5–6) |

### Round 77 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| DX | Governance pytest mirrors | **Agree** | 3 test modules + QUALITY_GATES sync |
| DY | Router/holdout/tenth skill | **Reject** | no change |
| DZ | LLM benchmark in CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 77)

- `plans/tests/test_validate_governance.py`: `CANONICAL_CONTEXT_LOAD` parity + live 9/9 pass + negative fixtures
- `plans/tests/test_validate_links.py`: live-repo zero errors + broken link / frontmatter negatives
- `plans/tests/test_lint_skills.py`: live-repo zero lint errors + nine SKILL.md detection + negative fixture
- `QUALITY_GATES_SUMMARY.md`: governance mirror tests; pytest floor 410+
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 77 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 77 sync

## Verification (Round 77)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 77** (options DX–DZ). Governance validator pytest mirrors complete; prompt-library contract sweep and governance anti-drift suite closed. Holdout expansion before router tuning remains recurrence-gated maintenance.

## Round 78 — Workflow skill thinking cross-links (2026-06-25)

User directive (repeat): review prompts, plans, skills, and Socratic/critical-thinking lenses in parallel until all roles agree, then implement.

### EA: Complete all nine workflow skill ↔ thinking-lens cross-links?

| Lens | Position |
| --- | --- |
| Opus | **Agree** — Round 71 covered three skills; remaining six leave Socratic/critical lenses untested |
| Codex | **Agree** — `SKILL_THINKING_SOURCES` parity with `CORE_SKILLS` is falsifiable |
| Gemini | **Agree** — dispatch/brief/minimality lenses are cost-relevant entry points |
| Composer | **Agree** — IDE users load skills with thinking lenses; reciprocal Prompt Sources required |
| Sakana | **Agree** — research multi-voice method needs explicit socratic + critical-thinking links |
| GLM | **Agree** — English canonical links; TW routing unaffected |

**Socratic Q:** Why skills after prompt contract sweep?
**Answer:** Skills are the harness-policy layer; thinking lenses must be traceable from every workflow skill Prompt Sources, not only implement/spec-plan/handoff.

**Consensus:** **Agree** — extend `SKILL_THINKING_SOURCES` to all nine skills; add missing `reflective-research` Prompt Sources links; `test_all_workflow_skills_have_thinking_cross_link`.

### EB: Skill Module Contract anti-drift for all nine skills?

| Lens | Position |
| --- | --- |
| All six | **Agree** — `lint_skills.py` warnings are not pytest-gated; bounded Trigger/Methods/Output/Never test |

**Consensus:** **Agree** — `test_skill_module_contract.py` for all `CORE_SKILLS`.

### EC: ROUTE-002/003 holdout expansion now?

| Lens | Position |
| --- | --- |
| All six | **Defer** — maintenance playbook item; this round targets skill ↔ thinking linkage |

### ED: Router / holdout / tenth skill / benchmark CI?

| Lens | Position |
| --- | --- |
| All six | **Reject** — unchanged |

### Round 78 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| EA | Nine-skill thinking cross-links | **Agree** | SKILL_THINKING_SOURCES + research Prompt Sources |
| EB | Module Contract anti-drift | **Agree** | `test_skill_module_contract.py` |
| EC | Holdout expansion | **Defer** | maintenance |
| ED | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 78)

- `skills/reflective-research/SKILL.md`: add `01-thinking/socratic-reviewer.md` + `critical-thinking-check.md` to Prompt Sources
- `plans/tests/test_prompt_cross_links.py`: `SKILL_THINKING_SOURCES` covers all nine `CORE_SKILLS`; lens file existence test
- `plans/tests/test_skill_module_contract.py`: Module Contract + Trigger/Methods/Output/Never anti-drift
- `QUALITY_GATES_SUMMARY.md`: skill cross-link + module contract tests; pytest floor 430+
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 78 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 78 sync

## Verification (Round 78)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 78** (options EA–ED). Nine-skill thinking-lens cross-link pass complete; Module Contract anti-drift closed for core skills. Holdout expansion remains recurrence-gated maintenance.

---

## Round 79 — Bidirectional thinking-lens ↔ workflow skill cross-links (2026-06-25)

**Options EE–EH** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 79 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| EE | Bidirectional thinking-lens ↔ workflow-skill links (`01-thinking/` Purpose lists consumer skills; pytest inverts `SKILL_THINKING_SOURCES`) | **Agree** |
| EF | Escalation subsection anti-drift (`lint_skills` suggestion only today) | **Defer** |
| EG | ROUTE holdout expansion | **Defer** |
| EH | Router / tenth skill / benchmark CI | **Reject** |

### Round 79 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| EE | Bidirectional cross-links | **Agree** | Purpose preambles + reciprocal pytest |
| EF | Escalation anti-drift | **Defer** | maintenance |
| EG | Holdout expansion | **Defer** | maintenance |
| EH | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 79)

- `01-thinking/socratic-reviewer.md`, `counterargument.md`, `critical-thinking-check.md`, `why-what-how-done.md`: Purpose preambles list primary consumer workflow skills
- `plans/tests/test_prompt_cross_links.py`: `THINKING_LENS_SKILL_CONSUMERS` + `test_thinking_lens_preamble_lists_consumer_skills` reciprocal anti-drift
- `GLOSSARY.md`: playbook Rounds 1–79; step 10 for reciprocal cross-links
- `QUALITY_GATES_SUMMARY.md`: 440+ pytest floor; reciprocal cross-link note; panel Rounds 1–79
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 79 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 79 sync

## Verification (Round 79)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 79** (options EE–EH). Bidirectional thinking-lens ↔ workflow skill cross-links complete; reciprocal pytest guards Purpose preambles. Holdout expansion and Escalation subsection anti-drift remain recurrence-gated maintenance.

---

## Round 80 — Escalation subsection anti-drift + thinking-lens preamble guards (2026-06-25)

**Options EI–EL** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 80 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| EI | Escalation subsection anti-drift for all nine `SKILL.md` Module Contracts + canonical `Escalation:` format on `reflective-minimality` | **Agree** |
| EJ | Require `Primary workflow surfaces` on all `01-thinking/` lenses + consumer-map completeness pytest | **Agree** |
| EK | ROUTE holdout expansion | **Defer** |
| EL | Router / tenth skill / benchmark CI | **Reject** |

### Round 80 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| EI | Escalation anti-drift | **Agree** | `test_skill_module_contract.py` + minimality format |
| EJ | Thinking-lens preamble guards | **Agree** | `test_thinking_prompts_eval_harness.py` + consumer-map test |
| EK | Holdout expansion | **Defer** | maintenance |
| EL | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 80)

- `skills/reflective-minimality/SKILL.md`: canonical `Output:` / `Never:` / `Escalation:` Module Contract subsections
- `plans/tests/test_skill_module_contract.py`: require `Escalation` alongside Trigger/Methods/Output/Never
- `plans/tests/test_thinking_prompts_eval_harness.py`: `Primary workflow surfaces` preamble guard
- `plans/tests/test_prompt_cross_links.py`: `test_all_thinking_lenses_tracked_in_consumer_map`
- `GLOSSARY.md`: playbook Rounds 1–80; step 11 for Module Contract Escalation upkeep
- `QUALITY_GATES_SUMMARY.md`: Escalation anti-drift note; panel Rounds 1–80
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 80 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 80 sync

## Verification (Round 80)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 80** (options EI–EL). Module Contract Escalation anti-drift closed; thinking-lens preamble consumer guards complete. Holdout expansion remains recurrence-gated maintenance.

---

## Round 81 — Thinking-lens Human Review + Escalation route-target guards (2026-06-25)

**Options EM–EP** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 81 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| EM | `## Human Review` preamble on all `01-thinking/` lenses + pytest | **Agree** |
| EN | Escalation route-target anti-drift (`reflective-*` cites only `CORE_SKILLS`; terminal `reflective-risk` exempt) | **Agree** |
| EO | ROUTE holdout expansion | **Defer** |
| EP | Router / tenth skill / benchmark CI | **Reject** |

### Round 81 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| EM | Human Review on thinking lenses | **Agree** | preamble + `test_thinking_prompt_has_human_review_section` |
| EN | Escalation route targets | **Agree** | `test_core_skill_escalation_routes_to_valid_workflow_skills` |
| EO | Holdout expansion | **Defer** | maintenance |
| EP | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 81)

- `01-thinking/socratic-reviewer.md`, `why-what-how-done.md`: `## Human Review` preamble routes to `reflective-risk`
- `plans/tests/test_thinking_prompts_eval_harness.py`: Human Review preamble guard on all five lenses
- `plans/tests/test_skill_module_contract.py`: Escalation route-target guard; `reflective-risk` terminal-gate exemption
- `GLOSSARY.md`: playbook Rounds 1–81; steps 12–13 for Human Review + Escalation route targets
- `QUALITY_GATES_SUMMARY.md`: 450+ pytest floor; Human Review / Escalation route notes; panel Rounds 1–81
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 81 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 81 sync

## Verification (Round 81)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 81** (options EM–EP). Thinking-lens Human Review preambles complete; Escalation route-target anti-drift closed. Holdout expansion remains recurrence-gated maintenance.


---

## Round 82 — Strict Primary workflow surfaces graph parity (2026-06-25)

**Options EQ–ET** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 82 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| EQ | Strict `Primary workflow surfaces` ↔ `SKILL_THINKING_SOURCES` parity + preamble trim + pytest | **Agree** |
| ER | Expand skill Prompt Sources to match narrative overlisting | **Reject** |
| ES | ROUTE holdout expansion | **Defer** |
| ET | Router / tenth skill / benchmark CI | **Reject** |

### Round 82 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| EQ | Primary surfaces exact graph | **Agree** | trim preambles + `test_thinking_lens_primary_surfaces_match_consumer_graph` |
| ER | Expand graph to match prose | **Reject** | `SKILL_THINKING_SOURCES` stays authoritative from skill Prompt Sources |
| ES | Holdout expansion | **Defer** | maintenance |
| ET | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 82)

- `01-thinking/counterargument.md`, `socratic-reviewer.md`, `why-what-how-done.md`: Primary workflow surfaces trimmed to graph consumers; adjacent workflow notes moved to Scope
- `plans/tests/test_prompt_cross_links.py`: `_primary_workflow_surfaces_skills` + `test_thinking_lens_primary_surfaces_match_consumer_graph`
- `GLOSSARY.md`: playbook Rounds 1–82; step 14 for strict primary-surfaces parity
- `QUALITY_GATES_SUMMARY.md`: primary-surfaces parity note; panel Rounds 1–82
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 82 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 82 sync

## Verification (Round 82)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 82** (options EQ–ET). Thinking-lens Primary workflow surfaces now match the inverted skill graph exactly. Holdout expansion remains recurrence-gated maintenance.

---

## Round 83 — Composable prompt Primary workflow surface parity (2026-06-25)

**Options EU–EX** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 83 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| EU | Strict `Primary workflow surface(s)` ↔ `*_SKILL_LINKS` parity for `02-engineering`–`06-repo` + engineering trim + pytest | **Agree** |
| EV | Supporting-lens exemption for `runtime-trust-boundary.md` (no Primary line) | **Agree** |
| EW | ROUTE holdout expansion | **Defer** |
| EX | Router / tenth skill / benchmark CI | **Reject** |

### Round 83 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| EU | Composable primary-surface parity | **Agree** | `ENGINEERING_SKILL_LINKS` + category primary tests; trim engineering escalations to Scope |
| EV | Supporting lens pattern | **Agree** | `_supporting_lens_skills` + `test_runtime_trust_boundary_supporting_lens_lists_skills` |
| EW | Holdout expansion | **Defer** | maintenance |
| EX | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 83)

- `02-engineering/*.md`: Primary workflow surface trimmed (escalate/pair skills moved to Scope); five prompts updated
- `plans/tests/test_prompt_cross_links.py`: `ENGINEERING_SKILL_LINKS`; `Primary workflow surfaces?` regex; primary parity tests for engineering/agent/context/domain/repo; supporting-lens guard for `runtime-trust-boundary.md`
- `GLOSSARY.md`: playbook Rounds 1–83; step 15 for composable prompt primary-surface parity
- `QUALITY_GATES_SUMMARY.md`: composable primary-surface parity note; panel Rounds 1–83; 470+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 83 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 83 sync

## Verification (Round 83)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 83** (options EU–EX). Composable prompts (`02-engineering`–`06-repo`) Primary workflow surface lines now match `*_SKILL_LINKS` exactly; supporting-lens pattern documented for `runtime-trust-boundary.md`. Holdout expansion remains recurrence-gated maintenance.

---

## Round 84 — Core prompt Primary workflow surface parity (2026-06-25)

**Options EY–FB** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 84 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| EY | Strict `Primary workflow surface(s)` ↔ `CORE_SKILL_LINKS` parity for `00-core` + pytest | **Agree** |
| EZ | Trim overlisted primary skills (`global-controller`, `important-task-full`) | **Agree** |
| FA | ROUTE holdout expansion | **Defer** |
| FB | Router / tenth skill / benchmark CI | **Reject** |

### Round 84 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| EY | Core primary-surface parity | **Agree** | `CORE_SKILL_LINKS` + `CORE_THINKING_LINKS` + primary tests |
| EZ | Primary-line trim | **Agree** | Move brief pairing and risk escalation to Scope |
| FA | Holdout expansion | **Defer** | maintenance |
| FB | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 84)

- `00-core/global-controller.md`, `00-core/important-task-full.md`: Primary lines trimmed; adjacent/escalation skills in Scope
- `plans/tests/test_prompt_cross_links.py`: `CORE_SKILL_LINKS`, `CORE_THINKING_LINKS`, core primary-surface parity tests
- `GLOSSARY.md`: playbook Rounds 1–84; step 16 for `00-core` primary-surface parity
- `QUALITY_GATES_SUMMARY.md`: core primary-surface parity note; panel Rounds 1–84; 520+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 84 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 84 sync

## Verification (Round 84)

- `make all`: pytest + ROUTE-001/002/003 100%

---

## Round 85 — Composable prompt Primary workflow surface preamble guards (2026-06-25)

**Options FC–FF** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 85 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| FC | `Primary workflow surface(s)` / Supporting-lens preamble guards in all composable `test_*_prompts_eval_harness.py` files | **Agree** |
| FD | GLOSSARY playbook step 17 + governance sync | **Agree** |
| FE | ROUTE holdout expansion | **Defer** |
| FF | Router / tenth skill / benchmark CI | **Reject** |

### Round 85 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| FC | Composable preamble guards | **Agree** | mirror `test_thinking_prompts_eval_harness.py`; Supporting-lens exemption for `runtime-trust-boundary.md` |
| FD | Playbook + docs | **Agree** | step 17; panel round 85 sync |
| FE | Holdout expansion | **Defer** | maintenance |
| FF | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 85)

- `plans/tests/test_core_prompts_eval_harness.py`, `test_engineering_prompts_eval_harness.py`, `test_context_prompts_eval_harness.py`, `test_domain_prompts_eval_harness.py`, `test_repo_prompts_eval_harness.py`: Primary workflow surface preamble guard
- `plans/tests/test_agent_prompts_eval_harness.py`: Primary vs Supporting-lens preamble guard (`runtime-trust-boundary.md` exemption)
- `GLOSSARY.md`: playbook Rounds 1–85; step 17 for composable preamble guards
- `QUALITY_GATES_SUMMARY.md`: preamble guard note; panel Rounds 1–85; 530+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 85 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 85 sync

## Verification (Round 85)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 85** (options FC–FF). Composable prompts now have eval_harness preamble guards matching thinking-lens pattern; full library parity (graph + preamble) closed. Holdout expansion remains recurrence-gated maintenance.


---

## Round 86 — Composable Human Review preamble guards (2026-06-25)

**Options FG–FJ** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 86 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| FG | `## Human Review` preamble guards on composable prompts (`02-engineering`–`06-repo`) that declare the heading + route to `reflective-risk` | **Agree** |
| FH | GLOSSARY playbook step 17 backfill (R85 preamble guards) + step 18 (composable Human Review guards) + governance sync | **Agree** |
| FI | ROUTE holdout expansion | **Defer** |
| FJ | Router / tenth skill / benchmark CI | **Reject** |

### Round 86 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| FG | Composable Human Review guards | **Agree** | parametrized tests via `prompt_eval_helpers.py`; align HR copy to `reflective-risk` |
| FH | Playbook + docs | **Agree** | steps 17–18; panel round 86 sync |
| FI | Holdout expansion | **Defer** | maintenance |
| FJ | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 86)

- `plans/tests/prompt_eval_helpers.py`: exact `## Human Review` heading detection (avoids `## Human Review Required` false positives)
- `plans/tests/test_{engineering,context,agent,domain,repo}_prompts_eval_harness.py`: Human Review preamble guards on prompts that declare the section
- Prompt copy aligned to `reflective-risk` in `memory-consolidation.md`, `retro.md`, `small-context.md`, `creative-template.md`, `cursor-rules.md`, `PROJECT_KNOWLEDGE.template.md`; contract `## Human Review` added to `AGENTS.md`
- `GLOSSARY.md`: playbook Rounds 1–86; step 17 (R85 backfill) + step 18 (composable Human Review guards)
- `QUALITY_GATES_SUMMARY.md`: Human Review guard note; panel Rounds 1–86; 550+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 86 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 86 sync

## Verification (Round 86)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 86** (options FG–FJ). Composable prompts with `## Human Review` now have eval_harness preamble guards matching thinking-lens pattern (R81); full library contract parity closed (graph + primary surface + Human Review). Holdout expansion remains recurrence-gated maintenance.

---

## Round 87 — Human Review helper DRY + GLOSSARY playbook repair (2026-06-25)

**Options FK–FO** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 87 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| FK | Fix GLOSSARY playbook step 17/18 newline merge + `test_maintenance_playbook_steps_on_separate_lines` | **Agree** |
| FL | DRY Human Review guards via `prompt_eval_helpers.assert_human_review_preamble` across all `test_*_prompts_eval_harness.py` | **Agree** |
| FM | GLOSSARY playbook step 19 + governance sync | **Agree** |
| FN | ROUTE holdout expansion | **Defer** |
| FO | Router / tenth skill / benchmark CI | **Reject** |

### Round 87 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| FK | Playbook repair | **Agree** | split merged steps; anti-drift pytest |
| FL | Shared HR helper | **Agree** | migrate thinking + composable harness files |
| FM | Playbook + docs | **Agree** | step 19; panel round 87 sync |
| FN | Holdout expansion | **Defer** | maintenance |
| FO | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 87)

- `GLOSSARY.md`: repaired step 17/18 newline merge; playbook step 19 for shared Human Review helper
- `plans/tests/test_glossary_structure.py`: `test_maintenance_playbook_steps_on_separate_lines`
- `plans/tests/prompt_eval_helpers.py`: `assert_human_review_preamble`
- `plans/tests/test_{thinking,engineering,context,agent,domain,repo}_prompts_eval_harness.py`: use shared Human Review helper
- `QUALITY_GATES_SUMMARY.md`: shared HR helper note; panel Rounds 1–87; 550+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 87 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 87 sync

## Verification (Round 87)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 87** (options FK–FO). Human Review guards now share one helper across thinking lenses and composable prompts; GLOSSARY playbook formatting anti-drift closed. Holdout expansion remains recurrence-gated maintenance.

---

## Round 88 — `00-core` Human Review preamble guards (2026-06-25)

**Options FP–FS** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 88 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| FP | `## Human Review` preamble on risk-bearing `00-core/` prompts + `test_core_prompts_eval_harness.py` guards | **Agree** |
| FQ | GLOSSARY playbook step 20 + governance sync | **Agree** |
| FR | ROUTE holdout expansion | **Defer** |
| FS | Router / tenth skill / benchmark CI | **Reject** |

### Round 88 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| FP | Core Human Review preambles | **Agree** | six risk-bearing prompts; shared `prompt_eval_helpers` guard |
| FQ | Playbook + docs | **Agree** | step 20; panel round 88 sync |
| FR | Holdout expansion | **Defer** | maintenance |
| FS | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 88)

- `00-core/{core-minimal,core-short,core-full,custom-instruction-en,custom-instruction-zh,important-task-full}.md`: `## Human Review` preamble routes to `reflective-risk`
- `plans/tests/test_core_prompts_eval_harness.py`: Human Review guards via `prompt_eval_helpers`
- `GLOSSARY.md`: playbook Rounds 1–88; step 20 for `00-core` Human Review guards
- `QUALITY_GATES_SUMMARY.md`: `00-core` HR guard note; panel Rounds 1–88; 560+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 88 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 88 sync

## Verification (Round 88)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 88** (options FP–FS). Full prompt library now has Human Review preamble guards on thinking lenses (R81), composable prompts (R86), and risk-bearing `00-core` prompts (R88). Holdout expansion remains recurrence-gated maintenance.

---

## Round 89 — `00-core` Human Review required/exempt set parity (2026-06-25)

**Options FT–FW** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 89 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| FT | Frozen `CORE_HUMAN_REVIEW_REQUIRED` / `CORE_HUMAN_REVIEW_EXEMPT` sets + pytest parity in `test_core_prompts_eval_harness.py` | **Agree** |
| FU | GLOSSARY playbook step 21 + governance sync | **Agree** |
| FV | ROUTE holdout expansion | **Defer** |
| FW | Router / tenth skill / benchmark CI | **Reject** |

### Round 89 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| FT | Core HR set parity | **Agree** | codify 6 required + 3 exempt opener prompts |
| FU | Playbook + docs | **Agree** | step 21; panel round 89 sync |
| FV | Holdout expansion | **Defer** | maintenance |
| FW | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 89)

- `plans/tests/test_core_prompts_eval_harness.py`: `CORE_HUMAN_REVIEW_REQUIRED`, `CORE_HUMAN_REVIEW_EXEMPT`, partition + detection parity tests
- `GLOSSARY.md`: playbook Rounds 1–89; step 21 for core HR required/exempt sets
- `QUALITY_GATES_SUMMARY.md`: core HR set parity note; panel Rounds 1–89; 560+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 89 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 89 sync

## Verification (Round 89)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 89** (options FT–FW). `00-core` Human Review coverage is now explicit via frozen required/exempt sets; full library HR contract parity closed (thinking R81, composable R86, core R88–R89). Holdout expansion remains recurrence-gated maintenance.

---

## Round 90 — library-wide Human Review required/exempt set parity (2026-06-25)

**Options FX–GB** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 90 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| FX | DRY Human Review set parity helpers in `prompt_eval_helpers.py` + refactor `test_core_prompts_eval_harness.py` | **Agree** |
| FY | Frozen `*_HUMAN_REVIEW_REQUIRED` / `*_HUMAN_REVIEW_EXEMPT` sets + pytest parity for `01-thinking`–`06-repo` | **Agree** |
| FZ | GLOSSARY playbook step 22 + governance sync | **Agree** |
| GA | ROUTE holdout expansion | **Defer** |
| GB | Router / tenth skill / benchmark CI | **Reject** |

### Round 90 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| FX | HR set parity helpers | **Agree** | `assert_human_review_required_matches_detection`, `assert_human_review_exempt_have_no_preamble_section`, `assert_human_review_sets_partition` |
| FY | Library HR frozen sets | **Agree** | codify required/exempt per category in all `test_*_prompts_eval_harness.py` files |
| FZ | Playbook + docs | **Agree** | step 22; panel round 90 sync |
| GA | Holdout expansion | **Defer** | maintenance |
| GB | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 90)

- `plans/tests/prompt_eval_helpers.py`: shared Human Review set parity helpers
- `plans/tests/test_core_prompts_eval_harness.py`: refactor to shared helpers
- `plans/tests/test_{thinking,engineering,context,agent,domain,repo}_prompts_eval_harness.py`: frozen HR required/exempt sets + partition parity tests
- `GLOSSARY.md`: playbook Rounds 1–90; step 22 for library-wide HR set parity
- `QUALITY_GATES_SUMMARY.md`: HR set parity note; panel Rounds 1–90; 580+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 90 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 90 sync

## Verification (Round 90)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 90** (options FX–GB). Human Review coverage is now explicit via frozen required/exempt sets across all prompt categories (`00-core`–`06-repo`). Holdout expansion remains recurrence-gated maintenance.

---

## Round 91 — cross-category Human Review library registry (2026-06-25)

**Options GC–GG** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 91 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| GC | `PROMPT_LIBRARY_CATEGORIES` + `test_human_review_library_registry.py` cross-category HR registry pytest | **Agree** |
| GD | Remove duplicate `*_PROMPTS_WITH_HUMAN_REVIEW` assignments in composable harness files | **Agree** |
| GE | GLOSSARY playbook step 23 + governance sync | **Agree** |
| GF | ROUTE holdout expansion | **Defer** |
| GG | Router / tenth skill / benchmark CI | **Reject** |

### Round 91 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| GC | HR library registry | **Agree** | `PROMPT_LIBRARY_CATEGORIES`; registry imports all frozen HR sets; library glob parity |
| GD | Harness dedupe | **Agree** | drop duplicate `prompts_with_human_review` lines |
| GE | Playbook + docs | **Agree** | step 23; panel round 91 sync |
| GF | Holdout expansion | **Defer** | maintenance |
| GG | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 91)

- `plans/tests/prompt_eval_helpers.py`: `PROMPT_LIBRARY_CATEGORIES` tuple
- `plans/tests/test_human_review_library_registry.py`: cross-category HR registry + library glob parity
- `plans/tests/test_{agent,context,domain,engineering,repo}_prompts_eval_harness.py`: dedupe duplicate HR prompt tuples
- `GLOSSARY.md`: playbook Rounds 1–91; step 23 for HR library registry
- `QUALITY_GATES_SUMMARY.md`: HR registry note; panel Rounds 1–91; 590+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 91 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 91 sync

## Verification (Round 91)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 91** (options GC–GG). Human Review frozen sets are now cross-checked by a single library registry (`00-core`–`06-repo`). Holdout expansion remains recurrence-gated maintenance.

---

## Round 92 — cross-category skill/thinking cross-link library registry (2026-06-25)

**Options GH–GL** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 92 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| GH | Missing `test_all_{agent,context,domain,repo}_prompts_have_skill_link` completeness guards in `test_prompt_cross_links.py` | **Agree** |
| GI | `test_prompt_skill_links_library_registry.py` cross-category `*_SKILL_LINKS` / `*_THINKING_LINKS` registry + library glob parity | **Agree** |
| GJ | GLOSSARY playbook step 24 + governance sync | **Agree** |
| GK | ROUTE holdout expansion | **Defer** |
| GL | Router / tenth skill / benchmark CI | **Reject** |

### Round 92 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| GH | Skill link completeness | **Agree** | four missing per-category `have_skill_link` tests |
| GI | Cross-link library registry | **Agree** | registry for composable categories + thinking consumer map |
| GJ | Playbook + docs | **Agree** | step 24; panel round 92 sync |
| GK | Holdout expansion | **Defer** | maintenance |
| GL | Router/tenth skill/benchmark CI | **Reject** | no change |

**All roles agree.**

## Implemented Changes (Round 92)

- `plans/tests/test_prompt_cross_links.py`: `test_all_{agent,context,domain,repo}_prompts_have_skill_link`
- `plans/tests/test_prompt_skill_links_library_registry.py`: cross-category skill/thinking link registry + library glob parity
- `GLOSSARY.md`: playbook Rounds 1–92; step 24 for cross-link library registry
- `QUALITY_GATES_SUMMARY.md`: cross-link registry note; panel Rounds 1–92; 600+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 92 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 92 sync

## Verification (Round 92)

- `make all`: pytest + ROUTE-001/002/003 100%

## Panel status (updated)

**Resealed 2026-06-25** after **Round 92** (options GH–GL). Primary workflow surface cross-links are now library-registry checked (`00-core`, `02-engineering`–`06-repo`) with thinking-lens consumer map parity for `01-thinking`. Holdout expansion remains recurrence-gated maintenance.

## Round 93 — cross-category eval_harness contract heading library registry (2026-06-25)

**Options GM–GQ** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 93 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| GM | DRY `PROMPT_CONTRACT_HEADINGS` / `PROMPT_EVAL_MIN_SCORE` / `assert_prompt_contract_headings` in `prompt_eval_helpers.py`; refactor `test_*_prompts_eval_harness.py` | **Agree** |
| GN | `test_prompt_contract_library_registry.py` cross-category contract registry + library glob parity | **Agree** |
| GO | GLOSSARY playbook step 25 + governance sync | **Agree** |
| GP | ROUTE holdout expansion | **Defer** |
| GQ | Router / tenth skill / benchmark CI | **Reject** |

### Round 93 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| GM | Shared contract constants | **Agree** | `prompt_eval_helpers.py` + harness refactor |
| GN | Contract library registry | **Agree** | `test_prompt_contract_library_registry.py` |
| GO | Playbook + docs | **Agree** | step 25; panel round 93 sync |
| GP | Holdout expansion | **Defer** | maintenance |
| GQ | Router/tenth skill/benchmark CI | **Reject** | no change |

### Socratic rationale (Round 93)

- **Opus:** Rounds 91–92 closed HR and cross-link library registries; contract headings remain duplicated across seven harness files with no library-wide falsifiability.
- **Codex:** Centralizing `PROMPT_CONTRACT_HEADINGS` prevents per-category drift; registry test mirrors HR/cross-link pattern.
- **Gemini:** Low-risk maintenance; no router or skill-count changes.
- **Composer:** `assert_prompt_contract_headings` DRYs seven identical test bodies.
- **Sakana:** `01-thinking` included in contract registry (unlike cross-link composable-only registry) because all categories share the same preamble contract.
- **GLM:** Unanimous — implement GM–GO only.

## Implemented Changes (Round 93)

- `plans/tests/prompt_eval_helpers.py`: `PROMPT_CONTRACT_HEADINGS`, `PROMPT_EVAL_MIN_SCORE`, `assert_prompt_contract_headings`
- `plans/tests/test_*_prompts_eval_harness.py`: import shared contract constants; DRY contract heading guards
- `plans/tests/test_prompt_contract_library_registry.py`: cross-category contract registry + library glob parity
- `GLOSSARY.md`: playbook Rounds 1–93; step 25 for contract library registry
- `QUALITY_GATES_SUMMARY.md`: contract registry note; panel Rounds 1–93; 615+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 93 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 93 sync

## Verification (Round 93)

- `make all`: pytest + ROUTE-001/002/003 100%

---

**Resealed 2026-06-25** after **Round 93** (options GM–GQ). Eval_harness contract headings are now library-registry checked across all `00-core`–`06-repo` prompts with shared `PROMPT_CONTRACT_HEADINGS`. Holdout expansion remains recurrence-gated maintenance.

## Round 94 — cross-category Primary workflow surface preamble library registry (2026-06-25)

**Options GR–GV** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 94 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| GR | DRY `assert_primary_workflow_surface_preamble` + `SUPPORTING_LENS_PRIMARY_SURFACE_BY_CATEGORY` in `prompt_eval_helpers.py` | **Agree** |
| GS | `test_prompt_primary_workflow_surface_library_registry.py` cross-category registry + library glob parity | **Agree** |
| GT | GLOSSARY playbook step 26 + governance sync | **Agree** |
| GU | ROUTE holdout expansion | **Defer** |
| GV | Router / tenth skill / benchmark CI | **Reject** |

### Round 94 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| GR | Primary surface preamble helper | **Agree** | shared helper + supporting-lens map |
| GS | Primary surface library registry | **Agree** | `test_prompt_primary_workflow_surface_library_registry.py` |
| GT | Playbook + docs | **Agree** | step 26; panel round 94 sync |
| GU | Holdout expansion | **Defer** | maintenance |
| GV | Router/tenth skill/benchmark CI | **Reject** | no change |

### Socratic rationale (Round 94)

- **Opus:** Rounds 91–93 closed HR, cross-link, and contract registries; Primary workflow surface preamble guards remain duplicated across seven harness files with no library-wide falsifiability.
- **Codex:** Centralizing `assert_primary_workflow_surface_preamble` prevents per-category drift; `runtime-trust-boundary.md` Supporting-lens exemption belongs in one map.
- **Gemini:** Registry adds one sweep over 49 prompts without extra CI cost beyond pytest.
- **Composer:** IDE contributors edit Purpose preambles often — one helper matches Round 87 HR DRY pattern.
- **Sakana:** Thinking lenses use plural "surfaces"; substring guard still matches without a separate code path.
- **GLM:** Supporting-lens map is English-canonical; no TW SKILL translation needed.

## Implemented Changes (Round 94)

- `plans/tests/prompt_eval_helpers.py`: `SUPPORTING_LENS_PRIMARY_SURFACE_BY_CATEGORY`, `assert_primary_workflow_surface_preamble`
- `plans/tests/test_*_prompts_eval_harness.py`: DRY primary-surface preamble guards
- `plans/tests/test_prompt_primary_workflow_surface_library_registry.py`: cross-category registry + library glob parity
- `GLOSSARY.md`: playbook Rounds 1–94; step 26 for primary-surface library registry
- `QUALITY_GATES_SUMMARY.md`: primary-surface registry note; panel Rounds 1–94; 630+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 94 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 94 sync

## Verification (Round 94)

- `make all`: pytest + ROUTE-001/002/003 100%

---

**Resealed 2026-06-25** after **Round 94** (options GR–GV). Primary workflow surface preambles are now library-registry checked across all `00-core`–`06-repo` prompts with shared `assert_primary_workflow_surface_preamble` and Supporting-lens exemptions in one map. Holdout expansion remains recurrence-gated maintenance.


## Round 95 — cross-category workflow skill coverage library registry (2026-06-25)

**Options GW–HA** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 95 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| GW | DRY `assert_category_workflow_skill_coverage` + frozen `*_COVER_WORKFLOW_SKILLS` per harness | **Agree** |
| GX | `test_workflow_skill_coverage_library_registry.py` — coverage registry; `01-thinking` exempt (empty tuple, consumer graph) | **Agree** |
| GY | GLOSSARY playbook step 27 + governance sync | **Agree** |
| GZ | ROUTE holdout expansion | **Defer** |
| HA | Router / tenth skill / benchmark CI | **Reject** |

### Round 95 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| GW | Workflow skill coverage helper | **Agree** | shared helper + frozen tuples per category |
| GX | Workflow skill coverage library registry | **Agree** | `test_workflow_skill_coverage_library_registry.py` |
| GY | Playbook + docs | **Agree** | step 27; panel round 95 sync |
| GZ | Holdout expansion | **Defer** | maintenance |
| HA | Router/tenth skill/benchmark CI | **Reject** | no change |

### Socratic rationale (Round 95)

- **Opus:** Rounds 91–94 closed HR, cross-link, contract, and primary-surface registries; per-category `cover_*` workflow skill guards remain duplicated with no library-wide falsifiability.
- **Codex:** Centralizing `assert_category_workflow_skill_coverage` prevents per-category drift; `01-thinking` empty tuple documents consumer-graph exemption explicitly.
- **Gemini:** Registry adds one sweep over seven categories without extra CI cost beyond pytest.
- **Composer:** IDE contributors edit workflow skill references often — one helper matches Round 94 primary-surface DRY pattern.
- **Sakana:** Thinking lenses route via consumer graph; empty frozen tuple is clearer than omitting the category.
- **GLM:** Coverage tuples are English-canonical skill filenames; no TW SKILL translation needed.

## Implemented Changes (Round 95)

- `plans/tests/prompt_eval_helpers.py`: `assert_category_workflow_skill_coverage`
- `plans/tests/test_*_prompts_eval_harness.py`: DRY workflow skill coverage guards + frozen `*_COVER_WORKFLOW_SKILLS`
- `plans/tests/test_workflow_skill_coverage_library_registry.py`: cross-category registry + library glob parity
- `GLOSSARY.md`: playbook Rounds 1–95; step 27 for workflow skill coverage library registry
- `QUALITY_GATES_SUMMARY.md`: workflow skill coverage registry note; panel Rounds 1–95; 640+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 95 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 95 sync

## Verification (Round 95)

- `make all`: 641 pytest + ROUTE-001/002/003 100%

---

## Round 96 — cross-category eval_harness score floor library registry (2026-06-25)

**Options HB–HF** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 96 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| HB | DRY `assert_prompt_meets_eval_harness_floor` in `prompt_eval_helpers.py` | **Agree** |
| HC | `test_prompt_eval_harness_score_library_registry.py` — score floor registry + library-wide sweep | **Agree** |
| HD | GLOSSARY playbook step 28 + governance sync | **Agree** |
| HE | ROUTE holdout expansion | **Defer** |
| HF | Router / tenth skill / benchmark CI | **Reject** |

### Round 96 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| HB | DRY eval_harness score floor helper | **Agree** | `assert_prompt_meets_eval_harness_floor` |
| HC | Score floor library registry | **Agree** | `test_prompt_eval_harness_score_library_registry.py` |
| HD | Playbook + docs | **Agree** | step 28; panel round 96 sync |
| HE | Holdout expansion | **Defer** | maintenance |
| HF | Router/tenth skill/benchmark CI | **Reject** | no change |

### Socratic rationale (Round 96)

- **Opus:** Rounds 91–95 closed HR, cross-link, contract, primary-surface, and workflow-coverage registries; per-category `meets_eval_harness_floor` guards remain duplicated with no library-wide falsifiability.
- **Codex:** Centralizing `assert_prompt_meets_eval_harness_floor` prevents score-floor drift; registry sweep catches regressions across all 49 prompts in one place.
- **Gemini:** Reject duplicating `EvalHarness.evaluate_file` logic in seven harness files — token/cost of maintenance, not runtime.
- **Composer:** IDE adopters need one playbook step when bumping `PROMPT_EVAL_MIN_SCORE`; library registry mirrors R93 contract pattern.
- **Sakana:** Score floor is orthogonal to thinking consumer graph — all seven categories including `01-thinking` belong in registry.
- **GLM:** TW surface unchanged; score floor stays English-only harness policy.

**All roles agree.**

## Implemented Changes (Round 96)

- `plans/tests/prompt_eval_helpers.py`: `assert_prompt_meets_eval_harness_floor`
- `plans/tests/test_*_prompts_eval_harness.py`: DRY eval_harness score floor guards
- `plans/tests/test_prompt_eval_harness_score_library_registry.py`: cross-category registry + library glob parity + library-wide sweep
- `GLOSSARY.md`: playbook Rounds 1–96; step 28 for eval_harness score floor library registry
- `QUALITY_GATES_SUMMARY.md`: score floor registry note; panel Rounds 1–96; 650+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 96 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 96 sync

## Verification (Round 96)

- `make all`: 652 pytest + ROUTE-001/002/003 100%

---

**Resealed 2026-06-25** after **Round 96** (options HB–HF). Eval_harness score floors are now library-registry checked across all `00-core`–`06-repo` categories with shared `assert_prompt_meets_eval_harness_floor` and per-category `MIN_SCORE` aliases to `PROMPT_EVAL_MIN_SCORE`. Holdout expansion remains recurrence-gated maintenance.

## Round 97 — cross-category workflow skill reference library registry (2026-06-25)

**Options HG–HK** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 97 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| HG | DRY `assert_prompt_references_workflow_skill` in `prompt_eval_helpers.py` (preamble-scoped) | **Agree** |
| HH | `test_prompt_workflow_skill_reference_library_registry.py` — library-wide preamble skill-reference sweep | **Agree** |
| HI | GLOSSARY playbook step 29 + governance sync | **Agree** |
| HJ | ROUTE holdout expansion | **Defer** |
| HK | Router / tenth skill / benchmark CI | **Reject** |

### Round 97 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| HG | Workflow skill reference DRY helper | **Agree** | `assert_prompt_references_workflow_skill` |
| HH | Workflow skill reference library registry | **Agree** | `test_prompt_workflow_skill_reference_library_registry.py` |
| HI | Playbook + docs | **Agree** | step 29; panel round 97 sync |
| HJ | Holdout expansion | **Defer** | maintenance |
| HK | Router/tenth skill/benchmark CI | **Reject** | no change |

### Socratic rationale (Round 97)

- **Opus:** Round 96 closed eval_harness score floors; seven per-category `reference_workflow_skills` guards still duplicate `"reflective-" in text` with no library-wide falsifiability and weaker preamble scoping than cross-link tests.
- **Codex:** Preamble-scoped helper aligns with `test_prompt_cross_links.py` engineering guard; registry sweep catches template-only skill mentions across all 49 prompts.
- **Gemini:** Cheap deterministic check; no router or prompt content churn.
- **Composer:** Mirrors R91–R96 registry pattern; one helper + one registry file.
- **Sakana:** Thinking lenses already require consumer skills in preambles; library registry documents that invariant explicitly.
- **GLM:** Preamble scope avoids false passes from fenced zh-TW templates; playbook step 29 gives operators a single checklist line.

**All roles agree.**

## Implemented Changes (Round 97)

- `plans/tests/prompt_eval_helpers.py`: `assert_prompt_references_workflow_skill`
- `plans/tests/test_*_prompts_eval_harness.py`: DRY workflow skill reference guards
- `plans/tests/test_prompt_workflow_skill_reference_library_registry.py`: cross-category registry + library glob parity
- `GLOSSARY.md`: playbook Rounds 1–97; step 29 for workflow skill reference library registry
- `QUALITY_GATES_SUMMARY.md`: workflow skill reference registry note; panel Rounds 1–97; 660+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 97 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 97 sync

## Verification (Round 97)

- `make all`: 663 pytest + ROUTE-001/002/003 100%

---

**Resealed 2026-06-25** after **Round 97** (options HG–HK). Workflow skill references are now library-registry checked across all `00-core`–`06-repo` categories with shared `assert_prompt_references_workflow_skill` (preamble-scoped). Holdout expansion remains recurrence-gated maintenance.

## Round 98 — cross-category eval_harness fixture library registry (2026-06-25)

**Options HL–HP** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 98 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| HL | DRY `make_category_eval_harness_fixture` + `PROMPT_LIBRARY_REPO_ROOT` in `prompt_eval_helpers.py` | **Agree** |
| HM | `test_prompt_eval_harness_fixture_library_registry.py` — fixture + `REPO_ROOT` parity registry | **Agree** |
| HN | GLOSSARY playbook step 30 + governance sync | **Agree** |
| HO | ROUTE holdout expansion | **Defer** |
| HP | Router / tenth skill / benchmark CI | **Reject** |

### Round 98 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| HL | EvalHarness fixture DRY factory | **Agree** | `make_category_eval_harness_fixture` + `PROMPT_LIBRARY_REPO_ROOT` |
| HM | EvalHarness fixture library registry | **Agree** | `test_prompt_eval_harness_fixture_library_registry.py` |
| HN | Playbook + docs | **Agree** | step 30; panel round 98 sync |
| HO | Holdout expansion | **Defer** | maintenance |
| HP | Router/tenth skill/benchmark CI | **Reject** | no change |

### Socratic rationale (Round 98)

- **Opus:** Round 97 closed workflow skill references; seven per-category harness files still duplicate identical module-scoped `EvalHarness` fixtures with no library-wide falsifiability.
- **Codex:** Centralizing `make_category_eval_harness_fixture` prevents `repo_root` drift; `PROMPT_LIBRARY_REPO_ROOT` object-identity checks catch path miscalculations.
- **Gemini:** Zero runtime cost; removes boilerplate only.
- **Composer:** Mirrors R91–R97 registry pattern; one factory + one registry file.
- **Sakana:** Fixture parity documents that all categories evaluate prompts against the same TeaPrompt root.
- **GLM:** Playbook step 30 gives operators a single checklist line for harness fixture edits.

**All roles agree.**

## Implemented Changes (Round 98)

- `plans/tests/prompt_eval_helpers.py`: `PROMPT_LIBRARY_REPO_ROOT`, `make_category_eval_harness_fixture`
- `plans/tests/test_*_prompts_eval_harness.py`: DRY harness fixtures via shared factory
- `plans/tests/test_prompt_eval_harness_fixture_library_registry.py`: cross-category fixture registry
- `GLOSSARY.md`: playbook Rounds 1–98; step 30 for eval_harness fixture library registry; dedupe step 28
- `QUALITY_GATES_SUMMARY.md`: fixture registry note; panel Rounds 1–98; 670+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 98 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 98 sync

## Verification (Round 98)

- `make all`: 672 pytest + ROUTE-001/002/003 100%

---

**Resealed 2026-06-25** after **Round 98** (options HL–HP). Eval_harness fixtures are now library-registry checked across all `00-core`–`06-repo` categories with shared `make_category_eval_harness_fixture` and `PROMPT_LIBRARY_REPO_ROOT`. Holdout expansion remains recurrence-gated maintenance.

## Round 99 — cross-category prompt path library registry + preamble fix (2026-06-25)

**Options HQ–HU** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 99 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| HQ | DRY `category_prompt_dir` + `sorted_category_prompts` in `prompt_eval_helpers.py` | **Agree** |
| HR | `test_prompt_category_paths_library_registry.py` — category dir + prompt tuple parity registry | **Agree** |
| HS | Fix `assert_prompt_references_workflow_skill` to preamble scope + GLOSSARY step 31 + governance sync | **Agree** |
| HT | ROUTE holdout expansion | **Defer** |
| HU | Router / tenth skill / benchmark CI | **Reject** |

### Round 99 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| HQ | Category prompt path DRY helpers | **Agree** | `category_prompt_dir` + `sorted_category_prompts` |
| HR | Category path library registry | **Agree** | `test_prompt_category_paths_library_registry.py` |
| HS | Preamble scope + playbook | **Agree** | `prompt_preamble` in workflow skill reference helper; step 31 |
| HT | Holdout expansion | **Defer** | maintenance |
| HU | Router/tenth skill/benchmark CI | **Reject** | no change |

### Socratic rationale (Round 99)

- **Opus:** Round 98 closed eval_harness fixtures; seven harness files still duplicate `Path(__file__).parent.parent.parent / "0X-category"` glob tuples with no library-wide falsifiability; Round 97 docs claimed preamble-scoped workflow skill references but helper still scanned full file bodies.
- **Codex:** Shared `PROMPT_LIBRARY_ROOT` + `category_prompt_dir` prevents off-by-one parent drift; preamble fix aligns implementation with `test_prompt_cross_links.py` and GLOSSARY step 29.
- **Gemini:** Deterministic path registry; no prompt content churn.
- **Composer:** Mirrors R91–R98 registry pattern; one helper pair + one registry file.
- **Sakana:** Category path parity documents that all harness modules resolve the same composable prompt globs.
- **GLM:** Preamble-scoped workflow skill check avoids false passes from fenced template mentions; playbook step 31 gives operators a single checklist line.

**All roles agree.**

## Implemented Changes (Round 99)

- `plans/tests/prompt_eval_helpers.py`: `PROMPT_LIBRARY_ROOT`, `category_prompt_dir`, `sorted_category_prompts`; `assert_prompt_references_workflow_skill` preamble-scoped
- `plans/tests/test_*_prompts_eval_harness.py`: DRY category dirs + prompt tuples via shared helpers
- `plans/tests/test_prompt_category_paths_library_registry.py`: cross-category path registry
- `GLOSSARY.md`: playbook Rounds 1–99; step 31 for category path library registry
- `QUALITY_GATES_SUMMARY.md`: category path registry note; preamble fix note; panel Rounds 1–99; 680+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 99 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 99 sync

## Verification (Round 99)

- `make all`: 682 pytest + ROUTE-001/002/003 100%

---

**Resealed 2026-06-25** after **Round 99** (options HQ–HU). Composable prompt category paths are now library-registry checked across all `00-core`–`06-repo` categories with shared `category_prompt_dir` / `sorted_category_prompts`; workflow skill reference guards are preamble-scoped as documented. Holdout expansion remains recurrence-gated maintenance.

## Round 100 — cross-category library registry helper DRY (2026-06-25)

**Options HV–HZ** | Six-lens panel (Opus, Codex, Gemini, Composer, Sakana, GLM)

### Round 100 options

| ID | Proposal | Verdict |
| --- | --- | --- |
| HV | DRY `assert_library_wide_unique_basenames` + `assert_registry_matches_library_glob` + `sorted_all_library_prompts` in `prompt_eval_helpers.py` | **Agree** |
| HW | `test_prompt_library_registry_helpers_library_registry.py` — registry helper parity + module guard | **Agree** |
| HX | Migrate all `*_library_registry.py` glob/unique guards + `test_prompt_cross_links.py` paths; GLOSSARY step 32 + governance sync | **Agree** |
| HY | ROUTE holdout expansion | **Defer** |
| HZ | Router / tenth skill / benchmark CI | **Reject** |

### Round 100 verdict table

| ID | Option | Verdict | Action |
| --- | --- | --- | --- |
| HV | Library registry helper DRY | **Agree** | `assert_library_wide_unique_basenames` + `assert_registry_matches_library_glob` |
| HW | Registry helper library registry | **Agree** | `test_prompt_library_registry_helpers_library_registry.py` |
| HX | Registry migration + playbook | **Agree** | DRY all `*_library_registry.py`; step 32 |
| HY | Holdout expansion | **Defer** | maintenance |
| HZ | Router/tenth skill/benchmark CI | **Reject** | no change |

### Socratic rationale (Round 100)

- **Opus:** Round 99 closed category path helpers; nine cross-category registry files still duplicated library-wide unique-basename and glob-parity loops with local `LIBRARY_ROOT` paths.
- **Codex:** Shared `assert_registry_matches_library_glob` ensures every registry uses `sorted_category_prompts` semantics; `sorted_all_library_prompts` gives one canonical library-wide tuple.
- **Gemini:** Deterministic helper extraction; no prompt content churn.
- **Composer:** Mirrors R91–R99 registry pattern; one helper trio + one registry test file + migration sweep.
- **Sakana:** Registry glob parity now falsifies if any module reintroduces ad-hoc `Path(__file__).parent` globs.
- **GLM:** Playbook step 32 gives operators a single checklist line for library registry edits.

**All roles agree.**

## Implemented Changes (Round 100)

- `plans/tests/prompt_eval_helpers.py`: `sorted_all_library_prompts`, `library_skills_dir`, `assert_library_wide_unique_basenames`, `assert_registry_matches_library_glob`
- `plans/tests/test_*_library_registry.py`: DRY unique/glob guards via shared helpers; remove local `LIBRARY_ROOT`
- `plans/tests/test_prompt_library_registry_helpers_library_registry.py`: cross-category registry helper registry
- `plans/tests/test_prompt_cross_links.py`, `test_project_knowledge_promotion_contract.py`: shared `category_prompt_dir` / `library_skills_dir`
- `GLOSSARY.md`: playbook Rounds 1–100; step 32 for library registry helper registry
- `QUALITY_GATES_SUMMARY.md`: registry helper note; panel Rounds 1–100; 690+ pytest floor
- `PROJECT_KNOWLEDGE.md`: Decision Index Round 100 entry
- `README.md`, `reflective-prompt-library/README.md`, `test_readme_governance.py`: panel round 100 sync

## Verification (Round 100)

- `make all`: 702 pytest + ROUTE-001/002/003 100%

---

**Resealed 2026-06-25** after **Round 100** (options HV–HZ). Cross-category library registries now share `assert_library_wide_unique_basenames` and `assert_registry_matches_library_glob` with a library-wide helper registry guard. Holdout expansion remains recurrence-gated maintenance.
