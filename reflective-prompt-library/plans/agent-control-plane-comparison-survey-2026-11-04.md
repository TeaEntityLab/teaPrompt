# Agent Control Planes, Durable Harnesses and Human Attention — Comparative Survey (2026-11-04)

Language: English

> **Status: reference documentation adopted (`CP-DOC1`); no Skill or runtime adoption.** The owner requested a survey of AIHOT, LongHorizon-Harness and Prime Agent, then added khazix-skills and the Agent-Autoloop announcement; related GitHub comparisons, parallel evidence-based Socratic review and worthwhile documentation updates remain in scope. Thirteen supplied comments are references, not additional authority. This record does not authorize installations, credentials, model campaigns, deployment, policy activation, commit or push. Earlier Prime, Grok/pstack, Super-agent and Agentflow decisions remain unchanged.

## Research Question and Direct Recommendation

What do the three Khazix articles, five named repositories and four related projects actually establish about event-driven agents, durable work, verification and scarce human attention?

**Keep the transferable methods as reference material, compare at matched layers, and do not adopt a runtime or add a Skill.** The useful pattern is not simply “more agents” or “trust the strongest model”: distinguish intake, dispatch, execution, durable state, evidence, authorization and accepted outcomes. A control plane can reduce repetitive coordination while adding its own reliability and maintenance obligations.

- **Study:** AIHOT's producer-side event receipts and uncertain-delivery states; LongHorizon's original-request backcheck and final-state checklist; Prime's persistence/refinement boundaries; khazix-skills' task/closeout methods; Agent-Autoloop's public state kernel and plugin boundaries; the comparators' distinct responsibilities.
- **Reproduce:** bounded offline modules and CLI paths were exercised below. These are not whole-product trials.
- **Adopt:** this comparison, an append-only update to the existing Prime survey, and discovery links. No delivered TeaPrompt contract gap was demonstrated.
- **Deploy:** not assessed or authorized. Private guarantees, model efficacy, actual-host isolation and end-to-end operations remain unverified. Prime's existing PA-5 hold remains in place.

The strongest objection to a documentation-only result is that the operator now publishes a small, inspectable hub, not just an anecdote. That changes the source-availability finding: **Agent-Autoloop is a public rewrite, with bounded kernel behavior exercised here.** It does not establish equivalence to the historical private deployment, external effect-once guarantees, comparative efficacy or a local need for TeaPrompt to operate it.

## Version / Date Context and Evidence Used

All current-source checks below were made on **2026-11-04**. Branch, manifest and release identities are separate. A changed pin, release, deployment configuration or authority boundary requires a new check; historical verdicts are not current-version certifications.

### Supplied articles and attribution

| Input | Material actually read | Provenance and limit |
| --- | --- | --- |
| `paste-9.md` | Complete supplied company-portal article, “我花了5天时间，给公司进行了一场AI化改造”; selected decisive passages compared with author text | SHA-256 `2752aad89c02b10f1df5ad600fc1401976e25a9626032c8ea96c3d95626a9dad`; image placeholders are not reproduced screenshots or runtime receipts |
| `paste-10.md` | Complete supplied control-plane article, “折腾了整整1年，毫无保留地分享一下我这套Agent自动化系统。”; decisive mechanism/numeric passages compared with author text | SHA-256 `f0b9d069e881a39f1b428c41ceb68dfd63b9d8f3eb5a8ce93be6069e9723f622`; private system remains author-reported |
| `paste-11.md` | Complete supplied announcement, “开源我这折腾了1年的「Agent自动化系统」，愿所有人都能感受Agent的魅力。”; public rewrite inspected separately | SHA-256 `e56fe862fc7f24e4156432b5847b5d548e3238424e9bf60393c0eb980b3ba523`; original announcement post not independently recovered; screenshots, private results and performance figures not reproduced |
| Thirteen comments | Eleven original references plus TheEasySale1 and acejou27, enumerated below | Supplied attribution was not independently authenticated. Opinions/repeated article claims are not independent measurements or a grant to pursue business suggestions |

