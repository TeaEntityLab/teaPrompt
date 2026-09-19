# Jev Architecture-Analysis Synthesis Survey — pasted thread by Roy Chen (@RoyChenBuild), 2026-09-18 (2026-09-19)

> **Status: decided — record-only; no installed change, no wording adopted.** The object is a pasted architecture-forensics thread asking what kind of pretrained model sits behind a decisions-instead-of-text API: a bidirectional encoder, or a causal decoder run without its generation loop. It cites twelve sources — vendor docs, an independent 10,000-call probe study, two independent open reimplementations, two arXiv precedents, and canonical papers. Every load-bearing attribution was read against its cited source on 2026-09-19 and **held** — the fourth pasted-synthesis survey and the first whose citations all survive their page reads (contrast: the 2026-09-16 graph-engineering synthesis, where four of four vendor attributions failed). One citation drifted without breaking: the direct-scoring reimplementation renamed itself the day after the probe essay published (old URL redirects; identity pinned below). The thread's epistemics — hypotheses held open under stated underdetermination, feasibility distinguished from identity, negative probes scoped to exactly what they exclude — are the discipline TeaPrompt's research and review skills already install, so no sentence is needed. Clean-room throughout; surveyed vocabulary is guarded out of installed surfaces.

## Research Question

User instruction: "survey" over a pasted thread (dated 2026-09-18, read 2026-09-19). Two questions: (1) do the thread's claims hold against its cited sources; (2) does any concept expose a verified gap on an installed TeaPrompt surface. A bare "survey" carries no adoption direction; the standing bar applied per candidate.

## Direct Recommendation (as of 2026-09-19)

- **Study: yes — as a model of the genre done right.** The thread makes an identification argument entirely out of bounded claims: every hypothesis is labeled a hypothesis, every feasibility demonstration is labeled "not evidence of a particular implementation", every negative probe is scoped ("rules out an unchanged public tokenizer, not a public base model"), and the closing preference names what evidence would settle it. The probe essay beneath it practices the same discipline at larger scale.
- **Reproduce: not applicable.** Nothing to run; the cited probe study publishes its request/response records, not a tool.
- **Adopt: nothing.** Every epistemic move the thread makes is an instance of rules already installed (Evidence vs Inference, verdict bounded by the check performed, identity-vs-behavior separation, tracking points for what would change a conclusion). The architectural content is runtime territory TeaPrompt does not own.
- **For citers:** the direct-scoring reimplementation the thread calls by its old name renamed itself **the day after the essay** (2026-09-18); the old GitHub URL redirects. Its README states "formerly" the old name and disclaims affiliation.

## Method

Coordinator reads (2026-09-19), no scouts, no panel: the pasted thread; the probe essay in full text (published 2026-09-17; ~10,000 API calls across 1,029 instrumented probes plus follow-up studies of 146/311/445/192/148/181/105/35 requests, per its own experiment note); the direct-scoring reimplementation's repository (README, file tree, pinned HEAD `b9cb32537e78`, 2026-09-18T15:33:38Z, MIT, 1,607 stars); the classification-head reimplementation's model card **and raw `config.json`** (MIT, base Qwen3.5-4B); the vendor docs index plus the confidence page and the training-overview page; the Qwen3.5-4B model card; two arXiv abstracts (2404.05961 decoder-to-bidirectional-encoder adaptation; 2402.05099 shared-prefix attention with tree-shaped sharing). Canonical references (BERT, Transformer, the HF sequence-classification Llama variant, sparsely-gated MoE) were not re-fetched; the thread's characterizations of them are standard and nothing load-bearing turns on their exact text.

**Scope / acceptance:** verify every load-bearing attribution against its cited page; map the concept set against installed surfaces; decide every candidate with evidence and a trigger; land nothing without a verified gap; keep the clean-room boundary; run `make all` from the repository root.

## What the Artifact Is

A thread (~1,600 words) arguing that two architectures could sit behind a typed-decision API — a bidirectional encoder (jointly encode state + question + candidates, score candidates; runtime-defined labels require interpreting descriptions, not fixed output neurons) and a causal decoder with the generation loop removed (a decision position under causal attention reads the whole prefix; a head maps its representation to candidate probabilities; serialization happens in application code). It weighs them with: the vendor's own statement that its training method is a post-training path from pretrained language models; an independent probe study favoring a causal transformer (shared-state computation, isolated question branches, direct probability readout, a mixture-of-experts suspicion the author himself marks least certain) while acknowledging its experiments cannot distinguish the two masks; a decoder-to-encoder adaptation paper showing ancestry and final architecture are separable claims; two independent reimplementations proving the causal path is technically ordinary (one reads designated answer-token logits off frozen weights in one forward pass with shared prefill and parallel branches; one trains a three-class NLI head with last-token pooling — config architecture string verified from its raw `config.json`); and a shared-prefix serving paper as engineering precedent for why causal attention makes state reuse attractive. It closes with a stated preference (causal decoder), the reasons, and the disclosure that would settle it — while noting a base checkpoint would need still more evidence, and that calibration is independent of either architecture.

Claim-check outcome: **all held.** Notables — the vendor's confidence field is documented exactly as the thread says ("a statistic computed from the probability distribution the answer already gives you"); the probe essay's underdetermination sentence exists verbatim in kind ("The experiments can't tell a causal decoder from a bidirectional encoder… I assume a causal decoder anyway, for good reason"); its tokenizer result is exactly as scoped (no match among 192 public tokenizers over 415 probes, closest public match agreeing 348/415, "rules out an unchanged public tokenizer, not a public base model"); the Qwen3.5-4B card states "Causal Language Model" with a hybrid Gated-DeltaNet-plus-attention layout; the sequence-classification config names `Qwen3_5ForSequenceClassification` with contradiction/entailment/neutral labels. One sub-detail was not independently verified: that the direct scorer's designated answer tokens are specifically uppercase (its README says "native option logits"; the method doc was not fetched).

## Concept Map

Tier is `prose` throughout — the artifact is an analysis thread; the concepts are epistemic moves.

