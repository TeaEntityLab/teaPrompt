# GLiNER2 Survey — `fastino-ai/GLiNER2` @ `d7c727458bf6` + EMNLP 2025 Demos Paper (2026-09-19)

> **Status: decided — record-only; no installed change, no wording adopted.** The objects are a mature Apache-2.0 repository (created 2025-07-07, 2,004 stars, maintained by GLiNER's original author under the Fastino AI org) and its EMNLP 2025 System Demonstrations paper (2025.emnlp-demos.10, pp. 130–140, read in full): a schema-driven information-extraction stack where one ~200M bidirectional encoder scores entities, classifications, structured records, relations, and span attributes in a single forward pass, with runtime-defined labels supplied as prompt tokens. Two findings organize the record: this is a production existence proof for the encoder hypothesis the Jev-architecture survey held open — with a lineage that predates Jev, so it is feasibility evidence, not identity evidence, exactly as that record's own rule bounds it — and its constraint-decoded joint classification is the first system in the surveyed decision-interface ecosystem where cross-answer consistency is a decode-time contract rather than a caller's problem. A bare "survey" carries no adoption direction; per the installed direction-scope rule only this survey's own candidates could fire, and none met the bar.

## Research Question

User instruction: "survey https://github.com/fastino-ai/GLiNER2 https://aclanthology.org/2025.emnlp-demos.10.pdf". Three questions: (1) what the artifact pair is, at a pinned revision and a fixed publication; (2) how the 2025 paper and the 2026 repository relate — one identity or a drifted pair; (3) whether any concept exposes a verified gap on an installed TeaPrompt surface.

## Direct Recommendation (as of 2026-09-19)

- **Study: the constrained-classification tutorial and the paper as a genre pair.** The tutorial documents coupled typed decisions done right — declared invariants, feasible-assignment search, explicit infeasibility surfacing. The paper is a clean system-demonstrations specimen: architecture, honest baselines, and a disclosed evaluation hole.
- **Reproduce: not done.** Nothing executed, no clone; every number in this record is author-claimed at paper/docs tier.
- **Adopt: nothing.** Bare survey; ten concepts map to installed rules, host territory, or corroboration. The one genuinely novel pattern (joint feasibility over coupled verdicts) has an installed artifact-level analogue and no verified prompt-level local instance to repair; it is parked with a concrete reopen (G2-2).
- **For citers:** the paper's own load string (`gliner/gliner2-base`) resolves to no shipped checkpoint — the org is `fastino` and the current default is `gliner2.5-base-v1`; the repo has drifted far past the paper (three task types → five; one architecture → two behind an auto-dispatching loader; a commercial cloud API added). The HF card's license field was not directly fetched; the Apache-2.0 claim rests on the repository's root LICENSE, the README badge, and the paper's statement.

## Method

Coordinator reads (2026-09-19), no scouts, no panel: GitHub API (repo metadata, three latest commits, root tree at the pin — LICENSE 11,357 bytes at root); pin `d7c727458bf6929bc9ef5ee04e13c3f717a7c455` (2026-09-18, an eval-loss fix merged by the original GLiNER author), tree `ef6b491265e2c3bc0f2ae325739f4618dabb6547`; the ACL Anthology PDF in full including both appendices; the pinned `README.md` head (identity, architecture split, checkpoint family, docs map — 300 of 1,366 lines) and `tutorial/14-constrained_classification.md` (300 of 343 lines); HF API for `fastino/gliner2.5-base-v1` (sha `78cea040597df251eedefa9d7ee2a756af39fe64`, created 2026-08-18, modified two days before the survey, 34,615 downloads, 193,581,591 F32 params). Installed-surface coverage citations re-verified by grep this session.

**Scope / acceptance:** pin the revision; read the paper in full; map the concept set against installed surfaces; decide every candidate with evidence and a trigger; land nothing without a verified gap; keep the clean-room boundary; run `make all` from the repository root.

## What the Artifact Is

**The paper (2025 state).** One DeBERTa-lineage encoder (205M params, 2048-token context; its predecessor was 512-token, NER-only) handles three task families through a schema-in-the-prompt interface: the task prompt and input text share one sequence, with learned special tokens marking structures, entity types, fields, and labels. NER scores span representations against entity-type embeddings (sigmoid dot product); hierarchical extraction predicts an instance count with a 20-way classifier over a structure token, then conditions field embeddings on occurrence-ID embeddings; classification pools label-token embeddings through an MLP — softmax for single-label, sigmoid for multi-label. Multiple tasks compose into one forward pass over a shared encoded context. Training data: 254,334 examples (135,698 real-source from news, law, Wikipedia, PubMed, ArXiv; 118,636 synthetic), all annotated by GPT-4o "using task-specific prompts and validated for quality" — the validation is not further specified. Results as published: zero-shot classification average 0.72 across seven benchmarks — best of the open systems compared, below GPT-4o's 0.84; CrossNER zero-shot F1 0.590 vs GPT-4o's 0.599 and its own predecessor's 0.615 — the paper publishes losing to GLiNER-M on the NER average. CPU latency is flat in label count (130–208ms from 5 to 50 labels) where a cross-encoder that runs a separate forward pass per label scales linearly (1,714ms → 16,897ms); ~2.6× faster than the GPT-4o API on their setup. One capability ships unevaluated, and the paper says so: "Hierarchical structure extraction was not evaluated due to the absence of established zero-shot benchmarks for this task type, which we plan to address in future work."

**The repository (2026 state).** Far past the paper: five task types — the README tagline is "Schema-driven information extraction and classification — entities, labels, records, relations, and span attributes in one local model." — and two architectures behind one loader: the span-grid family (legacy, plus guardrail and PII fine-tunes) and the boundary family (GLiNER2.5: sparse start/end pairing, any span length, 74M–287M). `AutoExtractor.from_pretrained` resolves the family: "It dispatches by the saved `architecture` field." — and the span-only loader refuses boundary checkpoints rather than mis-loading them. Around the core: quantization/compile, LoRA with runtime adapter switching, long-document chunked APIs, configurable word splitters (runtime-only — checkpoints reload the default, with a quality warning when inference splitting diverges from training), a hosted cloud API with a torch-free client, and a commercial fine-tuning path. Safety fine-tunes (LLM-guardrails, a 42-type PII filter, a combined model) mark the deployment domain: local typed decisions for guardrails and compliance.

**Constrained classification (tutorial 14).** The standout against everything previously surveyed in the decision-interface ecosystem. A `Classifier` schema declares single/multi/ordinal tasks plus cross-task constraints in a small DSL — implication, equivalence, exclusion, conjunction/disjunction, exactly-one, cardinality bounds, ordinal level bounds, selection predicates. The encoder scores all tasks in one pass; a decoder then searches for the best globally consistent assignment (exhaustive within a node budget, default 200k; beam otherwise; an `auto` mode picks). Infeasibility is a surfaced outcome, not a crash or a silent fixup: `on_infeasible` chooses relax / minimum-violations / raise, and results carry a `feasible` flag with a violations list; referencing an undeclared task is a schema error. The tutorial's own framing: without the constraint decoder, independent argmax could pick `intent=delete` and `effects=["read_only"]` — "The constrained path forbids that." And: "Always inspect `result.feasible` in production if you keep the default."

Claim posture: paper and docs tier, self-consistent, with disclosed losses and a disclosed evaluation hole; `gliner2/` package source not audited — docs-to-code fidelity is an open slice, as it was for the MiniMax Code survey before its trace-map follow-up.

## Concept Map

Tier is `paper`/`docs` throughout — package source not audited.

| ID | Concept (clean-room) | TeaPrompt coverage | Disposition |
| --- | --- | --- | --- |
| C1 | Production bidirectional-encoder typed decisions: runtime-defined labels as prompt tokens over learned special tokens, logit readout, no generation loop | The Jev-architecture survey's encoder hypothesis (C3/C4 there): a decoder-free encoder interpreting label descriptions is exactly what it described; its own rule bounds this as feasibility, not identity — the lineage predates the vendor product | No change — cross-record corroboration (G2-1) |
| C2 | Schema packet: many tasks composed into one forward pass over a shared context | Decision-model survey's packet-amortization and programmatic-assembly coverage; serving is host territory | No change |
| C3 | All-labels-single-pass vs per-label-forward economics (flat vs linear latency in label count) | Same amortization class as shared-prefill scoring in the architecture survey | No change |
| C4 | Constraint-decoded joint assignment over coupled typed decisions, with explicit infeasibility semantics | The stance — coupled answers need a joint consistency check, not independent argmax — is installed at artifact level: cross-link tests, router/fixture/cheatsheet parity guards, governance validators are joint-consistency checks over coupled artifacts. The decode machinery is host territory. No local instance of a workflow emitting jointly infeasible coupled verdicts | No change — reopen parked (G2-2) |
| C5 | Single-teacher label provenance: one frontier model annotates the whole corpus; external human benchmarks carry the honest eval | Judge-lifecycle lesson ("a model verdict is not a second independent channel"); training practice is an ML non-goal; the contrast with code-computed labels plus ablation checks (Nimble) is recorded | No change |
| C6 | Capability shipped without a benchmark, disclosed in the paper | Verdict-scope family; "missing usage data is `unknown`, not zero demand" | No change — specimen |
| C7 | Losing results published: below its predecessor on NER average, below GPT-4o on classification | Reporting-hygiene corroboration, same class as the Nimble and Jev-diffusion records | No change |
| C8 | Fail-closed loader contract: dispatch by the checkpoint's saved architecture field; narrower loaders refuse foreign checkpoints; undeclared schema references are errors | Artifact-carried-contract family (Nimble C6); enforcement host-owned | No change — corroboration |
| C9 | Deployment domain: guardrails, PII, compliance taxonomies as the load-bearing use of local typed decisions | Context evidence for the decision-interface production trend; host territory | No change |
| C10 | Runtime-only vs checkpoint-carried configuration split, with a divergence warning | Config-provenance specimen; host territory | No change |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| G2-1 | Encoder-path existence-proof note for the decision-interface ecosystem: a shipped, pre-Jev, independent encoder family does typed decisions with runtime-defined labels — the architecture survey's held-open hypothesis has a production instance; not added to the Jev-reproduction substrate count (independent lineage, extraction-centric) | Noted 2026-09-19 (record-only) | C1 row; JA C4's feasibility-is-not-identity rule applied in the encoder direction | DM-5 reopens per its own row — a pip-installable local scorer is tool existence, not host integration |
| G2-2 | Joint-feasibility sentence for coupled workflow verdicts (coupled decisions need a joint feasibility check, not independent argmax) | No change 2026-09-19 | C4 row: the artifact-level analogue is installed (cross-link, parity, and governance validators); no verified local instance of a workflow emitting jointly infeasible verdicts on coupled questions | Reopen if a TeaPrompt workflow is observed emitting jointly infeasible verdicts on coupled questions (e.g., a route and a strictness level contradicting a declared rule) |
| G2-3 | Packet/amortization wording | No change 2026-09-19 | C2/C3 rows: covered | None |
| G2-4 | Shipped-without-benchmark disclosure sentence | No change 2026-09-19 | C6 row: verdict-scope family | None |
| G2-5 | Teacher-label provenance rule | No change 2026-09-19 | C5 row: judge-lifecycle lesson; training practice is a non-goal | None |
| G2-6 | Paper↔repo drift citer note: the paper's load string matches no shipped checkpoint; three tasks → five; one architecture → two; commercial API added | Noted 2026-09-19 (record-only) | dated-identity discipline; For-citers bullet | None |

Deterministic guard: `plans/tests/test_gliner2_survey_record.py` (identity and number pins, quote pins, dispositions, clean-room boundary, index links).

## Shared Findings

1. **The architecture survey's other hypothesis now has a production existence proof.** Runtime-defined labels interpreted as descriptions — not fixed output neurons — in a shipped bidirectional-encoder family whose lineage predates the vendor product it is now compared against. This strengthens "the encoder path is ordinary" precisely within the bound the Jev-architecture record set: feasibility demonstrations are not identity evidence. The surveyed ecosystem now spans both candidate architectures in production — encoders here, no-loop decoder derivatives on the Nimble side.
2. **Cross-answer consistency as a decode-time contract is new to the surveyed ecosystem.** Every Jev-like system recorded so far scores fields mutually blind and returns per-field confidences; here, declared invariants constrain the joint assignment, infeasibility is a surfaced result with named violations, and the docs instruct production callers to check the flag. TeaPrompt's parity and cross-link guards are the same stance applied to coupled artifacts; the prompt-level candidate stays parked on G2-2's concrete reopen.
3. **Disclosure hygiene keeps converging across the ecosystem.** Publishing a loss to your own predecessor (0.590 vs 0.615), a loss to the frontier API on every classification benchmark (0.72 vs 0.84), and an unevaluated shipped capability with the reason — the same reporting class the Nimble and Jev-diffusion surveys recorded. Three independent projects now practice it.
4. **Two label-provenance regimes now sit side by side in the ecosystem.** One frontier teacher annotating everything with unspecified validation (here) versus code-computed labels with per-example ablation checks and a human-labeled second instrument (Nimble). Both then lean on external human benchmarks for honest evaluation — the judge-lifecycle compression story, in production, twice.
5. **Dated identity applies to mature artifacts, not just day-old ones.** Fourteen months in, the paper and repository have drifted in org name, task count, architecture count, and business model; the paper's own quickstart string no longer resolves. A citer of either object alone gets a different system.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Repo identity, creation date, root LICENSE (11,357B), tree, latest commits | Observed | GitHub API, 2026-09-19 |
| Paper content: architecture, training mix (254,334; GPT-4o-annotated), results tables, disclosed evaluation hole | Observed (paper tier) | ACL Anthology PDF read in full, 2026-09-19 |
| Repo current state: two architectures, five task types, loader dispatch, constraint DSL, infeasibility semantics | Observed (docs tier) | Pinned README head + tutorial 14; package source not audited |
| Default checkpoint identity (sha, dates, downloads, 193,581,591 F32 params) | Observed (API) | HF API, 2026-09-19; card license field not fetched |
| All benchmark and latency numbers (0.590/0.615/0.599; 0.72/0.84; 130–208ms; 1,714→16,897ms; 6.8×; 2.6×) | Author-claimed | Paper; nothing reproduced |
| GPT-4o annotation "validated for quality" means an effective validation | Not verified | The paper does not specify the validation; treated as unknown |
| "First surveyed system with decode-time cross-answer constraints" | `[INFERENCE]` (count) | Bounded to the six prior decision-interface survey records |
| Encoder family predates the vendor product | Observed (publication record) | GLiNER lineage (NAACL 2024) per the paper's own references |

## Evidence Actually Checked

- GitHub API: repo metadata, three commits, root tree at `d7c727458bf6` — 2026-09-19.
- ACL Anthology PDF 2025.emnlp-demos.10 in full (421 converted lines, appendices A/B, references) — 2026-09-19.
- Raw at the pin: `README.md` lines 1–300 of 1,366; `tutorial/14-constrained_classification.md` lines 1–300 of 343 — 2026-09-19.
- HF API: `fastino/gliner2.5-base-v1` — 2026-09-19.
- Installed-surface greps for every coverage citation and the survey vocabulary — 2026-09-19.
- Not done: execution or reproduction; `gliner2/` package source; the README tail and remaining tutorials/design docs (boundary architecture, design notes); `benchmarks/` contents; the HF card text and license field; PyPI.

## Falsifiability

- Every number is author-claimed at paper/docs tier; the record is wrong about the artifact if code diverges from docs — the slice a trace-map-style follow-up would settle.
- Finding 2's "first in the surveyed ecosystem" is a count over six records; a missed system with decode-time constraints renumbers it without changing G2-2's disposition.
- The Apache-2.0 claim for the HF checkpoint rests on repo LICENSE + README badge + paper statement; fetching the card's license field would settle it directly.
- Coverage rows cite installed surfaces re-grepped this session; a row is wrong if its cited rule is not found where claimed.
- G2-2's no-change is wrong if a jointly infeasible coupled verdict has already occurred locally but was not recorded; the reopen names the observable.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Both objects pinned (repo revision; fixed publication); identity and license recorded | done | this record |
| Paper read in full; repo docs read at the pin; drift between them recorded | done | Method; What the Artifact Is; G2-6 |
| Ten concepts mapped; six candidates decided with evidence and triggers | done | Concept Map; Candidate Adoption Ledger |
| Direction-scope rule applied: bare survey, nothing named fired | done | Research Question |
| Clean-room boundary on installed surfaces | done | guard vocabulary test |
| Guard written | done | `plans/tests/test_gliner2_survey_record.py` |
| Decision Index row (at head), case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`; `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |
