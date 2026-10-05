# Runtime-Skills Integration and Experiments — 2026-10-05

> **Status: user-directed in-place pack extension implemented; bounded experiments and source-review repairs verified.** Non-authoritative implementation and experiment record. Existing skill contracts and `06-repo/AGENTS.md` retain authority; no owned runtime or core-routing change is authorized. The configured model comparison remains provider-blocked; repository-gate observations are preserved separately after execution.

## Goal and authority

User instruction: “Fix advisory” and “do everything you can do for runtime skills and their experiments.” The implementation extends existing host-invoked packs, not a new skill, scheduler, fleet, broker, recorder or cancellation manager. Existing recurrence and demotion gates remain unchanged; synthetic maintenance experiments are not real-invocation rows.

Prior decisions were read in full before implementation:

- [Methodology-only rethink](methodology-only-rethink-panel-2026-10-01.md): MR-3 requires documented real-world script-structure failures that offline stubs cannot reproduce; MR-5 restricts reproduced-defect fixture cleanup; MR-6 rejects an owned runner.
- [Product/runtime ownership](product-runtime-ownership-panel-2026-08-25.md): execution success is not product acceptance; record and lifecycle promises require corresponding host guarantees.
- [Skills/runtime legitimacy](skills-runtime-legitimacy-panel-record-2026-07-06.md): a finite L3 verifier is not an L4 runtime; prompt text cannot manufacture enforcement.

Every delegated review brief retains complete-review delivery to Main before yield, with a complete structured-result fallback and explicit disclosure of messaging failure. No successful hub send is inferred from a delivered summary.

## Candidate Adoption Ledger

| ID | Candidate and destination | Status | Evidence / guard | Next action or trigger |
| --- | --- | --- | --- | --- |
| RS-1 | Selected `PREFLIGHT` before dispatch and result publication in both flow packs | Adopted 2026-10-05 (user-directed; recurrence unchanged) | Both pack templates/examples; `test_flow_generator_consumers.py`, `test_flow_loop_consumers.py`; 38 paired offline operational arms | Re-observe changed host/spec/oracle bindings; initial-success and quorum must not mask exit 4 |
| RS-2 | Finite generated delivery evidence-record checker and one-path executable wrapper | Adopted 2026-10-05 | Delivery template/example; `test_runtime_preflight_consumers.py`; 17 checker cases and four generated-loop coupling cases | Reject incomplete, malformed or stale required records; coherence does not authenticate enforcement |
| RS-3 | Matching role/profile/freshness evidence fields and host ownership in delivery and governance-scaffold generation | Adopted 2026-10-05 | Both contracts/examples; six positive and six exact-denial host controls; existing admission/protocol guards | Host owns protection and observation; no second governance runner, implicit cancellation or automatic human acceptance |
| RS-4 | Separate baseline/treatment, process, CLI, model and acceptance evidence | Adopted as experiment record only | Complete receipt bundle; named adoption rows P16, GD-20 and G10; maintenance log | Model repair needs the configured provider's usage credits; no efficacy, ROI, recurrence or complete-refuter promotion |

## Contract and traceability

- `PREFLIGHT` is one executable pathname, never shell text. A selected missing/non-executable/failing gate exits 4. Gate failure must not be absorbed as a tolerable branch failure or overridden by an already-successful deterministic verifier.
- Required host evidence binds `spec_version`, actual command/version/profile identity, the declared required controls, task-declared freshness and immutable file hashes. Missing or inconclusive required evidence remains `unknown` and holds; stale evidence requires re-observation/replanning.
- The checker verifies record coherence, not authenticity. A matching hash, principal label or zero exit does not prove role isolation or independent attestation.
- Worker-denial evidence needs the actual checked role, same-profile positive controls and the intended refusal. An owner-authorized oracle edit is not an adversarial worker-denial proof.
- `artifact-complete` never becomes `enforcement-proven`, and process/CLI exit never closes named human acceptance. Driver interruption does not imply descendant cancellation.
- Existing nine core skills, five registered packs, route fixtures, authoritative acceptance oracles and checkpoint criteria are intentionally unchanged.

## Evidence Actually Checked

### Complete-source baseline