| ID | Concept (clean-room) | TeaPrompt coverage | Disposition |
| --- | --- | --- | --- |
| C1 | Competing mechanism hypotheses held open under stated underdetermination; preference stated with reasons, not promoted to fact | `reflective-research` Evidence vs Inference split; perspective expansion names competing positions and the blind spot | No change |
| C2 | A reconstruction compatible with observed behavior is an explanation, not a recovered specification | `[INFERENCE]` labeling; "`verified` covers only what was actually checked" | No change |
| C3 | Ancestry and current architecture are separable claims (a decoder-born model can operate as a bidirectional encoder) | External Adoption Checks: record divergent identities separately; do not infer behavior from identity alone — the same separation, run in either direction | No change |
| C4 | Feasibility demonstrations are not identity evidence (open reimplementations prove the path is ordinary, not that the vendor took it) | Same verdict-scope family; the 2026-09-16 verdict-scope rule: a conclusion is bounded by the check performed | No change |
| C5 | A negative probe excludes exactly what it tested: no-match against public tokenizers rules out an *unchanged* public tokenizer, not a modified public base | Verdict-scope precedent ("not substantiated by the inspected sources" ≠ "refuted") | No change |
| C6 | Observable-bounded inference: latency does not reveal hardware or active parameters; a billing token count does not reveal whether text was generated | "A verdict is bounded by the check performed"; research skill's second-method rule for load-bearing counts | No change |
| C7 | Calibration is independent of architecture; probability outputs alone do not establish it | Decision-model survey DM-6 (calibration is a training/eval property); "evidence over confidence" | No change |
| C8 | Name what would settle it: the disclosure (attention pattern, training history) that would decide between hypotheses; a checkpoint claim needs still more | High-Volatility Facts: every volatile claim carries a tracking point — the concrete event that would change it | No change |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| JA-1 | Hypothesis-discipline sentence for `reflective-research` (hold competing mechanisms open; state the preference and its reasons separately) | No change 2026-09-19 | C1/C2 rows: the Evidence vs Inference split plus perspective expansion already require exactly this | Reopen only if a research record is found promoting a preferred hypothesis to fact |
| JA-2 | Ancestry-vs-current-state rule (provenance and present behavior are separate ledger claims) | No change 2026-09-19 | C3 row: External Adoption Checks already separate identity records from behavior inference | None |
| JA-3 | Feasibility-is-not-identity sentence | No change 2026-09-19 | C4 row: verdict-scope family | None |
| JA-4 | Negative-probe scoping sentence (a no-match excludes the unchanged hypothesis only) | No change 2026-09-19 | C5/C6 rows: the 2026-09-16 verdict-scope rule states the general form | None |
| JA-5 | Calibration-independence note | No change 2026-09-19 | C7 row: DM-6 already rejected prompt-level calibration; independence follows | None |
| JA-6 | Tracking-point discipline (name the evidence that would settle the open question) | No change 2026-09-19 | C8 row: High-Volatility Facts installs it | None |
| JA-7 | Cross-record evidence note: open local scorers now exist that expose real candidate scores (one reads answer-token logits off frozen weights; one ships trained heads) — the class of structural signal DM-5's reopen trigger names | Noted 2026-09-19 (record-only) | DM-5's trigger requires such scores exposed *to a TeaPrompt-run step*; TeaPrompt skills run on chat-completion harnesses and no host integrates one. Tool existence is not host integration; the trigger stays unfired, the evidence is now dated | DM-5 reopens per its own row if a host integrates such a scorer |
| JA-8 | Genre finding: fourth pasted-synthesis survey; first whose attributions all held | Noted 2026-09-19 (record-only) | The GE-1 intake rule (a summary's citation is the summary's claim until the page is read) is what this survey executed — and here the pages agreed. The rule's value is symmetric: it documents held attributions as cheaply as failed ones. GE-1 stays held (reserved wording; no user direction names it) | GE-1 lands per its own gate on user direction |
| JA-9 | Citation-drift note: the direct-scoring reimplementation renamed itself the day after the probe essay published; the cited URL redirects | Noted 2026-09-19 (record-only) | Identity pinned at HEAD `b9cb32537e78` with the rename in its README; the thread's claim checked against the renamed repository's committed artifacts | None — dated-identity discipline already installed |

Deterministic guard: `plans/tests/test_jev_architecture_survey_record.py` (identity, dispositions, held-claim pins, clean-room boundary, index links).

## Shared Findings

1. **The genre's failure mode is absent here, and the same intake discipline detects both outcomes.** On 2026-09-16 a pasted synthesis cited four real pages that said other things; today's thread cites twelve sources that say exactly what it claims. Reading the cited page settles both cases at the same cost — evidence for the GE-1 rule's symmetric value, not for relaxing it.
2. **The probe essay is a working example of observable-bounded forensics.** Its strongest moves are refusals: a billing figure "tells us nothing about whether Jev generates text"; matrix-plus-softmax "does not establish a separately named classifier module"; sparse experts "can't be observed from outside." This is the verdict-scope rule executed against a black box, at 10,000-call scale.
3. **The vendor's confidence docs and TeaPrompt's dispatch pattern converge independently.** The vendor documents a three-band act/confirm/route-to-human pattern with risk-scaled thresholds; `workflow-recipes.md`'s Confidence row and `reflective-dispatch`'s low-confidence escalation encode the same shape at prompt level. Convergence noted as corroboration, not adoption material — the pattern was already installed.
4. **The reimplementation ecosystem around the decision-API pattern is now three deep and one renamed.** A logit-scoring inference interface over stock instruction weights (the 2026-09-18 decision-model survey), a frozen-weights direct scorer with published fixtures and claim-bounded benchmarks, and a trained NLI-head cross-encoder. The second's benchmark hygiene — committed fixtures, pinned revisions, prompt hashes, a "systems comparison, not semantic equivalence" caveat, and an explicit "we did not run a live endpoint" line — is the same reporting discipline TeaPrompt's records require.
5. **The vendor docs identify no checkpoint, as the thread says** — and its primitives have grown past the launch framing (three question types with structured criteria, a confidence field derived from the distribution, an explicit uncertain-goes-to-human cookbook). Dated 2026-09-19; the docs are the tracking point.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Thread attributions to the probe essay (call count, causal+MoE proposal, cannot-distinguish acknowledgment, tokenizer scoping, latency limits) | Observed — held | Essay full text read 2026-09-19 (published 2026-09-17) |
| Thread attributions to vendor docs (typed results + probabilities; post-training path from pretrained LMs; confidence from the answer distribution; runtime-defined questions; no checkpoint identified) | Observed — held | Docs index + confidence page + training-overview page read 2026-09-19 |
| Direct-scoring reimplementation mechanics (frozen weights, one forward pass, option logits, no sampling, shared prefill + parallel branches) | Observed — held | Repository README at HEAD `b9cb32537e78`, read 2026-09-19; "uppercase" answer-token sub-detail not independently verified (method doc not fetched) |
| Classification-head reimplementation config (`Qwen3_5ForSequenceClassification`, 3 NLI labels, last-token pooling) | Observed — held | Model card + raw `config.json` fetched 2026-09-19 |
| Qwen3.5-4B is a causal LM with hybrid Gated-DeltaNet/attention layout | Observed — held | Model card read 2026-09-19 |
| Decoder-to-encoder adaptation and shared-prefix precedents say what the thread claims | Observed — held | arXiv abstracts 2404.05961, 2402.05099 fetched 2026-09-19 (tree-shaped sharing verbatim in the latter) |
| BERT / Transformer / HF Llama-classification / sparse-MoE characterizations | Standard references — not re-fetched | Canonical; nothing load-bearing turns on exact text |
| The probe study's own numbers (probe counts, benchmark records, MMLU-Pro figure) | Author-claimed | Essay self-report; its raw records are linked but were not audited |
| Which architecture Jev actually uses | Unknown — correctly so | The thread's own conclusion; underdetermined by all inspected evidence |

## Evidence Actually Checked

- Probe essay full text (445 converted lines) — 2026-09-19.
- Direct-scoring reimplementation: README, file tree, HEAD pin via commits API — 2026-09-19.
- Classification-head reimplementation: HF card + raw `config.json` — 2026-09-19.
- Vendor docs: `llms.txt` index, confidence page, training-overview page — 2026-09-19.
- Qwen3.5-4B HF card; arXiv abstracts 2404.05961 and 2402.05099 — 2026-09-19.
- Installed-surface greps for the surveyed vocabulary and for the covered-concept citations — 2026-09-19.
- Not fetched: the thread's original post on X (pasted text taken as the artifact); the probe study's raw JSON records; the direct scorer's method doc; canonical papers.

## Falsifiability

- The "all held" verdict is bounded by the pages inspected; it is wrong if the thread's X-post links differ from the pages fetched here, or if the one unverified sub-detail (uppercase answer tokens) is wrong in a way that matters to a citer.
- The "no sentence needed" mapping is wrong if an installed skill is later shown to lack a rule the Concept Map credits to it (coverage rows name the surfaces; re-grep them).
- JA-7's non-fire is wrong if a TeaPrompt-run host in fact integrates a local scorer today; that would fire DM-5's own trigger, not a new one.
- Finding 3's convergence claim is wrong if the vendor's confidence-band pattern postdates and derives from common ancestry with TeaPrompt's sources — nothing checked establishes independence beyond the absence of citation.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| All twelve cited source classes checked or tiered; identities pinned | done | this record |
| Thread claim-check: all load-bearing attributions held; one sub-detail flagged unverified | done | What the Artifact Is; Evidence vs Inference |
| Eight concepts mapped; nine candidates decided with evidence and triggers | done | Concept Map; Candidate Adoption Ledger |
| Clean-room boundary on installed surfaces | done | guard vocabulary test |
| Guard written | done | `plans/tests/test_jev_architecture_survey_record.py` |
| Decision Index row (at head), case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`; `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |
