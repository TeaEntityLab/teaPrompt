# teaBrain Concepts & Experiments Survey — `~/dev/teaBrain` @ `27b4d25` (2026-09-21)

> **Status: decided — record-only; no installed change, no wording adopted.** The
> object is a sibling research repository (`~/dev/teaBrain`, HEAD
> `27b4d25a9516075c4fe6753e71c2ab1dc1b5465f`, tree
> `0788d2cd29eddb5d5db4da495fefedb943065a2f`, clean working tree, 2026-09-21) that
> bets **insect-scale reflexive control can be learned online with local plasticity
> and fixed random dynamics — no backpropagation, no fine-tuning, no gradient
> descent**. Two facts make it unlike every prior survey object. (1) Its
> `docs/governance/` is a **host-side operationalization of TeaPrompt's own
> `agent-governance-scaffold` pack** — the four-power split, the fifteen-invariant
> checklist (word-for-word identical vocabulary), the full artifact set, the
> wrapper-contract with `bash` removed, the `run-agent.sh` interface, and the exact
> `artifact-complete` status literal — extended with runtime-learner primitives the
> pack does not carry. (2) Its mainline experiments were **reproduced locally at the
> pin** (pytest 12/12; every headline number matched), so its numbers are not
> author-claimed. Both facts are corroboration and usage evidence, not local
> promotion evidence, and a bare "survey" carries no adoption direction: nothing is
> installed here. Guard: `plans/tests/test_teabrain_survey_record.py`.

## Research Question

User instruction: "Survey from concepts and experiments of @~/dev/teaBrain". Three
questions: (1) what teaBrain's concepts are and at what evidence tier; (2) whether
its experiments actually run and support their claims; (3) whether any concept
exposes a **verified gap** on an installed TeaPrompt surface. A bare "survey"
carries no adoption direction; the standing bar applied per candidate is a verified
gap on one installed surface, a named failure the change defends against, a smaller
alternative rejected, and a deterministic guard. teaBrain is the same author's
sibling project and dogfoods TeaPrompt methodology; usage of one's own pack is
**corroboration and usage evidence, not promotion evidence** (`PROJECT_KNOWLEDGE.md`
Standing Non-Goals; primer: "External interest is not local promotion evidence"),
and n=1 same-author usage does not clear the recurrence gate.

## Direct Recommendation (as of 2026-09-21)

- **Study — the governance operationalization and the claim-audit discipline.**
  teaBrain is the first observed downstream host that instantiated the *entire*
  `agent-governance-scaffold` artifact set and then extended it with governance for a
  **self-modifying / online-learning** agent (metric-drift budgets, authenticated
  reward channels, behavioral-wireheading monitors) — a class the pack, scoped to
  bounded coding workers, does not address. Separately, its docs are an exemplar of
  the evidence-over-confidence discipline TeaPrompt requires: every number is tagged
  CONCEPT / CLAIM / TARGET, the "47% ceiling" was retracted as a `w_radius=1`
  artifact, a "richer value function" hypothesis was **tested and refuted** (63% <
  73%), a stale R5 scorecard line was fixed, and the ~5 pp residual to the baseline
  is named rather than buried.
- **Reproduce — done for the mainline.** Unlike every prior survey (all
  author-claimed, "nothing executed"), the numpy/stdlib experiments were run at the
  pin: `pytest tests/ -q` → **12 passed, 0 failed**; R2 73.0% (94% of Braitenberg
  78.0%), R3 65.0%→1.0%→65.0% while Braitenberg is stuck 78.0%→3.0%, R4 ring-attractor
  `amp_ratio` 1.00 / `circ_var` 0.000 vs leaky-reservoir 0.04, R5 62.0% (critic) vs
  11% (global baseline) — all match the docs. **Not run:** Track A (neuromorphic
  hardware — no boards) and M4 (flyGym/MuJoCo — deps absent), both deferred in the
  repo itself; PyTorch is not installed, so the "tensor backend" path is unexercised.