The initial experiment snapshot copied the reader's default 300-line view and continuation footer. It truncated later templates and caused a harness extraction exception before the DAG case. That output is preserved as a harness failure, not a pack defect or MR-3 case. Complete unchanged installed originals were then captured with explicit full ranges; every original captured source prefix matched exactly.

| Baseline pack | SHA-256 of complete original source |
| --- | --- |
| `flow-control-generator` | `bbf46b7f52e844a4a158f12b47a0fcaaa0bac128822e8d76148a9e8dcec15cab` |
| `flow-loop-harness` | `89ad2eb1ff8b096db6baf403d7672c3e0e36032630a4893eb69eb4fadd4692c8` |
| `governed-delivery` | `745ee40d34f9e617a81b6323773ac7d656a3f94e28a201cf7e17738c37ba6585` |
| `agent-governance-scaffold` | `4b50435c1a5d5335a3b5515a5fb2ce51cffa4c91739ed13aa373391a2973e73a` |

Baseline: 38 operational cases across five one-pass and four loop topologies. All nine normal arms exited 0. None of the faulty selected-gate arms exited 4; all 18 denied/missing-gate arms dispatched stub work. The remaining cases exercise mid-run oracle mutation and two already-successful initial-verifier paths. These are real subprocesses with explicit offline stdin stubs, not model-worker or product-acceptance evidence. The unchanged baseline did not promise the newly introduced optional `PREFLIGHT` interface; this comparison demonstrates the extension, not a previously claimed contract violation.

Treatment: all 38 operational cases met their expected outcomes. All nine normal arms still exited 0; all 29 faulty-gate or already-successful-but-held arms exited 4. The 18 denied/missing-gate arms dispatched no agent work.

### Emitted checker and flow coupling

The initial generated checker was exercised in 17 record-coherence scenarios using preserved real-role output as record data. Five expected holds instead returned `ready`: nonfinite `Infinity` age, overflow exponent age, timezone-free timestamp, unsupported binding proof field, and duplicate JSON claim. The source was repaired to reject nonfinite/duplicate JSON, require an unambiguous timezone, contain timestamp overflow, and reject unsupported binding keys. The same 17 scenarios then had zero mismatches: coherent records were `ready`/0; required unknown/missing, malformed or stale time/spec/host/oracle/artifact records returned `hold` or `stale`/4. This validates the records, not the producer or the active worker's profile.

Four actual generated-loop/checker coupling arms also matched:

| Coupled arm | Exit | Agent dispatches | Boundary |
| --- | --- | --- | --- |
| Python checker selected directly without JSON arguments | 4 | 0 | Correct CLI-usage hold; select the executable wrapper instead |
| Wrapper supplies coherent note/binding | 0 | 1 | Normal result accepted by the deterministic verifier |
| Wrapper sees required `unknown`, initial verifier already succeeds | 4 | 0 | No zero-work release bypass |
| Wrapper sees spec become stale after dispatch | 4 | 1 | Downstream acceptance blocked |

The wrapper is generated as `checks/run-preflight.sh`, selected by absolute pathname from the reviewed task root, and executes `python3 checks/preflight.py run-note.json binding.json`. Record `command` fields are data, never executed by the checker.

### Final source-review repairs

Both complete reviewer deliverables were preserved, including their messaging-unavailable disclosures; neither is claimed as a successful hub send. Their `AGREE WITH CHANGES` findings were repaired by Main and exercised against the changed templates:

- Checker: 16 additional before/after cases cover conflicting and malformed control observations, unknown controls, an optional `met` without evidence, omission of any of the five explicit control fields, embedded-NUL/surrogate paths, FIFOs and device files. Before repair, eight cases falsely returned `ready` and seven crashed or blocked; after repair, coherent input returned `ready`/0 and all 15 invalid cases returned `hold`/4 without traceback or blocking.
- Flow: final DAG preflight, router post-dispatch-before-label handling, concurrent worker-error/peer-hold precedence, malformed quorum/worker configuration, and unlaunchable selected gates were exercised in 15 scratch cases. Three initially alleged orchestrator environment-cap defects were harness expectation errors: that template declares literal caps, not those environment variables. The original receipt is retained; the corrected after-run had zero mismatches.
- The final 38-arm operational matrix was rerun against the repaired source: nine normal exits 0, 29 holds at exit 4, and no work dispatch in the 18 denied/missing-gate arms. The final 17-case checker run and four actual generated-loop coupling arms also had zero mismatches.
- Consumer isolation: direct generator/loop fixtures and five legacy call sites in four files no longer inherit ambient `PREFLIGHT`, quorum, iteration or worker settings. Exact executable-code pins and incidental size assertions were removed, not re-pinned; named protocol/adoption guards and behavioral regressions remain. The first expanded check reported 129 passes and one stale executable-code pin, not a runtime failure; its output is preserved.

