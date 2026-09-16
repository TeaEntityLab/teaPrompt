# All Thirteen Skills vs the September Concepts and Surveys — Review Record (2026-09-16)

> **Status: decided — six-lens review, `AGREE WITH CHANGES` 6/6; fourteen defect findings fixed (one template, two example files, three documentation files, four record surfaces, eight guard functions), six findings held as candidates, twelve ledger rows; no concept wording adopted.** User instruction: "Review all skills for newest concepts and surveys." Every adopted September sentence is present once at its recorded surface (L1, 78 candidates checked); no fired trigger is unhandled and no dated gate has passed (L3, 86 candidates); the router, fixtures, and cheatsheets agree to the phrase (L4, 353 phrases). The defects were in the layers around the skills — a backlog-loop template that retired untouched work, companion examples two fixes behind their templates, an installation guide counting three packs, a survey banner contradicting its own ledger, five GD-18 adoptions with no guard, and guards that pinned four-word fragments. Authorization basis: a review instruction fixes defects in TeaPrompt's own artifacts against their own stated contracts (precedent `cdfa835`); adoptions of new wording, cuts that remove a rule, metadata relabels, and cheatsheet cues are held as candidates. Verification state lives in the Completion Ledger.

## Research Question

Do the thirteen installed skills (nine frozen core, four registered domain packs) correctly reflect every adoption from the September 2026 surveys and reviews, and is any fired trigger, defect, or inconsistency outstanding? "Newest" = the twenty skill-touching commits since the 2026-09-05 baseline and the eighteen records dated 2026-09-03 or later (packet §Scope).

## Direct Answer (as of 2026-09-16)

- **Adoption fidelity: intact.** Seventy-eight adopted candidates (GL, CX, GA, GD anchors, GS Never sentences, JL, OG, A-7a, AF82, GD-18 R1–R9, GW, XM, RS) are each present exactly once at their recorded surface; the only alterations are the three recorded same-day merges (`b711499`), the GW-5 compaction restored on the second pass, and the RS-2 correction — all attributed to their commits.
- **Triggers: none fired unhandled; none expired.** Eighty-six deferred/held/record-only candidates enumerated; every dated gate points at 2026-10-11; GD-19, M5, and the traceability checklist fired and were resolved; GE-1's consideration gate fired and its landing was reverted for lack of direction.
- **Routing: consistent.** R8–R12 backed by fixtures at the recorded floors (16/128, 47/134, 26/91); EN/zh-TW cheatsheet parity holds; GD-17 (no pack names in core cues) holds.
- **Defects: fourteen findings, all in TeaPrompt's own artifacts, all fixed here** — one template (C1), two companion example files (L2.1–2), six documentation lines in three files (L4.1–3), one contradictory banner plus its guard (L6.1), two misplaced roadmap rows (L6.2), seven stale QUALITY_GATES figures (L6.3–4), and eight guard functions strengthened or re-pinned (L1.1–3, L4.4, plus the astra and skill-verification re-pins).
- **Held: twelve candidates** (Candidate Adoption Ledger) — pack and core-skill cuts, `context_load` relabels, cheatsheet cues for AF82-1/EP-1, a GLOSSARY status-vocabulary gloss, an implement-side `spec_version` cascade, trigger hygiene for `—` rows. Each has a named failure and a smaller alternative; none lands without direction.

## Method

Packet at the repository root (`review-packet-skills-september-2026-09-16.md`, deleted after synthesis) carrying scope, prior conclusions, standing rules, the deliverable shape, and six lens assignments. Six read-only scouts in one batch, each delivering the full §-shape by hub before yielding — 6/6 delivered, zero recovery tiers. Coordinator slice: fence-extracted all nine pack templates from current bytes and rigged the three never-rigged ones (sequential, router, backlog) plus regression runs of fan-out and multi-wave; three lens citations re-read locally (all held). Landing reviewed as landed bytes by an independent pass before commit (packet contract, 2026-09-15).

**Scope / acceptance:** fidelity of every September adoption; cross-skill consistency; every deferred trigger's state; routing and discoverability; minimality and budget; records and guards; template execution. Fix defects; ledger candidates; keep both flow packs under the 20,000-character lint budget; guards fail on the previous bytes; `make all`.

## Findings

