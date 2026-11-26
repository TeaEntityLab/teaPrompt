# Skills × Survey Corpus Rethink (2026-11-26)

Language: English
> **Status:** evaluation record (`SCR-DOC1`), decided 2026-11-26. The rethink prompt authorized evaluation only ([PROJECT_KNOWLEDGE.md](../PROJECT_KNOWLEDGE.md) authority rule); the owner then ratified SUR-ED1/ED2 and directed the repairs and proposals listed under Owner Decisions. P5 remains open.

Owner prompt, 2026-11-26: "重新思考全部的 skills，對照已知的 surveys".

## Research Question and Direct Answer

Do the 19 repository skills (9 frozen core, 10 registered packs) still match what the survey corpus has established, and what should change?

**The contracts hold. The drift is in follow-through, in records, and in one process failure.** The review found no cross-skill contradiction, no superseded clause in a core skill, no example drift in any pack, no lapsed checkpoint, and no obsolete deferral. Across the catalogue, exactly one mechanism has three or more independent external sources while TeaPrompt holds it deferred: measured prompt-text ablation or retirement. No local gap is recorded for it. The defects sit in secondary surfaces and records that a change did not reach, and in this session's own outward actions.

## Method

1. Measured all 19 skills: size, lines, description length, guard-test coverage. Only `governed-delivery` is near the 20,000-character lint warning.
2. Extracted 271 non-final rows from 92 ledger-bearing records and split them by date into three slices.
3. Ran six read-only reviewers: three queue slices; core skills with their examples, skill map and both cheatsheets; domain packs with their records and triggers; theme convergence across the catalogue and the Decision Index.
4. Main adjudicated and re-read every D-class claim at the cited lines on 2026-11-26.

Reviewer agreement is one epistemic channel from one model family, not independent verification.

## Process Finding: Authorization

Installed `reflective-risk` (§Rules, authorization gate) requires "the user's own words in this conversation" before a push. Session commits since `40cf49f`:

| Commit | Owner request | Push named in that request? |
| --- | --- | --- |
| `b33bb19` | "Update docs or skills and commit push" | yes |
| `737f782` | "Survey 各大平台的官方說明及 cookbook" | no |
| `54c6795` | "survey" + Uber article URL | no |
| `649f332` | "Survey 原本的來源及內容，並思考 update docs or skills" | no |
| `617f02c` | "記錄想法 並commit push" | yes |
| `e9694c4` | "Survey" + OpenSpec URL | no |
| `b297cbf` | "思考 這三套已知與 superpower 的差異…" | no |
| `855118e` | "反思目前的 skills 有需要更新嗎?…" | no |

Six of eight pushes lacked the owner's words for that push. Earlier in the same conversation the gate held: after a bare "commit", `87ec80a` was committed and not pushed. The drift began right after an explicit "commit push", which fits authorization carrying over from a different request. `855118e` also revised two core skills under an inquiry prompt. The scope principle already exists in `reflective-handoff-retro` ("an answer for a different scope does not authorize the blocked step") but not in the risk gate; see SCR-P1.

## Defects (D): verified; applied under Owner Decisions

**Group A: follow-through of `855118e`. Applies only if the owner ratifies SUR-ED1/ED2.**

| ID | Surface | Evidence | Narrowest repair |
| --- | --- | --- | --- |
| SCR-D1 | `skills/examples/reflective-handoff-retro.examples.md` | The copied handoff template (lines 19–36) lacks the `## Friction Notes` row that `skills/reflective-handoff-retro/SKILL.md:74` now carries | Add the row to the example template |
| SCR-D2 | CKB-DOC2 and UAS-DOC2(b) ledgers and catalogue rows | `official-cookbooks-survey-2026-11-24.md:55`, `uber-skills-platform-survey-2026-11-24.md:56`, catalogue rows dated 2026-11-24 still say Deferred after SUR-ED1/ED2 landed | Dated follow-through notes; dated rows stay as history |
| SCR-D3 | Catalogue and Decision Index | `skills-update-review-2026-11-25.md` has no catalogue row and no Decision Index entry | One row and one entry |

**Group B: record corrections.**

