# TeaPrompt Quality Gates Implementation Summary

## Overview

This document summarizes the Phase 1 quality gates implemented for TeaPrompt based on the research-backed engineering roadmap. The planned tooling and documentation tasks are implemented, and ROUTE-001 currently passes both the Phase-1 threshold and aspirational target on the expanded YAML-driven paraphrase set.

## Completed Tasks

### 1. Link + Schema Validation ✅

**File:** `reflective-prompt-library/plans/validate_links.py`

**What it does:**
- Validates `ref_file` references
- Validates `ref_snippet` references
- Validates markdown links
- Validates SKILL.md frontmatter schema
- Checks for required frontmatter fields (name, description)

**Results:**
- Latest observed `validate_links.py` scan: 121 files, 0 errors (snapshot-sensitive).
- All links and schema references were valid in that run.

**Usage:**
```bash
python3 reflective-prompt-library/plans/validate_links.py
```

### 2. Prompt/Skill Index Generator ✅

**File:** `reflective-prompt-library/plans/generate_index.py`

**What it does:**
- Generates machine-readable JSON index of all prompts and skills
- Extracts metadata (path, type, category, description)
- Tracks dependencies (ref_file, ref_snippet, markdown links)
- Documents structure (headings hierarchy)
- Categorizes content by library structure

**Results:**
- Current generated index snapshot: 107 total files after `generate_index.py` (2026-07-11 snapshot; includes prompt-library docs, skills, plans records, and the active planning artifacts).
- 2 main categories (prompt-library, skills)
- 10 prompt-library subcategories
- 11 skill subcategories (9 core + 2 registered domain packs)
- Output: `reflective-prompt-library/index.json`

**Usage:**
```bash
python3 reflective-prompt-library/plans/generate_index.py
```

### 3. Prompt/Skill Linter ✅

**File:** `reflective-prompt-library/plans/lint_skills.py`

**What it does:**
- Checks for required skill sections (Module Contract, key subsections)
- Validates frontmatter completeness
- Detects dangerous operation patterns such as recursive deletion or destructive SQL
- Identifies human review trigger patterns (production, auth, secret, etc.)
- Checks skill body length (warns if >500 lines or >20k chars)
- Provides actionable suggestions

**Results:**
- Latest observed lint run: scanned 121 files
- 0 errors, 5 warnings (length warnings on large markdown records)
- 88 files with suggestions (mostly non-critical)
- All 9 skills pass validation

**Usage:**
```bash
python3 reflective-prompt-library/plans/lint_skills.py
```

### 4. Routing Paraphrase Eval ✅

**File:** `reflective-prompt-library/plans/route_paraphrase_eval.py`

**What it does:**
- Implements ROUTE-001 from code-followups-plan.md
- Loads intent groups, adversarial sets, thresholds, trace fields, and expected workflows from `route-001-paraphrase-eval.yaml`
- Applies a small deterministic boundary classifier for ambiguous review/risk/planning and workflow-design phrasing
- Tests routing consistency across paraphrased intents
- Validates that same intent routes to same workflow
- Measures confidence, fallback behavior, low-confidence trace coverage, and silent downgrade incidents
- Generates consistency reports

**Results:**
- Tested 16 groups with 128 paraphrases, including 4 adversarial boundary groups, the minimality gate, and the Test Plan, executable-test, and workflow-design boundaries
- Overall consistency: 100.0% (passes Phase-1 threshold >=70% and aspirational target >=95%)
- Low-confidence route trace coverage: 100.0%
- Adversarial groups now pass through boundary rules rather than isolated synonym matching
- Output: `plans/route-001-results.json`

**Key Finding:** ROUTE-001 is now a fixture-driven quality gate rather than a hardcoded self-test. The router still remains deterministic and seeded, so the current result proves coverage of the defined boundary cases; it does not prove general semantic routing quality.

**Usage:**
```bash
python3 reflective-prompt-library/plans/route_paraphrase_eval.py
```

### 4.1 Holdout Routing Eval ✅

**File:** `reflective-prompt-library/plans/route-002-holdout-eval.yaml`

**What it does:**
- Adds an unseen holdout fixture separate from ROUTE-001 tuning cases
- Reuses `route_paraphrase_eval.py` with an explicit config path
- Measures whether boundary routing generalizes beyond the seeded examples
- Keeps a lower Phase-1 bar and separate aspirational target to avoid over-claiming

