# Tev-Gym / Tev Source Survey — 2026-10-16

Language: English

> **Status:** Survey completed 2026-10-16: project page, arXiv v1 paper, and both Hugging Face model cards inspected. No executable Tev-Gym code/data release was located in the checked project links or public `tev-agent` organization inventory; no training or benchmark execution was performed here. Reference-only: this record adopts nothing and authorizes no skill, runtime, or campaign change.

## Research Question

What exactly does Tev (tev-agent.github.io, arXiv 2610.18868) claim and demonstrate, which of those claims are checkable against the supplied artifacts, and does any claim create or close a structural gap in TeaPrompt's existing verification, oracle-separation, and measurement discipline?

## Direct Recommendation

Record-only. The paper describes latent-world-first synthesis that builds the answer key *before* the task, plus a dense progress-potential reward (PPRS, λ=0.25) intended to address GRPO group starvation on long-horizon tasks. Oracle protection, adversarial probes, and measurement disclosure overlap TeaPrompt's existing contract concerns; that correspondence does not establish an equivalent latent-world generator, disjoint code closures, reward mechanism, or enforced isolation. Every candidate below is `noted` or `deferred`; none fires an adoption gate. Reopen only on a reproduced local structural gap, not on the paper's existence.

## Version / Date Context

- All sources checked 2026-10-16.
- Paper: arXiv:2610.18868v1 [cs.CL] (also cs.AI, cs.CV, cs.LG), submitted 2026-10-13. Version v1 is the only version as of the check; a v2 would be a new identity, not a delta of this record.
- Project page https://tev-agent.github.io/ (accessed 2026-10-16): states "Code soon / Data soon — under internal approval, will release in 7 days". The page carries no date for that statement; the tracking point is a public repository appearing under the GitHub org.
- GitHub org `tev-agent` (accessed 2026-10-16): the public org page and `GET https://api.github.com/orgs/tev-agent/repos` both list one public repository, `tev-agent/tev-agent.github.io` (the project page, updated 2026-10-15). The known-present page repository is the discovery control. No code/data repository was located in this checked inventory or the project page's release links; this is not an all-GitHub absence claim.
- Model weights are already public: `gordonhu/Tev-27B` and `gordonhu/Tev-320B` on Hugging Face (both accessed 2026-10-16), each under CC BY-NC-4.0. Both cards carry the notice: "The model weights held in this repo are a reproduced version, not official model weights trained at Adobe." Identity divergence between the paper's Adobe-trained models and the published weights is therefore declared by the authors, not inferred here.

## Evidence Used

Official/upstream (all checked 2026-10-16):

- Project page https://tev-agent.github.io/ (accessed 2026-10-16) — headline numbers, teaser, ablation table, qualitative trace, BibTeX.
- Paper PDF https://arxiv.org/pdf/2610.18868v1 (accessed 2026-10-16) — version-pinned text including appendices A–D (task taxonomy, gates, statistics, decontamination, worked environments, reward details, training recipe, evaluation protocol).
- Abstract page https://arxiv.org/abs/2610.18868v1 (accessed 2026-10-16) — publication date and category identity.
- Model card https://huggingface.co/gordonhu/Tev-27B (accessed 2026-10-16) — license, base model, weights caveat, training hyperparameters, evaluation tables, vLLM serve recipe, sandbox warning.
- Model card https://huggingface.co/gordonhu/Tev-320B (accessed 2026-10-16) — license, base model (GLM-5.3-Flash, 320B total / 18B active MoE), weights caveat, per-category TB tables, the P@5-stagnation caveat.
- GitHub org page https://github.com/tev-agent and API https://api.github.com/orgs/tev-agent/repos (accessed 2026-10-16) — public repository inventory (one repo: the project page).

Supplemental:

- Paper references actually read only as citations: I. Rana / M. Ivanov "Anchor" (arXiv 2605.26321, artifact drift), Y. Wang "The dark room in the reward channel" (arXiv 2607.21273), Ng et al. 1999 (PBRS). Quoted as the paper's citations; not independently fetched.

## What Tev Is

**Latent-world-first synthesis.** A seeded generator program — written once by coding agents and reviewed by the authors, then model-free — constructs a complete, correct hidden *latent world* W (domain state, workflow, expected state after every step). The workflow is compiled by code into a DAG whose critical path sets the horizon; W is rendered into the agent-facing input tree with a round-trip assertion; declared, invertible corruptions (schema drift, duplicates/nulls, category drift, scrambled shard indices, stale caches) produce the task tree s₀. One environment is the quadruple E = (x, s₀, ver_W, Φ_W): prompt, corrupted inputs, strict pass/fail verifier, progress potential — all functions of the same W. The paper's stated purpose of the single anchor is preventing *artifact drift*: separately generated task, inputs, and verifier that each look valid but describe different problems. A sealed hidden suite (metamorphic transforms that must not change the grade; stale-output counterfactuals that must fail) is used only at verification time.

**Admission gates.** Eight benchmark-independent gates, each matched to a named failure class (paper Table 7): reward causality, exploit resistance (14 gaming probes — empty output, minimal schema-valid output, copied input, hard-coding, path traversal, private lookup, and others — must all score 0 under both verifier and progress scorer), role independence (reference solver, alternative solver, strict verifier, progress scorer have disjoint, audited code closures; none imports another), solver agreement (π^ref and π^alt produce identical output trees on every seed; disagreement rejects the environment), progress validity (0 < Φ < 1 on partial states, monotone to 1, negative increments on regression), metamorphic invariance, six-seed diversity, public-contract hygiene (no private authority or verifier code in the prompt or public tree).

**PPRS.** Progress contract: nodes V from the workflow DAG, weights w_v > 0 summing to 1, prerequisite sets; partial scorer c_v(s) ∈ [0,1] graded directly against W; credit is prerequisite-gated (c̃_v is the minimum over v and its prerequisites); Φ(s) = Σ_v w_v c̃_v(s) ∈ [0,1]. Rollout reward R(τ) = 1[pass] + λ·Φ(s_T) (telescoped from per-step increments), λ = 0.25 fixed in every run and never tuned, applied with per-turn credit (turn t gets λr_t; final turn additionally the terminal term), return-to-go γ = 1, per-turn-index group baseline. The paper is explicit that this is **not** policy-invariant shaping in the Ng et al. (1999) sense: zeroing the terminal potential would reinstate the starvation it exists to fix. What is preserved is ranking — a passing rollout earns 1 + λ > any failing rollout's λ — plus anchoring (Φ = 1 exactly when the verifier accepts). The stochastic-policy preference reversal is bounded and disclosed: the shaped objective can prefer the less successful policy only if p₂ − p₁ < λ(1−p₁)/(1+λ) ≤ λ/(1+λ) = 0.2, and only when its failures end near-complete.

**The starvation it repairs.** Under GRPO, a group of G rollouts where all fail has zero advantage everywhere; wasted fraction (1−p)^G = 66% at p=0.05, G=8; 92% at p=0.01; still 44% at p=0.05, G=16. Measured probe: 24 groups × G=8 rollouts on 12 seeds of one environment, graded after every turn — terminal reward is 0 on all 192 rollouts (every group zero-advantage), while Φ separates them onto prerequisite-gated plateaus (0.05, 0.26, 0.69, 0.78, 0.90, 1.0). The paper also cites Wang (2026): dense prediction rewards that are *not* aligned with the task collapse GRPO-trained agents — "the channel, not the content, decides what works" — and argues Φ is safe only because it is exact progress toward the ground-truth world.

## State Ledger

All rows checked 2026-10-16 against the sources above. Survey-specific candidates use the TEV- prefix. `verified` on an upstream claim means its existence and quoted number/text match the inspected source, not that the experiment, code independence, or efficacy was independently verified. Attribution/process and extrapolation limits remain in the final column; the upstream paper, site, and cards are one author-controlled evidence channel.

