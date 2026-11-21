# Crossroads Evaluation Survey — RSI, Accountability, and Computer Use (2026-11-17)
Language: English

> **Status:** source-qualified reference record (`CRS-DOC1`); no Skill, prompt-body, operating-rule, or runtime change. The owner supplied a synopsis and an adversarial critique of the Crossroads interview with Chenyang Zhao and requested a transcript search and survey. Both supplied texts are claims to check, not speaker quotations or instructions. A platform transcript entry was located, but a readable full transcript was not obtained.

## Research Question

What do the episode and related primary sources support about evaluable optimization, human accountability, and AI infrastructure—and which claims in the supplied synopsis or critique need correction? Does any finding establish a missing TeaPrompt contract?

## Direct Recommendation

**Retain the source distinctions and technical corrections; leave Skills and existing acceptance rules unchanged.** The useful mechanisms—bounded optimization, protected evaluation, evidence-qualified claims, and named authority—are already covered. Neither an optimization anecdote nor a critique of it establishes unlimited self-improvement, lossless evaluation, or a new governance rule.

## Evidence Used

All access and documentation checks below were made on **2026-11-17**. Source existence/text, measurement provenance, and extrapolation are separate checks.

| ID | Source actually inspected | Evidence class and boundary |
| --- | --- | --- |
| E1 | [YouTube episode `IaoYLdvibNU`](https://www.youtube.com/watch?v=IaoYLdvibNU), Koji杨远骋; [official Xiaoyuzhou episode `6af936ea14d01a26f8a9fd94`](https://www.xiaoyuzhoufm.com/episode/6af936ea14d01a26f8a9fd94) | Primary publisher metadata/show notes. Published 2026-11-15; YouTube duration 1:06:25. Chapter markers corroborate the topics, not exact spoken wording or experiments. |
| E2 | [Platform transcript entry](https://oia.xiaoyuzhoufm.com/player/6af936ea14d01a26f8a9fd94?openTranscript=true), linked from the syndicated description | Entry exists; retrieval redirected to an H5 app-download page. Transcript content was not exposed. |
| E3 | [Detailed Digest compilation](https://digest.hustwj.com/youtube/用%20Kimi%20加速%20Kimi：AI%20Infra%20研究者赵晨阳的十个%20Aha%20Moments); [wav episode page](https://wav.pub/e/WPTK_vo7WWBoOjNXJm71c); [Podcast Atlas episode](https://podcastatlas.ai/episodes/lhhxptqoanrsmgih0htfelq-znbg-lhhxptqoanrsmgih0htfelq-znbg) and [source note](https://podcastatlas.ai/wiki/sources/lhhxptqoanrsmgih0htfelq-znbg-lhhxptqoanrsmgih0htfelq-znbg) | Secondary material. Digest identifies a local-ASR-derived structured compilation with editorial name corrections; Atlas explicitly identifies structured-summary input. None is a verbatim substitute. Agreement does not establish independent provenance. |
| E4 | [OpenRSI × SGLang-Omni](https://index.openrsi.foundation/blog/2026/openrsi-sglang-omni/); [Introducing OpenRSI Index](https://index.openrsi.foundation/blog/introducing-rsi-index) | Primary project process/benchmark reports: fixed-weight runtime optimization, human task design/review, private tests and fresh evaluation environments. Published outcomes remain upstream-reported, not locally reproduced. |
| E5 | [SGLang: Kimi K3.1 Pro Day-0 support](https://www.sglang.io/blog/kimi-k3.1-pro-day0-support), 2026-11-04 | Primary serving/RL report. Establishes documented serving support, not that Kimi authored the code serving itself. |
| E6 | [OpenAI prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching); [Anthropic prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) | Primary API documentation. Image-containing contexts can be cached; eligible exact prefixes and provider-specific invalidation rules matter. No API experiment was run. |
| E7 | [Microsoft standard-control UI Automation support](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-controlsupport); [MSAA interoperability](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-msaa); [Playwright ARIA snapshots](https://playwright.dev/docs/aria-snapshots); [Origin Automation Server](https://docs.originlab.com/com/); [Origin external Python](https://docs.originlab.com/externalpython/) | Primary interface documentation, not an application-coverage or automation-success measurement. |
| E8 | [Python `if` grammar](https://docs.python.org/3/reference/compound_stmts.html#if); [Ruff RET505](https://docs.astral.sh/ruff/rules/superfluous-else-return/); [Ruff C901](https://docs.astral.sh/ruff/rules/complex-structure/); [PEP 8 introduction](https://peps.python.org/pep-0008/#introduction) | Primary language/style documentation; no linter, defect-rate study, or contributor-selection experiment was executed. |
| E9 | [BIEN basic-income definition](https://basicincome.org/about-basic-income/) | Primary definition: periodic, cash, individual, universal and unconditional. Not evidence of any program's political or economic effects. |

### Transcript Acquisition Outcome

- The YouTube reader returned no transcript, and the captured public player response had `captions: null`. This does not establish that no transcript exists elsewhere.
- The publisher advertises a WeChat text edition; E2 is a separate platform transcript entry. Neither yielded readable transcript content through the inspected public pages. The [official Bilibili alternative](https://www.bilibili.com/video/BV1fTsE62Ex6/) returned a CAPTCHA page; no bypass was attempted.
- E3 is the useful text alternative, explicitly **a structured secondary compilation**. [30Tool's roundup](https://www.30aitool.com/daily/read/10390/4/) and [Stream Reducer's AI-assisted summary](https://reducer.xgoose.org/items/14262) are additional summaries, not transcript recovery. No locally generated ASR was substituted.
- Exact speaker wording remains unverified. The source access limit is part of the result, not permission to attribute a summary verbatim.

## Findings and Claim Ledger

### 1. Evaluation and RSI: Real Engineering, Bounded Conclusions

| Claim / item | Source check and status | Conclusion and remaining limit |
| --- | --- | --- |
| An 80M speech model improved 1700% over a weekend | E1's 06:36 show notes explicitly publish the 80M / Claude / weekend / 1700% claim: **verified text; underlying experiment unknown** | The show notes do not identify Opus 5.5, a model checkpoint, hardware, baseline, precision, workload, metric denominator or quality contract. Those details in the supplied synopsis are not thereby verified. |
| The result means 17× throughput, not better output quality | **Needs qualification**: no matching metric definition or experiment receipt | An increase **by** 1700% would mean an 18× final higher-is-better value; **at** 1700% of baseline would mean 17×. Neither arithmetic establishes the actual metric. Throughput, latency and real-time factor are not interchangeable. Do not guess the model from parameter count. |
| Fixed-weight inference optimization cannot count as RSI | E4 describes accepted runtime improvements becoming later baselines: **verified upstream process description** | [INFERENCE] A system-level RSI interpretation is coherent without weight updates. Calling it only AutoML or kernel tuning understates the hypothesis/experiment/engineering loop. It still does not demonstrate a measured feedback loop that increases the optimizer's research capability, let alone unbounded improvement. |
| Kimi K3.1 wrote its own B300 inference engine | E1's 01:16 notes mention Kimi acceleration/B300/OpenRSI; E5 documents Kimi K3.1 Pro serving: **context corroborated; self-authorship unknown** | E5 attributes work to collaborating teams and describes NVIDIA GB300 NVL72 deployments. It does not supply the matching Kimi-as-coder trajectory or engine diff. Do not substitute served-model identity for authoring-model identity, or silently equate B300 with the report's deployment configuration. Its separate Miles RL results are a different evidence chain. |
| A clean private verifier guarantees correctness or a final unseen holdout | E4 describes isolated private tests, fresh Judge environments, feedback to the agent and best-valid-submission selection: **design verified; stronger guarantee unsupported** | Evaluation isolation is not distributional novelty. Repeated feedback can still select for evaluator peculiarities. A fresh environment is not automatically an untouched final statistical holdout. No such holdout was established for the 1700% anecdote. |
| The speaker ignored Goodhart effects and cross-model regressions | E1 includes metric imbalance among benchmark topics; E3 describes local gaming, cross-model regressions and environmental variables: **critique needs qualification** | These sources undermine the categorical omission charge, though exact wording remains unknown. Goodhart is a valid boundary to the conclusion, not evidence that this speaker failed to consider it. |
| What can be evaluated can be improved indefinitely without mistakes | E4 explicitly limits search by compute, evaluator quality and review bandwidth: **universal extrapolation unsupported** | [INFERENCE] A usable score enables optimization attempts; it guarantees neither a feasible gain nor improvement in omitted user outcomes. Source-reported guards and accepted changes are narrower evidence than a no-mistakes claim. |

E4 offers substantive evidence rather than only rhetoric: it reports merged serving changes and distinguishes human task/system design and review from agent experimentation. It also discloses before/after ranges containing other changes, image/version differences, startup and memory costs, tail-latency regressions, and reused reference recordings. WER checks transcription accuracy, not all perceptual speech quality. The report explicitly does not establish unchanged waveforms or perceptual quality. These limitations narrow causal attribution; they are not grounds to dismiss every localized gain. **None of E4's separate benchmark results verifies the 80M/1700% anecdote.**

### 2. Responsibility, UBI, and Maintainer Authority

The following are analytical rulings on the supplied synopsis and critique, not findings about the speaker's motives or authenticated quotations.

| Claim / item | Status | Assessment |
| --- | --- | --- |
| Human responsibility is the final barrier to replacement | **Unknown as a general causal or employment claim** | [INFERENCE] Legal authority, institutional accountability, liability, practical ability and willingness to delegate are distinct. Keeping a named human accountable does not determine how many human roles remain, or prove that capability and cost cease to matter. |
| UBI means benefits can be withheld when recipients disobey | **Refuted as a definition; actual policy effects unknown** | E9 defines unconditional payment. Conditional welfare is not the same concept. A broader concern about dependence on institutions remains a legitimate hypothesis, but loss of freedom is not established by the definition or this interview. No program-level causal evaluation was reviewed. |
| BDFL governance necessarily contradicts rejecting elite control over society | **Needs qualification** | [INFERENCE] A bounded project's decision rights and societal coercive power have different constituencies, exit options and accountability. The analogy can expose a tension worth asking about; it is not a contradiction without a shared principle and scope. Project consistency likewise does not by itself legitimate every rule. |
| Ming-era administration, *Ming Dynasty 1566*, or *The Wanli Fifteenth Year* proves current AI-governance effects | **Unverified attribution; historical/causal adjudication declined** | Treat these as analogies. The survey did not review the primary historical texts or establish which statements were spoken. Neither the speaker's motives nor a present-day political conclusion follows from the supplied literary reading. Ruling owner for this scope: survey coordinator; historical interpretation needs a separate primary-text question. |

The strongest useful version of the accountability thesis is narrower: identify who can authorize an action, who evaluates its outcome, and who owns remediation. That is a governance design requirement, not proof that a person cannot be displaced or that an audit log establishes responsibility.

### 3. Computer Use and Code Style: Corrections Apply to Both Texts

| Supplied proposition | Primary check / status | Corrected boundary |
| --- | --- | --- |
| Screenshots inherently prevent prefix/KV-cache reuse | E6: **refuted as a universal** | Both providers document image-containing cached context. Replacing content inside a prefix breaks matching from the changed content onward; appending an observation does not inherently replace prior history. Eligibility, rendering, residency and provider settings still matter. Anthropic specifically lists image additions/removals as message-cache invalidators, so append-only image history is not a universal reuse guarantee either. |
| An accessibility tree is a stable, cheaper cache prefix | E6/E7: **conditional, not measured** | Names, values, selection, expansion, ordering and tree structure can change. A tree serialized into a request obeys prefix-matching constraints too. Semantic access and potentially smaller observations are good reasons to investigate it; better hit rate, latency and task success require measurements. Cache-hit pricing, actual KV reuse and end-to-end speed are separate outcomes. |
| Old Win32 applications generally have no useful accessibility path | E7: **blanket impossibility refuted; prevalence unknown** | Standard Win32 controls have UIA support and MSAA interoperability, with control/version limitations, including ComCtrl32 v6 for full standard-control support. Custom controls can still lack useful semantics. No application population or coverage rate was measured. |
| Origin has no API/SDK, leaving vision as the only automation route | E7: **blanket automation-absence claim refuted** | OriginLab documents COM automation and external `originpro` APIs. `originpro` requires Windows and a local Origin 2021+ installation. This does not prove that the episode's application version, license or target task is supported, or that every UI workflow is exposed. |
| Every `if` needs `else: pass`, even after `return`, to be correct | E8: **language necessity refuted; defect-reduction effect unknown** | Python makes `else` optional; RET505 recommends removing an unnecessary post-return `else`. PEP 8 allows project-specific style. A maintainer may choose a house convention and follow it consistently, but that does not measure fewer defects or establish actual enforcement. |
| Early return automatically lowers cyclomatic complexity | E8: **refuted as an automatic consequence** | RET505 discusses reduced nesting. C901 measures decision points plus one. [INFERENCE] Keeping the same decisions while removing a redundant `else` generally keeps the same McCabe complexity. Readability and cognitive complexity are different claims. |
| Satisfying style rules or adding an attribution comment proves responsible human authorship | **Unsupported inference** | [INFERENCE] Observable, reproducible conventions cannot by themselves authenticate authorship, comprehension or accountability. A rule may still improve coordination or screen willingness to follow project norms. Neither universal model compliance nor a beneficial contributor-selection effect was measured here. |

A hybrid of structured APIs/accessibility and vision is a plausible application design, not an observed winner in this survey. Browser DOM access, desktop UIA, screenshot perception and transaction correctness are different surfaces. API availability does not prove complete coverage; visual observation does not prove a successful semantic action.

## Evidence vs Inference

- **Observed:** publisher metadata and chapter text; a transcript entry with an access limit; explicitly secondary compilations; primary project/API/language/definition documents. These support the source-qualified ledger above.
- **Not independently measured:** the episode's performance gain, upstream benchmarks, cache hit rates, application automation coverage, defect rates, employment effects, contributor selection or political outcomes. Two research slices helped inspect sources; agreement between them is not independent experimental verification.
- **Inference:** the scope distinctions connecting those sources to RSI, governance and TeaPrompt. The same evidence discipline applies to the supplied critique: a sound concern does not validate its arithmetic, terminology or accusation of omission.

## TeaPrompt Contract Map

| Useful distinction | Existing local surface | Disposition |
| --- | --- | --- |
| A summary is not its cited source; verified text is not verified measurement | [Reflective Research — State Ledger](../skills/reflective-research/SKILL.md#state-ledger); [Reflective Review — Four Evidence Dimensions](../skills/reflective-review/SKILL.md#four-evidence-dimensions) | Already required. This record applies the distinction to the synopsis and critique alike. |
| Optimizer/verifier separation, bounded loops and human acceptance | [Flow Loop Harness](../skills/flow-loop-harness/SKILL.md); [Governed Delivery](../skills/governed-delivery/SKILL.md); [earlier evaluation/optimizer survey](coordinate-codex-tasks-eval-survey-2026-09-30.md) | Existing method contracts. Host enforcement and untouched holdouts require actual implementation/evidence; no new runtime proposed. |
| Approval, evidence, execution, acceptance and accountability differ | [Agent Governance Scaffold](../skills/agent-governance-scaffold/SKILL.md); [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md) | Already covered, including audit not equaling accountability. No BDFL or political policy imported. |
| Corrections should become relevant executable checks, not arbitrary prose/style accumulation | [Agent Trust Pyramid survey](agent-trust-pyramid-survey-2026-11-15.md); [Project Knowledge — Standing Non-Goals](../PROJECT_KNOWLEDGE.md#standing-non-goals) | Already covered. Cache layout, UI adapters and benchmark harnesses are host/product engineering, not a missing Skill. |

### Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| CRS-DOC1 | This source-qualified record and catalogue discovery | Recorded: reference documentation only | Preserve transcript limits, primary-source corrections, and unresolved experiments. Refresh on a retrievable publisher transcript or matching benchmark receipt. |
| CRS-SK1 | New Skill or change to existing Skill/prompt contracts | No change | No local contract defect established. Missing local recurrence data remains unknown, not zero demand. Reopen on a reproduced local consumer failure. |
| CRS-RUN1 | Install OpenRSI, run GPU/model trials, or add a CUA/cache runtime | Not adopted | Not authorized by a source survey; no local requirement or operational acceptance record. Needs separate host, cost and effect authority. |
| CRS-RULE1 | Import unlimited-RSI, screenshot-no-cache, style-as-authorship, or universal social-policy claims | Rejected as general rules | Claims exceed the evidence or collapse distinct scopes. A narrower tested proposition would require its own evidence and decision. |

## Falsifiability, Risks, and Handoff

The evidence is sufficient for a **reference-only/no-Skill-change** decision: each load-bearing claim has a checked source boundary or an explicit unknown. No further broad source search is needed to make that decision.

- A readable transcript can change attribution and interpretation, but cannot by itself reproduce a benchmark. The original speaker's exact wording remains open, not disproved.
- A matched experiment receipt must identify the model/agent versions, baseline and treatment, hardware, workload, metric and quality constraints before the 1700% result is reassessed. Other SGLang gains do not fill that gap.
- Live API/vendor/rule pages are checked-date documentation, not immutable executable pins. Recheck the relevant provider, Origin version or control implementation before a deployment recommendation. This survey ran no such implementation.
- Documentation scope is the new record, existing external-adoption catalogue and generated `index.json`. Existing prompt bodies, Skills, routing, governance and runtime are untouched; no optional prompt reference is needed.
- Delivery checks are canonical index regeneration, its existing freshness test, scoped relative-link/anchor validation, and browser navigation through the rendered catalogue to this record. These check documentation delivery, not model efficacy. Full repository gates, upstream suites, provider/model calls and installations are outside this scope. Commit/push are not authorized.