**Results:**
- Tested 40 holdout groups with 114 paraphrases
- Overall consistency: 100.0% (passes Phase-1 threshold >=80% and aspirational target >=90%)
- Low-confidence route trace coverage: 100.0%
- Review, clarification, workflow-design, workflow-implementation, research, and orchestration-selection phrasing now pass through boundary concepts
- Output: `plans/route-002-results.json`

**Usage:**
```bash
python3 reflective-prompt-library/plans/route_paraphrase_eval.py reflective-prompt-library/plans/route-002-holdout-eval.yaml
```

### 5. Lightweight Governance Metadata ✅

**Files:** All 9 SKILL.md files updated

**What was added:**
- `risk_level`: low/medium/high
- `human_review_required`: true/false
- `external_io`: true/false
- `context_load`: low/medium/high

Field semantics: `external_io: true` means the skill expects the agent to reach outside the repository by default (web, DeepWiki, external APIs) — local file edits are not external IO. `human_review_required: true` means review gates the skill's core flow by default; conditional body-level triggers (e.g. auth/production escalation inside `reflective-implement`) are escalations, not frontmatter defaults.

**Applied to (risk_level, human_review_required, external_io, context_load):**
- reflective-dispatch (low, false, false, low)
- reflective-brief (low, false, false, low)
- reflective-spec-plan (low, false, false, high)
- reflective-implement (low, false, false, medium)
- reflective-review (low, false, false, medium)
- reflective-minimality (low, false, false, low)
- reflective-research (low, false, true, high)
- reflective-risk (high, true, false, medium)
- reflective-handoff-retro (low, false, false, medium)

**Validation:** Created `validate_governance.py` to ensure compliance

**Usage:**
```bash
python3 reflective-prompt-library/plans/validate_governance.py
```

### 6. CONTRIBUTING.md ✅

**File:** `CONTRIBUTING.md` (project root)

**What it includes:**
- Project philosophy and quality standards
- Prompt and skill quality requirements
- Technical requirements (links, frontmatter, length)
- Contribution process (fork, validate, submit, review)
- Quality gates (required vs recommended)
- Types of contributions (prompts, skills, docs, tooling)
- Language policy
- Testing guidelines
- Style guidelines

**Key sections:**
- Quality standards with specific requirements
- Step-by-step contribution process
- Automated validation commands
- Review process explanation
- Testing guidelines

### 7.1 Benchmark Fixture Validator ✅

**File:** `reflective-prompt-library/plans/validate_benchmark_fixture.py`

**What it does:**
- Validates golden-task shape in `benchmark_tasks.py` (workflow, criteria, uniqueness)
- Regenerates `benchmark-tasks.json` for local/manual runs
- Runs in `make validate` — **does not** execute LLM benchmark comparisons

**Usage:**
```bash
python3 reflective-prompt-library/plans/validate_benchmark_fixture.py
```

### 7.2 Skill Examples Validator ✅

**File:** `reflective-prompt-library/plans/validate_skill_examples.py`

**What it does:**
- Ensures each of the nine core skills has `skills/examples/<skill>.examples.md`
- Minimum content length gate (200 chars)

**Usage:**
```bash
python3 reflective-prompt-library/plans/validate_skill_examples.py
```

### 7.3 ROUTE-003 Adversarial Eval ✅
**File:** `reflective-prompt-library/plans/route-003-adversarial-eval.yaml`

**What it does:**
- Fresh adversarial boundary phrasing separate from ROUTE-001 tuning cases and ROUTE-002 holdout phrases
- Reuses `route_paraphrase_eval.py` with an explicit config path
- Third routing gate in `make validate`; catches regressions on traps such as implement-vs-plan, plain-review vs risk, multi-voice research, and mixed-language phrasing
- Post-panel maintenance: ROUTING_CONTRACT **R11** approved-spec delivery (`implement_not_plan_trap`) at 100%

**Results:**
- Tested 19 adversarial groups with 66 paraphrases
- Overall consistency: 100.0% (passes Phase-1 threshold >=80% and aspirational target >=90%)
- Low-confidence route trace coverage: 100.0%
- Output: `plans/route-003-results.json`

**Usage:**
```bash
python3 reflective-prompt-library/plans/route_paraphrase_eval.py reflective-prompt-library/plans/route-003-adversarial-eval.yaml
```

### 7.4 Route Fixture Gate ✅

**File:** `reflective-prompt-library/plans/validate_route_fixture.py`

