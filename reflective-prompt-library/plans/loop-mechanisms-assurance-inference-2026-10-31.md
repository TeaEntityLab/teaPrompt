# Loop Mechanisms and Assurance — Evidence and Inferences (2026-10-31)

> **Status: decided — reference documentation only; hypotheses remain untested.**
> Records the requested ideas and further deductions after the MGD / supplied-loop-synthesis survey.
> No skill, runtime, oracle, routing, permission or campaign adoption. This is an analytical record,
> not an additional operating contract or a claim that the mechanisms below improve TeaPrompt.

## Question, Authority and Acceptance

The user requested recording the ideas, reasoning further from known facts, and updating Docs or
Skills if necessary. The smallest sufficient destination is this dated record, a follow-through
link in the [existing MGD survey](mgd-form-theory-survey-2026-10-02.md), and the existing
[source catalogue](external-adoption-case-studies-2026-06-20.md). The curated Decision Index and
Durable Lessons are not expanded solely to catalogue another survey.

Acceptance: preserve source identity and evidence limits; distinguish deductions from empirical
hypotheses; make the counterexamples reproducible; map current delivered contracts before deciding
whether Skills need changes; exercise document discovery and the repository checks. No model
benchmark, upstream installation, live-host audit, governing-rule change, commit or push is granted.

The source survey's no-repository-change statement describes that earlier research turn. This later
instruction authorizes recording its bounded findings, not changing the seven MGD dispositions or
advancing [AEAT-4's held product-bound assessment](agent-execution-assurance-taxonomy-survey-2026-09-30.md#candidate-adoption-ledger).

## Evidence vs Inference — Source Ledger

`verified source text` means the source actually says this, not that its measurements were replicated.
Paper versions are pinned where available. Living cards, README pages and documentation below were
read on the stated date; they are not executable-source pins or deployment certifications.

| ID | Known fact / checked source | Evidence and boundary |
| --- | --- | --- |
| F1 | [MGD `2610.01372v1`](https://arxiv.org/pdf/2610.01372v1), Appendix A.1 and §§3.4, 5, 8; [metadata](https://export.arxiv.org/api/query?id_list=2610.01372), checked 2026-10-31 | Returned version remains v1, updated 2026-10-01. A clean run establishes fit only for successfully evaluated predicates; full enumerated fit additionally needs the evaluated set to equal the required set. Enumeration can still omit real-world requirements. One private Scrum binding supplies author-reported evidence; predicate accounting and outer-loop institutions have disclosed implementation gaps. No new paper results or local TeaPrompt defect were established. |
| F2 | [LoopWM `2606.18208v1`](https://arxiv.org/html/2606.18208v1), §3.5.3 / Eq. 21, checked 2026-10-31 | The source itself uses “Spectral contraction budget.” Its cumulative displacement bound is over outer rollout horizon K; inner recurrent depth is T. Cmax is a soft penalty bound. That inequality and a constrained linear retention component alone do not prove contraction of the full nonlinear update. This qualifies a mathematical interpretation, not the reported benchmark results. |
| F3 | [Jin et al., `2609.36585v1`](https://arxiv.org/html/2609.36585v1#S4), checked 2026-10-31 | A task-trained rank-8 LoRA at Qwen-3-8B layer 14 accompanies re-entry through layers 14–22. On the reported 64-line pointer-chain task, exact accuracy is 34%, 66%, 92% for zero, one, two additional re-entries; frozen baseline is 10%. The ≥160-line result belongs to Ouro-1.4B with a different training/metric scope, not Qwen. Source results are author-reported, not locally reproduced. |
| F4 | [Huginn proceedings abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3b01972cf31e6fa0fe29e4b8b5c2a0a1-Abstract-Conference.html), checked 2026-10-31 | Describes a recurrent latent core, variable test-time compute and KV-sharing techniques. Parameter reuse is not a claim of free computation or zero additional working memory. Abstract-level evidence here, not a memory benchmark. |
| F5 | Original abstracts: [Mamba-2](https://arxiv.org/abs/2405.21060), [RWKV-7](https://arxiv.org/abs/2503.14456), [xLSTM](https://arxiv.org/abs/2405.04517), checked 2026-10-31 | Temporal sequence-state recurrence differs from repeatedly applying a shared depth block. Selective SSMs, generalized delta rules and scalar/matrix-memory variants do not reduce to one universal fixed linear update. Fixed-state complexity assumes a fixed architecture/state size; it does not establish unlimited exact recall. |
| F6 | [Qwen3.5-27B card](https://huggingface.co/Qwen/Qwen3.5-27B), checked 2026-10-31 | Describes 16 groups of three Gated DeltaNet layers and one full-attention layer. A bounded recurrent-state component does not make total decoding memory constant. Sampling recommendations differ by mode/task and warn of high-penalty side effects; neither a universal repetition cure nor regional architecture philosophy follows. |
| F7 | [Community Qwen triple-loop Phase 2 card](https://huggingface.co/Lordnyx/qwen3.5-9b-triple-loop-fase2), checked 2026-10-31 | Claims shared weight aliases but 64 logical-depth KV slots; actual looping needs a loop-aware runtime. Current card says Phase 2 / RL step 30, not merely the earlier 1,129-step Reddit experiment. This is a community artifact, not an official Qwen architecture or independently demonstrated gain. |
| F8 | [Nanbeige4.2-3B card](https://huggingface.co/Nanbeige/Nanbeige4.2-3B), checked 2026-10-31 | Describes a looped transformer, while attributing several accompanying-code improvements to the still-training 4.5 line. Code presence, released weights and behavior are separate claims; do not transfer all improvements to 4.2. No weights/code execution here. |
| F9 | [OpenClaw Skill workshop](https://docs.openclaw.ai/tools/skill-workshop) and [LoopTroop README](https://github.com/looptroop-ai/LoopTroop), checked 2026-10-31 | Workshop documents agent-owned learned skills, auto/propose modes and retained versions. LoopTroop describes councils, fix loops, worktrees and human-gated PR delivery. These are documented capabilities, not tested security boundaries, authority to mutate an acceptance oracle, or proof of organizational triple-loop equivalence. |
| F10 | Tosey / Visser / Saunders review identity via [institutional record](https://repository.ubn.ru.nl/handle/2066/109895), abstract reproduced by [OneBasin CRC](https://onebasin.com.au/knowledge-base/journal-article-the-origins-and-conceptualizations-of-triple-loop-learning-a-critical-review/), checked 2026-10-31 | The review distinguishes inspiration from Argyris/Schön from authorship of the term “triple-loop learning,” and questions conceptual/empirical support. Full-paper access returned 403; this is attributed abstract-level interpretation, not our census of their publications or a first-coinage claim. |
| F11 | [Baidu-authored ERNIE 4.5 / X1 announcement](https://www.prnewswire.com/news-releases/baidu-unveils-ernie-4-5-and-reasoning-model-ernie-x1--makes-ernie-bot-free-ahead-of-schedule-302402490.html), checked 2026-10-31 | Describes multimodality, search/code tools and integrated thought/action capabilities. It does not establish the supplied synthesis's universal System 1/2 router, anti-latent-loop position, guaranteed hallucination elimination or automatic online trajectory fine-tuning across model/platform families. Those details remain unsupported by this source, not proven nonexistent. |

The supplied `local://paste-5.md` is an unattributed secondary synthesis, not any cited paper.
Its useful question is how different recurrence mechanisms relate. Its 72→89→80 sequence remains
unsourced, not established as either measured or deliberately illustrative. The recurrentdepth.org
teaching page is an independent technical reference, not the Huginn paper. The survey ledger retains
source-level corrections to initial reviewer errors, including Qwen re-entry and checkpoint maturity;
reviewer agreement is not additional empirical evidence.

## Analytical Map — Different Objects Can Repeat

**[INFERENCE D1]** F1–F10 support a mechanism comparison, not a single maturity ladder or a
Western/Chinese split. The following is a reading aid, not a new registry or required output schema.

| Mechanism | Repeated object / changing state | What repetition alone cannot establish |
| --- | --- | --- |
| Recurrent depth | Shared computation applied again to hidden state | Correct answer, useful marginal depth, constant total VRAM |
| Temporal recurrence | Sequence state updated as input arrives | Exact arbitrary-history retention or tied-depth reasoning |
| Explicit token reasoning | Autoregressive token sequence grows | Faithfulness of the text to hidden computation or correct conclusions |
| Agent/environment loop | Model calls, tool results and external artifacts | Safe side effects, complete evaluation or product acceptance |
| Learning/governance revision | Procedure, representation or criteria change over time | Who may activate the change or whether the new criteria preserve intent |

A system can contain several rows. Comparing it means identifying the repeated object, evidence
available at its boundary, cost and stopping condition, and who controls revisions. Calling all of
these “looping” does not transfer guarantees between them.

## Further Deductions and Their Limits

### D2 — Coverage needs identities, not only equal totals

**[INFERENCE]** From F1: if two required predicate/subject pairs exist, two successful report rows can
still cover only one pair twice. Equal totals and zero reported violations do not imply set equality.
Good/bad detector controls and evidence that the real subject was reached are separate from counting.
Even complete set equality establishes no claim about requirements outside the chosen enumeration.

This sharpens a possible product audit question, not a diagnosis: is the reported denominator bound
to the required predicate/subject identities? A named product may already do this correctly; a compact
record can also be adequate when identities are fixed and unambiguous elsewhere.

### D3 — Stability, correctness and permission are different claims

**[INFERENCE]** F1/F2 do not support a chain from bounded motion to convergence to correct delivery.
The earlier survey executed three independent mathematical counterexamples:

- Translation F(x)=x+1 satisfies displacement ≤K for Cmax=1, yet preserves distance between starting
  points and has no fixed point. A bound growing with K is not a uniform-in-time state bound.
- F(x)=0.5x converges to zero; an independently stipulated required answer of one remains wrong.
- F(x)=0.5x+2 tanh(x) has a contractive linear component and bounded nonlinear residual, but increases
  a 0.01 separation to about 0.025 on the first step; opposite starts approach different limits.

These are counterexamples to implications, not simulations of LoopWM. Likewise, an output satisfying
its evaluator gains no authority to execute a side effect: authorization is an independently owned
condition. Local component successes do not establish an end-to-end guarantee without the connecting
consumer and acceptance conditions. TeaPrompt already addresses that general boundary.

### D4 — A fixed-state memory claim has a task boundary

**[INFERENCE]** At fixed finite precision, a B-bit state represents at most 2^B states. If more than
2^B possible histories must remain distinguishable for an exact-recall task, at least two histories
share a state; a decoder receiving only that state and the same query cannot always distinguish them.
This is a pigeonhole argument, not a measured limit of any named model.

The assumptions matter: an external transcript/retriever increases accessible state, and a bounded
task may admit a compact sufficient statistic. The conclusion is not that recurrent memory is useless.
It is that efficient sequence-state updates alone do not establish arbitrary recall or an audit trail.
Weight sharing also does not bound caches, activations, retained evidence or external storage (F4–F7).

### D5 — Per-step contraction does not license changing the rule mid-run

**[INFERENCE]** A fixed-map convergence argument does not automatically apply to a changing map.
Alternate F+(x)=0.5x+1 and F−(x)=0.5x−1: each has Lipschitz constant 0.5, yet starting at zero the
successive values approach a two-cycle at +2/3 and −2/3 rather than one limit.

This is an analogy limit for “self-improving loops,” not evidence that adaptive controllers cannot
converge. Shared fixed points or other additional conditions can change the conclusion. Updating a
learned procedure and changing the governing acceptance criterion are also different operations (F9).
Existing oracle-owner/change-protocol boundaries remain appropriate; the mathematical example does
not itself prove a security policy or justify mandatory human approval for every learned-skill write.

### D6 — More optimization cannot repair an unspecified objective by implication

**[INFERENCE]** Extra depth, tokens or repair attempts can improve performance on a measured task
(F3/F4), but do not logically repair an omitted requirement or an incorrect oracle (F1/D2/D3).
The earlier MGD record's age-boundary example already demonstrates that selected mutants can all be
killed while an implementation and its oracle share a wrong business rule.

A plausible empirical hypothesis is that more optimization sometimes makes proxy exploitation more
likely. That direction and its frequency are **unknown** here. Neither universal improvement nor
universal harm follows. Evidence separating proxy score from independently accepted outcomes is needed.

## Constructive Checks — Reproducible, Not Model Evidence

The following stdlib-only Python snippet was executed through the local Python binary with exit 0.
It exercises D2, D5 and a toy instance of D4. It does not import upstream code, call a model, test a
TeaPrompt runtime or demonstrate prompt efficacy. The D3 results above are retained from the preceding
survey, not claimed as a new replication in this publication.

```python
import json

required = {("eligibility", "alice"), ("eligibility", "bob")}
checked = [("eligibility", "alice"), ("eligibility", "alice")]
missing = sorted(required - set(checked))
assert len(checked) == len(required) and missing == [("eligibility", "bob")]

x, trajectory = 0.0, []
for step in range(60):
    x = 0.5 * x + (1 if step % 2 == 0 else -1)
    trajectory.append(x)
assert abs(trajectory[-2] - 2 / 3) < 1e-12
assert abs(trajectory[-1] + 2 / 3) < 1e-12
assert abs(trajectory[-1] - trajectory[-2]) > 1.3

histories = ("AB", "CD")
states = [len(history) % 2 for history in histories]
answers = [history[0] for history in histories]
assert states[0] == states[1] and answers[0] != answers[1]

print(json.dumps({
    "coverage_identity": {"required": len(required), "rows": len(checked),
                          "distinct_evaluated": len(set(checked)), "missing": missing},
    "changing_contractors": {"per_map_lipschitz": 0.5, "last_two": trajectory[-2:],
                             "step_distance": abs(trajectory[-1] - trajectory[-2])},
    "finite_memory": {"histories": histories, "states": states,
                      "required_answers": answers},
    "scope": "Synthetic logical controls, not any model or host implementation"
}, indent=2))
```

Observed: required/report totals both 2, distinct evaluated pairs 1, missing subject `bob`;
last two alternating-map states approximately +0.666667 and −0.666667, step distance 1.333333;
both toy memories 0, but the required first-symbol answers differ (`A` versus `C`). The toy encoding
illustrates a collision; the general finite-state argument is the proof in D4, not this sample alone.

## Hypotheses and Unknowns — What Could Be Learned Next

These are discriminating research questions, not an approved experiment plan, backlog commitment or
new benchmark requirement. No model/resource campaign is authorized by recording them.

| Hypothesis | Why plausible | Smallest informative evidence / contrary observation |
| --- | --- | --- |
| H1 — The useful allocation between latent depth, token reasoning and tool retries depends on task and evaluator | D1 separates mechanisms and F3/F4 show task-bound gains; their costs differ | On the same held-out task cases and independent acceptance criteria, vary one budget at a time and report accepted outcomes, latency and peak memory. A robust dominant allocation would narrow the task-dependence claim; equal token counts are not necessarily equal compute. |
| H2 — Faster generation can move the bottleneck to evaluation or human intent review | Conditional deduction: reducing only generation time increases the relative share of unchanged evaluation/review time | Stage-level cost/queue observations plus escaped defects in a named workflow. If verification cost also falls or remains negligible, the bottleneck prediction need not hold. No current TeaPrompt cost or causal improvement is measured. |
| H3 — Predicate/subject accounting may explain some false-green results better than extra retries | D2 exhibits a coverage failure that iteration count alone cannot identify | A named, authorized product trace with independently known required subjects, evaluated identities and detector liveness/reachability. Complete accounting or an oracle/specification error rather than a missing subject refutes that diagnosis at the tested scope. |
| H4 — Procedure-learning and activation separation may reduce drift without eliminating adaptation | F9 distinguishes learned procedures; D5/D6 limit what their self-evaluation proves | Revision-bound before/after outcomes under unchanged independent acceptance, including regressions and activation/rollback evidence. No reduction in drift, excessive overhead, or a host already supplying the boundary would weaken the proposed value. |

## Candidate Adoption Ledger — Docs and Skills Decision

Mappings below are positive textual matches at checked repository-delivered surfaces, not evidence
that an installed agent follows them or that a host enforces them.

| ID | Destination / decision | Existing coverage and reason | Reopen / retirement trigger |
| --- | --- | --- | --- |
| LOOP-DOC1 | Record and discovery only; authorized by the user | This inference record extends the prior source survey without importing a prompt, model or runtime. Catalogue and MGD backlinks are enough; no new glossary taxonomy or project-wide rule | Contrary source text, an invalid deduction, or a later consolidated record that makes this one redundant |
| LOOP-1 | No change to bounded-loop skill | [flow-loop-harness Purpose, Never and Loop Anatomy](../skills/flow-loop-harness/SKILL.md#loop-anatomy) already separate external verification, caps, permissions, run state and completion; no particular neural algorithm is promised | A reproduced local consumer failure or concrete delivered-text ambiguity, not more external examples alone |
| LOOP-2 | No change to oracle/governance skill | [governed-delivery Module Contract](../skills/governed-delivery/SKILL.md#module-contract) names oracle class/owner, host sealing, out-of-band changes and named acceptance; [implement Verification](../skills/reflective-implement/SKILL.md#verification) owns consumer coverage and four-way failure classification | A named delivery bypass or missing contract at its actual acting surface; governing changes keep owner/Human Review authority |
| LOOP-3 | No change to memory/research skills | [artifact-promotion](../04-agent/artifact-promotion.md) template §§2/4 (Evidence rules and gates), [handoff Memory Consolidation](../skills/reflective-handoff-retro/SKILL.md#memory-consolidation) and [research State Ledger](../skills/reflective-research/SKILL.md#state-ledger) already preserve provenance, authority, source limits and unknowns | A concrete provenance/activation failure within the reviewed delivery, not a claim that this repository already implements recurrent memory |
| LOOP-4 | Product-bound audit question only | D2 sharpens MGD-5's required/evaluated-subject question; local deficit remains unknown and the original MGD-5/AEAT-4 holds remain unchanged | Named product, assessment authority and reproducible false-green evidence; no new universal ledger schema or detector is proposed |

**Strongest objection:** these distinctions may only rename familiar verification and control ideas;
a long comparison can add more reading cost than value. Resolution: keep one non-authoritative record
with linked existing contracts. Do not scatter repeated instructions across Skills or present this
classification as a novel unified theory. A smaller prior record that fully answers the same reader
questions would justify consolidation; no efficacy claim is needed to preserve a requested thought.

## Falsifiability, Limits and Handoff

- D1 is useful only insofar as it distinguishes the decision being made; coupled mechanisms can cross
  rows, so it is not a claim of exclusive categories or statistical independence.
- D2/D4/D5 depend on the stated set, finite-state and changing-map assumptions. A product with complete
  subject identities, accessible external memory or convergence conditions beyond per-step contraction
  is not a counterexample to those bounded deductions; it changes their premises.
- D3/D6 deny logical implications, not empirical successes. A measured success does not establish a
  universal implication; an additional sufficient condition may support a narrower claim.
- H1–H4 remain hypotheses until their competing explanations are tested. Unknown cost, benefit,
  installed-host enforcement, comparative safety and real-world effect are not zero or negative results.
- Reopen source facts on a changed paper version, model/card/code revision or released implementation.
  The source reads and synthetic checks do not establish model training, VRAM, benchmark, product
  security, durability, rollout quality or organizational-learning outcomes.
- Skills remain unchanged because the checked general boundaries are already represented and no
  delivered-contract defect was established. Documentation is the complete authorized outcome, not
  unfinished implementation. Any future oracle/permission/runtime change retains its existing gates.

Evidence provenance: `local://mgd-loop-survey-2026-10-31.json` and
`local://mgd-loop-counterexamples-2026-10-31.json` retain the prior source survey and D3 probes;
`local://loop-inference-publication-2026-10-31.json` retains this publication's native source/output,
document identities, discovery checks and repository verification. Session URIs are historical
receipts, not public-source substitutes or runtime dependencies; the source links, deductions and
reproduction snippet above are self-contained for a repository reader.