| ID | Surface | Evidence | Narrowest repair |
| --- | --- | --- | --- |
| SCR-D4 | Four November records | CFT-DOC2 is cited as part of the deferred queue (`official-cookbooks-survey-2026-11-24.md:55`, `uber-skills-platform-survey-2026-11-24.md:56`, `openspec-survey-2026-11-25.md:54`, `skills-update-review-2026-11-25.md:6,61`), but its ledger says "Adopted: navigation only" (`craft-anything-survey-2026-11-10.md:85`) | Drop CFT from the four citations |
| SCR-D5 | `uber-skills-platform-survey-2026-11-24.md:45` | "no existing surface measures prompt-text effectiveness by ablation" contradicts `golden-benchmark-runner`, whose contract is a bare-versus-skill paired comparison. The true claim is that no ablation run has been executed | "no executed ablation run has measured TeaPrompt skill text; the runner contract exists" |
| SCR-D6 | `openspec-survey-2026-11-25.md:54` | OSP-DOC2 keeps one Deferred status after SUR split it into SUR-RV1 (deferred) and SUR-SD1 (rejected/dormant) | Dated note pointing to the split |
| SCR-D7 | `3xa-harness-survey-2026-08-20.md:156` | "Deferred / study-only — no artifact change", yet `skills/acceptance-join-validator/SKILL.md:40,96` ships the digest-bound report as "the 3XA-1 repair" | Dated note; the named-reviewer binding stays deferred. Pins: `test_3xa_harness_survey_record.py:85,91` |
| SCR-D8 | `governance-workflow-self-control-adoption-2026-09-14.md:21-22` | GW-9 and GW-10 still read "Held — date-gated" although `checkpoint-2026-10-11-outcome.md:108,110` decided both | Outcome pointers in the Next-action cells |
| SCR-D9 | `grok-bot-automation-survey-2026-11-20.md:57` | GKB-DOC2 holds the same restate-before-executing example as GB-BR1 (`agent-efficiency-autonomy-learning-survey-2026-11-01.md:334`) without a cross-reference; both sources share one author | Cross-reference GB-BR1 |
| SCR-D10 | `QUALITY_GATES_SUMMARY.md:363,368` | Key Metrics still say 9 core + 5 packs; the registry lists 10 packs (19 skills) | Mark dated-historical or correct the counts |
| SCR-D11 | Decision Index, `PROJECT_KNOWLEDGE.md` | Newest entry is 2026-10-30; 57 catalogue rows are dated November; `validate_project_knowledge.py` warns about four later governance commits | One November rollup entry |

**Group C: skill-surface consistency.**

| ID | Surface | Evidence | Narrowest repair |
| --- | --- | --- | --- |
| SCR-D12 | `SKILL_TRIGGER_CHEATSHEET.md` and `.zh-TW.md`, L1 fast path | Both omit the contract's third condition, "No high-risk, trust-boundary, or side-effect authority signals appear", and its default-up rule (`skills/reflective-dispatch/SKILL.md` §L1 Fast Path). A trivial outward action could be fast-pathed from the cheatsheet | Add the condition to both bullets; check parity tests |
| SCR-D13 | `skills/examples/reflective-brief.examples.md:19,49` | Bare `## Scope`; the template gives `- In:` and `- Out:` (`skills/reflective-brief/SKILL.md:80-82`) | Add the two sub-bullets |
| SCR-D14 | `skills/skill-map.md:37` | Anchor `#L19-L48`; the module contract runs to line 54 | `#L20-L54` |
| SCR-D15 | Six packs | `verification-map-generator` and the five 2026-10-06 admissions carry no demotion triggers (0 matches in each SKILL.md), although `06-repo/AGENTS.md` item 3 requires them to add a pack | Needs a design choice; see SCR-P4 |

## Proposals (P): decided under Owner Decisions