Numbered by lens; severity per `reflective-review`. Every finding is attributed.

| # | Finding | Where | Severity | Introduced by | Disposition |
| --- | --- | --- | --- | --- | --- |
| C1 | **Backlog loop retires untouched work.** With a globally green verifier, a no-op agent and a crashing agent (`\|\| true`) each retired all three tasks and exited 0 "backlog empty"; real work was indistinguishable from none. Violates the pack's first rule (never trust "done" without an external verifier of the work) and Anatomy #4. | `flow-loop-harness` Task-Ledger Backlog template | High | 2026-07-11 template; pre-existing | Fixed (F1) |
| L2.1 | Example 5 (DAG) omits the RS-1 quorum-sink rule and dates its rig 2026-09-14 | `skills/examples/flow-control-generator.examples.md:104,108` | Medium | `be0d16e` | Fixed (F2) |
| L2.2 | Example 1 (fix loop) omits the RS-2 `state/` exclusion; Example 2 (backlog) stop conditions predate F1 | `skills/examples/flow-loop-harness.examples.md:17-18,22,41` | Medium | `be0d16e`/`e88bf5b`; F1 | Fixed (F2) |
| L4.1 | Installation guide says "the three domain packs" | `SKILL_INSTALLATION.md:86-87` | Medium | `526094a` | Fixed (F3) |
| L4.2 | "Last verified: 2026-07-18" on both installation guides after September edits | `SKILL_INSTALLATION.md:5`, `.zh-TW.md:7` | Low | pre-existing | Fixed (F3) |
| L4.3 | zh-TW README omits the packs and miscounts examples | `README.zh-TW.md:17,37,39` | Low | pre-existing | Fixed (F3) |
| L4.4 | ROUTE-001 actuals never asserted against the validator constants | `test_validate_route_fixture.py` | Low | pre-existing | Fixed (F5) |
| L6.1 | Survey banner says "adopted nothing on any installed surface" while its ledger, Decision Index, and both case-study rows say A-7a adopted; the guard pinned the contradiction | `astra-efficiency-rules-survey-2026-09-10.md:3,124`; its guard | Medium | `20a80a4` | Fixed (F4) |
| L6.2 | GD-19 and the traceability checklist sit under "Still trigger-gated" though resolved 2026-09-14 | `whole-project-roadmap-2026-07-11.md:129,134` | Low | `b5c3a10` | Fixed (F4) |
| L6.3 | §4.1 still says 44 groups / 124 phrases; four sections agree on 47/134 | `QUALITY_GATES_SUMMARY.md:116` | Low | `b5c3a10` | Fixed (F4) |
| L6.4 | Snapshot figures lag the tree: 148 index files (154 with this record), 184 scanned (190), scaffold "25,405 chars" (26,291 as lint measures) | `QUALITY_GATES_SUMMARY.md:22,42,68-69,286` | Low | `b711499`…`75a99d4` | Fixed (F4) |
| L1.1 | GD-18 R2, R3, R5, R6, R9 landed with no guard; the gate test checked only `intent`/`acceptance` ends, the trailer test only headings | `test_governed_delivery_adoption_state.py` | Medium | `1113dc0` | Fixed (F5) |
| L1.2 | GW-5 guard pinned four tokens; the authority hierarchy between them was unguarded | `test_governance_workflow_self_control_adoption.py::test_gw5…` | Low | `b5c3a10` | Fixed (F5) |
| L1.3 | XM-6/XM-7 guards pinned four-word fragments, not the operative duties | `test_managed_skill_promotion_adoption_state.py::test_september…` | Low | `9a756e5` | Fixed (F5) |
| L5.1 | Both flow packs within 16–21 characters of the 20,000 lint budget | loop 19,984; generator 19,979 | High (maintainability) | September additions | Loop pack: F1 landed net −28 (19,956); generator: held (H1) |
| L5.2 | `context_load` incoherent with size: packs at 16–20k declare `medium`; `dispatch` 11.4k declares `low` | pack and dispatch frontmatter | Medium | admission decisions | Held (H2) |
| L5.3 | Intra-skill duplicates: review:158-159, implement:42/200, dispatch:60/79, minimality ×4, risk:31-32, governed-delivery ×5, handoff-retro:55/79, brief:40/105, research:42/135 | nine skills | Low | mixed | Held (H3) |
| L4.5 | AF82-1 and EP-1 adopted on `reflective-dispatch` have no cheatsheet cue, fixture, or example | cheatsheets; `reflective-dispatch.examples.md` | Medium | `e723196`, `2fc377b` | Held (H4) |
| L3.1 | Status words `Held`, `Record-only`, `Concept-only`, `Blocked`, `Reserved` sit outside the GLOSSARY Adoption Guard Closure vocabulary | `GLOSSARY.md` §Adoption Guard Closure | Medium | pre-existing | Held (H5) |
| L3.2 | Thirty-odd record-only rows carry a `—` trigger; four candidate pairs share one trigger (I-1/A-5; AH-3/AH-14; GA-13/XS-4/GW-13; JL-9/JL-17) | agentflow, judge, astra records | Low | pre-existing | Held (H6) |
| L2.3 | `spec_version` cascade: spec-plan and the pack stale every keyed artifact; implement stales only dependent ledger items | `reflective-implement:115` vs `reflective-spec-plan:230` | Low | `1113dc0` | Held (H7) |
| L2.4 | Observations, no change: `governed-delivery` has no inbound escalation (host-invoked by design, GD-17); `exit 2` means cap in the loop pack and gate failure in the generator (each pack states its own table); Human Review heading names vary across four skills; example section headings vary; `skill-map.md` lists core skills by name (no contract requires one-liners) | — | Low | — | No change |

## Coordinator Rig Results (current bytes, pre-fix)

| Template | Case | Exit | Reading |
| --- | --- | --- | --- |
| sequential | happy / empty spec / tests fail / stage-1 agent exits 1 over a stale spec | 0 / 1 / 1 / 1 (spec truncated to 0 bytes) | fail-closed; stale spec cannot survive |
| router | `bug`, `Bug.`, `feature request`, multi-line | 0, routed | normalization works |
| router | `- bug`, `**bug**`, empty | 2, `unroutable label` | fail-closed by stated policy |
| backlog | no-op agent, green verifier | **0, three tasks "done"** | defect C1 |
| backlog | crashing agent, green verifier | **0, three tasks "done"** | defect C1 |
| backlog | verifier red at start | 3 preflight | as designed |
| fan-out | one empty branch: strict / `MIN_OK=2` | 2 / 0 | unchanged since 09-14 |
| multi-wave | partial failure to cap / all fail | 2 / 3 | unchanged since 09-14 |

## Landed Fixes

**F1 — Backlog template (`flow-loop-harness`).** A `snap()` function (the fix loop's signal: tracked diff stat plus untracked count with the worktree-relative `$STATE` excluded; empty outside git) is read before dispatch; a task is retired only when the verifier passes *and* the workspace changed; otherwise `- no change: <task>` and exit 3. Outside git the check is skipped (no signal), matching the fix loop's degrade-gracefully rule. The deviation sentence now states the rule. Offsets (zero-sum, no rule lost): Verification 1 no longer re-enumerates Anatomy #6's exit codes; Verification 3 no longer restates Anatomy #5; the writer-critic "Caution" no longer restates the Methods stop condition and Never #50; a meta remark ("Guidance, not a new template or runtime") and a dated vendor-product parenthetical in Host-Native Alternatives were dropped; the dispatch comment lost its ledger-tail hint (Anatomy #3 carries that rule). Pack: 19,984 → 19,956.

| Case (landed bytes) | Exit | Ledger |
| --- | --- | --- |
| no-op agent, green verifier | 3 | `- no change: task one (iter 1)` |
| crashing agent, green verifier | 3 | `- no change: task one (iter 1)` |
| agent writes only under `state/` | 3 | `- no change` — residue is not progress |
| agent creates a file per task | 0 | three `done` |
| agent edits a tracked file per task | 0 | three `done` |
| `MAX_ITER=2` with real work | 2 | two `done`, cap |
| verifier red at start | 3 | preflight |
| outside git, no-op agent | 0 | check skipped (no signal) |
| outside git, verifier red | 3 | preflight |

The first landing of F1 stalled every task outside git (both snapshots empty compared equal); caught by the rig's outside-git case before commit and fixed with the empty-signal skip — the fourth time this month a rig matrix found what the table did not contain.

**F2 — Companion examples.** Example 5 states the quorum-sink rule and records the 2026-09-16 sink case; Example 1 states the `state/` exclusion and the residue case; Example 2's stop conditions carry the unchanged-workspace exit.

**F3 — Documentation.** "four domain packs"; both installation guides re-verified 2026-09-16; zh-TW README mirrors the English North Star, `skills/`, and `skills/examples/` lines.

**F4 — Records.** Astra banner and Completion Ledger row now say what the ledger says (panel record-only, then A-7a by user direction); GD-19 and the traceability row moved into the roadmap's Adopted table with their guards named; QUALITY_GATES §4.1 → 47/134; snapshot figures re-measured (190 scanned, 154 indexed once this record was added, scaffold 26,291).

**F5 — Guards.** GD-18 R2/R3 pinned on the gate test, R5/R6 on the trailer test, R9 (skill-map trigger fairness) on the GD-17 test; GW-5's three hierarchy clauses pinned; XM-6's "independent pass reads each record claim" and XM-7's "fixture-backed first … passing fixture set bounds the phrases … fixture-backed or written" pinned; ROUTE-001 actuals asserted against its constants; the astra guard re-pinned to the corrected banner. Each strengthened guard was mutation-checked: R2 hollowed, R5 dropped, R9 dropped, GW-5 hierarchy dropped, XM-6 duty dropped — all five fail. The backlog dry run lives in this record's guard.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| H1 | Generator-pack headroom: cut the Acquisition-ladder paragraph (379 chars) and the DAG rejected-extras note (204) | Held 2026-09-16 | L5 measured both unpinned; both carry rules (promotion gate; rejected-features marker); 21 chars headroom | Lands on direction, or as the zero-sum offset of the next generator defect; the 2026-10-11 lint-tier decision (GW-9) is the alternative |
| H2 | `context_load` relabels: packs `medium`→`high` at 16–20k; `dispatch` `low` at 11.4k | Held 2026-09-16 | `governed-delivery` label pinned by its guard; `dispatch` `low` was a June panel decision (never defer the router) | Direction plus guard re-pin; falsifier: a host defers a pack at `medium` and the deferral costs nothing |
| H3 | Intra-skill duplicate cuts on nine skills (L5.3 list; largest: `governed-delivery` transcript rule ×5, `reflective-minimality` debt marker ×4) | Held 2026-09-16 | Core skills are additive-only by standing constraint; each cut removes one copy of a rule the skill states elsewhere | Direction; the OG-1/GW-4 discipline is the smaller alternative in force (search before add) |
| H4 | Cheatsheet cues (EN + zh-TW) and a dispatch example for AF82-1 (loaded-skill conflict) and EP-1 (resume from packet) | Held 2026-09-16 | Both rules are on `reflective-dispatch`; neither has a cue, fixture, or example; both are agent-internal operating rules a user rarely phrases | Direction; falsifier: a user phrase about conflicting skills or resuming from a packet misroutes |
| H5 | GLOSSARY gloss naming `Held`, `Record-only`, `Concept-only`, `Blocked`, `Reserved` as sub-families of `Deferred`/`Rejected` | Held 2026-09-16 | 86 rows use them; the Closure text names five states; guards parse by literal | Direction; the 2026-10-11 checkpoint is the natural seat |
| H6 | Annotate `—`-trigger rows as `closed: already held` / `closed: out of scope`; merge same-trigger pairs | Held 2026-09-16 | L3 table | 2026-10-11 checkpoint |
| H7 | `reflective-implement` GA-2 rule widened to every `spec_version`-keyed artifact, matching spec-plan B2 and the pack | Held 2026-09-16 | implement stales "dependent ledger items"; GD-18 R1 widened the other two surfaces only | Direction; falsifier: a run re-plans against a stale packet the implement ledger did not flag |
| H8 | Examples: one heading set across the four loop examples | Held 2026-09-16 | L2.3; examples validator passes; style | Direction |
| H9 | `skill-map.md` one-line descriptions for the nine core skills | No change 2026-09-16 | No contract requires them; the cheatsheet carries the cues | — |
| H10 | Inbound escalation route to `governed-delivery` | No change 2026-09-16 | Host-invoked by design (GD-17) | — |
| H11 | Unify `exit 2` semantics across packs | No change 2026-09-16 | Each pack states its own exit table; callers read the pack they ran | — |
| H12 | Second-order guard weaknesses (heading-only pins on the nine GD templates; sub-six-word fragments in seven guards) | Held 2026-09-16 | L6 table; the five highest-value pins were strengthened (F5) | Next guard pass |

Deterministic guard: `plans/tests/test_skills_september_concepts_review_record.py` (record shape and counts; backlog dry run on the landed template, failing on `75a99d4`; loop pack under budget).

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Every September adoption present once at its surface | Verified (scout) + 3 coordinator spot-checks | L1 table; `grep` per candidate |
| No fired trigger unhandled; no dated gate passed | Verified (scout) | L3 table, 86 rows; dates vs 2026-09-16 |
| Fixture floors and cheatsheet parity | Verified (scout, counts) | L4: 16/128, 47/134, 26/91 |
| Backlog template false completion | Observed / executed | coordinator rigs A, C on `75a99d4` bytes |
| F1 repairs hold; real work still retires; outside git skips the check | Observed / executed | rigs on landed bytes (nine cases) |
| Strengthened guards can fail | Observed / executed | five mutation checks |
| Pack sizes | Observed | `len()` 19,956 / 19,979 |
| Lens findings not independently re-derived (L5 duplicate pairs, L6 weak-assertion list) | Scout-read | cited lines; sampled, not exhaustively re-read |
| Six lenses are six independent channels | `[INFERENCE]`-bounded | same model family; one epistemic channel per `reflective-review` Evidence Tiers; the rigs are the non-model channel |

## Evidence Actually Checked

- Six lens deliverables via hub (`L1AdoptionFidelity`, `L2CrossSkillConsistency`, `L3DeferredTriggers`, `L4RoutingDiscoverability`, `L5MinimalityBudget`, `L6RecordsGuards`), each with a Claims Ledger and Socratic questions; transcripts at `history://<label>`.
- Coordinator: nine templates fence-extracted (`bash -n` / `py_compile` all pass); rigs under `/tmp/rig-all` — sequential (4 cases), router (8 labels), backlog (9 cases on landed bytes, 3 on prior), fan-out (2), multi-wave (2); `git diff` of extracted fix-loop, writer-critic, multi-wave blocks before/after F1 (unchanged).
- Coordinator spot-checks: `agent-flow-control-research-2026-07-11.md:50`, `reflective-spec-plan/SKILL.md:155`, `flow-loop-harness/SKILL.md:50` (held); validator counts re-measured (`validate_links.py`, `lint_skills.py`: 190 files; `index.json`: 154).
- Not executed: RSIAgent-style host runs; the conditional router on a real host (still uncovered, per GW-6).

## Falsifiability

- The fidelity claim is wrong if a September record quotes wording absent from its surface; L1's table lists each pair — re-grep it.
- F1 is wrong if a backlog task legitimately completes without changing the worktree (a pure external effect); the loop then exits 3 at that task and a human decides — the pack's stated preference over a silent retire.
- The trigger audit is wrong if a record's trigger condition is satisfied by the tree and L3 read it as unfired; the 86-row table names the grep for each.
- Held candidates are wrong to hold if a named falsifier fires (H2, H4, H7 name theirs).

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Six lenses delivered, synthesized, decisions preserved | done | Findings; six §-shape deliverables |
| Backlog template repaired with zero-sum offsets and a dry-run guard failing on `75a99d4` | done | F1; `test_skills_september_concepts_review_record.py` |
| Examples, docs, records, and guards fixed | done | F2–F5; mutation checks |
| Fourteen defect findings fixed; six held; twelve ledger rows with triggers | done | Findings table; Candidate Adoption Ledger |
| Both flow packs under budget | done | 19,956 / 19,979 |
| Independent landing review before commit | done | `AGREE` in substance: F1 diff, sizes, all nine rig rows and the HEAD defect, F2–F5, counts, and the guard reproduced; two nits fixed before commit (an unlisted comment trim in the F1 offsets; the index figure, which moved to include this record) |
| Decision Index entry; `index.json` regenerated; packet deleted | done | `PROJECT_KNOWLEDGE.md` |
| Full repository gate | done | `make all` |
