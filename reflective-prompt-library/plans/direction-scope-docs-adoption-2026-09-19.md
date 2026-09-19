# Direction-Scope Docs Adoption — "Update docs if worth it" (2026-09-19)

> **Status: decided — two sentences adopted (DS-1, DS-2); everything else checked no-change.** Same-day follow-up to the GE-1 landing (`bd06bf4`), under a generic docs direction. The worth bar applied per candidate: a verified local gap on the acting surface, the smallest sufficient destination, and a deterministic guard. Because the direction is generic, it fires only this pass's own candidates — the rule DS-1 itself installs.

## Research Question

User instruction: "Update docs if worth it", immediately after the GE-1 landing. One question: which documentation surfaces have a verified gap exposed by the 2026-09-19 adoption pass — the direction-scope precedent (MC-5 generic vs DR-5/GE-1 named-family, plus the reverted 2026-09-16 first GE-1 landing) and the `index.json` staleness miss — and which apparent candidates are already covered.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| DS-1 | Direction-scope rule in `04-agent/external-adoption-review.md` §5 Signal Accounting: a later user direction is read at the scope it names; generic direction fires only the current review's candidates; a fired consideration trigger authorizes a consideration, not a landing | Adopted 2026-09-19 | Gap verified by grep: neither adoption lens contained "direction" or "user-directed"; the lens teaches `defer` (§Acceptance Criteria) and counts "explicit user project decision" as promotion evidence (§5) without scoping it over deferred rows. Local recurrence, not external interest: MC-5 (generic same-day direction fired no named gates), DR-5 and GE-1 (direction naming the carrying family fired the held candidate), and the reverted 2026-09-16 first GE-1 landing (a consideration trigger read as authorization). The rule this pass needed was reconstructible only from three plans records | Reopen if a direction-scope dispute recurs despite the installed sentence, or if a generic direction is ever found to legitimately require firing a named hold |
| DS-2 | `index.json` staleness-guard sentence in `plans/QUALITY_GATES_SUMMARY.md` | Adopted 2026-09-19 | The summary documented the regeneration command but not the enforcing test or the edit-triggered duty; the gap reproduced this session — `test_committed_index_matches_generator_over_current_tree` failed after editing three indexed files without regeneration, under the mistaken belief regen is only needed for new files | — |
| DS-3 | State Ledger mirror updates in prompt lenses; further index-doc corrections; README/cheatsheet/skill-map/GLOSSARY updates for the GE-1 bullet | No change 2026-09-19 | "State Ledger" and "Source column" absent from `05-domain/`, `02-engineering/`, `03-context/` — the ledger construct is skill-local, so there is no mirror to drift and the single-surface convention holds; remaining `index.json` documentation accurate as written; routing surfaces describe skills at trigger level, which one added bullet does not change | Reopen if a prompt lens gains a ledger construct |

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| No "direction"/"user-directed" coverage on either adoption lens before this pass | Observed | grep over `external-adoption-review.md` and `artifact-promotion.md`, 2026-09-19 |
| Staleness test enforces the committed index in `make test` | Observed / executed | this session's gate failure and green rerun after `generate_index.py` |
| Precedent split (named-family vs generic direction; consideration is not authorization) | Observed | MC-5 addendum in `minimax-code-survey-2026-09-19.md`; DR-5 addendum in `dream-rsi-survey-2026-09-18.md`; GE-1 Landing Addendum and Post-Landing Corrections in `graph-engineering-synthesis-survey-2026-09-16.md` |
| The ledger construct exists only on `reflective-research` | Observed for the named tokens | grep over the three lens directories; bounded by vocabulary, per Falsifiability |

## Falsifiability

- DS-1 is wrong if a future named-family direction is correctly refused for reasons the sentence forbids, or a generic direction legitimately needs to fire a named hold; either requires a recorded rewording decision, not a silent exception.
- DS-3's no-drift claim is bounded to the tokens grepped; it is wrong if a lens carries ledger semantics under other vocabulary.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| DS-1 sentence installed once, inside §5 after the missing-usage rule | done | `plans/tests/test_direction_scope_docs_adoption.py` |
| DS-2 sentence installed; enforcing test named | done | same guard |
| Decision Index bullet at the head; case-studies State Ledger row; `index.json` regenerated | done | `PROJECT_KNOWLEDGE.md`; `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |
