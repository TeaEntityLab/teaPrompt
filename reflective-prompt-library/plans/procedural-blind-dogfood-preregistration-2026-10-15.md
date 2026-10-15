# Procedural-Blind Dogfood Preparation — 2026-10-15

Language: English

> **Status: preparation and private offline consumer verification complete; scoped freshness PASSED_SCOPED; campaign execution HELD.** Experiment `DF-PB1-2026-10-15`, protocol version `1`. This is a separate preparation population, not an amendment, admission or result of `DF-C2-2026-10-14` protocol 2.

## Goal and authority

The maintainer requested independent subagents to generate the pool metadata and corresponding custody evidence while keeping the contents unknown to the coordinator, then requested continuation until no actionable work remains. A public-marker preflight found that the coordinator could read both a child-created `0400` file and a child tool result in the backing session JSONL. The `history://` summary itself did not expose the marker bytes. Separate contexts, owner-only modes and worktrees therefore did not establish the original coordinator-exclusion criterion.

After that result, the maintainer explicitly selected **「改採程序性盲測」**: local subagents may generate independently; the coordinator does not read questions, answers or their execution histories and receives metadata only; the experiment is separately versioned and discloses that the platform can still recover the contents. Other execution and scoring gates are not automatically released.

The original [DF-C2 preregistration](fresh-dogfood-campaign-preregistration-2026-10-14.md), [strong-custody contract](df-c2-protected-custody-workflow-spec-2026-10-15.md), private consumer v3r1, owner-reported pool and historical receipts remain unchanged. The old accepted-inconclusive cohort remains 334 calls / 12 reserves / USD 0. This record does not reinterpret failed strong isolation as a pass.

## Selected method and limits

- **Procedural context separation, not enforced confidentiality.** After generation begins, the coordinator reads only the declared public metadata/summary files and metadata-only final reports. No raw family files, answers, generators, curator/auditor histories, session JSONL, captured streams or raw findings enter its context.
- Three fresh curator contexts independently generate Q-IMP, Q-REV and Q-HOF. A fourth, non-authoring auditor privately reviews the outputs, exercises the oracles and produces the combined metadata and custody record. The coordinator does not ask curators to reveal content to diagnose a failure.
- All content is newly authored public/synthetic material, never product/customer data, operator memory or credentials. Existing pools are not overwritten or relabeled. A new preparation population is not a claim of eligible confirmation data.
- The host, platform transcripts, tool results, memory/capture and provider retention remain potentially recoverable. Voluntary non-reading cannot prove technical exclusion, cognition-level blindness, provider-state equality or independence of model weights.
- The generation agents know their family and can know target-skill intent. That is a possible construction bias. There is no performance-based regeneration, best-seed selection, target tuning or efficacy claim. Mechanical/oracle construction defects may be repaired before freeze with preserved initial revisions and reasons.
- The auditor may know all task answers but sees no experimental C/T outcomes: no such outcomes are generated in this preparation. This audit is not qualified arm-blind human scoring.

## Population and input contracts

Public catalog provenance remains [B008, B012 and B010](benchmark-tasks.json), with the corresponding intent definitions in the [DF-C2 questions](fresh-dogfood-campaign-preregistration-2026-10-14.md#questions-and-population). This preparation creates new `PB1-{IMP,REV,HOF}-S01/S02` and `-F01/F02/F03` identities: six selection and nine final instances. S01 is challenge, S02 healthy, F01/F02 are distinct paraphrase/distraction challenges, and F03 is a healthy/opposite-consequence sentinel. Names and hashes alone do not prove semantic novelty.

- **Q-IMP / B008 / reflective-implement:** an actual bounded applied repair after a refactor, with a fixed intervening question, versus an explanation-only/no-edit boundary. A report claiming a repair over unchanged data is not a pass.
- **Q-REV / B012 / reflective-review:** identify an actual verification-binding defect and its consequence/evidence, versus a healthy map without invented findings. Do not score wording, headings or a mere nonempty report.
- **Q-HOF / B010 / reflective-handoff-retro:** a producer handoff must let a fresh successor perform the required recheck/hold/continuation from that handoff and the common brief only. The successor receives neither target skill nor producer DECISION sidecar.

Fixtures retain the existing worker's `instance`, string-to-string `files`, and `expected.workspace_allow` / `expected.reporting_allow` envelope. Initial messages and optional fixed intervention are separate artifacts. The target skill is not embedded in either arm's task files or common setup; future treatment delivery remains separately bound. DECISION sidecars and all semantic-scoring limits remain separate from the functional and authority outcomes.

For this bounded preparation, executable oracle calibration consumes **data-only workspace/report/event inputs**. Q-IMP can repair real configuration/data consumed by a deterministic check after a refactor; it must preserve the debugging/applied-change consequence rather than substitute an explanation task. No candidate-supplied Python, shell or other executable content is run on the host. Trusted, reviewed stdlib oracles evaluate data; a future case requiring arbitrary candidate execution remains subject to native containment and admission.

## Private artifacts and public exports

A fresh session-private root contains an immutable `protocol.json`, `generation-contract.json`, a coordinator-owned `public/` namespace and withheld per-family artifacts under `withheld/`. The name `withheld` denotes the voluntary read policy, not filesystem exclusion. Case artifacts include the fixture, messages, intervention, task contract, distinct functional/authority oracles and private calibration examples. Q-HOF additionally has successor setup contracts; it never precomputes a future real producer handoff.

The independent auditor owns the authoritative preparation manifest, private semantic/copy audit, oracle-calibration observations, and these answer-free exports:

1. `public/pool-metadata.json`: actual case identities and digests, frozen protocol/manifest identities, scoped freshness result, audit receipt, explicit procedural mode and unresolved admission gates.
2. `public/custody-receipt.json`: actual curator/auditor identities and copy channels, coordinator non-reading procedure, the observed **failure** of enforced exclusion, and the explicit accepted limitation. It is not a positive strong-custody certificate.
3. `public/audit-summary.json`: closed status enums, counts, calibration outcomes and evidence digests only. No task domain descriptions, answers, findings text, raw errors or streams.

The export schema is frozen in the private generation contract before generation. A coordinator-visible consumer checks it and rejects wrong identities, malformed/extra fields, false enforced-exclusion claims, unresolved audit status presented as readiness, and unexpected content fields. Detailed failures stay withheld and can be routed to the responsible curator without exposing them to the coordinator.

## Acceptance and verification

| ID | Required observation | Verification / boundary |
|---|---|---|
| PB-AC-01 | Separate experiment/protocol and exact procedural choice recorded before generation | Immutable private protocol identity; original DF-C2 identities retained |
| PB-AC-02 | Fifteen complete cases with the frozen six/nine registry and correct family/class coverage | Independent manifest/digest and fixture-envelope audit, not author counts alone |
| PB-AC-03 | Functional and authority oracles distinguish valid reference behavior from plausible consumer-visible failures | Actual oracle invocation over private positive, wrong-consequence, unauthorized-action and false-pass controls; no wording/wiring-only checks |
| PB-AC-04 | Q-HOF has matched successor setup and a functioning data-level handoff consequence check | Independent successor calibration; explicitly not evidence of a live model transfer |
| PB-AC-05 | New instances are semantically checked against each other and the available closed-cohort source corpus | Private scoped comparison record; missing prior-source coverage remains UNKNOWN and an admission hold |
| PB-AC-06 | Only approved answer-free exports reach the coordinator after generation | Closed export validation and coordinator read discipline; platform recoverability remains disclosed, not tested away |
| PB-AC-07 | Truthful custody/effect accounting | Two preflight recoveries retained as failures; generation/audit model usage distinguished from zero campaign trial/canary dispatch |
| PB-AC-08 | Usable metadata and reproducible offline verification are delivered without implying campaign readiness | Actual safe-export CLI/consumer smoke, immutable manifest and complete held-gate list |

## Falsifiability

Any revealed case/answer in a coordinator-visible return is a procedural-blinding failure. Preserve the exposure and affected population; do not silently regenerate or delete it to claim blindness. Calibration failures are not experimental task outcomes. No performance measurement is used to alter the cases or target skills.

## Execution sequence and ownership

1. Coordinator freezes the version, public contracts, output allowlist and separate root; it supplies no case answers.
2. Curators generate their disjoint families concurrently. Each returns only family, counts, status and digest. No mid-flight test/build/lint/formatter runs; the independent audit performs the combined checks after authoring.
3. Independent auditor reviews actual source artifacts, runs bounded offline oracle/fixture checks, records semantic-freshness coverage and copy channels, and freezes the population and oracles. Construction fixes preserve prior revisions; any post-freeze change invalidates the affected identity.
4. Coordinator validates only safe exports, exercises the safe consumer surface, and records the artifact disposition and remaining gates. It never opens withheld artifacts or curator/auditor transcripts to debug.

## Risk and remaining human gates

**GO:** the explicitly selected procedural-blind generation and offline artifact audit, using fresh private files and existing host subagents. **NO-GO:** claiming strong custody, automatically importing this population into DF-C2, or starting a new provider/native/campaign phase from these files alone.

Actual phase/source/credential/quota bindings, native containment and assigned-case access, current memory/capture evidence, required canaries, qualified human semantic scoring, freeze/leak-audit release, exact confirmation subset and named outcome acceptance remain separate. Existing Go-setting confirmation is preserved rather than requested again. There is no new execution allowance or counter reset from this preparation record.

The sink boundary is new synthetic generation artifacts and their host-managed subagent records. No operator service, permission, secret, external host, repository runtime, skill, campaign ledger or old pool is changed. Unknown provider/platform retention is disclosed. Recovery preserves original files and records; exposure cannot be undone by deleting a copy. No commit, push, skill adoption or TeaPrompt runtime promotion is implied.

## Evidence and disposition

Preflight evidence: session-private `df-c2-subagent-blinding-preflight-2026-10-15.json`, `df-c2-subagent-blinding-boundary-observation-2026-10-15.json`, and the two independent child receipts. New generation root: session-private `df-pb1-2026-10-15.chUGBO`. At initial freeze, generation and audit were pending; the completed preparation evidence follows.

### Completed preparation evidence

The three curator contexts returned five cases each without revealing case contents. The non-authoring `PbPoolAuditor` then reported **15 audited cases: six selection and nine final**, with **60/60 calibration controls passing and zero failures**. Each control checks the distinct functional and authority predicates. The public summary is bound to the private audit receipt and frozen manifest; the coordinator checked those public bindings without opening the withheld artifacts or any curator/auditor history. This is independent artifact-audit evidence, not a live C/T trial, human semantic score or demonstrated model-transfer result.

The initial audit reported freshness **UNKNOWN** and retained `FRESHNESS` as an admission hold. That receipt remains unchanged; its added-source requirement is corrected in [Readiness continuation and scope correction](#readiness-continuation-and-scope-correction). Neither the original artifact-audit PASS nor the scoped correction establishes global novelty or eligibility for confirmation.

The actual `python3 -I -B check_exports.py` entrypoint returned `PASS_PUBLIC_EXPORTS`, with `coordinator_exclusion_enforced: false` and `execution_admission: HELD`. A separate guarded smoke exercised **24 scenarios**: the actual export set passed; **23 negative controls** refused with exit 4 and no raw-marker disclosure. Controls included extra content fields, missing/duplicate cases, wrong identity, Boolean version/count confusion, false exclusion/admission/copy-denial claims, lost gates, failed calibration presented as success, digest drift, duplicate/nonfinite JSON, unsafe modes, links, FIFO and missing paths. The completed run exited 0 with no audit-boundary violations or withheld-file reads.

Two reader defects were observed before repair: the consumer treated the historical public `0644` failure receipt as a private export, and opening a FIFO blocked before the regular-file check. The repaired reader explicitly distinguishes that public receipt, retains owner-only checks for the new exports, and uses nonblocking open before the type check. Both before/after observations are preserved. The historical receipt's bytes and mode were not changed.

Two smoke-driver attempts failed separately: guarded module loading, then relative-directory-descriptor cleanup. Neither was counted as a successful run or an experimental outcome. The final driver loads the declared consumer source directly and cleans only its own absolute-path scratch tree. Failed-attempt identities, final observations and the replayable public-only driver are retained in `public/verification-receipt.json`; the two abandoned scratch directories were removed after evidence binding.

### Evidence identities

All files below are under the session-private preparation root named above unless otherwise stated. Digests identify bytes, not confidentiality, authenticity of human judgment or execution authority.

| Artifact | SHA-256 |
|---|---|
| Frozen protocol | `292b2fdff373385710a7936b49622003d402c41324c805252c71c85979c8a71e` |
| Independent frozen manifest, withheld from coordinator | `850633d2afbeb831ff0f481b133139dbf45ff8ed0c1e74efa4fa005dc3698290` |
| Independent private audit receipt | `3c6e9a222f69957d0a945485a0dedaf06769256eafae65f0eb65f1f35ab78a3f` |
| Private scoped-freshness receipt, status UNKNOWN | `c9d5ed78544a827c72d87d448e624279788475a10c89caa0fe0e18a963e6ec08` |
| `public/pool-metadata.json` | `98b4e7a1e14c5bcf3a4f4ef380732b4e90226a98e8b11a29bd5bb5830dada5b8` |
| `public/custody-receipt.json` | `4983fbdfa6d227e7fed176eda29a73173770800fa62f478226af27eb3dbde4d5` |
| `public/audit-summary.json` | `3ed394a7a9be5b2c72e2cc2082b160ae3ef00050c0fe6642bf0bf50302a7345e` |
| `check_exports.py` | `abd7e150f1f6ae6a18f2459a20d5c228941db25ed03af8d5e32c1191fb9576bd` |
| `public/verification-receipt.json` | `524139cda2ca1fdd74bade43103fbc0afabdb6140cbd9316e4a793fec15641bd` |

The three original DF-C2 preregistration/custody-spec/v3r1-source-manifest identities matched their pre-continuation hashes. The frozen PB1 protocol, generation contract, common setup and three target skills also remained byte-identical. The owner-reported DF-C2 pool and campaign ledgers were not opened or rewritten; the auditor's historical-source comparison is the separate, explicitly scoped read described above.

### Acceptance disposition and remaining gates

| Acceptance | Disposition |
|---|---|
| PB-AC-01 | Verified separate protocol and unchanged prior-record bindings |
| PB-AC-02–04 | Independently audited artifact completeness, functional/authority calibration and successor setup; no live role/transfer claim |
| PB-AC-05 | Initial UNKNOWN superseded by the supplemental PASSED_SCOPED ruling below for the frozen comparison universe; no global-novelty or execution claim |
| PB-AC-06–07 | Closed public exports and truthful procedural-custody receipt checked; coordinator non-reading is attested, not technically enforced |
| PB-AC-08 | Actual CLI plus public-only negative smoke passed; usable metadata delivered with execution HELD |

Consumer coverage is bounded: direct validation and the CLI were exercised; the independent auditor owns the private artifact/manifest checks; public persisted exports and their binding failures were exercised. No dispatcher, provider, native guest, actual role canary, human scorer or confirmation consumer used this population.

At preparation close, seven gates remained: `FRESHNESS`, `SOURCE_PHASE_BINDING`, `QUOTA_NATIVE_CAPTURE`, `ACTUAL_ROLE_CANARIES`, `HUMAN_SCORING_FREEZE`, `CONFIRMATION_SUBSET` and `OUTCOME_ACCEPTANCE`. The continuation below corrects the first gate's scope; the other six remain held. The next execution step requires the relevant missing evidence and a source/phase-bound PB1 decision, not another generic Go-setting confirmation. No new campaign dispatch, credential read or native guest occurred. Preparation used three curators and one auditor; their host/model usage is not zero and is not included in the unchanged old 334-call / 12-reserve / USD 0 campaign accounting. No skill change, runtime adoption, commit or push follows.

### Readiness continuation and scope correction

The maintainer's subsequent **「繼續」** continued offline preparation, not a new phase grant. Two independent contexts reviewed freshness and source compatibility; the coordinator exercised the public input boundaries without opening withheld cases, oracle bodies, either case-auditor history or session JSONL. New evidence lives in session-private `df-pb1-readiness-2026-10-15.0N3gZc`; all original preparation artifacts and DF-C2 source remain unchanged.

**Audit-scope defect and correction.** The frozen `protocol.json` `legacy_reference_scope` and PB-AC-05 require the explicitly bound, available closed-cohort corpus. The earlier coordinator-authored auditor assignment additionally required the unlocated owner-reported DF-C2 pool. That extra requirement was not in the frozen comparison universe. The continuation auditor initially carried it forward, then checked the authority discrepancy: bound coverage was complete, with no unavailable required source. Its supplemental ruling is **PASSED_SCOPED**, not a waived requirement, a changed oracle or a claim of universal novelty.

| Independent comparison coverage | Observed count |
|---|---:|
| Current PB1 cases | 15 |
| Within-population pairs | 105 |
| Historical source artifacts reviewed | 11 |
| Historical cases reviewed | 9 |
| Unavailable sources required by the frozen scope | 0 |

Semantic non-overlap is the independent auditor's scoped judgment over the actual artifacts; the coordinator verified the closed metadata and digest bindings, not the hidden reasoning. The unlocated owner-reported pool and global novelty remain outside-scope unknowns. The original `public/pool-metadata.json`, private freshness receipt and first continuation summary still record UNKNOWN and are preserved. `freshness-scope-resolution.json` links the earlier summary and a new private explanation; `readiness.json` consumes this supplement. Running the original `check_exports.py` therefore still correctly reports the original UNKNOWN/HELD view, not the later scoped disposition.

**Source compatibility, observed rather than inferred from hashes.** The existing eight-file v3r1 manifest is bound to DF-C2 protocol 2. A guarded, public-only smoke exercised five paths:

| Actual path | Observed result / boundary |
|---|---|
| PB1 `check_exports.validate` over the actual public exports | PASS_PUBLIC_EXPORTS with execution HELD |
| DF-C2 `protocol.validate_pool_metadata` over the actual PB1 export | Refused the distinct closed schema |
| DF-C2 `go_provider._secret` given the actual preparation protocol | Refused before credential access; preparation is not a live grant |
| `worker.validate_inputs` then `ToolGate.run_check` over an expressly public data-only control | Envelope accepted; the fixed diagnostic held rather than invoking a PB1 oracle |
| Actual gate action record versus the PB1 authority-event contract | Incompatible event shapes |

The source review traced `consumer.run_files/run`, ticket/source checks, provider admission, HOF producer lineage and safe exports. `worker.run_check` invokes the fixed `public_diagnostic` calculator diagnostic, not either PB1 `evaluate` API. Its action records also do not supply the required `{actor, operation, path, outcome}` projection. These are interface findings; the coordinator and source reviewer did not inspect the contents of PB1 fixtures.

Honest PB1 identities cannot be represented by the reviewed DF-C2 validators. Opaque pool/readiness digest fields do not prevent a caller from falsely labeling foreign content under a DF-C2 grant; that is not authorized PB1 admission. The separate PB1 identity is already decided: no relabeling, no imported allowance and no amendment of the closed cohort. The legitimate next source must implement PB1 identities, hidden data-only oracle evaluation and host-derived authority events, preserve real producer-bound handoff, and bind the actual source/policy/schedule to a PB1 phase decision. The reviewed source has not implemented those interfaces; this record does not claim an adapter exists or qualify an unreviewed host.

The first smoke driver was stopped by its undeclared-import read guard before any observation completed. The repaired driver loads the exact declared source bytes; the final run exited 0, completed all five observations, reported no audit violations, verified the original public/source files unchanged, and removed its owned scratch. Both driver revisions and results are retained. No production source, case, oracle or acceptance condition was changed to satisfy the smoke.

| Continuation evidence | SHA-256 |
|---|---|
| First freshness summary, superseded scope | `fe23fc5235d51f4a1aae3a3e62c89a78f10e94f512a880e18c931013ed879645` |
| Supplemental `freshness-scope-resolution.json` | `c99b18714a5eca60365344ed6ccac3f570fd5283f025943a214451d9786dd47f` |
| Final `source-smoke-final.json`, including replayable driver | `a3550bf4a0463a343c6d997833a5a9a002c9f8f5548ef34da5d30320fc6d4111` |
| Combined `readiness.json` | `fba5ba8543d415d6db3ca34b49a00fe1818ddb5d387226234b580335013005ee` |

**Readiness disposition at that point:** PB-AC-05 is satisfied within its frozen scope. `SOURCE_PHASE_BINDING`, `QUOTA_NATIVE_CAPTURE`, `ACTUAL_ROLE_CANARIES`, `HUMAN_SCORING_FREEZE`, `CONFIRMATION_SUBSET` and `OUTCOME_ACCEPTANCE` remain held. The legacy input/provider/tool boundaries were exercised; actual PB1 dispatch, scoring, native execution, live role canaries and human release were not. There is no new phase grant or campaign allocation. Additional review used two host/model contexts, not zero total model usage. Old cohort accounting remains 334 calls / 12 reserves / USD 0; no skill edit, runtime adoption, commit or push.

### Private offline consumer implementation and verification

The maintainer explicitly selected **完成新版 consumer，僅離線驗證**: complete
the PB1 source, data-only oracle evaluation, host-derived authority events and
producer-bound handoff execution, without a live phase grant or campaign calls.
This is a new session-private source revision, not a DF-C2 relabeling, a live
provider adapter, or a TeaPrompt-owned runtime.

**Initial source and evidence root:** session-private
`df-pb1-consumer-v1-2026-10-15.BHPWWv`.
The three executable sources are `consumer.py`, `pb1_inputs.py` and
`pb1_worker.py`; their identities are bound by `source-manifest.json`.
The frozen pool, protocol, cases, oracles, calibration controls and original
exports remain unchanged. New contexts, source files and receipts use their
explicit owner-only immutable-file contract. Existing case-file modes are
preserved: the frozen input contract rejects group/world writes, not every
owner-write bit; digest identity and change control do not imply OS isolation.

| Acceptance / consumer | Implementation and exercised evidence | Disposition |
|---|---|---|
| Exact PB1 source, pool and context binding | Digest-verified module loading; physical, bounded file reads; complete input validation before a new session; drift and duplicate namespaces refused | Verified offline |
| Actual operation consequences and authority events | Fresh filesystem clone; bounded read/write/delete/check operations; allowlist denials; host-generated actor/operation/path/outcome records; restored mutations remain observable | Verified offline |
| Hidden data-only oracle evaluation | All 15 original cases loaded; all 60 original calibration controls passed through the new evaluator, without changing their semantics | Verified by independent executor |
| Producer-bound Q-HOF continuation | Five actual producer/successor chains; original producer handoff, input identity and both event streams retained; successor mutation or substituted input refused | Verified by independent executor |
| Closed public CLI and private receipts | Actual prepare CLI, duplicate refusal, unbound-pool refusal and filesystem-operation smoke; stdout contains status/experiment/mode/session-count/admission only | Verified offline |
| Original evidence and no live effects | Fourteen public bindings and eight prior-source files matched; independent executor retained actual case bindings; no campaign/provider/native/credential effects | Verified within the recorded read set |

#### Offline entrypoints and output boundary

`consumer.py prepare --root <new-physical-root> --pool <frozen-pool> --freshness
<scoped-receipt> --source-sha256 <manifest-sha256>` initializes a distinct
offline namespace. `consumer.py run --root <root> --session-id <new-id>
--instance-id <bound-id> --operations <private-json>` executes the bounded data
operations; Q-HOF additionally requires `--successor-operations <private-json>`.
These are private operator interfaces, not permission for the coordinator to
read case bodies or hidden receipts. There is no provider, credential, native
guest or live-grant path.

`COMPLETED_OFFLINE` means evaluation finished, not that the task passed.
Functional/authority verdicts and task content stay in private immutable
receipts. `HELD` exits 4 without echoing input paths, exception text, actions or
scores. Both statuses retain `execution_admission: HELD`. The public `check`
operation is only a syntax/format diagnostic, never the hidden oracle.

#### Verification results and retained failures

The initial revision's final public suite passed **52 behavioral regressions**, with zero
failures, errors, skips or audit violations. An earlier 59-pass run included
seven duplicate regressions; their passing sources remain in
`public-reproduction-tests.json`, while equivalent module-level coverage
remains in the final suite.

The first integrated run retained 48 tests and nine assertion failures:
eight implementation failures and one invalid owner-write test assumption.
Repairs addressed link handling and producer/successor history; the mode test
was corrected to the already-frozen contract, not by changing case bytes or
modes. A subsequent run retained three failures: two writes refused hardlinks
only after truncation, and a parent-path alias was resolved away before
validation. The final implementation validates the opened descriptor before
truncation and rejects nonphysical input paths before adopting their resolution.
All failed-run receipts remain separate from passing evidence.

The independent `PB1FrozenVerifier` reported **15 completed consumer runs,
60/60 calibration controls, five completed handoff chains and eight passing
negative controls**, with zero failed controls or audit violations. Its public
summary binds a private receipt; the coordinator checked only the closed
metadata and digests, not cases, answers, oracle bodies or reviewer histories.
Scripted operations establish consumer mechanics, not actual-role canaries,
model transfer, human scores or skill efficacy.

| Evidence under the source root | SHA-256 |
|---|---|
| `source-manifest.json` | `f7119e828400432c80671f95d621fd3bafc754b19c4806d0c8e641d32a49a4a6` |
| `public-regressions-final.json` | `76e939e82c2bd4abaa555c052c15f3d91e2da26f0c13f8fb8a07e9c3e80630bd` |
| `public-cli-smoke.json` | `19c124cd77ceb2b46399eb268b98ac22963e1e62ff4cdf2f26d8daee45fecb68` |
| `frozen-verification-summary.json` | `449dca32551a3a24a8ead5fe402cd7e426bcdfac035364e690799d7dac1d57ab` |
| `preservation-after.json` | `e15b97cc47f2b9d71cc73f5f933ee28063924f56162a1204ad6ce406c75842c5` |

**Initial offline disposition:** the selected offline implementation is exercised.
Live `SOURCE_PHASE_BINDING`, `QUOTA_NATIVE_CAPTURE`, `ACTUAL_ROLE_CANARIES`,
`HUMAN_SCORING_FREEZE`, `CONFIRMATION_SUBSET` and `OUTCOME_ACCEPTANCE` remain
held. No live grant, campaign call/allocation, provider request, credential
read or native guest was created. Coordination/review used host/model
resources and is not zero total model usage. Old cohort accounting remains
334 calls / 12 reserves / USD 0. Procedural context separation is still not
technical confidentiality. No skill edit, runtime adoption, commit or push.

#### Source-review closure and current v1r1 source

The independent source-only review was bound to the initial `f7119e82…49a4a6`
manifest and did not inspect any frozen case or hidden receipt. Current-byte
triage confirmed one defect and rejected one erroneous premise:

- **Confirmed:** `_execute_one` created missing parent directories before
  refusing unauthorized workspace operations or reads/checks of unwritten
  reports. Regular-file snapshots hid those directory effects. Public controls
  also caught unnecessary parent creation when deleting an absent allowed path.
  Four focused tests retained seven failing assertions and zero harness errors.
- **Rejected:** the claimed `_Denial` escape from fixture cloning does not
  occur. `_Denial` subclasses `Exception`, already caught by the clone boundary
  and converted to `OperationError`. The public file/directory-collision probe
  observed `OperationError`; that source path was not changed.

The repair lives in separate session-private
`df-pb1-consumer-v1r1-2026-10-15.FPa49J`. Only `pb1_worker.py` changed among the
three executable sources: parent creation now occurs inside authorized writes,
after their size checks, in both workspace and report branches. No new helper,
fallback, oracle, case or live path was added. `test_pb1_worker.py` adds the four
behavior regressions, including successful nested writes to both sinks.

The revised public suite passed **56 tests**, with zero failures, errors,
skips or audit violations. Actual CLI/API smoke passed five scenarios,
including seven nested-path operations: denied and absent-delete parents
remained absent, while authorized nested writes reached disk. Thirteen
predecessor public files, fourteen original public bindings and eight prior
DF-C2 source files were rehashed unchanged. The complete initial source/evidence
root and private receipts remain intact. Revised frozen-corpus verification
has its own source-bound receipt; the initial run is not reused as proof for
changed code.

TWINS: searched `_ensure_dir_nolink(` - found 2 other callsites: the `pb1_worker.py` report branch (same defect, repaired) and `_clone_files` (authorized fixture creation, intentionally unchanged).

| Evidence under the v1r1 root | SHA-256 |
|---|---|
| `source-manifest.json` | `5c77e9f29a4ba3d31f83f086c290eb4320e496909f20007891a7f584ff2a3575` |
| `source-review-before.json` | `6000399e756265054589142b50ef4546d2eafde1bffcc9cdcb84ef29e1da986b` |
| `public-regressions-final.json` | `3b0d56a79636ccbf9faef9a7f51a63005132bce423a1e3183af8a454c9068052` |
| `public-cli-smoke.json` | `31c6779c0416ac768d8f3833890509db04b19b3b6d8dfe175bb5935bd5f4009e` |
| `frozen-verification-summary.json` | `acc4efab51f1402fdd37c691737ab755bc405a5e06c90f6017d54435faf573bb` |
| `preservation-after.json` | `7758f4b7000e09839ea54b5f7fc9feb59d14edc473dad15e2784a7ff8be91f41` |

The independent executor reran the unchanged corpus against the exact
`5c77e9f2…2a3575` revision: **15 loaded/completed cases, 60/60 calibration
controls, five handoff chains and the same eight negative controls passed**,
with zero failed controls or audit violations and original bindings unchanged.
The coordinator validated only the closed metadata, source identities and
receipt digests. Its first metadata-integration expression had a JavaScript
parse error before execution; the corrected integration passed without any
source, oracle or case change.

**Current disposition:** the authorized offline consumer implementation,
source-review triage and final-source verification are complete. All six live
execution gates listed above remain held. There is no live grant, campaign
call/allocation, provider request, credential read or native guest; coordination
model usage remains separate from unchanged old-cohort accounting.

