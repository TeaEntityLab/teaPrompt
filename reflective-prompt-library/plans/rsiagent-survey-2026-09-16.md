# RSIAgent (`AetherLabsAI/RSIAgent`) — Survey and Template-Repair Record (2026-09-16)

> **Status: decided — two template repairs landed, no wording or mechanism adopted from the source.** The object is a benchmark research harness for training-free self-improvement (memory, not weights). Its ten core concepts were mapped against every installed TeaPrompt surface; none needed a sentence. Two of its failure classes, however, reproduced as defects in TeaPrompt's own executable templates — the loop pack's no-progress exit was dead whenever `state/` sat inside an un-ignored git worktree, and the generator pack's DAG quorum gate accepted a sink left by a prior run — and both were repaired in place with dry-run guards that fail on the previous bytes. Clean-room throughout; the surveyed project's vocabulary is guarded out of installed surfaces. Verification state lives in the Completion Ledger.

## Research Question

User instruction: "Survey https://github.com/AetherLabsAI/RSIAgent and its core value concepts and record docs and update skills if worthy." (repository accessed 2026-09-16)

What does the framework actually establish, at what evidence tier, and does any of it expose a verified gap on an installed TeaPrompt surface? A generic "if worthy" fires no named or dated gate; the standing bar applied per candidate: a verified gap on one installed surface, a named failure the change defends against, a smaller alternative rejected, and a deterministic guard.

## Direct Recommendation (as of 2026-09-16)

