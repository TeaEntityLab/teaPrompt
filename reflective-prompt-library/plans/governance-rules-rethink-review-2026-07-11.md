# Governance Rules Rethink Review — 2026-07-11

## Purpose

Record the parallel-lens discussion and decision for the request: **"Rethink all principles/rules of this repo — are they reasonable or do they need modification? Review all skills, plans, and surveys."**

This record is governance / methodology evidence. It is not a standard, a compliance guide, a runtime commitment, or an agent operating rule. Any change it proposes is a candidate; none is applied by this record alone. Structural deletions and harness-policy rewrites additionally require explicit human approval per the promotion/authority rules.

## Panel Packet

The review used the `parallel-lens-review-packet` protocol. A temporary shared evidence packet was written to the repo root (`review-packet-governance-rethink-2026-07-11.md`, deleted after synthesis) with key evidence embedded in each reviewer assignment. The packet separated observed repository evidence, author-claimed evidence, and `[INFERENCE]`.

State at review time:

- Branch `main`, commit `9f571f2`, working tree clean, local date 2026-07-11.
- Executed this session before fan-out: `make all` from repo root — 732 pytest tests passed (~2.2s); all validators passed; ROUTE-001 (16 groups / 128 phrases), ROUTE-002 (40 / 114), ROUTE-003 (18 / 62) all at 100% consistency.
- Observed this session: `make all` fails from `reflective-prompt-library/` ("No rule to make target 'all'") because the only Makefile is at repo root, while [06-repo/AGENTS.md](../06-repo/AGENTS.md) says "Run `make all`" with no directory qualifier.

## Panel Lenses

Seven reviewer lenses ran as parallel same-host subagent workers (no claim of distinct provider personas). All seven returned `AGREE WITH CHANGES`; none returned `AGREE` or `DISAGREE`:

- Constitutional principles auditor
- Skill contract & routing boundary reviewer
- Decision-record & drift auditor
- Survey evidence & provenance reviewer
- Validator & test-suite effectiveness reviewer
- Newcomer / host-agent usability reviewer
- Adversarial minimality & deletion reviewer

## Panel Consensus

**Decision:** `AGREE WITH CHANGES`

**Core finding:** The principles and rules themselves remain reasonable — the nine-skill surface, no-owned-runtime default, local-gap adoption gate, holdout-before-tune, prompt-vs-runtime enforcement split, non-authoritative project-knowledge boundary, minimality gates, and evidence-over-confidence discipline are safety floors. **No lens proposed removing or loosening any constraint.** The defects are operational: candidate-adoption drift with no tracker, dual-authority ambiguity at the repo root, an oversized and unenforced Required Workflow, wording-parity gaps, ~10% doc-echo tests guarding phrases while named governance gaps go unguarded, and archive growth that violates the repo's own map-not-archive and minimality standards.

**Use-case recommendation:**

| Use case | Recommendation |
| --- | --- |
| `study` | Keep surveying external runtimes, memory systems, and workflows as reference material; record hygiene is already strong (OpenFugu record is the internal gold standard). |
| `reproduce` | Unchanged from 2026-07-06: sandbox-only; mock/sandbox success is not deploy evidence. |
| `adopt` | Fold ideas into existing prompts, lenses, SOPs, or skill-plus-verifier; adoption of THIS review's candidates requires the ledger mechanism below so drift is visible. |
| `deploy` | Unchanged: runtime only for prompt-impossible guarantees with host-runtime enforcement proof. |

## 2026-07-06 Candidate Adoption State (T1 — the top finding)

The [2026-07-06 workflow review](workflow-possibilities-constraints-review-2026-07-06.md) proposed five wording candidates and declared itself wrong "if the five candidate wording changes are never adopted and never re-litigated." Observed adoption state on 2026-07-11:

| # | Candidate | State | Evidence (observed) |
| --- | --- | --- | --- |
| 1 | Qualify "frozen" at high-traffic entry points | PARTIAL | Gloss present: `skills/skill-map.md:10`, `reflective-dispatch/SKILL.md:82`. Absent: `METHODOLOGY_MAP.md` (3 sites), `06-repo/AGENTS.md`, `PROJECT_KNOWLEDGE.md` Standing Non-Goals |
| 2 | Disambiguate three L-ladders in GLOSSARY | NOT APPLIED | No "Acquisition L" in `GLOSSARY.md`; ladder exists only in `04-agent/workflow-acquisition.md:117-123` |
| 3 | Surface L3 verifier path in routing | PARTIAL | Applied: dispatch Route row (`SKILL.md:73`). Absent: `04-agent/workflow-recipes.md` note, cheatsheet quick cue, ROUTE probe |
| 4 | Fail-closed security gates at L3 | NOT APPLIED | No prompt-injection / supply-chain / memory-write-provenance checklist in `04-agent/artifact-promotion.md` or the runtime-legitimacy record |
| 5 | Explicit evidence tiering | NOT APPLIED at governance layer | Tiers exist only inside `reflective-review/SKILL.md`; absent from `GLOSSARY.md`, `QUALITY_GATES_SUMMARY.md`, `PROJECT_KNOWLEDGE.md` |

**Classification (three lenses independently):** a missing tracking mechanism that had begun reading as governance failure. **This review is the re-litigation the falsifiability clause demanded**, so the 07-06 record's falsifier is discharged — provided the ledger mechanism below is adopted so the same drift cannot recur silently.

## Constraints Judged Reasonable (keep, unchanged)

- Nine compact workflow skills, recurrence-gated for a tenth ("frozen means gated, not never").
- No TeaPrompt-owned runtime/swarm/recorder/replay/side-effect enforcer; runtime only for prompt-impossible guarantees with enforcement proof.
- Local-gap gate for external adoption; reference-only records with promotion-time re-verification (event-gated, not calendar-gated).
- Holdout-before-tune; seeded ROUTE fixtures as regression guards, never semantic-routing proof.
- Non-authoritative `PROJECT_KNOWLEDGE.md` boundary with mechanical validation.
- Human Review / no-go when a required gate cannot be deterministically enforced.
- Anti-cheating rules and evidence-over-confidence discipline.

## Required Changes (candidates; not applied by this record)

### A. Adoption integrity (highest priority)

- **A1. Adoption ledger mechanism.** Every panel record that proposes candidates gets a `Candidate Adoption Ledger` table (ID / wording / status adopted-partial-deferred / evidence / next action / review trigger), and the matching Decision Index line states per-candidate status instead of "candidates". Mirror: one-line status update at `PROJECT_KNOWLEDGE.md` Decision Index 2026-07-06 entry.
- **A2. Disposition each open 07-06 candidate explicitly** (adopt or record deferral with trigger): #1 gloss at `METHODOLOGY_MAP.md` 3 sites + `06-repo/AGENTS.md`; #2 Acquisition-L paragraph in `GLOSSARY.md` + METHODOLOGY_MAP Level Taxonomy row; #3 second half (see disputed E4 below — mutually exclusive with folding `workflow-recipes.md`); #4 L3 fail-close checklist in `artifact-promotion.md` + `workflow-acquisition.md` L3 row; #5 evidence-tier labels in `GLOSSARY.md` + `QUALITY_GATES_SUMMARY.md`.
- **A3. Guard test** (`test_candidate_adoption_state.py` or equivalent): assert ledger rows exist and adopted candidates' wording is actually present at the named surfaces.

### B. Authority and usability

- **B1. Root `AGENTS.md` becomes an authority stub.** Explicit read-order header (system/user → `06-repo/AGENTS.md` canonical harness policy → invoked `SKILL.md` → non-authoritative `PROJECT_KNOWLEDGE.md`); claude-mem block labeled historical context only, never an operating-rule source. Removes the "active repository instruction file" ambiguity against `06-repo/AGENTS.md:164-165` ("the only repository sources of agent operating rules").
- **B2. Strictness-scale the Required Workflow** in `06-repo/AGENTS.md:58-94`: L1 no pre-read bundle and no final-report file; L2 relevant-docs-only + chat evidence; L3 full seven-field artifact set + skill Final Report (file optional unless cross-session); L4+ full set + `review/final-report.md` + Human Review triggers. Resolves the observed self-contradiction with the same file's Context Engineering section ("reading only relevant files") and the GLOSSARY context-load deferral rule. Harness-policy change → Human Review required.
- **B3. `make all` path fix:** qualify "from the repository root" at `06-repo/AGENTS.md:54` and `README.md`; optional delegating `reflective-prompt-library/Makefile` (`all: $(MAKE) -C .. all`).
- **B4. README non-goals refresh:** `reflective-prompt-library/README.md` non-goals summary omits the regression-guard caveat, methodology≠operational split, and runtime-guarantee declaration boundary.

