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

**Closed 2026-06-25** after **Round 20** (options A–AJ). Future promotions still require the three-recurrence gate.

_Ongoing maintenance: [GLOSSARY.md](../GLOSSARY.md) Governance Maintenance Playbook — expand ROUTE-002/003 holdout before router tuning; run `make all`; monitor undocumented-decision warnings._


## Residual Open Questions (after Round 5) — superseded by Round 6


## Superseded Open Questions

1. Should `reflective-implement` default-invoke `reflective-minimality`? (Deferred — needs recurrence evidence.)
2. Should ROUTE-002 holdout eval block merge? (Already in fixture; monitor in CI.)
3. Localized trigger cues beyond cheatsheet TW? (Defer until adoption signal.)

## Evidence

- Prior decision: Hyperplan / multi-agent planning — no change ([external-adoption-case-studies-2026-06-20.md](external-adoption-case-studies-2026-06-20.md))
- Routing CI: `Makefile` `validate` runs ROUTE-001, ROUTE-002 (80 holdout), ROUTE-003 (16 adversarial) via `route_paraphrase_eval.py`
- Governance: `validate_governance.py` after this change