- **Adopt — nothing.** Bare survey → record-only. Twelve concepts map to installed
  governance / thinking / spec surfaces (corroboration or usage instances) or to host
  territory (the neuroscience — TeaPrompt runs no neural runtime). The one verified
  pack gap (runtime-learner governance, TB-1) is logged with a reopen trigger, not
  landed: the pack's declared scope is coding workers, this is a single same-author
  instance, and DS-1 forbids a bare survey from firing anything.
- **For citers:** teaBrain is **greenfield, simulation-only, and governance
  `artifact-complete` — not enforcement-wired** (no broker, policy engine, verifier,
  or sandbox runs; its own status says so). Every performance number is a success
  rate on a 2D chemotaxis toy, **not** a hardware, energy, or latency claim (Track A
  is unbuilt; no wall-clock or Joules figure was measured). Node-perturbation sits
  ~5 pp below a hand-tuned Braitenberg on the *stationary* task; the thesis rides on
  **R3 online re-adaptation** (the primary go/no-go), where a static controller is
  disqualified — not on R2 competence.

## Method

Coordinator reads (2026-09-21) plus three read-only scouts. Coordinator read in
full: `docs/intents.md`, `docs/plans/00-master-plan.md`, `docs/plans/06-solution-spectrum.md`,
`docs/reviews/2026-09-21-panel-synthesis.md`, all four `docs/governance/` files
(`authority-map.md`, `invariant-map.md`, `worker-contract.md`, `contracts.yaml`),
`scripts/run-agent.sh`, and the source cores `teabrain/learning/critic_learner.py`
and `teabrain/neurons/ring_attractor.py`. Scout **PillarPlans** extracted plans
01–05 (P1–P4 + tracks) with `file:line` anchors and CONCEPT/CLAIM/TARGET tags.
Scout **ReviewsExp** extracted the M2-bottleneck, P3-upgrade, and governance
reviews. Scout **CodeVerify** mapped `teabrain/` + `bench/` + `tests/` to their
algorithms and **executed** the suite and the fast benches in the repo's `.venv`,
reporting the printed numbers below. TeaPrompt-side grounding grepped this session:
the `agent-governance-scaffold` SKILL and its concepts doc (zero runtime-learner
vocabulary — TB-1 gap), `04-agent/workflow-recipes.md` §Parallel Lens Review,
`01-thinking/falsifiability.md`.

**Scope / acceptance:** pin the revision; read the primary docs and source cores;
run the mainline experiments; map the concept set against installed surfaces; decide
every candidate with evidence and a trigger; land nothing without a verified gap and
an adoption direction; keep the clean-room boundary (teaBrain's neuroscience
vocabulary stays out of installed surfaces); run `make all` from the repository root.

## What the Artifact Is

teaBrain separates one component library into **two lines with independent gates**
(`docs/intents.md`): **R — Research** (can local plasticity + fixed dynamics do
adaptive control? — the science, level L3), and **P — Product** (can bio-inspired
middleware cut agent cost/latency? — engineering, L0/L1). The research loop stacks
four "pillars": **P1** a stateless sparse random projection (FlyHash / mushroom-body
Kenyon cells, `K/d ≈ 40×`, ~5% k-WTA, fixed binary fan-in ~6); **P2** leaky
integrate-and-fire "time as state" with an `O(1)` footprint and an honestly bounded
`3–5τ` fading horizon; **P3** three-factor backprop-free R-STDP with an RPE baseline
`δ = R − R̄`; **P4** a dual-regime recurrent layer — a contractive echo-state
reservoir (`ρ<1`, perception) plus an engineered ring-attractor sub-circuit
(persistent heading). The build order is **walking-skeleton-first** (a crude
complete loop at M1) precisely so the #1 risk — *compositional collapse* (static
code → spikes → timing-sensitive STDP → non-stationary loop) — is retired early, not
discovered at M4. Application tracks: A (neuromorphic edge hardware), B (2D
chemotaxis → flyGym, the default main line), C/C′ (an LLM reflex-cache layer and its
non-spiking middleware twin). A `06-solution-spectrum.md` ladder (L0 Redis-like cache
→ L4 neuromorphic) frames the honest question as "the cheapest level that solves the
actual problem," and names the **cannibalization risk**: L0/L1 can ship so cheaply
the science never happens.

