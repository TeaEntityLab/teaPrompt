# Harness and Intent-Drift Rethink — Panel Record (2026-09-06)

> **Status: decided, guarded, and verified — five theses held with changes by a seven-lens panel (7/7 delivered over hub; 7/7 `AGREE WITH CHANGES`); two glossary terms, one Adoption Guard Closure clause, one Durable Lesson, and one recipe bullet adopted; one candidate deferred with a trigger; no skill text changed.** User instruction: "By docs and find records in your memory. Try to think about harness and avoidance of intent drifting etc topics. Then update docs or skills if anything worth updated." The coordinator's packet carried five theses and seven candidates; the panel corrected two packet facts and reshaped four candidates before anything landed.

## Research Question

What is a harness, where does intent drift enter a chain of compressions, which of the loci already have an installed TeaPrompt defense, and does any locus observed in this session's records deserve a doc or skill change under the adoption bar ("would the installed text be better?": name the failure, name the smaller alternative rejected, show existing text does not already say it)?

## Method

Memory recall (Mnemopi) returned transcript pointers; the durable record was the source. Read: the Durable Lessons and Standing Non-Goals, the LLM-as-a-Judge survey's Coordinator Reflection (six-locus compression table), the runtime trust boundary, the recipe packet contract, the Adoption Guard Closure, and this session's records (skill-verification pass, agentflow survey addenda SS/C7/C7b, installed-skills general lessons). One shared packet at the repo root (deleted after synthesis); seven read-only lenses on the `task` backend — evidence auditor, minimality, methodology/architecture, usability, provenance/clean-room, adversarial red team, strategy/governance — each with the pre-yield hub-delivery instruction. Reason tally beside the verdict tally. Two artifacts: this record and the asker-facing answer.

## Panel Consensus

- Decision on the theses: `AGREE WITH CHANGES` 7/7. The changes converge: (a) the defense shape from the compression Lesson is a family for optimizer-read compressions of written intent, not an invariant across every locus (methodology lens `DISAGREE` on invariance; five others "family"); (b) the harness inventory needs budget enforcement and must not call oracle sealing a referee; (c) the repository is not "its own harness" — its author-side referees practised the doctrine, which is a record-level statement; (d) T4's ceiling (no referee for unwritten intent) is correct and bounds every candidate.
- Use-case recommendation: adopt the definitional and guard-shape survivors (docs), keep the session-facing rules where they already live (skills unchanged), defer the tool-status rule with a trigger.
- Reason tally: all seven agreed the compression Lesson already carries the shape; the split was over *destination* (a glossary term that points to the Lesson vs a restatement), not over the thinking. The strongest objection in five of seven deliverables was the same sentence: "ceremony over an already-adopted lesson" — the record answers it by pointing rather than restating (G-2), by dropping numerals and unrecorded items (L-1), and by minting no per-locus skill rules.

## Packet Corrections (evidence beat the packet)

1. **GLOSSARY "harness" occurrences.** The packet claimed 14 occurrences carrying three senses (host harness, harness policy, harness-generated). Five lenses and the coordinator's own grep: every hit is an `eval_harness` playbook test filename or "harness guards"; zero occurrences of the three senses in the file. Those senses live in `06-repo/AGENTS.md` (§Harness Policy), `PROJECT_KNOWLEDGE.md` (North Star; a Decision Index bullet), and `04-agent/workflow-recipes.md` ("Host harnesses add operational safeguards"). G-1's justification was rewritten; its body now disambiguates all three plus `eval_harness`.
2. **Template-defect count.** The packet said "thirteen"; the skill-verification record lists D and FLH rows and never states that numeral; one packet item (a bash 3.2 empty-array crash) is not in that record's landed-fixes table. The Lesson names the recorded defects and no count.
3. **Tool-incident details.** "Successfully wrote N bytes", "386 lines", "15 further edits", "grep miss" are the coordinator's recollection; the record states the truncation, the restore from the pre-edit read, and the diff against HEAD. Tiered as coordinator-claimed below.
4. **Guard collisions.** The record names three collisions (a boundary-token pin in both pack Purposes, an anchored handoff sentence, a status literal) behind four failing tests; "four real meaning changes" is the test count, not the collision count.
5. **E6 tiering.** "30%" and "no automated defense" are author-claimed; the runner's `not_proven` literal is observed at the pin (SS-1) — the packet had bundled them.
6. **Validator paraphrase.** The packet abbreviated the `validate_project_knowledge.py` directive regexes (plurals, `codex`/`claude`, `must not`, `are required to`, list/blockquote prefixes, more verbs); the landed Lesson was dry-run against the real patterns before landing (no match) and the validator passes.

