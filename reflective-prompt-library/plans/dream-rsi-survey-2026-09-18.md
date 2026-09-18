# Dream-RSI Survey — `zhengkid/Dream-RSI` / dream-rsi.com (2026-09-18)

> **Status: decided — one sentence adopted in a same-day follow-up under user direction (DR-5); otherwise record-only.** The object is a Google/Google DeepMind/UMD/UVA technical report (arXiv 2609.14858, resolving as of 2026-09-18 — published 2026-09-14; the repo badge still said "coming soon") plus a project site and a paper-only repository — README, PDF, figures, citation; "code is being prepared for release", **no LICENSE file**. Core claim: a completed discovery run's tree is an *exact* replay simulator over the realized search space, so thousands of candidate exploration policies can be scored off-policy at zero executions; the incumbent policy is always a candidate, so the selected revision is never worse *in average replay score on the recorded history*; each online lap appends another tree to the pool. Eight tasks across three domains; controlled baseline is Recursive Fixed Exploration (same agent, evaluator, budget; round 1 identical by construction). All claims are author-claimed — nothing executable exists to audit. Ten concepts mapped: the mechanism is a learning-loop architecture (non-goal), but its prompt-level echoes are already installed, and one finding — injected semantic guidance underperforms replay — is recorded as a bounded caution, landed same day as one sentence under user direction (DR-5; Adoption Addendum). Clean-room throughout; surveyed vocabulary is guarded out of installed surfaces.

## Research Question

User instruction: "Survey:" followed by three links (project site, PDF, GitHub). Two questions: (1) what does the report actually establish and at what evidence tier; (2) does any concept expose a verified gap on an installed TeaPrompt surface. A bare "survey" carries no adoption direction; the standing bar applied per candidate: a verified gap on one installed surface, a named failure the change defends against, a smaller alternative rejected, and a deterministic guard.

## Direct Recommendation (as of 2026-09-18)

- **Study: yes.** This is the cleanest statement yet of a principle TeaPrompt already practices at small scale: evaluate a proposed change against *recorded run evidence* before paying for a live run. Their version is a policy replayed over a discovery tree; ours is a template dry-run over a rig matrix and a router tuned only after holdout fixtures are recorded. Same shape, different substrate.
- **Reproduce: impossible today.** The repository ships no code, no tasks, no discovered programs (release plan: "being prepared"); there is no LICENSE. All numbers are author-claimed from the PDF.
- **Adopt: one sentence, in a same-day follow-up under user direction (DR-5; Adoption Addendum).** The mechanism is a learning-loop architecture — the same non-goal the RSIAgent survey recorded (run state is never project memory; TeaPrompt ships no learning loop). Its prompt-level echoes are installed. The one finding with a prompt-level edge — semantic guidance injected into prompts underperformed replay under equal budgets — is recorded as DR-5 — deferred at survey time because no installed surface injected such guidance; the same-day user direction landed it as a caution beside the existing consensus-amplification caution (Adoption Addendum).
- **Deploy: not applicable.** No code exists to deploy.
- **Scope corrections for citers:** (a) "the winner is never worse" holds for *average replay score on the fixed history* — the paper's own bound — not for online performance, which is stochastic; (b) "zero executions" means zero *discovery-agent* executions — the policy-development agent and its revision loop still cost model calls; (c) the repo has no license and the PDF's own footer reads "© 2026 Google. All rights reserved", so the paper and figures are all-rights-reserved despite the public posting.

## Method

Coordinator reads (2026-09-18): the project site in full; the technical report PDF (converted text, ~2,700 lines; method, experiments, analysis, related work, and appendix entry points read); the GitHub repository README, file tree, `CITATION.cff`, and API metadata (HEAD `4149ea9181ab1db80f85717ffda2c9f0f130e85b`, 2026-09-16T10:32:18Z; repo created 2026-09-13; 618 stars / 57 forks; license: none). No scouts: the corpus is three documents and the repo has no code to audit. No Parallel Lens panel: no wording was proposed for adoption and no TeaPrompt template was touched. Coverage check: installed surfaces grepped for the surveyed vocabulary; the RSIAgent survey record re-read for the learning-loop non-goal precedent.

**Scope / acceptance:** verify the site's claims against the PDF; map the concept set against installed surfaces; decide every candidate with evidence and a trigger; land nothing without a verified gap; keep the clean-room boundary; run `make all` from the repository root.

## What the Artifact Is

A technical report and site describing an orchestration layer that makes exploration *executable policy code* — branching, parallel batches, stopping — over a fixed coding agent and fixed evaluator. The loop: (1) the current policy drives an online discovery rollout that logs a tree of attempts (each node: workspace snapshot, artifact, score, diagnostics); (2) the tree joins a history pool as a replay world; (3) a policy-development agent writes M successive revisions of the policy code, each scored by deterministic replay over every recorded tree — the policy sees only revealed nodes, never unrevealed outcomes — and the argmax revision deploys next lap. Replay score = best node quality − β₁·(attempts) + β₂·(parallelism bonus). Because π⁰ = the incumbent is always in the candidate set, the selected policy is never worse *in replay score on the recorded history*.

Reported results (author-claimed): Lasso path solver — 317 vs 550 calls (Gemini-3.1-Pro) and 1879 vs 3200 (Gemini-3.7-Flash) against the fixed-exploration baseline at better held-out runtime; ~162× fewer calls than SimpleTES's 51,200-generation budget; math optimization — matches or beats baselines within 1k generations on two of three tasks (SimpleTES's autocorrelation number stands, at 51,200 generations, and there Dream-RSI also trails its own fixed baseline, 1.456375 vs 1.456001; the repo's own stats banner counts "2 of 3 tasks at or above the selected baseline"); KernelBench — 1.79×–2.43× fewer generations at comparable performance, or 1.44×–2.09× better at comparable budget. Analysis: the learned policy is adaptive, not monotonic (cuts attempts 110→50 while improving, re-widens at plateaus); **injected semantic guidance consistently underperformed unguided runs under equal budgets** — strong directional priors over-constrain parallel exploration.

## Concept Map

Tier is `prose` throughout — the repository ships no code; every mechanism is paper-described.

| ID | Concept (clean-room) | Source tier | TeaPrompt coverage | Disposition |
| --- | --- | --- | --- | --- |
| C1 | Recorded run history as an exact replay substrate: evaluate a candidate change against stored outcomes before paying for a live run | prose (paper §2–3) | Template dry-run rigs over recorded forms; ROUTING_CONTRACT R8 holdout-before-tune (fixtures recorded before any tune); mutation checks on prior bytes | No change — installed at prompt scale |
| C2 | Incumbent always in the candidate set → selected revision never worse on the recorded metric | prose (paper §3, argmax over M including π⁰) | Adoption ledger's `no change` disposition is always a scored candidate; a landed change must beat keeping the bytes | No change — installed |
| C3 | Growing pool of recorded worlds; evaluate across all of them, not the latest | prose (history pool ℋₜ) | Rig matrices span forms (trailing slash, absolute, outside-git, subdir); guards re-run against *prior* revisions (`9a756e5`, `be0d16e`), not just HEAD | No change — installed |
| C4 | Cost-aware objective: quality minus attempts plus parallelism bonus | prose (Eq. 1) | Pack size budgets, lint thresholds, zero-sum offsets; no scored objective exists — different substrate | No change — non-goal (no metric to optimize) |
| C5 | Reveal-only-what-was-earned: the policy sees revealed nodes, never unrevealed outcomes | prose (paper §3) | Holdout discipline: tune never sees holdout phrases; sealed-oracle split in governed-delivery | No change — installed |
| C6 | **Injected semantic guidance underperforms replay** — distilled directional priors over-constrain parallel exploration | prose + one figure (§5.1, ConvDiv, both paradigms) | none at survey time — no TeaPrompt surface injects directional guidance into exploration prompts | Adopted same day (DR-5) |
| C7 | Adaptive effort: conserve compute while improving, re-spend at plateaus | prose (§5.2) | Strictness ladder (escalate only when risk/ambiguity demands); no adaptive-budget mechanism | No change — installed in spirit |
| C8 | Orchestration layer makes exploration programmable; the underlying agent is unchanged | prose | The two flow packs exactly: host-agnostic templates over an unchanged agent | No change — installed |
| C9 | Controlled baseline shares round 1 by construction; held-out downstream eval | prose (§4) | Holdout-before-tune; "every figure bound to its measured revision" | No change — installed |
| C10 | Meta-level RSI loop: policy code revised by an agent against replay feedback | prose | none — learning-loop architecture | No change — non-goal (RS-6 precedent) |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| DR-1 | "Evaluate against recorded run evidence before a live run" as a stated principle | No change 2026-09-18 | Installed as behavior: dry-run rigs, holdout-before-tune, mutation checks on prior bytes; a sentence would restate them | None |
| DR-2 | Incumbent-in-candidate-set rule for adoption decisions | No change 2026-09-18 | `no change` is a standing ledger disposition; every adoption must beat it | None |
| DR-3 | Multi-world evaluation (all recorded forms, not the latest) | No change 2026-09-18 | Rig matrices + guards pinned to prior revisions; the 2026-09-16 rig-matrix lesson already generalizes it | None |
| DR-4 | Cost-aware scoring objective | No change 2026-09-18 | No metric exists to optimize; budgets are constraints, not an objective | Reopen only if TeaPrompt ever scores changes on a numeric objective |
| DR-5 | Caution: distilled directional guidance injected into exploration prompts can underperform unguided runs (their §5.1, one task, both paradigms, equal budgets) | Adopted 2026-09-18 (same-day user direction) | No installed surface injected such guidance at survey time (grep re-verified before landing: no directional/distilled/steer coverage in `04-agent/` or the flow packs); the finding is one figure on one task — the sentence carries that bound. Landed verbatim on `04-agent/workflow-recipes.md` beside the consensus-amplification caution: "Directional guidance distilled from prior runs can shrink the space a parallel exploration actually searches; prefer replayable evidence over advice when the budget is parallel." | Retire if the caution leaves `04-agent/workflow-recipes.md`; revisit if broader evidence overturns the single-task finding |
| DR-6 | Adaptive-effort policy (spend less while winning, more at plateaus) | No change 2026-09-18 | Strictness ladder covers the escalation direction; the conserve direction needs a measured signal TeaPrompt doesn't collect | None |
| DR-7 | Programmable exploration layer over an unchanged agent | No change 2026-09-18 | The flow packs are exactly this | None |
| DR-8 | Record correction: "never worse" is bounded to replay score on recorded history | Corrected 2026-09-18 (record-only) | Paper §3: argmax over average replay score on ℋₜ; online transitions are stochastic, so the bound does not transfer to live performance | — |
| DR-9 | Record correction: "zero executions" excludes the policy-development agent's own cost | Corrected 2026-09-18 (record-only) | Paper §3: M revisions × t replay worlds are free of *discovery-agent* calls; the development agent still reads trajectories and writes code each lap | — |
| DR-10 | Learning-loop architecture (meta-policy revised by an agent across laps) | No change 2026-09-18 | RS-6 precedent: TeaPrompt ships no learning loop; run state is never project memory | Reopen only if TeaPrompt's scope changes |

Deterministic guard: `plans/tests/test_dream_rsi_survey_record.py` (identity, dispositions, corrections, clean-room boundary, index links).

## Shared Findings

1. **The second RSI-flavored survey in three days, same verdict shape.** RSIAgent (training-free self-improvement harness) and Dream-RSI (meta-exploration RSI) are both learning-loop architectures; both times the mechanism is a non-goal and the transferable residue is a discipline TeaPrompt already has. The family resemblance is now a pattern worth one line in the case-studies table, not a skill.
2. **"Exact simulator" is the honest version of what rigs approximate.** Their replay is exact because it *is* the recorded space; TeaPrompt's dry-run rigs are approximate by construction — which is exactly why the rig-matrix lesson (a matrix bounds the forms in it, not the form space) keeps recurring. The paper is a useful citation for why recorded-evidence evaluation beats live trial, not a mechanism to copy.
3. **The semantic-guidance result cuts against a plausible TeaPrompt instinct.** If anyone proposes "distill what worked into the next exploration prompt," this paper is the counter-evidence: under equal budgets, guidance hurt in both paradigms on the measured task. Bounded — one task, one figure — but it is the only surveyed claim with a live prompt-level edge, hence DR-5's reserved wording.
4. **Disclosure quality is mixed.** Strengths: controlled baseline shares round 1 by construction, held-out downstream datasets, the "never worse" bound is stated precisely in the method (then loosened on the site), SimpleTES's reproduction is marked †. Weaknesses: no code, no license, no tasks, no discovered programs yet; "zero executions" elides the development agent's cost; arXiv badge says "coming soon" while `CITATION.cff` already prints an identifier (the identifier resolves — the badge is stale).
5. **The adaptive-effort trace is the interesting empirical detail.** Attempts fell 110→50 while round-best score rose, then re-widened at plateaus — the policy learned the strictness-ladder shape on its own. TeaPrompt's ladder is hand-written; this is evidence the shape is right, not that it should be learned.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Repo identity, HEAD `4149ea9`, dates, stars, absence of LICENSE and code | Observed | GitHub API + file tree, accessed 2026-09-18 |
| Site contents, figure captions, headline numbers | Observed | dream-rsi.com read in full 2026-09-18 |
| Method (tree, replay, objective, incumbent guarantee, reveal rule) | Observed (paper text) | PDF §2–3, read 2026-09-18 |
| All benchmark numbers; the guidance-underperforms finding; the adaptive-effort trace | Author-claimed | PDF §4–5; nothing executable exists to audit |
| arXiv identifier 2609.14858 | Observed | arXiv abstract fetched 2026-09-18 (same-day review): published 2026-09-14, title and authors match the PDF; the repo badge still said "coming soon" at the pinned read |
| Mechanism-to-TeaPrompt analogy (replay ≈ dry-run rigs) | `[INFERENCE]` | Structural comparison; different substrates |
| No installed surface carries the surveyed vocabulary | Observed | `test_survey_vocabulary_stays_out_of_installed_surfaces` |

