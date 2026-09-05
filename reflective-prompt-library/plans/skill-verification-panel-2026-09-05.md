# Skill Correctness and Logical-Consistency Pass — Panel Record (2026-09-05)

> **Status:** Complete. Thirteen installed skills reviewed by thirteen parallel lenses (one per skill) against a shared read-only packet; every text fix below landed at its named surface, `make all` is green (1129 tests with this record's guard, 1112 before it; validators 0 errors; ROUTE-001/002/003 100%; lint 1 pre-existing length warning), and `plans/tests/test_skill_verification_panel_record.py` guards the landed wording and both flow-pack size budgets. User instruction: "verify every single skill in this project, to examine their correctness and logical corrections."

## Research Question

For each of the nine core skills and four registered domain packs: is the text **correct** (no false claims, broken or wrong references, or instructions prompt text cannot execute) and **logically consistent** (no rule contradicts another rule in the same skill, in `reflective-dispatch`, in its examples file, in the cheatsheet, or in the Standing Non-Goals; every escalation target's Trigger accepts what is escalated; every Output field is produced by some step; every Never bullet is compatible with the Workflow)?

## Method

- One read-only lens per skill (`VBrief`, `VDispatch`, `VHandoff`, `VImplement`, `VMinimality`, `VResearch`, `VReview`, `VRisk`, `VSpecPlan`, `VGovScaffold`, `VGovDelivery`, `VFlowGen`, `VLoopHarness`) plus a routing-layer lens (`VRouting` over the dispatch table, cheatsheets, `skill-map.md`, `GLOSSARY.md`, `04-agent/workflow-recipes.md`). `VImplement` exhausted its first backend's quota and was re-fanned on a second backend.
- Fixed severity vocabulary: `defect` (false claim, internal contradiction, unexecutable instruction, escalation the target rejects, Never violated by the skill's own Workflow) · `inconsistency` (skill vs examples / cheatsheet / skill-map / dispatch row / GLOSSARY) · `ambiguity` (two readings, two actions) · `nit`. Style, length, tone, new-feature ideas, and re-litigation of guard-pinned adoptions were out of scope; a pinned sentence could still be flagged for a contradiction it creates.
- Pre-verified deterministically before fan-out (so lenses did not re-report them): every backtick repo path resolves; frontmatter is uniform; no pack appears on a dispatch route row; five cross-skill near-duplicate bullets are intentional family mirrors; `make all` green at packet time.
- The coordinator applied fixes skill by skill, re-running the affected guards and the bash/Python template dry-runs (stub agent, toggling verifier) after each batch. Lens reports were consumed in-session and are not retained; the durable trace is the landed diff, this record, and the guard.

## Landed Fixes by Skill

IDs are the in-session finding IDs. "Surface" is the file edited; every fix is in `skills/<name>/SKILL.md` unless noted.

| Skill | Landed fixes |
| --- | --- |
| `reflective-brief` | B-1: Workflow step 11 split into "Write the Minimal Plan" and step 12 "Choose the Next Action", so both Output fields have a producing step. |
| `reflective-dispatch` | D-1: the L1 Fast Path route trace lists the same fields as the full trace (`Route Confidence`, `Enhancements Enabled`, `Enhancements Available`), and default-up is scoped to *eligibility* ambiguity — content ambiguity after routing is handled by stating assumptions, not a second default-up. D-2: the resume rule names the owning skills for the continuation packet and State Ledger, requires creating one at Strictness L5 before yielding, and defines the neither-exists path (say so under `Enhancements Available`; re-evaluate strictness and risk rather than reuse a prior lower-rigor route). |
| `reflective-handoff-retro` | H1: summarize only after the Continuation Packet fidelity check. H2: the packet also lists relevant files and the commands/tests run so a continuation can rebuild the task packet (kept as a sentence *after* the GD-anchored one, which stays verbatim). H6: `prompt lens` added to the Promotion Destination enum. H7: "already granted" approval wording aligned with `04-agent/artifact-promotion.md`. H8: `audit trail` added to the runtime-guarantee list. H10: Project-Knowledge Promotion Candidates appended only when a PK layer exists or the user asks to establish one. |
| `reflective-implement` | No text change landed in this pass. |
| `reflective-minimality` | M3: origin-before-cut — origin found → keep the rule; not found → record the negative result before the ceremony test. M4: correctness or test adequacy requested → combine with `reflective-review`; complexity-only stays here; "Lean already. No complexity cuts." replaces "Ship." |
| `reflective-research` | RR-1: example output labelled as research headings + ledger status literals, not Evidence Tiers. RR-2: `verified`→`stale` is a freshness transition, not a lowered bar. RR-3: "input set" means the population counted. RR-4: State Ledger gains `Checked (date)` and `How (command + input set, or freshness kind)`. RR-5: volatile-fact example carries check date and tracking point. RR-6: Workflow classification labels match Output labels. RR-7: cheatsheet do-not-use aligned with the Trigger. RR-8: no official source → `unverified`/`unknown`, DeepWiki is not sole authority. RR-9: research recommends changes; it does not edit the repository. |
| `reflective-review` | RV-1: "record-only correction" defined for the revision-binding rule. RV-3: a load-bearing `unverifiable` claim blocks `Approve` and goes to Required Fixes. |
| `reflective-risk` | F1: unbounded risk → recommend no-go (Human Review is not a substitute). F2: `Sink Inventory` and `Unattended Envelope` added to the Output list and fenced template, which other sections already required. F3: "ungated production changes" replaces "direct production changes". |
| `reflective-spec-plan` | SP-1: `workflow-spec.md` contents conditional on formalization level and risk. SP-2: Formalization levels use GLOSSARY's L0–L4 labels (was 1–5). SP-3: TEST-001 `Type` gains `hidden-evaluation` and `anti-cheating`. SP-4: default artifact emission stated per mode. |
| `governed-delivery` | GD-V1: a mid-task spec change also re-plans the affected slice before work continues (matches `reflective-spec-plan` / `reflective-implement`). |
| `agent-governance-scaffold` | AGS-1: PII cross-reference `§3`→`§4a`. AGS-2: `tests/governance/**` and `tests/security-invariants/**` added to worker-immutable `deny_write`. AGS-3: constitutional check conditional on the objects being in scope. AGS-4: wrapper-agent contract listed in Output. AGS-5: `authorization_epoch`→`activation_epoch`. AGS-8: HANDOVER carries exactly one of the two `**Governance status:**` literals (both spelled out, so the R12/R14 guard's literal stays). AGS-9: three-no clause defined. |
| `flow-control-generator` | D1: fan-out quorum counts succeeded branches — a failed or empty branch removes its output. D2: merged-result gate (`checks/verify-merged.sh`) in the orchestrator and DAG templates, not only the branch tally. D3: DAG nodes consume upstream outputs. D4: explicit `# gate: none (accepted)` where a stage has no gate. D5: fenced-JSON plan parsing; plan must be a list. D6: worker id sanitized before use as a path. D7: DAG quorum path now reaches the merged gate (`MIN_OK` previously exited before it; found while restoring the file, see Evidence). A1/I1/I4: NODES comment, "run note", "Acquisition L3". Size 20543→19935 chars by trimming unpinned prose. |
| `flow-loop-harness` | FLH-1: `MAX_ITER=20` justified in the backlog template. FLH-2: Loop Anatomy 4 matches the code (any no-change iteration aborts); a silent non-git verifier yields a random signal, so detection is disabled and the cap exits. FLH-3: `git diff HEAD --stat` counts staged changes. FLH-4: ACCEPT must be the whole critique, not one line. FLH-5: backlog anatomy deviations declared. FLH-6: multi-wave preflight exits early when converged; missing prompts exit 4. FLH-7: description names the writer-critic advisory-tier exception. FLH-8: multi-wave stall signal hashes branch outputs only (the summary header named the wave and hid stalls). FLH-9: `TASKS.md` format stated. FLH-10: unattended writer-critic must splice the deterministic floor. FLH-11: "Acquisition L3". Size 20431→19927 chars; the pre-existing hard guard (`test_loop_pack_stays_under_lint_length_threshold`) was failing before the trim. |
| Routing layer | No change landed (dispatch table, cheatsheets, `skill-map.md`, `GLOSSARY.md`, `04-agent/workflow-recipes.md`). |

## Not Changed

- `agent-governance-scaffold` is 26,291 chars against the 20,000 soft lint warning; the warning pre-dates this pass (26,074 at HEAD) and cutting ~6k of governance text is a scope decision, not a correctness fix. Left as the single lint warning.
- The `04-agent/runtime-trust-boundary.md` authority table and Standing Non-Goals were read as constraints, not edited.
- No new skill, no new dispatch row, no pack registry change.

## Evidence vs Inference

- Evidence: the landed diff (`git diff HEAD -- skills/`), `make all` output (1112 passed; validators 0 errors; ROUTE evals 100%), the template dry-runs — every bash block passes `bash -n`, both Python blocks compile, the fan-out template rejects a conflicting synthesis (guard), and the DAG template exits 2 on strict failure, on quorum met with the sink missing, and on quorum met with a conflicting merge, exits 0 on clean strict and clean quorum runs.
- Evidence (process incident): while trimming, an editor tool truncated `flow-control-generator/SKILL.md` at line 300 and wrote its pagination footer into the file. The tail was restored from the pre-edit full read and diffed against HEAD line by line; the D7 gap was noticed during that restoration. `make all` and the dry-runs were re-run after restoration. Lesson: re-run the whole gate after any tool-assisted edit of a >300-line file, and diff against the index, not memory.
- Evidence (guard collisions found by `make all`, fixed): an earlier trim removed the word "methodology" that `test_p8_methodology_boundary_in_purpose` pins in both pack Purposes (the assertion sat on a line elided from the coordinator's read); H2 had extended a GD-anchored sentence instead of following it; AGS-8 had dropped the R12/R14 literal. All three were repaired without changing the guards.
- [INFERENCE] The lens verdict distribution (SOUND / SOUND WITH FIXES / DEFECTIVE) is not recorded because the reports were not retained; the landed-fix table is the only durable proxy. Treat "no text change landed" for `reflective-implement` and the routing layer as exactly that, not as a certified clean bill.

## Evidence Actually Checked

Read fully: all thirteen `skills/*/SKILL.md`; `plans/tests/test_flow_pack_adoption_state.py`, `test_governed_delivery_adoption_state.py`, `test_agent_governance_scaffold_adoption_state.py`, `test_llm_judge_lifecycle_survey_record.py`, `test_installed_skills_general_lessons_record.py`, `test_dormant_item_watch.py` (pinned-sentence inventory before trimming); `plans/lint_skills.py` (`check_body_length` measures the whole file in characters); `plans/validate_record_hygiene.py`. Executed: `make all` (three times: red on 4 collisions, then green), `/tmp` dry-run script over all 8 bash and 2 Python template blocks. Not opened: lens transcripts after synthesis.

## Falsifiability

- If any sentence in the Landed Fixes table is absent from its surface, or either flow pack exceeds 20,000 characters, `plans/tests/test_skill_verification_panel_record.py` fails.
- If the DAG template exits 0 when `MIN_OK` is met but `checks/verify-merged.sh` rejects the sink output, D7 has regressed (guarded by dry-run).
- If a later panel finds a `defect`-tier contradiction in `reflective-implement` or the routing layer, the "no text change landed" rows here were incomplete, not clean; supersede this record rather than editing it.

## Completion Ledger

| Item | Status | Where |
| --- | --- | --- |
| Thirteen-lens verification run; fixes applied per skill | done | `skills/*/SKILL.md` diff; this record |
| Flow packs back under the 20,000-char budget; hard guard added for the generator (harness already had one) | done | `plans/tests/test_skill_verification_panel_record.py` |
| Record indexed | done | `PROJECT_KNOWLEDGE.md` Decision Index; `plans/external-adoption-case-studies-2026-06-20.md` State Ledger |
| `agent-governance-scaffold` size | not done (out of scope) | lint warning, pre-existing |