## The Theses as Held (amended by the panel)

- **T1 — Harness.** Host-side machinery that holds when the model does not: authority over gate release, gate sequencing, the record of state, referees, confinement of reachable sinks, **and budget enforcement** (methodology lens: budget is a named host precondition, an envelope field, Loop Anatomy part 2, and the implement Budget Rule; it folds into neither sinks nor referees). Oracle sealing is write-protection of the measure — a confinement — not a referee. TeaPrompt writes contracts for each and operates none. `governed-delivery`'s five host preconditions and the trust boundary's Authority Map are different cuts of the same space; neither list is the other's error.
- **T2 — Loci.** The six optimizer-read loci of the 2026-09-05 reflection stand. Five loci observed this session are distinct by *reader role* (not "reader is not the model" — three of the five readers are models): record→answer (asker), surface→surface (editor), contract prose→template (interpreter/author), tool status→belief (coordinator), coordinator frame→panel (lenses). Lenses named further loci the coordinator missed: measurement→reported count (already adopted as C2), host HISTORY digest→resume (EP-1's neither-exists hatch is the path; prompt text cannot restore dropped tokens), referee pin→author (E5: a guard is itself a compression of intent), session memory→next session (retain gates are loose), and human instruction→coordinator interpretation (this packet was itself that compression; the panel tested it and found the G-1 frame wrong).
- **T3 — Defense shape.** For optimizer-read compressions of written intent: name, seal against the reader, version with `stale`, re-anchor on a risk-set cadence, audit by reason (the Lesson). For the other readers: a local check, not a seal — altitude (record vs answer), currency before propagation, execute-don't-read, artifact-not-message, test-the-frame. A tool status line cannot be sealed; a review frame cannot be versioned. The shape is a family, not an invariant.
- **T4 — Ceiling.** No referee detects drift from intent that was never written; Intent Fidelity, the minimality existence challenge, and the Human Review Boundary are the *defenses* T4 names (write more intent; re-anchor), not counterexamples. No candidate may promise a session guarantee against it — the original G-2 operational test did, and was cut.
- **T5 — This repository.** Its author-side referees caught three real meaning changes this session; an oracle outside the tool (diff against the git index) caught a tool's false success report; the dry-run guard is the referee the templates lacked. Record-level statement; the repository is not a harness for sessions (Standing Non-Goal, bullet 8).

## Locus Table (as of this record)

| Locus | Reader | Installed defense (surface) | Prompt-supplied? | Residual |
| --- | --- | --- | --- | --- |
| intent → spec | planner | `reflective-brief` Intent Fidelity | names the loss | unwritten taste (T4) |
| spec → oracle | executor | `reflective-spec-plan` oracle manifest; `governed-delivery` | contract only; host seals | proxy bar chosen by the author |
| oracle → executor | executor | `reflective-implement` sealed oracles; loop pack verifier immutability, rubric excluded | contract only | host must deny writes |
| verdict → decision | reviser/reviewer | `reflective-review` reason audit; recipe reason tally | yes (visibility) | honest tally not enforced |
| judge → time | unattended critic | loop pack drift spot-check; gate retro | cadence text only | calendar not enforced |
| run → memory | next session | task/continuation packet; ledger tail; AF-19 | producer-side | host digest injected as conversation (EP-1 hatch) — named, no text |
| record → answer | asker | recipe record ≠ answer (SS-9); host manual step | yes | altitude judged by the writer |
| surface → surface | editor | `reflective-implement` currency rule (C7b) | yes (fail-closed sentence) | reconcile-after-unknown |
| contract prose → template | interpreter/author | Lesson (this record) + Closure dry-run clause + pack dry-run guards | author-side guard | stub-blind defects off the gate paths |
| tool status → belief | coordinator | trust boundary "verified tool results"; GLOSSARY Artifact "not a transient tool result"; index diff (practice) | deferred (I-1) | tool-layer bug; prompt cannot fix |
| coordinator frame → panel | lenses | recipe frame-test (this record) | yes (duty) | same-channel confirmation |
| measurement → count | reader of a number | `reflective-research` counts carry command + input set (C2) | yes | — |
| referee pin → author | author | Closure (structural checks, not paragraph pins) | author-side | a green proxy pin |
| session memory → next session | future coordinator | handoff Memory Consolidation; artifact-promotion §4 | loose | TeaPrompt operates no memory ACL |
| human instruction → coordinator | coordinator | `reflective-brief`; this panel's frame-test | partial | the compression under review |

## Required Wording Changes (final, adopted 2026-09-06)

1. `GLOSSARY.md` — new `## Harness / 執行框架`: six-part inventory (adds budget), sealing-is-confinement clause, "writes contracts for these parts and operates none", disambiguation of harness policy / `harness-generated` / `eval_harness`; operational test: a sentence claiming this library or the skill enforces something is a defect. Placed after `## Skill (Workflow Skill)`.
2. `GLOSSARY.md` — new `## Intent Drift / 意圖漂移`: points to the Durable Lesson for the optimizer chain and its shape (not restated); names the non-optimizer readers and "a local check rather than a seal"; states the ceiling; operational test is author-facing ("a lesson, recipe, or skill that names a compression without naming the reader … is incomplete. A glossary entry seals nothing").
3. `GLOSSARY.md` §Adoption Guard Closure — "executable behavior (for a shipped pack template: a stub dry-run over each gate path that template implements)".
4. `PROJECT_KNOWLEDGE.md` — Durable Lesson "A shipped template drifts from its contract prose; only execution finds it" with Pattern / Evidence / Review trigger (validator-shaped; no numeral; trigger scoped to fenced templates in registered packs without a covering dry-run guard).
5. `04-agent/workflow-recipes.md` §Packet and verdict contract — "Frame test" bullet: the packet states the frame-test; at least one named lens answers it before the candidates without re-running the coordinator's research; a frame-testing lens is not a second epistemic channel. Recipe only (2026-07-11 split: method authority = recipe; host manual = tooling).

## Candidate Adoption Ledger

| ID | Candidate | Status | Lens tally (adopt / adopt-with-wording / reject / defer) | Evidence / reasons | Next action or trigger |
| --- | --- | --- | --- | --- | --- |
| G-1 | Glossary term Harness | **Adopted** (wording merged) | 1 / 4 / 2 / 0 | Rejecters: the GLOSSARY-local failure was mislocated (packet correction 1) and the enforcement boundary is already stated (Standing Non-Goal 7; recipe host-wrapper line). Adopters: the six-part inventory exists nowhere; GLOSSARY is the canonical definitional source; the operational test changes an author's next sentence. Landed with the rejecters' facts: justification rewritten, `eval_harness` disambiguated, "this repository's harness" phrasing dropped, budget added, sealing ≠ referee. | Falsifier: an author writes "the skill enforces" after this entry exists and cites nothing — then the term was decorative |
| G-2 | Glossary term Intent Drift | **Adopted** (wording merged) | 1 / 4 / 2 / 0 | Rejecters: a restatement of the compression Lesson violates "pointed to, not restated" and GLOSSARY is not a promotion destination. Adopters: a definition is missing; the non-optimizer readers are unnamed anywhere; the ceiling belongs beside the term. Landed as a pointer plus reader list plus ceiling; the universal handoff-naming test was cut (over-promised against T4; five lenses) and replaced by an author-facing test. | Falsifier: the term and the Lesson diverge, or an author cites the term as a session guarantee |
| L-1 | Durable Lesson: template drifts from contract prose | **Adopted** (wording merged) | 4 / 2 / 1 / 0 | Meets the Lessons intro bar (two records, same pattern, many instances). Rejecter: the dry-run guard, GL-6's falsifier, and the Decision Index already defend it. Adopters: the guard defends one pack's paths; the Lesson carries the pattern for future templates; the reader (interpreter/author) differs from the compression Lesson's optimizer. Numeral and unrecorded item dropped (evidence lens). | Review trigger in the Lesson |
| L-2 | Closure clause: dry-run over each gate path | **Adopted** (wording merged) | 5 / 1 / 1 / 0 | Closure named the class ("executable behavior") without the check; AGENTS.md defers guard shape to Closure; the pinned class phrases stay contiguous. | Falsifier: a pack template ships without a covering dry-run and the guard suite is green |
| R-1 | Recipe frame-test | **Adopted** (wording merged) | 2 / 4 / 0 / 1 | One occurrence (E1: 6/6 lenses confirmed a presupposed direction) on the recipe surface, where SS-9 set the one-occurrence precedent; the smaller alternatives (prior-conclusion field; strongest objection; C7b) were present and failed. Deferrer: this packet's own question 1 already tested the frame — accepted as evidence that the practice works when asked, which is why the duty now sits in the packet, answered by a named lens, not solely on the evidence lens (strategy lens: survives lens omission). Recipe only, not the host manual (strategy lens). | Falsifier: a panel with the frame-test still unanimously confirms a wrong direction |
| I-1 | Tool status line is a claim, not the artifact | **Deferred** | 0 / 0 / 0 / 7 | One occurrence; trust-boundary and GLOSSARY Artifact cover the belief but not the moment; the packet's "cheap check" hedge would have excused the incident (usability, red team). | Trigger: a second tool misreport in any record. If fired, `reflective-implement` Verification: "A tool status line is a claim about an effect, not the artifact. Before a second edit to the same file, or before treating the write as done, read the file or diff it against a copy taken before the write." Not trust-boundary §4, not a Lesson. |
| TK-1 | Extra-work offer ≠ finding | Deferred (unchanged) | — | Same-source rule (session-outline addendum) | unchanged |

## Disagreements / Residual Risks

- Minimality lens: rejects every doc candidate as ceremony over the Lesson; its falsifier is recorded in the G-/L- rows and is the record's own falsifier below. Overruled by 5–6 lenses per row with the reasons above; the record adopts its facts (mislocation; no numerals; no restatement) and its ladder (no per-locus skill rules; nothing on AGENTS.md).
- Red team: L-2's dry-run is stub-blind to defects off the gate paths (bash-version quirks, progress detectors) — a green guard can become the drift (E5 class). Accepted as residual; the packs' own Verification already says stub success is rig-tier evidence.
- Red team: the HISTORY-digest and memory-write loci have no prompt-supplied defense and cannot have one (Standing Non-Goals). Named in the locus table; no text.
- Usability: GLOSSARY is not in the installed unit; the two terms change author lookups, not sessions. Accepted — that is what "update docs" means here; the skills were left unchanged on purpose.

## Evidence vs Inference

- **Observed:** every line cite in the packet's prior-state section re-verified by the evidence lens (Lesson text, six-locus table, Standing Non-Goals, Closure wording, trust-boundary rows, recipe lines, AGENTS Harness Policy); GLOSSARY heading count 31→33; the SS-7/C7/C7b rows; the skill-verification record's landed-fixes table and process incident; GL-6; the validator's regexes and the dry-run of the Lesson text against them; `make all` after landing.
- **Coordinator-claimed:** the tool-incident details in packet correction 3; that six lenses shared the frame in E1 (the record shows 6/0/0 on C7).
- **Author-claimed (surveyed product, 2026-09-05):** "30%" prompt-prohibition failure; "no automated defense — only human supervision".
- **[INFERENCE]:** that the five session loci generalize beyond this repository's practice (one session, one coordinator); that "family, not invariant" is the right ontology (methodology lens's argument, adopted).
- **Not done:** no skill edited; no external checkout opened; no host operation (sealing, sampling, rollback) claimed.

## Evidence Actually Checked

Coordinator: `PROJECT_KNOWLEDGE.md:51-99`; `plans/llm-judge-lifecycle-survey-2026-09-05.md:134-176`; `GLOSSARY.md` (headings, Closure, playbook harness lines, Skill entry); `04-agent/runtime-trust-boundary.md` (Authority Map, §4); `04-agent/workflow-recipes.md:152-168`; `04-agent/artifact-promotion.md` destinations; `06-repo/AGENTS.md` Harness Policy; `plans/validate_project_knowledge.py` (directive patterns; lesson evidence check); `plans/tests/test_glossary_structure.py`; the three session records cited above. Executed: grep counts, the validator dry-run, `make all`. Lenses: per-deliverable "Evidence actually checked" sections (consumed in-session; durable trace is this record and the guard).

## Falsifiability

This record is wrong or must be re-litigated if: (1) an author writes an enforcement claim into a skill after the Harness entry exists and no guard or reviewer cites the entry; (2) the Intent Drift entry and the compression Lesson diverge in shape; (3) a registered pack template is edited without a covering stub dry-run guard and the suite stays green (L-1's trigger and L-2's clause were decorative); (4) a panel run with the frame-test still unanimously confirms a wrong currency direction; (5) a second tool misreport occurs and I-1 is neither adopted nor re-litigated; (6) any of the adopted wording is absent from its surface or present on a second surface (guard).

## Completion Ledger

| Item | Status | Where |
| --- | --- | --- |
| Memory recall + doc read; packet; seven lenses delivered over hub | `verified` | Method |
| Two glossary terms, Closure clause, Lesson, recipe bullet landed | `verified` | Required Wording Changes |
| I-1 deferred with trigger and destination; TK-1 unchanged | `verified` | ledger |
| Guard | `verified` | `plans/tests/test_harness_intent_drift_rethink_record.py` |
| Indexes | `verified` | `PROJECT_KNOWLEDGE.md` Decision Index; case-study State Ledger |
| Repository verification | `verified` | `make all` after the changes |
