# MAMUBench / Worse Together Survey — Fidelity and Contract Map (2026-11-20)

Language: English

> **Status:** source-qualified reference record (`MAM-DOC1`); no Skill, prompt-body, operating-rule, or runtime change. The owner supplied two sources — `alignment.anthropic.com/2026/worse-together/` and `github.com/safety-research/MAMUBench` — plus two zh-TW summaries (one inline, one via `x.com/kingofspace0wzz`). This record verifies every numeric claim against the primary post and the repository. No installs, model calls, Skill changes, commits, or pushes are authorized.

## Research Question

Are the digest's figures and mechanism claims faithful to the primary publication and repository, and does the work expose anything missing from TeaPrompt's contracts?

## Direct Recommendation

**Adopt the record only.** The authors report that, across all 25 scenarios and models, the request was sent in 94–99% of episodes but was in the committing agent's context in only 47–67%. (Figure 4 plots only the two Claude models — Opus 98.6%→65.0%, Sonnet 93.6%→47.1%; the 67% upper bound comes from a model it does not plot.) Blocking checkout until pending messages were read recovered 62–73% of rerun failures. These measure different things; neither establishes that every affected user agreed. TeaPrompt describes approval and evidence requirements but provides neither a mailbox guard nor a multi-user consent service.

## Evidence Used