The planning set was hardened by a **five-lens parallel Socratic panel**
(`2026-09-21-panel-synthesis.md`): two lenses voted DISAGREE on the pre-revision
docs and their objections were adopted as changes (ESP↔attractor contradiction,
metric-mirage baselines, streaming-wireheading vs file-ACLs, a "match/exceed LLM"
category error). Governance is treated as a first-class pillar because the runtime
agent **rewrites its own synapses online** and may one day drive actuators or
production LLM traffic.

## Concept Map

Two tiers. **Methodology / governance concepts (C1–C9)** are TeaPrompt-relevant and
drive the ledger. **Neuroscience concepts (C10–C12)** are the artifact's science,
recorded faithfully but out of scope for a repo with no neural runtime. Tier for
C1–C9 is `installed-surface comparison`; tier for C10–C12 is `read + reproduced`.

| ID | Concept | TeaPrompt coverage | Disposition |
| --- | --- | --- | --- |
| C1 | **Four-power split + fifteen-invariant checklist**, with **word-for-word identical** invariant vocabulary (`model-output≠effect` … `control-effective-under-full-disclosure`, same order) — `docs/governance/authority-map.md`, `invariant-map.md` | `agent-governance-scaffold` §Four-Power Split + §Fifteen-Invariant Checklist | No change — first observed downstream operationalization; corroboration |
| C2 | **Full artifact set instantiated** in `contracts.yaml`: `capability_token` (with `state_predicate`), broker `effect_receipt` (`issued_by: broker`, `before_hash`/`after_state`), lease + cross-purpose budgets, `acceptance_ladder` L0–L5, `constitutional_paths`, `policy_activation` (`usable_by_existing_leases: false`), `named_approval`, `escalate_if`, `checker_profile` (identical placeholders 0.9/0.2/0.1/1.0/0.9), `mutation_suite`, `approver_canary`, `agenda_check`; `worker-contract.md` (three-no clause, `bash` removed); `run-agent.sh` (mode-validated, `--cd`-fenced, stdin prompt, state-predicate TOCTOU check) | `agent-governance-scaffold` §Artifact Set + §15.1/§15.2 | No change — usage instance of the generator; **artifact-complete, not host-wired** |
| C3 | **Runtime-learner governance the pack lacks**: `runtime_agent_budget` (metric-drift `‖W(t)−W₀‖_F/‖W₀‖_F ≤ 0.15`, single-step clip 0.01, golden-reflex regression, `on_budget_exhaustion: freeze_plasticity_and_escalate`, `max_reflex_promotions_per_epoch: 0`); `reward_channel_provenance` (hmac/mtls, rejects `internal_agent_self_report`); `behavioral_wireheading_monitors` (sensor-pinning / motor-freeze / output-entropy-collapse) + learner mutation cases; `irreversible_effect_guard` concrete bounds + production circuit-breaker | Verified gap: `agent-governance-scaffold` SKILL + concepts doc grepped — **zero** matches for these tokens | No change — reopen trigger **TB-1** below |
| C4 | **Governance activation-timeline minimality**: three tiers (active-now dev surface / active-at-M1 sim / deferred real-effect); "in pure simulation, good acceptance gates + monitors-as-asserts substitute for a host broker"; "pay governance cost when the effect surface appears, not before" | `reflective-minimality` + `agent-governance-scaffold` §"emit only what the task needs" + Gate 2.0 risk-thickness | No change — corroboration; sharpest governance-minimality instance seen |
| C5 | **`artifact-complete` vs `enforcement-proven` status literal** used verbatim ("artifact-complete — contracts emitted and parse-checked; host wiring … is a precondition this document cannot enforce") | `agent-governance-scaffold` §Verification Status gate (the exact two-literal contract) | No change — the pack's own status vocabulary observed downstream; methodology-vs-operationalization boundary corroborated |
| C6 | **Five-lens parallel Socratic review** with structured yield, a candidate-adoption ledger, and **disagreements preserved** (two DISAGREE lenses adopted as changes, not dismissed) | `04-agent/workflow-recipes.md` §Parallel Lens Review; managed skill `parallel-lens-review-packet` | No change — downstream usage instance, as specified |
| C7 | **Falsifiability-first**: every assumption A1–A5 and every goal R1–R6 / P1g–P5g carries an explicit "falsified / killed if"; a single go/no-go (R3) is named | `01-thinking/falsifiability.md` | No change — corroboration |
| C8 | **Walking-skeleton-first / integration-risk-retired-at-M1**: component gates "never substitute for closing the loop"; the crude complete loop precedes any polished pillar | `reflective-spec-plan` usage-first + integration-risk-first | No change — corroboration |
| C9 | **Concepts-vs-experiments honesty**: numbers tagged CONCEPT/CLAIM/TARGET; the 47% "ceiling" retracted as a `w_radius=1` artifact; a richer-`V` hypothesis tested and **refuted** (63% < 73%); stale R5 line fixed; ~5 pp residual named | `01-thinking/critical-thinking-check.md` claim audit; `06-repo/AGENTS.md` §Anti-cheating (execution claims); record byte-pinning practice | No change — strongest external corroboration of claim-audit; **experiments reproduced** (TB-5) |
| C10 | **P1 sparse random projection** (fixed binary fan-in, k-WTA, geometric not semantic; character n-gram hashing prohibited for semantic routing because negations share >85% n-grams) — `flyhash.py` | Host territory — no TeaPrompt neural runtime; the semantic-embedder-mandatory point already lives in host-serving surveys | No change — out of scope |
| C11 | **P2 time-as-state** `O(1)` footprint with an honestly **bounded** fading horizon (no infinite recall without P4 attractors) — `reservoir.py` | Host territory; the transferable bit (honesty about the bound) is C9's claim-audit | No change — out of scope |
| C12 | **P3/P4 dynamics**: three-factor advantage learner `A = r − V(s)`, `W += lr·A·e` (`critic_learner.py:64-73`); dual-regime honesty — an ESP reservoir (`ρ<1`) and a persistent attractor are *mutually exclusive*, so they are separated (ring `W = (j_exc/n)·cos(Δφ) − j_inh/n`, `ring_attractor.py:32,46`) | Host territory; the mutually-exclusive-regimes honesty is again C9 | No change — out of scope |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| TB-1 | Add runtime-learner governance primitives to `agent-governance-scaffold` (metric-drift budget, reward-channel provenance, behavioral-wireheading monitors + learner mutation cases) | No change 2026-09-21 | C3: gap grep-verified (pack SKILL + concepts doc carry none), and the named failure is real (a reward-driven agent motor-freezes to game a penalty, which the pack's op-count budget + file-ACL constitutional paths cannot catch); **but** the pack's declared scope is bounded coding workers, this is n=1 same-author usage, and the survey supplies no adoption direction | Reopen if a user directs governance scaffolding for a **self-modifying / online-learning / reward-driven** agent (a second such need is the recurrence signal; expanding a pack's domain needs a registry decision + human approval per Standing Non-Goals) |
| TB-2 | Add a governance activation-timeline / monitors-as-asserts-substitute-for-broker sentence to the pack or `reflective-minimality` | No change 2026-09-21 | C4: the pack already teaches "emit only what the task needs" + risk-thickness sizing, and minimality already teaches pay-cost-when-needed; teaBrain's three-tier timeline is a domain *application*, not a gap | Reopen if a pack user ships premature governance a timeline lens would have prevented |
| TB-3 | teaBrain as a host-integration instance firing the DM-5/MV-6/JA-7-class trigger | Not fired 2026-09-21 | teaBrain is **artifact-complete** (its own status; no broker/verifier/policy engine wired), matching the pack's own status — usage of the generator, not an enforced host integration; the class trigger names an *executed* host integration wiring enforcement to a TeaPrompt-run step ("tool/artifact existence is not host integration") | Reopen if teaBrain (or any project) wires the pack's broker/verifier and runs the `mutation_suite` (i.e. reaches `enforcement-proven`) |
| TB-4 | Parallel-lens / falsifiability / walking-skeleton corroboration onto any surface | Noted (record-only) | C6/C7/C8: downstream usage of installed methods exactly as specified; no gap | None |
| TB-5 | Reproduced experiments as an evidence-tier note | Noted (record-only) | C9: first survey where the surveyed artifact's experiments were **run** locally at the pin (12/12 tests; all headline numbers matched); corroborates evidence-over-confidence | None |
| TB-6 | Neuroscience pillars (P1–P4) onto a TeaPrompt surface | No change (out of scope) | C10–C12: TeaPrompt operates no neural runtime; the science is host territory; the transferable honesty is already C9 | None |

Deterministic guard: `plans/tests/test_teabrain_survey_record.py` (identity/tree pins,
reproduced-number pins, quoted-literal pins, six dispositions, clean-room boundary,
index links).

## Experiments Reproduced (the distinctive evidence)

Run in `~/dev/teaBrain/.venv` at the pin (Python 3.14, NumPy 2.5.3; **no PyTorch**).
`pytest tests/ -q` → **12 passed, 0 failed**.

| Experiment | Script | Measured (this run) | Docs claim | Match |
| --- | --- | --- | --- | --- |
| M0 baselines | `bench/run_baselines.py` | Braitenberg (gain 40) **78.0%**, RandomWalk **14.0%** | 78% / 14% | ✓ |
| M1 walking skeleton (R1) | `bench/train_skeleton.py` | 14% → **44.0%** greedy; PASS | ~44%, R1>30% | ✓ |
| M2 bottleneck sweep | `bench/m2_sweep.py` | inst-norm **47.0%**; fixed-scale 39–41% | 47%; 39–41% | ✓ |
| P3 normalization probe | `bench/p3_upgrade.py` | inst **66.0% ± 0.0**, running **68.0% ± 0.0** (6 seeds) | 66% / 68%, 0 std | ✓ |
| P3 critic / R2 (1-D) | `bench/p3_critic.py` | **73.0% ± 0.0** (6 seeds) = 94% of Braitenberg | 73% = 94% | ✓ |
| R3 reversal (primary go/no-go) | `bench/r3_adapt.py` | learner **65.0% → 1.0% → 65.0%**; Braitenberg **78.0% → 3.0%** stuck; PASS | 65→1→65; 78→3 | ✓ |
| R4 heading persistence | `bench/r4_persistence.py` | ring `amp_ratio` **1.00**, `circ_var` **0.000**, drift 0.000; leaky `amp_ratio` **0.04** decays; PASS | 1.00 / 0.000; 0.04 | ✓ |
| R5 multi-output (global) | `bench/r5_highdim.py` | 1-D 41%, 2-D **11%**; status REVIEW (by design) | ~11% collapse | ✓ |
| R5 multi-output (critic) | `bench/p3_critic.py` | 2-D **62.0% ± 6.5** (4 seeds: 64/53/68/63) | 62% vs 11% | ✓ |

The advantage baseline `A = r − V(s)` is the lever: it lifts the ~66–68% global-baseline
ceiling to 73% and recovers 2-D control from 11% to 62% (+51 pp), all backprop-free
(`critic_learner.py:64-73`). The stdlib `agents/reflex_loop.py` was deliberately left
at `w_radius=1` (un-retuned) pending a dedicated transfer test — a documented, honest
residual, not a hidden one.

## Shared Findings

1. **teaBrain is the first surveyed object that is a downstream consumer of
   TeaPrompt's own methodology.** Its governance layer is the `agent-governance-scaffold`
   artifact set operationalized on a real project — four-power split, byte-identical
   fifteen-invariant vocabulary, identical `checker_profile` placeholders, identical
   L0–L5 ladder, the wrapper-contract with `bash` removed, the `run-agent.sh`
   interface, and the exact `artifact-complete` status literal. Its planning was
   hardened by the `parallel-lens-review-packet` method; its assumptions use
   `falsifiability`; its build order uses spec-plan's integration-risk-first. This is
   strong **corroboration** the packs are usable end-to-end — and, being one
   same-author project that used them as designed, it is **not** promotion evidence
   for anything new.
2. **The one thing teaBrain needed and the pack did not provide is the one candidate.**
   It hand-authored governance for a *self-modifying learner* (metric-drift budgets,
   authenticated reward channels, wireheading monitors, freeze-plasticity-not-halt).
   The pack, scoped to bounded coding workers, has none of it (grep-verified). That
   is a real gap (TB-1) with a real named failure — but a bare survey lands nothing,
   and one instance is below the recurrence gate.
3. **This survey upgrades the evidence tier of the series.** Every prior survey
   ended "nothing executed, author-claimed." Here the mainline ran: 12/12 tests and
   nine benchmarks reproduced their documented numbers exactly at the pin. The
   research claim that survives is **R3 — online re-adaptation without an offline
   step** (65→1→65 while a fixed controller is stuck at 3%); R2 competence sits ~5 pp
   below a hand-tuned baseline and the repo says so.
4. **The honesty discipline is the artifact's strongest transferable property.**
   Retracting the 47% ceiling as a hyperparameter artifact, refuting its own
   richer-`V` hypothesis (63% < 73%), fixing a stale scorecard line, and tagging
   every number CONCEPT/CLAIM/TARGET is exactly the claim-audit / evidence-over-
   confidence stance TeaPrompt's records require — applied by a downstream project to
   its own science.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Repo identity, tree, clean working tree, 2026-09-21 | Observed | `git log`/`status` at the pin |
| Governance = `agent-governance-scaffold` artifact set; vocabulary byte-identical | Observed | Both texts read this session; token-for-token comparison |
| Pack has no runtime-learner governance vocabulary (TB-1 gap) | Observed | grep over SKILL + `agent-governance-four-power-concepts-2026-07-17.md` — zero matches |
| All nine benchmark numbers + 12/12 tests | Observed (reproduced) | Run in `.venv` at the pin, 2026-09-21 |
| teaBrain governance is artifact-complete, not enforcement-wired | Observed | teaBrain's own status literal + no broker/verifier code present |
| teaBrain was generated *by* the pack (vs independently converged) | `[INFERENCE]` | Same author, byte-identical vocabulary and placeholders; not proven from a commit trail |
| "First downstream operationalization" | `[INFERENCE]` (bounded) | Bounded to the objects recorded across this survey series |
| Track A energy / M4 locomotion claims | Not verified — correctly unbuilt | No hardware, no MuJoCo run; deferred in the repo |

## Evidence Actually Checked

- Coordinator read in full: `intents.md`, `plans/00`,`plans/06`, `reviews/2026-09-21-panel-synthesis.md`,
  all four `governance/` files, `scripts/run-agent.sh`, and source cores
  `critic_learner.py`, `ring_attractor.py` — 2026-09-21.
- Scouts (read-only): plans 01–05 (PillarPlans); the three reviews (ReviewsExp);
  `teabrain/` + `bench/` + `tests/` mapping **and execution** (CodeVerify) — 2026-09-21.
- Executed: `pytest tests/ -q` (12 passed) and benches `run_baselines`, `train_skeleton`,
  `m2_sweep`, `p3_upgrade`, `p3_critic`, `r3_adapt`, `r4_persistence`, `r5_highdim`.
- TeaPrompt-side greps: `agent-governance-scaffold` SKILL + concepts doc (TB-1 gap),
  `workflow-recipes.md` §Parallel Lens Review, `falsifiability.md`; clean-room token check.
- Not done: Track A hardware, M4 flyGym/MuJoCo, the PyTorch tensor path (dep absent),
  `bench/harness.py`/`controllers.py`/`chemotaxis2d.py` line-audit beyond the scout map,
  and any claim that teaBrain was literally generated by the pack (inferred, not traced).

## Falsifiability

- The governance-identity claim is wrong if any cited teaBrain governance object
  diverges from the pack's artifact set or vocabulary — both texts are quoted and pinned.
- TB-1's gap is wrong if the pack SKILL or its concepts doc contains runtime-learner
  budget / reward-provenance / wireheading vocabulary — the guard greps for it.
- The reproduced numbers are wrong if a re-run at `27b4d25` prints different values;
  they are bounded to this pin and this NumPy build, and to simulation success rates.
- "First downstream operationalization" is bounded to the recorded surveys; a missed
  prior instance renumbers Finding 1 without changing the no-adoption conclusion.
- TB-3's "not fired" is wrong the moment a project wires the pack's broker/verifier
  and runs the mutation suite; that is its reopen condition.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Revision pinned; identity and clean tree recorded | done | this record; `git` at the pin |
| Concepts read (plans 01–06, intents, reviews, governance, source cores) | done | Method; What the Artifact Is; Concept Map |
| Experiments reproduced (12/12 tests + 9 benches) | done | Experiments Reproduced table |
| Twelve concepts mapped; six candidates decided with evidence and triggers | done | Concept Map; Candidate Adoption Ledger |
| Direction-scope rule applied: bare survey, nothing fired; TB-1 gap logged not landed | done | Research Question; Direct Recommendation |
| Clean-room boundary on installed surfaces | done | guard vocabulary test |
| Guard written | done | `plans/tests/test_teabrain_survey_record.py` |
| Decision Index row (at head), case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`; `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |
| Generic direction re-ran the six candidates; none fired; rows byte-unchanged | done | Direction Addendum |

## Direction Addendum (2026-09-21, generic direction)

Follow-up direction: "anything worth updated about docs or skills" — generic,
naming no survey family. Per the installed direction-scope rule it fires only this
survey's own candidates and no named hold elsewhere; a fired consideration trigger
authorizes a consideration, not a landing. All six candidates re-ran at the worth
bar with the direction present; none meets it, and the ledger rows above are
**byte-unchanged**:

- **TB-1** — the gap is real and re-verified this session (grep over the
  `agent-governance-scaffold` SKILL, its concepts doc, `reflective-risk`, and
  `04-agent/runtime-trust-boundary.md`: **zero** matches for reward-channel /
  wireheading / metric-drift / `freeze_plasticity` / `runtime_agent_budget` /
  online-learning vocabulary). But the destination is a **domain-scope expansion,
  not a defect**: the pack governs bounded external-effect *coding workers*;
  governing a *self-modifying / online-learning* agent is a different domain
  TeaPrompt does not serve (Standing Non-Goal: no runtime). Expanding a domain
  pack needs a registry decision plus three-cross-session recurrence plus explicit
  human approval; n=1 same-author usage and a generic direction supply none.
  Adopting the primitives on external elegance for an unserved domain is what §5
  Signal Accounting forbids.
- **TB-2** — no verified gap: the pack already teaches "emit only what the task
  needs" + Gate 2.0 risk-thickness sizing, and `reflective-minimality` teaches
  pay-cost-when-needed; the three-tier timeline is a domain application, so a
  sentence would restate installed guidance.
- **TB-3** — its reopen is fired by evidence (a wired enforcement host running the
  mutation suite), not by direction; teaBrain is artifact-complete, so it stays
  unfired.
- **TB-4 / TB-5 / TB-6** — corroboration / record-only / out-of-scope (no neural
  runtime); a generic direction does not convert corroboration into a landing.

A scope-clarification note ("this pack does not cover runtime weight-drift") was
also considered and rejected as defensive bloat: the pack's trigger and
compatibility already scope it to external-effect agents, and the note defends
against no named failure.

Direction outcome recorded so it is not re-litigated; the reopen triggers stand as
written.