## Evidence Actually Checked

- GitHub API: repo metadata, `commits` (HEAD `4149ea9…`), file tree, README, `CITATION.cff` — 2026-09-18.
- dream-rsi.com in full — 2026-09-18.
- `assets/dream-rsi.pdf` converted text: §1–3 and §5–7 read in full; §4's results read via the PDF's results lines plus the site's full tables (identical figures); appendix solver code skimmed for existence — 2026-09-18.
- Installed surfaces grepped for surveyed vocabulary; RSIAgent record re-read for the RS-6 precedent — 2026-09-18.
- Not executed: nothing exists to execute; no clone.

## Falsifiability

- The "no sentence needed" mapping is wrong if an installed skill is later shown to lack a rule the Concept Map credits to it (coverage rows name the surfaces; re-grep them).
- DR-5's adoption is wrong if the caution suppresses legitimate task decomposition (a disjoint slice is not directional guidance — the landed sentence distinguishes them) or if broader evidence overturns the single-task finding; the ledger row names the retire condition.
- The author-claimed results stand or fall with the promised code release; the release plan is the tracking point.
- The "family resemblance" finding is wrong if a future RSI-flavored survey produces a verified gap on an installed surface — the ledger pattern is ready for it either way.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| All three cited sources read; artifact pinned (`4149ea9`); license absence recorded | done | this record |
| Site claims checked against the PDF; three scope corrections recorded | done | Direct Recommendation, DR-8/DR-9 |
| Ten concepts mapped with tier and coverage | done | Concept Map |
| Ten candidates decided with evidence and triggers | done | Candidate Adoption Ledger, dispositions guarded |
| Clean-room boundary on installed surfaces | done | `test_survey_vocabulary_stays_out_of_installed_surfaces` |
| Guard written | done | `plans/tests/test_dream_rsi_survey_record.py` |
| Decision Index row, case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`, `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |

## Review Addendum (2026-09-18, same day)

A four-lens review panel was attempted twice (scout and task backends); all eight assignments died on provider quota with zero assistant turns, so this review is coordinator-executed — **no independent lens verdicts exist**. Findings fixed: the repository pin upgraded to the full 40-hex sha (house convention); the arXiv identifier now verified against the live listing (published 2026-09-14 — the repo badge, not the ID, was stale); the math-optimization transcription now carries the source's own "2 of 3" qualifier and the fixed-baseline comparison on autocorrelation; the PDF-coverage line in Evidence Actually Checked tightened to what was actually read in full versus via results lines and the site's tables; the license correction now cites the PDF's own all-rights-reserved footer. Guard probes: the ledger regex captures the Status cell on all ten rows; status-flip, date-deletion, and row-deletion mutations are all caught.

## Adoption Addendum (2026-09-18, same day, user direction)

The user's follow-up ("consider update skills that inspired by dream-rsi and jev/decision concepts") supplied the adoption direction a bare survey lacks, firing DR-5's gate. The gap was re-verified before landing: no sentence in `04-agent/` or either flow pack addressed seeding parallel workers with distilled directional priors (the packet contract's frame test governs the *questions'* frame; the decorrelation practice lived only in session records). The reserved sentence landed verbatim in the pattern-table caution stanza of `04-agent/workflow-recipes.md`, beside the consensus-amplification caution — the same external-evidence-to-one-sentence move that stanza already made — with its single-task evidence bound stated and no surveyed vocabulary (the guard's clean-room check covers the surface). The guard flipped from wording-absent to pinned-once. The other nine dispositions were re-read under the direction and stand: the learning-loop mechanisms stay non-goals; the decision-model side of the same direction stays unadopted (margin/calibration are self-report, the forbidden gate class; close-call escalation is installed at the workflow-recipes Confidence row and the panel dissent rule). GE-1 is untouched — the direction names these two surveys only.