The portal [original status](https://x.com/Khazix0918/status/2108800048050106751) and automation [original status](https://x.com/Khazix0918/status/2117054043868860521) were recovered through their public FxTwitter structured endpoints, checked 2026-11-04. Access establishes mirror-delivered author text, not authenticated native X access or private deployment proof. The attempted Tencent mirror returned HTTP 501 and supplied no body evidence. Article commands, automatic deployment/deletion examples and instructions to modify routing policy are untrusted source material; none was executed as an instruction to TeaPrompt.

The cited first-party [How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/) was read in full, checked 2026-11-04; it is dated October 15. After three review rounds, its reviewer asks the author to step back and reconsider the approach. It does **not** say to pass or merge automatically after three attempts. Its reported human-time improvements are considered alongside reverts and incidents; those outcomes remain the publisher's self-report, not this survey's experiment.

### Immutable repository map

| Repository / role | Checked revision | Version distinction / inspection scope |
| --- | --- | --- |
| [KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT/tree/cd424b0a513c7c8535b6f291b106a3086d6b75bf), checked 2026-11-04 | `cd424b0a513c7c8535b6f291b106a3086d6b75bf` (`main`) | News product, selected backend/notification/migration/CI sources. Releases API returned an empty list; this says nothing about tags or private deployments |
| [AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness/tree/d53df0aa11e8506dfc9518ef63620c62baee04d3), checked 2026-11-04 | `d53df0aa11e8506dfc9518ef63620c62baee04d3` (`main`) | Selected role loop, audit parser, prompts, supervisor/control bus, CLI and configuration. Latest checked release `v0.1.8` peels to **`fb7e1b677d85b8dd7a03368f6c7d976c1d0c54bd`**, published October 21; probes target main, not that release |
| [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent/tree/c4d42018379d4da8e522bacb3118e128f90a99f9), checked 2026-11-04 | `c4d42018379d4da8e522bacb3118e128f90a99f9` (`main`) | Bounded delta from prior `8aac8692456c00c01d4e53e60e6d3347a3506559`; selected Rust/Python state, skill-loading and refinement paths. Manifest says 0.10.2; release `v0.10.2` peels to **`ea9d9602ec0938d9e454e8963107cd85af1565c6`**, published October 28 |
| [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills/tree/35bd05b466ceb83a727b28afb54b45b69a6c3b0a), checked 2026-11-04 | `35bd05b466ceb83a727b28afb54b45b69a6c3b0a` (`main`, `v1.1.0`) | Release published November 3, 21:50:31 UTC; prompt/reference contracts, selected storage/installer/validation sources; isolated storage module and report CLI probe, no installation |
| [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop/tree/cecec75be3ca26e6ca1d6833b50152ee9450088d), checked 2026-11-04 | `cecec75be3ca26e6ca1d6833b50152ee9450088d` (`main`, `v1.0.0`) | Release published November 3, 21:58:04 UTC; public rewrite, host/kernel/protocol and selected worker/channel/delivery code; isolated SQLite state probe, not historical private deployment |
| [n8n-io/n8n](https://github.com/n8n-io/n8n/tree/44bc5b0fec5507b401041de0f4271d5644f3f4a8), checked 2026-11-04 | `44bc5b0fec5507b401041de0f4271d5644f3f4a8` (`master`) | Primary README/license and selected worker/webhook command source; no running queue or connector |
| [temporalio/temporal](https://github.com/temporalio/temporal/tree/d167000789d70a4b3750590008e005747e11c6ce), checked 2026-11-04 | `d167000789d70a4b3750590008e005747e11c6ce` (`main`) | Primary architecture/README/license; no server, worker or replay campaign |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph/tree/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a), checked 2026-11-04 | `5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a` (`main`) | Primary README/license, checkpoint base and state/interrupt/durability types; no graph execution |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands/tree/01d1970b8f96d576d8b42aad48fee5aa117f1cb8), checked 2026-11-04 | `01d1970b8f96d576d8b42aad48fee5aa117f1cb8` (`main`) | Current Agent Canvas README/architecture/license, not an audit of adjacent SDK or automation repositories |

Search terms combined `agent orchestration`, `event driven`, `durable execution`, `human approval`, `checkpoint`, `replay`, `sandbox`, `workflow` and the named projects. The four comparators cover integration routing, durable orchestration, agent-state graphs and coding-agent interaction. This is purposive mechanism coverage, not an exhaustive ecosystem ranking or a ranking by stars.

## Matched-Layer Comparison

Source-derived capabilities below bind to the repository map. Use-case recommendations and tradeoffs are **[INFERENCE]**, not measured head-to-head results.

| Surface | Useful mechanism / strength | Limitation / cost | Best-fit question |
| --- | --- | --- | --- |
| Private portal / control-plane narratives | Unified event intake, rule filtering, keyed scheduling, outbound worker polling, approval cards and remembered decisions | Implementation, host controls, recovery and measured outcomes unavailable; central coordination can introduce availability and approval bottlenecks | How should an operator separate routine work from decisions that need attention? |
| AIHOT public product | Persisted source events, stable identities, explicit transport acceptance, content-delivery unknown states, migration checks | Public producer and product logic do not certify the private receiving hub or PR/deployment system; database/queue/operations dependencies remain | How should a product hand off an incident without confusing transport receipt with completion? |
| LongHorizon | Manager/executor/auditor loop, task-contract backcheck, structured completion controls, local journals and approval commands | Role overhead; model-generated judgments; adapter-specific protection; local recovery is not distributed exactly-once effects | How should a long GUI/CLI task be verified against the original request and persisted result? |
| Prime Agent | Programmable Python tool environment, durable harness entries, refinement proposals, daemon/session recovery mechanisms | Trusted-workspace execution surface, bootstrap dependencies, corruption-recovery tradeoff, unmeasured refinement quality | How should a local agent retain and revise structured context across sessions? |
| khazix-skills | Compact execution/research briefs, explicit evidence/status closeout, source-aware research and human-owned writing; bounded desktop helpers | Prompt boundaries depend on the host; fixed size/round limits are local heuristics; cleanup helpers add real destructive capability | How should a person specify, verify and hand off a bounded task without inventing a new runtime? |
| Agent-Autoloop public rewrite | Deterministic decisions, transactional facts/projections, persisted waits, claim/receipt deduplication and traceable state; pluggable sources/agents/channels/delivery | Single-host state and trusted local plugins; external effects remain at-least-once; actual credential isolation, provider behavior, HA and operational cost unverified | How should CLI agents wake on events, stop while waiting and resume with a recorded decision? |
| n8n | Integration-oriented workflow composition, webhook/worker split and queue-mode execution | Operating Redis/database/workers and external connectors; workflow-specific deduplication, authorization and safe code execution still matter; license restrictions differ from MIT | Is the primary problem connecting services and routing events? |
| Temporal | Durable event-history replay; deterministic Workflow logic separated from side-effecting Activities | Requires a service/database/worker deployment and deterministic workflow discipline; activity retries need a sink-aware contract | Must work survive process failure and long waits across business steps? |
| LangGraph | Code-first cyclic agent state, checkpoint abstraction and explicit interrupt/resume types | Persistence/durability mode and application integration must be chosen; graph state does not isolate tools or authenticate a human decision | Is the primary problem expressing and resuming an agent's state transitions? |
| OpenHands Agent Canvas | Developer-facing conversations, terminal/browser/files and backend selection | Execution/sandbox and event automation are separate services; local host mode is not isolated by the UI | Is the primary problem operating and observing coding agents through a coherent interface? |

Checked 2026-11-04: [Temporal's architecture](https://github.com/temporalio/temporal/blob/d167000789d70a4b3750590008e005747e11c6ce/docs/architecture/README.md) explicitly requires Activities to be idempotent or non-retryable. Durable workflow progression does not make a payment, message or shell command exactly-once. The architecture does not establish that every installation requires multiple nodes, nor does a central service inherently imply an unmitigable single point of failure.

Checked 2026-11-04: [OpenHands' architecture](https://github.com/OpenHands/OpenHands/blob/01d1970b8f96d576d8b42aad48fee5aa117f1cb8/docs/architecture.md) says Canvas does not execute actions, provide sandbox isolation or run scheduled/event automations without a backend. `software-agent-sdk`, `automation` and `typescript-client` are adjacent, unpinned here. Its host development mode explicitly gives the agent host filesystem access; recommending a Docker mode is not proof that mounted files, credentials or outbound effects are safe.

Checked 2026-11-04: [n8n's license](https://github.com/n8n-io/n8n/blob/44bc5b0fec5507b401041de0f4271d5644f3f4a8/LICENSE.md) allows specified internal-business/non-commercial uses under the Sustainable Use License, excludes `.ee` portions into separate enterprise terms, and says other branches are not licensed by that grant. Do not collapse this into either “MIT/open-source equivalent” or “all commercial internal use prohibited.” This is source-based license classification, not legal advice or a deployment decision. The three other comparator root licenses inspected are MIT; service terms and dependencies need separate review before operation.

## What the Articles Establish—and Do Not

### Portal: identity integration is not a complete authorization proof

The portal article describes a roughly 30-person company using an agent-facing MCP integration, Feishu sign-in, publishing, user-bound services and personalized views. It also acknowledges deliberately limited manual configuration paths. These are **author-reported design choices**, not tested authorization properties.

**[INFERENCE]** Reusing identity can remove duplicate account administration, but does not by itself demonstrate resource-level authorization at every deployed application, connector or data sink. A useful verification would exercise direct application access, changed membership, revoked credentials and changed publication scope—not just successful portal login. Agent-only configuration can simplify a narrow operator workflow while making recovery and accessibility depend on that agent path. No result here proves that all reads lack a manual fallback or that the private implementation is vulnerable.

### Event and CI middle tier: coherent decomposition, unknown operational guarantees

The automation article describes a normalized event envelope, agent-editable `rules.json`, keyed grouping, bounded parallelism, roughly 50-second outbound long polling, a single normal notification exit, decision cards and decision/declined-decision records. Its five-stage development flow separates changes, review, fresh-environment checks, deployment and verification of the running revision.

The transferable distinctions are useful:

- Intake noise versus work worth dispatching; event identity versus the target resource being changed.
- A queued job versus a leased worker, a completed command, a committed receipt and an accepted business result.
- Independent review attempts versus an independently grounded acceptance oracle.
- The normal notification path versus failure fallback and a route for genuinely missed decisions.
- A decision record versus an active, current, parameter-bound authorization.

For the **historical private deployment**, receiving-side deduplication and effect idempotency, worker leases/reconciliation, stale approvals, policy activation authority, reviewer isolation, hosted branch protection and backup/failover receipts remain unknown—not proven absent. The later public rewrite makes several corresponding mechanisms inspectable and locally exercisable; its findings are separated below, not back-projected onto that deployment. A 50-second poll timeout does not bound queue delay, work duration or human-decision latency. A fresh VM does not alone prove correct credentials, mounted resources, egress or acceptance checks.

The article describes agent edits to routing rules becoming effective after a check, but does not provide enough enforcement evidence to decide who can activate which policy revision. A remembered owner decision is useful context; it must not be promoted into blanket approval for changed parameters merely because it appears in a file.

### Metrics: preserve attribution, reject outcome inflation

| Reported item | What was checked | What remains unestablished |
| --- | --- | --- |
| 298 PRs, 333 findings, 306 fixed, 51 severe | Numeric text matches the recovered automation article | Finding taxonomy, distinct true defects, dismissed/duplicate findings, severity adjudication, all attempted PRs and escaped defects |
| Review token overhead of 5–15%; roughly two-minute review median | Author-reported text | Complete cost denominator, distributions/tails, re-review and failed-attempt costs, matched baseline |
| Roughly 2–3 minutes to deployment | Author-reported summary | Queue/human wait, unsuccessful attempts, operating window and rollback burden |
| Fewer interruptions and fewer bugs | Narrative plus plausible filtering/review mechanisms | Escalation recall, false negatives, incidents/reverts, rework and accepted outcomes per unit of total effort |
| Strongest-model manager, heterogeneous reviewer | Design heuristic and described model assignment | Universal routing rule, independent ground truth or comparative model-selection effect |
| Announcement: roughly 80 review suggestions, over 70 handled automatically, under an hour | Supplied `paste-11.md` narrative only | Ground-truth dispositions, all attempted work, model/human time and escaped defects; no private outcome reproduction |
| Small kernel, “zero consumption” while waiting, memory/latency figures | Public source exposes persisted waits and a package with no declared runtime dependencies; Node 24+ and external CLIs are still prerequisites | No resource benchmark here; waiting agents can exit while the hub remains resident. Source size/dependency count is not security or total operating-cost evidence |

“306 fixed” is an attributed count of reported fixes. Even if each meant that a review loop accepted a revision, **loop convergence would not establish 306 real defects removed**. The actual disposition definition is unavailable; the panel's stronger claim that convergence was definitely what the counter measured is not adopted. Likewise, a claimed user count or star count is not causal evidence for the pipeline.

The three-round cap is a stopping/escalation mechanism, not a correctness oracle. The primary Anthropic source supports reconsideration after three rounds; the private article's exact terminal policy still needs its own evidence. “No detail published” and “not running at all” are different claims.

## Source-Derived Mechanisms in the Five Named Projects

### AIHOT: inspect the producer and product, not an imagined public control plane

Checked 2026-11-04: [`notify/agent.ts`](https://github.com/KKKKhazix/AIHOT/blob/cd424b0a513c7c8535b6f291b106a3086d6b75bf/packages/backend/src/notify/agent.ts) persists an event before delivery, retains its identity over uncertain HTTP outcomes, records acceptance on HTTP 200 and retries only unaccepted receipts. Its header relies on the hub's idempotency contract. The historical receiver was not inspected; the later Agent-Autoloop rewrite's source/event deduplication was exercised separately, not as an AIHOT-to-deployed-hub integration test.

Checked 2026-11-04: [`notify/deliver.ts`](https://github.com/KKKKhazix/AIHOT/blob/cd424b0a513c7c8535b6f291b106a3086d6b75bf/packages/backend/src/notify/deliver.ts) reserves per-target deliveries transactionally, treats ambiguous sending outcomes as `unknown`, and exposes operator reconciliation. Stale `sending` becomes `unknown`; stale unsent `pending` becomes `failed`. Version-checked operator resend differs deliberately from retrying a transport request to a receiver with an asserted idempotency contract. These are source facts; no database or Feishu request was executed.

Checked 2026-11-04: [`migration-safety.ts`](https://github.com/KKKKhazix/AIHOT/blob/cd424b0a513c7c8535b6f291b106a3086d6b75bf/scripts/migration-safety.ts) and [`check-migrations.ts`](https://github.com/KKKKhazix/AIHOT/blob/cd424b0a513c7c8535b6f291b106a3086d6b75bf/scripts/check-migrations.ts) protect deployed migration history and admit a limited online-migration vocabulary, including bounded catalog-only drops. “No destructive migrations” is an inaccurate paraphrase of this source. The actual checker was exercised below; no SQL was applied.

Checked 2026-11-04: [public CI](https://github.com/KKKKhazix/AIHOT/blob/cd424b0a513c7c8535b6f291b106a3086d6b75bf/.github/workflows/check.yml) describes install/typecheck/build, database-backed tests, browser checks and Docker smoke with collection/model calls disabled. Reading that workflow is neither running it nor verifying hosted branch rules, reviewer isolation, Nix jobs or the private release pipeline. Public product hardening is worth studying without recasting the product as the private orchestrator.

### LongHorizon: final-state verification and contract backcheck

Checked 2026-11-04: [`prompt_texts.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/d53df0aa11e8506dfc9518ef63620c62baee04d3/src/lh_harness/prompt_texts.py) names five useful final-state questions: the actual consumer/state carrier, authoritative inputs, legitimate state-production process, save/submit/persistence boundary, and stale or competing candidate artifacts. Its auditor backcheck reconstructs constraints from the original request rather than assuming the manager's contract is correct. These are prompt instructions, not proof that an auditor model follows them.

The same backcheck distinguishes observable final state from historical process/security claims. A missing transcript is not by itself proof of tampering, and an already-unobservable past non-action cannot be established by repeating the task. Material process guarantees need prospective evidence; do not silently add a stricter acceptance requirement after execution.

Checked 2026-11-04: [`auditor_agent.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/d53df0aa11e8506dfc9518ef63620c62baee04d3/src/lh_harness/auditor_agent.py) parses completion/integrity/contract-audit headers and downgrades completion when recognized blocking constraints remain. [`manager.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/d53df0aa11e8506dfc9518ef63620c62baee04d3/src/lh_harness/manager.py) reconstructs rounds from a ledger, with the last valid record for an index winning and malformed lines skipped. Direct module probes verify those specific behaviors, not semantic truth or an end-to-end crash recovery guarantee.

Checked 2026-11-04: [`dashboard/state.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/d53df0aa11e8506dfc9518ef63620c62baee04d3/src/lh_harness/dashboard/state.py) persists approval records and sends resolution commands through a durable control bus. The exercised path reopens pending records, admits an exact repeated decision once and rejects a conflicting decision. It does not establish actor authentication, expiry, target-revision binding or concurrency correctness for a deployed web service.

The inspected Claude adapter has a bounded workspace mutation-detection path. Do not generalize it into universal protection across every adapter, prevention of arbitrary shell/network effects, or rollback of external effects. Role separation is not automatically privilege separation.

Checked 2026-11-04: the [README benchmark table](https://github.com/AMAP-ML/LongHorizon-Harness/blob/d53df0aa11e8506dfc9518ef63620c62baee04d3/README.md#hundreds-of-real-tasks-measured-gains) reports WeaveBench pass rates 51.8→80.7, OSWorld binary scores 2.8→8.3 and Terminal-Bench success 69.7→77.2, using Qwen 3.7-Plus with Claude Code as execution backend. These are upstream-reported populations/settings, not a reproduction or universal gain. A relative multiplier can coexist with low absolute success. The full Git tree contains all three `eval/` harness families: an initial review confused their omission from the sparse checkout with upstream absence. Source availability does not independently validate the reported results.

### Prime: useful state machinery, unchanged adoption boundaries

The [owning Prime survey](prime-agent-survey-2026-08-06.md#control-plane-comparison-refresh--2026-11-04) preserves the older TypeScript survey, October Rust-port refresh and current delta separately. Current mechanisms are not retroactive proof for the old tree.

Checked 2026-11-04: [Python harness state](https://github.com/PrimeIntellect-ai/prime-agent/blob/c4d42018379d4da8e522bacb3118e128f90a99f9/prime-agent-runtime/src/rlm/harness.py) uses locked, atomic replacement, but loads malformed state as empty. The current fixture confirmed that a later write replaces the malformed bytes without retaining a backup in that fixture. Atomic writing and preservation of corrupt evidence are different properties. A synchronized two-process schedule preserved both distinct updates; this is not exhaustive race or crash proof.

Checked 2026-11-04: Rust [`refinement/mod.rs`](https://github.com/PrimeIntellect-ai/prime-agent/blob/c4d42018379d4da8e522bacb3118e128f90a99f9/crates/pa-core/src/refinement/mod.rs) retains the empty-state fallback and subsequent locked update path. Project-local skill discovery feeds Python bootstrap; [`venv.rs`](https://github.com/PrimeIntellect-ai/prime-agent/blob/c4d42018379d4da8e522bacb3118e128f90a99f9/crates/pa-core/src/kernel/bootstrap/venv.rs) installs missing/changed Python skills with `uv pip install --editable`. The inspected path provides no confirmation at that install point. No package installation or exploit was executed; this is source-derived trust-surface evidence, not a claim that merely displaying any directory always executes a package.

The source delta includes refinement disabling and daemon/journal hardening. The exercised Python setting gate rejected a refinement mutation when disabled. In-context structured edits and their rollback proposals are not model-weight learning or reversal of external side effects. Source-read journal recovery and Rust behavior were not executed.

**PA-1/PA-2 remain deferred; PA-3 concept-only; PA-4 rejected; PA-5 blocked.** Better upstream isolation would warrant a fresh assessment but would not itself authorize lifting TeaPrompt's runtime non-goal or any held candidate.

### khazix-skills: workflow contracts and desktop helpers, not the hub

Checked 2026-11-04 at `35bd05b4`: this repository publishes six distinct skills, not the event coordinator described in the articles. The later Agent-Autoloop repository supplies that separate public surface. The methods below are reference patterns; their prompt wording does not establish installed-host compliance.

| Surface / pinned source | Transferable method | Qualification |
| --- | --- | --- |
| [leader](https://github.com/KKKKhazix/khazix-skills/blob/35bd05b466ceb83a727b28afb54b45b69a6c3b0a/leader/SKILL.md) | Check repository facts before asking; distinguish goal, proposed means and constraints; split execution from research; name evidence, write ownership and failure signals | A compact brief and held-back checks can help, but do not create a sealed oracle or filesystem sandbox. Its 4,000-character and three-failure heuristics are not universal limits. “No come back to me” wording must be read with its explicit authorization boundaries, not as permission to bypass a consequential decision |
| [neat-freak](https://github.com/KKKKhazix/khazix-skills/blob/35bd05b466ceb83a727b28afb54b45b69a6c3b0a/neat-freak/SKILL.md) | Reconcile code, runtime, docs, rules, authorized memory and workspace; distinguish merged, deployed, live-verified, knowledge-closed and cleaned | Inspection depth does not expand authority; irrelevant surfaces may be not-applicable. A clean tree is not evidence of production state, and age/size is not deletion authority |
| [hv-analysis](https://github.com/KKKKhazix/khazix-skills/blob/35bd05b466ceb83a727b28afb54b45b69a6c3b0a/hv-analysis/SKILL.md) | Compare historical development with contemporaneous alternatives; preserve primary-source priority, dates, conflicts and unknowns | A useful research organization, not evidence of causal superiority. Do not import its broad trigger, long-report preference or PDF dependency merely to preserve the method |
| [khazix-writer](https://github.com/KKKKhazix/khazix-skills/blob/35bd05b466ceb83a727b28afb54b45b69a6c3b0a/khazix-writer/SKILL.md) | AI assists evidence, alternatives and structure; the user owns firsthand experience, selected angle and final voice | Style instructions cannot authenticate experience. Claims about what AI can never create are the author's stance, not a measured universal capability boundary |
| [storage-analyzer](https://github.com/KKKKhazix/khazix-skills/tree/35bd05b466ceb83a727b28afb54b45b69a6c3b0a/storage-analyzer) | Tiered actions, protected roots/worktrees, canonical-path checks and an inspectable report | Executable deletion capability, not prompt-only advice. Stable-path direct-function probes passed; HTTP authorization, races, Windows junctions and host-wide cleanup remain untested |
| [aihot client skill](https://github.com/KKKKhazix/khazix-skills/tree/35bd05b466ceb83a727b28afb54b45b69a6c3b0a/aihot) | Packages access to a named product; installer/package verification offers a concrete distribution boundary | Distinct from the AIHOT backend and control-plane hub. Installer and network behavior were not executed; distribution checks do not certify product availability or content quality |

The storage probe exercised the actual `build_report.py` CLI and inspected emitted HTML/data escaping without opening a browser. This is output evidence, not a visual or DOM/XSS audit. No skill, installer, PDF toolchain, HTTP server or real-home scanner was installed or run.

### Agent-Autoloop: public state mechanisms with explicit effect boundaries

Checked 2026-11-04 at `cecec75b`: [`decide.ts`](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/kernel/decide.ts) takes state, input, time and environment explicitly. [`store.ts`](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/kernel/store.ts) and [`host/runtime.ts`](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/host/runtime.ts) commit facts and projections together using SQLite WAL/FULL before answering. This separates deterministic state decisions from effectful host/plugin work; it does not put an external API call inside the SQLite transaction.

- **Identity and replay:** source/event identity deduplicates ingestion; the exercised changed-payload retry kept the first payload rather than reporting a parameter conflict. Claim replay and stale-token rejection were observed. An identical result under the same accepted token was acknowledged as duplicate; a changed result conflicted. These are different contracts, not one universal idempotency rule.
- **Waiting and recovery:** an `ask` result persists a card and lets the execution round finish; an accepted answer queues continuation with the saved session/context. The probe observed persisted waits, a synthetic missing-run transition to `unknown`, late-result acceptance, fact-derived trace, projection rebuild and clean second-process reopen. No agent was launched, so process/token savings were not measured. The [README](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/README.md) and [security statement](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/SECURITY.md) explicitly distinguish process-kill checks from untested whole-machine power loss; this survey ran neither campaign.
- **Bounded cascades:** returned events inherit an incremented hop count; human answers/timers preserve the chain context. Hop nine was recorded but not dispatched in the fixture. This bounds one causal chain, not unrelated events, total spend, global rate or service availability.
- **Instruction/data separation:** [`validate.ts`](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/protocol/validate.ts) rejects event control fields, while [`worker/contract.ts`](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/worker/contract.ts) directs the agent to read event text as data. Source-read field separation prevents that structural override; it is not complete prompt-injection resistance. `askFirst` depends on the agent/adapter, `command` does not sandbox arbitrary programs, and same-account file permissions do not isolate secrets.
- **Decision authority:** channel answers and run tokens have scoped checks; the exercised link is a bearer capability for one card and expires after seven days. This is not third-party OAuth refresh, universal approval expiry, or proof that every downstream effect is bound to unchanged target parameters. Trusted plugins execute as local code. The source's owner/channel restrictions still need a real-host and real-provider check before deployment.

Checked 2026-11-04: [`delivery.ts`](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/plugins/delivery/delivery.ts) reads settings from `main`, rechecks the PR head, current main and labels before merge, reads back ambiguous merge outcomes, and separately verifies configured release/health state. [`review.ts`](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/plugins/delivery/review.ts) builds a text-only Git snapshot without checking out PR code; the default Codex command disables user configuration/memory and requests read-only permissions. These are valuable source mechanisms, not an executed PR pipeline, verified model sandbox or substitute for hosted branch protections. A custom review command carries its own permission obligation.

### Plugin semantics: determinism is not effect-once delivery

C13 identifies a real integration boundary, but **reentrancy, deterministic output and effect idempotency are not synonyms**. A repeatable function can still publish twice. The [plugin protocol](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/docs/plugins.md) separates event, agent, channel and delivery extensions; their external systems have different failure semantics.

| Boundary | Public source / observed behavior | Remaining contract question |
| --- | --- | --- |
| Effect completed, result receipt lost | Internal duplicate receipts are handled, but the external action is outside the hub transaction | What operation key, target/parameter binding, provider retention and query path decide whether replay is safe? |
| Card sent, delivery acknowledgement lost | Actual hub probe reissued the card after a minute with no external message reference | How does the sink distinguish “not sent” from “sent but unacknowledged”? Retrying the hub record alone cannot decide |
| Feishu versus generic Webhook | [Feishu source](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/plugins/feishu/channel.ts) sends a card-derived idempotency key and updates known messages; [Webhook source](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/plugins/webhook/channel.ts) lacks an external once-only guarantee | Provider semantics/retention were not exercised. Do not generalize the Feishu key to every plugin or to arbitrary agent actions |
| Credentials expire or require the owner | Worker prompt preserves completed work and asks for human recovery; seven-day card-link expiry is separately enforced | Which errors are transient, revoked or human-only; who may refresh credentials; what access remains after revocation? No provider-auth lifecycle was exercised |
| Partial success | Public delivery code reads current external state; worker prompt says to retain completed business and unaccepted steps | Reconcile actual sink state before replay. Compensation is a separately authorized effect, not an automatic inverse or proof that the original effect did not happen |

**[INFERENCE]** A useful prospective plugin review would inject loss after the sink commits but before acknowledgement, inspect the sink independently, and test replay with both identical and changed parameters plus credential revocation. This is a reference test design, not a new TeaPrompt interface, an executed external test or permission to compensate a real transaction.

## Evidence Actually Executed

Coordinator-owned probes imported unmodified upstream modules or invoked the real CLI at the main revisions above. They used disposable fixtures, minimal environment variables and a macOS `sandbox-exec` profile denying network, `/Users` reads, a synthetic canary and writes outside the scratch work directory except `/dev/null`. Six positive/negative controls checked owned read/write, outside-write denial, canary denial, user-directory denial, network denial and child-process inheritance. These controls qualify this probe environment, not the upstream products or other operating systems.

| Target / input | Observed result | Boundary |
| --- | --- | --- |
| Prime persisted entry, reopen, file alias and parent-directory symlink | Entry retained; new store mode `0600`; aliases resolve to their target, all within disposable work | Explicit store paths are canonicalized, not constrained to a project root; no actual user files touched |
| Prime two-process stale snapshots | Both writers exited 0 and both distinct entries survived | One synchronized schedule, not arbitrary concurrent/crash safety |
| Prime malformed JSON followed by a write | Empty load, then previous malformed bytes replaced; no fixture-local backup found | Concrete corruption-recovery tradeoff, not universal irreversible data-loss frequency |
| Prime disabled refinements | Mutation rejected with the disabled-setting diagnostic | Exact Python operation; no model review/refinement campaign |
| LongHorizon real `init`, repeated `init`, unsupervised `run --resume`, invalid `[run]` key | First init 0; existing-config refusal 1; resume/config refusals 2; rejection paths created no run | No model/GUI/web process or full supervised resume |
| AIHOT migration checker over disposable Git history | Unchanged history admitted; edit/delete of deployed migration rejected; bounded new `DROP` admitted; plain index rejected; concurrent `IF NOT EXISTS` index admitted | Actual checker modules; no database, SQL application, private CI or production |
| LongHorizon audit reports | Clean/aligned fixture `complete`; recognized blocker `incomplete`/`unknown`; missing header `blocked` | Grammar/control result, not independent truth of the synthetic report |
| LongHorizon round ledger with duplicate index and truncated tail | Latest valid duplicate won, indices reconstructed in order, partial tail ignored; latest audit controlled completion predicate | Direct reader invocation, not a supervisor/process-crash campaign |
| LongHorizon persisted approval reopened in a second state object | Pending decision recovered; invalid action/input rejected; exact retry admitted once; conflicting choice rejected | Sequential local control-bus calls, not web authentication, concurrent requests, expiry or changed-target authorization |
| khazix storage tiers, protected roots/worktrees and symlink fixtures | Allowed synthetic cache removal succeeded; other tiers and outside targets survived; stable direct/parent aliases rejected as specified; bounded traversal excluded symlink bytes | Six groups including the actual static-report CLI; no live HTTP/browser, real Trash, Windows, TOCTOU or whole-home scan |
| Agent-Autoloop decisions, event/claim/result replay and persisted wait | Deterministic fixture decisions; first event payload retained; stale token and changed receipt rejected; wait/session state persisted | Direct public host/kernel functions with disposable SQLite; no model, worker or external effect |
| Agent-Autoloop card resend, answer binding and link expiry | Unacknowledged card reissued with `ref: null`; tested invalid answer rejected; seven-day link expired | External duplicate suppression, user authentication over HTTP and provider credential renewal not tested |
| Agent-Autoloop unknown/late result, hop boundary, rebuild and reopen | Missing-run fixture became unknown and accepted a late result; hop nine not routed; fact replay and a second process recovered matching projection | Ten groups across this and the preceding two rows; clean reopen is not SIGKILL, power loss, backup recovery or HA |

Five successful drivers cover **33 named scenario groups** (8 Python state/CLI, 6 migration, 3 additional LongHorizon state, 6 khazix storage/report and 10 Agent-Autoloop), not 33 independent product trials. The recorded exit-0 stdout JSON `scenarios` arrays supply that population; the failed pre-scenario invocation is excluded and retained below. Commands used the same `sandbox-exec -f <profile>` boundary with `python3 -B -S <probe.py>`, `node <migrations.mjs>`, `python3 -I -B <longhorizon-state.py>`, `python3 -I -B -S <khazix-probe.py>` and `node --disable-warning=ExperimentalWarning <autoloop-probe.mjs>`. The six containment controls also passed inside the Node kernel driver. Commands, source pins, stdout/stderr and driver/profile digests are retained in the companion evidence ledger; this record internalizes the inputs/results/limits without depending on the scratch workspace.

**Failures and warnings retained:** the first additional LongHorizon state invocation used `-S` and exited 1 before any scenario because it hid the declared `packaging` dependency. The environment was corrected to isolated `-I` using already-installed `packaging 25.0`; no dependency installation, upstream edit, stub or changed expectation was used. The migration probe emitted denied macOS `xcrun` cache-write diagnostics outside the scratch boundary while its Git fixture and checker scenarios completed; permissions were not relaxed and those diagnostics remain in stderr.

Not run: full upstream test/build suites; Rust daemon/kernel/skill bootstrap; model or performance campaigns; GUI/browser surfaces; khazix installation, HTTP server or real-home scan; Agent-Autoloop HTTP server, plugins, SIGKILL or power-loss campaign; Redis/PostgreSQL, Feishu, Nix, Docker or Temporal services; private hub/portal; hosted branch protections; HA/failover, restoration or billing experiments. No full-product safety or efficacy conclusion follows from the local probes.

## Thirteen Supplied Comments: Questions, Counterarguments and Falsifiers

These are user-supplied references, not independently authenticated posts. Each is represented without treating agreement as consensus or importing unrelated instructions.

| ID / attributed commenter | Useful question and adjudication | Evidence that would support or overturn it |
| --- | --- | --- |
| C1 — ShenDuAILab | Start from concrete repeated work; manual understanding can precede automation. Do not turn the traffic/YouTube/TikTok suggestion into authorized business work | Compare accepted outcomes and rework on a defined workflow before/after automation; articles alone are not a reproduction recipe |
| C2 — jinbuge102 | Event intake, deduplication, bounded work and decisions matter beyond prompt wording. “Cyber leadership” is an interpretation, not a measured architecture property | Trace one event through dispatch, effect, receipt and acceptance; test duplicate/crash boundaries. Three review rounds still do not authorize merge |
| C3 — howardl70735386 | Availability, monitoring and maintenance are legitimate questions. Do not prescribe HA machinery without an SLO or claim it is absent because the article omits it | Name workload, outage tolerance, RTO/RPO and restore evidence; observe worker loss, queue age and failover. CPU/bandwidth alone do not establish correct outcomes |
| C4 — JeffSmithAi | Model/human intent can diverge, especially around taste, context and product choices; autonomy can amplify a wrong objective | Prospective acceptance examples, disputed decisions and owner-correction rates; neither fluent summaries nor universal incapacity claims settle the issue |
| C5 — Santhtony | Human approvals can remain the bottleneck; private execution is unverified | Real end-to-end traces and approval latency including failures. Missing public receipts neither establish nor refute deployment |
| C6 — ibx1112599 | Decision-card quality may matter more than model count; fewer decisions are not necessarily better | Assess evidence completeness, correct routing, escalation precision/recall, omission audits, approval time and later reversals |
| C7 — xiaoshan0413 | Deterministic filtering may save model work and attention; “rules rather than better models caused the gains” is not demonstrated | Same task/event distribution with filtering/model changes isolated; sample suppressed events and measure missed material decisions |
| C8 — Ra1noy | Trust may be earned operationally, but the anecdote about no longer reading code cannot transfer authority or eliminate verification | Stable outcome/error evidence under bounded grants, protected checks and accountable owners; human-review amount is a risk decision, not a trust slogan |
| C9 — luo_luoche97272 | The article can complement Grok/poteto's trust/routine pedagogy with an event/control-plane account | Link the existing Grok record; reader enthusiasm is not a usability study, and neither system supplies proof for the other's runtime |
| C10 — cc6pazpo | Task decomposition can reduce attention demands, but fragments also require coordination and reintegration | Compare bounded-task and coarser-task outcomes including handoff errors, shared-state conflicts and merge effort, not just parallel task count |
| C11 — yuexuan2333 | Attention scarcity recurs across this discussion and Super-agent | Record external conceptual recurrence; require independent outcomes for efficacy and a local failed consumer before a new TeaPrompt promotion |
| C12 — TheEasySale1 | Context contention and opaque failure location are credible risks, not demonstrated bottlenecks of this deployment. Separate trigger/execution/review, stabilize small tasks before scaling; the author's most effort-consuming stage remains unknown | Compare small and expanded workloads, ownership conflicts, queue age, missed handoffs and time to diagnose/recover. Public causal traces aid investigation but do not measure operator effort |
| C13 — acejou27 | Preserve the concern about duplicate effects, expired credentials and partial success; distinguish deterministic output/reentrancy from sink idempotency | Public hub resend was exercised; external effect-once was not. The plugin table above names parameter binding, lost acknowledgements, provider expiry and authorized reconciliation/compensation boundaries |

The [Grok/pstack follow-through](agent-efficiency-autonomy-learning-survey-2026-11-01.md#grok-methodology-follow-through--2026-11-04) already owns the trust-versus-authority/routine-admission comparison. The [Super-agent supplement](agent-efficiency-autonomy-learning-survey-2026-11-01.md#full-text-follow-through-2026-11-02) owns its multi-owner handback evidence. Those records are complementary references, not additional private-system replications.

## Parallel Socratic Review and Adjudicated Disagreement

The first shared packet was read by six concurrently dispatched read-only roles: AIHOT mechanisms, LongHorizon mechanisms, Prime delta, comparator architecture, trust boundaries, and evidence/human factors. They received the eleven-comment addendum. Two further parallel lenses reviewed the later khazix-skills input; another two reviewed the later public Agent-Autoloop disclosure and received C12/C13. The initial six did not review those later inputs. The coordinator owned execution, corrections and publication. Full outputs were retained: **ten advisory lenses in three scoped batches**, not independent empirical replications or verified different-model channels.

| Lens | Contribution retained | Coordinator qualification / rejected extension |
| --- | --- | --- |
| AIHOT mechanisms | Product-versus-control-plane split; durable handoff and migration vocabulary | Source/fixture observations are not deployed database/CI results |
| LongHorizon mechanisms | Final-state questions, original-request backcheck, local recovery and approval paths | Corrected false `eval/` absence from sparse checkout; proposed checklist promotion remains reference-only; “stdlib-only” probe recipe corrected after the import failure |
| Prime delta | Rust/Python corruption path, editable Python-skill trust surface, refinement/journal changes | Corrected main/tag conflation; no universal instant data-loss claim or executed bootstrap exploit; earlier PA decisions preserved |
| Comparator architecture | Integration, replay, graph state and developer-control surfaces are different layers | Rejected “Canvas itself guarantees sandbox safety,” mandatory multi-node Temporal framing, blanket exactly-once external effects, and an unnecessary new schema verifier |
| Control-plane trust | Identity versus sink authority, dispatch deduplication versus effect idempotency, approval scope and policy activation | Article omissions become unknowns and prospective probes, not confirmed deployed vulnerabilities |
| Evidence / human factors | Denominators, missing-incident channel, approval load and attention-cost questions | “306 fixed” remains reported fixes, not proven convergence or real bugs; poll timeout is not a latency guarantee; no known-present private system inferred from popularity |
| khazix workflow methods | Brief ownership, research/execution split, evidence/status closeout, source-aware research and human-owned writing | Fixed limits are author heuristics; prompt rules do not seal oracles or enforce host paths; no new standalone Skill |
| khazix executable bounds | Desktop helper guardrails, package/installer scope and source-versus-runtime distinctions | Direct synthetic cleanup/report evidence does not establish HTTP authorization, visual safety or host-wide cleanup; “not the hub” applies to this repo, not every public Khazix repo |
| Autoloop state mechanisms | Deterministic decisions, transactional log/projection, persisted waits, replay and hop boundaries | Public rewrite supersedes blanket source-unavailability; upstream crash/benchmark descriptions are not coordinator executions; historical private gains and whole-machine recovery remain unknown |
| Autoloop authority/delivery | Trusted-main review configuration, commit-bound checks, scoped answer/run capabilities and channel-specific delivery | Default review flags are not a verified sandbox; internal deduplication does not cover external effects; link expiry is not provider credential renewal |

All completed lenses returned **AGREE WITH CHANGES** within their assigned scope. This is agreement about the research frame, not blanket endorsement of every sentence. The main disagreement was destination: mechanism-focused proposals favored importing checklists/schema fields; evidence/minimality favored an auditable reference only. The coordinator chose the latter because no local failing consumer established a missing contract. Earlier “no public hub” framing was narrowed after the disclosure; source-only test/performance assertions were not promoted into observed results. Corrections follow evidence, not vote count.

### Answered Socratic questions

1. **Are these competing systems?** Only partly. AIHOT is a product with an event producer; Agent-Autoloop publishes a hub rewrite; khazix-skills supplies workflows/helpers; LongHorizon verifies long tasks; Prime supplies a local execution/context environment; n8n, Temporal, LangGraph and Canvas address different coordination needs. A single “best agent framework” score would mix unlike claims.
2. **What survives a crash?** Only the state and effects covered by a particular persistence/receiver contract. Observed local reload, ledger reconstruction and decision deduplication do not prove distributed recovery. A timeout after an external effect remains ambiguous without a receiver query, idempotency contract or explicit reconciliation.
3. **Who decides that completion is real?** A final consumer/result and original-request acceptance, not merely a reviewer header, green CI, deployment revision or another model's agreement. A review model can supply evidence and criticism without becoming the human intent owner.
4. **Does removing interruptions improve work?** Possibly, but only if material decisions and errors are not silently filtered out. Count suppressed/undecided items, incidents and rework alongside human minutes and token spend.
5. **Is rejecting a new runtime reflexive minimalism?** No. A separately authorized product with durable multi-system work might justify one. TeaPrompt currently supplies methodology, not that service; useful external patterns do not prove a local runtime requirement.
6. **What would reverse the documentation-only decision?** A reproduced gap in a named delivered consumer, a separately approved operational requirement, or new source/host evidence that changes a particular held decision—not another similar article or panel majority.

## Measuring Attention Without Hiding Failure

This is an **[INFERENCE] evaluation design**, not a performed study, new verifier or authorization to run a campaign. Define the unit before comparing systems: incoming event, work attempt, distinct finding, PR, human decision, deployed change and accepted outcome are not interchangeable.

| Outcome family | Useful evidence | Failure hidden by the easier metric |
| --- | --- | --- |
| Intake / filtering | All eligible events, suppressed-event sample, duplicate definition, material-event recall | Fewer wakes/cards by dropping difficult or important events |
| Review quality | Distinct adjudicated defects, severity rubric, false positives and escaped-defect channel | More findings or closed threads mistaken for better code |
| Human attention | Decision preparation plus reading, waiting, correction, override and incident-recovery time; latency distributions | Shorter approval clicks while burden moves to debugging or recovery |
| Throughput / cost | Accepted outcomes over all attempted work, model/infrastructure/human costs and rework | Successful-only medians, omitted retries or token savings with worse outcomes |
| Reliability / recovery | Declared SLO, backup restoration, outage/worker-loss behavior, pending/unknown outcomes | Heartbeats, CPU graphs or durable rows mistaken for business continuity |
| Intent / authority | Parameter/target-bound decisions, expired/revoked approvals and owner corrections | Historical precedent or fluent card wording mistaken for current approval |

A matched workload and independently adjudicated outcome sample would help compare topology/filtering choices. Cross-model or multi-role review alone does not provide that independence. No new universal threshold, numeric review cap or requirement for heavyweight HA is adopted here.

## TeaPrompt Mapping and Candidate Adoption Ledger

Existing contracts already address the decision classes: [research](../skills/reflective-research/SKILL.md) separates source/claim/inference; [review](../skills/reflective-review/SKILL.md) challenges acceptance and evidence; [implementation](../skills/reflective-implement/SKILL.md) exercises consumers; [runtime trust boundaries](../04-agent/runtime-trust-boundary.md) separate authority, effects and recovery; [workflow acquisition](../04-agent/workflow-acquisition.md) distinguishes a captured method from an operational runner; [minimality](../skills/reflective-minimality/SKILL.md) preserves safety floors; [artifact promotion](../04-agent/artifact-promotion.md) governs new durable surfaces. Textual coverage is not proof that a host enforces these contracts.

| ID | Candidate | Disposition | Evidence / destination / reopen trigger |
| --- | --- | --- | --- |
| CP-DOC1 | Preserve matched-layer comparison, public-rewrite correction, bounded observations and thirteen-comment analysis | Adopted: reference documentation only | This record, append-only Prime refresh, existing catalogue and generated discovery; authorized by the owner's survey/document request |
| CP-SK1 | New control-plane/leader/closeout/domain Skill, copied final-state guard or schema verifier | No change | No missing delivered contract or failing local consumer demonstrated; re-open the smallest existing surface if a concrete gap is reproduced |
| CP-EVAL1 | Product-specific attention/omission and recovery evaluation | Deferred; not a task or campaign grant | Needs named product/workload, authority, ground-truth adjudication, sink contracts and an approved execution envelope; this record supplies questions only |
| CP-RUN1 | Install/adopt/deploy the private hub or any surveyed runtime into TeaPrompt | Not adopted | Operational layer outside this request and project direction; isolated source probes are not deployment qualification |
| Prior PA-1–PA-5 | Prime structured ledger, refine gate, RLM concept, runtime adoption and deployment | Unchanged | PA-1/2 deferred, PA-3 concept-only, PA-4 rejected, PA-5 blocked; current source/fixture evidence appended in the owning record |

## State Ledger and Evidence vs Inference

| Claim / item | Status | Checked / evidence | Remaining boundary |
| --- | --- | --- | --- |
| Source pins and branch/release splits | verified | 2026-11-04 Git refs/peels and selected primary files | Volatile refs must be checked again for later adoption |
| Public AIHOT product differs from private portal/hub | verified | Source scope and supplied/recovered author accounts | Private runtime not audited; no nonexistence claim |
| Three rounds imply automatic success/merge | refuted as a claim about the cited first-party method | Primary Anthropic article, checked 2026-11-04 | Private terminal policy unverified |
| Article figures appear in recovered author text | verified for text; needs-qualification for outcomes | Attributed body comparison, 2026-11-04 | No adjudicated defect counts, causal effect or independent operation receipts |
| LongHorizon lacks an `eval/` tree | refuted | Complete Git tree query at `d53df0aa`, 2026-11-04 | Benchmark results not reproduced |
| Main revision equals latest release in Prime/LongHorizon | refuted | Separate pinned commits, 2026-11-04 | Identity difference alone is not behavioral difference |
| Prime corruption fallback and bounded write behavior | verified for executed Python inputs | Recorded direct-module smoke, 2026-11-04 | Rust/source-only findings and other failure schedules unexecuted |
| AIHOT restricted drops are admitted by checker | verified for executed checker inputs | Disposable Git fixture, 2026-11-04 | No SQL execution or production-safety claim |
| LongHorizon refusal/parser/ledger/approval cases | verified for executed inputs | Real CLI and direct-module smoke, 2026-11-04 | No end-to-end agent, web-security or restart campaign |
| Thirteen comments establish efficacy/consensus | needs-qualification | Supplied-reference analysis, 2026-11-04 | Hypotheses and counterarguments only; operator effort distribution unknown |
| Public control-plane source is unavailable | refuted for the new rewrite | Agent-Autoloop `cecec75b` source and direct state probe | Historical private deployment correspondence/guarantees remain unknown |
| khazix prompt/helper boundaries | verified for selected source and executed storage inputs | `35bd05b4` source, direct functions and report CLI | No installed-agent compliance, browser/HTTP or race-safety claim |
| Autoloop replay, wait, link expiry and reconstruction | verified for executed inputs | Disposable SQLite public host/kernel probe | No external effect-once, provider auth, real worker, crash/HA or deployment qualification |
| Private HA, approval binding and isolation | unknown | Source/host evidence unavailable | Explicitly retained; not converted into defects or certified guarantees |
| New local Skill/runtime need | unverified | Existing contract mapping, 2026-11-04 | Local demand/utility unknown; no promotion, no claim of zero demand |

**Sufficiency gate:** the decision depends on pinned source scope, observed bounded behavior, explicit corrections and existing local ownership—not on private deployment claims, unmeasured gains or new operating authority. All load-bearing claims are source-bound or explicitly unknown; scoped reviewer disagreements and all thirteen comment perspectives are preserved. The blind spots are private operational ground truth and live integration behavior: missed events, incidents, approvals, external effects, credentials and total maintenance cost. More lookalike repositories would not resolve them, so research stops here.

## Falsifiability and Handoff

- Authenticated private source/configuration plus independent receipts could establish specific controls currently unknown. Reassess those controls without retroactively upgrading this record.
- A matched outcome study including omissions, failures, rework and total human cost could support or overturn the attention/quality claims. Panel agreement cannot substitute for it.
- A changed upstream receiver contract, migration vocabulary, audit grammar, persistence/bootstrap path or comparator responsibility invalidates the corresponding source-bound observation; re-pin and exercise the changed surface.
- Prime corruption quarantine/recovery and a verified project-local execution authorization boundary could reopen PA-5. They would not automatically approve PA-1/2 or reverse PA-4.
- A local consumer failure against an existing declared contract could justify an in-place repair; a separately authorized operational product might justify a runner. External recurrence alone establishes neither.

Publication acceptance: preserve all three articles, five named projects, four comparator roles, thirteen references, the scoped 6+2+2 review, failures/limits and prior dispositions; expose the record through the existing catalogue/index and actual composer; verify repository compatibility. The [delivery report](../../review/final-report.md#agent-control-plane-comparison-publication-2026-11-04) records publication checks separately from upstream observations. No Skill, operating-rule, oracle, runtime or deployment change is made.
