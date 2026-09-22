# EMBER Survey — arXiv:2604.12167v1 (SNN-as-LLM-memory) — 2026-09-22

> **Status: decided — record-only; no installed change, no wording adopted.** The
> objects are a preprint — **EMBER** (Experience-Modulated Biologically-inspired
> Emergent Reasoning), arXiv:2604.12167v1 [cs.AI], 14 Apr 2026, CC BY-NC-ND 4.0,
> William Savage (Independent Researcher, digitalember.dev), NeurIPS-checklist
> formatted — and a paste (`local://paste-1.md`) that is a **lossy reader-mode copy
> of that same paper**, not an independent synthesis. Verified this session: the
> paste's text matches the arXiv HTML at the pin (same abstract, contributions,
> numbers, tables), so the "a pasted synthesis is a claim about its source" lesson
> resolves trivially — the paste *is* the source, at lower fidelity. EMBER is an
> SNN+LLM cognitive-architecture paper: neuroscience-runtime territory for a repo
> with no neural runtime. It is the **second brain-inspired SNN artifact surveyed
> this session** (after `teaBrain`), and its adversarial-association risk is a second
> external witness to `teaBrain`'s TB-1 runtime-learner governance class. Code is
> "released upon publication" (unavailable); all results are N=1 and author-claimed.
> Bare survey → DS-1: nothing installed. Guard: `plans/tests/test_ember_survey_record.py`.

## Research Question

User instruction: "survey local://paste-1.md https://arxiv.org/html/2604.12167v1".
Three questions: (1) what the artifact is and at what evidence tier; (2) whether the
paste faithfully represents its source; (3) whether any concept exposes a **verified
gap** on an installed TeaPrompt surface. A bare survey carries no adoption direction;
the standing bar per candidate is a verified gap on one installed surface, a named
failure the change defends against, a smaller alternative rejected, and a
deterministic guard. TeaPrompt operates no neural runtime, so EMBER's SNN mechanisms
are host territory; the transferable content is its scientific-honesty discipline and
one governance cross-link.

## Direct Recommendation (as of 2026-09-22)

- **Study — the honesty discipline and the SNN-as-associative-memory reframing.**
  EMBER's thesis is a clean inversion: instead of augmenting an LLM with retrieval
  tools, place the LLM as a *replaceable reasoning engine* inside a persistent SNN
  associative substrate where associations are learned by STDP and expressed by
  lateral propagation "not constructed by prompt engineering or retrieved by
  similarity search." Its reporting is scrupulous: **N=1 stated repeatedly**, "we make
  no claims about consciousness or subjective experience," LLM-confabulation and
  prompt-ordering bias named, ablation labelled preliminary, every autonomous action
  "logged, timestamped, and inspectable." That is the evidence-over-confidence stance
  TeaPrompt records require, applied by an external author to an easily-overhyped result.
- **Reproduce — blocked.** Source code and logs are "released upon publication"
  (unavailable at the pin); results are a single system instance with a single user;
  nothing was executed. Every number (82.2% retention, 7-exchange first action, 23
  impulse-driven actions, weight trajectory) is author-claimed at docs tier.
- **Adopt — nothing.** Bare survey → DS-1 record-only. Six concepts map to
  out-of-scope neuroscience (SNN/STDP/encoding/concept-cells — no TeaPrompt neural
  runtime) or to installed methodology (honesty, ablation/second-method); the one
  governance-shaped concept (EM-4, adversarial-association persistence) is a second
  external witness to `teaBrain`'s TB-1 class, logged and cross-linked, **not** landed
  (still zero user directions to scaffold self-modifying-agent governance).
- **For citers:** license is **CC BY-NC-ND 4.0** (no derivatives — quote, do not
  adapt into installed text). Everything is N=1 and author-claimed; the "autonomous
  reach-out" is one observed instance; the journal narratives are LLM-generated over
  impulse signals and "may confabulate." The author discloses a prompt-ordering bias
  (journaling listed before reach-out) that makes the single reach-out notable but not
  a statistic.

## Method

Coordinator read (2026-09-22), no scouts, no panel: `local://paste-1.md` in full and
the arXiv HTML at `https://arxiv.org/html/2604.12167v1` in full, comparing the two to
establish the paste is a copy. Installed-surface grep confirmed EMBER vocabulary is
absent from every skill and category surface (clean-room boundary). No code exists at
the pin to execute; nothing reproduced.

**Scope / acceptance:** identify the artifact and its evidence tier; confirm the
paste=source relationship; map the concept set against installed surfaces; decide each
candidate with evidence and a trigger; land nothing without a verified gap and an
adoption direction; keep the clean-room boundary; run `make all`.

## What the Artifact Is