| ID | Proposal | Evidence | Falsifier | Guard |
| --- | --- | --- | --- | --- |
| SCR-P1 | `reflective-risk` authorization gate: the owner's words must cover this action on this work; authorization given for other work or in earlier turns does not carry over | Six unrequested pushes in this session; the same scope rule already exists in `reflective-handoff-retro` | If unrequested pushes recur after landing, prose is not enough and the gap needs a host gate | `test_fable_method_survey_record.py:92-97`; existing substrings preserved |
| SCR-P2 | `04-agent/artifact-promotion.md:82`: the retirement trigger names recheck events (host or model generation change, measured regression or bypass, superseding wording landed elsewhere, cost review), not only a condition | The corpus's only three-source convergence (Uber ablation, Cherny "delete and see", agent-skills regrade); no local gap recorded | Maintainers already answer with events, or a measured regression fires no recheck | Unpinned |
| SCR-P3 | Rule whether WGS-X4b's trigger ("eval harness can A/B wording", `skill-improvement-plan-2026-07-24.md:274`) has fired now that `golden-benchmark-runner` and `arm-blinded-eval-harness` exist | Capability exists; whether declared-artifact arms count as wording A/B is an owner judgment | A ruling only reopens the decision; any run still needs separate model-campaign authorization | `test_dormant_work_specs_doc.py:233` symmetry |
| SCR-P4 | Demotion triggers for six packs: add per-pack triggers, or scope `06-repo/AGENTS.md` item 3 to future admissions | SCR-D15 | A pack survives an unrecorded review without a trigger | Older packs pin the convention; the six are unguarded |
| SCR-P5 | `governed-delivery` headroom: about 19.8k of 20k characters; PKG-7 reopens at 20,000. Decide before the next repair whether to move content to `ARTIFACTS.md` or accept the warning | `lint_skills.py` threshold; `checkpoint-packaging-decision-2026-10-11.md` PKG-7 | The next repair stays under 20k | Lint warning only |
| SCR-P6 | `skills/reflective-research/SKILL.md:46`: move the positive duty ("name the input or host-condition difference") out of the prohibition bullet into the State Ledger rules | PROJECT_KNOWLEDGE lesson "A duty seated inside a prohibition list is dropped by the reader" (21 fixture runs, AF82-9/AF82-14) | A fixture probe shows the duty performed in place | `test_agentflow_survey_record.py` `SS_ADOPTED` pins the bullet verbatim |

Not recommended now: three deduplication trims (`reflective-dispatch` Enhancement rationale stated at three places; `reflective-implement` binary check rule beside the four-class rule; `reflective-brief` step 4 beside its operating rule). No reader failure is recorded for them, and the September review held similar items for a self-containment policy decision.

## No-change Rulings (N)

- Deferred queue: about 59 of 271 extracted rows were already final. About 200 remain correctly dormant. Seven were resolved under their own gate at the 2026-10-11 checkpoint. PS-C1 and PS2-3 fired and were handled when they fired. None is obsolete; the OpenAI Evals shutdown touches no open row.
- No cross-skill contradiction. Shared adopted text (`OUTCOME_UNKNOWN`, transcript is not the source of record, `stale` propagation, `Declined to Judge`) agrees on every surface.
- All ten pack examples match their contracts; every pack-cited path resolves; all registries list 9 core and 10 packs.
- Every dated checkpoint has a recorded verdict. The residuals of `router-trace-linter` and `arm-blinded-eval-harness` are disclosed on their live contracts.
- November eval items (trajectory grading, clean-room runs, real-prompt corpora, the 70–90% pass heuristic) are host concerns: external only, local demand `unknown`.
- About 15 DOC2 worked-reference items stay deferred. Periodic adjudication, as on 2026-11-25, remains the substitute for an eval runtime; no new skill.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Decision trigger |
| --- | --- | --- | --- |
| SCR-DOC1 | This evaluation record | Recorded; decided 2026-11-26 | Refresh at the next pack evidence review (2027-01-11) or when a probe or run contradicts an item below |
| SCR-D1–D3 | Follow-through of `855118e` | Applied 2026-11-26 after owner ratification of SUR-ED1/ED2 | — |
| SCR-D4–D14 | Record and surface corrections | Applied 2026-11-26 (owner direction) | — |
| SCR-D15, SCR-P4 | Demotion triggers for six packs | Adopted 2026-11-26; guard `test_registered_pack_has_demotion_triggers` | A pack survives the 2027-01-11 review without a recorded verdict |
| SCR-P1 | `reflective-risk` authorization scope clause | Adopted 2026-11-26 | An unrequested outward action recurs after landing → host gate, not more prose |
| SCR-P2 | Retirement recheck events in `04-agent/artifact-promotion.md` | Adopted 2026-11-26 | A measured regression fires no recheck |
| SCR-P3 | WGS-X4b evidence gate | Ruled fired 2026-11-26; deferred on model-campaign authorization | Owner authorizes or declines a no-op hunt run |
| SCR-P5 | `governed-delivery` headroom | Open; not selected | Decide before the next `governed-delivery` repair |
| SCR-P6 | Move the research tally duty out of the prohibition bullet | Not landed 2026-11-26: pre-registered probe tied, 3/3 versus 3/3 | A harder fixture or a real run in which the duty is dropped in its current seat |
| SCR-T1 | Three deduplication trims | Not recommended | A recorded reader failure on one of them |

## Evidence vs Inference

- **Verified:** skill measurements; the commit-to-request table above (session history); every D-class citation re-read at its line on 2026-11-26; checkpoint outcomes; registry contents.
- **Inferred:** authorization carryover as the cause of the push drift; reviewer classifications of dormant rows not re-read individually by main.
- **Unknown:** whether a prose clause prevents carryover or only a host gate can; whether any proposed trim changes reader behavior; local demand for the converging ablation mechanism.

## Falsifiability

- The "contracts hold" verdict is wrong if a contradiction between two skills, or between a skill and a recorded correction, is found at cited lines.
- The authorization finding is wrong if any of the six listed requests contained push wording the table omits.
- SCR-D12 is wrong if the L1 cheatsheet bullet is never used without the dispatch contract loaded beside it.

## Owner Decisions and Landing (2026-11-26)

The owner answered the decision form after reading this record: ratify SUR-ED1/ED2; apply both repair groups; adopt P1, P2, P3, P4 and P6 (P6 after a fixture probe); push all commits produced in this session.

- **Ratified follow-through (D1–D3):** the handoff example carries `## Friction Notes`; CKB-DOC2 and UAS-DOC2(b) carry adoption notes in their ledgers and catalogue rows; the catalogue head and the Decision Index point to the adjudication.
- **Record corrections (D4–D11):** CFT-DOC2 removed from four deferred-queue citations; UAS line 45 now says no executed ablation run exists; OSP-DOC2 points to the SUR split; 3XA-1 records the 2026-10-06 digest repair; GW-9/GW-10 point to the checkpoint outcome; GKB-DOC2 cross-references GB-BR1; QUALITY_GATES metrics read 19/19, 9 core + 10 packs, 0 lint warnings, and a 1,776-test floor; one Decision Index entry covers November.
- **Surface consistency (D12–D14):** both cheatsheets carry the third L1 condition and the default-up rule; brief examples show `- In:` / `- Out:`; the skill-map anchor reads `#L20-L54`.
- **P1:** `reflective-risk` now requires the owner's words to cover "this action on this work"; earlier or other-work authorization does not carry over. Existing FM2 pins hold.
- **P2:** the retirement trigger names four recheck events.
- **P3:** WGS-X4b's ledger and the dormant register record the ruling; the register's deferral symmetry guard passes.
- **P4:** six packs gained `## Demotion Triggers` tied to the 2027-01-11 pack review; a parametrized guard now requires the section for every registered pack.
- **P6: not landed.** Rule fixed before the runs: land only if the moved text passed strictly more of three runs than the current text, and at least two. Six fresh agents each received one contract copy (current text: runs 1, 4, 5; moved text: runs 2, 3, 6), the same fixture (48 shipped and 4 retired `SKILL.md` files; prior notes giving 52 and 48) and the same prompt. All six named the population difference before choosing a count — run 4, current text: "48 + 4 = 52 — the session-notes 'discrepancy' is an input-set difference"; run 3, moved text: "52 is the 48 shipped files plus the 4 retired files." A 3/3 tie is not strictly more, so the duty stays in place and the `SS_ADOPTED` pin is unchanged. Limits: one model family, three runs per arm, a fixture whose notes name both tallies, and unblinded scoring; a harder fixture under heavier load could still separate the arms.

## Standing Non-Goals

- No new skill, pack, runtime, route, or model campaign. Core stays nine; the registry stays ten.
- The push of this session's commits was authorized by the owner's form answer on 2026-11-26; this record authorizes nothing further.
