# Four Harness Sources — Selection, Verification, and Promotion (2026-11-13)
Language: English

> **Status: reference documentation and navigation adopted (`H4-DOC1/2`); no Skill, operating-rule, or runtime change.** The owner requested “update docs or skills if worth it” after the four-repository survey. This record makes existing acceptance and promotion boundaries concrete; it does not authorize installation, model calls, benchmark campaigns, or automatic experience-to-Skill writes.

## Research Question and Direct Recommendation

What is worth borrowing from these four different artifact types, and does any expose a missing delivered TeaPrompt contract?

**Keep the source-qualified contrasts; leave Skills unchanged.** Harness² contributes a research mechanism, WalkingLabs a teaching path, Awesome-Agent-Harness a taxonomy/navigation index, and TrishamBP an executable reference implementation. None demonstrated a missing local acceptance duty. Reader utility and installed-agent compliance remain unmeasured; a source record is the smallest useful destination, not evidence that a new workflow is needed.

## Version and Source Identity

Checked 2026-11-13 using `git ls-remote --symref <repo> HEAD refs/heads/main refs/heads/master refs/tags/*`, GitHub release feeds, and detached checkouts. All four release feeds returned `[]`. These are inspected revisions, not claims about later versions.

| Source / artifact type | Branch and immutable revision | Version / reuse boundary |
| --- | --- | --- |
| [google-research/harness2](https://github.com/google-research/harness2/tree/6868817518876de8fd170c6a8354daca273b6191) — recursive harness research | `main` `6868817518876de8fd170c6a8354daca273b6191` | No advertised tag; source package `0.1.0` is not a release claim. Apache-2.0; third-party code/data have separate terms. |
| [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering/tree/a9342ff471f2c0e60be0c08b9f4a7c502df4e442) — course and scaffolding tools | `main` `a9342ff471f2c0e60be0c08b9f4a7c502df4e442` | Tag `1.0` peels to `95c42edf2563db22c400e36125270ba2059cc250`, not this pin. MIT. |
| [Gloriaameng/Awesome-Agent-Harness](https://github.com/Gloriaameng/Awesome-Agent-Harness/tree/c717e129748c0681c2c35a011abd3fb3e8a28745) — directory and survey material | `main` `c717e129748c0681c2c35a011abd3fb3e8a28745` | No advertised tag. CC-BY-4.0; README distinguishes archived DOI v3, repository PDF v4, living index, and unpublished v5. PDF not read in this survey. |
| [TrishamBP/harness-engineering](https://github.com/TrishamBP/harness-engineering/tree/74f6550589f02163b4d530e6975d41b8ed12eed0) — independent reference runtime | `master` `74f6550589f02163b4d530e6975d41b8ed12eed0` | No advertised tag. No LICENSE/LICENCE/COPYING/NOTICE file found in tracked-tree and filesystem name scans; both scans found the WalkingLabs MIT file as a positive control. Reuse permission remains unestablished, not legally adjudicated. |

No upstream code or prompt body is copied into TeaPrompt's operational assets. Refresh on a changed branch, release, tag, license, or cited mechanism; do not transfer observations between artifacts merely because their names match.

## Evidence Used and Its Limits

All repository links are pinned; source and execution observations below were checked on 2026-11-13.

| Source inspected | Useful mechanism / observed boundary | What it does not establish |
| --- | --- | --- |
| Harness² [recursion](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/harness2/core/recursion.py#L354-L577), [selection](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/harness2/core/selection.py#L93-L111), [library](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/harness2/core/library.py#L101-L152), and [paper v1](https://arxiv.org/html/2610.14224v1) §§2–4, Appendices B, D, E.6, F | Propose–Probe–Compose; parallel/sequential task refinement and prior same-domain experience reuse. Final selection excludes reference executions. | Selection is not a baseline-win test; library admission is not independent verification of lesson truth. Paper gains remain author-reported, not locally replicated. |
| WalkingLabs [Lecture 09](https://github.com/walkinglabs/learn-harness-engineering/blob/a9342ff471f2c0e60be0c08b9f4a7c502df4e442/docs/en/lectures/lecture-09-why-agents-declare-victory-too-early/index.md), [scorer](https://github.com/walkinglabs/learn-harness-engineering/blob/a9342ff471f2c0e60be0c08b9f4a7c502df4e442/skills/harness-creator/scripts/lib/harness-utils.mjs#L220-L354), and [benchmark description](https://github.com/walkinglabs/learn-harness-engineering/blob/a9342ff471f2c0e60be0c08b9f4a7c502df4e442/skills/harness-creator/scripts/run-benchmark.mjs#L24-L35) | Teaches verification, cross-session state, and bounded workflows. Scorer examines structured text/schema/script content; upstream explicitly labels it a structural benchmark, not an LLM judge. | Structural score does not execute the verification entrypoint. The [graph example](https://github.com/walkinglabs/learn-harness-engineering/blob/a9342ff471f2c0e60be0c08b9f4a7c502df4e442/docs/en/lectures/lecture-14-graph-engineering/code/maker_checker_graph.py#L23-L32) still requires real model wiring. No universal three-tier duty or productivity result was validated. |
| Awesome [README](https://github.com/Gloriaameng/Awesome-Agent-Harness/blob/c717e129748c0681c2c35a011abd3fb3e8a28745/README.md) and [matrix](https://github.com/Gloriaameng/Awesome-Agent-Harness/blob/c717e129748c0681c2c35a011abd3fb3e8a28745/docs/systems.json#L12-L70) | ETCSLV taxonomy separates runtime coverage, modules, and evaluation infrastructure; cells carry source/confidence metadata. | Coverage is not quality, safety, or TeaPrompt strictness. A direct check of the matrix's [pinned Claude Code README](https://github.com/anthropics/claude-code/blob/3deb873687379f0c199a69fdaccc65f0865f7a29/README.md) found general product/install/plugin information, insufficient alone for detailed compaction/hook/checkpoint ratings. This qualifies that citation, not the product's capabilities or every matrix row. |
| TrishamBP [verification engine](https://github.com/TrishamBP/harness-engineering/blob/74f6550589f02163b4d530e6975d41b8ed12eed0/reference-harness/harness/verification/engine.py#L100-L146), [state](https://github.com/TrishamBP/harness-engineering/blob/74f6550589f02163b4d530e6975d41b8ed12eed0/reference-harness/harness/core/state.py#L42-L72), [file precondition](https://github.com/TrishamBP/harness-engineering/blob/74f6550589f02163b4d530e6975d41b8ed12eed0/reference-harness/harness/tools/builtins/fs.py#L66-L75), and [limitations](https://github.com/TrishamBP/harness-engineering/blob/74f6550589f02163b4d530e6975d41b8ed12eed0/README.md#L234-L253) | Verify-on-stop, mutation/evidence freshness, and explicit `unverified` output. Configured validators can veto completion. | Without a task validator, a fresh unrelated successful command can permit `completed`. Process hygiene is not sandboxing; live provider and confinement guarantees were not verified. |

Awesome's README gives matrix cutoff 2026-10-13 while `docs/systems.json` says 2026-10-12. The difference is retained, not silently reconciled. The reference runtime's cited [eleven-system study](https://arxiv.org/abs/2609.00006) was checked at abstract level only; this independent implementation is not evidence of code shipped by the paper's authors.

### Protected evaluation boundary

Harness² [execution documentation](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/docs/EXPERIMENTS.md#L87-L109) separates base evaluation and discloses unrestricted network, sandbox-disabled Codex, and an observed rubric download during a release-validation run. Its marker tripwires are not network isolation. This disclosure warrants external evaluation isolation; **it does not establish contamination of historical paper results**. [Pinned dependencies](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/dependencies/PINNED.md#L40-L42) explicitly allow historical runs to differ from the public workflow. No protected benchmark or real model was run here.

## Bounded Execution Receipt

These are coordinator-observed offline executions of pinned upstream code with caller-created fixtures, not model trials. Python 3.13 and Node v25.1.0 ran with a scrubbed environment, scratch HOME/TMPDIR, read-only source checkouts, and an external Seatbelt profile. Controls observed scratch I/O allowed and project reads, checkout writes, outside-scratch writes, and loopback connections denied. Those controls bound these observations only; they do not certify upstream containment.

| Observation and input set | Command / path exercised | Result |
| --- | --- | --- |
| Harness² built-in signed-ledger tasks `ledger-1` and `ledger-2`, both parallel and sequential modes | `python -B -m harness2.cli.demo --output <scratch> --k 2 --mode both`; scripted editor/selector, actual generated Python executions | CLI exit 0. All four selected artifacts matched independent Decimal sums: `85.15` and `20.25`, respectively. No baseline superiority or model competence measured. |
| WalkingLabs two structural fixtures, identical except entrypoint `exit 0` versus `exit 7` | Node `--jitless` with `OPENSSL_CONF=/dev/null`; import original `scoreHarness(files)`; separately execute each entrypoint via `/bin/sh` | Actual exits 0 and 7; both scored **96**. Empty file-array control scored 20. |
| TrishamBP official bugfix demo | `python -B reference-harness/examples/demo_bugfix.py`; original `ScriptedModel` and real unit-test subprocesses | Demo exit 0; verification failed then passed. Independently checked `mean([2,4,6]) == 4` and empty input raises `ValueError`. |
| TrishamBP task requires `answer() == 42`; scripted read, write `return 1`, run unrelated `python -c "pass"`, request stop; no validators | `build_harness` with `Mode.AUTO_EDIT`, `max_iterations=8`, `max_verification_attempts=1`, scripted steps and permissive approval callback under the external sandbox | Artifact still returns 1; status **`completed`**. |
| Same task, fresh fixture and steps, but `CommandValidator('answer-is-42', ['python', '-c', 'from calc import answer; assert answer() == 42'])` | Same upstream runtime and configuration apart from the bound validator | Artifact still returns 1; status **`unverified`**, reason **`verification_failed`**. |

The WalkingLabs input was the following caller-created file array, plus `init.sh` containing `#!/bin/sh\n# set -e test build Evidence\nexit ${exitCode}\n`. The `set -e` words are a comment, not shell enforcement. This is recorded fixture data, not a recommended harness or a runnable installation recipe.

```javascript
const files = [
  { path: 'AGENTS.md', content: '# Startup Workflow\n- ./init.sh\n- feature_list.json progress.md\n## Definition of Done\n- Verification Commands: test build\n- One feature at a time\n- Stay in scope\n## End of Session\n- clean restartable\n' },
  { path: 'feature_list.json', content: JSON.stringify({ features: [{ id: 'f1', name: 'fixture', description: 'No product implementation', status: 'not-started', dependencies: [] }] }) },
  { path: 'progress.md', content: '# Current State\n- Blockers Files Next Session\n- Last Updated Current Objective Recommended Next Step\n' },
  { path: 'session-handoff.md', content: '# Last Updated\n- Current Objective\n- Recommended Next Step\n' },
];
```

The TrishamBP pair began with `calc.py` returning 0, read it before overwriting, and independently executed the final `answer()` after each run. A newly named validator alone is not sufficient: its command must actually test the requirement, as this pair does.

### Failures and provenance retained

- **Refuted prediction:** the WalkingLabs driver predicted 100, observed 96, saved the receipt, and exited 1 on its unchanged full-score assertion. This was not a green smoke run. The narrower observed conclusion is equal structural scores for opposite exit outcomes, not “arbitrary prose scores 100”.
- Initial sandbox launches failed before usable observations: exit 134 for directory/dynamic-library access, Bun exit 133, and Node refusal to read host OpenSSL configuration. The profile allowed the necessary runtime paths; Node used `/dev/null` instead of loading host configuration. Earlier Python imports emitted nonfatal unavailable-blake2 diagnostics; these were not upstream product failures.
- The TrishamBP demo succeeded before a coordinator `/tmp` versus `/private/tmp` path assertion failed. Recovery read existing artifacts rather than repeating the demo. The first contrast pair omitted the required read-before-write and therefore did not perform its intended mutation; only corrected fresh fixtures support the contrast above.
- The Harness² wrapper's baseline-file glob matched nothing. No baseline-comparison claim rests on it. Complete upstream suites, model benchmarks, production deployment, and live sandbox/provider paths were not run.

Original survey and driver/profile/receipt bundle names are `harness-four-survey-2026-11-13.md` and `harness-four-evidence-2026-11-13.json` in session storage. They are supplemental provenance, not fresh-clone dependencies or operating authority. Pins, decisive inputs/results, limitations and decisions are internalized here; scratch drivers were removed. Raw logs and full per-event/subsystem payloads remain session-only and are not needed to follow this record's bounded conclusion.

## Optional Worked Reference — Acceptance Needs Relevant Evidence

This applies the existing [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md) §§2a, 4 and 6, plus [Reflective Implement](../skills/reflective-implement/SKILL.md) Verification; it adds no rule.

| Apparent assurance | What the observation supports | Existing acceptance question |
| --- | --- | --- |
| “The harness has a high structural score.” | Required-looking files and script text can coexist with a failing entrypoint. The upstream scorer explicitly measures structure. | Which executed behavior supports this task's acceptance criterion? |
| “Verification is newer than the last edit.” | Freshness can hold while the successful command checks nothing about the requested result. | Is the evidence bound to this requirement and the final artifact, rather than merely recent? |
| “The runtime reports completed.” | Terminal control flow can be satisfied without the requested result; the requirement-bound validator rejects that same artifact. | What independently checked postcondition permits product acceptance? |

## Optional Worked Reference — Selection Is Not Promotion

Harness² offers a concrete example for [Workflow Acquisition](../04-agent/workflow-acquisition.md) §§5–7 and [Artifact Promotion](../04-agent/artifact-promotion.md) §4. These events have different evidentiary roles:

| Event | What happened | Separate evidence still needed |
| --- | --- | --- |
| Generated / composed | A candidate harness was produced. | Successful execution and task-relevant verification. |
| Selected | The final was chosen among eligible candidates; reference executions are excluded, and `k=1` needs no selector. | A separately evaluated baseline, protected comparison and full cost accounting before an improvement claim. |
| Entered the experience library | A selected prior same-domain harness and populated experience record were retained. | Lesson truth, scope and transfer evidence; stored text is not promotion authority. |
| Promoted into a governed Skill or runtime | A different, local owner decision; not performed by this survey. | Applicable local promotion gates, provenance, approval, review/rollback, and host enforcement evidence. |

The isolated scripted demo supports execution mechanics only. It does not establish selection quality, beneficial cross-task learning, or authorization to import the experience library into TeaPrompt.

## Local Gap Test and Candidate Adoption Ledger

Existing acceptance, replay, provenance, promotion and host-enforcement contracts cover the transferable distinctions. No missing delivered Skill duty or local consumer defect was reproduced. Local recurrence remains `unknown`, not zero.

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| H4-DOC1 | One source-qualified record, catalogue entry and discovery metadata | Adopted: reference documentation only | Owner requested worthwhile updates; retain the failed prediction and evidence classes. Refresh when pinned sources or cited mechanisms change. |
| H4-DOC2 | Optional links from runtime-trust-boundary and workflow-acquisition, outside prompt fences | Adopted: navigation only | Makes existing contracts concrete without adding a checklist or changing prompt output. |
| H4-SK1 | New Skill or expanded existing Skill contract | No change | No verified local structural gap. Reopen on a reproduced failure against a named delivered acceptance duty. |
| H4-RUN1 | Install upstream runtimes, run model campaigns, or automate experience-to-Skill promotion | Not adopted | Standing runtime non-goal and separate host/authority/evaluation decisions; this record grants none. |
| H4-RULE1 | Universal three-tier verification, fixed memory caps, ETCSLV-to-strictness mapping, or “local overrides always win” | Rejected | Host-specific advice or unsupported new duties; local scope cannot outrank higher-authority instructions. |

## Evidence vs Inference and Falsifiability

- **Observed:** pinned source/disclosure text, actual scripted/demo execution, score/exit mismatch, validator contrast, and one sampled citation's limited scope. This is not a four-product benchmark or a directory-wide re-audit.
- **Author-reported:** paper gains and course anecdotes. The Harness² paper was read only in the sections named above; the eleven-system paper only at abstract level. Neither constitutes independent replication.
- **Inference:** these examples may help readers apply existing contracts. No reader study or with/without-Skill evaluation was conducted.
- **Unknown:** model efficacy, negative transfer, full optimization cost, historical evaluation contamination, production containment, local demand, and unresolved reuse permission. External popularity or a green repository check cannot settle these.
- **Falsifiers:** a requirement-relevant check that changes these contrast outcomes would qualify the corresponding upstream claim; a reproduced local contract gap could warrant an in-place repair. Neither automatically authorizes a new Skill, runtime, or campaign. Preserve prior receipts when re-pinning rather than retroactively assigning new behavior to them.
