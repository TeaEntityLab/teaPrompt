# Self-Governance Dogfood Record — 2026-09-24

> **Status: decision record (non-authoritative).** Evidence for the 2026-09-23/24
> self-application of TeaPrompt's own governance surfaces: the
> `verification-map-generator` pack run on this repository (commits `6f43b67`,
> `7d8de92`, `33d7f1a`) and the ROUTING_CONTRACT R13 review-led inspection
> boundary (R8 holdout-first). Durable rules live in `ROUTING_CONTRACT.md` R13,
> the fixtures, and `validate_route_fixture.py`; this file is the audit trail.

## Trigger

User instructions, in order: "using its own skills to govern this project",
"continue", "validate_skill_examples.py then commit", "Fix risky issues",
"Review", "yes do them all", "do them all". The last closed the two residuals
left by the review follow-up: sweep evidence existed only in chat (model-judgment
tier, not persisted), and ROUTE-003 review-led phrases won only by priority
tie-break.

## Part A — Verification map sweeps

Map: root `VERIFY.md`, `features/` (test suite, validators, route evals,
registry), `acceptance.yaml`. Two fresh task agents with no conversation
history drove the map. Each was told to read only the map and to report every
place it was insufficient.

| Arm | Tree | Result | Classification |
| --- | --- | --- | --- |
| Healthy | `c1cdf14` + map | 4/4 areas pass; 1287 tests; 8/8 validator scripts exit 0; 3/3 route evals 100% | none; two doc-drift findings (below) |
| Seeded | `c1cdf14` + map, `reflective-handoff-retro` deleted from `CORE_SKILLS`, no label | doctor FAIL (`validate_governance.py` exit 1: unregistered skill directory); pytest 14 failed / 1270 passed, every failure asserting 8 == 9 or the missing name; registry area FAIL (8 vs 9); route evals pass | product regression on every failing area; root cause traced to the deleted line; `validate_skill_examples.py` exited 0 while printing "All 8 core" |

Map defects found by the arms and their dispositions:

| Finding | Arm | Disposition |
| --- | --- | --- |
| `ls -d skills/*/` counts 15, not 14 (`examples/` is a directory) | healthy | fixed: `find … -mindepth 2 -maxdepth 2 -name SKILL.md` (14) |
| Route-eval group names stale | healthy | false positive: names verified against `route-003-results.json` |
| `cd /Users/teee/dev/teaPrompt` machine-local | seeded | fixed in `33d7f1a`: `cd "$(git rev-parse --show-toplevel)"` |
| `acceptance.yaml` route-evals check ran route-003 only | seeded | fixed in `33d7f1a`: all three fixtures |
| `validate_skill_examples.py` exit 0 masks a registry shrink | seeded | fixed in `6f43b67` (cardinality self-check); pinned by `test_validator_fails_when_core_registry_shrinks` and siblings in `test_validate_skill_examples.py` |

The independent review of `6f43b67` found 11 issues. All were fixed in `7d8de92`
(validator comment scope, hook coverage for root map files, blank lines) and
`33d7f1a` (route-evals coverage, portable `cd`, the lock described as a
convention because git stores mode 100644, the false git-status quirk,
validator and test-file counts, the missing sweep-report pointer, stale
`source_commit`, GNU `find` flag order).

## Part B — R13 review-led inspection tune (R8 holdout-first)

Problem: review-verb-led phrases whose object is a spec or plan tied
`reflective-spec-plan` on raw keywords (`spec`, `plan`, `計畫`) and won only on
the priority list, capped at the 0.45 contested confidence. Roadmap, PRD, and
implementation-plan or release-plan objects also triggered the planning
boundary's "delivery artifact requested" boost and lost outright.

Order of work: fixtures written first, measured pre-tune, router changed,
measured post-tune.

| Fixture group | Expected | Pre-tune | Post-tune |
| --- | --- | --- | --- |
| ROUTE-002 `review_led_artifact_holdout` (4, written unprobed) | review | 2/4 (roadmap, PRD → spec-plan 0.70); 2 at 0.45 tie | 4/4 at 0.80 |
| ROUTE-003 `approved_spec_verify_not_implement_trap` (existing, 3) | review | 3/3 at 0.45 tie | 3/3 at 0.80 |
| ROUTE-003 `review_led_inspection_not_plan_trap` (4) | review | 2/4 (implementation plan 0.80, release plan 0.45 → spec-plan); 2 at 0.45 tie | 4/4 at 0.80 |
| ROUTE-003 `review_led_authoring_not_review_trap` (3) | spec-plan | 3/3 | 3/3 |
| ROUTE-003 `review_led_delivery_not_review_trap` (2) | implement | 2/2 | 2/2 |
| ROUTE-003 `review_verb_catalog_not_review_trap` (3) | dispatch | 3/3 | 3/3 |
| ROUTE-003 `review_led_cut_not_review_trap` (3) | minimality | 3/3 | 3/3 |
| ROUTE-003 `review_led_production_not_review_trap` (2) | risk | 2/2 | 2/2 |

The traps for the other workflows were written before the tune. They cover
every workflow that shares the review verbs or the spec/plan nouns, so a
boundary that stole their phrases would have failed them. All 12 cross-workflow
trap phrases held before and after the tune. After the tune, all three evals
remain at 100%.

Fix (`route_paraphrase_eval.py` `boundary_adjustments`): the boundary fires when
a phrase opens with a review verb and names an existing planning artifact, and
none of these apply: authoring, repository delivery, catalog, no-code, risk
signal, or minimality vocabulary. When it fires, review gets +3 and the planning
boost is suppressed. Floors ratcheted: ROUTE-002 48 groups / 138 phrases,
ROUTE-003 32 groups / 108 phrases.

Probes outside the fixtures (every one recorded, per R8):

| Phrase | Expected | Pre | Post | Disposition |
| --- | --- | --- | --- | --- |
| review the approved spec and tell me what's missing | review | review 0.45 | review 0.80 | holds |
| critique this spec before the team signs off | review | review 0.45 | review 0.80 | holds |
| review the design doc against the requirements and check each claim | review | review 0.45 | review 0.90 | holds |
| 審查這份已核准 spec 並驗證每個主張 | review | review 0.45 | review 0.80 | holds |
| write a spec for the export feature, no code yet | spec-plan | spec-plan 0.45 | spec-plan 0.45 | holds; untouched by R13 |
| turn this approved spec into tickets and acceptance criteria, no code changes | spec-plan | spec-plan 0.90 | spec-plan 0.90 | holds |
| plan the rollout and review checkpoints for the new billing spec, planning only | spec-plan | spec-plan 0.90 | spec-plan 0.90 | holds |
| implement the approved spec in the repository and run the tests | implement | implement 0.90 | implement 0.90 | holds |
| review the design and remove unnecessary complexity | minimality | minimality 0.70 | minimality 0.70 | holds |
| audit the implementation plan for overengineering and trim it | minimality | spec-plan 0.80 | spec-plan 0.80 | **miss, not fixed**: minimality vs planning-boundary collision (`implementation plan` +2); R13 excludes minimality vocabulary, so this tune does not touch it. A separate boundary, to be fixture-backed before any tune |
| review the spec against the upstream RFC and cite sources | research | review 0.45 | review 0.80 | **expectation withdrawn**: reviewing an artifact against a cited source is a defensible review; the research reading was the prober's guess, not a contract rule |

## Evidence

Checked this session, by command output:

- `make all` exit 0 after each commit. Final run: 1290 passed; ROUTE-001/002/003
  at 100%.
- Seeded-registry regression: `validate_skill_examples.main()` returns 1 with
  "CORE_SKILLS has 8 entries, expected 9". Deterministic pytest now pins this;
  before, only an agent's reading showed it.
- Pre/post tables above: `ParaphraseRouter().route()` on each phrase.

[INFERENCE] The healthy-arm and seeded-arm classifications are model judgment
by two fresh agents. They are independent of the author's context but are still
model judgment, not a deterministic channel. The deterministic part (validator
exit code, pytest failures) is now pinned; the classification skill is not.

## Falsifiability

- R13 is wrong if a review-verb-led phrase whose real ask is authoring,
  delivery, catalog, cutting, or a production hazard, and that the exclusions do
  not name, routes to review. The six `review_led_*` groups are the current
  counterexample set.
- The verification map fails its contract if a fresh agent cannot complete the
  sweep unaided, or misclassifies an unlabeled seeded regression.