| Source | Class | What it supplies |
| --- | --- | --- |
| [Worse Together post](https://alignment.anthropic.com/2026/worse-together/) (Paliskara, Namchittai, Tay, Griffin, Lampinen; Anthropic Fellows, 2026-11-11) | **Primary** — full blog text with figures | Verbatim basis for every number below |
| [MAMUBench repo](https://github.com/safety-research/MAMUBench) | **Primary** — README, repo tree, license, setup | 74-scenario count, three released envs + runnable merge queue, MIT, modal/local harness, model keys |
| [arXiv 2610.00583](https://arxiv.org/abs/2610.00583) | Linked paper | Full experimental detail behind the post |
| X reshare `2122495202216841395` | Owner-supplied secondary | Privacy/permission/audit framing — treated as commentary, not an independent source |
| Prior TeaPrompt records | `mcode-stack-survey` (coordination), `agent-trust-pyramid` (oracle precedence), `claude-code-verification-survey` (guardrails) | Baseline for contract map |

## Fidelity Ledger

| # | Digest/paste claim | Primary check | Verdict |
| --- | --- | --- | --- |
| 1 | Coordinator beats per-user peer team in all four environments; ~10–45pp | Figure 2: Opus 64 vs 30, 84 vs 71, 88 vs 44, 92 vs 81; Sonnet 32 vs 12, 74 vs 65, 75 vs 37, 93 vs 78 | **verified** |
| 2 | Sent vs in-commit-context, illustrated by the gluten-free order: 94–99% sent, 47–67% in context | Figure 4 aggregates all 25 personal-assistant scenarios but plots only the two Claude models: 98.6%→65.0% (Opus), 93.6%→47.1% (Sonnet) — the 47–67% range is the authors' own and its upper bound comes from a model the figure does not plot; the gluten-free order is one example scenario, not the denominator | **verified with corrected denominator** |
| 3 | "Read all pending messages" guard recovers 62–73% of failures | Mitigation section: 73.1% (Opus), 62.3% (Sonnet) | **verified** |
| 4 | Unconsented cancellation of others' jobs scores higher → eval blind spot | "Episodes in which agents canceled or shrank other users' jobs without asking usually got a higher group score" + "scoring only looks at total value… not whether anyone had their work destroyed or agreed" | **verified** |
| 5 | 74 scenarios, three environments | README: 74 across api_key, clinic, personal_assistant; merge queue is a fourth runnable env not in the 74 | **verified** — digest says "74 個多使用者協作測試場景" correctly |
| 6 | Privacy, permission, audit boundaries as key risks | Discussion: consent, override, fabrication about other users; README frames per-user agents | **verified** — matches digest's three-bullet framing |
| 7 | "Multi-agent < one coordinated agent" | Coordinator is the control and wins in all four envs | **verified** — the paper itself notes this is formation-dependent and not always feasible |
| 8 | Message sync, shared resource, permission boundary as the three problem classes | Sections on acting too little/too late, racing checkout, unconsented cuts, fabrications | **verified** |

## TeaPrompt Contract Map

| Paper mechanism | Existing surface | Disposition |
| --- | --- | --- |
| Coordinator outperformed peers in four simulated environments | `flow-control-generator` describes several topologies, including orchestrator/worker | A coordinator is one option, not the default for all shared-resource tasks. The host executes the chosen topology. |
| Block checkout until the committing agent reads its pending messages | [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md) distinguishes a gate from evidence of host enforcement | Related principle only. The benchmark tested a specific mailbox precondition; the library does not supply it. |
| Agents acting too little/too late (stall) | `flow-loop-harness` stall/heartbeat loop-template clause (host-executed) + `03-context/context-handoff.md` | Method present — the template emits the check; the host runs it |
| Cancellation of another user's work without consent | [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md) §4 requires Human Review for destructive actions; §4a records the acting principal, scope, approval source and epoch | Approval for an action is not evidence that every person affected consented. The host must enforce whichever approvals its policy requires. |
| Fabricated claims about other users' data | Written anti-cheating oracle separation; "a green run proves its tested assertions" | Written-rule present — a methodology claim, not a run here |
| Group-outcome-vs-behavior eval gap | `golden-benchmark-runner` methodology (measured outcome plus behavioral check); incident→rule admission | Method present — methodology only; no benchmark was run for this record |
| Shared-resource consent and audit trail | [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md) §4a specifies what authority and outcome evidence to retain | A record schema is not a receipt from the host, much less proof of another user's consent. |
| Model-dependent failure modes differ (Opus vs Sonnet vs GPT vs Qwen) | `golden-benchmark-runner` comparison harness (host-run methodology) | Method present — no MAM model-matrix run was executed here |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Reopen condition |
| --- | --- | --- | --- |
| MAM-DOC1 | This dated record + catalogue navigation | **Adopted — reference documentation only** | A corrected paper, a new benchmark version, or a local consumer failure |
| MAM-DOC2 | Optional worked example of the unread-message checkout guard | **Deferred** | Reopen for an independent source using that same precondition, or a local need for it. Agentflow's request/digest/HEAD check is different: a new message can arrive while HEAD is unchanged; HEAD can move while the mailbox is empty. |
| MAM-SK1 | Skill/prompt-body change encoding multi-user coordination rules | **No change** | A demonstrated gap in a named existing surface |
| MAM-RUN1 | Running MAMUBench locally or against hosted models | **Not adopted** | Separate scoped evaluation with its own model-key, isolation and cost authority; README itself requires API keys + optional Modal |
| MAM-RULE1 | "One coordinator always beats a team" as an operating rule | **Rejected** | The paper explicitly conditions this on environment and feasibility; it is a finding, not an invariant |

## Evidence vs Inference

- **Verified:** every figure cited above (Figures 2–5); environment/scenario counts; license; runnable harness structure; model list (Claude Opus 5, Sonnet 5, GPT-5.6-sol, GPT-5.6-terra, Qwen3.8-max).
- **Verified as self-report:** all numerical results are the authors' own measured benchmark; no independent reproduction was run (MAMUBench itself is not executed here). The 47–67% in-context range spans all 25 scenarios and models; Figure 4's Claude-only values span 47.1–65.0, so the figure alone does not account for the upper bound. The gluten-free order is one illustrative scenario.
- **Inference (mine):** contract-map dispositions; the "no local gap" verdict; the MAM-DOC2 deferral.
- **Unknown:** whether the fourth (merge-queue) environment's results differ when run at scale; whether the guard's failure-recovery figure holds under other models or real (non-simulated) DoorDash integrations.

## Falsifiability, Risks, and Handoff

- The benchmark's headline numbers are measured, but they are **model- and environment-specific**; the digest's "一個 Agent 單獨協調結果更好" is a finding about these four simulated setups, not a universal claim.
- The X post's privacy/permission/audit framing is the commentator's own; it accurately paraphrases the paper's discussion but is not a primary source.
- MAMUBench is real, MIT-licensed, and runnable — but running it requires model API keys and a Modal or local backend; that is a separate gated step, not authorized by this record.
- Delivered scope: this record, the external-adoption catalogue, and regenerated `index.json`. No prompt-body, Skill, routing, governance, or runtime changes.