**What it does:**
- Enforces minimum ROUTE-001/002/003 group and phrase counts before paraphrase eval runs
- Current minimums: ROUTE-001 (12 intent + 4 adversarial groups, 128 phrases); ROUTE-002 (40 holdout groups, 114 phrases); ROUTE-003 (19 adversarial groups, 66 phrases)
- Round 22 panel compromise: deterministic hygiene without YAML dependency explosion
- Integrated in `make validate` after skill examples gate; mirrored by pytest in `test_validate_route_fixture.py`
- Cheatsheet parity anti-drift: `test_cheatsheet_boundary_quick_cues.py` (R12 quick-cue summary), `test_cheatsheet_*_parity.py` (holdout probe cues in EN/zh-TW cheatsheets)

**Usage:**
```bash
python3 reflective-prompt-library/plans/validate_route_fixture.py
```

### 7. Small Benchmark Set ✅

**File:** `reflective-prompt-library/plans/benchmark_tasks.py`

**What it does:**
- Defines 24 golden tasks for validation
- Covers all nine frozen workflow skills
- Balanced difficulty distribution (6 easy, 11 medium, 7 hard)
- Diverse categories (15 different categories)
- Clear acceptance criteria for each task
- Expected workflow mapping

**Results:**
- 24 benchmark tasks created
- Tasks cover: routing, implementation, planning, review, research, risk, handoff, debugging, refactoring, retrospective, runtime governance, scaffold provenance, SOP compiler planning, minimality, test planning, and workflow design
- Output: `plans/benchmark-tasks.json`

**Usage:**
```bash
# CI: fixture shape only
python3 reflective-prompt-library/plans/validate_benchmark_fixture.py

# Manual (optional, LLM-cost): compare baseline vs skill-assisted runs
python3 reflective-prompt-library/plans/benchmark_tasks.py
```

## Research Alignment

The implementation aligns with research findings:

1. **Quality over quantity** - TeaPrompt maintains a compact generated index (92 files after regeneration) vs thousands in other repos.
2. **Hierarchical organization** - 7 prompt-source directories plus skills/plans map onto the 10-layer taxonomy.
3. **Focused skills** - nine frozen workflow skills (including reflective-minimality gate) vs comprehensive documentation
4. **Validation discipline** - Automated quality gates catch structural regressions; semantic quality still needs review evidence.
5. **Lightweight governance** - 4 governance fields (`risk_level`, `human_review_required`, `external_io`, `context_load`)

## Key Metrics

| Metric | Value | Status |
|--------|-------|--------|
| Files validated | 121 snapshot | ✅ 0 link/schema errors in latest observed run |
| Links validated | 0 broken | ✅ Pass |
| Skills with governance | 9/9 | ✅ 4-field governance metadata complete |
| Benchmark tasks | 24 | ✅ Ready |
| Routing consistency | 100.0% | ✅ ROUTE-001 seeded deterministic ParaphraseRouter fixture, not live dispatch proof |
| Holdout routing consistency | 100.0% | ✅ ROUTE-002 (40 groups, 114 paraphrases), seeded holdout fixture |
| Adversarial routing consistency | 100.0% | ✅ ROUTE-003 (19 groups, 66 paraphrases), seeded adversarial fixture |
| Skill example coverage | 9/9 | ✅ validate_skill_examples.py |
| Linting | 0 errors / 5 warnings | ✅ Errors clean; warnings tracked separately |

Evidence tiers (see `GLOSSARY.md` Evidence Tier): ROUTE metrics above are regression-guard tier (seeded deterministic fixtures); panel consensus records are advisory/model-vote tier; external survey and maintainer benchmark numbers are non-load-bearing unless independently reproduced.

### Routing Consistency Tracking

The current routing consistency measurement is 100.0% on ROUTE-001 across 16 groups and 128 paraphrases. The eval fixture is now the single source of truth for thresholds, expected workflows, trace fields, and adversarial sets, while `route_paraphrase_eval.py` is responsible for loading the fixture and measuring the current router. This passes the Phase-1 threshold (>=70%) and aspirational target (>=95%) for the expanded seeded boundary set, including the minimality gate and the Test Plan, executable-test, and workflow-design boundaries. The ROUTING_CONTRACT.md keeps both bars explicit so future evals can distinguish minimum acceptance from aspirational quality.

### Critical Reflection

