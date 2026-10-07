# Recent-Changes Parallel Review Handoff — 2026-10-07

> **Status (2026-10-07):** Non-authoritative review/handoff record, English. Verdict: **Request Changes**. Ten runtime findings RV-01–RV-04, RV-06–RV-09, RV-13–RV-14 and locked-oracle migration RV-05 remain **UNIMPLEMENTED**. Documentation-only corrections RV-10–RV-12 and comment maintenance are applied in this recording change. Skill contracts and locked oracles are unchanged; registry remains 9 core + 10 packs.

## Handoff contract (dated 2026-10-07)

The dated observations, source references, fixture conditions, proposed repairs, and approval boundaries below are the continuation payload. Temporary files and raw transcripts are not required to understand the findings. No previously observed failure was rerun to author this record. Fresh recording-turn verification is separate from the preserved survey/review receipts.

## Scope

- **Review target:** five initial survey/navigation files and eight commits from `c454738` through `2989110`, inclusive; Git comparison baseline `40d7b70..2989110`. The eight commits are `c454738`, `8f610df`, `dfa1789`, `72e18f7`, `1124535`, `6da06ef`, `b947fb4`, `2989110`.
- **Method:** six specialist slices (read-only; no fixes or commits during review), interrupted for a diagram-design survey, then delivered as Request Changes with archived synthetic offline evidence.
- **Evidence provenance (plain, not dependencies):** prior-review findings JSON and receipts under a temporary parallel-review scratch directory — `reproduction-results.json`, `supplemental-results.json`, `round-cap-result.json`, and probe scripts `reproduce.py`, `supplemental.py`, `round_cap.py`. All concrete observations needed to continue are transcribed below; the temporary paths are not required to resume.

## Disposition summary

- **Open runtime defects:** RV-01–RV-04, RV-06–RV-09, RV-13–RV-14.
- **Open spec/oracle migration:** RV-05; explicit Human Review is required before changing the locked expectation.
- **Applied documentation corrections:** RV-10–RV-12; no runtime fix implied.
- **Advisory dispositions:** AD-01 valid maintenance correction; AD-02/AD-03 rejected as defects; AD-04 process advice.
- **Recording scope:** survey qualifications, navigation, rendered table placement, generated discovery metadata, and a commit of the related changes.

### Goal, state, and acceptance

The user requested durable recording of the session's conclusions followed by a commit. Recording acceptance is: recover evidence and rationale; distinguish source observations, inference, unknowns, and proposed repairs; preserve every open finding; render the case-comparison rows correctly; refresh discovery metadata; run the affected documentation gates; commit only the related changes. Runtime repair and oracle migration are not acceptance criteria for this recording turn.

Canonical artifacts for continuation: [Diagram Design survey](diagram-design-survey-2026-10-07.md), [leaked-prompt survey](system-prompts-leaks-survey-2026-10-07.md), [Matt delta survey](mattpocock-skills-v131-delta-survey-2026-10-07.md), [case-study index](external-adoption-case-studies-2026-06-20.md), [maintenance log](flow-pack-usage-log.md), and the current skill files named per finding. Earlier runtime-spec/ticket evidence already lives in [RSD-2](runtime-skills-workflow-spec-2026-10-06.md) and [TASK-001](runtime-skills-task001-ticket-2026-10-06.md); the present review does not reopen their accepted dry-run scope.

## Open runtime findings (UNIMPLEMENTED)

### RV-01 [P1] Fan-out / wave digit-guard bypass (`00`, `08`) — UNIMPLEMENTED

- **Source:** `reflective-prompt-library/skills/flow-control-generator/SKILL.md:141,172`; `reflective-prompt-library/skills/flow-loop-harness/SKILL.md:333-334,380`.
- **Observed input:** `MAX_JOBS=00` and `MAX_JOBS=08` against the published Parallel Fan-out/Fan-in template (5 branch prompts) and the Multi-Wave template (`MAX_WAVES=1`, plus `MAX_WAVES=00` case). Controls `MAX_JOBS=4` (5/5 outputs, exit 0) and `MAX_JOBS=0` (exit 4, zero outputs) behave as configured.
- **Observed output:**
  - Fan `00`: exit **0** after **1 of 5** branch outputs (`fan-1.md`); stderr `fan.sh: line 41: i % MAX_JOBS: division by 0 (error token is "S")`. Expected configuration exit 4 with zero outputs.
  - Fan `08`: exit **0** after **1 of 5** outputs; stderr `fan.sh: line 41: 08: value too great for base (error token is "08")`. Expected exit 4.
  - Wave `00` / `08` (`MAX_JOBS`): exit **2** after **1 of 5** wave outputs (`w1-1.md`) with the same division/base stderr. Expected exit 4 before dispatch.
  - Wave `MAX_WAVES=00`: exit **2**, expected exit 4.
  - Digit guards reject only literal `0`, accepting `00` and `08`; arithmetic errors abort dispatch without entering branch-failure accounting (fan) or with a generic exit 2 rather than configuration exit 4 (waves).
- **Requested repair/verification:** Validate canonical positive-decimal caps before any work (or safely normalize decimal values); classify invalid caps before dispatch with configuration exit 4 and zero branch outputs. Re-verify with `00`, `08`, `0`, empty, non-numeric, and negative inputs on both fan and wave templates.

### RV-02 [P1] Unvalidated arithmetic iteration/round caps permit command expansion — UNIMPLEMENTED

- **Source:** `reflective-prompt-library/skills/flow-loop-harness/SKILL.md:83,131,167,192,248,290`.
- **Observed input (two stages):**
  - Stage A (uninitialized scalar): `MAX_ITER=x[$(printf marker > arithmetic-expanded)]` and `MAX_ROUNDS=x[$(printf marker > arithmetic-expanded)]` against the Verify-Gated Fix Loop and Evaluator-Optimizer/Writer-Critic templates. Result: exit 1, stderr `run.sh: line 55: x: unbound variable` (MAX_ITER) / `run.sh: line 31: x: unbound variable` (MAX_ROUNDS), `command_expansion: false`, no marker. This stage did **NOT** prove command expansion — it proved only an unbound-scalar abort, not the requested exit-4 rejection and not zero-expansion by design.
  - Stage B (initialized scalar — the proving probe): `r=1` preset, `MAX_ROUNDS=r[$(printf marker > arithmetic-expanded)]`, stub `AGENT_CMD=/bin/echo ACCEPT`. Result: exit **0**, `timed_out: false`, `shell_expanded: true`, marker file contains `marker`, empty stdout/stderr. The shell expanded the command substitution inside Bash arithmetic and the run accepted.
- **Requested repair/verification:** Validate numeric iteration/round caps before first dispatch and before any arithmetic evaluation; reject expressions with configuration exit 4 and provably zero command expansion. Re-verify with both uninitialized and initialized-scalar expression payloads plus `00`/`08`/empty/non-numeric cases. [INFERENCE] Any arithmetic-evaluation site fed by an environment cap needs the same guard; the probes exercised the two loop templates named above.

### RV-03 [P1] ARM blinded-eval scorer recovers both arm identities from public order — UNIMPLEMENTED

- **Source:** `reflective-prompt-library/skills/arm-blinded-eval-harness/SKILL.md:150-155,169-185,220`.
- **Observed input:** Published harness with declared public execution order `['control','treatment']`; opaque random candidate names (e.g. `P1-d8809fc3b797.py`, `P1-ad19d430c838.py`); predictor oracle that reads only an invocation-ordinal counter and the declared public order, never the sealed map: `inferred_arm = ['C','T'][ordinal]`.
- **Observed output:** Exit 0; both predictions match: `P1-d8809fc3b797.py → C (match true)`, `P1-ad19d430c838.py → T (match true)`. Extraction preserves declared public arm order and scoring walks insertion order, so ordinal plus public schedule deblinds without reading the sealed map. Opaque filenames do not blind scorer invocation order.
- **Requested repair/verification:** Separate execution-order provenance from a randomized, scorer-opaque scoring schedule; keep schedule metadata inaccessible to the scorer. Verify that scoring order has no deterministic mapping to the public arm schedule and preserve a content-reading positive control. An ordinal-only predictor can guess correctly by chance in one two-arm pair; one failed or successful guess is not a statistical blinding proof.

### RV-04 [P1] Router-trace linter R4 bypasses and case gap — UNIMPLEMENTED

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

### RV-05 [P1] Locked acceptance oracle still expects 5 packs; registry holds 10 — UNIMPLEMENTED, requires human-reviewed migration

- **Source:** `acceptance.yaml:14-17`; `features/registry.md:13-34`; `reflective-prompt-library/plans/validate_skill_examples.py` (`DOMAIN_PACK_SKILLS` count check).
- **Observed input/output:** Canonical acceptance command returns **10** domain packs while the locked expectation declares **5**; probe records `declared_expect: 5, actual: 10, exit 0` on the count query. The surface and oracle disagree.
- **Requested repair/verification:** Human-reviewed spec/oracle migration with the approved ten-pack acceptance scope. Do **not** silently edit a locked expectation to get green. Requires explicit human approval; no permission widening. Parent supplies post-migration evidence.