A **hybrid cognitive architecture**: a 220,000-neuron spiking neural network (SNN)
with spike-timing-dependent plasticity (STDP) as a persistent associative-memory
substrate, plus an LLM (Claude Sonnet 4.6) as a swappable reasoning engine that
"reasons over associations the SNN provides; it does not create them." Six components:
the SNN substrate (four layers — sensory 5k / concept 150k / category 25k /
meta-pattern 10k — plus 30k inhibitory interneurons; LIF neurons with σ=0.1 background
noise giving ~0.9 Hz spontaneous firing, essential so idle lateral cascades can
express); depression-dominant reward-modulated STDP with cascade-scaled decay (Fusi
2005); a **"soul layer"** (persistent identity + immutable safety values, injected into
every reasoning call); three memory systems (episodic replay, perfect recall, journal)
under complementary-learning-systems theory; the LLM reasoning engine (model-agnostic
adapters); dual consumer GPUs. Two distinctive mechanisms: **z-score standardised
top-k population encoding** (solves the dimension-dependence of power-law codes;
82.2% "discrimination retention" at 1024-dim, 83.8% at 384-dim → dimension-independent)
and **person concept cells** ("Jennifer Aniston neuron" analog; STDP encodes
person→topic associations that fire laterally during idle). Autonomy is
**content-triggered**: lateral impulses >3× baseline, 3+ in a 5-min window, trigger an
LLM action selection over a structured vocabulary (journal, `reach_out`, continue,
silent) — "actions it can take, not actions it should take." Reported N=1 result: from
zero weights, the first SNN-triggered action came after 7 exchanges and was an
unsolicited `reach_out`; over a 3-day 5-domain 52-message baseline, 23 impulse-driven
actions (1 reach-out, 22 journals). An SNN-disabled ablation (same LLM/soul/memory/
protocol) shows more cross-domain integration and journal diversity with the SNN on —
both conditions N=1.

## Concept Map

Tier is `docs` throughout (preprint text at the pin; no code audited, nothing run).

| ID | Concept | TeaPrompt coverage | Disposition |
| --- | --- | --- | --- |
| EM-1 | SNN associative substrate: 4-layer STDP, LIF + spontaneous-noise idle dynamics, cascade-scaled decay, reward-modulated learning, person concept cells, impulse detection | Host territory — TeaPrompt runs no neural runtime; same substrate family as `teaBrain` P1–P4 (out of scope there too) | No change (out of scope) |
| EM-2 | Scientific-honesty discipline: N=1 stated repeatedly, "no claims about consciousness," confabulation + prompt-ordering bias named, ablation labelled preliminary, every action logged/timestamped/inspectable | `01-thinking/critical-thinking-check` (claim tagging), evidence-over-confidence, verdict-scope / author-claimed-vs-verified | No change — corroboration |
| EM-3 | SNN-disabled ablation isolating one component's contribution under an otherwise-identical control (same LLM/soul/memory/protocol/operator) | `reflective-research` second-method discipline; `reflective-review` overengineering/edge scan; ablation-as-attribution | No change — corroboration |
| EM-4 | Adversarial-association persistence: learned STDP weights "resist decay through cascade scaling and cannot be filtered like prompt-injected text"; the soul layer (immutable safety values) is a partial reasoning-stage defence only; mitigations = weight auditing, association quarantine, topology-aware gating | Runtime self-modifying-agent governance — the exact class of `teaBrain`'s **TB-1** (governance the `agent-governance-scaffold` pack lacks); TeaPrompt runs no such runtime | No change — cross-linked to TB-1; second external witness; trigger unfired |
| EM-5 | Content-triggered autonomy (vs system-event triggers in MemGPT/Generative Agents) over a structured action vocabulary; "affordances not prescriptions" | Host-runtime autonomy design; the affordance/authority separation echoes `agent-governance-scaffold` proposal-vs-effect, but is runtime | No change (out of scope) |
| EM-6 | Discrimination-retention metric (model-independent population-code evaluation) + z-score top-k encoding solving dimension-dependence | Out-of-scope encoding metric; no TeaPrompt population code to evaluate | No change (out of scope) |

## Candidate Adoption Ledger

All rows decided under a **bare survey** (no adoption direction); none installed.

