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

## Residual Open Questions (after Round 5)

1. Undocumented-decisions git check (Knowie-style) — **defer** until decision-drift recurrence (panel unanimous).
2. Fresh ROUTE-002 cases beyond Round 5 seed — **ongoing** before further router tuning.
3. Full `SKILL.md` localization — **still reject** (English canonical).

## Superseded Open Questions

1. Should `reflective-implement` default-invoke `reflective-minimality`? (Deferred — needs recurrence evidence.)
2. Should ROUTE-002 holdout eval block merge? (Already in fixture; monitor in CI.)
3. Localized trigger cues beyond cheatsheet TW? (Defer until adoption signal.)

## Evidence

- Prior decision: Hyperplan / multi-agent planning — no change ([external-adoption-case-studies-2026-06-20.md](external-adoption-case-studies-2026-06-20.md))
- Routing CI: `Makefile` `validate` runs ROUTE-001 and ROUTE-002 via `route_paraphrase_eval.py`
- Governance: `validate_governance.py` after this change