| Claim / Item | Status | Evidence and method | Limits |
|---|---|---|---|
| Paper exists, v1, 2026-10-13, six authors, Adobe Research + UCLA | `verified` | arXiv abs page + PDF header | Author affiliation split read from PDF (¹Adobe, ²UCLA) |
| 1,170 environments, 7 domains; Math & Science 264 / ML 242 / Coding & System 664 | `verified` | Paper Table 8 + abstract | Author-reported composition; corpus not yet released |
| Latent-world-first pipeline: seeded generator, code-compiled DAG, round-trip rendering, declared invertible corruption, sealed hidden suite | `verified` | Paper §2.1 + Figure 3 walkthrough | Static description; no generator code to run |
| 8 qualification gates incl. 14 gaming probes at 0, disjoint grader closures, π^ref/π^alt agreement | `verified` | Paper §2.2, Table 7, Appendix A.6 | Probes are generator-authored and author-reviewed; no third-party adversarial red-team of Φ is reported |
| PPRS definition, λ=0.25 fixed/untuned, per-turn credit, passing-rollout ranking preserved, stochastic-policy success-probability gap bound 0.2 | `verified` (source text) | Paper §3.3, Appendix B | Conditional bound under the stated reward assumptions, not general policy invariance; no training replication performed here |
| Starvation numbers: (1−p)^G = 66% / 92% / 44% at the stated (p, G) | `verified` | Paper §3.1 + Appendix B; arithmetic consistent with the formula | Applies to GRPO-style group normalization, stated for that estimator |
| 24-group / 192-rollout Φ probe: terminal reward 0 on all, Φ plateaus separate rollouts | `verified` | Paper Appendix B ("Measured groups") | One environment family (warehouse), one harness; author-run |
| Corpus stats: median 6 stages (3–12), 8 progress nodes, 6 reward components, 2 corruptions (1–7), 12 input files (≤501), 51 KB (≤6.1 MB), 23 wire formats, 583-token median prompt; balance 0.89 / 0.91 | `verified` | Paper Appendix A.7 | Medians/maxima over the unreleased corpus |
| Difficulty: base Qwen3.8-27B single-rollout P@1 3.2%; Gemini 3.6 Flash P@1 29% / P@8 40% on a fixed 92-env subsample; agent time median 12.4 min (mean 14.8) vs 0.5–2.0 min prior corpora | `verified` | Paper Table 1, A.7, A.8 | "Agent time" is wall-clock of one evaluator, not human effort; Terminal-Universe has no released environments and cannot be timed |
| Ablations (9B): full method S@1 0.29 @ 9.0 GPU-h/step; public-view verifier 0.24 @ 22.3 (discards 88% of groups); prompt-first 0.23 @ 11.8; sparse terminal 0.25 @ 16.7 (no gain over base 0.25); PPRS pooled-norm 0.28 @ 10.9; direct additive Φ 0.29 @ 9.7 but P@5 stays 0.06 | `verified` | Paper Table 5 | 9B only, one configuration; λ not tuned; ablations are author-run |
| Tev-27B: ALE-CM P@5 0.17→0.28 (+65%), S@1 0.33→0.40; matches GPT-6 Astra and Claude Opus 5 at P@5; closes >2/3 of gap to Fable 5 (0.33); beats Qwen3.8-2.4T-A95B on P@1 | `verified` | Paper Table 2 + model card | Open models run in the training harness; frontier models in native harnesses ("most favorable to them") |
| Zero-shot TB: Tev-27B 3.0-CM 0.09→0.14 (+56%), 4.0-CM 0.04→0.10 (2.5×); TB 2.1 0.764→0.794 (Opus 4.8: 0.789) | `verified` | Paper Tables 3–4 | Subsets are 22/18 tasks selected by Claude judging + CPU-harness runnability |
| Tev-320B (GLM-5.3-Flash base): 3.0-CM 0.20→0.27 (+35%), 4.0-CM 0.29→0.37 (+28%); TB 3.0 security 0.22→0.45; trails only Opus 5 / Fable 5 / GPT-5.6 (sol) on 4.0-CM; P@5 gains +0.05 / 0 → "training mainly makes the model solve the tasks it can already reach more reliably" | `verified` | Paper §4.2, Table 3; Tev-320B card | Self-evaluated, explicitly not official-leaderboard; P@5 stagnation is the authors' own caveat |
| Decontamination: zero 13-gram/8-gram sharing between all 1,170 prompts and ALE-CM / TB 3.0 / 4.0 / 2.1; NN Jaccard median 0.13 (TB) / 0.22 (ALE) vs 0.24–0.28 same-benchmark calibration | `verified` | Paper Appendix A.9, Table 10 | Lexical measure only; no semantic-overlap analysis |
| Both HF model cards state the weights are a reproduction, "not official model weights trained at Adobe" | `verified` | Both model cards, Notice section | Whether the published weights reproduce the paper's tables is not demonstrated anywhere in the supplied artifacts |
| No executable code/data release located in the checked upstream surfaces; site promises release "in 7 days" (undated) | `verified` (scoped inventory) | GitHub org page and API both list the known-present project-page repository; site has Code/Data-soon badges, not release links | Tracking point: a release link or new public org repository; other organizations, private repositories and mirrors were not inventoried |
| AI use: coding agents authored generators (specs, reference solvers, verifiers, progress scorers); authors reviewed each; generation/verification/reward are model-free afterward; Claude judged TB "CM" subset membership | `verified` | Paper AI Use Statement + Appendix C.2 | Model-assisted authoring of the graders whose independence the gates assert |
| Existing TeaPrompt contracts address related oracle, adversarial-probe and measurement concerns | `verified` (contract text only) | [reflective-research](../skills/reflective-research/SKILL.md#external-adoption-checks); [intent-compression lesson](../PROJECT_KNOWLEDGE.md#lesson-intent-lives-with-humans-every-downstream-artifact-is-a-lossy-compression-read-by-an-optimizer); [four-way failure classification](../skills/verification-map-generator/SKILL.md#failure-classification-canonical-table-copy-into-verifymd); [governed-delivery oracle split](../skills/governed-delivery/SKILL.md#module-contract) | These are methodology contracts, not an implemented Tev generator, disjoint-code audit, training system, or host-isolation proof |

## Evidence vs Inference

**Observed:** the method, gates, formulas, statistics, tables, disclosures, licenses, weight-provenance notices, and release status above — each read directly from the project page, the paper PDF (including appendices), the two model cards, and the GitHub org page.

**Author-reported (verified as claims, not as results):** every experimental number — training gains, ablation GPU-hours, decontamination counts, balance scores, agent-time medians. No runnable corpus or generator release was located in the checked upstream surfaces; no Tev code, weights, training or evaluation was executed here. The model cards' "reproduced version" notice means the published weights are not identified as the paper's original training outputs; their result equivalence remains unverified.

**[INFERENCE]:** (1) The eight gates are designed to make Φ harder to game than an LLM-written or test-fraction grader, but the probes are authored by the same pipeline as Φ; the paper reports no independent red-team of the progress scorer, so this survey cannot establish exploit resistance. (2) The public-view-verifier ablation (LLM writes the verifier from the agent's view: no S@1 gain, 22.3 GPU-h, 88% of groups discarded) supports the authors' concern under that configuration; it does not prove that every public-view grader is incapable of certification. It is a conceptual correspondence, not evidence for TeaPrompt's spec/oracle-error class. (3) No reproduced TeaPrompt structural gap follows from this source review; the mappings below concern recorded contract text, not equivalent operational mechanisms.

## Candidate Adoption Ledger

Bare survey (no adoption direction): only this survey's own candidates can fire; a survey never adopts. Dispositions: `noted` (recorded correspondence, no action) / `deferred` (adjacent, held with trigger).

| Candidate | Tev mechanism | TeaPrompt surface today | Disposition | Trigger to reopen |
|---|---|---|---|---|
| TEV-1 | Answer key before task (latent world anchors prompt, inputs, verifier, and progress scorer) | Related oracle-before-implementation and sealed-manifest contracts in `governed-delivery`; locked acceptance spec in `verification-map-generator`. Neither constructs Tev's latent world | `noted` — conceptual correspondence, not implementation equivalence | A local case where an oracle was authored after the implementation and the drift was caught only downstream |
| TEV-2 | Artifact drift: separately generated task/verifier/inputs that each look valid but describe different problems | Spec-version `stale` propagation; pstack four-way classification (product regression / doc-map drift / spec-oracle error) | `noted` | A spec/oracle disagreement misclassified as a product regression in a TeaPrompt-owned check |
| TEV-3 | 14 gaming probes must score 0 before admission; metamorphic + stale-counterfactual suite | `reflective-research` External Adoption Checks: self-tests/CI are evidence only for their tested assertions; safety needs adversarial boundary probes | `noted` | A TeaPrompt verifier whose only adversarial evidence is its own author's probes |
| TEV-4 | Role independence: solver/verifier/progress-scorer in disjoint code closures | Owner/oracle separation and decorrelated-verification contracts in `governed-delivery`; no equivalent disjoint-code-closure audit established here | `noted` — related concern, distinct guarantee | A graded artifact whose producer and grader share code in a way that causes a reproduced correlated error |
| TEV-5 | Per-turn credit + per-turn-index baseline instead of pooled normalization | No equivalent reward/advantage surface. `acceptance-join-validator` statically resolves REQ/AC IDs to runnable checks; it neither executes them nor assigns credit or aggregates scores | `deferred` — RL-specific, not an acceptance-join wording gap | An explicitly authorized rollout-grading/training surface with a reproduced credit-assignment or normalization defect |
| TEV-6 | Dense exact-progress reward for long-horizon training | No TeaPrompt-owned RL/training surface exists | `deferred` | TeaPrompt gains a model-training or rollout-grading runtime |
| TEV-7 | Declared deviation from policy invariance with a bound (≤ λ/(1+λ) = 0.2) and a control arm (sparse arm trained on the same tasks) | Measurement discipline in `golden-benchmark-runner` and `arm-blinded-eval-harness` (RTH-1, adopted 2026-10-07 preventively) | `noted` — same disclosure shape, different domain | A TeaPrompt comparison whose methodology change lacks both a bound and a control |
| TEV-8 | Model-card provenance notice: "reproduced version, not official weights" | Pin-the-checked-artifact rule: claims scoped to the exact revision/digest checked | `noted` | A TeaPrompt record citing an artifact whose identity (tag vs digest vs reproduction) is unpinned |

Recommended Core Additions: none.

## Classification Summary

- Related Contract Coverage: TEV-1/2/3/4/7/8 address concerns already discussed by recorded surfaces; this is not evidence of equivalent implemented mechanisms. No new skill, pack, or runtime is justified by correspondence alone.
- Deferred / Domain-Specific: TEV-5 concerns RL credit assignment and normalization, not static acceptance joins. No local acceptance-join gap is established.
- Not Applicable to Current Scope: TEV-6 — TeaPrompt operates no model-training runtime.

## Falsifiability

This survey's coverage mapping is invalid if a mapped surface does not support the wording attributed to it; correct this survey rather than presuming the cited record is wrong. A reproduced local oracle/consumer correlated-error failure may justify reopening TEV-3/TEV-4 under its actual scope and authority. A Tev code/data release enables a follow-up execution review of the declared gates; any observed disagreement between Φ and verifier acceptance would challenge those upstream claims, not automatically justify TeaPrompt adoption. Efficacy and published-weight equivalence remain unverified here until the relevant recipe, corpus, artifacts and evaluation are independently exercised.

## Handoff

Evidence sufficient to stop this source review: the cited mechanisms and numbers were checked against primary-source text, experimental outcomes remain attributed to the authors, and each candidate has an explicit disposition and trigger. Changes are limited to this survey and its navigation/index entries; no skill, operating contract, runtime or campaign change is adopted. If a code/data release link appears on the project page or a public repository appears under `github.com/tev-agent`, a follow-up delta survey can inspect the exact executable revision and exercise the declared gaming/Φ/verifier gates. Any future adoption would require that evidence plus a verified local gap, not this reading alone.
