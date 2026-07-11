# Flow Pack Coverage Panel Record (2026-07-11)

Six-lens parallel adversarial review of `skills/flow-control-generator` + `skills/flow-loop-harness` COVERAGE against the full `plans/` survey corpus — the reverse question of the same-day legitimacy panel ([flow-control-pack-panel-record-2026-07-11.md](flow-control-pack-panel-record-2026-07-11.md)): not "is the pack legitimate" but "does the pack implement every possible-and-worthy flow-control idea already recorded in `plans/`" (user directive). Protocol: `parallel-lens-review-packet` — one shared packet (repo root, deleted after synthesis), six read-only lenses with disjoint survey slices, synthesis with adoption ledger. Adoption state lives in the P8–P15 rows of [agent-flow-control-research-2026-07-11.md](agent-flow-control-research-2026-07-11.md); this record holds the panel evidence.

Baseline: branch `main`, HEAD `1c4199d`; `make all` green at 752 tests before the panel's changes.

## Panel Packet

`review-packet-flow-coverage-2026-07-11.md` (temporary, repo root): pack inventory (7 templates, Script Contract, Loop Anatomy, exit codes), prior-decision constraints (P6/P7 deferrals, Standing Non-Goal, frozen nine core, evidence tiers, bash 3.2), required output shape (candidate table with verdict per idea, ≥3 Socratic questions, strongest objection, decision), questions Q1–Q5 (worthy absences; correct absences with prior-rejection cites; contradictions; recipes-vs-SKILL landing; verification bar).

## Lenses

| Lens | Survey slice (disjoint) | Decision |
| --- | --- | --- |
| LoopStateMiner | harness-1-state-ledger-research, memory-mechanisms-research-2026-06-25, agent-flow-control-research-2026-07-11 | AGREE WITH CHANGES |
| OrchestrationMiner | five-layer-agent-sop-reference-record-2026-07-04, agentic-sop-workflow-reflection-2026-06-13, agent-tooling-research-2026-06-25, agent-workflows-plan, skill-workflow-research-synthesis | AGREE WITH CHANGES |
| HarnessCaseMiner | vllm-micro-agent record + brief (2026-06-30), openfugu record + brief + reference plan (2026-06-25) | AGREE WITH CHANGES |
| PanelArchaeologist | multi-agent-panel-consensus-2026-06-25 (138 KB, full), external-adoption-case-studies-2026-06-20 | AGREE WITH CHANGES |
| GovernanceBoundary | governance-rules-rethink-review-2026-07-11, workflow-possibilities-constraints-review-2026-07-06, skills-runtime-legitimacy-panel-record-2026-07-06, ponytail-minimality-reflection, runtime-governance-learning-plan, project-knowledge-authority-promotion-decision, ROUTING_CONTRACT | AGREE WITH CHANGES |
| ReflectionMiner | storm-perspective-discovery, fable-5-scaffold-provenance, project-adjustment, skill-optimization, socratic-change-inquiry, knowie-project-knowledge reflections; code-followups-plan; prompt-library-build-plan | AGREE WITH CHANGES |

