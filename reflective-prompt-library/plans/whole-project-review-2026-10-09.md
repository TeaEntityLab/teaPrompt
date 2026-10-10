# Whole-Project Review and Recording — 2026-10-09

> **Status (2026-10-09):** Non-authoritative English review and continuation record. **Request changes** at `116f05f047ddd121ff5f9224666714b8aa5ad4a7`; **all 18 confirmed findings remain OPEN**. The user authorized recording everything into docs or skills where worthwhile, not implementation, a commit, a push, host adoption, a campaign, or an early checkpoint outcome.

## Goal and recording scope

Preserve the whole-project review of correctness, roadmaps, intent, and test quality so continuation does not depend on chat, session-local files, or temporary probe directories. Record every confirmed finding, its evidence tier, repair criterion, rejected or qualified hypothesis, and unchanged ownership gate. Promote only reusable lessons whose evidence warrants an existing destination.

The review preceded this recording turn and changed no repository files. This turn adds the record, discovery pointers, and evidence to an existing durable lesson; executable source, skill contracts, examples, fixtures, oracles, installation helpers, CI configuration, and adoption states are intentionally unchanged. Findings below are repair proposals, not repairs or new agent instructions.

**Decision:** Request changes. F01 is introduced by `116f05f`'s `_fold` implementation; F02–F18 predate that commit. The verdict concerns the inspected consumers, not nine-core routing as a design or the host-owned runtime boundary.

## Evidence Actually Checked

### Provenance and limits

- Review target: `116f05f047ddd121ff5f9224666714b8aa5ad4a7`. Before recording, all **15 retained SHA-256 source bindings** matched the repository files. A documentation-only discovery pointer added later to the roadmap does not rewrite its reviewed hash or alter its scheduling semantics.
- Main ran six offline CLI/fault-control probe groups, **30 case records**, against extracted published templates or the actual developer CLI. The repeated-pipeline case contains two invocations; 30 is a case count, not an invocation or repair-pair denominator. Stub agents and deterministic scorers were used; **zero model/provider calls** were made by these probes.
- Five read-only specialist reviews (`FlowReview`, `PackReview`, `RoadmapReview`, `IntentReview`, `TestReview`) supplied hypotheses. Main's runtime controls, source checks, and adjudications determine the findings below. Five model perspectives are **not five independent empirical confirmations**.
- The same-revision baseline receipt is **1,568 tests passed, zero validator errors, three routing evaluations passed**, with nine non-blocking skill warnings and 35 historical-record warnings. It was reused, not rerun during the read-only review. A green suite coexists with the reproduced defects; it is not their closure evidence.
- No prior failing probe was rerun just to record it. Fresh documentation verification belongs in the recording completion section of [the final report](../../review/final-report.md#whole-project-review-recording-2026-10-09), separate from these historical observations.
- Original session provenance, not repository dependencies: `whole-project-review-evidence-2026-10-09.json`; baseline receipt `artifact://2169`; probe receipts listed below. All concrete inputs, outcomes, rulings, source hashes, and continuation criteria needed for the findings are preserved in this document. Temporary paths, raw transcripts, and private host artifacts are not prerequisites for understanding it.

| Probe group | Case records | Original receipt | Findings / ruling |
| --- | ---: | --- | --- |
| Blinded output-path identities | 4 | `artifact://2193` | F01 |
| Prompt composer CLI | 2 | `artifact://2205` | F02, F08 |
| Core installation helpers | 4 | `artifact://2205` | F09 |
| Routing policy fault controls | 4 | `artifact://2329` | F04 |
| Flow-generator published templates | 6 | `artifact://2346` | F05–F07, F14 |
| Router-trace extracted CLI | 10 | `artifact://2348` | F03, F11; Next Action scope ruling |

### Claims ledger

| Claim | Checked how | Status and boundary |
| --- | --- | --- |
| All four requested review dimensions were considered | Whole-project sources, canonical plan/roadmap/specs, intent declarations, test consumers and six runtime groups | Verified as review coverage, not an exhaustive proof of correctness |
| Published consumer paths have reachable failures despite green gates | Inputs and observed results in F01–F11/F14 | Verified for the named cases |
| Join validation and golden-ledger examples disagree with their contracts | Methods/Output clauses compared with documented ordinary inputs and examples | Verified spec/example defects; no owned join or golden runner was executed |
| Current aggregate documentation is stale | Registry, installation loops, roadmap/spec ownership and executable validator compared with narratives | Verified source/navigation drift; no adoption or dormant execution follows |
| Prior blinded-output repair covers every output alias | New missing-parent traversal probes | Refuted: F01 is a new escape from the checked identity classes |
| Installed skill use improves model utility or enforces host isolation | Not exercised by these probes | Unverifiable here; remains host/campaign work |
| Excluded CI inputs can be merged without checks | Only local workflow filters and test consumers inspected | Unverifiable; suite skip is established, remote branch-protection consequences are not |

## Confirmed findings

All finding statuses are **OPEN**. Source locations bind to the reviewed revision; later edits need current source review. Repair acceptance below is **proposed and not executed**.

### F01 — High — Missing-parent traversal defeats blinded-output identity

- **Source:** [arm-blinded-eval-harness](../skills/arm-blinded-eval-harness/SKILL.md), lines 162–174; runtime defect introduced by `116f05f`.
- **Observed:** The unchanged documented control exits 0, dispatches four scorers, and keeps its arm-labelled sealed map outside `blinded/`. Setting `sealed_map` to `new-parent/../blinded/sealed-map.json` also exits **0** and dispatches **four scorers**, but physically places the arm-labelled map inside `blinded/`. Setting `blinded` to `new-parent/../blinded` with `sealed_map: blinded/sealed-map.json` has the same escaped boundary. Setting `run_note` to `new-parent/../results/scores.jsonl` exits **4** with an exclusive-open collision and zero scorer dispatch, but only **after reserving** `blinded/`, `map/`, `results/`, and `new-parent/`.
- **Cause/effect:** `_fold()` reconstructs a missing suffix containing `..` without eliminating or refusing parent traversal. The identity tested by preflight differs from the identity used by filesystem creation; scheduling metadata can reach scorer-visible data. This is not merely a late error message.
- **Repair acceptance:** Reject parent traversal or canonicalize it with defined filesystem semantics before output-identity comparisons. Preserve strict existing-ancestor resolution and loop/dangling-parent refusal. Both traversal directions and the output alias must refuse before any output reservation or scorer dispatch; a corrected configuration must still work in the same namespace and recover the planted outcomes. Ordinary missing suffixes need a valid positive control. No claim of actor isolation or atomic publication follows.

### F02 — High — Low-token composition removes primary instructions

- **Source:** [prompt_composer.py](prompt_composer.py), lines 176–182; runtime defect predating `116f05f`.
- **Observed:** Actual CLI composition of `core-short` for task `Review a data migration` exits **0** both with and without `--low-token`. Full output contains `Inputs / Outputs`, `Failure Conditions`, `Self-check`, and `對 AI 產物保持不信任`. Low-token output retains `Self-check` but drops the other three, including the primary fenced prompt's anti-cheating instruction.
- **Contract/test mismatch:** The option promises to strip extended examples while keeping the template and core rules. `_strip_examples` instead deletes all fenced blocks. `test_prompt_composer.py:63–70` reinforces the wrong behavior by requiring fences to disappear and output to shorten.
- **Repair acceptance:** Remove only explicitly identified examples, preserving primary instructions and safety/acceptance content whether fenced or not. Replace incidental fence/length assertions with consumer-visible semantic-retention checks on `core-short` and another primary template. Compression must not manufacture a successful but instruction-poor artifact.

### F03 — Medium — Folded YAML hides the action from trace risk checking

- **Source:** [router-trace-linter](../skills/router-trace-linter/SKILL.md), lines 119–130; runtime defect predating `116f05f`.
- **Observed:** A complete low-risk control passes. Replacing its Goal with inline `deploy to production` and keeping `Human Review: not required` exits **1**, as expected. Encoding the same action as `Goal: >` followed by an indented continuation exits **0**; output reports `Goal: >` as complete and Human Review as acceptable.
- **Cause/effect:** The parser advertises YAML input but ignores continuation lines; representation changes remove the action from the risk check.
- **Repair acceptance:** Parse the supported multiline scalar form, or explicitly refuse unsupported scalar syntax rather than treating `>` as the Goal. Equivalent high-risk content must reach the same review obligation across supported forms; ordinary complete low-risk traces still pass. Do not confuse this reproduced parser loss with the separately declined Next Action scope extension.

### F04 — Medium — Missing routing-policy keys disable mandatory checks

- **Source:** [route_paraphrase_eval.py](route_paraphrase_eval.py), lines 918–958 and 1020–1040; runtime defect predating `116f05f`.
- **Observed:** In a disposable copy of the adversarial fixture and router, one injected silent misroute produces consistency **107/108**. With `forbid_silent_downgrade` present, the CLI exits **1** with one incident; removing that key leaves the same consistency but exits **0** and reports zero incidents. A separate injected low-confidence missing-rationale fault exits **1** with trace coverage **14/15** and one failure when `require_route_trace_on_low_confidence` is present; omitting that key exits **0**, reports coverage **1.0**, and suppresses the failure.
- **Cause/effect:** Optional-key defaults silently turn off obligations needed by the CLI's hard-gate decision.
- **Repair acceptance:** Validate required policy keys and their types before evaluation. Omitted keys must be a configuration failure, not a reduced policy. Retain the two fault-injection contrasts and valid configured controls; do not tune routing or weaken fixture thresholds to close this finding.

### F05 — Medium — Zero quorum with no survivors never reaches the merged gate

- **Source:** [flow-control-generator](../skills/flow-control-generator/SKILL.md), line 139 and lines 185–198; runtime defect predating `116f05f`.
- **Observed:** Published fan-out template, two branch prompts, failing stub, `MIN_OK=0`: two dispatches, `branch gate=0 successful=0`, then exit **1** at unmatched `cat ./state/fan-*.md`; the merged gate never runs. The passing control dispatches both branches plus synthesis, reaches the merged gate, and exits **0**.
- **Contract:** Zero quorum deliberately accepts any branch tally; the merged result still decides acceptance. Rejecting zero survivors outright would silently replace that policy.
- **Repair acceptance:** Assemble a synthesis input safely when no branch output survives and still execute the merged acceptance gate. Exercise both accepting and rejecting merged gates, plus the ordinary surviving-branches control; no unmatched-glob abort may stand in for the declared gate.

### F06 — Medium — Published pipeline omits its repeated-failure discipline

- **Source:** [flow-control-generator](../skills/flow-control-generator/SKILL.md), line 86 and lines 108–117; contract/runtime defect predating `116f05f`.
- **Observed:** Two identical failed sequential-pipeline runs in the same fixture each dispatch the failed first step, both exit **1**, and log start/failure again. The template does not persist or consult the failure signature promised by Script Contract. Specialist source review identifies the same missing integration in other generator templates; only the sequential repeated-run path was runtime-probed here.
- **Repair acceptance:** Make the shipped templates honor the declared repeated-failure rule using a driver-owned location outside worker-writable `STATE/`. The host owns protection; script mechanics cannot claim to enforce hostile-worker isolation. A repeated signature must stop before identical redispatch, while an explicitly changed strategy or declared correction can proceed under the contract. Review sibling templates before closing the broader integration gap; preserve raw failed-run receipts.

### F07 — Medium — DAG has an undeclared Python-version requirement

- **Source:** [flow-control-generator](../skills/flow-control-generator/SKILL.md), compatibility line 5 and eager union annotation at line 381; runtime/compatibility defect predating `116f05f`.
- **Observed:** The published DAG executed with actual `/usr/bin/python3` **3.9.6** exits **1** at `str | None`, with `TypeError`, zero dispatches, and no merged gate. Python **3.14** control exits **0**, dispatches four nodes, and reaches the merged gate. Compatibility declares only `python3` for Python templates.
- **Repair acceptance:** Postpone/remove eager union annotations to honor the declared environment, or deliberately declare a supported Python floor and migrate all affected compatibility guidance. A sibling pack's floor is not this pack's contract. Exercise the declared oldest supported runtime and the current runtime before closure.

### F08 — Medium — Missing indexed input produces a successful partial composition

- **Source:** [prompt_composer.py](prompt_composer.py), lines 193–200 and 225–230; runtime defect predating `116f05f`.
- **Observed:** In a temporary indexed corpus, remove `spec-writer` and request `core-full spec-writer`. The CLI prints a missing-file warning but exits **0**, claims `Generated from 2 prompts`, and emits only Prompt 1.
- **Repair acceptance:** Propagate the missing required input as a nonzero failure without publishing a success-shaped partial composition. Keep valid multi-prompt composition as the positive control; include output-file mode so partial data is not committed as an apparently complete artifact.

### F09 — Medium — Core install helpers swallow source-resolution failure

- **Source:** [SKILL_INSTALLATION.md](../SKILL_INSTALLATION.md), lines 115–142; runtime defect predating `116f05f`.
- **Observed:** Both documented core-copy and core-symlink functions emit a `cd` error for a missing source, create the destination, install **zero skills**, and exit **0**. Their valid-source controls each install **nine skills** and exit **0**.
- **Repair acceptance:** Propagate source-resolution and filesystem-operation failures before reporting installation success; reject a source with none of the expected core skills. Keep copy/symlink positive controls and existing non-link replacement refusal. Review the bilingual helper surfaces together; no permission widening or unrelated destination deletion is authorized.

### F10 — Medium — CI trigger filters omit inputs consumed by checks

- **Source:** [python-tools.yml](../../.github/workflows/python-tools.yml), lines 5–15; [.pre-commit-config.yaml](../../.pre-commit-config.yaml), line 9; static-configuration defect predating `116f05f`.
- **Observed source mismatch:** Workflow filters cover `reflective-prompt-library/**`, `Makefile`, and the workflow itself, but omit `acceptance.yaml`, `VERIFY.md`, `features/**`, and root README files. Existing tests consume those root inputs. The local hook covers the first three categories but not root README files.
- **Evidence boundary:** This establishes a **skipped check suite** on excluded-only changes, not a remotely observed green required check or permission to merge.
- **Repair acceptance:** Align CI and hook scope with the inputs their checks consume. Verify included/excluded path decisions without recursively running all acceptance commands inside pytest. Remote branch-protection behavior remains a separate untested owner boundary.

### F11 — Medium — Trace linter rejects documented low-risk forms

- **Source:** [router-trace-linter](../skills/router-trace-linter/SKILL.md), lines 95–100, 214–215, 237, and 244–247; runtime/contract defect predating `116f05f`.
- **Observed contrasts:**
  - `Goal: credit the original author in the changelog` with no hazardous action exits **1** because substring `auth` in `author` fires R4; the ordinary local-rename control passes.
  - A complete six-field machine alias trace with `rationale: copy change only` exits **1** as missing Assumptions; the longer non-deferred rationale `Only copy changes are needed for this local update.` passes. The alias form does not require an independent Assumptions field, and the sentence-length requirement belongs to deferral justification, not every alias rationale.
  - With an available but disabled enhancement, `Assumptions: The existing suite already covers this surface well` exits **1** as rationale missing, although Assumptions is a documented rationale seat. Adding undocumented matching words, `The performance review is deferred because the existing suite covers this surface.`, passes.
  - Low-risk `Human Review: skipped` with no deferred enhancement exits **1** as missing R5/R7 rationale even though skipped review is an accepted low-risk representation. Whole-trace deferral scanning confuses review status with a deferred enhancement.
- **Repair acceptance:** Use intentional risk-token boundaries, field-scoped deferral detection, and the advertised alias/rationale-seat rules. Retain the contrastive low-risk matrix and genuine hazard/deferral refusal controls; a permissive blanket regex is not a repair.

### F12 — Medium — Static command resolution misinterprets ordinary shell forms

- **Source:** [acceptance-join-validator](../skills/acceptance-join-validator/SKILL.md), line 39; **spec defect**, predating `116f05f`.
- **Source-level cases:** The prescribed first-word/segment algorithm resolves `cd sub && ./test.sh`'s second segment against the product root instead of `sub`; `FOO=1 make test` treats `FOO=1` as an executable. There is no owned join runner, so these are not observed failures of an executed TeaPrompt validator.
- **Repair acceptance:** Define the supported static shell grammar, directory context, and leading environment-assignment semantics; explicitly classify unsupported syntax. Command resolution stays static and never runs acceptance commands. A fixture consumer may verify the algorithm, but must not become a shipped runner or widen TeaPrompt's runtime scope.

### F13 — Medium — Golden-ledger examples omit required evidence fields

- **Source:** [golden-benchmark-runner examples](../skills/examples/golden-benchmark-runner.examples.md), lines 18–19; [Output contract](../skills/golden-benchmark-runner/SKILL.md), line 48; example-contract defect predating `116f05f`.
- **Observed source mismatch:** The two canonical JSONL rows omit completion/censoring status and reason, plus scorer executable identity and revision, despite those fields being required. Following the example cannot distinguish completed failures from censored or unscored outcomes as required.
- **Repair acceptance:** Show completed/censored status, reason, pinned scorer identity and revision, and the unscored/null distinctions. Parse the documented rows and check their semantics against the contract; no new golden runner or comparative efficacy result is implied.

### F14 — Low — Empty agent command crashes instead of holding configuration

- **Source:** [flow-control-generator](../skills/flow-control-generator/SKILL.md), lines 264 and 289; runtime defect predating `116f05f`.
- **Observed:** Explicitly empty `AGENT_CMD` in the published orchestrator yields `IndexError`, exits **1**, records `plan.json start` without completion, dispatches **zero agents**, and never reaches the merged gate.
- **Repair acceptance:** Validate the parsed command before any dispatch and return the declared configuration-failure class with a retained diagnostic. Exercise empty and whitespace-only values plus a valid argv control; do not select a provider as a silent default for invalid explicit input.

### F15 — Low — Aggregate narratives still report five or six packs

- **Source:** [whole-project plan](whole-project-plan-2026-07-11.md), line 49; [usage log](flow-pack-usage-log.md), line 4; [English installation prose](../SKILL_INSTALLATION.md), line 98; roadmap admission history.
- **Observed:** The plan's dated supersession says **six**; the usage-log header and English installation prose say **five**; aggregate roadmap admission waves end at the fifth pack. The current registry, pack lists, and installation loops correctly contain **ten** packs.
- **Repair acceptance:** Add a dated current supersession and October admission pointers without rewriting test-pinned historical literals or changing registry cardinality. Every current count claim must use the live registry. This turn records the mismatch and adds a review pointer, but does **not** reconcile those count claims or close F15.

### F16 — Low — Aggregate queue omits S3 and July H3/H4 discovery pointers

- **Source:** [whole-project roadmap](whole-project-roadmap-2026-07-11.md), lines 134–168; [dormant spec-book coverage map](dormant-work-specs-2026-07-11.md), lines 58–118; owning spec details at lines 648–702 and domain-plan ledgers.
- **Observed:** S3 packaging and July H3/H4 dormant work are absent from the current aggregate queue/coverage map, although owning specs and dormancy guards still exist. They are navigation omissions, **not ownerless work**. July H3/H4 are distinct from similarly named September H rows.
- **Repair acceptance:** Add source/disposition pointers preserving each existing trigger and owner. No execution, scheduling, adoption, or blanket closure follows. The recording pointer added to the roadmap is not that inventory repair; F16 remains open.

### F17 — Low — Requirement definitions and references are underspecified

- **Source:** [acceptance-join-validator](../skills/acceptance-join-validator/SKILL.md), lines 36–38, and its [examples](../skills/examples/acceptance-join-validator.examples.md); spec-clarity defect predating `116f05f`.
- **Observed source ambiguity:** Extraction records ID occurrences, but the duplicate rule says an ID is **defined twice**. The clean example mentions `AC-101.1` across sources and expects zero duplicates. A repeated reference is not automatically a duplicate definition; the contract does not explain classification.
- **Repair acceptance:** Distinguish authoritative definition sites from references, including `covers` references. Fixtures must contrast a genuine double definition with multiple legitimate mentions. Do not turn every repeated token into an error to obtain an apparently simple validator.

### F18 — Low — Maintenance descriptions lag executable and routing contracts

- **Source:** [QUALITY_GATES_SUMMARY.md](QUALITY_GATES_SUMMARY.md), line 198; [root README](../../README.md), line 35; [CONTRIBUTING.md](../../CONTRIBUTING.md), lines 32 and 37; [GLOSSARY.md](../GLOSSARY.md), line 477.
- **Observed source mismatch:** Documentation says the benchmark fixture validator regenerates JSON; the executable only compares the committed artifact and reports drift. Maintenance navigation still ends at R12 although R13 is live.
- **Repair acceptance:** Correct compare-versus-regenerate instructions and rule-range pointers using the actual existing generator and routing contract. Do not change validator behavior, thresholds, fixtures, or routing merely to match stale documentation.

## Advisory adjudication

These dispositions retain considered claims rather than silently dropping them. Specialist outputs are hypothesis sources; the ruling is Main's evidence-first synthesis.

### Withdrawn claims

| Source | Claim considered | Ruling and evidence boundary |
| --- | --- | --- |
| TestReview | Contested routes are silent downgrades | Withdrawn: current code and feature contract explicitly expose contested traces as visible. |
| TestReview | Exact cardinality ratchets violate grow-only fixtures | Withdrawn: same-change pin updates preserve coverage; the incorrect greater-than mutation claim was withdrawn. |
| TestReview | All acceptance checks should run inside pytest | Rejected: this would recursively invoke `make all`/pytest. The existing two scalar registry consumers are the safe boundary. |
| TestReview | `eval_harness` exit 0 violates a gate contract | Withdrawn: no CLI gating promise established; this is a static scorer/reporting surface. |
| RoadmapReview | I-1 fired because a checker status had trailing-tail behavior | Withdrawn: the owning addendum requires writer false-success with artifact corruption; this incident does not establish that class. |
| FlowReview | A raw worker exit 4 necessarily violates a reserved-code contract | Withdrawn: exit-4 exclusivity is not promised by the generator, and raw worker results are logged. A distinct worker/config class is a design option; do not import the loop pack's separate rule. |
| PackReview | The headless CLI recipes were never probed | Withdrawn after checking the archived 2026-10-06 four-CLI re-probe and private receipts. Do not erase observed slots to `UNKNOWN` or launch providers to repair a rejected claim. |
| PackReview | Risk in Next Action proves a linter implementation defect | Declined as a scope expansion: Goal/Assumptions scan scope is explicit and keyword misses are not approvals. The probe with production credential deletion only in Next Action passed; widening the scanner requires an owner design decision. |
| TestReview | Later cheatsheet overlap invalidates all committed holdout regression gates | Withdrawn: R8 requires fresh-before-tune evidence; committed seeded fixtures are disclosed regression guards, not blind efficacy measurements. |

### Qualified observations

| Source | Observation considered | Disposition and next allowed interpretation |
| --- | --- | --- |
| RoadmapReview | E-5 acceptance closed over an unmet oracle | **Unverified.** The recorded FAIL preceded an owner-authorized oracle re-pin and later exit 0; a contemporaneously unmet acceptance oracle was not established. No trigger is activated. |
| RoadmapReview | S3 and July H3/H4 are missing from aggregate discovery | **Navigation gap only**, retained as F16; owning specs and dormant guards exist. |
| TestReview | CI is green on excluded-only root changes | **Suite skipped**, retained as F10; remote branch-protection/merge behavior is untested. |
| RoadmapReview | TASK-001 dry-run must count as a real invocation | **Not established.** The usage convention excludes stub/rig template maintenance; do not inflate recurrence without artifact-use classification. |
| RoadmapReview | Flow-pack size cadence is dead policy | **Unreconciled recorded exception.** Cadence still states a 20,000-character ceiling; the runbook records 31,172/28,518-character flow packs and user-directed maintenance. The checkpoint owns lint-tier treatment; no threshold increase or contract trimming is authorized here. |
| PackReview | Optional request text must have a trace-linter CLI parameter | **Design/documentation question.** An optional skill-level human/agent input does not necessarily promise an emitted CLI API; no new consumer is created. |
| PackReview | Mixed machine/display names receiving alias treatment prove a bug | **No demonstrated harmful outcome.** The observed extra fields still populate correctly; naming purity is not a consumer-visible failure. |
| IntentReview | Glossary L1/L5 summaries contradict dispatch routing | **Navigation clarity only.** The canonical workflow and descriptive main-surface tables use different abstractions; no misroute was demonstrated. |
| TestReview | Static eval silently skips missing files/unknown conditions | **Reporting limit.** Score output reports skips; links/index gates cover the checked repository. No gating or semantic-quality promise was established for this scorer. |
| TestReview | Old feature-card verification dates and short dependency lists prove failure | **Not established.** Dates are historical unless claimed fresh; the inspected code remains standard-library. No dependency lock or ritual date refresh is justified. |

## Intent and roadmap traceability

| Requested area | What was checked | Result / unchanged boundary |
| --- | --- | --- |
| Whole project | Published templates, composer CLI, installation functions, trace checker, route hard gates, cross-surface documentation | Reachable defects and drift retained as F01–F18; review complete, repairs not started |
| Roadmaps | Whole-project plan/roadmap, October 11 runbook, skill-surface and improvement plans, owning dormant specs and trigger addenda | F15/F16 and qualified size/trigger observations; missing usage remains `unknown`, not zero; no early checkpoint decision |
| Intents | North star, authority precedence, nine-core bounded routing, opt-in registered packs, installed-skill self-containment, no-owned-runtime declarations | Design remains coherent; primary mismatch is existing contract versus delivered consumer, not a mandate for another skill/runtime |
| Tests | Extracted-template consumers, semantic versus incidental assertions, policy fault controls, platform compatibility, trigger coverage, independent oracle scope | Substantive consumer tests exist but miss traversal aliases, folded YAML, zero-survivor quorum, absent policy keys, and declared Python compatibility; F02's current test pins the bug |

### Declined to Judge

- **Actual-host isolation, model utility, and skill efficacy:** not measured by trusted synthetic probes; ruling owners are the TEST-001 host owner and campaign/human acceptance owners.
- **Remote branch protection and merge permission:** workflow scope only was inspected; ruling owner is the repository/CI administrator.
- **Early checkpoint outcomes, pack merge/demotion, or new admission:** existing user-owned decisions and date/event gates; this review grants none.
- **Historical vendor/survey behavior as current adoption evidence:** no external refresh performed; a future adoption owner must refresh the relevant pin before relying on it.
- **Next Action risk-scan widening:** a separate owner design choice, not a demonstrated violation of the declared Goal/Assumptions scanner.

## Candidate Adoption Ledger

The user's recording request supplies approval for bounded documentation capture and worthy in-place evidence promotion. It does not approve executable repairs, new agent rules, new skills/packs, host adoption, or a campaign.

| Candidate | Recurrence / source | Destination and decision | Rejected alternative / falsifier |
| --- | --- | --- | --- |
| WPR-P1 — shipped-template drift despite correct prose | Prior September template probes plus F01/F05/F06/F07/F09's independent consumer paths | **Amend existing durable-lesson evidence** in PROJECT_KNOWLEDGE; non-authoritative project-design judgement, approved for this recording | No new skill; the current implementation/review verification contracts already cover runtime and consumer checks. Revisit if the alleged drift is refuted at the pinned consumer. |
| WPR-P2 — semantic retention outranks fence/length success | F02; existing minimality Safety Floor and implementation consumer-map/test-adequacy rules | **Reuse existing skills**, record the concrete defect and proposed semantic regressions here; no skill edit | Another generic testing clause would duplicate operating guidance while leaving `_strip_examples` broken. Reopen only on a demonstrated missing workflow step rather than missing implementation coverage. |
| WPR-P3 — missing inputs/policy must not produce success-shaped output | F04/F08/F09/F14; prior [RV-08 queue-read false success](recent-changes-review-handoff-2026-10-07.md#rv-08-p2-canonical-queue-read-failure-is-treated-as-empty--fixed); existing failure-preservation and no-silent-default contracts | **Targeted existing-consumer repairs + developer-only behavioral regressions**, pending a repair request at recording time; not a new verifier or promotion candidate | No wrapper, retry layer, provider fallback, new verifier surface, or shipped runner; falsifier is a valid current consumer proving the alleged failure absent. |
| WPR-P4 — representation and compatibility contrasts | F01/F03/F07/F11; existing consumer-map and risk rules | **Targeted contract-consumer regressions**, pending repairs; retain exact contrasts in this record | No general YAML dependency or platform abstraction selected in a recording turn. A narrower supported contract needs deliberate migration, not silent narrowing. |
| WPR-P5 — aggregate documentation needs owning-disposition pointers | F15/F16/F18; existing roadmap/spec ownership | **Record open documentation work and add a discovery pointer**, without closing the inventory/count defects | No scheduling redesign, new gate, or dormant adoption; correct current navigation and source-bound count claims would falsify the repair need. |
| WPR-P6 — model review is hypothesis generation, not independent proof | Five specialist reports plus withdrawn/qualified claims | **No operating-rule change**; existing reflective-review evidence tiers and coverage dispositions already carry this rule | No sixth reviewer or consensus-count ritual; non-model controls remain the evidence for runtime claims. |

**Promotion metadata:** WPR-P1's source is this dated local review plus the cited prior repository records, not a managed-skill memory or imported vendor procedure. Evidence is tagged as observations and adjudications, not new instructions. Scope is TeaPrompt's author-side template/consumer maintenance. Review/retirement trigger: a source change that refutes a case, a repaired consumer with current closure evidence, or an already-equivalent destination making the evidence pointer redundant. Rollback is removal of the new evidence paragraph/pointer, preserving this dated record and earlier rationale. WPR-P2–P6 add no governing skill text, verifier implementation, or runtime surface.

**Counterargument:** The old green suite and strong existing prose could suggest this is only documentation noise. The six non-model consumer groups refute that for the named runtime cases. Conversely, observed consumer gaps do not establish that more skills help; an existing contract plus the missing implementation/regression is the smaller repair. No paired with/without-skill benefit measurement exists, so this turn makes no such claim.

## Remaining work and repair order

1. **F01 and F02 first:** metadata-boundary escape and deletion of primary instructions. Preserve strict resolution, preflight-before-reserve, semantic safety content, and corrected-run controls.
2. **Executable/gate defects next:** F03–F11 and F14, including repeated-failure ownership and declared Python compatibility. Use the recorded failure cases as behavioral regressions; do not weaken gates or change expected outcomes to obtain green results.
3. **Contract/example clarity:** F12/F13/F17. Define static resolution and definition/reference semantics without creating an owned runner; bring example evidence up to its declared contract.
4. **Documentation/navigation:** F15/F16/F18. Preserve historical pinned literals with dated supersession; source pointers do not activate dormant items.

A finding closes only with the relevant changed consumer exercised against its repair criteria and a current source-bound receipt. Recording, passing unrelated tests, or adding a warning is not closure. Existing acceptance/invariant/security oracles remain read-only unless separately approved for Human Review migration.

### External gates — unchanged

- **TEST-001:** requires a qualified designated host, accepted real-input authority consumer, pinned scorer executable and golden-ledger procedure, actual-host protected evidence, named host/capture and leak-audit owners, and passed controls. The rejected historical fixture-only reference is not a substitute.
- **Stage-1 / TEST-002–004:** require an explicit campaign envelope, separately enforced session/model/reserve/spend caps, named roles, memory-source digests, and worker/capture isolation. A zero-dollar budget is valid when approved; zero spend alone is not authorization.
- **2026-10-11 checkpoint:** remains date-gated and user-owned. Source and invocation evidence are refreshed in that checkpoint session; no early proceed/hold/close, merge, demotion, or admission is recorded here. Size/lint-tier decisions remain with the owning checkpoint.
- **Git delivery:** no commit or push is authorized by this recording request. Private campaign manifests and evidence remain outside repository publication.

## Falsifiability and continuation

- The record is incomplete if any of F01–F18, the six probe groups, nine withdrawn claims, ten qualified observations, a source binding, or a named external gate is lost.
- A runtime finding is refuted only by a source-bound contrast at its triggering input showing the consumer satisfies the actual contract; a green general suite or convincing rationale is insufficient.
- A static/spec finding is refuted by an authoritative supported grammar/definition or current source that resolves the claimed mismatch, not an invented implementation.
- This promotion is too heavy if it adds skills, runners, dependencies, agent authority, or duplicate generic rules instead of preserving evidence in existing destinations.
- Continuation starts from this ledger and current sources. Source changes can stale a reviewed claim; a documentation-only pointer does not retroactively rewrite historical receipts. Do not repeat a probe simply to confirm the recorded failure before acting on an authorized repair.

## Repair closure (2026-10-09, later same day)

The user authorized repairs after the recording turn. The initial closure was recorded at `a4b238e`; delayed feedback subsequently identified residual F04/F10 gaps and an F07 coverage gap, now addressed below. The "all 18 remain OPEN" statements above are historical at-recording text. Original source bindings remain pins of the *reviewed* revision, not of the repaired files.

| Finding | Repair | Closure evidence |
| --- | --- | --- |
| F01 | `_fold()` rejects `..` before identity comparison; refusal runs before any output reservation | `test_arm_blinded_eval_consumers.py` traversal/refusal/corrected-run controls |
| F02 | `_strip_examples` removes explicitly marked Example sections while retaining fenced primary instructions | Real `core-short`/`spec-writer` CLI retention plus marked-example regressions; no substantive example removal or token-saving claim for the seven primary directories |
| F03 | `>`/`|` block scalars parse into field values; other scalar markers are refused as unsupported, never read as content | `test_router_trace_linter_scaffold.py` folded/literal parity tests green |
| F04 | Both boolean policies required and typed; mandatory hard-gate threshold required; both numeric thresholds (when present) exclude bool and lie in `[0,1]` before float conversion; trace-field list nonempty and supported | Actual baseline/repaired CLI comparisons: missing threshold/trace fields and invalid optional threshold refuse at exit 2 without publication; valid, omitted-optional and boundary controls retained |
| F05 | Fan-out zero-survivor synthesis via guarded loop + `[zero-survivor]` note; holds evaluated before quorum | `test_fanout_zero_survivor_*` green in `test_flow_generator_consumers.py` |
| F06 | All five templates carry `FAIL_SIGS`/`RETRY_REASON` repeated-failure discipline; ledger defaults beside resolved `STATE`, inside-`STATE` refused at exit 4 | refusal/retry/correction tests green in `test_flow_generator_consumers.py` |
| F07 | Eager union annotations removed; Python 3.9+ declared; floor tests select only a live 3.9 interpreter; CI installs 3.9 and 3.10 | Actual extracted orchestrator/DAG run on Python **3.9.24**, dispatch and reach acceptance; empty command holds at 4 without redispatch; remote CI not observed |
| F08 | Missing indexed input exits 1 before output publication; destination-write errors have independent coverage | Real copied CLI/index missing-source controls retain stdout/fresh/existing-file refusal; valid composition into a permission-denied existing destination exits 1 without success output or changing its bytes |
| F09 | Install helpers propagate cd/mkdir/cp/ln failure and refuse zero-core sources before creating the destination | Copy/symlink missing-source, empty-source, nine-core and replacement-refusal controls |
| F10 | Workflow has no path exclusions; local hook has no file filter and `always_run: true`; main push/PR scope retained | Workflow YAML parsed and `pre-commit validate-config` passed; actual outside-library hook invocation recorded in follow-up verification; remote branch protection remains untested |
| F11 | Hazard token boundaries exclude the `author` family; field-scoped deferral; alias rationale seat; low-risk skipped forms pass | `test_low_risk_documented_forms_pass_without_weakening_hazards` + retained contrastive matrix green |
| F12 | Static shell grammar defined: `&&`-separated simple commands, leading `NAME=value`, `cd` directory context; unsupported syntax is refusal, never execution | `test_acceptance_join_golden_contract_consumers.py` (4 tests) green |
| F13 | Golden-ledger rows carry completion/status_reason/scorer_executable/scorer_revision; `score:null` means unscored | same test file green |
| F14 | Explicitly empty/whitespace `AGENT_CMD` holds as configuration failure, never falls back to a provider | All five template consumers; additional orchestrator/DAG floor smoke exits 4 with zero new dispatches |
| F15 | Dated October supersessions and pointers added; test-pinned five-pack literal untouched | `test_september_skills_review_record.py` green |
| F16 | S3 and July H3/H4 discovery pointers added preserving triggers/owners | `test_dormant_*` suites green |
| F17 | Definition seats (heading, ID-led list/table row, `Requirement:`/`ID:` line) versus references, including `covers:` | same contract-consumer tests green |
| F18 | Compare-vs-regenerate wording corrected to the actual `save_benchmark`/`validate_benchmark_fixture.py` split; R8–R13 pointers updated | `test_quality_gates_summary.py`, `test_validate_benchmark_fixture.py` green |

Repair-turn integration notes: a new `FAIL_SIGS` default initially shipped a `$STATE/../` literal that violated the repo-wide "no parent-relative paths in shipped bodies" invariant — the default now derives from `dirname "$(cd "$STATE" && pwd -P)"` (identical sibling-of-`STATE` semantics, no `../` literal). The doc-anti-drift pytest floor rose to 1,626 from the new regression files. A repeated-failure hold (exit 3) is a driver decision and is never quorum-tolerable, including under `MIN_OK=0`.

Final receipt for this turn: `make all` → **1,626 passed, 0 validator errors, all three routing evals passed** after `generate_index.py`. External gates (TEST-001 host, Stage-1 campaign, 2026-10-11 checkpoint) remain unchanged and unclaimed by this repair turn.

## Delayed-review residual closure

This follow-up stays inside the authorized existing-consumer repair. No new skill, runner, dependency, route tuning, fixture threshold, host/campaign authorization, or early checkpoint outcome is introduced.

### Advisory dispositions

| Delayed claim | Disposition and evidence |
| --- | --- |
| FAIL_SIGS reorder must fix bash defaults and prose while preserving sibling placement | Already repaired: three bash defaults derive from resolved `STATE_ABS`; prose names the sibling; nested-STATE and explicit inside-STATE refusal controls remain |
| The two earlier full-suite failures probably came from Python 3.9 execution | Refuted by the retained failure names: lesson wording assertion and parent-relative-path invariant, not floor execution |
| QUALITY_GATES lost list items and a comma made the pytest floor parse as 626 | Already restored before this follow-up; full list/tail retained, comma-free live floor refreshed from actual collection |
| GeneratorRepair's five failures are test-fixture bugs | Already fixed before this follow-up: one-call markers and lazy fixture selection; no prompt-construction change |
| CI and the oldest-runtime helper can miss the declared 3.9 floor | Valid coverage gap; repaired and exercised as F07 above |
| The earlier F08 smoke can fail before reaching a missing prompt | Evidence weakness addressed with a copied real CLI, live index, two-file positive control and named `spec-writer` refusal in all three output modes |
| F02 retention passes without demonstrating actual example compression | Qualified: seven primary directories have no marked Example headings; `spec-writer` body is identical and `core-short` differs by one whitespace byte. The mode label remains; no meaningful token savings claimed |
| F04 still defaults an omitted threshold and accepts an empty trace-field list | Valid residual defect; repaired and reproduced before/after as F04 above |
| F10 still omits Markdown and other consumed inputs | Valid residual defect; input filters removed rather than expanding another fragile allowlist |
| F01 should allow existing-ancestor `..` and ValueError might escape | Not adopted: the repair acceptance explicitly allows traversal rejection, the live contract documents it, and the caller catches ValueError as exit 4. Narrowing it is not necessary for this repair |

### Evidence and limits

- Focused policy/composer/lesson regressions: **65 passed**. Flow-generator regressions: **91 passed**, no floor skips; both Python templates executed on real **3.9.24**.
- Actual policy CLI comparisons bind to baseline `a4b238e` and the repaired source below. The missing threshold previously published `0.70`; omission now holds before reporting. A 320-digit numeric threshold previously raised OverflowError; comparison before conversion now yields configuration exit 2. NaN, infinity, bool and out-of-range controls remain refusals.
- Actual composer smoke used a copied live index and CLI, not `cwd` substitution or an absent-index shortcut. A valid two-input control precedes removal of `spec-writer`; stdout stays empty, a fresh file is absent, and a previous file is byte-preserved.
- The incidental exact-English lesson-trigger assertion was **removed**, not re-pinned. Lesson/evidence registration and deferred-authority guards remain.
- Browser lifecycle: managed-tab inventory was empty; scoped `browser.close(all=true, kill=true)` released zero tabs and targets only this process's spawned applications. No global Chromium kill or user-browser shutdown was used.
- Verification tooling: Python Eval backend unavailable; equivalent Python subprocess smoke ran through the retained JavaScript Eval kernel. Python LSP unavailable. Ruby YAML parsing succeeded despite two local native-extension warnings; hook schema validation exited 0.
- Consumer map: direct evaluation API and actual CLI, stdout/file composition, exact-floor/current templates, CI/hook configuration, documentation and generated index are checked here. Historical receipts keep their original pins. Remote Actions, branch protection, hostile-worker isolation, model utility and host/campaign execution remain explicitly untested.
- Twin sweep: the route-fixture validator also reads trace-field defaults but already rejects missing required fields; it was left unchanged. The faulty threshold fallback and permissive floor-selection helper have no other executable sites.
- Final outside-library hook: `pre-commit run make-all --files review/final-report.md --verbose` **Passed**; **1,653 passed**, zero validator errors, all three routing evaluations at **100%**. Nine lint warnings and 35 record warnings remain. The command and external limits are retained in [the final report](../../review/final-report.md#whole-project-repair-delayed-advisory-follow-up).

### Follow-up source bindings

These SHA-256 hashes bind the runtime/configuration sources and regressions exercised by this follow-up, not the original review. Unchanged composer source is included because the missing-source smoke executes it.

| Source path | Follow-up SHA-256 |
| --- | --- |
| `.github/workflows/python-tools.yml` | `112129b6b24f334565b3d2de144fd7b13abbf7c9b472a56e3713d391d1e60fb5` |
| `.pre-commit-config.yaml` | `56387c083107a4728a5bb3b09a4173ea0baa5659764001a546e93454e968c1ab` |
| `reflective-prompt-library/plans/route_paraphrase_eval.py` | `1e7caddfc24e0e821a13df418cd7bf915a47fd51a4bb314e1ed4cdcb96f856ae` |
| `reflective-prompt-library/plans/prompt_composer.py` | `4645894f939ca1bd303681cc8fe5d5cf2823c542e620d44d43e6de2a9103c055` |
| `reflective-prompt-library/plans/tests/test_route_policy_consumers.py` | `908afda24bbd478b830e15d6f082293207a59294cc9a52b9cf6c39ad1de0a888` |
| `reflective-prompt-library/plans/tests/test_flow_generator_consumers.py` | `89a09592980d5ad721f0d18f9bc41f93ebcc86a8370e1bbea899eb0f6dcadaa2` |
| `reflective-prompt-library/plans/tests/test_prompt_composer.py` | `8ec77e0fbafe1fa20ab3c096d698b7af29b2b6ba4f54c0b3f7e1a3ae575ac715` |
| `reflective-prompt-library/plans/tests/test_harness_intent_drift_rethink_record.py` | `8153238f1fad5f1fc56e7116a43cd76f49b5d38eb451805092d7f8684e03af4f` |

## Remaining-advisory closure (2026-10-09)

The earlier **1,626** and **1,653** gate receipts and their source bindings remain historical. This later follow-up changes only optional numeric-threshold validation and developer regression coverage; fixture thresholds, routing rules, the optional `0.95` default and all external gates are unchanged.

| Advisory | Disposition | Observable evidence |
| --- | --- | --- |
| Mandatory oversized threshold can still overflow during conversion | Stale: original-value range validation already precedes conversion | Retained mandatory 320-digit CLI control exits 2 without publication or traceback |
| Optional aspirational threshold converts without validation | Valid; reuse the existing numeric/range guard before conversion | Before: valid control exits 0, oversized optional value exits 1 with OverflowError. After: oversized value exits 2 with a configuration diagnostic, no result and no traceback |
| Missing-source coverage replaced the independent output-write-error case | Valid coverage gap; restored without removing missing-source controls | Deterministic PermissionError regression checks exit 1, empty stdout and preserved prior bytes; actual CLI control succeeds before the permission-denied destination case |

### Current consumer evidence

- Policy CLI: four positive controls (valid, optional omitted, optional zero, optional one) exit 0 and publish; seven invalid controls (optional oversized, bool, string, infinity, negative, above one; mandatory oversized) exit 2 without publication or traceback.
- Composer CLI: successful two-input composition precedes a real permission refusal at a `0400` existing destination under uid 502. Refusal exits 1 with a destination diagnostic, empty stdout and unchanged prior bytes. This proves the permission-refusal path, not atomic recovery from a partial write or disk exhaustion.
- Policy/composer regressions: **71 passed**, including direct-API nonfinite checks for both numeric fields and the retained three missing-source CLI output modes. Final repository gate: `generate_index.py && make all` passed with **1,665 tests**, zero validator errors and all three routing evaluations passed. Nine lint warnings and 35 historical-record warnings remain.
- Consumer map: direct evaluation API, actual policy CLI, configuration defaults/boundaries, composer write-error branch and actual composer CLI are covered. Discovery regeneration and documentation/index checks are separate post-receipt verification steps. Remote CI, host isolation and comparative/model efficacy remain explicitly untested.
- TWINS: searched unchecked aspirational_route_consistency_target float conversion - found 0 other sites: none.

### Current source bindings

These hashes bind the source exercised by the actual smoke, not the previous committed follow-up. The unchanged composer source is included because its separate write-error path was executed.

| Source path | Current SHA-256 |
| --- | --- |
| `reflective-prompt-library/plans/route_paraphrase_eval.py` | `67631efb84d9dd31f19f4f11d0ccfaeeb219bbf46ebeb9e247c4c26170580104` |
| `reflective-prompt-library/plans/prompt_composer.py` | `4645894f939ca1bd303681cc8fe5d5cf2823c542e620d44d43e6de2a9103c055` |
| `reflective-prompt-library/plans/tests/test_route_policy_consumers.py` | `86a5ddeab454d8bc0f9785fa202f7d78f7064e923702288e385d747fa2497598` |
| `reflective-prompt-library/plans/tests/test_prompt_composer.py` | `9ad6563cc38374586facd984b0c388d352d1dd5fcf14407749bbf36cdc9e8d91` |
| `reflective-prompt-library/skills/governed-delivery/SKILL.md` (H12 assessment) | `43528a06eb02b4ce78ce7994c3b9049f7b00ffdadecd1fd8d2d90af087a166d5` |
| `reflective-prompt-library/plans/tests/test_governed_delivery_adoption_state.py` (H12 assessment) | `a85ecdc1d83301d2918a3331a4e08ba2bd7ce63ce467ceb24489980b613e67f3` |

### Roadmap continuation and owner gates

This is maintenance continuation, not the date-gated checkpoint. The owning [roadmap](whole-project-roadmap-2026-07-11.md), [flow roadmap](flow-control-roadmap-2026-07-11.md), [runbook](checkpoint-2026-10-11-runbook.md), and [dogfood plan](skill-dogfood-test-plan-2026-10-08.md#execution-readiness-and-risk-gate) retain their existing authority and gates.

| Reachable area | Current disposition / next action |
| --- | --- |
| Standing maintenance | Current consumer repairs, source-bound closure, Decision Index and test floor updated; final repository gate passed. Post-receipt discovery/documentation verification remains a separate step. No routing tune, adoption collision or pack-template edit in this follow-up |
| T1–T4 and flow F3 | Completed dated outcomes remain completed; F3's template-evolution queue is empty. Do not re-adopt T2 or repeat completed repairs as new invocation evidence |
| Flow F4 source watch | No new host-feature reliance or demotion claim is made. The October 1 source-only re-check remains dated evidence, not an October 9 refresh; re-check all six primary-source rows in the checkpoint session before taking a branch |
| October 11 checkpoint | Still date-gated; no outcome file or early P6/GD/G9-AS9/H5-H6/lint-tier decision created. The operator must refresh sources, measurements and invocation evidence, preserve unknown-vs-zero, and record every owning agenda outcome; absence after the date activates the existing deadman consequence |
| TEST-001 | Held pending accepted/pinned real-input consumer and scorer/golden-ledger procedure, authenticated actual-host evidence, named capture/leak-audit owners and passed controls. Neither the rejected historical `64b4556a` build nor fixture repair receipts supply those inputs |
| Stage-1 / TEST-002–004 | Held pending the separate campaign grant, enforced session/model/reserve/spend caps, roles, memory/capture evidence and tool-using worker isolation. Zero approved spend is not by itself an envelope grant |
| Other dormant candidates | Each named trigger/direction gate remains separate. New guard passes may prompt H12 consideration, not blanket H1–H8 adoption; H5/H6 remain separately seated at the checkpoint. No claim that watched-source guards prove the absence of external trigger events |

### H12 triggered guard-pass consideration

The assessment below is the 2026-10-09 state. Its separately authorized H12-GD repair is recorded in [the dated successor](#h12-gd-semantic-developer-check-repair-2026-10-10); the original seven-guard branch remains Held.

The [owning H12 row](skills-september-concepts-review-2026-09-16.md#candidate-adoption-ledger) names the next guard pass. This pass considered its two branches separately; it does not adopt or close the original Held row, change protected oracles, or expand the nine-core/ten-pack registry.

| ID | Candidate branch | Current assessment | Disposition / ruling owner |
| --- | --- | --- | --- |
| H12-GD | Nine static contract templates | Source review maps all nine bodies to `test_gd2_to_gd10_contract_set_has_nine_templates` at lines 208–211. A throwaway execution safely parses all nine YAML blocks as mappings, then confirms the existing heading guard accepts the baseline, a hollowed contract set and an `acceptance-record` changed to `closed: true`. This demonstrates the heading guard's discrimination limit, not a defect in today's parsed baseline or a whole-suite mutation result | Re-litigation executed; adoption remains Held. Maintainer owns an accepted developer-check scope for parsed fields/defaults/reference bindings; no new incidental English phrase pins |
| H12-fragments | Historical seven-guard list | The durable record retains the count and references `L6RecordsGuards`, but not the itemized inventory; its packet was deleted after synthesis, and `history://L6RecordsGuards` is not registered here. Current source examples exist in AGS (`enforce` / `host`), artifact-promotion (`fails closed` / `prompt-injection` / `Memory writes`) and the later Agentflow 8.3 addendum (`unchanged` / `counterargument`). They are examples, not a reconstructed original seven | Original seven-item coverage remains unresolved and Held, not silently replaced with seven arbitrary matches. Maintainer owns the historical inventory or a separately accepted current assessment scope |

The census covers `intent-record`, `oracle-manifest`, `task-packet`, `failure-log`, `verification-plan`, `evidence-ledger`, `acceptance-record`, `envelope` and `gate-retro`. Neighboring gate/anchor assertions and index staleness do not establish every template body's semantics; generated-index freshness cannot substitute for a semantic oracle. Short machine fields and statuses are not interchangeable with incidental prose fragments.

Review decision: the candidate has a demonstrated heading-guard coverage gap and an explicitly bounded historical-inventory limit. A prospective repair should discriminate hollow/malformed objects, unsafe defaults and severed references at a real consumer; extending exact-English pins is not the chosen remedy. No guard redesign or host-enforcement claim is landed by this maintenance repair.

### Verification tooling limits

The initial H12 probe omitted the plans import path and could not load `validate_skill_examples`; correcting the harness import path produced the observed result above. Ruby safe parsing succeeded with the same two local native-extension warnings. Actual Chromium DOM/layout inspection retained all 18 findings, the new closure and no horizontal page overflow at 1200×800. PNG and JPEG screenshot helper calls both timed out; pixel capture is therefore unverified, not silently recorded as visual proof. The preview is an owned loopback process, not a user-browser session.

## H12-GD semantic developer-check repair (2026-10-10)

**Decision and scope:** the maintainer explicitly selected “Repair H12-GD + commit.” The approved repair covers required fields, safe defaults and reference slots in the nine existing YAML templates, through the developer governance consumer. It does not authorize changing protected acceptance oracles, the historical seven-guard inventory, host/campaign grants or the date-gated checkpoint.

`plans/validate_governance.py` now safely parses the real fenced Contract Set, requires each named template once, and checks typed top-level and nested fields. Duplicate/non-string YAML keys, malformed objects and heading/fence decoys cannot substitute for a valid body. `PyYAML>=6.0` is declared in `requirements-dev.txt`; CI already installs that development file. The installed skill and its stdlib-only host preflight remain byte-unchanged.

| Template | Consumer-visible protection |
| --- | --- |
| `intent-record` | Named intent, unknown owners and required Human Review slots; initial status remains unsigned |
| `oracle-manifest` | Version slot and oracle name/class/owner/seal/change protocol; authoritative specimens cannot default to no seal |
| `task-packet` | Version, State Ledger, oracle reference and file slots; missing acceptance stops and repairs |
| `failure-log` | Oracle/error-class/surface signature, typed correction status and rollback/strategy-change/escalation exits; no identical-retry exit |
| `verification-plan` | Typed channel/independence and compatibility slots; mandatory non-model rule and an independent non-model specimen; self-assessment cannot claim independence |
| `evidence-ledger` | Separate claim/source/attester, supported freshness kind and date slot |
| `acceptance-record` | Version, named accepter, oracle reference and product-evidence slots; initially open and without pre-claimed evidence |
| `envelope` | Budget/pause/kill/accepter slots, task-declared failure limit, no pre-granted sinks and existing L1–L6 choices |
| `gate-retro` | Named gate and typed initial receipt flags; policy change remains separate from activation |

Version/reference checks concern required, string-typed **unbound template slots**. They do not resolve live artifacts, establish freshness, authenticate an oracle or validate an instantiated host contract. Editable text and legitimate enum choices are not exact-English prose pins.

### Evidence actually exercised

- Before-fix actual `validate_governance.py` CLI: baseline and equivalent-YAML controls exit 0; all **14 invalid inputs** also incorrectly exit 0, including one hollow body for each of the nine templates, `closed: true`, a removed oracle reference, pre-bound version, duplicate key and malformed YAML.
- Final actual CLI: **20 controls**; four valid inputs exit 0, and 16 invalid inputs exit 1 with diagnostics and no traceback. Additional controls cover duplicate headings, a Contract Set hidden in an example fence, and standard tilde/four-backtick YAML fences.
- Final focused developer suite: `test_governed_delivery_adoption_state.py` plus `test_validate_governance.py` — **100 passed**. Coverage includes missing nested owners/class/seal/change protocol, quoted/numeric boolean impostors, empty/mistyped oracle specimens, reference/version pre-binding, and an unsafe YAML object tag that cannot execute its marker expression.
- Live repository governance CLI: **19 valid skills, 0 invalid**. Full repository gate: `generate_index.py && make all` passed with **1,733 tests**, zero validator errors and all three routing evaluations passed. Nine lint warnings and 35 historical-record warnings remain. Final documentation/index checks follow this receipt update; the full gate is not inferred from focused tests.
- Chromium DOM/layout inspection of the review, final report, QUALITY_GATES, Decision Index and September successor passed at 1200×800 without horizontal page overflow; the review still exposes all 18 historical findings. The viewport screenshot exceeded the 20-second outer deadline, so pixel capture remains unverified. The owned tab was released; no user-browser session was used.
- TWINS: searched heading-only `assert f"### {name}"` template guards and the retired GD heading-guard symbol - found 0 other executable sites: none. The surviving symbol mention above is historical evidence, not a live guard. This search does not reconstruct H12's seven historical fragments.

### Exercised source bindings

| Source path | SHA-256 |
| --- | --- |
| `reflective-prompt-library/plans/validate_governance.py` | `916dff2b1499d7e49faa1d4fe0ff02f262c07b48f8bd181314b6083eae4f39ca` |
| `reflective-prompt-library/plans/tests/test_governed_delivery_adoption_state.py` | `6f0c4d92ff9e3dd146d75cbd0f5e801dacc1f3c8e4fa9d63bdb23a0b3b42e07e` |
| `reflective-prompt-library/requirements-dev.txt` | `a765e0db320728c043e4ed8a606a2f710cb350f50308323f6ab08f363bb1c96c` |
| `reflective-prompt-library/skills/governed-delivery/SKILL.md` (unchanged) | `43528a06eb02b4ce78ce7994c3b9049f7b00ffdadecd1fd8d2d90af087a166d5` |

### Disposition, limits and next action

The approved H12-GD consumer repair is implemented and its negative/positive paths are verified. The original September H12 row and counts remain historical; the unresolved seven-guard branch remains Held, with its inventory or separately accepted scope still maintainer-owned. No arbitrary current fragments replace that inventory.

Consumer classes: direct validator API and CLI are covered; `make validate`/`make all` reach the same checker; CI's existing requirements-file install supplies the development dependency; dated records and generated discovery metadata carry this scoped successor. Installed skill contracts, host preflight, registry membership, actual-host authentication and campaign caps remain outside the change.

TEST-001 and Stage-1/TEST-002–004 remain Held under their existing owner/evidence/grant gates. The October 11 checkpoint remains date-gated; no early outcome, demotion or policy activation is recorded. No provider/model call or push is part of this repair. Remote CI and host enforcement remain untested.

## H12-GD advisory follow-up and checkpoint preparation (2026-10-10)

**Scope:** continuation of the explicitly approved developer repair and scoped
commit, not a new runtime/campaign grant. The earlier 100/1,733-pass receipts
and source bindings above remain historical. This follow-up fixes a surviving
authority-default gap, closes the clean-environment/setup evidence gap and
prepares the eleven checkpoint inputs without writing an outcome.

### Advisory dispositions

| Claim | Current ruling and action |
| --- | --- |
| Developer-only oracle specimens pass as authority | Valid. The developer consumer now requires at least one `class: authoritative` specimen with a non-`none` seal. Legitimate developer specimens remain valid alongside that sealed authority. Actual CLI contrasts exercise both classes. |
| Regex crosses sections or duplicate headings substitute for templates | Stale for the current line-oriented, fence-aware consumer. New regressions and actual CLI controls cover removal of every complete template section, unsupported `yml` fences and a shadowed unsafe envelope; the safe YAML parser is retained. |
| PyYAML missing from standalone/local-hook setup | Valid setup drift. One `PyYAML>=6.0,<7.0` declaration lives in `plans/requirements.txt`; `requirements-dev.txt` includes it. CONTRIBUTING, VERIFY and the system hook require the installed, active developer environment. |
| CI installs only pytest / author tooling must be stdlib-only | Wrong premise. The current workflow installs `requirements-dev.txt`. The stdlib-only boundary is the installed host checker, not author-side governance validation. CI configuration is inspected; remote execution is not claimed. |
| Clean Python 3.9 was never exercised | Valid evidence gap. A new virtualenv without system/user site packages installs the documented requirements and runs the actual consumer plus focused regressions. |
| Replace PyYAML with a custom YAML subset parser or add a silent import fallback | Declined. The existing safe loader parses the real nested templates. A parallel parser or optional import would hide setup failures; the dependency stays developer-only. Ruby is not a consumer dependency. |
| The floor smoke reveals eager `tuple[...] \\| list[...]` annotations | Valid existing harness defect. Both eager helper annotations now use `typing.Union`; deferred annotations elsewhere remain unchanged. |
| Checkpoint preparation is reachable | Completed as a [dated read-only packet](checkpoint-2026-10-11-preparation-2026-10-10.md), with source/usage/EOF limits. No P6 branch, demotion, G9 ruling or H5/H6 adoption is taken. |

The checkpoint scout's proposed zero-solo loop count and early P6 branch were
not adopted: S2/S3 composite tasks include separate script responsibilities.
Its 95-entry figure is **inclusive** of July 11; the strict-after count is 84.
Its blanket absence of GDR observations is also rejected: the October 6 ticket
preserves granted narrow refuter receipts, without proving the full current
actual-model campaign. The durable packet carries these distinctions.

### Evidence actually exercised

- Before repair, the developer-only regression failed while 35 other selected
  controls passed. The surviving gap was not inferred from a static heading.
- Python **3.9.24** virtualenv: `include-system-site-packages = false`, user
  site disabled, pytest **8.4.2** and PyYAML **6.0.3** resolved inside the venv
  by the documented requirements-file install.
- Actual floor CLI smoke: **27 controls** — five valid controls accepted,
  22 invalid controls refused with diagnostics and no traceback. Controls
  include developer-only/mixed authority, each removed section, unsupported
  fences, a shadowed unsafe envelope and standard equivalent YAML/fences.
- Focused governance/adoption suite: **112 passed**. Live governance CLI:
  **19 valid, 0 invalid**. Dormant-watch/conditional/calendar checks:
  **64 passed**; the checkpoint outcome file remains absent.

TWINS: searched eager PEP 604 type annotations without postponed evaluation - found 1 other site: `plans/tests/prompt_eval_helpers.py::assert_registry_matches_library_glob`; both helper sites are repaired. An AST sweep parsed all 129 Python files under `plans/` and found no remaining eager union annotation.

### Final repository and rendered-record receipt

- Actual `pre-commit run make-all --all-files --verbose`, with the clean
  Python 3.9.24 environment first on `PATH` and `PYTHONNOUSERSITE=1`,
  returned **Passed**. Its `make all` ran **1,745 tests**, eight validators
  with **zero errors**, and all three routing evaluations passed. Nine lint
  warnings and 35 historical-record warnings remain.
- Nine disposable Chromium Markdown previews passed content and layout
  inspection at 1200×800 without horizontal page overflow. Direct CDP
  `Page.captureScreenshot` captured a **198,683-byte PNG** of the preparation
  viewport, which was opened and inspected. Earlier Puppeteer screenshot
  timeouts remain historical; this is local documentation preview evidence,
  not deployed-host verification.
- An earlier full-gate attempt had 1,744 passes and one record-hygiene failure:
  the new packet lacked the required Evidence heading. The heading and
  source-access dates were corrected; the successful hook receipt is separate.
- Session receipts: `local://h12-followup-cli-2026-10-10.json`,
  `local://h12-followup-2026-10-10.json` and `artifact://2700`.
  The hook changed none of the sixteen scoped source/document files.


### Current exercised source bindings

| Source path | SHA-256 |
| --- | --- |
| `reflective-prompt-library/plans/validate_governance.py` | `ef7bb94ab92e3fcc6b683fb71df616cde791cce052f1b25716db77bac94277fb` |
| `reflective-prompt-library/plans/tests/test_governed_delivery_adoption_state.py` | `e7ada2b42be642e5883c0813920ce75ed6085d8006987f3249fc972b7ac9fdff` |
| `reflective-prompt-library/plans/tests/prompt_eval_helpers.py` | `e64b074d8f54cc880120bee53bc6585f5912c99c612c9fcd936cc4ba25c7d727` |
| `reflective-prompt-library/requirements-dev.txt` | `c5d6aa2bbde86b799c5e79a0a81169ea9cd1b3872f7a2b17f3ea5b24fafb7dfa` |
| `reflective-prompt-library/plans/requirements.txt` | `8860aecfb525fbabec6a15bf49f9e48b30d027a16e96c1d55e13c13a0d853872` |

### Consumer coverage and remaining gates

Direct developer API, actual CLI, clean dependency installation and focused
regressions are covered. Make/system hook, final discovery and rendered
records are verified in the final receipt. CI configuration consumes
the same requirements file; remote CI remains untested. The installed skill,
stdlib host checker, registry membership and protected oracles are unchanged.
The source-bounded preparation does not establish absent external use,
independent GD utility, model efficacy or actual-host containment.

The original H12 seven-guard branch, TEST-001 host qualification, Stage-1
campaign and October 11 outcome retain their existing owners and gates.
No model/provider call, runtime adoption or push belongs to this follow-up.

## Reviewed source bindings

SHA-256 hashes below bind the original review, not a future repair or the recording-turn discovery edit. Other cited locations are source observations, not additional hash-bound artifacts. Original source lines remain historical after edits.

| Source path | Reviewed SHA-256 |
| --- | --- |
| `reflective-prompt-library/skills/arm-blinded-eval-harness/SKILL.md` | `8071a47359e761d7507646bbbc9a9dec3edfc3f63ced1bff0efa8eb96b1569af` |
| `reflective-prompt-library/skills/flow-control-generator/SKILL.md` | `6a055fb9c92c1c947644e88a6e367966074cceced97fccecb43bf7aa40074348` |
| `reflective-prompt-library/skills/router-trace-linter/SKILL.md` | `bd75808ce62ed88502b1222425684ae2503bfbdb5bcaad136db7ea181c2ce66f` |
| `reflective-prompt-library/skills/acceptance-join-validator/SKILL.md` | `f02107d205f79161a64c0476df5c91376f64994dc7ec2a2305612c03b3fa742e` |
| `reflective-prompt-library/skills/golden-benchmark-runner/SKILL.md` | `08de636ed72ee2acc34cfa8accfabe066fbf6b0b1b438ae5de3a045bdcc815a3` |
| `reflective-prompt-library/skills/examples/golden-benchmark-runner.examples.md` | `6247a73f4dff5bb8bbbe1c022f111796cdcd9613c826734d3e9897a898225cc3` |
| `reflective-prompt-library/plans/prompt_composer.py` | `79a455c127a70372b068de461b96e4c3386ec157b9adb48bf9bdbee2eb6a7fc9` |
| `reflective-prompt-library/plans/route_paraphrase_eval.py` | `f35662d3f3c899e816a483102973f39aaeef3170d09ad0671cf3e01212e5c729` |
| `reflective-prompt-library/SKILL_INSTALLATION.md` | `f6666196a383855fa30a4a46c4f8e4f90120810d52c1a6e7c3bf332d37260929` |
| `.github/workflows/python-tools.yml` | `028cf58d057749dd216c2e0ffc08cc9dd88d595f4b91e701d26552f600bcb124` |
| `.pre-commit-config.yaml` | `34514cabc97be11d4a5d54a0f878c9af045e1dfe5f6ea983cf8dfb20fd8da00f` |
| `reflective-prompt-library/plans/whole-project-plan-2026-07-11.md` | `98b79a730d6018c0f062f04e73cd1edc20fc362d613c6117ad848a0cd4341706` |
| `reflective-prompt-library/plans/whole-project-roadmap-2026-07-11.md` | `9fd8dce6291959ca67b5ef60631ddc3a9c250d305e00d69bf632e7ab93963803` |
| `reflective-prompt-library/plans/dormant-work-specs-2026-07-11.md` | `4b678cb3b59122b1e760df8ab4062156d5b62973ef35066720f01d7760c922a4` |
| `reflective-prompt-library/plans/flow-pack-usage-log.md` | `7d7fc07cbfdce3e42200d721cf79a75f8b37f2e6804f092bcec300088eb90903` |
