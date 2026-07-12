# Final Report — Roadmap Specs, P7 Closure, and Linter Repair

Date: 2026-07-11

## Summary

Completed the documentation/test pass, then executed every remaining fix that
local evidence made truthful today.

Two additional defects were actionable:

1. **P7/N12 routing collision debt** — the required holdout trigger could be
   satisfied without inventing usage evidence. Nine fresh pack-adjacent phrases
   were measured pre-tune; all preserved the intended core workflow. P7 therefore
   closed as **no core-router integration**, with three fixture groups, ratcheted
   floors, a decision record, and permanent structural guards. No router keyword,
   dispatch row, core workflow, pack contract, or quick cue changed.
2. **Linter scope misclassification** — `lint_skills.py` treated every Markdown
   file as a prompt, then emitted “Skill body” warnings for plans, glossaries,
   installation docs, and reports. It now distinguishes skill / composable prompt
   / document. Documents remain inventoried but do not receive routing-input
   heuristics. Observed warnings fell from 10 to 0 without suppressing checks on
   actual prompts or skills.

All other roadmap candidates remain date-, recurrence-, usage-, or
evidence-gated. No trigger evidence was fabricated to “finish” them.

## Acceptance criteria status

| ID | Criterion | Status | Evidence |
| --- | --- | --- | --- |
| AC-1 | Reason over current roadmaps/plans, including unimplemented work | **Met** | Consolidated dormant-work specs, dependency inference, acceptance/test plans, reopen bars |
| AC-2 | Write substantial documentation usable before implementation | **Met** | Dormant-work spec book, 2026-10-11 checkpoint runbook, P7/N12 successor decision |
| AC-3 | Add executable tests for unimplemented work where possible | **Met** | Dormancy watches, conditional activation guards, checkpoint deadman, roadmap↔spec self-guard |
| AC-4 | Do not silently adopt gated work | **Met** | P7 fired its named holdout trigger and received a decision record; all other gated items stayed dormant |
| AC-5 | Fix remaining feasible defects | **Met** | P7 collision debt measured/closed; T2 section parity strengthened; linter misclassification fixed; isolated quality-test import fixed |
| AC-6 | Preserve bounded core routing | **Met** | Packs absent from router targets, `VALID_WORKFLOWS`, and dispatch rows; P7 decision is no integration |
| AC-7 | Preserve full quality gates | **Met** | Final `make all`: 912 pytest tests; every validator passed; ROUTE-001/002/003 100% |
| AC-8 | Keep unavailable evidence honest | **Met** | P6 and E2 retain their original gates; adopted items record recurrence `unknown` rather than fabricated demand |

## Tests / checks run

### Original dormant-work suite

- Four new modules: **91 focused tests passed**.
- Temporary-file mutation smoke proved expected failures for incomplete P7,
  silent P12 template addition, M6 without ledger flip, and checkpoint overdue
  behavior; completed states passed.

### P7 pre-tune and focused evidence

- Temporary pre-tune ROUTE-002 groups: 6/6 phrases, 100%.
- Temporary pre-tune ROUTE-003 group: 3/3 phrases, 100%.
- Focused routing/adoption/dormancy suite: **122 passed**.
- `validate_route_fixture.py`: ROUTE-002 ≥44 groups / ≥124 phrases;
  ROUTE-003 ≥22 groups / ≥76 phrases.
- Adopted ROUTE-002: 44 groups / 124 phrases, 100%.
- Adopted ROUTE-003: 22 groups / 76 phrases, 100%.

### Linter evidence

- Focused linter tests: **8 passed**.
- Live linter: 148 Markdown files inventoried; 0 errors; 0 warnings;
  38 composable prompt/skill files with non-blocking suggestions.
- Tests prove category prompts remain prompt-checked, skills remain
  skill-checked, long documents skip routing heuristics, and long prompts receive
  type-correct `Prompt body` warnings.

### Skill scenario panel (2026-07-12, user-invoked)

A seven-lens Parallel Lens Review of the skill layer (record:
`reflective-prompt-library/plans/skill-scenario-panel-record-2026-07-12.md`).
Provider quota blocked true parallel fan-out (two `resource_exhausted`
failures); lenses ran sequentially on one host and the record says so. Ten
wording-level updates adopted (implement Small-Change Fast Path + doc-edit
scope, dispatch ladder note, risk data-egress trigger + M7 cross-link, brief
spike framing, handoff ledger bridge, two bilingual boundary cues, install
fallback); ENT-1 / LONG-2 / ZH-2 deferred with named triggers. Guards:
`plans/tests/test_skill_scenario_panel_adoption_state.py` (18 tests). Addendum
PORT-1 (user-directed, same day): all 11 shipped SKILL.md bodies made
install-portable — provenance disclaimers under every `## Prompt Sources`,
load-bearing repo-path instructions inlined with source-repo attribution,
promotion boundaries fail closed without the lenses, `../../` paths removed.

### Final repository gate

Command: `make all` from repository root.

- **917 pytest tests passed**.
- Link + Agent Skills schema validation: 148 files, 0 errors.
- Lint: 148 files, 0 errors, 0 warnings.
- Governance: 11/11 skills valid.
- PROJECT_KNOWLEDGE contract: passed.
- Record hygiene: 2 enforced records, 0 errors.
- Benchmark fixture: 24 tasks, 9/9 core workflows.
- Skill examples: 9 core + 2 domain packs.
- ROUTE-001: 128 phrases, 100%.
- ROUTE-002: 44 groups / 124 phrases, 100%.
- ROUTE-003: 22 groups / 76 phrases, 100%.
- Generated index: 115 files (104 prompts, 11 skills).

## Failures or skipped checks

No check was skipped.

Observed and repaired:

1. Original documentation pass raised collection from 790-era snapshots to 881;
   the `780+` pytest floor failed and was ratcheted upward; the latest floor is `900+` after the scenario-panel wave (912 collected).
2. P7 full-gate run initially failed because the Holdout Tracking paragraph did
   not include the new 44/124 and 22/76 floor step; the historical paragraph was
   extended rather than rewriting prior snapshots.
3. Isolated `test_quality_gates_summary.py` failed because it relied on another
   test polluting `sys.path`; the test now imports its helper path explicitly and
   passes alone.

## Files changed

Created:

- `reflective-prompt-library/plans/dormant-work-specs-2026-07-11.md`
- `reflective-prompt-library/plans/checkpoint-2026-10-11-runbook.md`
- `reflective-prompt-library/plans/p7-pack-routing-decision-2026-07-11.md`
- `reflective-prompt-library/plans/tests/test_dormant_item_watch.py`
- `reflective-prompt-library/plans/tests/test_dormant_conditional_contracts.py`
- `reflective-prompt-library/plans/tests/test_checkpoint_2026_10_11.py`
- `reflective-prompt-library/plans/tests/test_dormant_work_specs_doc.py`
- `review/final-report.md`

Updated implementation / fixtures / tests:

- `reflective-prompt-library/plans/lint_skills.py`
- `reflective-prompt-library/plans/validate_route_fixture.py`
- `reflective-prompt-library/plans/route-002-holdout-eval.yaml`
- `reflective-prompt-library/plans/route-003-adversarial-eval.yaml`
- `reflective-prompt-library/plans/route-002-results.json`
- `reflective-prompt-library/plans/route-003-results.json`
- `reflective-prompt-library/plans/tests/test_lint_skills.py`
- `reflective-prompt-library/plans/tests/test_validate_route_fixture.py`
- `reflective-prompt-library/plans/tests/test_quality_gates_summary.py`
- `reflective-prompt-library/plans/tests/test_candidate_adoption_state.py`

Updated decision / roadmap / evidence surfaces:

- `reflective-prompt-library/PROJECT_KNOWLEDGE.md`
- `reflective-prompt-library/plans/QUALITY_GATES_SUMMARY.md`
- `reflective-prompt-library/plans/agent-flow-control-research-2026-07-11.md`
- `reflective-prompt-library/plans/flow-control-pack-panel-record-2026-07-11.md`
- `reflective-prompt-library/plans/flow-coverage-panel-record-2026-07-11.md`
- `reflective-prompt-library/plans/governance-necessity-panel-record-2026-07-11.md`
- `reflective-prompt-library/plans/flow-control-roadmap-2026-07-11.md`
- `reflective-prompt-library/plans/routing-holdout-plan-2026-07-11.md`
- `reflective-prompt-library/plans/whole-project-plan-2026-07-11.md`
- `reflective-prompt-library/plans/whole-project-roadmap-2026-07-11.md`
- `reflective-prompt-library/index.json`

## Implementation summary

### Dormant-work preparation

The spec book and checkpoint runbook make future decisions verification work,
not archaeology. Deferred rows are guarded only for ledger presence and trigger
state; conditional contracts enforce complete activation when a dormant surface
appears.

### P7/N12 closure

R8 order was preserved:

1. Nine candidate phrases were routed against the unchanged router.
2. All nine matched their hypothesized core workflows.
3. Three fixture groups were added.
4. Floors ratcheted from 42/118 and 21/73 to 44/124 and 22/76.
5. No router tune occurred because no boundary failed.
6. The successor decision recorded no core-router integration and a concrete
   re-open trigger.

The permanent invariant is now simpler than the old conditional loophole: pack
names must remain absent from bounded core routing surfaces until a successor
decision explicitly reverses P7.

### Conditional-guard strengthening

T2 parity now scopes assertions to the actual domain-pack appendix and requires
all three EN/zh-TW bullets, both pack identifiers, and the dispatch-still-routes
line. A `reflective-dispatch` mention elsewhere in the zh-TW document can no
longer produce a false pass.

### Linter repair

The linter still inventories every Markdown file. Only:

- `SKILL.md` / skill-frontmatter files receive skill checks;
- Markdown under `00-core`–`06-repo` receives composable-prompt checks;
- other Markdown is classified `document` and does not receive routing-input
  length/danger/Human-Review heuristics.

No dependency, exclusion list, or per-file suppression was added.

## Risks

1. **Seeded routing evidence only.** P7's 9/9 and full ROUTE 100% results are
   regression guards, not proof of general semantic routing.
2. **No usage telemetry.** P6 still depends on the manual usage log; absence is
   `unknown`, not zero.
3. **Intentional future red gate.** After 2026-10-11, tests require
   `plans/checkpoint-2026-10-11-outcome.md`.
4. **Migration tripwires.** Template-set, P7 pack-absence, and Makefile
   composition guards intentionally fail on legitimate changes until their
   decision records and guards migrate together.
5. **Spec size remains a maintenance risk, not a routing warning.** The
   consolidated spec is large, but splitting it would add archive surface. It
   carries explicit compression/retirement triggers; the corrected linter no
   longer mislabels it as a routing input.

## Spec-to-code traceability

| Requirement / risk | Artifact | Executable proof |
| --- | --- | --- |
| Trigger drift must not remain prose-only | Dormant-work spec + checkpoint runbook | dormant watch, conditional, deadman, and spec-parity tests |
| P7 must follow holdout-before-tune | P7 decision + routing ledger | pre-tune 9/9; three fixture groups; no router diff; R8 floor guards |
| Packs remain outside bounded core routing | P7/N12 no-change decision | pack-absence tests across router, fixtures, `VALID_WORKFLOWS`, dispatch |
| Plan/select/executable vocabulary stays distinct | P7 collision groups | nine canonical probe assertions + full ROUTE-002/003 evals |
| T2 future parity must cover the real appendix | T2 dormant spec | section-scoped three-bullet conditional test |
| Docs/plans are not routing inputs | linter classification repair | document/long-document/category-prompt/long-prompt tests |
| 2026-10-11 cannot pass undocumented | checkpoint outcome schema | calendar deadman + outcome-heading contract |
| Roadmap and decision state cannot diverge silently | roadmap/spec/ledger updates | adoption-state and spec self-guards |

## Remaining work

No additional item is currently actionable from repository evidence.

Still deliberately gated:

- **2026-10-11:** P6 pack merge re-litigation and T2 EN-stability/zh-TW parity.
- **Recurrence:** P12 DAG template, P13 multi-wave template, M4 internalization,
  M6 orientation, minimality-default invocation.
- **First real local case:** M7 sensitive-evidence redaction, writer-critic
  deterministic companion, S3 packaging.
- **Second independent signal / boundary evidence:** E2 restructuring, D4
  record-hygiene validator, H3/H4 routing boundaries, localized trigger cues.

Implementing those now would convert `unknown` into fabricated evidence or
silently waive their owning gates. The next mandatory action is the
2026-10-11 checkpoint runbook and outcome record.

## Human review needs

The user's “fix the rest if possible” instruction authorized the P7 re-litigation
and narrow governance/linter repairs. No high-risk Human Review category was
touched: no auth, permission, privacy, migration, billing, public API,
production, destructive operation, runtime side effect, core-skill contract, or
domain-pack contract changed.

Future Human Review remains required where the owning records say so: P6/P7
successor decisions, frozen-core edits, pack-contract edits, E2 destructive
restructuring, and high-risk runtime or side-effect work.