| ID | Candidate | Status | Evidence | Reopen trigger |
| --- | --- | --- | --- | --- |
| EM-1 | SNN mechanisms onto a TeaPrompt surface | No change (out of scope) | No neural runtime; host territory (same disposition as `teaBrain` P1–P4) | None |
| EM-2 | Honesty-discipline sentence from EMBER's reporting | No change | Held by claim-audit / evidence-over-confidence / verdict-scope; adoption on external elegance is forbidden without a local gap | A local case where a skill lacks an N=1 / confabulation-scope caveat it needs |
| EM-3 | Ablation-as-attribution sentence | No change | Held by second-method + overengineering-scan discipline | A local gap where a review/research surface omits the isolate-one-variable control |
| EM-4 | Adversarial-association / poisoned-persistent-state governance into `agent-governance-scaffold` | No change (cross-linked to TB-1) | Same class as TB-1 (runtime-learner governance the pack lacks); EMBER is a **second external witness** (Tay-analog risk + weight-auditing/quarantine/topology-gating mitigations) but n=0 user directions; bare survey; CC BY-NC-ND forbids adapting its text | Reopen TB-1 when a user directs governance scaffolding for a self-modifying / online-learning / reward-driven agent (external witnesses strengthen evidence, they do not fire the trigger) |
| EM-5 | Content-triggered autonomy / action-vocabulary affordances | No change (out of scope) | Runtime autonomy design; Standing Non-Goal | None |
| EM-6 | Discrimination-retention metric / z-score encoding | No change (out of scope) | Encoding metric; no local population code | None |

Recurrence is `unknown`; a preprint is not local recurrence. No installed surface
changed; no wording adopted.

## Cross-Link: EMBER and teaBrain's TB-1

`teaBrain`'s TB-1 (this session) logged that the `agent-governance-scaffold` pack has
no vocabulary for governing a **self-modifying / online-learning** agent, with a named
failure (a reward-driven agent games or poisons its own persistent state, which
op-count budgets and file-ACL constitutional paths cannot catch). EMBER independently
names the same class from the opposite direction: STDP-learned associations "resist
decay through cascade scaling and **cannot be filtered like prompt-injected text**,"
so prompt-level and text-filter defences do not reach the poisoned weights; its
proposed mitigations (weight auditing, association quarantine, topology-aware gating)
are runtime-neural, not prompt-level. This is a **second external witness** that the
class exists in the wild (teaBrain hand-authored runtime-learner governance primitives;
EMBER names the risk and mitigations). It **strengthens TB-1's evidence, not its
authorization**: TB-1's reopen is a *user direction* to scaffold such an agent, of
which there are still zero. Recorded so the recurrence accounting stays honest
(n=2 external witnesses; n=0 user directions).

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| arXiv identity (2604.12167v1, 14 Apr 2026, CC BY-NC-ND 4.0, author, NeurIPS checklist) | Observed | arXiv HTML at the pin, 2026-09-22 |
| paste-1.md is a lossy copy of the same paper | Observed | Line-by-line comparison; same abstract, numbers, tables, references |
| Architecture, mechanisms, protocol as described | Observed at docs tier | Paper read in full; no code audited |
| All quantitative results (82.2%, 7 exchanges, 23 actions, weight trajectory, ablation deltas) | Author-claimed | Preprint; N=1; nothing executed or reproduced |
| EMBER is the second brain-inspired SNN artifact this session | Observed | `teaBrain` survey earlier today |
| EM-4 is the same class as TB-1 | `[INFERENCE]` | Both describe self-modifying-agent poisoned-persistent-state risk; drawn from the two texts, not a unified formal model |
| Whether behaviours are architecture- vs model-specific | Unknown — correctly so | Paper says cross-model validation is "underway" |

## Evidence Actually Checked

- `local://paste-1.md` (356 lines) and `https://arxiv.org/html/2604.12167v1` read in
  full, 2026-09-22; paste-vs-source fidelity compared.
- Installed-surface grep for EMBER vocabulary (EMBER, STDP, spiking, `reach_out`,
  digitalember, Jennifer Aniston, z-score, cascade-scaled, concept cell) — absent.
- Not done: no code (unreleased), no reproduction, no citation-chain audit of EMBER's
  ~20 neuroscience references, no independent check of the N=1 logs.

## Falsifiability

- Wrong about identity if the arXiv page did not carry the quoted id/date/license on
  2026-09-22 — all quoted from the HTML at the pin.
- Wrong about paste=source if a substantive claim in the paste is absent from or
  contradicts the arXiv text — none found; the paste is lower-fidelity, not divergent.
- EM-2/EM-3 "held" is wrong if the claim-audit / second-method discipline is not on the
  cited installed surfaces; both are grep-checkable.
- EM-4's cross-link is interpretive; the underlying risk statements are quoted from
  both artifacts and TB-1's record. A preprint is not local recurrence and does not
  fire TB-1.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Artifact identified; license and evidence tier recorded | done | Status; Direct Recommendation |
| Paste verified as a copy of the arXiv source | done | Research Question; Evidence vs Inference |
| Six concepts mapped; six candidates decided with triggers | done | Concept Map; Candidate Adoption Ledger |
| Governance cross-link to TB-1 recorded (witness, not authorization) | done | Cross-Link section |
| Bare-survey direction-scope rule applied: nothing installed | done | Status; Research Question |
| Clean-room boundary on installed surfaces | done | guard vocabulary test |
| Guard written | done | `plans/tests/test_ember_survey_record.py` |
| Decision Index row (at head), case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`; `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |
