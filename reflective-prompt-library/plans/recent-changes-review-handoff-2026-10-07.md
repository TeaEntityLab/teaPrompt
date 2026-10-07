# Recent-Changes Parallel Review Handoff — 2026-10-07

> **Status (2026-10-07, repair turn):** Non-authoritative review/handoff record, English. **Supplied findings closed at the tested consumers.** Ten runtime findings RV-01–RV-04, RV-06–RV-09, RV-13–RV-14 are repaired; RV-05's five-to-ten oracle migration is implemented with explicit Human Review approval. RV-10–RV-12 were already corrected. Fresh repair evidence is below; historical failures remain preserved. Registry remains 9 core + 10 packs; no owned runtime, new skill, commit, or push is introduced by this repair.

## Handoff contract (dated 2026-10-07)

The dated observations, source references, fixture conditions, proposed repairs, and approval boundaries below are the continuation payload. Temporary files and raw transcripts are not required to understand the findings. No previously observed failure was rerun to author this record. Fresh recording-turn verification is separate from the preserved survey/review receipts.

Source line ranges and observed failures in the original findings refer to the
pre-repair snapshot. Their requested repairs remain as rationale, not open work.
The current implementations, acceptance evidence, and limits are recorded in
§Repair-turn closure below.

## Scope

- **Review target:** five initial survey/navigation files and eight commits from `c454738` through `2989110`, inclusive; Git comparison baseline `40d7b70..2989110`. The eight commits are `c454738`, `8f610df`, `dfa1789`, `72e18f7`, `1124535`, `6da06ef`, `b947fb4`, `2989110`.
- **Method:** six specialist slices (read-only; no fixes or commits during review), interrupted for a diagram-design survey, then delivered as Request Changes with archived synthetic offline evidence.
- **Evidence provenance (plain, not dependencies):** prior-review findings JSON and receipts under a temporary parallel-review scratch directory — `reproduction-results.json`, `supplemental-results.json`, `round-cap-result.json`, and probe scripts `reproduce.py`, `supplemental.py`, `round_cap.py`. All concrete observations needed to continue are transcribed below; the temporary paths are not required to resume.

## Disposition summary

- **Repaired runtime defects:** RV-01–RV-04, RV-06–RV-09, RV-13–RV-14.
- **Approved and implemented spec/oracle migration:** RV-05; user selected **Approve ten-pack migration**. `locked: true`, nine core skills, the other checks, and `0444` file mode are retained.
- **Applied documentation corrections:** RV-10–RV-12; no runtime fix implied.
- **Advisory dispositions:** AD-01 valid maintenance correction; AD-02/AD-03 rejected as defects; AD-04 process advice.
- **Original recording scope:** survey qualifications, navigation, rendered table placement, generated discovery metadata, and a commit of the related changes. The subsequent user request **Fix** authorized the repair turn documented below.

### Original recording goal, state, and acceptance

The original user request was durable recording followed by a commit. Its acceptance was: recover evidence and rationale; distinguish observations, inference, unknowns, and proposed repairs; preserve every open finding; render the comparison rows; refresh discovery metadata; run documentation gates; commit the related changes. Runtime repair and oracle migration were outside that recording turn, then authorized separately by **Fix** and the explicit RV-05 approval.

Canonical artifacts for continuation: [Diagram Design survey](diagram-design-survey-2026-10-07.md), [leaked-prompt survey](system-prompts-leaks-survey-2026-10-07.md), [Matt delta survey](mattpocock-skills-v131-delta-survey-2026-10-07.md), [case-study index](external-adoption-case-studies-2026-06-20.md), [maintenance log](flow-pack-usage-log.md), and the current skill files named per finding. Earlier runtime-spec/ticket evidence already lives in [RSD-2](runtime-skills-workflow-spec-2026-10-06.md) and [TASK-001](runtime-skills-task001-ticket-2026-10-06.md); the present review does not reopen their accepted dry-run scope.

## Runtime findings (original evidence; now repaired)

### RV-01 [P1] Fan-out / wave digit-guard bypass (`00`, `08`) — FIXED

- **Source:** `reflective-prompt-library/skills/flow-control-generator/SKILL.md:141,172`; `reflective-prompt-library/skills/flow-loop-harness/SKILL.md:333-334,380`.
- **Observed input:** `MAX_JOBS=00` and `MAX_JOBS=08` against the published Parallel Fan-out/Fan-in template (5 branch prompts) and the Multi-Wave template (`MAX_WAVES=1`, plus `MAX_WAVES=00` case). Controls `MAX_JOBS=4` (5/5 outputs, exit 0) and `MAX_JOBS=0` (exit 4, zero outputs) behave as configured.
- **Observed output:**
  - Fan `00`: exit **0** after **1 of 5** branch outputs (`fan-1.md`); stderr `fan.sh: line 41: i % MAX_JOBS: division by 0 (error token is "S")`. Expected configuration exit 4 with zero outputs.
  - Fan `08`: exit **0** after **1 of 5** outputs; stderr `fan.sh: line 41: 08: value too great for base (error token is "08")`. Expected exit 4.
  - Wave `00` / `08` (`MAX_JOBS`): exit **2** after **1 of 5** wave outputs (`w1-1.md`) with the same division/base stderr. Expected exit 4 before dispatch.
  - Wave `MAX_WAVES=00`: exit **2**, expected exit 4.
  - Digit guards reject only literal `0`, accepting `00` and `08`; arithmetic errors abort dispatch without entering branch-failure accounting (fan) or with a generic exit 2 rather than configuration exit 4 (waves).
- **Requested repair/verification:** Validate canonical positive-decimal caps before any work (or safely normalize decimal values); classify invalid caps before dispatch with configuration exit 4 and zero branch outputs. Re-verify with `00`, `08`, `0`, empty, non-numeric, and negative inputs on both fan and wave templates.

### RV-02 [P1] Unvalidated arithmetic iteration/round caps permit command expansion — FIXED

- **Source:** `reflective-prompt-library/skills/flow-loop-harness/SKILL.md:83,131,167,192,248,290`.
- **Observed input (two stages):**
  - Stage A (uninitialized scalar): `MAX_ITER=x[$(printf marker > arithmetic-expanded)]` and `MAX_ROUNDS=x[$(printf marker > arithmetic-expanded)]` against the Verify-Gated Fix Loop and Evaluator-Optimizer/Writer-Critic templates. Result: exit 1, stderr `run.sh: line 55: x: unbound variable` (MAX_ITER) / `run.sh: line 31: x: unbound variable` (MAX_ROUNDS), `command_expansion: false`, no marker. This stage did **NOT** prove command expansion — it proved only an unbound-scalar abort, not the requested exit-4 rejection and not zero-expansion by design.
  - Stage B (initialized scalar — the proving probe): `r=1` preset, `MAX_ROUNDS=r[$(printf marker > arithmetic-expanded)]`, stub `AGENT_CMD=/bin/echo ACCEPT`. Result: exit **0**, `timed_out: false`, `shell_expanded: true`, marker file contains `marker`, empty stdout/stderr. The shell expanded the command substitution inside Bash arithmetic and the run accepted.
- **Requested repair/verification:** Validate numeric iteration/round caps before first dispatch and before any arithmetic evaluation; reject expressions with configuration exit 4 and provably zero command expansion. Re-verify with both uninitialized and initialized-scalar expression payloads plus `00`/`08`/empty/non-numeric cases. [INFERENCE] Any arithmetic-evaluation site fed by an environment cap needs the same guard; the probes exercised the two loop templates named above.

### RV-03 [P1] ARM blinded-eval scorer recovers both arm identities from public order — FIXED

- **Source:** `reflective-prompt-library/skills/arm-blinded-eval-harness/SKILL.md:150-155,169-185,220`.
- **Observed input:** Published harness with declared public execution order `['control','treatment']`; opaque random candidate names (e.g. `P1-d8809fc3b797.py`, `P1-ad19d430c838.py`); predictor oracle that reads only an invocation-ordinal counter and the declared public order, never the sealed map: `inferred_arm = ['C','T'][ordinal]`.
- **Observed output:** Exit 0; both predictions match: `P1-d8809fc3b797.py → C (match true)`, `P1-ad19d430c838.py → T (match true)`. Extraction preserves declared public arm order and scoring walks insertion order, so ordinal plus public schedule deblinds without reading the sealed map. Opaque filenames do not blind scorer invocation order.
- **Requested repair/verification:** Separate execution-order provenance from a randomized, scorer-opaque scoring schedule; keep schedule metadata inaccessible to the scorer. Verify that scoring order has no deterministic mapping to the public arm schedule and preserve a content-reading positive control. An ordinal-only predictor can guess correctly by chance in one two-arm pair; one failed or successful guess is not a statistical blinding proof.

### RV-04 [P1] Router-trace linter R4 bypasses and case gap — FIXED

- **Source:** `reflective-prompt-library/skills/router-trace-linter/SKILL.md:135-156,184-188,217-218`.
- **Observed inputs/outputs** (base trace: dispatch/L2 production goal unless noted; expected exit 1 = deny, 0 = pass):
  - `Goal: No auth changes, deploy to production, and rotate credentials` + `Human Review: not required` → exit **0** (expected 1). Negation is not scoped to the actual action.
  - `Goal: deploy to production` + `Human Review: false` → exit **0** (expected 1).
  - `Human Review: not applicable` → exit **0** (expected 1).
  - `Human Review: tbd` → exit **0** (expected 1).
  - `Human Review: **none**` (markdown-bold) → exit **0** (expected 1).
  - `Human Review: "none"` (quoted) → exit **0** (expected 1).
  - `Workflow: Reflective-Risk` (capitalized) on a low-risk rename → exit **0** (expected 1; workflow-gated rule missed).
  - Controls that already behave: low-risk rename + `not required` → 0; production + `none` → 1; production + `skipped` → 1.
- **Requested repair/verification:** Scope negation to the actual action; normalize supported field representations (false / not-applicable variants / placeholders / markdown / quoting) and workflow case; fail closed for missing/placeholder review on production actions. Re-verify the full contrastive matrix above with no regression on the passing controls.

The complete ordinary low-risk control trace was:

```text
Mode: dispatch
Strictness: L2
Goal: rename a local variable
Assumptions: Only the actions in Goal are planned.
Workflow: reflective-implement
Route Confidence: medium
Enhancements Enabled: none
Enhancements Available: none
Human Review: not required
Next Action: execute the named change
```

The RV-04/RV-09 matrix substitutes only the named Goal, Workflow, Human Review, or Confidence fields; the other fields stay as shown. This avoids mistaking missing-field failures for the observed normalization/negation defects.

### RV-05 [P1] Locked acceptance oracle still expects 5 packs; registry holds 10 — APPROVED AND MIGRATED

- **Source:** `acceptance.yaml:14-17`; `features/registry.md:13-34`; `reflective-prompt-library/plans/validate_skill_examples.py` (`DOMAIN_PACK_SKILLS` count check).
- **Observed input/output:** Canonical acceptance command returns **10** domain packs while the locked expectation declares **5**; probe records `declared_expect: 5, actual: 10, exit 0` on the count query. The surface and oracle disagree.
- **Requested repair/verification:** Human-reviewed spec/oracle migration with the approved ten-pack acceptance scope. Do **not** silently edit a locked expectation to get green. Requires explicit human approval; no permission widening. Parent supplies post-migration evidence.

### RV-06 [P2] ARM scorer-input boundary not enforced (extra outsider data arg) — FIXED

- **Source:** `reflective-prompt-library/skills/arm-blinded-eval-harness/SKILL.md:172-183,228`.
- **Observed input:** Oracle argv `['oracle.py', '{CAND}', '<scratch>/outside-input.txt']` where the extra file is outside `blinded/` and outside both arm directories; the oracle reads `sys.argv[2]` when present.
- **Observed output:** Exit **0** with both arms scored (exits 0/1 by content), expected configuration exit 4. The claimed blinded-only candidate-data boundary is not enforced.
- **Requested repair/verification:** Define trusted scorer code versus data arguments explicitly; enforce allowed candidate-data paths; exclude arm/config/metadata inputs from scorer access. Re-verify with outsider-arg (must exit 4), arm-dir-arg, config-arg, and clean positive control.

### RV-07 [P2] Documented ARM CONFIG is not runnable (`KeyError: blinded`) — FIXED

- **Source:** `reflective-prompt-library/skills/arm-blinded-eval-harness/SKILL.md:122-124,148,186-201,209-221`.
- **Observed input:** Verbatim documented JSON CONFIG run through the published harness.
- **Observed output:** Exit **1**; `KeyError: 'blinded'` at `blinded = Path(cfg["blinded"])`. The shown CONFIG lacks mandatory `blinded`, `arm_dirs`, `sealed_map`, `results`, `run_note` fields.
- **Requested repair/verification:** Provide a complete runnable configuration matching the scaffold's required inputs (or mark the excerpt explicitly partial with the full runnable form adjacent). Re-verify by executing the documented CONFIG verbatim.

### RV-08 [P2] `TASKS.canon` directory misreported as empty backlog — FIXED

- **Source:** `reflective-prompt-library/skills/flow-loop-harness/SKILL.md:266-267,290-292`.
- **Observed input:** `state/TASKS.canon` is a directory; `TASKS.md` contains `an unfinished task`.
- **Observed output:** Exit **0**, stdout `backlog empty`; stderr `grep: ./state/TASKS.canon: Is a directory` swallowed by `|| true`. Initialization can copy `TASKS.md` into the directory path; the read error is erased and treated as an empty queue.
- **Requested repair/verification:** Require a readable regular canonical queue file; propagate read errors instead of treating them as empty; never copy a file onto a directory path silently. Re-verify with directory-canon, missing-canon, unreadable-canon, and normal-file cases.

### RV-09 [P2] Router linter rejects legitimate quoted confidence `"medium"` — FIXED

- **Source:** `reflective-prompt-library/skills/router-trace-linter/SKILL.md:119-121,211-214`.
- **Observed input:** Low-risk rename trace with `Route Confidence: "medium"` (YAML-style quoted scalar).
- **Observed output:** Exit **1**, `Route Confidence: unparseable (presence/parse)`; expected 0. Field values are not normalized for supported quoted representations.
- **Requested repair/verification:** Normalize supported quoted representations consistently, or explicitly narrow and demonstrate the supported contract. Re-verify quoted/unquoted confidence values with no regression on genuinely unparseable inputs.

### RV-13 [P2] Verify-gated fix loop zero-cap misclassification (`MAX_ITER=00`) — FIXED

- **Source:** `reflective-prompt-library/skills/flow-loop-harness/SKILL.md` Verify-Gated Fix Loop template.
- **Observed input:** `MAX_ITER=00`, failing `checks/verify.sh` (exit 1).
- **Observed output:** Exit **2**; expected configuration exit 4. Zero-equivalent caps are not classified as invalid configuration before dispatch.
- **Requested repair/verification:** Same canonical-cap validation as RV-01/RV-02 applied to the fix-loop entry; exit 4 before any iteration. Re-verify alongside RV-01.

### RV-14 [P2] Raw critic worker exit 4 collides with configuration exit 4 — FIXED

- **Source:** `reflective-prompt-library/skills/flow-loop-harness/SKILL.md` Evaluator-Optimizer / Writer-Critic template.
- **Observed input:** `AGENT_CMD` stub that exits 4 immediately.
- **Observed output:** Template exits **4** — indistinguishable from configuration/verification failure. Expected: agent failure classified distinctly from config/verifier failure.
- **Requested repair/verification:** Reserve exit 4 for configuration/verification; map raw worker exits into a distinct worker-failure class (or remap before propagation). Re-verify with worker exits 1/4/127 and genuine config errors.

## Documentation-only corrections (parent-applied, same commit)

### RV-10 [P2] Leaked-prompt survey overclaims — parent DOC-FIX (qualify samples, preserve qualifiers)

- **Source:** `reflective-prompt-library/plans/system-prompts-leaks-survey-2026-10-07.md:30-54`.
- **Problem preserved:** Sample artifact text was promoted into universal vendor runtime-enforcement and secrecy-extraction claims; Grok's explicit `unless-the-user-asks` qualifier was dropped; TeaPrompt scaffolds were said to enforce controls despite the repository's host-enforcement boundary. No vendor-runtime or efficacy experiment was performed.
- **Applied correction (parent, not a runtime fix):** Scope claims to the sampled files, retain source qualifiers (including Grok's), distinguish described expectations from exercised runtime guarantees, keep generalization as inference.

### RV-11 [P2] Matt delta-survey commit counts — parent DOC-FIX

- **Source:** `reflective-prompt-library/plans/mattpocock-skills-v131-delta-survey-2026-10-07.md:3,9,15`; `reflective-prompt-library/PROJECT_KNOWLEDGE.md:139`; `reflective-prompt-library/plans/external-adoption-case-studies-2026-06-20.md:59`.
- **Problem preserved:** Recorded 32-commit main delta is **34** reachable commits for `d81f3a18..6fd94792` under `git rev-list --count`; `v1.3.1` tag `24fe0ef7..6fd94792` contains **28** commits. The survey did not explain a different counting population; tag identity versus main-range identity was conflated.
- **Applied correction (parent):** Correct or explicitly define the counted population; preserve tag/main identity separation in all repeated records.

### RV-12 [P2] Case-comparison table blank-line rendering — parent DOC-FIX

- **Source:** `reflective-prompt-library/plans/external-adoption-case-studies-2026-06-20.md:58-60`.
- **Problem preserved:** Blank line 58 terminates the comparison table; the two appended 2026-10-07 survey rows render as prose rather than table cells. Probe (markdown-it-py, commonmark + table): expected 2 date cells, actual **0**; `appended_rows_render_as_cells: false`.
- **Applied correction (parent):** Place new rows inside the table and verify rendered Markdown.

## Advisory dispositions (no repository defect)

- **AD-01 — Valid stale-comment maintenance correction, now resolved:** `validate_skill_examples.py` named five packs in a comment while its enforcing guard already expected 10. The comment now points to the executable pin; behavior and registry membership are unchanged. This was a real maintenance defect, not a rejected finding or pack invocation.
- **AD-02 — Retracted ten-pack warning rejected:** A retracted warning about ten packs was evaluated and rejected; registry holds at the approved 10. Not a defect.
- **AD-03 — 1,237 corpus count correct for its population:** 1,237 is reproducible over file-like entries inside the original non-hidden directory buckets. 1,245 counts tracked root-inclusive entries — a different population, not a defect. Do not change a correct count to match a different set.
- **AD-04 — Delivery/kernel/search/parallel-depth notes are workflow advice:** Evaluated as process guidance, not repository defects. No code change.

## Declined to judge

The review explicitly declined to judge: (a) real provider sandbox containment or model-worker security; (b) comparative skill efficacy; (c) actual vendor enforcement from mirrored prompt text alone. No conclusion in this record implies any of these.

## Historical verification preserved (not current evidence)

- Prior advisory-fix checks: standalone skill-example validator reported **9 core + 10 packs**; focused validator regression and index-freshness tests reported **7 passed**. This was not a seven-fence syntax sweep.
- Prior link validation: **0 errors**; record hygiene: **0 errors**, **35 existing warnings**.
- Historical full-suite pass: **1453 passed**. Those fixtures did not cover the newly observed boundary failures. No preserved result is closure evidence for RV-01–RV-09/RV-13–RV-14.

## Original ordered repair plan (completed)

The original ordering below is preserved as rationale. All six steps are completed under the subsequent repair authorization; consumer evidence is in §Repair-turn closure. This review record itself did not authorize implementation.

1. RV-01/RV-02/RV-13: validate cap inputs before dispatch/arithmetic; classify invalid values with exit 4, zero outputs, and zero command expansion. Exercise canonical, zero-equivalent, octal-looking, empty, negative, non-numeric, and initialized-scalar expression inputs.
2. RV-04/RV-09: normalize documented representations and workflow case, scope negation to the action, and deny high-risk traces without actual review. Exercise the full contrastive matrix and ordinary low-risk control.
3. RV-03/RV-06/RV-07: separate scoring order from arm provenance, define/enforce scorer code-versus-data access, and publish complete runnable CONFIG. Exercise order leakage, outsider/config access, and the documented configuration.
4. RV-08/RV-14: preserve canonical-queue read errors and distinguish worker failure from configuration failure. Exercise directory/unreadable/missing queues and worker exits 1/4/127.
5. RV-05: obtain explicit Human Review of the five-to-ten spec/oracle migration, its affected feature counts, and canonical acceptance command. An approved pack registry is not permission to silently change a locked oracle.
6. After authorized repairs, verify each named consumer path; do not substitute historical suite-green or syntax-only checks for those observations.

## Authority / trust boundaries and blockers

Generated-script consumers now validate caps, scorer data arguments, trace fields, and queue paths. Those checks enforce only their named local boundaries; this prose grants no authority. The host still controls scorer isolation, sealed metadata, permissions, and effect execution.

No blocker remains for the requested repairs. The subsequent user request **Fix** authorized runtime changes, and explicit RV-05 approval authorized only the five-to-ten oracle migration. Neither grants new permissions, product-runtime adoption, provider usage, commit, or push authority. A provider `BLOCKED` result still must not be retried with wider permission flags.

## Retro / process lessons

- Interruption cost: six-slice parallel review was interrupted for the diagram survey and resumed as Request Changes — the handoff record (this file) is what preserves continuity, not memory of the session.
- Guard-shape lesson: rejecting only literal `0` while accepting `00`/`08`, and entering arithmetic before validation, are the same defect class — validate-then-use, never use-then-handle.
- Exit-code discipline: the current template contract reserves exit 4 for configuration/verification failure. A raw worker exit colliding with that class (RV-14), partial-dispatch aborts (RV-01), and queue errors swallowed into success (RV-08) require consumer-level checks, not a prose claim of enforcement.
- Blinding lesson: randomizing names without randomizing order is not blinding; provenance visible to the scorer is scorer input.
- Normalization lesson: a linter that accepts `tbd`/`false`/`**none**` as review while rejecting `"medium"` as confidence has its normalization inverted — normalize both sides of every enumerated field or narrow the contract explicitly.
- Historical-green lesson: 1453 passing tests plus 0 link errors coexist with every defect above; suite-green is not boundary coverage.

## Evidence vs Inference

- **Observed (archived receipts + source text):** all exit codes, outputs, stderr strings, counts, and file excerpts transcribed under RV-01–RV-14, AD-01–AD-04, and historical verification above.
- **[INFERENCE] Original requested repairs** proposed the smallest guard/normalization/boundary shapes consistent with the archived observations. The implemented choices and current checks are recorded below; neither historical suite-green nor a proposed shape is repair evidence.
- Population definitions are observed accounting, not interchangeable estimates: prior-to-main 34 reachable commits versus tag-to-main 28; directory-bucket 1,237 file-like entries versus root-inclusive 1,245 tracked paths. No alternative population was supplied for the earlier 32-commit statement.

## Falsifiability

Repair closure is falsified by a current consumer that dispatches or expands invalid cap inputs; derives its sealed scoring schedule from public execution order; accepts a contrastive high-risk trace without review; disagrees with the approved oracle counts; dispatches undeclared outsider scorer data; cannot run the documented CONFIG; reports a canonical-queue read error as success; or classifies raw worker exit 4 as configuration exit 4. RV-10–RV-12 remain documentation corrections. One random predictor miss or a full-suite pass alone cannot establish the boundary claims.

## Recording-turn verification (2026-10-07)

- The actual Markdown consumer smoke used `markdown-it-py` with CommonMark plus table support. All three new case-comparison rows rendered as six-cell table rows; the earlier two-row prose defect is corrected.
- The rendered Diagram Design record contains all 15 preserved helper rows; the rendered review contains all 14 RV finding headings. These are preservation/rendering checks, not new executions of the archived probes.
- Real Chromium loaded that generated documentation surface and observed the three visible six-column survey rows, 15 helper rows, and 14 review findings. A screenshot was captured and the owned tab was closed. This verifies the available local renderer, not a hosted documentation website.
- The recording-turn index regeneration and `make all` preceded these repairs. Its historical results are preserved above, not reused as runtime closure evidence. Repair-turn verification is separate below.

## Repair-turn closure (2026-10-07)

### Decision and minimality

- User direction **Fix** authorized all ten remaining runtime repairs. The user
  separately selected **Approve ten-pack migration** for RV-05. The owner-write
  window on `acceptance.yaml` was limited to that approved migration; its file
  mode was restored to `0444`.
- Reused four existing domain packs and their companion examples. No new skill,
  routing row, runner, dependency, permission mode, or provider call was added.
- Canonical positive decimal caps were chosen over implicit normalization:
  `1`–`2147483647`, no leading zero or expression, and explicitly empty values
  do not fall back to defaults. `MIN_OK` retains its documented empty/`0`
  strict-policy sentinel.

### Acceptance and spec-to-code traceability

| Findings | Current implementation / consumer | Observed closure |
|---|---|---|
| RV-01/RV-02/RV-13 | `flow-control-generator/SKILL.md` fan-out/DAG caps; `flow-loop-harness/SKILL.md` fix/critic/backlog/wave caps | Invalid values hold with exit 4 before dispatch or arithmetic expansion; ordinary and upper-bound valid caps retain behavior |
| RV-03 | `arm-blinded-eval-harness/SKILL.md` private scoring schedule and sealed map | Same host-held replay seed with swapped public orders yields the same sealed arm schedule; default seed is privately derived; public run note does not expose seed/schedule |
| RV-04/RV-09 | `router-trace-linter/SKILL.md` action-scoped hazard negation, workflow case normalization, review/confidence scalar normalization | Contrastive high-risk routes deny absent/placeholder/negative review; ordinary low-risk, affirmed review, and quoted confidence controls pass |
| RV-05 | `acceptance.yaml`, `features/registry.md`, `VERIFY.md`; `test_registry_acceptance_consumers.py` | Locked expectations and observed counts agree at 9 core / 10 packs; feature-map drive observes 19 contracts; `locked: true` and `0444` remain |
| RV-06/RV-07 | `arm-blinded-eval-harness/SKILL.md` trusted scorer-code manifest, blinded-only data validation, complete documented CONFIG | Outsider/arm/config/metadata/undeclared-code arguments refuse with exit 4 before dispatch; verbatim CONFIG runs and its content-reading scorers recover the planted pattern |
| RV-08 | `flow-loop-harness/SKILL.md` backlog regular-file/readability checks and explicit `grep` status handling | Directory/missing/unreadable queues hold with exit 4 and zero dispatch; valid queues retire, preserve completion ledgers, and return success even on the final iteration |
| RV-14 | `flow-loop-harness/SKILL.md` worker failure handling | Raw worker exit 4 maps to worker class 5 rather than configuration class 4; critic exits 1/127 retain those values and raw codes remain logged |

The skill names above resolve under `reflective-prompt-library/skills/`.
Original finding source ranges are historical; this table names current symbols
and consumers without pretending that old line offsets remain current.

### Fresh executed verification

- Emitted Bash recipes: **89/89 scenarios matched** — 60 invalid/beyond-ceiling
  cap cases rejected before dispatch/expansion, 23 valid cap paths, three queue
  errors, and critic worker outcomes **1 / 5 / 127** for raw **1 / 4 / 127**.
  The five-branch fan-out and wave controls produced all five branch outputs.
- Emitted router checker CLI: **16/16 scenarios matched**, including
  mixed-negation production actions, workflow case, negative/quoted review
  values, quoted confidence, and affirmative/low-risk controls.
- Emitted blinded harness plus **verbatim documented CONFIG**:
  **16/16 scenarios matched**, including 12 negative input-boundary cases.
  Planted pass/fail content was recovered via the sealed map; the public-order
  independence check passed. Hold/discarded candidates remain outside the
  repair-pair denominator.
- Approved oracle consumer smoke: **PASS**, core **9**, packs **10**,
  feature-map drive **19**, every command exit **0**, `locked: true`,
  file mode **0444**.
- Focused regression command:
  `python3 -m pytest reflective-prompt-library/plans/tests/test_flow_generator_consumers.py reflective-prompt-library/plans/tests/test_flow_loop_consumers.py reflective-prompt-library/plans/tests/test_arm_blinded_eval_consumers.py reflective-prompt-library/plans/tests/test_router_trace_linter_scaffold.py reflective-prompt-library/plans/tests/test_registry_acceptance_consumers.py -q --tb=short`
  — **163 passed**.
- Integration failures were repaired, not hidden: the backlog's empty-queue
  `grep` status previously triggered `set -e`, its verifier precheck and done
  ledger entry had been dropped, and eight cap guards used nine digits for a
  ten-digit ceiling. New ceiling regressions first produced **9 failures /
  3 passing refusal controls**, then passed in the 163-test run. The router
  regression now asserts an actual R4 failure instead of assuming R4 must be
  the only rule that can fail.
- The first full-suite run collected **1,533 tests** and reported
  **1,531 passed / 2 failed**: a stale documented pytest-size floor and an
  older backlog test's incidental crash diagnostic. The floor was refreshed
  from the observed collection. The backlog test retains its original exit
  expectations and now checks actual canonical task retention/retirement,
  cap remainder, red-start preservation, and the outside-git tradeoff instead
  of pinning crash/cap/preflight wording. No test was deleted or skipped.
  Focused checks of these two owning surfaces then reported **14 passed**.
- Integrated repository command:
  `python3 reflective-prompt-library/plans/generate_index.py && make all`
  — **1,533 passed**, zero validator errors, all **19** skill contracts valid,
  examples present for **9 core + 10 packs**, and **100% consistency** in
  ROUTE-001/002/003. These fixture scores are not general routing proof.
- All **13 emitted Bash/Python fences** passed syntax checks. The actual
  Markdown consumer retained **14 finding headings** and rendered all
  **seven three-column closure rows**, joining all eleven repaired RV IDs.
  Real Chromium observed those rows, captured the table, and the owned tab was
  closed. The 1600px local rendering had no horizontal page overflow; this is
  evidence for the available local renderer, not a deployed documentation site.
  Final DOM revalidation also observed the refreshed gate notes and the same
  table without horizontal overflow. Both final screenshot retries timed out;
  the earlier unchanged-table capture remains the visual receipt. The final
  owned tab was closed, and the capture failure was reported to tool QA.

### Consumer map and residual risks

- Direct emitted-script callers, the Python DAG cap entry point, companion
  examples, documented CONFIG, developer regressions, the acceptance oracle,
  and feature-map commands are covered by the executions above.
- Pre-admission proposal and earlier survey/spec receipts remain historical,
  intentionally unchanged. Registry/install membership and the frozen
  nine-core routing surface are unchanged.
- Generated discovery metadata is regenerated after the last source/doc edit.
- **Untested boundaries:** real provider/model utility, scorer filesystem or
  process isolation, hidden-answer read sealing, comparative skill efficacy,
  statistical arm-blinding, host permission enforcement, and external effects.
  Synthetic workers and deterministic content scorers do not establish them.
- **Visible warnings:** eight long-skill warnings across six packs, including
  the repaired blinded-eval and router-linter bodies, plus 35 historical
  record-hygiene warnings. No warning threshold or oracle was weakened.
- No open supplied finding or Human Review decision remains. No commit or push
  was performed during this repair turn.

### Delayed-advisory recheck (2026-10-07)

- Rechecked the aggregated feedback against current canonical files rather
  than its old offsets. Backlog retirement appends the completion ledger;
  verifier executability is checked before `run_verify`; both queue `grep`
  calls capture nonzero status; Loop Anatomy documents worker class 5.
  The old failing integration-state advisories are superseded, not new fixes.
- The scorer boundary, privately derived default seed, sealed-only schedule,
  complete CONFIG, content-reading `add` fixtures, and router R4/confidence
  consumers are present. The installed router skill is a symlink to the
  canonical repository skill, not a separately repaired copy.
- RV-05 approval, oracle mode, current registry-map metadata, inherited
  before-fix provenance, and the final green gate evidence were already
  recorded. Operational advice about pending agents/smokes predates closure.
- The tab-destruction explanation for the host eval variable is not
  established: its assignment was outside the page callback. The actual
  returned DOM receipt was retained; no tab reopening was needed to recover it.
- **Valid doc drift repaired:** `VERIFY.md` and `features/validators.md`
  still described the initial single lint warning; `features/test-suite.md`
  presented an older drive as current. Refreshed the two affected map
  source/date fields, qualified the committed base versus tested working
  tree, and retained older test snapshots as explicitly dated history.
  Warning observations are not an acceptance waiver; R10 does not cover
  other warnings automatically. No code, test, lint threshold, oracle,
  permission, install, commit, or push change was made.
- Fresh published-map consumer: all eight standalone validator commands
  exited 0; the test-suite Drive reported **1,533 passed**; the registry Drive
  observed **19** contracts. Oracle `locked: true` and mode `0444` remain.
- The first map Drive caught generated-document drift: **1,532 passed /
  1 failed** because this new handoff text had not yet been regenerated into
  `index.json`. Regenerated the discovery index before rerunning; the
  freshness guard then passed. No assertion or acceptance rule was changed.

### Decision rationale and Git delivery (2026-10-07)

This is a non-authoritative retrospective and delivery record, not a new agent
rule, skill admission, or runtime guarantee.

- **Consumer evidence over plausible scaffolds:** the numeric-cap, queue,
  worker-exit, router-review, and scorer-boundary failures justified repairing
  existing contracts and executable consumers together. A green documentation
  gate or syntax check alone could not establish those boundary behaviors.
- **Narrow repair over redesign:** preserve the nine-core/ten-pack registry and
  existing generators. Normalize supported router representations, but reject
  noncanonical execution caps before arithmetic or dispatch. Keep the approved
  oracle migration separate from ordinary developer-regression changes.
- **Blinding claim stays bounded:** a private scoring schedule independent of
  public execution order removes the observed ordinal leak; argv/path checks
  do not establish scorer filesystem isolation or statistical arm-blinding.
- **Already-correct files stay untouched:** the final four delayed advisories
  described intermediate states. Reapplying repairs would add risk without
  resolving a current defect. The final recheck refreshed discovery metadata
  and ran the freshness consumer; it did not alter contracts or source docs.

| Final delayed advisory | Disposition and evidence |
|---|---|
| The closing handoff edit left `index.json` stale | Already resolved before the advisory recheck; the index was newer than that edit. Content correctness was confirmed by regeneration followed by `test_index_json_current.py`: **1 passed**, not inferred from timestamps alone. |
| Preserve the first map Drive's failure and passing rerun | Already recorded above and in the final report: **1,532 passed / 1 failed** at `test_committed_index_matches_generator_over_current_tree`, then **1,533 passed** after regeneration. This is evidence that the consumer caught drift, not noise to erase. |
| Classify the stale-index failure and verify the repair | Generated-document drift, not a runtime regression. The freshness assertion and acceptance checks were retained; the last advisory recheck reran only the focused freshness test, not the full suite. |
| An empty failed semantic search is not absence evidence | The search failed with provider HTTP 403 on all seven requests. Literal search found `source_commit`, `last_verified_at`, `verification_status`, and the event-driven maintenance rule in `features/README.md`; no absence claim was made. |

- **Verification order for this delivery:** finish the repository records,
  regenerate `index.json`, exercise the rendered record, run `make all`, then
  commit and push. Any later indexed-document edit requires regeneration and
  a new freshness check; a local session receipt is not an indexed repo edit.
- **Visual evidence limit:** the later five-document Chromium DOM smoke passed,
  but its viewport screenshot repeated content in tiles and was reported to
  tool QA. That capture is not clean-layout proof. Earlier screenshot timeout
  receipts and the untested host/provider/statistical boundaries remain.
- **Separate delivery authorization:** the user requested “record your thoughts
  and commit push.” The configured target is `main` → `origin/main`; fetching
  observed zero remote-only commits and four prior local commits. Normal push
  is authorized; no force push, history rewrite, permission change, or additional
  product scope is introduced. Earlier “no commit or push” statements describe
  the completed repair turns, not this separately authorized delivery.