### C. Wording parity and labels

- **C1.** `reflective-handoff-retro/SKILL.md:129` "gated-not-never" → dispatch wording "frozen means gated, not never".
- **C2.** `reflective-brief/SKILL.md`: delete the Never sentence duplicated in Operating Rules (keep the Never section as canonical).
- **C3.** Define `external_io` semantics once (skill expects agent to reach outside the repo by default — web/DeepWiki/APIs; file edits are not external_io) in `QUALITY_GATES_SUMMARY.md` or the `validate_governance.py` docstring.
- **C4.** `reflective-implement` frontmatter `human_review_required: false` vs body Human-Review-on-auth/production: gloss frontmatter as the default case with body triggers as conditional escalation.
- **C5.** Cheatsheet quick cue for the L3-verifier route (EN + zh-TW) plus a ROUTE-003 probe for verifier-artifact task shapes; also surface R9 production-negation / R10 brief-before-plan / R11 approved-spec in the dispatch Route table or an explicit pointer to `ROUTING_CONTRACT.md`.
- **C6.** `ROUTING_CONTRACT.md` "current measured: 100.0%" gets the inline caveat "(seeded deterministic fixture; not semantic routing proof)".
- **C7.** `plans/harness-1-state-ledger-research.md` status line: "Implemented" conflates shipped prompt patterns with unreplicated upstream performance claims — relabel "Prompt pattern implemented; upstream performance claims author-reported / non-load-bearing".
- **C8.** `surveys/ornith-1.0-survey.md`: add record-class line "reference-only survey; benchmark numbers non-load-bearing unless independently reproduced".
- **C9.** `QUALITY_GATES_SUMMARY.md` snapshot hygiene: label the 121-file lint and 92-file index counts as snapshot-dated (live `index.json` observed at 94); refresh the stale "next target: holdout expansion" conclusion (expansion already done 2026-07-06).
- **C10.** `PROJECT_KNOWLEDGE.md:29` Principle 5 pointer: add `06-repo/AGENTS.md` § Anti-cheating Rules alongside `critical-thinking-check.md` (claim audit vs execution claims).

### D. Test mechanism (replace phrase-pins with contract checks)

- **D1.** Five literal-phrase assertion sites for "nine frozen workflow skills" (`test_readme_governance.py:81,87`; `test_quality_gates_summary.py:121,126`; `test_validate_benchmark_fixture.py:134`) → replace with `len(CORE_SKILLS)==9` + gloss-presence regex at high-traffic surfaces. Named tautologies: `test_methodology_map_en_lists_nine_frozen_skills`, `test_routing_contract.py` heading pins, `test_repo_prompts_eval_harness.py` asserting the string "make all" appears in prose.
- **D2.** Named missing guards: candidate adoption state (A3), make-all path claim, frozen-gloss parity across entry points, Required Workflow artifact observability.
- **D3.** Packet correction (evidence beat the packet): `test_skill_module_contract.py` does **not** assert the literal frozen phrase; it checks Module Contract structure and escalation targets. The 07-06 record's note listing it among literal-phrase asserters is wrong on that one file.
- **D4.** No validator checks research-record hygiene (judgment-artifact disclaimer, evidence-vs-inference block, fact-check date). Optional low-cost lint extension; record quality is currently convention-only and has held (all eight audited records passed with only C7/C8 label fixes).

### E. Archive hygiene (recurrence-gated; human approval required; disputed scope)

- **E1.** `PROJECT_KNOWLEDGE.md` Decision Index has ~70 dated entries, ~60% panel-round lines, an out-of-order Round 85–101 block, and the map-not-archive blockquote interrupting the list at :115-117. Candidate: collapse Rounds 77–101 (or 8–101) into rollup lines; move the disclaimer above or below the whole index.
- **E2.** `plans/multi-agent-panel-consensus-2026-06-25.md` (3,149 lines; 42% of all plans markdown): demote round-by-round transcript bodies to an archive; keep a ~300-line verdict index. Rounds 1–6 shipped consumer-wired behavior; Rounds 7–101 shipped test-registry DRY with no runtime consumer since.
- **E3.** Merge-then-archive candidates (conservative list): technical briefs into their research records (openfugu ×2, vllm ×1); the three 2026-06-25 surveys into `external-adoption-case-studies`; early-June reflections retired with archive headers. Do-not-delete floor: `ROUTING_CONTRACT.md`, `QUALITY_GATES_SUMMARY.md`, both 07-06 records, five-layer record, external-adoption case studies, panel verdict index, authority-promotion decision.
- **E4. Disputed (needs human decision):** minimality lens additionally proposes merging 00-core clusters (only `core-short.md` has a skill Prompt Sources consumer; 8 of 9 core prompts have none), merging `03-context/low-token.md`+`small-context.md`, and folding `04-agent/workflow-recipes.md` (zero inbound refs from skills/dispatch/cheatsheet) into `METHODOLOGY_MAP.md`. Counter-steelman: `METHODOLOGY_MAP.md` explicitly rejects a single master prompt — multiplicity is policy (host character caps, zh-TW, daily/important variants), and recipes are operator-greppable composition guidance. Note the interaction: folding recipes and applying candidate #3's recipes-note are mutually exclusive — pick one destination for the L3 note.

## Shared Findings

1. All constraints survive adversarial review; every lens converged on `AGREE WITH CHANGES` for operations, not rules.
2. The adoption pipeline is the weakest link: the repo documents decisions better than it maintains them (partial, untracked candidate adoption; stale Decision Index wording; no guard test).
3. Authority is clear inside `reflective-prompt-library/` and murky at the repo root (stub vs snapshot vs canonical policy).
4. The Required Workflow contradicts the repo's own context-engineering and strictness-deferral principles and is enforced nowhere.
5. Meta:product ratio observed at ~2.45:1 by lines (product 7,418; meta ~18,158; tests 4,668 > all skills 2,390; one panel transcript > all 00-core combined). For a discipline library some overweight is the point; the panel-transcript sediment and doc-echo tests are not.
6. Evidence hygiene in research records is strong and consistent; no surveyed benchmark number is load-bearing in live docs (verified by grep); the two label fixes (C7, C8) are the only corrections.
7. Routing is healthy at the fixture level (100% on three gates, verified this session) with five concrete boundary gaps (C5, plus research-vs-spec-plan ambiguity, debug-without-edits fallthrough, promotion-vs-retro ambiguity) — fixture-level truth, not semantic proof.

## Disagreements / Residual Risks

- **Archival scope:** minimality lens wants ~20 records archived plus core/context merges; plans auditor holds a conservative do-not-delete floor with merge-then-archive; the steelman for keeping everything (meta-layer IS the product; multiplicity is policy; 2.2s test runtime is cheap insurance) was recorded and not refuted on cost grounds. All structural deletions stay recurrence-gated with explicit human approval.
- **No operator-toil dataset exists**, so every "this rule causes friction" claim above the observed-contradiction level remains `[INFERENCE]`; by the repo's own three-recurrence gate, relaxations need the same evidence as promotions.
- **B2 (Required Workflow rewrite) changes agent operating rules** — it must go through Human Review, not silent adoption.
- Same-host panel caveat: seven lenses ran as same-host subagent workers; consensus is advisory / model-vote-tier evidence, not operational proof (consistent with candidate #5's tiering).

## Evidence Actually Checked

- Executed (this session, read-only + validators): `make all` from repo root (732 tests, all validators, three ROUTE gates green); `make all` failure from `reflective-prompt-library/`; `git log`/`status`/`branch`; greps verifying candidate adoption state (frozen gloss, Acquisition-L, fail-close wording, evidence-tier labels, workflow-recipes L3 note); direct reads of `PROJECT_KNOWLEDGE.md`, `06-repo/AGENTS.md`, `reflective-dispatch/SKILL.md`, `QUALITY_GATES_SUMMARY.md`, `Makefile`, `workflow-possibilities-constraints-review-2026-07-06.md`.
- Lens-verified (subagent reads/greps this session, reported with file:line): all nine SKILL.md files, skill-map, cheatsheets (EN/zh-TW), GLOSSARY, METHODOLOGY_MAP, READMEs, LANGUAGE_POLICY, SKILL_INSTALLATION, 04-agent lenses inbound-reference counts, ~22 of 41 test modules, validators, ROUTE yaml fixtures, eight research/survey records, plans drift checks, wc-based size measurements.
- Author-claimed, not reproduced: historical panel-round outcomes, upstream survey source contents, Ornith/Harness-1/vLLM benchmark numbers.
- Not run: LLM benchmark comparisons; fresh external web recency checks on surveyed tools.

## Falsifiability

This record is wrong if: (a) the adoption-ledger mechanism (A1/A3) is adopted and drift still recurs silently; (b) a constraint reaffirmed here blocks a verified recurring workflow that meets the promotion gate; (c) operator-usage evidence shows the Required Workflow as written is followed at L1-L2 without the predicted toil; or (d) the disputed E4 merges are executed and the predicted losses (host-variant discoverability, recipe greppability) do not materialize — which would mean the conservative floor was too conservative. Any of these means correct the relevant judgment and record the outcome.

## Adoption Update (2026-07-11)

User-approved application of tiers A and C plus B3 in the same session:

- A1/A3: Candidate Adoption Ledger added to the 2026-07-06 record; guard test `plans/tests/test_candidate_adoption_state.py` added; Decision Index entries updated with per-candidate status.
- A2: candidates #1, #2, #4, #5 adopted at their named surfaces; #3 remains partial — dispatch Route row and EN/zh-TW cheatsheet quick cues adopted, `workflow-recipes.md` note deferred pending the E4 fold-vs-annotate decision; the ROUTE-003 verifier-artifact probe is deferred until the router grows a verifier-artifact concept.
- C1–C10 applied: handoff-retro gloss alignment, brief Never dedupe, `external_io`/`human_review_required` semantics in QUALITY_GATES_SUMMARY §5, cheatsheet L3 quick cues + dispatch contract-boundaries pointer, ROUTING_CONTRACT fixture caveat, harness-1 status relabel, Ornith record-class line, QUALITY_GATES snapshot labels (index snapshot 95) + conclusion refresh + pytest floor 740+, PROJECT_KNOWLEDGE Principle 5 dual pointer.
- B3 applied: `make all` qualified with "from the repository root" in `06-repo/AGENTS.md`, the library README, and the GLOSSARY playbook.
- Still open (human-gated): B1 root AGENTS.md authority stub, B2 strictness-scaled Required Workflow, B4 README non-goals refresh, all of E (archive/merge/demote), D1 literal-phrase test-pin replacement, D4 record-hygiene lint.

Verification: `make all` from the repository root green after application (747 pytest tests; all validators; ROUTE-001/002/003 at 100%).

## Adoption Update 2 (2026-07-11)

User approved proceeding on all remaining items with explicit reasoning per disputed possibility. Decisions and rationale:

- **E4 — annotate, not fold.** The 07-06 panel approved *adding a note to* `workflow-recipes.md` (candidate #3); folding the file into METHODOLOGY_MAP would contradict an approved candidate, lose the only greppable recipe index, and the keep-steelman (operator discoverability, Looper Topologies vocabulary) was never refuted. Candidate #3 is now fully adopted; only the ROUTE-003 verifier-artifact probe stays deferred (router lacks a verifier-artifact concept; adding the probe without router support would fail the gate it is meant to guard).
- **B1 applied.** Root `AGENTS.md` is now an explicit authority stub (read order: system/user → `06-repo/AGENTS.md` → invoked SKILL.md → non-authoritative PK); the claude-mem block is labeled historical context only. Risk accepted: claude-mem regeneration may rewrite the header; if that recurs, move the stub outside the managed region.
- **B2 applied.** Required Workflow in `06-repo/AGENTS.md` is strictness-scaled (L1 no ceremony; L2 relevant-docs-only; L3 full artifact set, final-report file only for cross-session work; L4+ full set + `review/final-report.md` + Human Review). Resolves the self-contradiction with Context Engineering and the GLOSSARY context-load deferral rule. Cross-link/eval-harness pins (thinking links, skill links, Harness Policy heading, `make all`) preserved.
- **B4 applied.** Library README non-goals now carry the regression-guard caveat, methodology≠operational split, and the declare-vs-enforce runtime-guarantee boundary.
- **D1 applied.** Literal-phrase pins upgraded to contracts: README/skill-map/QUALITY_GATES "nine frozen workflow skills" tests now also assert exactly nine `SKILL.md` files on disk and (where applicable) the gated-not-never gloss; the benchmark docstring phrase pin was dropped because `test_benchmark_covers_all_nine_workflows` already asserts set-equality coverage. Net: wording can be requalified honestly without losing count/coverage protection.
- **E1 applied (scoped).** Decision Index Rounds 69–101 (mechanical contract-standardization and registry-DRY rounds; no runtime consumers) collapsed into two rollup lines; the map-not-archive disclaimer moved under the heading. Rounds 4–68 entries kept — they encode distinct behavioral policy (L1 fast path, holdout expansions, R11/R12, rejections).
- **E3 applied (non-destructive).** Eleven retired/superseded records under `plans/` received a historical-record status header instead of merge/delete: zero link breakage, Durable Lesson evidence pointers stay valid, and stale wording (e.g. eight-skill era) is explicitly framed as historical. [INFERENCE] Merge-then-archive would save lines but breaks inbound links and rewrites history for no consumer benefit.
- **E2 + 00-core/03-context merges — deferred, recurrence-gated.** The panel transcript demotion and prompt-cluster merges remain contested (minimality lens vs keep-steelman: multiplicity-is-policy per METHODOLOGY_MAP, 2.2s test cost, transcript already labeled non-instruction). No operator-toil evidence exists; by the project's own gate, destructive restructuring needs recurrence evidence. Revisit trigger: a second independent complaint about archive weight, or a maintainer hitting real navigation failure attributable to these surfaces.
- **D4 — adopted 2026-07-12 (user-directed; recurrence `unknown`).** Originally deferred convention-only; all eight audited records passed with only two label fixes, so a validator would then have enforced a standard nothing violated. Revisit trigger was: a new record ships without evidence separation or fact-check dating. Now implemented forward-only: `plans/validate_record_hygiene.py` enforces status banner, evidence separation / `[INFERENCE]`, fact-check dating (warning), Candidate Adoption Ledger presence, and Falsifiability on records dated ≥ 2026-07-12; historical records stay out of scope so nothing breaks retroactively. Wired into `make validate`; negative tests in `plans/tests/test_validate_record_hygiene.py`.

Verification (this pass): `make all` from the repository root green after application — 748 pytest tests collected and passed, all validators, ROUTE-001/002/003 at 100%.

## Adoption Update 3 (2026-07-11)

User approved executing the two remaining actionable possibilities (P1, P7 from the possibility analysis):

- **P1 — ROUTE-003 verifier-artifact trap (closes candidate #3's last open item).** Followed holdout-before-tune strictly: candidate phrases were routed against the untuned router first (all four misrouted — three to `reflective-review`, one to `reflective-dispatch`, observed), then the fixture group `verifier_artifact_not_runner_trap` (4 phrases, expected `reflective-implement`), probe tuple, and cheatsheet cues were added, and only then the router gained a `verifier-artifact boundary` adjustment (deterministic-check signals + recurring context → implement +4). Post-tune: all four phrases route to `reflective-implement` at 0.80–0.90 confidence; ROUTE-003 at 100% with 19 groups / 66 phrases. Constants, QUALITY_GATES counts, ledger row 3, and the guard test updated; design followed the pre-decided option (adversarial trap expecting the primary workflow — no eval-schema change).
- **P7 — adoption-integrity mechanism templated for reuse.** `06-repo/PROJECT_KNOWLEDGE.template.md` now carries the Candidate Adoption Ledger contract (Decision Index guidance + acceptance criterion) and the four evidence-tier labels, exporting this repo's adoption-integrity pattern to any project using the template. Kept inside the existing template per the minimality gate — no tenth registry-managed file in `06-repo/`.

Verification (this pass): routed the four new phrases pre- and post-tune (observed); ROUTE-003 eval 100% (19 groups / 66 phrases); full `make all` from the repository root green.