### Executable-pin removal and behavioral coverage closure — 2026-10-05

User follow-through: "fix advisory". The previous removal affected **eight executable-code pins**, not seven: four generator pins and four loop pins in `test_skill_verification_panel_record.py` (`PINS` plus `AT_LEAST_ONCE`). The WR-05 named progress-contract prose remains pinned. The originating decisions are the [2026-09-05 panel](skill-verification-panel-2026-09-05.md) and the [whole-library WR findings](../../review/final-report.md#final-report--whole-library-plan--skill-review); not every pin originated in a WR finding.

**Tradeoff:** literal pins cheaply detect a missing spelling but neither establish execution nor permit equivalent implementations. Removing them without a consumer map can hide a real gap. Decision: keep named protocol/adoption guards, replace executable spellings with observable runtime invariants, and retain the size warnings as observations rather than an acceptance threshold. This closure adds developer regressions; it changes no runtime template, acceptance oracle, adoption decision, recurrence criterion or checkpoint outcome.

Generator cases below live in `tests/test_flow_generator_consumers.py`; loop cases live in `tests/test_flow_loop_consumers.py`. The evidence bundle preserves the eight former literals and the complete offline smoke receipt.

| Former executable pin | Origin / invariant | Behavioral guard and disposition |
| --- | --- | --- |
| Bash stdin runner plus nonempty-output condition | D1; WR-21 stdin channel; WR-20's shared empty-evidence rule was originally observed in the loop | **Strengthened:** `test_bash_fanout_large_prompt_avoids_argv_limit` runs a 2 MiB prompt; `test_bash_fanout_empty_success_cannot_satisfy_strict_policy` requires exit 2 with no synthesis/final artifact despite one successful peer. Existing Python empty-output and large-goal guards remain. |
| `status.get(FINAL_NODE)` acceptance predicate | WR-04; D7's merged-result gate | **Already behavior-covered:** `test_multi_tail_dag_checks_explicit_merge_independent_of_order` exercises both traversal orders; failed/missing/nonterminal final-node cases and the legacy quorum/merged-gate dry-run remain. The smoke mutation actually targets `report.out` instead of `assemble.out` and is caught. |
| Sanitized `wid` without a silent fallback | D6; WR-02 output identity | **Already behavior-covered:** invalid/empty effective IDs, exact/sanitization/case-fold collisions and distinct surviving worker evidence. The smoke's fallback `"task"` falsely accepts an empty effective ID; the existing rejection test catches it. |
| Planner root `isinstance(tasks, list)` | D5; WR-02 whole-plan validation before workers | **Strengthened:** object and JSON-null roots join the invalid-plan matrix; exit 2, one planner call, no workers/final. Removing the root guard turns null into a traceback/exit 1 and is caught. |
| Branch-only summary `cksum` | FLH-8; WR-03/20 require current, nonempty branch evidence | **Strengthened:** `test_wave_stall_uses_evidence_not_changing_wave_headers` stops repeated evidence at wave two/exit 3; changing evidence reaches the declared three-wave cap/exit 2. Existing reused-STATE/empty/failed-branch guards remain and catch stale-artifact and empty-evidence mutations. |
| Whole-critique `ACCEPT` expression | FLH-4/10; not itself a WR repair | **Strengthened:** `test_writer_requires_the_whole_critique_to_accept` rejects mixed ACCEPT/REJECT and accepts only ACCEPT plus blank lines, in both attended and companion-floor entry points. A present but rejecting floor also blocks release; WR-06's missing/non-executable floor tests remain. |
| Executable `VERIFY` guard | Loop Anatomy 1/6; WR-06 is the companion-floor availability analogue | **Strengthened:** `test_declared_broken_verifier_holds_before_loop_work` requires exit 4, zero agent calls and no final artifact for missing/non-executable verifiers in fix, backlog and multi-wave entry points. Removing the guard changes these to ordinary cap/verify-failure exits and is caught. |
| Canonical absolute STATE path for snapshot exclusion | WR-05 content progress, excluding run state | **Already behavior-covered:** `test_fix_state_logs_and_probes_do_not_mask_real_stall` requires exit 3 after one call when only STATE changes, including tracked/staged STATE. `test_fix_content_progress_survives_equal_churn_and_file_transitions` preserves two changing-content calls and reaches cap/exit 2, while `test_backlog_retires_equal_churn_content_changes` retires both changed tasks/exit 0. Equal diff-stat churn is not equal content: treating the former as a stall would restore WR-05's bug. `test_non_git_constant_diagnostic_is_not_workspace_stall` explicitly disables workspace detection outside git and reaches cap/exit 2, not a fabricated stall. The stored failed-STATE-exclusion mutation fabricates progress and reaches cap/exit 2 instead of first-call stall/exit 3; the existing test catches it. |

**Observed:** 17 parameterized cases added; both direct consumer modules pass all 79 cases under poisoned ambient gate/quorum/cap variables. The isolated emitted-program smoke has 20 unmodified-template control arms and 18 altered-template arms across 12 regressions; all controls match their expected outcomes and all altered arms are rejected, with zero mismatches. It records actual subprocess argv, exit, stdout/stderr and resulting artifacts; mutations exist only in disposable fixtures, never in repository templates. The scratch source and receipt are preserved under `advisoryClosure` in `local://runtime-skills-final-evidence.json`.

Delayed-advisory follow-through is record-only: the named WR-05 progress-prose pin remains in `test_skill_verification_panel_record.py`; the seven delayed notices reveal no remaining runtime/test gap. Unchanged SHA-256 bindings preserve the prior passing consumers and stored equal-signal/STATE-exclusion controls rather than re-running them just to reconfirm. One fresh outside-git fix-loop probe changes only STATE, leaves workspace content unchanged, observes disabled workspace detection, makes two stub calls and reaches the declared cap/exit 2 without a NO PROGRESS claim. Multi-wave branch-only checksums remain independent of git; the stored repeated-evidence control has identical `3679282965 14` signals in waves one/two and exits 3. The follow-through source bindings and receipt are preserved under `delayedAdvisoryDisposition` in the same evidence bundle; no runtime, test, oracle, adoption or checkpoint change is authorized by these notices.

This is coordinator-produced deterministic/runtime control-flow evidence, not an independent re-review, model efficacy result, full GDR refuter, real invocation, host-enforcement proof or checkpoint clearance. Earlier reviewer verdicts retain their original packet bindings. Behavioral fixtures do not exhaust all possible template edits; deleting a named contract requires its own authority rather than a passing fixture score.

### Consumer map

| Consumer class | Disposition and evidence |
| --- | --- |
| Direct generated scripts and alternate topology entry points | Covered: all nine topologies; initial-success, quorum, pre/post-dispatch and final-release paths |
| Generated checker and executable-wrapper selection | Covered: 17 original and 16 review cases; four actual loop/checker coupling arms |
| Existing fixture callers | Covered: direct and legacy helpers use isolated environments; final test results are retained in the evidence bundle |
| Examples, adoption rows and maintenance/checkpoint references | Covered: four pack examples, P16/GD-20/G10 and this record; observations do not change recurrence or checkpoint criteria |
| Persisted source/catalog values | Covered: complete original and final source snapshots with digests; committed catalog regenerated before the repository gate |
| Actual model worker, continuous sealing, cancellation and human acceptance | Explicit untested boundary: model repair is provider-blocked; a finite coherence check cannot establish these host guarantees |

### Real OS role and CLI observations

A scoped macOS sandbox worker probe exited 0 with six same-profile positive controls: mutable write, oracle read, mutable rename/chmod/unlink, and an allowed loopback connection. Six intended forbidden operations returned exact `EPERM`: oracle direct write, replacement, unlink and chmod, scratch-external write, and a disallowed loopback connection. Oracle bytes remained unchanged. An unsandboxed control reached both live loopback targets, ruling out target unavailability for the network refusal.

Rejected network-address syntax, a restrictive-policy Node abort and incorrectly OR-composed write exclusions were preserved as harness failures. Only failed worker observations were retried; successful CLI/control observations were retained. The final profile uses `localhost` and `require-all` for conjunctive write exclusions. This proves named operations under one profile, not full OS containment or enforcement on a different model-CLI role.

Actual local CLIs: Claude Code `2.1.289`, Codex CLI `0.160.0`. Their invalid output-format/sandbox arguments were rejected with exits 1 and 2 respectively, before a provider call. CLI parsing/version evidence is separate from a model-worker repair result.

### Process interruption

A generated baseline verify loop ran a stand-in agent that spawned a child. Killing only the driver with SIGTERM produced exit -15; both agent and child remained alive, and the agent was reparented to PID 1. Cleanup killed only the coordinator-owned private process group. This falsifies “driver exit proves child cancellation”; it is not a real-model cancellation experiment, a cancellation guarantee or an MR-3 qualifying failure.

### Model and repository verification

The bounded real-model trial invoked the unchanged published verify loop through Claude Code with `--safe-mode`, `--restricted`, no filesystem tools, no session persistence and a $0.50 call cap. The configured default Fable 5.1 returned: “Fable 5.1 requires usage credits.” The CLI reported `api_error`, no model usage/result and cost 0; the driver exited 2, the independent verifier remained at exit 1, and immutable inputs were unchanged. This is one actual model-CLI invocation and its error path, not a model repair result. No fallback model was selected; billing, credentials and settings were not changed. A comparable model baseline/treatment repair remains blocked by that prerequisite. Actually executed repository verification is retained in the evidence bundle and final delivery report; no passing gate is inferred from this record's adoption status.

## Source measurements and preserved evidence

Whole-file character counts below use the same Unicode-character measure as `lint_skills.py`; they are observations, not assertions that source size is an acceptance oracle.

| Pack | Characters | Checked source SHA-256 |
| --- | --- | --- |
| `flow-control-generator` | 27,731 | `046affcaac57baaed9eb827cc94261474d3af67a6effaa73c44cb08acfced012` |
| `flow-loop-harness` | 24,566 | `464e2baf384b5344a2fc6a2c3eff18f35b7f83a0e2a0e047882d4aed1d94ebee` |
| `governed-delivery` | 34,517 | `c33e8ca4d46769edf25f9075adbdce77ce0632426b2815da784a188d87996d5c` |
| `agent-governance-scaffold` | 27,769 | `7fe256e49ebebd1664ea500bd72980fcabaad3b6dc22a6e2446150b4029a5951` |

All four exceed the nonblocking 20,000-character warning threshold. The generator and loop were below it at the dated 2026-10-01 prep measurement; governance-scaffold's warning predates this extension. Incidental source-size tests were deleted rather than re-pinning their thresholds; behavioral, protocol and adoption guards remain. No warning is hidden and no size observation clears the 2026-10-11 minimality review.

Complete coordinator receipts, including rejected harness attempts, before/after stdout/stderr, source hashes and exact argv, are preserved in the session artifact `local://runtime-skills-final-evidence.json`. It is a coordinator-produced evidence bundle, not independent attestation or a repository-hosted runtime. The checked baseline, treatment, role, CLI and parser outcomes remain separately labeled.

## Falsifiability and evidence limits

- Maintenance arms do not alter real-invocation counts, prove recurring demand, clear the 2026-10-11 checkpoint, or pass the full GDR-1–GDR-6 campaign. Partial oracle/metadata rejection must not be upgraded to a complete refuter result.
- No durability, restart/reattach, cancellation, remote transport, broker-mediated side effects or named product acceptance is supplied by the record checker.
- No provider/model or OS-containment guarantee is inferred from the offline stub arms. One successful bounded model proposal would remain narrow utility evidence, not coding efficacy or ROI.
- The implementation is wrong if any selected gate is skipped before dispatch/result release, quorum masks a configuration hold, incomplete required evidence is admitted, or a stale bound input can be released as current.
- The report is wrong if a model call, host role, passing gate, complete refuter, real invocation or human acceptance is claimed without its preserved observed output.