GovernanceBoundary additionally produced the scoring rubric (R1 minimality ceiling … R13 survey-grounded provenance) and an 18-item veto list (V-01 TeaPrompt runtime … V-18 PK-over-AGENTS authority inference) that the synthesis scored every candidate against.

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES` (6/6). The pack's coverage is sound: no lens found a survey-accepted flow idea wrongly absent, and no lens found the pack silently resurrecting a survey-rejected proposal (PanelArchaeologist, Q3: zero first-class contradictions; one interpretive naming collision, resolved by boundary wording, not rename).
- **Shape:** worthy gaps were governance-lifecycle wording and three small template features — not missing topologies. The two biggest candidate topologies (Conductor DAG, dedicated multi-wave ReMoM) were deferred on the pack's own local-gap/signal-accounting discipline: external mechanism detail without local recurrence evidence does not buy a new template the day after the minimality dissent was recorded.

## Adopted (P8–P11, P14 — all implemented 2026-07-11)

1. **P8 governance wording, both SKILL bodies:** methodology-vs-operationalization sentence in each Purpose (PAN-CHG-01); Never additions — platform vocabulary is never an adoption mandate (GOV-003), generated stages never edit their own gates (GOV-015), epistemic perspective expansion is never scripted as parallel fan-out (RFM-01), cap exhaustion never returns last unverified output (HCM-028, OpenFugu negative example), run state is never project memory and promotion goes through handoff-retro + §4(c) memory-write provenance (GOV-011, LSM-022, RFM-R2 homonym disambiguation); Demotion Triggers sections (GOV-001); stub-success-is-rig-tier clause in both Verifications (GOV-014); recurrence + human approval before team-standard elevation (GOV-005); generated-by provenance comment in Script Contract item 1 (RFM-02); per-call timeout as host-provided wrapper, macOS caveat (HCM-015, C2); orchestrator plan-is-data-not-authority comment (GOV-010) and Stop-Doing #2/AY boundary prose (PAN-CHG-02 — boundary line adopted, rename rejected for vocabulary fidelity to the surveyed sources); topology-selection local-gap + signal-accounting sentence (GOV-004, PAN-CHG-03).
2. **P9 parallel quorum gate:** `MIN_OK` env var — empty = strict (any branch failure or zero non-empty outputs aborts, exit 2), `N` = explicit ReMoM-style partial-failure quorum (HCM-005, HCM-016/032 skip-on-error-never-default). `wave_wait` now counts failures instead of dying mid-wave, so strict mode reports total failures at the gate.
3. **P10 router observability:** `route-trace` line appended to `state/flow.log` before dispatch; fail-closed vs default-up documented as an explicit policy choice per ROUTING_CONTRACT R4/R5 (GOV-006/007; HCM-003 folded in).
4. **P11 loop state hygiene:** RESUMED stanza on restart with non-empty ledger (if-guarded — `[ -s ] && …` at top level is a `set -e` kill on fresh runs); ledger tail documented as the context-compaction budget (harness-1 Budget Rule); `state/` documented disposable-per-run, kept for post-run review (auditability argument LSM-002 rejected auto-prune); writer-critic template header names its by-design anatomy deviations (LSM-R05); backlog dispatch comment points at fix-loop ledger-tail pattern for shared-constraint tasks (LSM-R04).
5. **P14 recipes cross-refs:** Looper Topologies see-also block (sop-compiler, workflow-engine §4–§6, runtime-trust-boundary, flow packs with explicit-script-intent qualifier); Parallel Lens Review input-contract/lens-cap/merge-owner line → sop-compiler §4, workflow-engine §6 (ORC-03/07 — cross-reference, never duplicate).

## Deferred / Escalated (P12, P13, P15)

- **P12 Conductor-style DAG executor template** (HCM-024/025, HCM's High priority). Deferred on R1 + GOV-004 + the pack's own signal-accounting rule: OpenFugu's `ultra.py --self-test` proves the mechanism is stdlib-scriptable, but no local task has needed dependency-gated fan-out that pipeline/parallel/orchestrator cannot express; HCM's own Socratic question concedes sequential + explicit state-file naming may cover ~everything local. Trigger: first such local task.
- **P13 dedicated multi-wave ReMoM template** (HCM-004). Composition note adopted instead (Topology Selection: parallel template inside a flow-loop-harness loop with state-file truncation between waves). Trigger: recurrence of real multi-wave runs.
- **P15 frozen-core parity items** (RFM-05: reflective-research Blind Spots parity with 05-domain/research.md; historical-banner forward pointers in June plans). Outside pack scope — core skills are frozen and plans-file hygiene is its own deferred item (governance rethink E2). Escalated for a separate review; the panel record is the paper trail.

## Rejected (with the veto that fired)

- STORM/perspective fan-out as a generator topology row — RFM-01; prior rejection storm-reflection §Rejected Alternatives (R-STORM skill, fixed quotas). Landed as a Never line instead.
- Fable-style provenance ledger header on every generated script — RFM-02; scaffold-provenance targets third-party mirrored code, not locally generated scripts; §4 owns L3 provenance. One-line generated-by comment adopted instead.
- Harness-1 semantic columns (claim/source/status) in the default loop ledger — LSM-010: intentional layering; semantic ledgers belong to reflective skills' in-task State Ledger, operational ledgers to `state/`.
- mem0/MemPalace-style memory backends for loop state — LSM/memory survey: repo-native Markdown only (V-01-adjacent; memory-mechanisms Direct Recommendation).
- Orchestrator-Workers rename to planner-workers — PAN-CHG-02 alternative; rejected for vocabulary fidelity with the advisory-tier survey sources and shipped P5 discoverability sections; boundary prose adopted instead.
- Retry-with-exponential-backoff (HCM-017: not documented in any slice source — no survey basis); semantic-router families, trace/replay, contract-repair, learned coordination weights, grounding-encoder fusion, seven-slot litellm pool (HCM-011/012/013/026/007/027: V-01 Standing Non-Goal, serving-layer); auto-recipe hidden multi-call identity (HCM-033: V-11 silent rigor change).
- Numeric token budgets with enforcement (HCM-014): needs a serving runtime; iteration/concurrency/wall-clock caps stay the script-level budget vocabulary.
- New dispatch route rows / cheatsheet quick-cues (V-07, P7 deferral honored); skill merge (V-08, P6); tenth core skill in any form (V-02; June panel AX/CD/BN).

## Shared Findings

1. The June panel consensus and case studies form a coherent rejection perimeter (no TeaPrompt runtime, no tenth core skill, no mandatory panels) that the pack respects; what the surveys ACCEPTED for flow control (looper-topology vocabulary, multi-voice as optional method, holdout-before-tune) all landed on other surfaces, so the pack's coverage duty was governance mirroring, not idea transplantation (PAN, ORC, GOV concur).
2. Layering is load-bearing and now explicit: cross-session project memory (repo Markdown) ≠ in-task semantic State Ledger (reflective skills) ≠ per-run operational ledger (`state/`) — the State Ledger homonym was the panel's most repeated confusion risk (LSM-022, RFM-R2).
3. The surveys' control-plane depth (five-layer α–ζ, SOP compiler gates, per-action trust boundaries) is deliberately NOT topology content; cross-references keep the pack thin while making the depth reachable (ORC-02/04/05: "confirmed — by design").
4. Verification bar: the pack met the stub-dry-run bar but not the tier honesty around it; stub≠deploy wording closes GOV-014. Rig-tier evidence claims are now labeled as such in both skills.

## Disagreements / Residual Risks

- **HCM priority vs panel verdict on P12:** HarnessCaseMiner rated the Conductor DAG template High; GovernanceBoundary's R1/GOV-004 and the minimality trajectory outweighed it. Preserved here as the strongest pro-add dissent; the P12 trigger is deliberately cheap (one local task) so the dissent re-fires on first real demand.
- **Trigger-phrase collisions** ("pipeline", "orchestrate", "loop until") between pack triggers and dispatch vocabulary remain unmeasured until P7's ROUTE-002/003 holdout groups exist (RoutingDiscovery 07-11a, RFM-R3, PAN-SOC-01).
- **PAN-SOC-04 precedent question** — whether user-directed L2 exceptions on top of DOMAIN_PACK_SKILLS are now the standing path around the June "no runtime" seal — is answered by this record only for THIS pack (scripts host-executed, runner never operated); any future pack claiming the same exception needs its own panel.
- Writer-critic remains the pack's only advisory-tier gate; its deviation label is honesty, not mitigation. A deterministic companion check (GOV Socratic Q2) stays an open design question for users who reach for it.

## Evidence Actually Checked

- **Executed (this panel):** six `task` lenses over disjoint slices (all six full outputs read via `agent://`, not previews); post-adoption rig re-verification of changed templates (see P9–P11 transcript below); `make all` before (752 passed) and after adoption.
- **Read:** every markdown survey in `plans/` was covered by exactly one lens slice (30 records; the 138 KB multi-agent-panel-consensus read in full by PanelArchaeologist); both SKILL.md files read fully by every lens.
- **Author-claimed / [INFERENCE]:** lens coverage judgments are inference over cited quotes; survey line numbers are lens-reported and spot-checked, not independently re-verified line-by-line.

## Falsifiability

- Wrong if a `plans/` survey records a flow-control mechanism that is worthy under R1–R13, absent from the pack, and absent from this record's candidate dispositions — that is a missed-coverage finding against THIS panel.
- Wrong if P12/P13 triggers fire and the deferral is silently ignored (adoption ledger discipline: rows must move to Adopted or a re-litigated rejection).
- The candidate ledger (P8–P15) lives in `agent-flow-control-research-2026-07-11.md`; the deterministic guard for adopted wording is `plans/tests/test_flow_pack_adoption_state.py`.