### RV-06 [P2] ARM scorer-input boundary not enforced (extra outsider data arg) — UNIMPLEMENTED

- **Source:** `reflective-prompt-library/skills/arm-blinded-eval-harness/SKILL.md:172-183,228`.
- **Observed input:** Oracle argv `['oracle.py', '{CAND}', '<scratch>/outside-input.txt']` where the extra file is outside `blinded/` and outside both arm directories; the oracle reads `sys.argv[2]` when present.
- **Observed output:** Exit **0** with both arms scored (exits 0/1 by content), expected configuration exit 4. The claimed blinded-only candidate-data boundary is not enforced.
- **Requested repair/verification:** Define trusted scorer code versus data arguments explicitly; enforce allowed candidate-data paths; exclude arm/config/metadata inputs from scorer access. Re-verify with outsider-arg (must exit 4), arm-dir-arg, config-arg, and clean positive control.

### RV-07 [P2] Documented ARM CONFIG is not runnable (`KeyError: blinded`) — UNIMPLEMENTED

- **Source:** `reflective-prompt-library/skills/arm-blinded-eval-harness/SKILL.md:122-124,148,186-201,209-221`.
- **Observed input:** Verbatim documented JSON CONFIG run through the published harness.
- **Observed output:** Exit **1**; `KeyError: 'blinded'` at `blinded = Path(cfg["blinded"])`. The shown CONFIG lacks mandatory `blinded`, `arm_dirs`, `sealed_map`, `results`, `run_note` fields.
- **Requested repair/verification:** Provide a complete runnable configuration matching the scaffold's required inputs (or mark the excerpt explicitly partial with the full runnable form adjacent). Re-verify by executing the documented CONFIG verbatim.

### RV-08 [P2] `TASKS.canon` directory misreported as empty backlog — UNIMPLEMENTED

- **Source:** `reflective-prompt-library/skills/flow-loop-harness/SKILL.md:266-267,290-292`.
- **Observed input:** `state/TASKS.canon` is a directory; `TASKS.md` contains `an unfinished task`.
- **Observed output:** Exit **0**, stdout `backlog empty`; stderr `grep: ./state/TASKS.canon: Is a directory` swallowed by `|| true`. Initialization can copy `TASKS.md` into the directory path; the read error is erased and treated as an empty queue.
- **Requested repair/verification:** Require a readable regular canonical queue file; propagate read errors instead of treating them as empty; never copy a file onto a directory path silently. Re-verify with directory-canon, missing-canon, unreadable-canon, and normal-file cases.

### RV-09 [P2] Router linter rejects legitimate quoted confidence `"medium"` — UNIMPLEMENTED

- **Source:** `reflective-prompt-library/skills/router-trace-linter/SKILL.md:119-121,211-214`.
- **Observed input:** Low-risk rename trace with `Route Confidence: "medium"` (YAML-style quoted scalar).
- **Observed output:** Exit **1**, `Route Confidence: unparseable (presence/parse)`; expected 0. Field values are not normalized for supported quoted representations.
- **Requested repair/verification:** Normalize supported quoted representations consistently, or explicitly narrow and demonstrate the supported contract. Re-verify quoted/unquoted confidence values with no regression on genuinely unparseable inputs.

### RV-13 [P2] Verify-gated fix loop zero-cap misclassification (`MAX_ITER=00`) — UNIMPLEMENTED

- **Source:** `reflective-prompt-library/skills/flow-loop-harness/SKILL.md` Verify-Gated Fix Loop template.
- **Observed input:** `MAX_ITER=00`, failing `checks/verify.sh` (exit 1).
- **Observed output:** Exit **2**; expected configuration exit 4. Zero-equivalent caps are not classified as invalid configuration before dispatch.
- **Requested repair/verification:** Same canonical-cap validation as RV-01/RV-02 applied to the fix-loop entry; exit 4 before any iteration. Re-verify alongside RV-01.

### RV-14 [P2] Raw critic worker exit 4 collides with configuration exit 4 — UNIMPLEMENTED

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

## Remaining work / ordered actions

The ordering below is a proposed repair plan, not implementation authorization from this record:

1. RV-01/RV-02/RV-13: validate cap inputs before dispatch/arithmetic; classify invalid values with exit 4, zero outputs, and zero command expansion. Exercise canonical, zero-equivalent, octal-looking, empty, negative, non-numeric, and initialized-scalar expression inputs.
2. RV-04/RV-09: normalize documented representations and workflow case, scope negation to the action, and deny high-risk traces without actual review. Exercise the full contrastive matrix and ordinary low-risk control.
3. RV-03/RV-06/RV-07: separate scoring order from arm provenance, define/enforce scorer code-versus-data access, and publish complete runnable CONFIG. Exercise order leakage, outsider/config access, and the documented configuration.
4. RV-08/RV-14: preserve canonical-queue read errors and distinguish worker failure from configuration failure. Exercise directory/unreadable/missing queues and worker exits 1/4/127.
5. RV-05: obtain explicit Human Review of the five-to-ten spec/oracle migration, its affected feature counts, and canonical acceptance command. An approved pack registry is not permission to silently change a locked oracle.
6. After authorized repairs, verify each named consumer path; do not substitute historical suite-green or syntax-only checks for those observations.

## Authority / trust boundaries and blockers

Caps, scorer data arguments, trace fields, and queue paths are inputs at generated-script consumers; validating them is a proposed repair, not an enforcement guarantee from this prose. The host controls scorer isolation, sealed metadata, permissions, and effect execution.

No information blocker remains for recording. Runtime changes need their own authorized repair scope; RV-05 also needs explicit oracle-migration approval. This commit does not grant either. Do not widen permissions, claim the Request Changes verdict is cleared, or retry a provider `BLOCKED` result with wider permission flags.

## Retro / process lessons

- Interruption cost: six-slice parallel review was interrupted for the diagram survey and resumed as Request Changes — the handoff record (this file) is what preserves continuity, not memory of the session.
- Guard-shape lesson: rejecting only literal `0` while accepting `00`/`08`, and entering arithmetic before validation, are the same defect class — validate-then-use, never use-then-handle.
- Exit-code discipline: the current template contract reserves exit 4 for configuration/verification failure. A raw worker exit colliding with that class (RV-14), partial-dispatch aborts (RV-01), and queue errors swallowed into success (RV-08) require consumer-level checks, not a prose claim of enforcement.
- Blinding lesson: randomizing names without randomizing order is not blinding; provenance visible to the scorer is scorer input.
- Normalization lesson: a linter that accepts `tbd`/`false`/`**none**` as review while rejecting `"medium"` as confidence has its normalization inverted — normalize both sides of every enumerated field or narrow the contract explicitly.
- Historical-green lesson: 1453 passing tests plus 0 link errors coexist with every defect above; suite-green is not boundary coverage.

## Evidence vs Inference

- **Observed (archived receipts + source text):** all exit codes, outputs, stderr strings, counts, and file excerpts transcribed under RV-01–RV-14, AD-01–AD-04, and historical verification above.
- **[INFERENCE] Requested repairs** propose the smallest guard/normalization/boundary shapes consistent with the observations; alternative shapes (e.g., safe decimal normalization instead of strict rejection) are acceptable if they produce the same verified exit/output behavior.
- Population definitions are observed accounting, not interchangeable estimates: prior-to-main 34 reachable commits versus tag-to-main 28; directory-bucket 1,237 file-like entries versus root-inclusive 1,245 tracked paths. No alternative population was supplied for the earlier 32-commit statement.

## Falsifiability

Open findings are retired only with evidence at the affected current consumer: invalid caps rejected before work/expansion; no deterministic scoring-order/arm mapping; contrastive R4 failures and quoted-confidence acceptance; an approved oracle migration; rejected outsider scorer data; runnable documented CONFIG; canonical-queue read errors preserved; and worker/config failure classes separated. RV-10–RV-12 are documentation corrections, not open runtime allegations. A newer source state can supersede the dated findings, but one random predictor miss or a full-suite pass alone cannot falsify them.

## Recording-turn verification (2026-10-07)

- The actual Markdown consumer smoke used `markdown-it-py` with CommonMark plus table support. All three new case-comparison rows rendered as six-cell table rows; the earlier two-row prose defect is corrected.
- The rendered Diagram Design record contains all 15 preserved helper rows; the rendered review contains all 14 RV finding headings. These are preservation/rendering checks, not new executions of the archived probes.
- Real Chromium loaded that generated documentation surface and observed the three visible six-column survey rows, 15 helper rows, and 14 review findings. A screenshot was captured and the owned tab was closed. This verifies the available local renderer, not a hosted documentation website.
- Final gate commands are index regeneration followed by `make all`; actual final-state results belong to the committing message and delivery receipt. No historical green result is substituted for that run, and no result clears the still-open runtime/oracle findings.
