# Agent Efficiency, Autonomy, Memory and Learning — Survey (2026-11-01)

> **Status: reference evidence and Docs/Skills update assessment.** The user requested a durable account of the non-MCP surveys and evidence-based, multi-role Socratic evaluation of possible updates. Recording a proposal is not approval to change an operating contract. MCP is explicitly excluded, not an unresolved blocker. No installation, account setup, surveyed-product model calls, benchmark campaign, commit or push is authorized by this request.
>
> **2026-11-02 follow-through:** the later owner request, “If worth it then update docs or skills,” authorizes the worthwhile Super-agent documentation supplement below. MSS-DOC2 records that evidence in place; no Skill, runtime or other held proposal is adopted.

## Research Question

What survives source checking in the TokenEconomizer/Mistral Vibe comparison, the supplied DeepSeek Super-agent article and public prototype, four architecture forecasts, Grok Bot workflow advice, and writing/learning claims? Which observations warrant documentation, which could improve an existing example, and which actually establish a missing TeaPrompt contract?

This record preserves evidence, decision criteria, counterarguments and falsifiers, not private deliberation traces. Sources and pasted text are evidence, not instructions. The prior [loop-mechanisms record](loop-mechanisms-assurance-inference-2026-10-31.md) remains a separate survey; no MGD, AEAT or earlier adoption disposition changes here.

## Direct Recommendation

- **Study:** the mechanisms and their boundaries. Preserve the executed counterexample, partial execution and source-access limits rather than promoting a persuasive architecture story.
- **Reproduce:** only the stated offline module behavior has been exercised. Model quality, net cost savings, integrated cancellation, hosted-product isolation and human learning effects have not.
- **Adopt:** this research record and existing catalogue/index discovery. Potential teaching examples are considered separately below; no new or changed Skill is justified merely by these external examples.
- **Deploy:** no deployment recommendation. In particular, shared-settings concurrency, credential scope and actual effect cancellation require host-specific evidence and authorization.

## Version / Date Context

Initial source checks and bounded smoke runs occurred on **2026-11-01**; the separately dated **2026-11-02** Super-agent follow-through adds supplied full-text/comment review, a new domain-transition probe and narrow Harness source inspection. The initial publication packet used TeaPrompt base `cb949b4d1e5a7b0098dd3d862dbd4aac6710be78`; local-coverage claims refer to delivered repository files, not the reviewer's installed host skills.