- **Study: yes.** The repository is an unusually complete example of the host-enforcement discipline TeaPrompt's lessons describe in prose: every documented control except the failure taxonomy is code plus a named test, and the docs disclose their own reporting exceptions (a setup-failure zero kept in a paper aggregate that the runtime would now leave unscored; a versioned "correction" mechanism that supports exactly one task).
- **Reproduce: not undertaken.** Runs need a Linux host with Docker and KVM, gated benchmark assets, and model credentials. Nothing from the repository was executed; test counts and smoke results are author-claimed (`docs/RELEASE.md`) with CI read by a scout.
- **Adopt: two in-place template repairs, no surveyed text.** RS-1 (DAG quorum gate requires this run's sink) and RS-2 (fix-loop progress count excludes `state/`) are TeaPrompt defects in the source's C8 and C2 failure families; the fixes are TeaPrompt's own bytes, proven by rigs and guarded. No skill, lens, glossary, pack, or knowledge sentence was added.
- **Deploy: not applicable.** A benchmark harness, not a tool one runs on TeaPrompt work.
- The curriculum role, broad-then-deep exploration, wave memory barrier, and practice-lineage learning are a training-loop architecture; TeaPrompt ships no learning loop and never treats run state as project memory. They stay study material.

## Method

Coordinator reads (2026-09-16): repository and commit metadata via the GitHub API, `README.md`, `docs/ARCHITECTURE.md`, `docs/PAPER.md`, `docs/RELEASE.md`, `docs/OPERATIONS.md`, and the arXiv abstract; three coordinator spot-checks of scout-cited source lines (all held). Two read-only scouts ran in parallel on one concept list (C1–C10): a source-mechanism audit deciding the enforcement tier of each concept at the pinned commit, and a TeaPrompt coverage map locating the nearest installed sentence for each concept and answering four pointed questions about the pack templates. No Parallel Lens Review panel: no surveyed wording was proposed for adoption, and the two changes are template defects, the channel the 2026-09-14 second pass found most reliable (deterministic rigs, not lens reads). The packet-contract falsifier (`04-agent/workflow-recipes.md`: one review pass would reach the same decision) was judged to hold; the landing itself was reviewed as landed bytes by an independent pass before commit (XM-6).

Coordinator rigs: the two templates were extracted from the pack files by fence, run with stub agents in `/tmp`, re-extracted after the edit and re-run. Rig figures below are bound to the pre-edit bytes (`9a756e5`) and the landed bytes of this commit respectively.

**Scope / acceptance:** map all ten concepts; decide every candidate with evidence and a trigger; land only defects proven on TeaPrompt's own templates; keep both flow packs under the 20,000-character lint budget; guards fail on the previous bytes; run `make all` from the repository root.

## What the Artifact Is

Pinned identity (GitHub API, accessed 2026-09-16): `AetherLabsAI/RSIAgent`, public, Apache-2.0, Python, 192 stars / 14 forks at first fetch (198 / 15 by 01:59Z the same day), main at `dcd4e580c2f4bb65aa28bf4d5ecbf2ac8fe3bfa4` (2026-09-16T01:01:56Z, a README title/icon commit). Paper: arXiv 2609.15364, published 2026-09-14 (abstract fetched 2026-09-16); the repository ships an author-supplied 50-page PDF mirror dated 2026-09-15.

Three roles under a host harness: an actor that does the work and later distills its own verified experience; a verifier that judges candidate evidence in its own persistent context and returns pass, fail, or unverified; a curriculum that chooses the next practice or target attempt and may neither grade nor write the actor's memory. Three phases: parallel broad exploration with an ordered memory consolidation barrier; sequential target-conditioned practice; frozen-memory evaluation with the official grader sealed away from the agents. Reported benchmark movements (transcribed from the manuscript, per `docs/PAPER.md`, read 2026-09-16) are author-claimed and explicitly not a result-file audit: partial credit 71.97 → 78.98 and 83.75 → 84.82 on the two benchmarks, with retained baselines for tasks that had no new run.

## Concept Map

Tier is the source-audit finding at the pinned commit (`code+test` = host check plus a named test under `tests/`; `prose` = docs only). Coverage names the nearest installed TeaPrompt sentence.

| ID | Concept (clean-room) | Source tier | TeaPrompt coverage | Disposition |
| --- | --- | --- | --- | --- |
| C1 | Four-way authority split: worker, judge, task-selector that neither grades nor writes memory, host that commits memory only at valid boundaries and invokes the sealed grader | code+test (`core/self_evolving_loop.py`, `tests/test_self_evolving_loop.py`, `tests/test_curriculum_memory_access.py`) | `agent-governance-scaffold` proposer/broker/effector/accepter split; `04-agent/runtime-trust-boundary.md` | No change — the task-selector role is a learning-loop role (RS-6) |
| C2 | Judge isolation: inspects a rollback-protected snapshot with the worker's private artifacts mechanically masked; its own local mutations are reverted before the worker resumes; shared remote services are the stated limit | code+test (`core/verifier_runtime.py`, `env/qemu_rollback.py`, `tests/test_verifier_isolation.py:430,267`) | `governed-delivery` host-supplied sink isolation; loop pack Anatomy #5 host precondition | **Local instance found and fixed (RS-2)**: the loop's own `state/` residue counted as worker progress |
| C3 | Wave barrier: branches start from one snapshot, distill serially in authored order only after every branch has a valid verdict; an incomplete branch blocks the wave and its memory is never merged | code+test (`explore/phase1_wave.py` join, `tests/test_vm_lifecycle_and_wave_recovery.py`) | Generator pack fan-out: strict default, explicit `MIN_OK` quorum, lexical/`sorted()` merge order (template behavior) | No change (RS-6) |
| C4 | Real target first; pass and fail both feed learning; after practice a fresh attempt on the unchanged target is required; selector "readiness" is not a correctness verdict | code+test (`core/self_evolving_loop.py`, `tests/test_self_evolving_loop.py`) | Loop pack: one external verifier decides; critic `ACCEPT` advisory; `reflective-implement` "every edit after the last verification run reopens verification" | No change (RS-6, RS-10) |
| C5 | An infrastructure error is never a verdict; stalled and budget exits stay distinct from convergence; an unscored run is not a zero | code+test (`benchmarks/osworld/task.py` exit 75, `benchmarks/ale/report.py` explicit `missing`) | Loop pack exits 0/2/3/4; `reflective-handoff-retro` `OUTCOME_UNKNOWN`; GLOSSARY "unknown, never zero" | No change (RS-7) |
| C6 | Sealed evaluation: frozen memory, reset environment, grader runs after the agents finish, grader output cannot enter a later learning phase, grader files never enter prompts or memory (a host-side leakage scanner enforces it) | code+test (`benchmarks/osworld/task.py`, `tools/exam_fence.py`, `tests/test_exam_fence_observations.py`) | `governed-delivery` oracle split (authoritative oracles read-only in-run); `ROUTING_CONTRACT.md` R8 holdout-before-tune | No change — benchmark-integrity control, rejected as drafted (RS-4) |
| C7 | Provenance: config, task-release, and memory hashes plus terminal statuses recorded; corrections identified and reported apart from unmodified evaluation; README figures labelled manuscript-reported | code+test (`benchmarks/osworld/pipeline.py`, `benchmarks/osworld/evaluator_corrections.py` source-hash binding) | `reflective-research` "verified covers only what was actually checked"; packet contract "every figure bound to its measured revision" | No change (RS-8) |
| C8 | Operational hygiene: side-effect-free dry run; smoke proves mechanics not scores; a batch name is never reused (`run_osworld.py:113-114`); reports keep missing results explicit and reject duplicate scored attempts | code+test (`run_osworld.py`, `tools/smoke_osworld.py`, `benchmarks/ale/report.py`) | Both packs: stub dry run; bash fan-out clears stale branch outputs before its gate | **Local instance found and fixed (RS-1)**: the DAG quorum gate read a stale sink |
| C9 | Failure taxonomy: under-targeted exploration, incomplete verification, unreliable memory consolidation | prose (`docs/PAPER.md`, `README.md`) | `reflective-review` evidence rules; `reflective-handoff-retro` memory quality gate; `04-agent/artifact-promotion.md` §4 memory-write gate | No change (RS-11) |
| C10 | Task-selector memory view is read-only by default; its context persists within one target lineage | code+test (`benchmarks/osworld/phase2.py`, `tests/test_curriculum_memory_access.py`) | none — no learning-loop role exists | No change (RS-6) |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| RS-1 | DAG executor (`flow-control-generator`): in quorum mode the merged gate must require the sink node to be `done` in this run, not merely an existing `<sink>.out` | Adopted 2026-09-16 | Pre-edit rig (`9a756e5`): run 1 clean, then run 2 in the same `STATE` with the sink failing and `MIN_OK=3` exited 0 while `verify-merged.sh` printed run 1's output and the ledger read `assemble failed`; a fresh `STATE` exited 2 only because the check script rejects a missing file. Landed bytes: exit 2; clean rerun 0; blocked sink (`api` fails, `MIN_OK=2`) 2. Guard `_run_dag(..., stale_sink=True)` in `test_skill_verification_panel_record.py` fails on `9a756e5` (`assert 0 == 2`) | Retire only if the DAG template drops quorum mode; rejected smaller alternative: clearing `*.out` at start (more characters, and would not cover a sink that failed in a fresh directory when the check script accepts a missing path) |
| RS-2 | Verify-gated fix loop (`flow-loop-harness`): the git progress snapshot counts untracked files outside `$STATE`; Anatomy #4 says so | Adopted 2026-09-16 | Pre-edit rig (`9a756e5`): a no-op agent with the template default `STATE=./state` in an un-ignored worktree ran to the cap, exit 2, signatures `+u6` through `+u14` (two loop files per iteration); with `STATE` outside the tree or gitignored it exited 3 at iteration 1. Landed bytes: exit 3 at iteration 1 from the root and from a subdirectory; an agent that edits a tracked file each iteration still reaches the cap with three distinct signatures; a verifier that flips exits 0. Guard `test_fix_loop_no_progress_exit_survives_state_inside_worktree` fails on `9a756e5` (`sig: +u6`) | Retire only if the snapshot stops counting untracked files; rejected smaller alternative: `git ls-files --exclude=/<state>` (anchors at the repository root, so a loop run from a subdirectory kept the defect); a documented "gitignore `state/`" precondition was rejected because the template default itself disabled the exit |
| RS-3 | Loop pack sentence requiring the verifier to run on a workspace snapshot or revert its local writes (coverage-map candidate from C2) | Rejected 2026-09-16 | A shell template cannot snapshot a workspace; the sentence would restate Anatomy #5's host precondition. The only local instance of "harness residue read as progress" was the loop's own `state/`, fixed by RS-2 | Reopen if a TeaPrompt-run loop shows a verifier's own writes masking a stall after RS-2 |
| RS-4 | `governed-delivery` sentence hiding authoritative oracle content from the executor (coverage-map candidate from C6, the leakage fence) | Rejected 2026-09-16 | A benchmark-integrity control: delivery oracles are visible by design (CX-1 red-first tests; GA oracle split keeps them read-only, not hidden). The transferable part — a score that steers edits stops measuring — is installed as R8 holdout-before-tune | Reopen only for a delivery task whose acceptance oracle is a hidden evaluation set |
| RS-5 | Run-keyed `STATE` directories or refusing to reuse one (coverage-map candidate from C8, the source's new-batch-name rule) | Rejected 2026-09-16 | Both packs declare `state/` a host-honored resume convention (generator Never, loop Anatomy #3); refusing reuse breaks resume. The bash fan-out already clears stale branch outputs; the DAG needed a sink gate (RS-1), not a naming rule | Reopen if a resume-free topology is added to the generator pack |
| RS-6 | Task-selector role, broad-then-deep exploration, wave memory barrier, practice lineage (C1, C3, C4, C10) | No change 2026-09-16 | Training-loop mechanisms; TeaPrompt ships no learning loop, and run state is never project memory (loop pack Never; `04-agent/artifact-promotion.md` §4). Fan-in quorum-versus-strict and deterministic merge order already exist as template behavior | Reopen only if TeaPrompt's scope changes to shipping a learning loop |
| RS-7 | Infrastructure error is never a verdict; unscored is not zero (C5) | No change 2026-09-16 | Loop pack distinct exits; `reflective-handoff-retro` `OUTCOME_UNKNOWN`; GLOSSARY missing-data rule | None |
| RS-8 | Provenance and reporting discipline (C7): manuscript-reported versus audited; corrections reported apart | No change 2026-09-16 | `reflective-research` verified-versus-checked rule; packet contract landing-review bullet (2026-09-15) | None |
| RS-9 | Critic keeps its own prior verdicts across rounds (the source's persistent verifier context, `core/verifier.py:180`) for the writer-critic template | Deferred 2026-09-16 | The template's critic is stateless per round by design; only the reviser sees the critique. A stateless critic can re-accept an A-fixed-B-broken, B-fixed-A-broken cycle until the round cap absorbs it; no local run has shown this | Reopen on an observed oscillation across rounds in a TeaPrompt-run writer-critic loop; the fix would feed the critic the prior critique file, within the pack's size budget |
| RS-10 | Judge builds its requirement inventory from the authoritative instruction before reading the candidate (source verifier prompt rule) | No change 2026-09-16 | `reflective-review` Review Flow orders requirement identification (step 1) before claim extraction (step 2) | None |
| RS-11 | Failure taxonomy (C9) as a named triad | No change 2026-09-16 | Each leg is defended by an installed rule (see Concept Map); a heading would restate them | None |
| RS-12 | "Check published artifacts, not a live process"; "a missing candidate cannot be reconstructed by relabeling a result" (`docs/OPERATIONS.md`) | No change 2026-09-16 | Durable Lessons: runtime truth is not product acceptance; a stated decision is not an observable; packet contract landing-review bullet | None |

Deterministic guards: `plans/tests/test_rsiagent_survey_record.py` (identity, dispositions, clean-room boundary, index links, fix-loop dry run) and the extended DAG dry run in `plans/tests/test_skill_verification_panel_record.py`.

## Landed Repairs

### RS-1 — DAG quorum gate (`skills/flow-control-generator/SKILL.md`)

Previous line: `if ok < int(MIN_OK): sys.exit(2)  # explicit quorum`. Landed line: `if ok < int(MIN_OK) or status.get(order[-1]) != "done": sys.exit(2)  # quorum; sink from this run`. The strict path is untouched. Dependents already ran only when their deps were `done` this run, so the merged gate was the single place a stale file could be read. The exact pin on the quorum line in `test_skill_verification_panel_record.py` was re-seated on the unchanged strict line; the structural contract for this block is the dry run.

| Rig case (same `STATE` unless noted) | `9a756e5` | landed |
| --- | --- | --- |
| all nodes pass, strict | 0 | 0 |
| sink fails, `MIN_OK=3`, stale sink present | **0** (gate read run 1's file) | 2 |
| sink fails, `MIN_OK=3`, fresh `STATE` | 2 (check script rejects a missing file) | 2 |
| all pass, `MIN_OK=3` (fresh sink overwrites stale) | 0 | 0 |
| `api` fails, `MIN_OK=2` (sink blocked) | not run | 2 |

### RS-2 — Fix-loop progress count (`skills/flow-loop-harness/SKILL.md`)

Previous snapshot term: `git ls-files -o --exclude-standard | wc -l | tr -d ' '`. Landed: `git ls-files -o --exclude-standard | grep -vc "^${STATE#./}/" || true`. `git ls-files -o` prints paths relative to the working directory, so the filter is correct from the repository root and from a subdirectory for every relative `STATE` form; an absolute `STATE` outside the tree matches nothing and is unaffected. Anatomy #4 now reads "untracked-file count excluding `state/`, the loop's own files".

| Rig case | `9a756e5` | landed |
| --- | --- | --- |
| no-op agent, `STATE=./state` in an un-ignored worktree, from root | 2 after 5 iterations (`+u6` … `+u14`) | 3 at iteration 1 |
| same, run from a subdirectory with `STATE=state` | not run | 3 at iteration 1 |
| no-op agent, `STATE` outside the worktree | 3 at iteration 1 | not run |
| no-op agent, `state/` gitignored | 3 at iteration 1 | not run |
| agent appends to a tracked file each iteration, cap 3 | not run | 2 (three distinct signatures) |
| verifier flips to pass after one iteration | not run | 0 |

Sizes after landing (lint measure, characters): `flow-loop-harness` 19,983; `flow-control-generator` 19,979; both under 20,000.

## Shared Findings

1. **Doc-to-code fidelity is high and the tiering is honest.** Nine of ten concepts are host checks with named tests; the docs themselves label the README figures manuscript-transcribed, disclose the retained-baseline aggregation, and say smoke success proves mechanics, not scores.
2. **The judge's verdict channel refuses ambiguity.** Verdicts are one of three tokens on a standalone line (`core/verifier.py:545-546`); a pass accompanied by non-empty doubts is sent back as a contradiction (`core/verifier.py:290`). This is the same rule the writer-critic template enforces with an exact `ACCEPT` match and the 2026-09-14 rig proved for `ACCEPT`-plus-TODO.
3. **Persistent judge context is a data structure, not an instruction** (`core/verifier.py:180`, a list subclass carrying the conversation, probe telemetry, and an archived scratch area across executor reattachments). This is what RS-9 would approximate at prompt level.
4. **Surprises recorded by the source audit** (scout-read, coordinator not verified unless marked): the paper aggregate keeps a zero for one task's setup failure while the runtime now leaves such runs unscored (`docs/PAPER.md`, coordinator-read); the "evaluator correction" mechanism supports exactly one task and identifier and raises on any other; the curriculum memory-view ablation is reachable from an internal module but not the public protocol file; the release check skips the two evaluator tests unless an environment variable opts in.
5. **Two of the source's failure classes were TeaPrompt's failures.** Both packs' prose already stated the rule the templates broke (the fan-out comment "stale outputs from a prior run must not satisfy the gate"; Anatomy #4's "no observable change"); only execution found the gap — the 2026-09-05 lesson that a shipped template drifts from its contract prose, again.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Identity, license, stars/forks, main commit and date | Observed | GitHub API, accessed 2026-09-16 |
| Paper identity and publication date | Observed | arXiv abstract page, fetched 2026-09-16 |
| Role split, phases, sealed evaluation, reporting scope | Observed (docs) | `README.md`, `docs/ARCHITECTURE.md`, `docs/PAPER.md`, `docs/RELEASE.md`, `docs/OPERATIONS.md`, read 2026-09-16 |
| Enforcement tiers C1–C10 with file and test names | Scout-read; three coordinator spot-checks held (`run_osworld.py:113-114`, `tests/test_verifier_isolation.py:430`/`:267`, `core/verifier.py:180`/`:545`) | Source audit over the pinned commit; coordinator line numbers re-derived from the raw bytes after the landing review showed the URL reader's numbering drifts |
| 718 portable tests, smoke results, CI composition | Author-claimed / scout-read | `docs/RELEASE.md`; `.github/workflows/tests.yml` read by the scout only |
| Benchmark improvements | Author-claimed | Transcribed manuscript table; no result files audited by anyone in this survey |
| Pre-edit template defects (RS-1, RS-2) | Observed / executed | Coordinator rigs on bytes extracted from `9a756e5` |
| Repairs hold and real progress is still detected | Observed / executed | Rigs on re-extracted landed bytes; guards fail on `9a756e5`, pass on the landed tree |
| A stateless critic would re-accept an oscillation (RS-9) | `[INFERENCE]` | Template read; no local run observed |
| No installed surface carries the surveyed vocabulary | Observed | `test_survey_vocabulary_stays_out_of_installed_surfaces` |

## Evidence Actually Checked

- GitHub API: repository metadata and `commits/main` (`dcd4e580…`), 2026-09-16.
- Coordinator full reads: `README.md`, `docs/ARCHITECTURE.md`, `docs/PAPER.md`, `docs/RELEASE.md`, `docs/OPERATIONS.md`, arXiv abstract.
- Coordinator spot-checks (raw files at the pinned commit): `run_osworld.py`, `tests/test_verifier_isolation.py`, `core/verifier.py`.
- Scout source audit: `explore/phase1_wave.py`, `explore/commit.py`, `explore/charter.py`, `core/self_evolving_loop.py`, `core/verifier.py`, `core/verifier_runtime.py`, `env/qemu_rollback.py`, `benchmarks/osworld/{pipeline,phase1,phase2,task,evaluator_corrections}.py`, `benchmarks/ale/report.py`, `tools/{exam_fence,check_rsi_release,smoke_osworld}.py`, `config/` role profiles, `tests/` (governance-relevant files), `.github/workflows/tests.yml`. Skipped: ALE VM plumbing, guest transport, imagery, practice apps, the PDF.
- Scout coverage map: all thirteen `SKILL.md` files, `skills/examples/`, `04-agent/`, `PROJECT_KNOWLEDGE.md`, `GLOSSARY.md`, `plans/ROUTING_CONTRACT.md`, prior survey ledgers.
- Coordinator rigs: `/tmp/rig-d1` (six loop runs) and `/tmp/rig-d2` (eight DAG runs), templates extracted by fence before and after the edit.
- Not executed: any RSIAgent code, tests, or smoke; no clone.

## Falsifiability

- The "no sentence needed" mapping is wrong if an installed skill is later shown to lack a rule the Concept Map credits to it (the coverage rows cite file and line; re-grep them).
- RS-1 is wrong if a legitimate quorum topology needs the merged gate to run without a completed sink; the dry run would then need a new case, not a revert.
- RS-2 is wrong if a host's `git ls-files -o` prints root-relative paths from a subdirectory (the subdirectory rig case would then fail), or if a loop legitimately writes its own progress into `state/`.
- RS-9 stays deferred only while no writer-critic run oscillates; one observed oscillation reopens it.
- The tiering is wrong if the source's named tests do not exercise the mechanisms the audit attributes to them; three spot-checks held, the rest are scout-read.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Source pinned, license and paper identity recorded | done | this record, `test_rsiagent_survey_record.py` |
| Ten concepts mapped with tier and coverage | done | Concept Map |
| Twelve candidates decided with evidence and triggers | done | Candidate Adoption Ledger, dispositions guarded |
| RS-1 landed with dry-run case failing on `9a756e5` | done | `test_skill_verification_panel_record.py` |
| RS-2 landed with dry-run case failing on `9a756e5` | done | `test_rsiagent_survey_record.py` |
| Flow packs under the lint budget | done | 19,983 / 19,979 characters |
| Clean-room boundary on installed surfaces | done | `test_survey_vocabulary_stays_out_of_installed_surfaces` |
| Independent landing review (XM-6) before commit | done | `AGREE WITH CHANGES`: both template edits, both sizes, every rig cell on both revisions, both guard failures on `9a756e5`, all twelve dispositions and counts, and every TeaPrompt coverage citation reproduced; five source line citations were wrong (the URL reader's line numbering drifts from the raw file) and were re-derived from raw bytes; star/fork counts had moved within the day and are now time-bound |
| Decision Index, Case Comparison row, State Ledger row, `index.json` | done | `PROJECT_KNOWLEDGE.md`, `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |
