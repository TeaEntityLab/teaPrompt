# Flow-Pack Usage Log

> **Status: living evidence ledger (non-authoritative).** Manual invocation log
> for every registered domain pack (`DOMAIN_PACK_SKILLS`: ten since 2026-10-06;
> five since 2026-09-23 is the dated historical count, preserved below;
> scope widened 2026-09-14 so the `governed-delivery` recurrence checkpoint reads
> the same ledger), established 2026-07-11 per
> [necessity record N11](governance-necessity-panel-record-2026-07-11.md) and
> T3/F2 of the [whole-project plan](whole-project-plan-2026-07-11.md). TeaPrompt
> has no telemetry; this log aggregates host-supplied evidence feeding the 2026-10-11
> P6 merge re-litigation and pack demotion reviews. Owning records remain evidence
> sources even when a use was logged late. Append-only;
> absence of entries is recorded `unknown`-vs-zero honestly: an empty log means
> "no invocation was *recorded*", and the 2026-10-11 review must weigh whether
> unlogged use is plausible before treating it as zero.
> **Dated supersession 2026-10-09:** the prior "five since 2026-09-23" header is historical; the current count is ten from the live registry after the 2026-10-06 five-pack admission ([survey](managed-skills-learned-survey-2026-10-06.md), ticket [runtime-skills-task001-ticket-2026-10-06.md](runtime-skills-task001-ticket-2026-10-06.md)).

## Convention

One row per real invocation (not stub/rig runs, not tests of the templates
themselves):

| Date | Skill | Host / context | Task shape | Outcome + evidence pointer |
| --- | --- | --- | --- | --- |

- "Real invocation" = the skill's contract was used to generate its declared
  artifacts for an actual task (a script, governance contracts, or verification
  surface); generated scripts need not have run to completion.
- Rig verification runs during pack maintenance do not count; note them below
  the table only when they change a template.
- Anyone (human or agent) touching the packs appends here in the same change.
- Failure channel (added 2026-10-01; criterion corrected in the prep re-check):
  [MR-3 / Standing Non-Goals](../PROJECT_KNOWLEDGE.md#standing-non-goals)
  counts documented real-world host-agent executions of generated flow-pack
  scripts that fail due to deterministic script-structure defects that offline
  stub tests **cannot reproduce**. Log the host/script revision, failing command
  and output, expected result, and attempted stub reproductions with results.
  Stub-reproducible failures, or unknown reproducibility, do not establish a
  qualifying MR-3 case. At ≥3 documented qualifying failures, open re-litigation;
  this is not authorization to ship a runtime or change project direction.

## Entries

| Date | Skill | Host / context | Task shape | Outcome + evidence pointer |
| --- | --- | --- | --- | --- |
| — | — | — | — | Zero-state recorded 2026-07-11: no real invocation on record since pack adoption (2026-07-11). |
| — | `agent-governance-scaffold` | — | — | Zero-state recorded 2026-09-14: no real invocation on record since pack adoption (2026-07-17). |
| — | `governed-delivery` | — | — | Zero-state recorded 2026-09-14: no real invocation on record since pack adoption (2026-09-03); the 2026-10-11 checkpoint reads this row — absence stays `unknown`, and demotion is a policy consequence of missing evidence. |
| 2026-09-23 | `verification-map-generator` | omp task agents | Four-product verification-map generation (wsgiLite.js, fpGo, fpEs, fpRust) | Adopted same-day: pattern generated VERIFY.md + features/ + locked spec on four products; fresh-agent arms classified product regression, doc drift, spec-oracle error correctly; evidence in `plans/pstack-survey-2026-09-22.md`. |
| 2026-09-23 | `verification-map-generator` | teaPrompt self-application (dogfooding) | Verification map for this repo's own gate suite | Generated `VERIFY.md` + `features/` (4 areas: test suite, validators, route evals, registry cardinality) + `acceptance.yaml` (read-only by convention) at repo root; fresh-agent healthy sweep passed 4/4 areas and an unlabeled seeded `CORE_SKILLS` deletion was classified product regression, same-day; evidence in [self-governance-dogfood-2026-09-24.md](self-governance-dogfood-2026-09-24.md) Part A (classifications are model-judgment tier; the registry-shrink exit code is pytest-pinned). |
| 2026-07-17 | `agent-governance-scaffold` | lite-ad host (`.agent/` emit) | Governance-scaffold emit (four-power map, fail-closed pending/deny templates, constitutional paths) | **Correction appended 2026-10-01:** first solo invocation — refutes the 2026-09-14 zero-state row above, which is preserved as dated history. Falsifies the zero-use leg only; does not clear the 2026-10-11 recurrence/size checkpoint. Evidence: [field-use panel](agent-governance-scaffold-field-use-panel-2026-07-17.md) (FU7), [adoption record](agent-governance-scaffold-adoption-2026-07-17.md). |
| 2026-09-07 | `flow-control-generator` | omp / teaagent roadmap-rethink task (S1) | One-pass eval fan-out/fan-in and proposal synthesis | **Late correction 2026-10-01:** `.teaagent/flows/roadmap-rethink-evals/run-evals.sh`; skill read `1f861c8f`, successful write `cfc025f8`. Historical `3e3f3aa1` records five deterministic branches and stub synthesis, exit 0; not production-content acceptance. |
| 2026-09-07 | `governed-delivery` | omp / teaagent roadmap-rethink task (S1) | Delivery contracts for the roadmap/gate evaluation | **Late correction 2026-10-01:** `.teaagent/delivery/roadmap-rethink-2026-09-07/`; user-invoked skill event and populated writes including evidence ledger `4fc2d05d`, acceptance `217c30a2`, retro `13f953fa`. One artifact-group invocation; acceptance open, seals absent, refuters unknown. |
| 2026-09-21 | `agent-governance-scaffold` | omp / teaBrain learning/control governance task (S4) | Four-power authority map, contracts and run interface | **Late correction 2026-10-01, re-checked:** user requested project governance (`ffe26847`); the model selected the pack, successful skill read `c944b7c4`, then writes `b535b886` (authority map), `de3c68d3` (contracts), `a0e0d9f3` (worker contract), `d1cdc3ed` (run interface). One actual contract-generation invocation under §Convention; user naming the skill is not required. The survey's earlier INFERENCE attribution remains dated history, not enforcement proof. |
| 2026-09-23 | `governed-delivery` | omp / teaBrain G0 LLM-facade task (S4) | G0 delivery packet and handover | **Late correction 2026-10-01, re-checked:** user-invoked event `53ce0236`; successful creation edits after empty-file creation: `6409029c` (intent), `635de806` (task packet), `074841d2` (HANDOVER). Inner event timestamps precede the drills; outer timestamps are batch persistence. Current archive: `docs/governance/archived/g0-llm-facade/`; generation, not enforcement or accepted delivery. |
| 2026-09-23 | `flow-control-generator` | omp / teaBrain G0 LLM-facade task (S4; paired G0 use) | Seven-gate pipeline whose execution stage calls the repair loop | **Late correction 2026-10-01, re-checked:** successful installed-file skill read `3dd5d656` (S4:1860; 09:59:44.732Z), creation edit `89d37d33` (S4:1941; 10:12:45.719Z). One paired G0 task with the next row, not a solo invocation: archived run-note:13 explicitly describes pipeline→loop composition. All times UTC, from inner message timestamps. Drills and a later already-verified pipeline exit do not prove model repair or GDR completion. |
| 2026-09-23 | `flow-loop-harness` | omp / teaBrain G0 LLM-facade task (S4; paired G0 use) | Bounded verify-gated loop inside the pipeline execution stage | **Late correction 2026-10-01, re-checked:** successful installed-file skill read `e7ebaff0` (S4:1861; 09:59:44.800Z), creation edit `4696b3d9` (S4:1940; 10:12:38.330Z). Same paired G0 task, not a second task or solo invocation. Archive contains stub drills; later S5 reaches missing `agent-cli` and then an already-verified branch, not an evidenced model-worker repair. |
| 2026-09-24 | `verification-map-generator` | omp / teaagent governed verification-map task (S2) | Product verification control doc, feature map and acceptance spec | **Late correction 2026-10-01:** explicit user-invoked skill event; successful writes `c9257a91` (VERIFY.md), `b2d98727` (feature index), `48099a2d` (acceptance). One map-generation invocation, not one per feature, worker or seeded-fault arm. |
| 2026-09-24 | `flow-control-generator` | omp / teaagent governed verification-map task (S2) | Fresh-agent read-only verification sweep | **Late correction 2026-10-01:** `verify/sweep.sh`; successful write `62ff67be`. Historical Claude receipt `58f46247` records three PASS and two DOC_DRIFT at HEAD `a193aa1b`; handover records exit 2. Named real host-script run, not a whole delivery/refuter campaign. |
| 2026-09-24 | `flow-loop-harness` | omp / teaagent governed verification-map task (S2) | Event-driven feature-map freshness repair | **Late correction 2026-10-01:** `verify/refresh.sh`; successful write `28895a4d`. Historical Claude receipt `003169e6` records exit 0, iter 1 VERIFIED on a stale-seeded clone; only feature source_commit changed. Not oracle sealing or signed acceptance. |
| 2026-09-24 | `governed-delivery` | omp / teaagent governed verification-map task (S2) | GD objects in joint GD/AGS contracts | **Late correction 2026-10-01:** skill read and successful write `f4a7fc46` (`verify/governance/contracts.yaml`), with HANDOVER attribution. One GD contract-generation invocation; unsigned intent, no seal, acceptance open; co-generated with AGS. |
| 2026-09-24 | `agent-governance-scaffold` | omp / teaagent governed verification-map task (S2) | AGS objects and run-interface binding in joint GD/AGS contracts | **Late correction 2026-10-01:** skill read `39fb8294`, joint contract write `f4a7fc46` and `verify/run-verifier.sh` / HANDOVER attribution. One AGS invocation in the same composite task; no broker/policy-engine enforcement inferred. |
| 2026-09-27 | `agent-governance-scaffold` | omp / metaCognitionAndSelfStudyByStories task (S3) | Learning-workflow governance artifacts | **Late correction 2026-10-01:** user-invoked skill event; successful writes `3ac118eb` (`.agent/run-interface.yaml`) and `c0ff0a8b` (`.agent/handover.md`), with capability/policy contracts. Static generation, not an enforcement receipt. |
| 2026-09-27 | `flow-control-generator` | omp / metaCognitionAndSelfStudyByStories task (S3) | Sequential draft-production queue | **Late correction 2026-10-01:** skill read `95983354`, successful write `7d68c250` (`loops/produce-batch.sh`), with matching header and RUN-NOTE. Draft-complete only; not accepted-complete or publish authorization. |
| 2026-09-27 | `flow-loop-harness` | omp / metaCognitionAndSelfStudyByStories task (S3) | Separate bounded supervised repair loop | **Late correction 2026-10-01:** skill read `d51e2324`, successful write `4c2aedb0` (`loops/repair-batch.sh`), with verifier hook and RUN-NOTE. A separate loop responsibility, not a nested loop inside draft production. |
| 2026-09-27 | `verification-map-generator` | omp / metaCognitionAndSelfStudyByStories task (S3) | Learning-workflow verification map and locked acceptance file | **Late correction 2026-10-01:** skill read `671e8bb1`; successful writes `523914cf` (VERIFY.md), `98b0c4f4` (feature map), `b1531c5c` (acceptance.yaml). Generation confirmed; the earlier malformed checker run is historical harness-failure evidence, not a current map verdict. |

| 2026-10-06 | `headless-agent-cli-contract` | teaPrompt runtime-skills dry run | Per-provider headless invocation recipes for ollama/devin/cursor-agent/agy (transport, permission flags, strip lists, BLOCKED policy) | Adopted same-day as sixth domain pack: contract emitted all four recipes from TASK-004 receipts; agy correctly BLOCKED on provider policy denial; evidence in `plans/runtime-skills-task001-ticket-2026-10-06.md` and `local://runtime-skill-planning-evidence-2026-10-06.json`. |

| 2026-10-06 | `arm-blinded-eval-harness` | teaPrompt runtime-skills dry run | Paired-arm evaluation scaffold (blinded extraction, sealed map, leak assertion) | Adopted same-day: mechanics smoked in /tmp/proposal-smoke (label-stripped extraction, zero arm-token leaks); by-construction guarantees only, zero observed blinded production runs — disclosed. |
| 2026-10-06 | `acceptance-join-validator` | teaPrompt runtime-skills dry run | REQ/AC→check join lint (dangling FAIL, orphan info, unrunnable FAIL) | Adopted same-day: mechanics smoked on synthetic repo (all three verdict classes fired); TeaPrompt self-run vacuous (zero REQ/AC ids) — disclosed. |
| 2026-10-06 | `golden-benchmark-runner` | teaPrompt runtime-skills dry run | Baseline-vs-skill paired runner over benchmark_tasks corpus | Adopted same-day: cat-stub smoke proved arm alternation + ledger schema; comparative signal requires real model arms (manual-execution tier) — disclosed. |
| 2026-10-06 | `router-trace-linter` | teaPrompt runtime-skills dry run | Router Output Contract lint (fields, confidence, R5 rationale, R4/R7 Human Review) | Adopted same-day: mechanics smoked (pass/downgrade-flag/missing-confidence fixtures all correct); declaration-completeness only, cannot judge deferral merit — disclosed. |

## Template maintenance (not invocations)

- 2026-09-05 — skill-verification pass changed templates in both flow packs
  (`flow-control-generator` D1–D7: quorum counting, merged-result gates, plan
  parsing, worker-id sanitizing, upstream-dependency consumption; `flow-loop-harness`
  FLH-1–FLH-10: progress detection, writer-critic sole-ACCEPT verdict and
  deterministic floor, backlog preflights) — rig-tier stub runs only
  ([record](skill-verification-panel-2026-09-05.md)). Recorded 2026-09-14; the
  convention's same-change note was missed at the time.
- 2026-10-05 — user-directed runtime-aware maintenance of both flow packs,
  `governed-delivery` and `agent-governance-scaffold`: selected preflight
  dispatch/release gates, a finite evidence-record checker and matching
  role/binding/lifecycle contracts. [Implementation and experiment
  record](runtime-skills-experiments-2026-10-05.md). Offline subprocess,
  real-OS role-denial, local CLI and bounded synthetic model arms are
  maintenance evidence, not new §Entries invocations, recurrence proof,
  complete GDR refuter results or qualifying MR-3 cases. Original harness
  failures remain preserved. The final 38-arm treatment, 17 original checker
  cases, 16 checker-review cases and 15 corrected flow-review cases matched
  expected outcomes; the configured real-model CLI returned a usage-credit
  prerequisite, not a repair. Flow source sizes are 27,731
  (`flow-control-generator`) and 24,566 (`flow-loop-harness`) characters at the
  record's source digests, both above the nonblocking 20k warning threshold.
  These measurements do not clear the checkpoint; final gate observations
  are recorded only after execution.
- 2026-10-07 — delayed-advisory correction in `validate_skill_examples.py`:
  removed the stale five-pack comment and pointed to the executable cardinality
  pin below it. The registry and guard already require ten domain packs;
  behavior, membership, and acceptance pins are unchanged. Maintenance only,
  not a domain-pack invocation or recurrence claim.
- 2026-10-07 — user-directed RV repair of `flow-control-generator`,
  `flow-loop-harness`, `arm-blinded-eval-harness`, and `router-trace-linter`:
  canonical cap guards before arithmetic/dispatch, queue-read error handling,
  worker exit classification, private scoring order, blinded-only scorer data,
  runnable CONFIG, and router review/confidence normalization. RV-05's locked
  oracle migration was separately approved; registry membership remains
  9 core + 10 packs. Emitted-script smoke matched 89 flow, 16 router, and
  16 blinded scenarios; 163 focused regressions passed.
  [Repair evidence and limits](recent-changes-review-handoff-2026-10-07.md#repair-turn-closure-2026-10-07).
  Template maintenance only, not a §Entries invocation, model-efficacy result,
  recurrence claim, or checkpoint decision.
- 2026-10-08 — user-directed latest-survey refresh of
  `arm-blinded-eval-harness` and `golden-benchmark-runner`: malformed-config,
  candidate-path and hold guards, retained scorer launch/timeout evidence,
  final-state hash naming, full captured-output auditability, timestamp-only
  determinism normalization, and predeclared treatment construction.
  Standalone consumer smoke matched 15/15 synthetic checks, including the
  published argv example and rendered documentation; no provider invoked.
  [Rulings and limits](cross-survey-rethink-2026-10-07.md#latest-survey-refresh-2026-10-08).
  Template maintenance only: not an Entries invocation, recurrence evidence,
  model-efficacy result, new admission, or 2026-10-11 checkpoint decision.

## Pre-checkpoint prep scans

- 2026-10-01 (prep, not the checkpoint verdict — the 2026-10-11 run re-verifies):
  check 8 scan found no host-supplied `governed-delivery` invocation
  (`git log` on pack + plan-doc grep; recurrence stays `unknown`); check 9
  shared-block read shows `artifact-complete`/`enforcement-proven`,
  constitutional-path and host-precondition wording still coherent across
  `governed-delivery` and `agent-governance-scaffold` (no divergence seen);
  F4 watch rows 1–6 checked via docs/search — none fired (Codex Record & Replay
  and Antigravity↔Gemini rows stay `unknown`); flow-pack chars 19,890/19,985;
  AGS 27,126.

### Verification correction (2026-10-01)

**Installation-command smoke:** extracted the current Antigravity Markdown
blocks and EN helper definitions, then ran `/bin/bash -s` in isolated temporary
workspaces/HOMEs (Bash 3.2.57). All nine cases passed: EN copy/symlink for
workspace, CLI global and desktop/IDE global, plus the three zh-TW copy cases.
Every destination contained exactly the nine core skills with matching source
bytes; optional packs were absent. Temporary directories were removed. This
exercises the instructions, not live host skill discovery.

Supersedes the earlier prep entry's blanket "none fired" and its undifferentiated
shared-block claim; the entry remains above as dated history. This is preparation,
not the 2026-10-11 checkpoint outcome. Host logs and private session histories
were not supplied: the earlier git/plan-doc scan cannot establish global absence,
zero recurrence, or independent `governed-delivery` use.

**T2 / check 3 (dated 2026-10-01; five-pack historical receipt, preserved):** an independent AST-registry/first-symbol smoke found the same
five `DOMAIN_PACK_SKILLS`, in registry order, followed by `reflective-dispatch`,
in both appendices (six bullets each; exit 0). The most recent appendix edit is
`5087ffe` (2026-09-29), adding the Software Factory / AI-native SDLC cue in both
languages; this is the current stability baseline, not stability since July.
Re-verify at the 2026-10-11 checkpoint against the live ten-pack registry; no new adoption or localization scope.

**GD↔AGS / check 9:** semantic comparison, not identical block/schema text:

| Shared obligation | `governed-delivery` surface | `agent-governance-scaffold` surface | Finding |
| --- | --- | --- | --- |
| Host enforcement is a precondition | Output/Never; Host Preconditions lists sealing, isolation, budgets, storage, human channel | Output/Never names broker, verifier, policy, approval, budget and canary enforcers | Compatible boundary; inventories differ by task. No observed host enforcement. |
| Artifact presence is not enforcement | Run-note `status`; Verification requires observed evidence for `enforcement-proven` | HANDOVER Governance status; Verification requires observed rejection/receipt/budget/mutation/canary evidence | Same distinction, different output syntax. |
| Workers cannot change control paths | Never: oracle manifest, verification plan, acceptance record and envelope; different owner, out-of-band change | Never and Constitutional paths/activation: worker exclusions, host owner, separate activation epoch | Same control-plane ownership obligation; AGS specifies additional machinery. |

No contradiction found in these three shared obligations. Whether GD ran
independently of AGS, or either host actually enforced the contracts, remains
`unknown`; neither redundancy-in-use nor consolidation is decided here.

**F4 / check 5 — primary sources read on 2026-10-01:**

| Watch | Source finding | Disposition / named follow-up |
| --- | --- | --- |
| `/goal` deterministic/tool-running evaluator | [Goal docs](https://code.claude.com/docs/en/goal) still say a model judges surfaced output and does not run commands/read files independently | Unchanged on the watched property; source text, not a live host test. |
| Stop-hook packaged loop hygiene | [Hooks guide](https://code.claude.com/docs/en/hooks-guide#stop-hook-hits-the-block-cap) documents an eight-consecutive-block cap without progress, with an override | Partial hygiene delta; the old current-tense "no caps" claim is unsafe. [Fresh source-only F1 table](flow-pack-demotion-evaluation-2026-07-11.md#source-only-f1-re-check-2026-10-01) covers all four current templates; full packaged enforcement is not established. |
| Codex Record & Replay | [Official guide](https://learn.chatgpt.com/docs/extend/record-and-replay.md) describes macOS demonstration→skill with Computer Use enabled | Feature confirmed; already present in the July survey. Maturation delta and actual local replay remain `unknown`. Reference for [workflow acquisition](../04-agent/workflow-acquisition.md), not new promotion. |
| Antigravity replaces consumer Gemini CLI | [Gemini banner](https://geminicli.com/) and [Google announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) confirm the June 18 consumer transition; enterprise/paid API access remains supported | Fired; S4 host-coverage check found CLI/IDE global-path drift in [skills docs](https://antigravity.google/docs/skills). EN/zh-TW install guides now distinguish CLI, desktop/IDE and legacy IDE paths. No live discovery claim. |
| AgentKit visual-builder wind-down | [Agent Builder guide](https://developers.openai.com/api/docs/guides/agent-builder) and [deprecations](https://developers.openai.com/api/docs/deprecations#2026-06-03-agent-builder) confirm announcement 2026-06-03 and scheduled shutdown 2026-11-30; ChatKit remains available | Confirmed only for Agent Builder; dated follow-ups in both July survey records supersede that narrow unknown. Whole-AgentKit retirement or an SDK-only replacement is not established. |
| Agent Skills frontmatter / `allowed-tools` | [Specification](https://agentskills.io/specification) still lists the same six fields as `validate_links.py`; `allowed-tools` remains experimental | No watched table/field change established; no migration or S1 re-run triggered. **Existing validation gaps:** the spec requires string-to-string metadata and 1–500 characters for optional `compatibility`; current frontmatter has unquoted YAML booleans, and the validator checks neither constraint. Table parity and a green local gate are not full conformance or a new reference-validator result. |

These checks cover the named documentation surfaces, not every ecosystem package
or a deployed host. Current `wc -m` measurements: generator 19,890; loop 19,985;
AGS 27,126 (the existing warning). The MR-3 observation channel now matches
"cannot reproduce"; its threshold, owner-sentence authority and promotion gates
are unchanged. Final repository checks use `make all`; the date-gated checkpoint
and its outcome record remain unperformed.

### Continuation evidence (2026-10-01)

**Recorded uses / checks 1, 2 and 8:** a registry-aware Python `-c` inventory
counted only real dated rows in §Entries; independent grep
`^\| 2026-[0-9]{2}-[0-9]{2} \|` over that table returned the same three rows.
In registry order, recorded-row counts are:

| Pack | Recorded real invocation rows |
| --- | --- |
| `flow-control-generator` | 0 |
| `flow-loop-harness` | 0 |
| `agent-governance-scaffold` | 1 |
| `governed-delivery` | 0 |
| `verification-map-generator` | 2 |
| `headless-agent-cli-contract` | 0 |
| `arm-blinded-eval-harness` | 0 |
| `acceptance-join-validator` | 0 |
| `golden-benchmark-runner` | 0 |
| `router-trace-linter` | 0 |

**Dated supersession (2026-10-01, primary-receipt re-check):** this
0/0/1/0/2 table is the earlier repository-record-only inventory, not the
current §Entries count. The source-linked corrections below supersede it
with 4/3/4/3/4 (18 rows). Pack-row counts are not P6 solo-use counts:
teaBrain's two flow rows are one paired G0 task and contribute zero solo
invocations to either pack.

The lite-ad FU7 emit and the two verification-map rows are known-present controls.
The first verification-map row aggregates four products: these are row counts,
not product counts, worker turns, verifier arms or completed runtime executions.
Repository-record searches found no additional documented flow-pack invocation
or qualifying MR-3 failure. Maintenance rigs are stub-reproducible, not real
host executions that stubs cannot reproduce; teaBrain generation by the pack is
still inference. Private sessions and external host logs are unavailable:
unlogged use and independent GD use remain `unknown`, not observed zero.

**Dated supersession (2026-10-01, primary-receipt re-check):** the preceding
inference-only teaBrain attribution and blanket session-unavailability
statement describe the earlier search scope. S4 confirms model-selected AGS
generation and successful installed-file loads plus paired flow generation;
S1–S5 are now accessible primary sources. Only supplied IDs `01a0cbbd`,
`01a0d1d3` and `01a0e7b9` remain unlinked in the inspected local store.
Unlogged external use remains unknown; accessible generation is not host
enforcement, a P6 solo-use finding or qualifying MR-3 failure evidence.

**Decision Index / check 7:** regex inventory and an independent literal
dated-line/date-filter scan agree on 78 entries since 2026-07-11, including 41
after 2026-09-14. Eight missing owner-pointer groups are now paired in the
[roadmap](whole-project-roadmap-2026-07-11.md#still-trigger-gated) and
[spec coverage](dormant-work-specs-2026-07-11.md#current-queue-coverage-2026-10-01):
SFR-4, MR-5, AEAT-4, TB-1, XM-12, RS-9, XM-8 and H1–H8/H12.
TB-1 remains No change, not a newly deferred adoption; the H rows keep separate
conditions and later WR repairs do not close the cluster wholesale. The
next-checkpoint falsifier has not become an elapsed deadline. No adoption,
scheduling, pack expansion, tuning or upstream-runtime transfer is authorized.

**G9 / AS9 / check 11:** `misroute|discoverability` grep across `plans/` and
`review/`, plus the retained repository-record scout search, did not establish
a governance-vocabulary fire event. The same search finds actual non-G9
misroute controls: R13's four pre-tune review-led failures in
[QUALITY_GATES_SUMMARY](QUALITY_GATES_SUMMARY.md) and July P1's four in the
[governance rethink record](governance-rules-rethink-review-2026-07-11.md).
The [field-use G9 row](agent-governance-scaffold-field-use-panel-2026-07-17.md)
records no local misroute from that emit; low-confidence dispatch is not pack
leakage. This is no recorded event in the searched population, not global absence.
The owning [G9](agent-governance-scaffold-adoption-2026-07-17.md) /
[AS9](all-skills-panel-record-2026-07-18.md) conditions and the runbook's
2026-10-11 proceed/hold/close duty remain unchanged; ≥3 fresh holdout groups and
R8 pre-tune observation still precede any tune. No checkpoint verdict is taken.

### G9 measurement provenance correction (2026-10-01)

The earlier `misroute|discoverability` search was incident discovery, not a
governance-vocabulary pre-tune measurement. Direct inspection separates these
populations:

| Source | Vocabulary / measured surface | What it establishes |
| --- | --- | --- |
| [G9](agent-governance-scaffold-adoption-2026-07-17.md#candidate-adoption-ledger) / [AS9](all-skills-panel-record-2026-07-18.md#candidate-adoption-ledger) | govern / gate / approval / constrain / make-safe against core workflows and the host-invoked pack | G9 explicitly records no pre-tune observation; AS9 defers under G9. Low-confidence dispatch probes are not a measured leakage event. |
| [GW-1 / GD-19](governance-workflow-self-control-adoption-2026-09-14.md) | deliver / autonomous / unattended, approved-delivery-plan context and R11 traps | Delivery-vocabulary measurements and actual misroutes, not the G9 vocabulary baseline. |
| [R13](QUALITY_GATES_SUMMARY.md#holdout-tracking) | Review-led roadmap / PRD / implementation-plan / release-plan inspection | Four of 24 new-group phrases misrouted pre-tune; a known-present incident control, not a G9 vocabulary measurement. |

These later routing measurements do not fill G9's named baseline gap. Additional
host-session measurements remain `unknown`; the source check proves neither a
G9 fire event nor global absence. It also makes no ruling that an earlier tune
bypassed R8. The 2026-10-11 proceed/hold/close duty, ≥3 fresh holdout groups and
R8 pre-tune observation remain unchanged. No tuning or holdout adoption here.

### Primary host-generation correction (2026-10-01)

**Refreshed recorded-row inventory:** the live-registry AST/datetime-row
driver and independent `^\| 2026-[0-9]{2}-[0-9]{2} \|` grep of §Entries
agree on 18 real invocation rows, with no duplicate task/pack identities:

| Pack (live registry order) | Recorded real invocation rows |
| --- | --- |
| `flow-control-generator` | 4 |
| `flow-loop-harness` | 3 |
| `agent-governance-scaffold` | 4 |
| `governed-delivery` | 3 |
| `verification-map-generator` | 4 |
| `headless-agent-cli-contract` | 0 |
| `arm-blinded-eval-harness` | 0 |
| `acceptance-join-validator` | 0 |
| `golden-benchmark-runner` | 0 |
| `router-trace-linter` | 0 |

The three dated zero-state rows remain. Controls include the previously
recorded lite-ad/verification-map rows and primary successful generation
receipts below. These are recorded task/artifact-group counts, not global
use totals, successful host-run counts or recurrence-policy decisions.


The late §Entries rows supersede the earlier prep's 0/0/1/0/2 inventory and
inference-only teaBrain classification; both remain historical observations.
Count one actual task/artifact group per pack, not each file, edit, retry,
worker, stub branch or runtime run. Shared GD/AGS generation is one row for
each used contract; later maintenance writes do not add invocations.
Successful generation does not certify artifact completeness, methodology
efficacy, host enforcement or product acceptance.

**Primary session locator key:** receipt IDs in the rows above refer to JSON
events in the following local source files under `~/.omp/agent/sessions/`.
Message-event dates use inner `message.timestamp`, not batched outer JSONL
timestamps; custom skill-prompt events use their own event timestamp.
Neither session-start filenames nor inferred UUID dates establish invocation dates.

| Key | Source directory | JSONL file |
| --- | --- | --- |
| S1 | `-dev-teaagent/` | `2026-08-31T04-20-00-049Z_01a0560b-a9b1-756b-b324-87b879d03601.jsonl` |
| S2 | `-dev-teaagent/` | `2026-09-24T08-47-27-232Z_01a0d299-2600-71ab-9a65-cb3f9cb79420.jsonl` |
| S3 | `-dev-metaCognitionAndSelfStudyByStories/` | `2026-09-27T00-22-26-477Z_01a0e03d-dfad-730c-a1ce-8ab919597605.jsonl` |
| S4 | `-dev-teaBrain/` | `2026-09-21T07-07-48-810Z_01a0c2ca-d8ca-7669-839a-56354d8b265c.jsonl` |
| S5 | `-dev-teaBrain/` | `2026-09-23T14-32-13-403Z_01a0ceae-6f5b-7441-9282-1882389ca674.jsonl` |

**Full-source provenance re-check (2026-10-01):** streaming JSON-event
decoding reached EOF for S4 (13,085,727 bytes / 3,350 lines) and S5
(42,157,389 bytes / 8,537 lines), with zero invalid JSON rows. It inspected
successful `read` requests/results for both `skill://` and installed
`SKILL.md` paths, `custom_message` skill-prompt events, and creation results.
An independent full-byte literal-field scan found S4 flow-path read requests
at 1681/1682 and 1685/1686. Positive controls include AGS URI read
`c944b7c4` and GD skill-prompt `53ce0236`. A capped grep's missing match is
not absence evidence; the prior header-only attribution is superseded.

**Live-source qualification (2026-10-02):** the byte/line fingerprints above
are the dated 2026-10-01 scan, not a claim about S5's current EOF. S5 is a
growing session source; later append events do not invalidate that historical
scan or prove a changed invocation count. Re-scan the complete source and
record the new bound before relying on it at the checkpoint. This note does
not assert a new EOF scan or advance the 2026-10-11 verdict.

The rows cite the earliest successful load pair, `3dd5d656` / `e7ebaff0`,
as load-of-record before artifact creation. S4 also contains a second
successful pair: `1e35fe23` (generator, :1863, 10:00:21.062Z) and
`086cbb7e` (loop, :1864, 10:00:21.064Z). These are additional reads of
the same packs, not another task or artifact-group invocation; their
retry/reload motive is not established by the receipts.

S4:1894–1916 records failed edits on missing paths, empty-file creation, then
successful population edits. Intent `6409029c` has inner timestamp
`1790158256340` = 10:10:56.340Z; loop and pipeline creation follow at
10:12:38.330Z / 10:12:45.719Z, before the 10:17Z drills. Outer
10:20:58.8xxZ values are batch-persist times, not creation chronology.
`git rev-list -n 1 --before=2026-09-23T10:10:56Z main` selects TeaPrompt
`c1cdf1404d50df16e17d7a9987a819e9ff2ecc4c` (commit time 04:13:29Z).
At that pin the generator Script Contract:77 requires four provenance
fields; its DAG header:269 uses `dry-run-first`, while the bash pipeline
and fix-loop templates have no literal generated-by header. Today's
`pipeline|fix` / `dry-run-required` literals cannot disprove September use.
The recovered successful loads plus creation receipts, not header
self-attribution alone, support the two counted flow rows.

**Evidence limits / checks 1, 2 and 8:** generator and loop artifact generation
is confirmed for teaagent, the learning repository and teaBrain. Per-pack
row counts do not establish solo use. teaBrain's archived run-note:13
explicitly describes the loop as the pipeline execution stage, confirmed
by `pipeline.sh:66`: one paired G0 use, with zero solo contributions from
this case to either pack. It does not clear P6's zero-solo condition.
Paired use is relevant to the preserved Minimality merge dissent, not
proof that merging is correct; the differing review boundaries remain
the counterargument. No early P6, consolidation or demotion decision.
September 7's GD artifact group contains only GD objects; that does not
disprove AGS use elsewhere in that task/session. September 24's GD/AGS
emit is explicitly joint. The inspected September 27 GD skill read alone
does not establish a GD invocation. Further contextual reads or maintenance
writes do not automatically establish another artifact-group invocation.

teaBrain's original AGS emit and G0 delivery generation now have primary
receipts. The [teaBrain survey](teabrain-concepts-experiments-survey-2026-09-21.md)
keeps its earlier attribution/benchmark evidence tier; this correction does
not retroactively convert its INFERENCE row into enforcement evidence.

**teaBrain execution / bypass re-check (2026-10-01):** archive sources below
are under `~/dev/teaBrain/docs/governance/archived/g0-llm-facade/`.
They establish executed script drills, not a real model-worker repair:

| Source | Observed result | Boundary |
| --- | --- | --- |
| `run-note.md:13,20,23`; `evidence/pipeline-unsigned.txt:1–9` | Explicit pipeline→loop composition; STATE=/tmp/g0-state. Unsigned real packet exits 2 before the loop; sentinel absent. | Missing default state directory is not nonexecution or zero-use evidence. |
| `evidence/pipeline-acceptance-blocked.txt:1–15` | Signed fixture logs `loop_ran:yes`; green stub execution/verifier still exits 2 at open acceptance. | Fixture drill, not model execution or signed product acceptance. |
| `evidence/loop-dry.txt:1–44`; `evidence/loop-exit2.txt:1–10` | Already-green 0, missing verifier 4, no-progress 3, repeated signature 3. Cap drill first exits 3, then fresh untracked filenames reach cap exit 2. | The count-based snapshot misses rewrites of an existing untracked file; the stub reproduced this deviation. Never re-label the first cap result as 2. |
| `evidence/worker-no-cli.txt:1–2` | Worker interface exits 2 without `agent-cli`. | Preflight stop, not a successful model-worker call. |

The archive's `run-note.md:11,87` facade-absence/unimplemented statements
are pre-implementation history, not current product status. In S4,
direct host edit receipts `17884817` / `c13f723b` populate facade.py /
test_g0_facade.py at 10:53:31Z, outside the generated loop. `2650c8c8`
shows verifier exit 0; `0c739186` shows the facade tests' 9 passes.
`cd99961d` still logs pipeline intent FAIL / exit 2. S4 `132.bash.log:98–112`
records that split; `159.bash-original.log:21–29` records commit `1923042`,
"Add the G0 chat facade without releasing the packet." Later `8f275194`
shows HEAD `5bf32e7` (G1–G5 landed) while pipeline intent still exits 2.
This is observed implementation bypass of the generated pipeline, not
pipeline intent-gate failure or evidence that its loop wrote the product.

S5 provides later real repository pipeline execution, so "all runs were
stub drills" would also be wrong. On 2026-09-24 (UTC), `e06dd666` logs
spec FAIL with a misleading `EXIT: 0` from trailing `tail`; `c39f6f54`
uses PIPESTATUS and records missing `agent-cli` / pipeline exit 3.
After owner signature/acceptance edits and owner-authorized oracle re-pin,
`28c1a604` records pipeline exit 0 at 00:15:51Z through `already verified`,
without a model call. The archived contract-set drills and these later
preflight/already-verified runs establish no real agent repair execution.
`features/facade.md:21` records signed acceptance at `714d9b1`, explicitly
qualified by F20 in `docs/reviews/2026-09-24-intents-tests-review.md:75,141`:
hollow per-gate retro, unreleased fields and unproven host sealing.
Do not erase that dated owner acceptance or promote it to whole-GDR proof.
Seven logged gate stages completed; that is not evidence of seven
independently enforced gates.

**GD-16 host-run evidence:** named historical teaagent sweep/refresh runs,
teaBrain archived fixture drills and later repository pipeline runs are
different evidence tiers. None establishes a first named harness run of
the whole current GDR contract set. teaBrain's out-of-pipeline product
landing further limits utility/enforcement attribution.
The owning [GD-16](governed-delivery-adoption-2026-09-03.md#candidate-adoption-ledger)
condition remains unchanged:

| Refuter | Accessible evidence | Full current-contract result |
| --- | --- | --- |
| GDR-1 | teaagent mutated acceptance and weakened a drive block; exit 1 detected it after the write. teaBrain F20 records an owner-authorized `g0_oracle.py` edit despite its worker-must-not-edit header. | Detection, not sealed rejection; the authorized oracle write shows host sealing was unenforced, not an unauthorized adversarial attempt. PASS not established. |
| GDR-2 | No tool-result-instruction-to-sink run receipt established. | Unknown. |
| GDR-3 | Stub no-progress exits exist; no repeated oracle/error-class/surface signature test across a correction was established. | Narrow exit evidence; canonical result unknown. |
| GDR-4 | HANDOVER says construction; RESUMED ledger code exists, but no transcript-loss/packet-rebuild run receipt was established. | Construction only; host-run result unknown. |
| GDR-5 | Malformed/non-PASS sweep outputs are rejected and refresh has a deterministic floor; no complete delivery-gate self-report-only release attempt was established. | Narrow rejection evidence; canonical result unknown. |
| GDR-6 | Covered-source mutation yields feature STALE; no mid-run spec-version bump, all-keyed-artifact propagation and replanning run was established. | Feature staleness, not the full current criterion. |

teaBrain's archived G0 `refuters.yaml` lists all six as unknown. Preserve the
historical September 7 wording rather than treating it as a test of the
later widened GDR-6 criterion. Source-unavailable reported sessions
`01a0cbbd`, `01a0d1d3` and `01a0e7b9` stay unlinked; campaign/coordinator
artifacts attributed to them are not counted, dated or declared nonexistent.

**MR-3 / utility boundary:** zero qualifying cases are established in this
inspected set, not a global claim of zero failures. teaBrain archive runs
use stubs/fixtures, including the reproduced cap-drill 3-vs-2 deviation.
The later missing-agent/pin/already-verified paths do not establish a
real-world model repair failure offline stubs cannot reproduce.
Expected stops, a malformed checker and stub-reproducible mutation probes
also fail that criterion. The stub-attempt requirement and ≥3-failure
trigger remain unchanged. Generation and narrow runtime checks are utility
evidence only; bypass and owner acceptance do not prove methodology efficacy,
independent GD usage, enforcement or global coverage.

**Advisory dispositions:** H5/H6 now have separate Horizon-2 seats, paired
[spec coverage](dormant-work-specs-2026-07-11.md#current-queue-coverage-2026-10-01)
and [runbook Agenda item 9](checkpoint-2026-10-11-runbook.md#agenda-item-9--h5--h6-september-held-candidate-review);
their owning Held gates and the other H candidates remain unchanged. That
coverage map addresses the actual roadmap queue, not every candidate in
every survey. The G9 measurement-provenance correction above still separates
GW-1/R13 from the missing G9 vocabulary baseline; no R8 bypass/tuning ruling.
Existing Agent Skills metadata-value/compatibility-length gaps are recorded,
not repaired or called reference conformance. No skill, registry, validator,
router, owning adoption ledger or checkpoint outcome is changed here.

### Pre-checkpoint packet (2026-10-10)

The [dated eleven-check preparation](checkpoint-2026-10-11-preparation-2026-10-10.md)
records fresh source-page reads, live registry/row counts, character/source
digests and complete S1–S5 EOF fingerprints. The older inventories above
remain dated observations. Five October 6 admission dry-run rows are
reported separately from the historical generation population; neither
maintenance nor this preparation adds a real invocation. P6 solo-use
classification and the checkpoint's owner rulings remain open, and external
use stays unknown. No early outcome, demotion, merge or policy activation.

## Review checkpoints

- 2026-10-11 — P6 merge re-litigation consumes this table
  ([pack record §Required Changes 6](flow-control-pack-panel-record-2026-07-11.md));
  zero recorded solo invocations for either skill re-opens the merge question.
- Host-native demotion trigger evaluations cite this log for the
  zero-recurrence branch
  ([first evaluation, not fired](flow-pack-demotion-evaluation-2026-07-11.md)).
- 2026-10-11 — `governed-delivery` recurrence checkpoint consumes the
  `governed-delivery` row ([GD adoption §Demotion Triggers](governed-delivery-adoption-2026-09-03.md),
  [runbook Agenda item 7](checkpoint-2026-10-11-runbook.md)).
