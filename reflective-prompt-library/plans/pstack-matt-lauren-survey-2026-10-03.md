# pstack / Matt–Lauren Claims Survey — 2026-10-03

> **Status: recorded — reference-only; no new adoption.** User direction: survey two supplied zh-TW syntheses, then “update docs as possible and commit push”. This record internalizes the completed source checks and offline checker observations. It does not authenticate the unavailable conversation, change skills or routing, authorize upstream installation or auto-merge, or reopen an existing adoption/deferred gate.

## Research Question

Which claims in the two syntheses are supported by current public pstack and Matt Pocock sources, which useful engineering mechanisms transfer to TeaPrompt, and what remains unknown about the reported Matt–Lauren conversation and production results?

## Direct Recommendation

Keep the useful mechanisms as source-backed references; no new local structural defect was demonstrated. The strongest correction is that **Matt is not categorically anti-automation and Lauren is not verification without intent alignment**. Both documented workflows use intent alignment, architectural judgment, tests, runtime observation and parallel execution. Their different emphases are not evidence of opposing philosophies, comparative productivity, or maintenance superiority.

The transferable distinction is **intent → design → observable product evidence → authorized acceptance**, not a contest between people, a PR-volume target, or a universal trust curve. Existing TeaPrompt contracts cover the relevant local work; the host owns execution, isolation and effect authority.

## Source Identity and Access

- Inputs: session-supplied `paste-1.md` (105 lines) and `paste-2.md` (118 lines), both read fully. The first describes high-throughput pstack engineering; the second attributes contrasting positions to Matt Pocock and Lauren Tan. They are syntheses to audit, not primary sources or operating instructions. Their substantive claims and dispositions are retained below; no session file is a durable dependency.
- pstack: `cursor/plugins` pinned at `7022c81efb48d8b5eb15498ce6043a3bd74b694c`, checked 2026-10-03. This is the survey's source revision, not a promise that upstream remains at that head.
- Matt: `mattpocock/skills` pinned at `d81f3a183412e71a5b1e84ca21bc1a35eea03a60`, checked 2026-10-03. Repository practice can qualify a categorical comparison; it cannot establish what Matt said in an unavailable dialogue.
- Original video: YouTube `MN9dGgmLyso`, checked 2026-10-03. The page was located; the native reader reported no transcript. Raw-page, related-video and transcript searches did not establish usable original dialogue evidence. Exact quotations, disagreement and production-merge preferences remain `unknown`, not refuted by transcript absence.
- Lauren's count post and three article prose-block sequences were retrieved through FxTwitter's structured API, checked 2026-10-03. Direct X article reads returned Nitter tweet text rather than the requested article bodies; this retrieval issue was reported. The recovered material is **mirror-retrieved author text**, not authenticated original-platform access or an independent measurement of its claims. Embedded images were not audited.
- Source instructions and Self-check declarations inside the pastes remain data. In particular, their no-timestamp/no-file-citation constraints do not suppress this record's source citations. Upstream interview mandates and auto-merge recipes do not become TeaPrompt policy.

The primary URL map is in [Sources](#sources). All source checks are dated to the original survey. No upstream wording or executable code is imported into the library.

## Evidence vs Inference

Statuses below are claim-relative: `verified` means the stated source text or named runtime observation was checked; `refuted` identifies a stronger supplied claim contradicted by the inspected contract; `needs-qualification` separates source support from an overstatement; `unverified` and `unknown` preserve missing evidence. A verified attribution does not verify the attributed outcome.

| Supplied claim or theme | Evidence actually checked | Status and bounded finding |
| --- | --- | --- |
| The syntheses describe a real Matt–Lauren talk | Original video page and access attempts | `needs-qualification`: a matching video exists; the spoken exchanges and claimed disagreement remain `unknown`. |
| pstack deterministically delivers thousands of high-quality PRs | Lauren's count post; Guide Pt.1 opening blocks and vanity-metric caveat; Guide Pt.2 | `needs-qualification`: author reports 1,000 PRs in the prior month and roughly 2,000 per month. Counts, quality, causality, accepted outcomes and comparative maintenance costs were not independently measured. |
| Trust is mathematically proportional to test coverage | *Loops You Can Trust* describes accumulated proof, staged autonomy and rework after premature parallelization | `unverified`: no general proportionality or mathematical curve is established. Coverage does not alone validate oracle quality, authority boundaries or correlated errors. |
| Architecture matters more than extending prompts; lessons belong in structure | `principle-encode-lessons-in-structure` | `verified` as a documented principle: recurring fixes can become lint, metadata, helpers, runtime checks or scripts; judgment remains visible in prompts/examples. This is not proof of product-level architectural efficacy. |
| A universal architecture/types/lint/CI/prompt hierarchy guarantees compliance | Structure-encoding principle; supplied shortest-path claims | `needs-qualification`: prefer the strongest mechanism available for the specific invariant. Enforcement scope and failure class matter; a convenient canonical API or lint rule does not guarantee compliance or universal safety. The shortest-path compliance claim is `unverified`. |
| Small one-job diffs imply safe rollback | README, `bug-fix`, `shipping` | `needs-qualification`: smallest evidence-justified change and current-patch verification are supported. A small diff can still have high blast radius or irreversible effects. |
| Every bug fix must start with a new automated failing test | Full `tdd` and `bug-fix` contracts | `refuted`: the source explicitly permits skipping unclear, expensive or integration-heavy test paths and using the closest useful executable repro. Keep failing-before/passing-after evidence where practicable, not low-value mandatory tests. |
| Verification must observe the actual user surface rather than trust model self-report | `create-verification-skill`, `bug-fix` | `verified`: launch, doctor, drive, retain evidence and clean up; the original same-surface repro must pass. Observation still depends on the correct build/account, driver and acceptance oracle. |
| Coordinator, playbook and principle are three equivalent execution tiers | Guide Pt.2; `orchestrate` roles and placement | `needs-qualification`: playbooks are conditionally loaded reference artifacts; coordinator, optional track and workers are execution roles. Artifact taxonomy is not a permission/isolation model. Rigid trees are not a universal requirement. |
| Mature verification automatically authorizes low/zero-touch merges | `shipping`, `autopilot-full` | `refuted` as an unconditional claim: landing requires the operator's grant and a clean current independent verdict. Operator-named items remain held; forge approval requirements are not waived. Platform enforcement and deployment outcomes were not exercised. |
| pstack evaluates skills with isolated candidates and blinded judging | Full `eval` playbook | `verified` as a documented method: sanitize names/prompts, withhold rubric and chain-telling clues from candidates, use a different-family judge, and inspect candidate outputs/transcripts. A judge is not an independent deterministic product oracle. |
| Every skill release must reach a near-perfect score | Full `eval` playbook | `unverified`: this threshold is not supported by the inspected playbook. The entire upstream release pipeline was not audited. |
| High PR volume is explained by a 10–50 LOC cap and required CI below 30 seconds | Paste1; *Loops You Can Trust* discussion of small work after a large migration; Guide Pt.2 | `needs-qualification`: small standalone units are supported; these supplied numbers are not established universal prerequisites. No PR-size or CI-time distribution was independently measured. |
| Prompts alone cannot settle runtime facts; actual product feedback is required | `bug-fix`, `create-verification-skill` | `needs-qualification`: both require direct executable evidence, but prompts still specify workflow and judgment. Drivers can fail or observe the wrong build/account; runtime feedback is not the sole solution to intent or architecture problems. |
| Matt opposes multi-agent orchestration while Lauren represents automation | Matt README, `implement-spec`, `retro`, `code-review`; Lauren Guide Pt.2 | `refuted` as a categorical description of current public practice: Matt uses task-graph worktree implementers and merger subagents; Lauren uses restatement, teach/how/why and interface sketches. This does not refute an unverified quotation from the talk. |
| Matt's grill-me interview proves the AI's reasoning/code is correct | README and `grilling` | `refuted`: grilling aligns the owner's decisions by working a design-tree frontier. Actual-code feedback comes from types, tests and browser access; a coherent explanation is not a correctness oracle. |
| DDD/Clean Code labels are universal author architecture rules | Matt README and `codebase-design` | `needs-qualification`: shared vocabulary, deep modules, caller-facing leverage, test seams and deletion tests are concrete mechanisms. Do not inflate them into universal prescriptions or attribute rhetoric to the unavailable talk. |
| Planning and coding always require separate conversations | Supplied prescription; `orchestrate` | `needs-qualification`: cheap work may collapse into the direct session. Isolate a reviewer's input from the generator's persuasion narrative while retaining requirements, baseline and relevant consumer context; split only when useful. |
| One method has far higher productivity or maintenance quality | Supplied comparison | `unverified`: no matched tasks/operators or independent outcome study was supplied. Treat causal and comparative claims as hypotheses. |
| A plan-checker success attests completed work and valid receipts | Exact checker artifact and three Node CLI controls | `refuted` as an interpretation of the result: the exercised checker accepts structurally complete unchecked plans and checked plans without screenshot files. The observed boundary is structural validation, not evidence attestation. |

### Four Evidence Dimensions

| Load-bearing claim | Existence | Number/text | Attribution/process | Extrapolation |
| --- | --- | --- | --- | --- |
| Reported dialogue conflict | Video located | Original spoken wording `unknown` | Participant positions in that conversation `unknown` | A stable Matt-vs-Lauren philosophy split is not established. |
| 1,000/2,000 PR reports | Author post/article material retrieved through mirror | Reported numbers checked in the retrieved prose | Author attribution checked; counting/quality process not independently audited | Determinism, causal productivity and superior maintenance remain unverified. |
| Current workflow mechanisms | Named files inspected at immutable revisions | Described clauses checked | Public repository practice, not a reconstruction of the talk | No private/cloud production efficacy claim. |
| Checker acceptance boundary | Exact file plus subprocess execution | Exit codes, summaries and missing files observed | Offline fixture inputs and artifact digest bound below | Three fixtures do not establish general checker completeness or plugin safety. |

## Source-Bound Method Comparison

| Work | Matt's documented emphasis | Lauren/pstack's documented emphasis |
| --- | --- | --- |
| Intent | Design-tree frontier interview; owner choices separated from discoverable facts | Restatement and teach/how/why; operator corrects the compressed problem and assumptions |
| Design | Deep modules, caller interface leverage, seams and deletion tests | Usage-first examples, interface sketches, prototypes and repeated friction as design evidence |
| Parallel execution | Task-graph frontier; worktree implementers and merger subagents | Conditional playbooks; cloud workers where suitable; coordinator/track/worker roles |
| Verification | Types, tests, browser feedback; separate Standards and Spec review axes | Real-product control surface, feature map, runtime evidence, current patch binding and independent verdict |
| Learning | Mechanical retro findings routed to deterministic checks | Recurring fixes encoded as lint, metadata, helper or runtime mechanisms; judgment retained in prose |

These are differences of workflow emphasis, not exclusive categories or measurements of superiority. Metaphors and role labels are not execution guarantees.

## Executed Checker Evidence

Only the offline plan-checker surface was exercised. Original invocation: `node <scratch>/checker-smoke.mjs`, with the temporary path normalized here; Node `v25.1.0`. Each fixture was passed to the real `check-plan.mjs` subprocess in the disposable directory. No fixture task was executed and referenced screenshot files were checked absent.

Artifact identity:

- Source: `skills/poteto-mode/scripts/check-plan.mjs` at the pstack revision above.
- Exact size: **7,684 bytes**.
- Git blob: `6c07f4e903d10332702a2ac4602ada9273e71609`.
- SHA-256: `1f9e788ce90a13a9973e35e8c3a52737857c375e057bdccc13c8510a9af30f04`.
- Recovery: the raw reader dropped the final newline, yielding 7,683 bytes and a different blob. Execution stopped on the mismatch. Pinned GitHub Contents API base64 restored the exact artifact; its digest was checked before execution. The inspected source imports only `node:fs` and `node:process`.

The complete fixture contained the required reading rules, program checklist, a PR with Files/Build/You see/unit verification, ten live lanes, performance Metric/Probe/Baseline/Rule, Merge, a closing section and Appendix prototype evidence. Ten lanes referenced absent `missing/lane-<n>.png` files. The negative control removed only lane 10; the checked control changed all unchecked boxes to checked without creating receipts.

| Fixture | Boxes / live lanes | Receipts present? | Exit | Observed output |
| --- | --- | --- | --- | --- |
| `unexecuted-unchecked` | 19 / 10; unchecked | no | `0` | `1 PR sections, 0 problems` |
| `missing-lane-10` | 18 / 9 | no | `1` | `1 PR sections, 1 problems`; `lanes are [1,2,3,4,5,6,7,8,9], expected 1 to 10` |
| `checked-without-receipts` | 19 / 10; checked | no | `0` | `1 PR sections, 0 problems` |

The CLI reports `files=1 build=1 you-see=1 verify-unit=1 verify-perf=4 review-gate=0 merge=1` in all three controls, with `verify-live=10/9/10` respectively. This is **not an allegation that its advertised format check failed**. Its parser-level success cannot be promoted into proof of task execution, receipt validity, independent verification or production acceptance.

## Candidate Adoption Ledger

| ID | Candidate | Status | Local evidence and decision | Reopen trigger |
| --- | --- | --- | --- | --- |
| PML-1 | Ask high-impact owner choices rather than interrogate every discoverable fact | No change — existing coverage | [reflective-brief](../skills/reflective-brief/SKILL.md#workflow) separates look/assume/ask and treats unresolved irreversible assumptions as Human Review triggers. No new local defect demonstrated. | A real brief consumer confuses repository facts with owner decisions despite the existing clause. |
| PML-2 | Usage-first architecture, minimal one-job changes and proportional planning | No change — existing coverage | [reflective-spec-plan](../skills/reflective-spec-plan/SKILL.md#workflow), [reflective-minimality](../skills/reflective-minimality/SKILL.md#minimality-ladder) and [reflective-implement](../skills/reflective-implement/SKILL.md#verification) already carry usage-first planning, the smallest safe change and consumer coverage. | A named product exposes a missing invariant, not just different terminology. |
| PML-3 | Real-product controls and maintained feature maps | No change — already adopted locally | [verification-map-generator](../skills/verification-map-generator/SKILL.md#module-contract) already requires fresh-agent proof and four-class failure discrimination. The historical pstack pilot/promotion trail below is the evidence, not PR volume. | A real generated map cannot launch/drive/classify a product shape the current recipe does not cover. |
| PML-4 | Independent review, current-head evidence and explicit merge authority | No change — existing contracts / host boundary | [reflective-review](../skills/reflective-review/SKILL.md#evidence-tiers) and [governed-delivery](../skills/governed-delivery/SKILL.md#delivery-gate-sequence) distinguish channels, oracles and named acceptance. Patch binding, permissions and forge enforcement are host obligations. | A reproduced local contract gap; runtime scope change still requires explicit owner direction. |
| PML-5 | Blind candidate evaluation and inspect observable outputs/transcripts | Reference-only | Upstream `eval` supplies a useful evaluation design, not measured TeaPrompt efficacy. No new release threshold, universal interview or model-only acceptance rule. | An authorized matched local evaluation demonstrates a missing check in an existing evaluation surface. |
| PML-6 | Encode recurring mechanical lessons into checks | No change — existing promotion boundary | [reflective-handoff-retro](../skills/reflective-handoff-retro/SKILL.md) and [artifact-promotion](../04-agent/artifact-promotion.md) already separate incidents, repeated procedures and promotion authority. Record a named defect before adding a new guard or skill. | A recurring local consumer-visible defect has an executable repair and the relevant approval. |
| PML-7 | Cloud orchestration, universal PR/CI caps, trust curves and automatic merge claims | Not adopted | Cloud orchestration is host territory; numerical/causal claims lack independent evidence; unconditional merging contradicts the inspected source. | Specific evidence and local scope, not external popularity or a supplied Self-check. |

No new lesson, core skill, domain pack, route, runtime, schema, oracle or permanent wording test is introduced. In particular, this documentation direction does not fire unrelated held-candidate gates.

## Relationship to Earlier pstack Records

- [Initial survey and product pilots](pstack-survey-2026-09-22.md): historical source pin `53e579f1481697931fc44f5445171397cfa2b24b`; the original record's later addenda contain the wsgiLite.js discrimination and arm×scenario runs, plus later product validation. Those observations are not measurements at this survey's current upstream revision.
- [Deep-research synthesis](pstack-synthesis-survey-2026-09-22.md): preserves PS2-* dispositions and the original A/B/C pilot proposal. Later PS-C1 pilots and verification-map-generator promotion supersede the unstarted-pilot framing; the original held/proposed rows remain historical, not newly flipped here.
- [Verification-map project lesson](../PROJECT_KNOWLEDGE.md#lesson-a-verification-maps-value-is-regression-visibility-and-time-to-verify-not-correctness): maps expose drift/regression and help classify it; an acceptance oracle is a distinct authority. The existing four-product trail supports the installed generator, not causal productivity gains.
- [Agent Execution & Assurance taxonomy](agent-execution-assurance-taxonomy-survey-2026-09-30.md): AEAT-4's independent acceptance-oracle binding remains held under its named-product trigger; this source survey does not authorize it.

The healthy wsgiLite.js mini A/B reported 19/19 in 4m08s with docs and 26/26 in 5m58s without; the locked-spec healthy arm later reported 23/23 in 2m49s. Different denominators and a single pass per cell prohibit treating these as matched efficiency or quality measurements. The first full matrix's labeled seeded bug also assisted no-docs detection; later unlabeled product pilots do not retroactively remove that limitation. Effective throughput, operator time, escaped-regression rates and causal maintenance benefits remain unmeasured.

## Verification Scope and Handoff

- Executed non-model channel: exact-artifact Node CLI outputs plus filesystem observations for the three fixtures. Source prose is a separate external-source channel. Read-only model scouts organized source leads; their reports are not independent empirical efficacy evidence.
- Not exercised: original audio/transcript, embedded article images, plugin installation, app GUI, cloud-agent lifecycle, private SpaceX/Dune runtime, PR mutation, forge enforcement, merge, deployment or production acceptance.
- Documentation-only delivery: this record plus Decision Index, Case Comparison, State Ledger and regenerated `index.json`. Recording-commit verification is reported in the accompanying delivery message; the historical runtime outputs above remain bounded to their unchanged inputs.
- For future adoption: start with a reproduced local consumer failure and the smallest existing contract that can repair it. Preserve public-practice versus dialogue-attribution and structure-validation versus evidence-validity distinctions.

## Falsifiability

1. A usable original transcript/audio with grounded passages can overturn the held dialogue attributions; current repository files cannot substitute for it.
2. A matched independent outcome study may substantiate productivity/maintenance claims, but author counts or differently sized pilot checklists do not.
3. A source change that makes the checker validate executions or receipt contents invalidates reuse of the recorded structural-boundary claim; pin and exercise that new artifact before updating it.
4. A reproduced local defect that survives the mapped contracts may justify an in-place repair. This record would be wrong if it silently treated source recurrence, publicity or the documentation request as promotion authorization.

## Sources

All entries below were checked 2026-10-03; dates describe access, not publication or independent validation. Article links pair the original location with the mirror route actually used.

| Source | URL / inspected surface | Access date |
| --- | --- | --- |
| Original dialogue | [YouTube MN9dGgmLyso](https://www.youtube.com/watch?v=MN9dGgmLyso); page located, no verified dialogue | checked 2026-10-03 |
| Matt README | [README at pin](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/README.md) | checked 2026-10-03 |
| Matt intent | [grilling](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/grilling/SKILL.md) | checked 2026-10-03 |
| Matt design | [codebase-design](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/codebase-design/SKILL.md) | checked 2026-10-03 |
| Matt orchestration | [implement-spec](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/implement-spec/SKILL.md) | checked 2026-10-03 |
| Matt review | [code-review](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/code-review/SKILL.md) | checked 2026-10-03 |
| Matt learning | [retro](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/retro/SKILL.md) | checked 2026-10-03 |
| pstack README | [README at pin](https://github.com/cursor/plugins/blob/7022c81efb48d8b5eb15498ce6043a3bd74b694c/pstack/README.md) | checked 2026-10-03 |
| pstack bug tests | [tdd](https://github.com/cursor/plugins/blob/7022c81efb48d8b5eb15498ce6043a3bd74b694c/pstack/skills/tdd/SKILL.md) | checked 2026-10-03 |
| pstack structure | [principle-encode-lessons-in-structure](https://github.com/cursor/plugins/blob/7022c81efb48d8b5eb15498ce6043a3bd74b694c/pstack/skills/principle-encode-lessons-in-structure/SKILL.md) | checked 2026-10-03 |
| pstack product verification | [create-verification-skill](https://github.com/cursor/plugins/blob/7022c81efb48d8b5eb15498ce6043a3bd74b694c/pstack/skills/create-verification-skill/SKILL.md) | checked 2026-10-03 |
| pstack bug workflow | [bug-fix](https://github.com/cursor/plugins/blob/7022c81efb48d8b5eb15498ce6043a3bd74b694c/pstack/skills/poteto-mode/playbooks/bug-fix.md) | checked 2026-10-03 |
| pstack evaluation | [eval](https://github.com/cursor/plugins/blob/7022c81efb48d8b5eb15498ce6043a3bd74b694c/pstack/skills/poteto-mode/playbooks/eval.md) | checked 2026-10-03 |
| pstack landing | [shipping](https://github.com/cursor/plugins/blob/7022c81efb48d8b5eb15498ce6043a3bd74b694c/pstack/skills/poteto-mode/playbooks/shipping.md) | checked 2026-10-03 |
| pstack autonomous authority | [autopilot-full](https://github.com/cursor/plugins/blob/7022c81efb48d8b5eb15498ce6043a3bd74b694c/pstack/skills/poteto-mode/playbooks/autopilot-full.md) | checked 2026-10-03 |
| pstack orchestration | [orchestrate](https://github.com/cursor/plugins/blob/7022c81efb48d8b5eb15498ce6043a3bd74b694c/pstack/skills/poteto-mode/playbooks/orchestrate.md) | checked 2026-10-03 |
| Executed checker | [check-plan.mjs](https://github.com/cursor/plugins/blob/7022c81efb48d8b5eb15498ce6043a3bd74b694c/pstack/skills/poteto-mode/scripts/check-plan.mjs); exact artifact recovered via pinned GitHub Contents API | checked 2026-10-03 |
| Author count post | [original](https://x.com/poteto/status/2090141955695198633); [retrieved mirror](https://api.fxtwitter.com/status/2090141955695198633) | checked 2026-10-03 |
| Guide Pt.1 | [original article](https://x.com/i/article/2094151284949688320); [retrieved mirror](https://api.fxtwitter.com/status/2094457600259842065) | checked 2026-10-03 |
| Guide Pt.2 | [original article](https://x.com/i/article/2094940651607715840); [retrieved mirror](https://api.fxtwitter.com/status/2097732320606507506) | checked 2026-10-03 |
| Loops You Can Trust | [original article](https://x.com/i/article/2066965659259686912); [retrieved mirror](https://api.fxtwitter.com/status/2069824386283319343) | checked 2026-10-03 |