ROUTE-001 should not be interpreted as proof that routing is solved. The useful project direction is not to keep adding isolated synonyms until the score is perfect, but to keep a compact fixture that exposes meaningful intent boundaries:
- implementation vs spec planning (including approved-spec delivery in repository)
- review vs risk gating
- research vs local review
- clarification vs planning
- handoff vs dispatch
- workflow design vs executable orchestration
- workflow research or review vs first-draft design
- workflow formalization selection vs committing to a workflow

The latest router improvement uses concept-level boundary rules for these cases instead of raw synonym accumulation. Future improvements should add unseen holdout cases or baseline-vs-skill evaluation before claiming general routing quality.

### Holdout Tracking

ROUTE-002 measures unseen phrasing separately from ROUTE-001. Round 7 (2026-06-25) added Traditional Chinese holdout groups with matching router intent keywords — fairness test without full `SKILL.md` translation. Round 65 expanded to 36 holdout groups; post-Round 68 maintenance added ROUTING_CONTRACT **R11** boundaries (102 ROUTE-002 phrases, 15 ROUTE-003 adversarial groups / 53 phrases including `implement_not_plan_trap`, `approved_spec_plan_not_implement_trap`, `dispatch_meta_skill_trap`, and `minimality_not_implement_trap`) at 100%. The 2026-07-06 post-goals review raised the floor to 40 ROUTE-002 groups / 114 ROUTE-002 phrases and 18 ROUTE-003 adversarial groups / 62 phrases, covering promotion routing, runtime-trust side effects, scaffold provenance, dependency deletion, and zh-TW context-load deferral; the 2026-07-11 verifier-artifact expansion raised ROUTE-003 to 19 ROUTE-003 adversarial groups / 66 phrases (`verifier_artifact_not_runner_trap`, fixture added before the matching router boundary per holdout-before-tune). Treat this as a seeded holdout, not proof of broad semantic routing; add fresh cases before further router tuning.

## Phase 2 Status (post-Round 68 maintenance)

### Done ✅

1. **CI/CD** — `.github/workflows/python-tools.yml` runs `make all` on push/PR
2. **ROUTE-001/002/003 in CI** — 128 + 114 + 66 paraphrases at 100% consistency (seeded fixtures); `validate_route_fixture.py` gates minimum coverage
3. **Governance validators** — links, lint, governance metadata, PROJECT_KNOWLEDGE, benchmark fixture, skill examples
4. **Harness policy docs** — CONTRIBUTING, AGENTS, SKILL_INSTALLATION, maintenance playbook
5. **Doc anti-drift** — `test_routing_contract.py`, cheatsheet parity tests, `test_readme_governance.py`, `test_thinking_prompts_eval_harness.py`, `test_engineering_prompts_eval_harness.py`, `test_prompt_cross_links.py`, `test_core_prompts_eval_harness.py`, `test_human_review_library_registry.py`, `test_prompt_skill_links_library_registry.py`, `test_prompt_contract_library_registry.py`, `test_prompt_primary_workflow_surface_library_registry.py`, `test_workflow_skill_coverage_library_registry.py`, `test_prompt_eval_harness_score_library_registry.py`, `test_prompt_workflow_skill_reference_library_registry.py`, `test_prompt_eval_harness_fixture_library_registry.py`, `test_prompt_category_paths_library_registry.py`, `test_prompt_library_registry_helpers_library_registry.py`, `test_prompt_governance_surface_paths_library_registry.py`, `test_agent_prompts_eval_harness.py`, `test_context_prompts_eval_harness.py`, `test_domain_prompts_eval_harness.py`, `test_repo_prompts_eval_harness.py`, `test_validate_governance.py`, `test_validate_links.py`, `test_lint_skills.py`, `test_skill_module_contract.py` (Escalation subsection + Trigger/Methods/Output/Never; 762+ pytest anti-drift suite in CI); reciprocal thinking-lens ↔ skill checks and `00-core` + composable `Primary workflow surface(s)` ↔ `*_SKILL_LINKS` parity in `test_prompt_cross_links.py` (including strict Primary workflow surfaces parity via `test_thinking_lens_primary_surfaces_match_consumer_graph`); Human Review + Escalation route-target guards in thinking/skill contract tests; composable `Primary workflow surface(s)` / Supporting-lens preamble guards and composable `## Human Review` preamble guards (route to `reflective-risk`) via `prompt_eval_helpers.assert_human_review_preamble` in `test_*_prompts_eval_harness.py`; frozen `*_HUMAN_REVIEW_REQUIRED` / `*_HUMAN_REVIEW_EXEMPT` set parity across all prompt categories (Round 90); library-wide contract heading registry (`PROMPT_CONTRACT_HEADINGS`, Round 93); workflow skill coverage registry (`*_COVER_WORKFLOW_SKILLS`, Round 95); eval_harness score floor registry (`PROMPT_EVAL_MIN_SCORE`, Round 96); workflow skill reference registry (`assert_prompt_references_workflow_skill`, Round 97); eval_harness fixture registry (`make_category_eval_harness_fixture`, Round 98); category path registry (`category_prompt_dir` / `sorted_category_prompts`, Round 99); library registry helper registry (`assert_registry_matches_library_glob`, Round 100); governance surface path registry (`cheatsheet_en_path` / `glossary_path`, Round 101); workflow skill reference helper preamble-aligned (Round 99); library registry helper DRY (`assert_library_wide_unique_basenames` / `assert_registry_matches_library_glob`, Round 100)

### Ongoing maintenance (not blockers)

1. **Continue ROUTE-002/003 holdout expansion** before any router tuning — add fresh phrases first, then adjust rules only if a meaningful boundary fails
2. **Collect feedback** — CONTRIBUTING.md process
3. **Monitor** — undocumented-decision warnings from `validate_project_knowledge.py`

### Recurrence-gated (deferred by panel consensus)

1. **Manual benchmark runs** — `benchmark_tasks.py`; not in CI (non-deterministic / LLM-cost)
2. **Default minimality in implement** — needs three cross-session recurrences; signal scan active
3. **Full SKILL.md i18n** — rejected; cheatsheet + glossary + router keywords suffice
4. **Tenth core skill** — rejected without promotion gate evidence

See [panel Recurrence-Gated Backlog](multi-agent-panel-consensus-2026-06-25.md#recurrence-gated-backlog-not-panel-blockers).

## Files Created/Modified

**Created:**
- `reflective-prompt-library/plans/validate_links.py`
- `reflective-prompt-library/plans/generate_index.py`
- `reflective-prompt-library/plans/lint_skills.py`
- `reflective-prompt-library/plans/route_paraphrase_eval.py`
- `reflective-prompt-library/plans/validate_governance.py`
- `reflective-prompt-library/plans/benchmark_tasks.py`
- `CONTRIBUTING.md`
- `reflective-prompt-library/plans/QUALITY_GATES_SUMMARY.md`

**Committed generated artifact:**
- `reflective-prompt-library/index.json` (uses relative paths, safe to commit; regenerate with `python3 reflective-prompt-library/plans/generate_index.py`; not run by `make validate`)

**Generated (gitignored run outputs):**
- `reflective-prompt-library/plans/route-*-results.json` (test results)
- `reflective-prompt-library/plans/benchmark-tasks.json` (test data)

**Modified:**
- All 9 SKILL.md files (governance metadata covered)
- `.gitignore` (added entries for generated test files)

## Validation Commands

To refresh the committed catalog and validate the entire project:

```bash
# 1. Regenerate committed prompt/skill index when docs, skills, or plans change
python3 reflective-prompt-library/plans/generate_index.py

# 2. Run the full CI-equivalent gate
make all
```

`make all` runs pytest plus link/schema validation, linting, governance metadata checks, project-knowledge validation, benchmark fixture validation, skill-example validation, route fixture validation, and ROUTE-001/002/003 deterministic routing evals.

## Conclusion

Phase 1 quality-gate tooling and documentation are **complete**. Routing consistency on seeded fixtures (ROUTE-001 tuning, ROUTE-002 holdout, ROUTE-003 adversarial) is at **100%** as of Round 68 (R11 approved-spec delivery + R12 boundary quick-cue maintenance); treat this as regression protection, not proof of broad semantic routing. TeaPrompt has:

- ✅ Automated validation to prevent quality degradation
- ✅ Machine-readable index for tool integration
- ✅ Governance metadata for risk management
- ✅ Clear contribution process
- ✅ Benchmark fixture gate plus optional manual benchmark runs
- ✅ Research-backed design decisions

The project is positioned to grow sustainably with quality discipline built in from the start. No blocking validation failures remain from panel Rounds 1–101; non-blocking governance warnings should still be resolved through Decision Index hygiene. The standing quality discipline is **holdout expansion before router tuning** (floors last raised 2026-07-06: ROUTE-002 40 groups / 114 phrases, ROUTE-003 19 groups / 66 phrases) and optional manual baseline-vs-skill benchmark runs — not shipping new core skills without promotion evidence.