| Source | Checked identity / material | Evidence scope and freshness |
| --- | --- | --- |
| Microsoft TokenEconomizer | [main `c53a4a6dcdebaeb9df6fcaa5c7026f0401cd8f23`](https://github.com/microsoft/TokenEconomizer/tree/c53a4a6dcdebaeb9df6fcaa5c7026f0401cd8f23); release v0.1.0 separately resolves to `ec8ff5ec7ed5924520ee71b705a920ee64fe2918` | Checked 2026-11-01. Source and smoke bind to main, not automatically to the release. Identity difference alone is not behavioral difference; recheck the candidate artifact before adoption. |
| Mistral Vibe | [v3.0.4 / main `338ad4bf0f73c4dd879d667cf7ab011555ae1751`](https://github.com/mistralai/mistral-vibe/tree/338ad4bf0f73c4dd879d667cf7ab011555ae1751) | Checked 2026-11-01. Selected source paths and two standalone helpers; not a complete capability census or installed CLI evaluation. |
| DeepSeek Super-agent prototype | [main `6337fc823ce20251c8de8085948165c81aaa701e`](https://github.com/deepseek-ai/dsh-superagent-prototype/tree/6337fc823ce20251c8de8085948165c81aaa701e) | Checked 2026-11-01; rechecked unchanged 2026-11-02. Public research code and separately dated domain-module probes; not the internal system described by the article. |
| Supplied DeepSeek article | User-provided `paste-6.md`, attributed to `hao.cnyes.com`; [original-design URL attempted](https://zhuanlan.zhihu.com/p/2099987320443237060) | Checked 2026-11-01 at the stated access tier: secondary article text was read; original Zhihu body returned HTTP 403. Article-only numbers remain secondary-attributed. |
| Supplied full Super-agent essay and comments | User-provided `paste-7.md`, attributed to DeepSeek, “Super-agent Design Exploration: Towards a More Autonomous Agent System,” edited 2026-11-01 | Checked 2026-11-02. Supplied article and comments read in full; original Zhihu body still returned HTTP 403. Transcription fidelity, figure bodies and raw experiment data remain unverified; the earlier secondary account is not silently upgraded to fetched primary evidence. |
| DeepSeek Harness, async slice | [master `ce7073d51254c26cd63b22a60835b8f948deb447`](https://github.com/deepseek-ai/deepseek-harness/tree/ce7073d51254c26cd63b22a60835b8f948deb447) | Checked 2026-11-02. Background jobs, completion delivery and cancellation source only; not a released-artifact evaluation, live-host run or whole-runtime recertification. |
| Four architecture forecasts | User-provided transcription/analysis, checked against the primary sources linked below | Original forecast image was not supplied; image authorship and wording are not certified. Future deployment predictions remain predictions. |
| Grok Bot | [official skills/routines](https://docs.x.ai/grok-bot/skills-routines-and-automations), [Bots](https://docs.x.ai/grok-bot/bots), [Vault](https://docs.x.ai/grok-bot/vault), [approvals/security/privacy](https://docs.x.ai/grok-bot/approvals-security-and-privacy) | Living documentation, checked 2026-11-01; no account or hosted workflow exercised. Recheck on product/rollout changes before use. |
| Human writing and learning | Original indexed meta-analysis abstract; original ACL study abstracts and label-preference paper text, linked below | Published-source evidence, not local replication. Populations, tasks and measured constructs constrain each conclusion. |

## TokenEconomizer and Mistral Vibe

### Source Findings

The pinned [architecture diagram](https://github.com/microsoft/TokenEconomizer/blob/c53a4a6dcdebaeb9df6fcaa5c7026f0401cd8f23/docs/assets/framework_overview.png), checked 2026-11-01, names **three mechanisms**: micro-skills, tool pruning and failure-loop intervention. The five stages below are an analytical comparison requested for this survey, not five labels or components claimed by upstream.

| Analytical stage | TokenEconomizer at the checked pin | Mistral Vibe at the checked pin | Bounded conclusion |
| --- | --- | --- | --- |
| Observe | Recorded sessions, tool outcomes, edits/errors and verification signals | Persisted session messages and runtime state | A trace is input evidence, not learned operating knowledge. |
| Learn across sessions | Micro-fact proposal, promotion, firing and retirement lifecycle | File/registry skill discovery and session loading in inspected paths | Static skill loading or history replay does not demonstrate the same experience-conditioned lifecycle. No repository-wide absence claim. |
| Economize tools/context | Usage-informed tool proposals applied through host settings | Configured tool filtering and summary-based compaction | Both can affect context, but configured filtering and learned pruning are not interchangeable mechanisms. |
| Intervene in loops | Detector and optional judge/redirect; live final rung is a notice | Iteration/run budgets and scheduled-loop constraints | A warning, a scheduler limit and actual cancellation are different effects. |
| Account for feedback/cost | Execution plus mechanism LLM overhead, using cache-aware cost weights | Usage/run-budget controls in inspected paths | No matched task/quality/cost comparison was performed; this table is not a savings benchmark. |

Source paths (checked 2026-11-01): TokenEconomizer [`microskills/lifecycle.py`](https://github.com/microsoft/TokenEconomizer/blob/c53a4a6dcdebaeb9df6fcaa5c7026f0401cd8f23/tokeneconomizer/microskills/lifecycle.py), [`plugin/denylist.py`](https://github.com/microsoft/TokenEconomizer/blob/c53a4a6dcdebaeb9df6fcaa5c7026f0401cd8f23/tokeneconomizer/plugin/denylist.py), [`plugin/controller.py`](https://github.com/microsoft/TokenEconomizer/blob/c53a4a6dcdebaeb9df6fcaa5c7026f0401cd8f23/tokeneconomizer/plugin/controller.py), [`ledger.py`](https://github.com/microsoft/TokenEconomizer/blob/c53a4a6dcdebaeb9df6fcaa5c7026f0401cd8f23/tokeneconomizer/ledger.py); Vibe [`skills/manager.py`](https://github.com/mistralai/mistral-vibe/blob/338ad4bf0f73c4dd879d667cf7ab011555ae1751/vibe/core/skills/manager.py), [`tools/manager.py`](https://github.com/mistralai/mistral-vibe/blob/338ad4bf0f73c4dd879d667cf7ab011555ae1751/vibe/core/tools/manager.py), [`compaction/context.py`](https://github.com/mistralai/mistral-vibe/blob/338ad4bf0f73c4dd879d667cf7ab011555ae1751/vibe/core/compaction/context.py), [`loop.py`](https://github.com/mistralai/mistral-vibe/blob/338ad4bf0f73c4dd879d667cf7ab011555ae1751/vibe/core/loop.py), and [`turn.rs`](https://github.com/mistralai/mistral-vibe/blob/338ad4bf0f73c4dd879d667cf7ab011555ae1751/harness/core/src/turn.rs).

**Local engine does not imply local inference.** TokenEconomizer's [live configuration](https://github.com/microsoft/TokenEconomizer/blob/c53a4a6dcdebaeb9df6fcaa5c7026f0401cd8f23/tokeneconomizer/plugin/config.py#L144-L169), checked 2026-11-01, defaults to micro-skills off, tool pruning auto and LoopGuard nudge. [Sidecalls](https://github.com/microsoft/TokenEconomizer/blob/c53a4a6dcdebaeb9df6fcaa5c7026f0401cd8f23/tokeneconomizer/plugin/sidecall.py#L1-L42) use the already-authenticated host CLI and consume its account/billing context. No extra API key does not mean no provider transfer, no quota consumption or zero overhead. These calls were not executed here.

**Detector label does not imply cancellation.** The live [controller's `abort` branch](https://github.com/microsoft/TokenEconomizer/blob/c53a4a6dcdebaeb9df6fcaa5c7026f0401cd8f23/tokeneconomizer/plugin/controller.py#L338-L354), checked 2026-11-01, deliberately emits a stop notice rather than stopping the host turn. The offline detector's labels must not be reported as a demonstrated host-stop mechanism.

**Settings timing is a separate boundary.** The pinned denylist documentation says automatic application waits for a proposal and a quiet period, affects the next session rather than changing a running session's tool set, and can cause a resumed conversation's history to be re-cached with the new tool set. This is a host cache effect described upstream, not evidence that TokenEconomizer edits prior transcript text. Neither the quiet-period scheduling nor a host's cache behavior was exercised here.

### Executed Boundary and Counterexample

The coordinator executed actual upstream Python modules under a macOS sandbox denying network access and file writes outside an isolated scratch root. The CLI used synthetic HOME/repository state. No model judge or authenticated agent session was invoked.

| Probe | Observed result | Boundary |
| --- | --- | --- |
| Micro-fact lifecycle | Three distinct-file confirmations made the high-stakes fixture ACTIVE but not injectable; its next exercise enabled injection; contradiction retired it. Repeated same-file confirmations did not satisfy the distinct-file fixture. | Synthetic lifecycle inputs, not evidence that generated facts are true or useful. |
| Settings ownership | Restore preserved the pre-existing `Bash` denial and owner field; another checkout's receipt and `Grep` denial survived. | Tested JSON host-settings path, not every host adapter. |
| Parent symlink | A `.claude` parent symlink escaping the repository was refused; outside bytes remained unchanged. | Tested parent-symlink case, not exhaustive path/security proof. |
| Concurrent settings writer | A second real process added `concurrent_owner_edit` after the plugin read; `denylist.apply` added `WebFetch` but erased that concurrent field. | Deterministic scheduling injection at `_read_settings`; actual read-modify-write path and second-process write, not a spontaneous stress-test rate. |
| Loop detector | Alternating edits and repeated failed checks produced `nudge` at fixture call 20 and `abort` at call 40. | Explicit envelope 10 and synthetic trace; these are not universal/live default thresholds. Controller cancellation was not executed. |
| Actual status CLI | `python3 -B -m tokeneconomizer.plugin.cli --cwd <scratch-repo> --host claude status --json` exited 0; host `claude`, zero recorded sessions. | A real CLI invocation over empty isolated state, not host integration. |
| Vibe helpers | Summary extraction returned `Keep task X.`; missing/empty summaries returned `None`; 30-second schedule accepted and 15 seconds rejected. | Summary parser and interval validator only, not model compaction or Rust iteration limits. |
| Vibe tool manager | Import could not run: `No module named 'dotenv'`. | No dependency installed. Filtering remains source-verified only. |

The concurrency reproduction starts with `{"owner":"initial"}`. A wrapper calls the real `_read_settings`, then synchronously starts a second Python process which writes `concurrent_owner_edit="must-survive"`, then returns the earlier snapshot. Calling the real `denylist.apply(repo, ["WebFetch"], store)` returns `["WebFetch"]`; final bytes omit the concurrent field. The wrapper is restored afterward. [`_apply_json_list`](https://github.com/microsoft/TokenEconomizer/blob/c53a4a6dcdebaeb9df6fcaa5c7026f0401cd8f23/tokeneconomizer/plugin/denylist.py#L244-L262), checked 2026-11-01, reads and later replaces settings; the inspected CLI apply path does not supply a settings-version transaction. **[INFERENCE]** Adoption with concurrent writers needs an enforced serialization/reconciliation contract; neither a successful return nor an ownership receipt proves preservation of other writers' changes. No upstream fix was attempted.

**Failure accounting:** the first Python driver exited 1 after the lifecycle/ownership/symlink/concurrency assertions because its later no-edit-churn loop fixture wrongly expected an intervention. The strict no-model fallback requires churn as well as repeated failure. The remaining-check driver used the corrected trace and exited 0; earlier file mutations were not rerun. This was a probe-input error, not an upstream regression, and the initial run is not relabeled as passing.

### Socratic Assessment

- **Does fewer context tokens establish a cheaper completed task?** No. Mechanism sidecalls, cache pricing, failed attempts and accepted-output quality change the denominator. A matched end-to-end measurement could change the adoption decision; the diagram cannot.
- **Does Vibe's different mechanism imply it lacks learning everywhere?** No. The comparison only establishes the inspected mechanisms and bounded smoke; it is neither a product ranking nor an exhaustive absence proof.
- **Does a reproduced external lost update prove TeaPrompt needs a new rule?** No. The delivered Research contract already names concurrent-write probes, and Runtime Trust Boundary already assigns canonical-state concurrency to the host. A worked example may aid application without repairing missing policy.

## DeepSeek Super-agent: Article, Prototype and Product Are Different Surfaces

The public [README](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/6337fc823ce20251c8de8085948165c81aaa701e/README.md), checked 2026-11-01, explicitly calls the code a research prototype for reference, not an official product or production-ready software. It also says the publication differs from the internal version and design article, with some article directions unimplemented. Its existence is primary evidence for the published prototype, not for every feature attributed to the internal system.

The source, checked 2026-11-01, describes a DSH/Cordis bundle for one configured GitHub repository, optionally Feishu. Its useful design separation is event intake → assessment → authorized ticket/mandate → worker execution → delivery and human-facing state. [Authorization](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/6337fc823ce20251c8de8085948165c81aaa701e/docs/002-authorization.md) distinguishes observation of inferred work from an explicit authorized request. Subscriptions carry context, not new authority. Worker activity or a terminal worker report does not by itself establish that the user received an acceptable result.

At this pin, `observe` assesses inferred candidates and records a positive result as ignored / "would accept"; explicit requests still work. A Policy version change sends affected live tickets a notice and does **not** immediately revoke their Mandates. Before resuming an executor-ended ticket, the current policy is revalidated: a valid human follow-up can resume the same work under its unchanged Mandate without a new Eval/Decision; failed revalidation leaves it ended and releases messages to a fresh Eval when no other ticket owns them. A person-stopped ticket does not resume this way. A stop command and an ordinary message saying "stop" also take different entry paths. These distinctions come from the authorization document and `Tickets.wake`, not a live-host cancellation test.

The coordinator's Bun smoke imported the actual [`Intake`](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/6337fc823ce20251c8de8085948165c81aaa701e/src/core/intake.ts), [`Tickets`](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/6337fc823ce20251c8de8085948165c81aaa701e/src/core/tickets.ts), model and [stage](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/6337fc823ce20251c8de8085948165c81aaa701e/src/core/stage.ts) modules (source checked 2026-11-01) with in-memory storage and captured executor ports. It exited 0 and observed:

- Duplicate intake retained one input; a live follow-up resolved to its existing ticket owner without a new assessment request.
- Context-only input did not reopen an ended ticket as an authorized instruction; it queued assessment.
- A human-stopped ticket remained stopped; the new event queued assessment rather than implicitly resuming it.
- A newly received event under an invalidated mandate queued assessment without worker fan-out or executor calls.
- Stage classification prioritized ended state, then delivery error, then human review in the exercised fixtures.

This proves those domain transitions only. It did not boot DSH, execute a worker model, access GitHub/Feishu, exercise the Eval/Policy machinery, test external-effect reconciliation or prove OS isolation. The policy revalidation callback in the smoke was a fixture; [policy-change processing](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/6337fc823ce20251c8de8085948165c81aaa701e/src/policy.ts) and the real stop/cancellation path, checked 2026-11-01, remain source-inspected rather than integrated execution evidence.

### Secondary Performance Claims

The supplied `paste-6.md` reports synthetic workloads of roughly 300 messages including roughly 20 actual work requests, repeated five times per setup. It reports task p50 12.4 minutes and p95 15.7 minutes, versus a neutral single-session baseline p95 of 29.5 minutes. It explicitly limits the exercise to scheduling with simulated tool behavior, not real coding quality. Its cache-read and batching figures belong to the same secondary account; no raw workload, benchmark harness or internal service was reproduced here. The inaccessible original article prevents upgrading attribution merely because the public repository is official-hosted.

**Socratic questions:** What becomes authorized when a thread is observed? Only the applicable explicit request or current policy, not the subscription itself. What does an idle worker prove? Not delivery or business acceptance. What would justify adopting the architecture? A named host's task/authority/delivery requirements and end-to-end evidence, not the simulated latency numbers alone.

**[INFERENCE]** A useful transferable design question is where attention, authority and delivery are tracked separately. TeaPrompt can ask that question through existing lenses; it does not acquire the prototype's runtime by recording it.

### Full-Text Follow-through (2026-11-02)

The new material is the supplied full essay and discussion, not a prototype revision. This supplement preserves the initial evidence above and distinguishes supplied-text claims, inspected public code, executed domain behavior and design inference. The online original and its figures were not obtained. Two read-only source-gathering slices informed the review; they are not another adoption panel or independent benchmark replications.

#### Executed Multi-owner Handback

On 2026-11-02, a standalone Bun driver imported the actual pinned [`Engine`](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/6337fc823ce20251c8de8085948165c81aaa701e/src/core/engine.ts) (source checked 2026-11-02) and core dependencies. It ran under macOS `sandbox-exec` with network denied and writes confined to the probe directory. Repositories were synthetic in-memory implementations, and executor ports captured requests rather than executing work.

The scenario bound two scoped tickets, `fix-a` and `fix-b`, to one thread through `bindThread`, added `context-reader` through `followForContext`, received one cross-topic event through `receive`, and called `handback` for each owner in sequence. The process exited **0** with these observations:

| Transition | Observed domain result |
| --- | --- |
| Receive the shared event | Delivery requested for all three tickets; owners are only `fix-a` and `fix-b`; no fresh evaluation is pending |
| `fix-a` hands back | Returns false for queued evaluation; `fix-b` still owns the event |
| `fix-b` also hands back | Returns true; no owners remain and the event enters the pending evaluation queue with both reasons retained |
| After both handbacks | All three original Mandate scopes and subscriptions remain unchanged |

This exercises the core's routing and ownership transitions, not SQLite transaction/concurrency behavior, semantic scope judgment, actual worker delivery, GitHub/Feishu, or a running DSH host. An `atomic` wrapper in an in-memory fixture is not transaction proof. Re-evaluation being queued does not prove that the next model decision or cross-task solution is correct.

#### Reported Benchmark Denominators

The supplied full text, checked 2026-11-02, §7.1 describes approximately 300 messages, about 20 work requests and five runs per configuration. Coding is replaced by a time-consuming tool. Arrivals and simulated task durations are scaled to one quarter while model-call time remains real; §7.2 uses a real Router model and mock Workers. These are author-reported scheduling experiments, not locally replicated coding, cost or safety measurements.

| Reported comparison | Bounded interpretation |
| --- | --- |
| Neutral single-Session p95 29.5 minutes versus Super-agent 15.7 minutes | The neutral baseline never delegated in the five reported runs; the delegation-favoring baseline delegated in four. This compares the stated scheduling policies and workload, not every single-Session/Subagent design or real coding quality. |
| Removing bypass raises cache-read tokens from 23.23M to 31.77M | `(31.77 - 23.23) / 23.23` is about 36.8%, consistent with the reported 37% increase. Adding bypass relative to the no-bypass baseline reduces that metric by about 26.9%, not 37% of total monetary cost. |
| Trigger rate about 1 to 40/minute; batch 1.0 to 2.8; request time 2.5 to 3.9 seconds; amortized decision time 6.4 to 1.6 seconds | Request and decision aggregates cannot be reconciled by simple division without step counts and raw aggregation definitions. Missing traces prevent verification; they do not establish false numbers. |

**[INFERENCE]** Keeping model latency unscaled changes its weight relative to task duration and arrivals. Generalization needs a matched workload, defined aggregation/variance and accepted-output accounting. The strongest contrary interpretation is that the essay already labels these experiments preliminary: their narrow scheduling hypothesis can be useful without establishing deployment readiness or general superiority.

#### Source-only Mechanisms and Comment Adjudication

| Mechanism or criticism | Checked evidence and bounded judgment |
| --- | --- |
| “There is no coordinating center” | Checked 2026-11-02: the executed Engine transitions and [main-session prompt](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/6337fc823ce20251c8de8085948165c81aaa701e/prompts/orchestrator.md) support assessment/routing with implementation assigned to Workers. Lack of direct execution tools is not absence of coordination; notification fan-out does not solve shared-resource conflicts or prove cross-task technical synthesis. |
| Chain-of-Recall; “versioned files solve memory” | Checked 2026-11-02: [cards](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/6337fc823ce20251c8de8085948165c81aaa701e/src/app/cards.ts) expose previews/read pointers; [resources](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/6337fc823ce20251c8de8085948165c81aaa701e/src/app/resources.ts) paginate and check main-only, same-ticket and trigger visibility. **[INFERENCE]** Durable bytes and exact matches do not establish freshness, retrieval relevance, summary completeness or semantic reconciliation. These API guards are not audited multi-tenant/OS isolation. |
| Background tasks and cancellation | Checked 2026-11-02: [bash](https://github.com/deepseek-ai/deepseek-harness/blob/ce7073d51254c26cd63b22a60835b8f948deb447/packages/shell/tool-bash/src/index.ts) supports background work and timeout promotion subject to registry/configuration/admission. [Job tools](https://github.com/deepseek-ai/deepseek-harness/blob/ce7073d51254c26cd63b22a60835b8f948deb447/packages/jobs/tool-jobs/src/index.ts) wake an idle owner or inject a notice, and `job_kill` returns `cancellation-requested` or `already-finished`. Notice delivery, model processing, cancellation request, resource termination and already-escaped effects are different observations; none was live-host-tested here. The essay's illustrative tool names are not established API defects. |
| Independent Watchdog and cloud daemon | Checked 2026-11-02: the inspected [Passes](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/6337fc823ce20251c8de8085948165c81aaa701e/src/app/passes.ts) path periodically drives effects/evaluations and health status. It does not verify the essay's separate model Watchdog or cloud daemon. The README's explicit internal/public distinction prevents treating unverified internal features as disproven. |
| Workspace separation as security | Checked 2026-11-02: [environment guardrails](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/6337fc823ce20251c8de8085948165c81aaa701e/src/infra/environment.ts#L1-L5) explicitly are not an OS security boundary; Workers run under the operator's OS user. The survey's own execution sandbox does not certify upstream deployment isolation. |

**[INFERENCE]** The useful Watchdog challenge is to separate detection, intervention and changes to policy/acceptance criteria, with a named enforcement owner; another model Session is not automatically an independent verifier. Missing or stale monitoring data is unknown, not clean. Discarding speculative computation does not retract a published PR or disclosed information, and indefinite retention of discarded work is not automatically desirable either.

The essay itself leaves intermediate human intervention and broader context/A2A/security boundaries open. Source-visible ticket/transcript resources refute categorical unobservability, not demonstrate good UX; no interface was exercised. A short-reply target is a channel heuristic, not a measured universal optimum. Commenter outage histories, originality/copying allegations and AGI predictions remain unverified; the survey coordinator declines to adjudicate them from anecdotes.

#### Documentation Disposition

**MSS-DOC2: adopt this supplement and existing discovery only.** Its local benefit is preserving the concrete scenario, denominators and evidence boundaries without requiring the original temporary files. [Research](../skills/reflective-research/SKILL.md) and [Review](../skills/reflective-review/SKILL.md) already separate source, execution and extrapolation; [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md) already assigns authority, concurrency and external effects to the host; [Flow Loop Harness](../skills/flow-loop-harness/SKILL.md) already requires caps, a verifier and protected acceptance artifacts. [Context Engineering](../03-context/context-engineering.md) and [Artifact Promotion](../04-agent/artifact-promotion.md) cover canonical context and memory provenance.

That is delivered textual coverage, not proof of reader compliance or runtime capability. No new local structural gap warrants a Skill, example or runtime change. Reopen on a concrete consumer failure, newly available original/raw experiment evidence, or a different candidate source revision before adoption. The broader MSS-1–MSS-8 proposals retain their own dispositions; this owner request concerns the immediately preceding Super-agent survey.

## Four Architecture Forecasts

The supplied forecast is treated as four claims to qualify, not a forced choice between accepting every prediction and dismissing the mechanisms. Source existence, source-reported measurement, evaluation conditions and future extrapolation are separate evidence dimensions.

| Claim | Primary evidence read, checked 2026-11-01 | What survives | What remains unproven / would change the decision |
| --- | --- | --- | --- |
| Very large context becomes widespread by 2027 | Checked 2026-11-01: [Gemini 1.5 paper](https://arxiv.org/abs/2403.05530), [Llama 4 Scout model card](https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama4/MODEL_CARD.md), [Magic 100M research report](https://magic.dev/blog/100m-token-context-windows) | Research/declared contexts at 10M and a reported 100M prototype exist. Long-context capability is not imaginary. | Widespread cheap, reliable deployment is a forecast, neither established nor already falsified by these examples. Need a dated target deployment, workload, hardware/cost and quality contract; no exhaustive current-product census was performed. |
| TTT/Titans gives everyone durable personal memory | Checked 2026-11-01: [TTT, 2407.04620](https://arxiv.org/abs/2407.04620), [Titans, 2501.00663](https://arxiv.org/abs/2501.00663) | TTT learns a hidden-state model during sequence processing; Titans combines test-time neural memory and attention. | User identity, cross-session persistence, tenant separation, exact forgetting/deletion and permission checks are additional product contracts. No model run here; no blanket claim of impossible batching, guaranteed immunity to forgetting, inevitable base-model collapse or fixed per-user memory size. |
| Diffusion coding LLMs make work 5–10 times faster | Checked 2026-11-01: [Mercury report, 2506.17298v1](https://arxiv.org/html/2506.17298v1) | The report gives high API output throughput under a dated comparison and describes parallel token generation. | Its approximately 1K-input/1K-output API workload is not total engineering-task latency at matched accepted quality. Provider hardware/batch parity was not established; no benchmark replication. Diffusion is not autoregressive speculative decoding, and universal inability to stream is not supported. |
| Long context eliminates RAG for small/medium enterprises | Checked 2026-11-01: [LC/RAG comparison, 2407.16833](https://arxiv.org/abs/2407.16833), [OP-RAG, 2409.01666](https://arxiv.org/abs/2409.01666) | Long context can outperform a baseline retrieval pipeline with sufficient resources; retrieval/hybrid strategies can reduce cost or distractors in tested tasks. RAG is not synonymous with a vector database. | No universal enterprise replacement verdict follows. Application-specific source freshness, access control, removal/invalidation and evidence attribution remain necessary whichever architecture is selected. Retrieval alone does not guarantee them. |

Mercury's text/Table 4 first-token latency values disagree (`25 ms` versus `0.25 s`); that value is deliberately excluded from the conclusion. Table 1 throughput is source-reported, not a locally measured speedup. No inference here depends on resolving that discrepancy.

The retained numerical correction is Table 1's reported Mini/Small throughput **1109/737 tokens per second**, HumanEval **88.0/90.0** and MBPP **77.1/76.6**, in the report's February 2025 endpoint comparison. Earlier advisory values and a blanket "uniform H100, batch=1" description were not supported by that table and were rejected. These numbers remain attributed report values, not local measurements or a quality-parity claim.

**Socratic questions:** Which metric became a product claim without an intermediate test? Output throughput became completed-work speed; sequence memory became personal-memory service; nominal context became useful reliable recall. Would the opposite architecture automatically fix the problem? No: a retrieval system can also serve stale or unauthorized content. What can be decided now? Which measurement and authority boundary a future comparison must name, not which architecture will universally win in 2027.

## Grok Bot Workflow and Authority Boundaries

The [original post](https://x.com/poteto/status/2116576229319233596) and [routine reply](https://x.com/poteto/status/2116580481236115933), checked 2026-11-01, were partly recovered through public syndication: identity, date and short text were visible; the full long post and all quoted replies were not independently recovered. Those portions remain supplied excerpts, not verified verbatim quotations. Official product documentation supplies the independently read workflow and security claims below.

As checked 2026-11-01, the official [skills/routines guide](https://docs.x.ai/grok-bot/skills-routines-and-automations) recommends a successful one-time task, then a reusable skill, then a tested routine. It names ownership, inputs/access, validation, approval boundaries, source/schedule context and handling of missing or stale data. The [Bots guide](https://docs.x.ai/grok-bot/bots) recommends the smallest useful roster and clear jobs rather than maximizing agent count.

The [Vault](https://docs.x.ai/grok-bot/vault) and [approval/security](https://docs.x.ai/grok-bot/approvals-security-and-privacy) documents, checked 2026-11-01, state that account Bots share the cloud computer, files, browser sessions and credentials; Vault entries are not restrictable to a single Bot. Auto Review uses model judgment. Saved payment cards do not require a separate approval for each use, and deleting a Bot does not remove shared files/browser sessions. These are **documented product boundaries**, not results of a hosted-product security audit.

**[INFERENCE]** Distinct role names or hidden secret values do not establish distinct capabilities. An automation design should identify its actual account/credential/action boundary; an autonomous email account or ability to sign up elsewhere is not a grant of permission. Use source-system scoped accounts and explicit external-action approval where the product supports them; prompt wording cannot manufacture unsupported per-Bot isolation.

**Socratic questions:** Is “each Bot has one job” isolation or task organization? The latter unless the host enforces separate authority. Does a reusable skill authorize scheduled execution? No; the schedule, sources, effects and approval boundary are a separate decision. Does deleting the Bot reverse work? The docs expressly distinguish Bot identity from retained shared state; effect rollback was not exercised.

The useful workflow idea is to preserve a proven sequence with boundaries before automating it. [Workflow Acquisition](../04-agent/workflow-acquisition.md) already distinguishes trace evidence, human-owned decisions, side effects, replay and promotion. Product-specific recommendations in this section do not become a new TeaPrompt bot-management workflow.

## Writing, Learning, Detection and Preference

Four claims that sound mutually supportive actually measure different things.

| Claim | Evidence actually read | Bounded interpretation |
| --- | --- | --- |
| Writing supports learning | Checked 2026-11-01: [Graham, Kiuhara and MacKay meta-analysis, indexed original abstract](https://eric.ed.gov/?id=EJ1249514): 56 true/quasi-experiments in Grades 1–12 science, social studies and mathematics; mean effect size 0.30 | Supports writing-to-learn effects in those studied educational settings. Full text was inaccessible; it does not establish adult intelligence gains, prevention of brain decline or a universal daily-writing dose. |
| Readers can recognize AI writing | Checked 2026-11-01: [Russell, Karpinska and Iyyer, ACL 2025 abstract](https://aclanthology.org/2025.acl-long.267/): selected frequent LLM-writing annotators, 300 non-fiction English articles from humans and GPT-4o/Claude/o1; majority vote of five frequent users misclassified one article | Strong performance in that particular task/cohort; not universal one-sentence detection by any reader, language or model generation. |
| People prefer human work | Checked 2026-11-01: [Zhu et al., ACL Findings 2025](https://aclanthology.org/2025.findings-acl.1329/): rephrasing, summarization and persuasive-writing experiments, including swapped labels | A human-authorship label affected preference. Detection, preference, prose quality and learning are different outcomes; it does not prove everyone prefers objectively worse human writing. |
| Reading and writing occupy completely different vector spaces | Supplied commentary/metaphor; no validating cognitive-model evidence in the inspected sources | Useful metaphor at most, not a demonstrated cognitive architecture or explanation established by those studies. |

**[INFERENCE / untested practice idea]** If the goal is judgment or retention, a learner could first write an explanation from memory, use AI for counterexamples/corrections, then later attempt an unaided transfer task. That is a testable practice design, not a protocol validated by the cited studies. It is not a requirement to avoid AI, endure struggle or meet a writing streak.

**Socratic questions:** Is the target better prose, more persuasive authorship, calibrated detection or retained knowledge? These require different checks. Does selected-annotator accuracy transfer to the general population? Unknown without a matched study. Would elegant AI-assisted output prove the writer learned? No; [Learning Coach](../05-domain/learning-coach.md) already calls for delayed retention/application rather than fluency, confidence or effort alone.

## Evidence vs Inference

- **Observed execution:** upstream module transitions, isolated CLI output, helper behavior and the controlled settings lost update. These establish the stated input/output boundaries only.
- **Verified source text:** pinned implementation/documentation and the explicitly named primary papers/abstracts. Verification of wording is not verification of the authors' raw data or deployed service.
- **Secondary / partial:** the unavailable DeepSeek article's reported simulation, truncated social-post recovery, supplied replies and forecast transcription. They keep their original provenance even when a related repository or paper exists.
- **[INFERENCE]:** compare accepted outcomes and total cost rather than isolated throughput; keep mechanism, authority, delivery and learning constructs separate; prefer a bounded example over a duplicate general rule.
- **Unknown:** net savings, hosted isolation/cancellation efficacy, prompt-example usefulness, real-world task quality, human-learning transfer and local recurrence of a missing delivered instruction. Unknown demand is not zero demand.

### Reproducibility and Ephemeral Evidence

The source-survey ledger `local://multi-source-survey-2026-11-01.json` was sealed for the panel at SHA-256 `a6d0776e4447792b762644fabdf5d75e05266969924922ed60215d0319c84c93`. The shared packet `local://survey-publication-panel-packet-2026-11-01.md` records the common question, source identities, prior conclusion, current delivered surfaces and adversarial frame. These are historical receipts, not public-source links or runtime dependencies; all load-bearing conclusions and primary links are internalized above.

The isolated source root was `/tmp/teaprompt-token-vibe-qJcQga`; scratch root was `/tmp/teaprompt-survey-smoke-nLyvlD`. The actual invocation shapes were `sandbox-exec -f offline.sb /opt/homebrew/bin/python3 -B mechanisms.py` (exit 1, fixture error), the same prefix with `remaining.py` (exit 0, tool-manager boundary reported), and `sandbox-exec -f offline.sb /Users/teee/.bun/bin/bun run prototype.ts` (exit 0). Arguments here are shortened to basenames relative to the scratch root; the original receipt retains absolute argv. The sandbox denied network and allowed writes only beneath scratch plus `/dev/null`.

Temporary-file disposition: `paste-6.md` is internalized as explicitly secondary claims; `mechanisms.py`, `remaining.py`, `prototype.ts` and `offline.sb` are internalized as the procedures/results/limits above and are not shipped dependencies; source clones are replaced by immutable public links. No script, synthetic state, credential or fixture is added to the repository. Before publication, the coordinator re-read three load-bearing sentinels in the pinned source: the live notice-not-cancel branch, the settings read-modify-write path, and the prototype's release disclaimer. All three matched the recorded boundaries.

## Panel Consensus

Five read-only reviewer jobs were dispatched together from the same sealed packet: EfficiencyEvidence, AutonomyAuthority, ForecastMethods, HumanLearning and FrameMinimality. All five complete reviews were recovered, including findings, answered Socratic questions, strongest objections and terminal verdicts. The source-gathering scouts from the preceding survey are not additional votes in this panel.

| Role | Terminal verdict | Reason that bears on the decision |
| --- | --- | --- |
| EfficiencyEvidence | AGREE WITH CHANGES | Preserve the five-stage projection, sidecall billing, notice-not-cancellation, fixture limits and concurrent-write precondition. A credential-reuse example is potentially useful, not a missing general rule. |
| AutonomyAuthority | AGREE | The plan already requires the DSH authority/resume distinctions and Grok docs-only limits. A shared-state example may help later, but no new authority clause was established. |
| ForecastMethods | AGREE WITH CHANGES | Preserve source/measurement/extrapolation boundaries. Proposes context-range wording clarification and an attributed-benchmark example, not a new research Skill. |
| HumanLearning | AGREE WITH CHANGES | Separate population, construct and source-access tiers. Suggests an optional analogy clarification; keep the proposed learning practice in this record rather than presenting it as an endorsed protocol. |
| FrameMinimality | AGREE WITH CHANGES | Record plus existing discovery is sufficient. Opposes unnecessary companion-example edits and rule duplication; requires the frame test, explicit MCP exclusion and no authority expansion. |

The verdict split is **one AGREE / four AGREE WITH CHANGES**, not four votes for operating-rule changes. All supported bounded publication; reasons diverged over teaching value, context wording and whether examples belong outside this record. These are parallel advisory perspectives from one host/model-family channel, not independent empirical replications. No provider-diversity claim is made.

### Frame Test and Disagreements / Residual Risks

**Frame tested:** does the prior "no new Skill" conclusion hide a missing instruction or a useful reader-facing clarification? The delivered Research/Review/Risk, acquisition, promotion, trust-boundary and Learning Coach surfaces already decide the general evidence/authority questions. That is textual coverage, not proof an installed agent will comply. Conversely, absence of a runtime defect does not make a teaching example worthless.

The main disagreement is marginal teaching value. Efficiency and Forecast favor optional examples; FrameMinimality favors keeping them inside this record because existing clauses already decide the questions. HumanLearning identifies a possible one-sentence analogy clarification but accepts no change as equally defensible. No reader study or comparative prompt evaluation settled that disagreement. The coordinator keeps exact proposals below without treating the panel as an adoption grant.

**Context wording adjudication:** ForecastMethods called the two labels in [Large Context](../03-context/large-context.md) a contradiction: introduction/Purpose say `200K–1M`, while the composition note says `200K+`. Both wordings are observed. The coordinator classifies this more narrowly as a **scope ambiguity**, not a confirmed incompatible instruction or hard 1M limit: the ranges overlap, and the prompt does not explicitly prohibit larger inputs. A clarification is worth proposing; blindly replacing the range with `200K+` would not prove reliability at larger sizes. Neither intended cap nor reader failure is established.

**Authority corrections to reviewer suggestions:** a forecast draft still called MCP blocked; the current user explicitly excluded it, so that wording was rejected. A frame-review draft described local recurrence as zero; the survey has no such usage census, so recurrence remains unknown. Proposed examples and analogy clauses are not adopted because a reviewer labels them helpful. The original survey's no-repository-edit boundary applied to that earlier research turn; the later user instruction authorizes this record/navigation publication, not unrelated contract edits.

### Required Wording Changes

The necessary publication corrections are incorporated in this record: three upstream mechanisms versus five analytical stages; local-engine versus provider/billing path; detector versus live controller; settings application versus transcript/cache behavior; controlled concurrency versus failure rate; DSH policy notice, pre-resume revalidation and actual stop as separate events; secondary simulation versus public-prototype performance; forecast versus deployment; and writing outcome versus detection/preference/metaphor. A rule already covering these distinctions is not copied into another Skill.

### Shared Findings and Existing Coverage

| Decision class | Current delivered surface | Why no additional general clause is required by this survey |
| --- | --- | --- |
| Provenance, version identity and source-only versus executed claims | [Research](../skills/reflective-research/SKILL.md), External Adoption Checks and State Ledger; [Review](../skills/reflective-review/SKILL.md), Four Evidence Dimensions / Evidence Tiers | The checked byte identity, attributed measurement and extrapolation are already separate obligations. |
| Shared settings and concurrent writers | Research External Adoption Checks; [External Adoption Review](../04-agent/external-adoption-review.md), template §4 | Existing checks already name parent-path containment, ownership receipts and concurrent-write behavior. The observed defect is upstream, not a newly missing TeaPrompt probe requirement. |
| Observation, permission, cancellation and external effects | [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md), template §§2a–4; [Risk](../skills/reflective-risk/SKILL.md), Sink Inventory / Rules | Host-owned authority, concurrency and effect boundaries already exist; role names and notices are not enforcement proof. |
| Learned facts, personal memory and skill promotion | [Workflow Acquisition](../04-agent/workflow-acquisition.md), trace/replay and L4 boundary; [Artifact Promotion](../04-agent/artifact-promotion.md), template §§2–5; [Handoff/Retro](../skills/reflective-handoff-retro/SKILL.md), Memory Consolidation | Observations and model drafts do not silently become instructions; persistence/identity/ACL guarantees need a host. |
| Human learning and scientific transfer | Research Source Priority; Review Four Evidence Dimensions; [Learning Coach](../05-domain/learning-coach.md), Acceptance Criteria / Optional Human Support Menu | Population/task/outcome limits and delayed retention/application are explicit. An attractive practice recipe is not a tested intervention. |

## Candidate Adoption Ledger

`MSS-DOC1` and the separately authorized `MSS-DOC2` supplement are adopted here as reference documentation and discovery only. `Proposed` and `deferred` rows are complete recommendations with reopening conditions, not unfinished authorized implementation. No operating text, companion example, prompt or Skill change is landed by these rows; the Super-agent follow-through does not reopen unrelated held proposals.

| ID | Candidate / existing destination | Status and decision | Evidence / dissent | Next action, falsifier and smallest useful check |
| --- | --- | --- | --- | --- |
| MSS-DOC1 | This record, [existing catalogue](external-adoption-case-studies-2026-06-20.md), generated index and delivery report | **Adopted — reference documentation only** | Explicit user request; unique source pins, execution limits and adjudicated disagreements cannot fit in a catalogue row. Consolidates EFF-1–6, AUT-1–4/7, FOR-1–3, HUM-4, FRM-1–5. | Exercise actual composition/slug discovery, relative navigation and existing repository checks. Wrong if a conclusion needs private session files or silently becomes an operating instruction. |
| MSS-DOC2 | [Super-agent full-text follow-through](#full-text-follow-through-2026-11-02), existing catalogue/index and delivery report | **Adopted 2026-11-02 — reference documentation only** | Later owner request; unchanged prototype pin, supplied-full-text limits, executed multi-owner handback, benchmark arithmetic and source-only async boundaries. Not a new panel verdict or internal-system replication. | Exercise final composer output, local file/fragment navigation and existing repository checks; preserve Skill bytes. Reopen on a named local consumer gap or new source/experiment evidence, not anecdotal agreement. |
| MSS-1 | [Large Context](../03-context/large-context.md), introduction, Purpose and composition note | **Proposed — bounded documentation clarification; not applied** | FOR-4 observed `200K–1M` versus `200K+`; coordinator rejects calling this a proven hard cap or runtime defect. | Suggested direction: “Use this for large-context tasks while avoiding context rot,” with matching Purpose/composition wording; do not imply a validated maximum. If a deliberate bounded scope is documented, retain that scope and clarify the composition note instead. Check a reader's applicability decision without inferring comprehension from window size. |
| MSS-2 | [Research examples](../skills/examples/reflective-research.examples.md), a credential-reuse worked example | **Deferred — optional example, strongest teaching candidate** | EFF-7 / FRM-5/7: this survey required correction of “local/no extra key” → “no cost/egress”; current mechanism-versus-product and sink rules already cover it. Teaching benefit and recurrence are unknown. | Proposed text: “A local plugin can call the host's authenticated model CLI. Check the provider path, billing/quota and transmitted context before concluding no egress or cost.” Owner-authorized example work or a named reader ambiguity can reopen it; compare against the existing rule, not exact-word presence. |
| MSS-3 | Research examples, Example 3 State Ledger | **Deferred — optional attributed-measurement example** | FOR-5 proposes a `needs-qualification` row. FRM-6 rejects another generic secondary-source example because Example 3 already covers that distinction. | Distinct draft: “Vendor reports X tokens/s under a dated input/output workload; report text checked, performance not reproduced; end-to-end task benefit unknown.” Reopen only if it teaches attribution/extrapolation beyond the existing summary row; remove if redundant. Do not label a copied real number an invented example without saying which it is. |
| MSS-4 | [Risk examples](../skills/examples/reflective-risk.examples.md), shared-role credential scenario | **Deferred — optional teaching example** | AUT-5: multiple named Bots share account state; sink inventory already supplies the decision. A real case can be clearer without proving present instructions broken. | Draft: “Two named Bots share a browser session and credential vault; separate names do not isolate access. Identify the enforcing account/credential/action boundary; model review is not a deterministic gate.” Future example work needs scoped authorization; check the same decision with current clauses before adding prose. |
| MSS-5 | Research Source Priority analogy sentence; Research/adoption credential-reuse clause | **Proposed, not recommended over an example now** | HUM-1 and FRM-7 each compress existing rules into another clause. No missing decision obligation established; strongest objection is duplication. | Analogy draft: “An analogy can suggest a hypothesis but is not evidence of a measured mechanism.” Credential draft: “Reusing an authenticated host session does not remove egress or billing review.” Reopen for a named misclassification that existing delivered text cannot adequately resolve; any operating change requires explicit authority. |
| MSS-6 | Learning practice idea in this record; Learning Coach / writing-learning Skill | **Record only; no Learning Coach edit or new Skill** | HUM-2/3/5: practice, drafting and critique have existing destinations. No cited study validates the proposed AI-feedback sequence. | The optional idea remains labeled untested beside its description. A future study must measure the target learners' delayed unaided transfer, not polished output or confidence. No study/campaign authorized here. |
| MSS-7 | Research, Review, Risk, Handoff, loop and authority operating contracts | **No change — generic coverage established textually** | EFF-8, AUT-6, FOR-6/7 and the coverage map above. A host hook's inability to cancel does not imply a defect in TeaPrompt's generated-loop contract. | Reopen on a concrete missing/contradictory delivered instruction or consumer-visible failure. Host-specific enforcement remains a host audit, not a prose guarantee. |
| MSS-8 | New skill/runtime/taxonomy, curated-knowledge backfill, duplicated README pointers or wording-pin tests | **Rejected for this request** | EFF-9, FOR-8/9, HUM-3 and FRM-8–12: no distinct skill trigger, authorized runtime direction or new indexing policy; discovery already flows through the catalogue. | Reconsider only the named gap under its own authority/promotion contract. Existing held candidates retain their own triggers. Use current generic validators and real document-consumer smoke; no test that merely pins these paragraphs. |

**Priority if a later docs-edit request is made:** resolve MSS-1's scope wording first; consider the concrete MSS-2 example next; MSS-3/4 only if they improve a named reader decision. MSS-5 is lower value than a worked example and is not a recommendation to enlarge a Skill. This prioritization is an engineering judgment, not a measured teaching-effect ranking.

## Falsifiability and Untested Ideas

| Inference / hypothesis | Observation that would change it | Smallest relevant future check |
| --- | --- | --- |
| Existing generic Skills suffice for these survey decisions | A standalone consumer reaches the wrong permission/evidence decision because a relevant distinction is missing or contradictory on its delivered surface | A named before/after consumer scenario; not a source-string assertion or panel vote |
| The context-range clarification improves applicability decisions | The current scope is already deliberately bounded and unambiguous to the target reader, or the rewrite implies unsupported larger-window reliability | Compare the current three labels and proposed wording on a concrete >1M task, preserving the no-reliable-understanding warning |
| The credential-reuse example has incremental teaching value | The existing clauses already prevent the exact no-key/no-cost error, or the example still leaves provider/account scope unclear | A bounded reading scenario with the current material and the proposed example; no vendor calls needed |
| A nominal token/throughput advantage improves completed-task efficiency | Accepted quality, retries, mechanism overhead, cache economics or source preparation erase the advantage | A separately authorized matched workload and accounting design; the current module smoke is not this test |
| TTT/Titans or long context can replace part of a retrieval workload | Required freshness, exact removal, permission or recall quality cannot be met under the actual application contract | Task-bounded recall plus explicit product identity/ACL/persistence checks, not architecture-name comparison |
| The proposed writing/AI-critique sequence helps learning | Delayed unaided transfer fails to improve despite nicer assisted output | A learner-owned comparison on a new task with credible feedback; no claimed efficacy until measured |

## Evidence Actually Checked and Handoff

The coordinator's earlier executions and source reads are distinguished above from this publication panel's read-only judgments. Primary-source claims were checked at the stated access tier; the panel did not rerun upstream smoke or turn documentation into enforcement evidence. Complete reviewer findings were integrated by one owner, with the three disputed scope/authority corrections recorded explicitly.

Publication acceptance is: preserve every non-MCP topic; retain source versus execution versus inference limits; preserve disagreements and explicit candidate dispositions; keep the record usable without ephemeral artifacts; exercise the real document-discovery path and applicable repository checks. The executed publication results belong in [the delivery report](../../review/final-report.md), not as claimed vendor/model/human efficacy.

No Human Review is needed merely to finish this bounded record. Any later operating-clause change, deployment, shared-setting mutation, credential use or experiment keeps its own approval boundary. MCP remains excluded by the user; its previously unknown target is not silently identified, substituted or judged.
