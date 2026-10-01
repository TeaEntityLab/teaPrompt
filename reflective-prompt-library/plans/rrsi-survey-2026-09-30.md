# RRSI Survey — `google-research/rrsi` (2026-09-30)

> **Status: decided — all twelve upstream candidates record-only or no-change; no RRSI mechanism adopted into a skill or runtime.**
> The object is a harness-evolution research codebase (search loop + three domain adapters + benchmarks),
> not a prompt library. Its regularizers are benchmark-search controls for an evolve-measured loop TeaPrompt
> does not run. The transferable distinctions (noise vs signal, missing vs zero, repeatedly-selected
> validation vs fresh final data, task-domain tradeoff vs safety) are already covered at contract level or
> recorded in ECT-2/ECT-4; the exact formulas stay study material. The separate local recipe repair is AF841-M1.

## Research Question

User live wording (preserved verbatim in intent): "Fix advisor notes; Survey agfnow/agentflow v8.4.1;
Survey https://github.com/google-research/rrsi; and if worth it then update docs or skills."
Sources checked 2026-09-30. This record assesses RRSI under the conditional update direction: a landing needs a verified local
structural gap, a named failure, a smaller alternative rejected, and a guard at the owning surface.
Record/no-change below is justified by existing coverage or host-only mechanisms, never by lack of
authorization. The STS banner repair and the local recipe seal-attribution repair are separate from RRSI
mechanism adoption; the latter is recorded as AF841-M1 in the Agentflow survey.

What does Regularized Recursive Self-Improvement actually change (frozen policy vs harness, proposal budget /
history / exploration, critic screen, scoring denominator, noise / cost / within-band / novelty selection,
domain guards, pruning, worktree lifecycle), at what evidence tier, and does any of it expose a verified gap
on an installed TeaPrompt surface?

## Direct Recommendation (as of 2026-09-30)

- **Study: yes.** A worked example of regularizing an adaptive harness search rather than restricting the
  harness: open edit space, constrained trajectory. The paper's L0/L1/L2 language is an explicitly qualitative
  analogy (Appendix C), not a norm-penalized objective — cite it as analogy only.
- **Benchmark replication: not undertaken.** Full runs need Claude Opus 4.8 on Vertex AI (proposer, analyst, critic,
  frozen policy), Docker + harbor (coding), a Harvey LAB checkout at a pinned commit plus judge models
  (workspace), and EngDesign bench + gateway + grading venv (eng). Nothing benchmark- or provider-backed ran here.
- **Adopt: nothing.** Twelve RRSI-* candidates decided below: seven no-change (covered or host-only or
  non-goal), five record-only (RRSI-5, -6 and -11 explicitly ECT-adjacent; RRSI-10 is a benchmark
  missing-data distinction and RRSI-12 a transfer-tradeoff clarification, neither ECT-adjacent; the exact RRSI
  formula is not a TeaPrompt sentence). No verified local declared-contract defect was found by this slice.
- **Deploy: not applicable.** A benchmark search loop, not a tool one runs on TeaPrompt work.
- **Scope corrections for citers (load-bearing):**
  (a) regularization trades evolve-set points for transfer points — a measured task-domain tradeoff, not safety;
  (b) the critic's leakage screen is benchmark integrity (don't score a memorizer), not a safety boundary and not
  generalization proof; (c) evolve scores are repeatedly-selected validation, not fresh final data — only the
  held-out/OOD arms (never entering selection) support transfer claims; (d) missing-trial-0 is a benchmark
  pass-rate convention paired with an explicit invalid-missing gate and retry/reevaluate path, not a general
  missing-data rule — an unscored TeaPrompt ledger entry stays unknown, never zero.

## Source Identity and Version / Date Context

| Item | Value (checked 2026-09-30) |
| --- | --- |
| Repository | `google-research/rrsi`, public, Python; stars 966 / forks 79 / issues 4 at read time (volatile; tracking point = live GitHub counts) |
| Main pin (this survey) | `be50316e1db05914068a973f322770ef08ed7ba1`, commit date 2026-09-23T22:16:24Z, message "Fix date format and enhance README clarity" (README-only diff vs parent `e4d1a7a`), tree `530e3127`, verified signature; GitHub API read 2026-09-30 |
| Root license | Apache-2.0 — `LICENSE` at pin verified (Apache License, Version 2.0, January 2004, full text); README §License: "Apache 2.0; see LICENSE. Third-party code under `third_party/` carries its own license." |
| Third-party boundary | `third_party/archipelago/LICENSE` (blob `d645695`, Apache-2.0 text) and `third_party/harbor_terminus2/LICENSE` (blob `261eeb9`, Apache-2.0 text) each carry their own license at the pin; starting harnesses are Terminus-2 (harbor fork) and react_toolbelt (archipelago vendored) per README Acknowledgements |
| Paper | arXiv 2609.24972; abstract lists publication on 2026-09-21; versioned PDF `2609.24972v2`, §§1–6 + Appendices A–E read via converted text; checked 2026-09-30 |
| Project page | https://regularized-rsi.com/ read 2026-09-30 (+4.0 evolve avg, +3.4 held-out avg, −36% policy tokens per trial vs unregularized; headline does not specify a domain; author-claimed) |
| Config pins at main pin | `domains/coding/rrsi.json` delta 0.017; `domains/workspace/rrsi.json` delta 0.004; `domains/eng/rrsi.json` delta 0.020; T 20/20/40, k 2/2/4, m 2, b 4→1 / 3→1 / 4→1, w 3, m_draft 1, repair_rounds 5 |
| Tracking points | release movement (post-pin commits), paper v3+, promised round-by-round trajectory explorer data, Harvey LAB / EngDesign upstream layouts |

## Method

Coordinator reads at the pin (no scouts; corpus is one repo + paper + site): README in full; `rrsi/`
`selection.py`, `evaluate.py`, `critic.py`, `history.py`, `components.py`, `schedule.py`, `calibrate.py`,
`config.py`, `domain.py`, `gitops.py`, `loop.py` (incl. `_draft`/`_evaluate`/`readjudicate`/`reevaluate` tails),
`propose.py` (system template, `Workspace`, `done()` contract), `analyst.py`/`llm.py` headers (provider-backed,
not executed); domain adapters (coding/workspace/eng scoring, guards, smoke, critic patterns), all three
`rrsi.json` files, `tests/test_core.py`; paper §§2–4 + Appendices A–E; project page; license files and
third-party listing. Coverage map: installed skills grepped (`governed-delivery`, `reflective-implement`,
`reflective-minimality`, `reflective-research`/`reflective-review`, `flow-loop-harness`,
`flow-control-generator`, `04-agent/workflow-recipes.md`, `plans/ROUTING_CONTRACT.md`) plus the ECT-2/ECT-4,
RS-4/FM3/JL-9/DR-5, XM-3/XM-12 rows re-read. Search caveat: `find` returns HTTP 403 on every judge with a
misleading no-hits message (parent-reported, not re-run); known-path direct reads and literal `grep` supplied
all evidence — no absence inferred from the failed search.

## What the Artifact Is

An agent = frozen policy π + harness H (prompts, control flow, tools, skills, memory, context management).
RRSI evolves H with π frozen (Claude Opus 4.8 everywhere in the main runs; Gemini 3.5 Flash coding arm
separately). Each round: analyst writes three-lens feedback F_t from the incumbent's own evolve evaluation;
annealed budget b_t caps bundled edits; stall/untried/prune directives shape the draw; m=2 candidates are
drafted in isolated git worktrees, critic-screened with bounded repair, smoke-checked, evaluated on the full
evolve set (k trials/task), then judged admissible-or-not with argmax-or-incumbent selection; the winner
fast-forwards `evolve/<domain>`. Edit history L_t records every measured edit (component, hypothesis, diff,
ΔS, ΔC, accepted); unmeasured drops (critic reject, smoke fail, invalid eval) are recorded with
`delta_S = None` and excluded from tried/yield statistics. One method, three instances: coding
(Terminal-Bench 2.1 evolve → SWE-bench Verified OOD), workspace (Harvey LAB 120 evolve + 40 pristine held-out
→ JobBench/GDPval/APEX-Agents OOD), eng (EngDesign-Open 61 evolve, no ID held-out → Frontier-Eng OOD).

## Mechanism Map (code-verified at the pin)

| # | Mechanism | Paper | Code (pin) | Observed behavior |
| --- | --- | --- | --- | --- |
| M1 | Open edit space, regularized trajectory; K = prompt, control_flow, config, output_plumbing, context_mgmt, client_tool, skill, memory, subagent; K_str = client_tool, skill, memory, subagent | §3.1, C.1–C.2 | `components.py` K/K_STR; `propose.py` SYSTEM_TMPL permits only scaffold edits and describes the policy as frozen and "DIFFERENT"; paper §4.1 uses Claude Opus 4.8 for policy, proposer, analyst and critic | Template wording verified, not distinct-backbone enforcement; role separation does not establish model independence |
| M2 | Annealed L0-style edit budget b_t = ceil(b_min + (b_max−b_min)·½(1+cos(πt/T))); bounds \|\|z_t\|\|_0 per candidate only | Eq. 4, C.2 | `schedule.py:edit_budget` (+ float guard at t=T); `loop.py` computes per round; `propose.py` `done()` contract bounces over-budget/untagged | Smoke: budget_table(20,1,4) matches independent recomputation; edit_budget(T)=b_min |
| M3 | Evidence-aware credit: L_t per-edit records; proposer conditioned on full history + attribution scoreboard (predicted_affected hit/miss, unpredicted regressions); falsified hypotheses are negative evidence | §3.2, C.2 | `history.py:append_candidate/render` (render caps unmeasured wall at 4); `loop.py:attribute/scoreboard`; `propose.py` context assembly | Smoke: unmeasured critic-rejected config excluded from `tried()`; render cap holds |
| M4 | Structured exploration: σ_t = 1[S_t − S_{t−w} ≤ δ]; U_t = K\T_t; m_draft reserved slots for never-exercised components when stalled | Eq. explore, C.2 | `history.py:stall_flag/exploration`; `loop.py` reserved = σ ∧ untried ∧ variant-slot; re-tag from diff can still fail a reserved slot | Smoke: windowed stall flags + RESERVED text verified |
| M5 | Critic leakage screen BEFORE evaluation: generic denylist + domain regex patterns + Claude Opus 4.8 intent review; bounded repair (repair_rounds=5); unrepairable → dropped, recorded without measurement | §3.3, Alg. 1 | `critic.py:precheck/review` (3 parse attempts then reject); `loop.py:_draft` critic→repair loop; domain `critic_patterns` (coding task-name-per-task regexes; workspace task/world ids + judge refs; eng grader/toolchain/network/task-id patterns) | Smoke (deterministic layer only): task.json hit rejected, clean prompt diff passes, credential pattern hits; LLM layer not invoked |
| M6 | Empirical score/cost: Ŝ = Σrw/Σw; Ĉ averages positive observed token counts only; missing trial r=0 with FULL reward denominator, weights respected (Harvey criterion weighting) | Eq. 3, App. A | `evaluate.py:aggregate/TaskResult/EvalResult`; adapters supply reward zeros; `None`/nonpositive tokens excluded, all absent → C=None | Smoke: 2-task aggregate S=0.5 with full n_expected; token-None skipped; empty population → 0; missing cost is not a missing-reward count |
| M7 | Missingness convention vs infrastructure gate (no contradiction): zero is the benchmark scoring rule; `invalid_missing_frac` (0.2/0.1/0.15) invalidates baseline/candidate evals; harbor partial jobs renamed `*.stale.*` and re-run; `reevaluate` + `readjudicate` commands exist | App. A.6/A.8, loop baseline/_evaluate | `loop.py:baseline` SystemExit when missing > frac; `_evaluate` one retry then `eval_invalid`; coding `_harbor` stale-dir rule; `readjudicate` re-applies Alg. 2 on stored measurements only | Code-read; not executed (needs Docker/harbor + benchmarks) |
| M8 | Noise-adjusted floor: admissible only if S′ ≥ S* − δ; δ fixed per instance (0.017 ≈ 3/178 passes; 0.004 ≈ 60/~14,100 criteria; 0.020 ≈ 5/244 passes) or calibrated (`calibrate.py`: repeated base evals preferred, else bootstrap over trials, δ = z·sd, z=2) | Eq. 5, §3.3, D.1 | `selection.py:judge` floor check; `calibrate.py:bootstrap_se/pooled/calibrate` | Smoke: 0.30 vs S*=0.55/δ=0.05 rejected with "floor" reason; bootstrap δ>0 on synthetic evals |
| M9 | Cost rule above band (ΔS>δ): ΔC ≤ β0+β1ΔS; within band: w_sΔS − w_cΔC + w_nν > 0; coding w_s=0; ν counts touched structural types with zero accepted edits, an admission term rather than an exact-score tie-break | Eq. 7/17, C.3 | `selection.py:cost_rule/judge/select_round`; `relative_cost_change` returns 0 when either cost is absent; per-instance weights in `rrsi.json` | Initial smoke: expensive gainer blocked, cheaper-neutral admitted, costlier-neutral rejected; supplemental probe: missing-cost gainer and slightly lower-score novel candidate admitted |
| M10 | Non-compensatory domain guards after cost checks: coding/workspace none (g=1); eng rejects valid-rate drop >0.03 or no-payload rise >0.02 | §3.3, C.3 | `domain.py:guards` default []; eng `adapter.py:guards`; `selection.py` guard veto | Smoke: guard_fn veto blocks an admitted gainer with "guard" reason |
| M11 | Pruning: B_t = {ℓ ∈ T_t : g_t(ℓ) ≤ 0} over window n_prune; proposer receives B_t with accepted machinery to remove | Eq. prune, §3.3 | `history.py:yield_g/prune_set/accepted_edits/incumbent_component_counts` | Smoke: all-exercised-no-recent-gain components listed with carried machinery |
| M12 | Worktree lifecycle: branch `<domain>/r<t><variant>` off incumbent; `diff_with_new_files` (incl. untracked); tag `normalize` re-tags mislabeled edits from diff evidence; compile/ctor/smoke gate; parallel evaluate; argmax-or-incumbent; fast-forward `evolve/<domain>` only if descendant; harness-tree hash in frontier; resume-safe jobs | §3, loop docstring, gitops docstring | `gitops.py` worktree_add/remove, commit_path, fast_forward (merge-base check), tree_hash; `loop.py:_draft/_evaluate/round/readjudicate/reevaluate` | Code-read; git lifecycle not executed here (no repo mutation per contract) |
| M13 | Data separation: evolve = repeatedly-selected validation (adaptive reuse, paper §2); workspace 40-task held-out pristine; OOD suites never scored during search; H_0 and each arm measured in the same window/tooling/judge/trials | §4.1, App. A | `adapter.py` evolve_ids/heldout_ids/smoke_ids; workspace split generated deterministically from Harvey checkout; eng heldout empty (scripts cover OOD); Frontier-Eng overlap/unbuildable exclusions symmetric across arms | Code + paper-read; split generation and OOD scripts not executed |

Selection boundaries: the source's "tie-break" terminology means the noise-band admission rule, not only
equal scores or a novelty-ranked argmax. A candidate can replace the incumbent at a slightly lower score
while above S*−δ. Separately, missing token measurements become ΔC=0, not `eval_invalid`; the `_evaluate`
missing-fraction gate checks missing reward trials, not token coverage. Neither behavior proves that an
actual published benchmark run had missing costs. The supplemental probe below exercises both conditions.

## Reported Performance (author-claimed; NOT replicated)

README table (Claude Opus 4.8 frozen policy, each number vs unevolved H_0 in the same window):
coding TB2.1 evolve 74.2→80.2 (+6.0), SWE-bench OOD 82.0→83.8 (+1.8); workspace Harvey evolve 89.4→90.5
(+1.1), ID held-out 86.9→89.2 (+2.3), JobBench 36.0→40.7 (+4.7), GDPval 48.8→52.3 (+3.5), APEX 34.2→37.9
(+3.7); eng EngDesign evolve 50.0→54.9 (+4.9), Frontier-Eng OOD 17.7→22.0 (+4.3). Gemini 3.5 Flash coding arm:
64.6→78.7 evolve (+14.1), 76.8→79.0 OOD (+2.2). Cross-backbone (Flash-evolved harness under Flash Lite):
11.2→14.6. Baselines (same H_0/evolve/budget): Meta-Harness strongest on evolve, +0.9 OOD avg; HarnessX ≈ base;
AHE/TTHE finish at/below H_0 OOD. Ablations: w/o acceptance 91.5 evolve / 41.0 OOD / 3.59M tokens; w/o proposal
90.7 / 41.9 / 2.69M; unregularized 92.8 / 40.3 / 3.80M; RRSI 90.5 / 89.2 ID / 43.6 OOD / 2.42M vs H_0 89.4 /
86.9 / 39.7 / 1.56M (workspace). Site: +4.0 evolve avg, +3.4 held-out avg, −36% policy tokens per trial vs unregularized.
Sample/grading limits: k=2 (coding/workspace), k=4 (eng); m=2; T=20/20/40; Harvey-family judging is
model-mediated (Flash judge; JobBench Flash+Opus avg; GDPval 3-judge majority with position swap), coding/eng
grading is deterministic (hidden tests, frozen simulators); Frontier-Eng 38/47 tasks contribute symmetrically.
Evidence tier: existence + number/text verified against paper/site/code; attribution/process = vendor
self-reported counts with no result-file audit here; extrapolation beyond the 8 suites is unsupported.

Token-saving scope: the abstract says **30% fewer policy tokens** than unregularized evolution without
specifying aggregation or domain there; the site headline says **−36%** without naming a domain. Paper
§4.3 Table 2 gives **2.42M vs 3.80M tokens/trial for the agentic-workspace comparison**, about 36.3% lower;
this supports that bounded comparison, not a cross-domain saving. Its 2.42M remains above unevolved H_0's
1.56M. The cause of the 30%/36% difference is not established by the checked sources; retain both scopes
rather than silently reconcile them. All figures remain author-claimed, not independently replicated.

## Evidence Actually Checked

- GitHub API: repo metadata + pin commit object (`be50316e`, 2026-09-23T22:16:24Z, README-only patch shown) — 2026-09-30.
- Full reads at pin: README; `rrsi/` selection, evaluate, critic, history, components, schedule, calibrate, config, domain, gitops, loop (incl. round tail, `_draft`, `_evaluate`, `readjudicate`, `reevaluate`), propose (system template, Workspace jail, `done()` contract), analyst/llm headers; `tests/test_core.py`; coding/workspace/eng adapters (scoring, guards, smoke, critic patterns); all three `rrsi.json`; LICENSE + both third-party LICENSE directory entries.
- Paper: abstract + §§1–6 + Appendices A–E (method, baselines, hyperparameters Table 5, qualitative Table 6, references); site front page + BibTeX.
- Installed surfaces: literal grep over governed-delivery, reflective-implement/minimality/research/review, flow packs, `04-agent/workflow-recipes.md`, ROUTING_CONTRACT, plus ECT-2/ECT-4, RS-4/FM3/JL-9/DR-5, XM-3/XM-12 rows re-read.
- Offline smoke: real pinned modules executed in sandbox (section below). Not executed: any provider call (proposer/analyst/critic LLM), Docker/harbor, Harvey/EngDesign benches, OOD scripts, split generation, git worktree lifecycle, upstream tests.
- A reported unavailable check is not a negative result: unrun provider/benchmark paths bound the smoke, not the source.

## Offline Smoke (observed runtime evidence)

Fetched 13 pinned modules (`__init__`, selection, evaluate, history, components, schedule, calibrate,
config, critic, llm, propose, gitops, domain) via curl from `raw.githubusercontent.com/.../be50316e` into
owned scratch `/tmp/rrsi-smoke-Ku3IM5/src/rrsi` (sha256 recorded in run output; no install).
Probe `/tmp/rrsi-smoke-Ku3IM5/work/probe.py` (owned, disposable) imports the real modules and runs 34 checks.

- Isolation: `env -i PATH=/usr/bin:/bin HOME=<scratch>/home TMPDIR=<scratch>/work sandbox-exec -f
  sandbox.sb /usr/bin/python3 probe.py`; profile `(version 1)(allow default)(deny network*)(deny file-write*)
  (allow file-write* subpath <scratch> + /private/tmp variant)(deny file-read* /Users, /private/Users)`.
  No credentials inherited; writes confined to scratch; no upstream or shared checkout mutated.
- Boundary control (separate probe, exit 0): `/Users` read → DENIED PermissionError; TCP connect →
  DENIED; write outside scratch → DENIED; write inside scratch → ALLOWED. Network denial is sandbox
  enforcement, not proof of source behavior.
- Result: **34/34 PASS, exit 0** (`/usr/bin/python3` 3.9.6). Coverage: schedule table vs independent
  formula recomputation (positive control) + monotonicity + `edit_budget(T)=b_min` clamp; aggregate missing=0
  full-denominator + token-None skipping + empty-population adversarial + cost-None case; selection argmax,
  floor rejection wording, gate-failure propagation, expensive-gainer cost block, guard veto, within-band
  cheaper-admit / costlier-reject / novelty-tiebreak; history unmeasured-exclusion, best-recent yield,
  prune-with-machinery, render unmeasured-wall cap, windowed stall flags, RESERVED exploration text;
  components mislabel-fallback / evidenced-keep / bogus-recovery / text-only-prompt / novelty counting /
  vocabulary sizes (9, 4 structural); calibrate bootstrap δ>0 + empty-input ValueError (adversarial);
  critic precheck leak-hit / clean-pass / credential-pattern.
- Two first-run failures were probe bugs, not source bugs: (1) probe asserted `budget_table(T-1)==b_min`
  but the schedule only clamps at `edit_budget(T)` — corrected to assert the clamp; (2) `tempfile` needed the
  `/private/tmp` write variant — profile widened within scratch only. Recorded here so the table is not misread.
- What this proves: the pure selection/evaluation/history/tagging/calibration/precheck control flow at the pin
  behaves as documented, including adversarial/error boundaries. What it does not prove: benchmark efficacy,
  transfer, cost savings, critic LLM judgment, or any provider/Docker path — those need the unavailable
  full-run prerequisites (Vertex credentials, harbor/Docker, Harvey + EngDesign checkouts, judge models).
- Interpreter boundary: the repository declares Python ≥3.10, while this pure smoke used 3.9.6.
  Successful module-level control flow is not evidence for a supported install or complete runtime.

### Supplemental selector boundary probe

Integration exercised the real pinned `aggregate` → `select_round` path with synthetic measurements and
the actual workspace selection constants (δ=0.004, β0=0.10, β1=35.4, w_s=1414, w_c=15, w_n=0.5).
Four complete modules (`__init__`, components, evaluate, selection) were fetched at `be50316e` into owned
scratch `/private/tmp/teaprompt-rrsi-selection-Q2XceG`; SHA-256s and results were saved in
`local://rrsi-selection-boundary-smoke.json`. No extracted-function reimplementation or provider stub ran.

| Synthetic input; incumbent S=0.5, S*=0.5 | Observed selector result |
| --- | --- |
| Candidate S=0.6, C=10000; incumbent C=100 | Rejected: ΔC=99 exceeds budget 3.640 |
| Same candidate score, C=None; incumbent C=100 | Admitted: ΔC=0 |
| Candidate S=0.6, C=10000; incumbent C=None | Admitted: ΔC=0 |
| Candidate S=0.4999, C=100, new memory component; incumbent C=100 | Admitted: ν=1, shaped=+0.3586, still above floor 0.496 |
| Same lower score/cost, prompt component instead | Rejected: ν=0, shaped=−0.1414 |

Command: `env -i PATH=/usr/bin:/bin HOME=<scratch>/work TMPDIR=<scratch>/work sandbox-exec -f
sandbox.sb /usr/bin/python3 -B <scratch>/work/probe.py`, cwd `<scratch>/work`. Sandbox denies network,
`/Users` and `/private/Users` reads, and all writes except `<scratch>/work`; fetched source is read-only.
Result: **5/5 selection cases and 5/5 sandbox controls, exit 0**, Python 3.9.6. Controls: user-directory
read, network connect, outside write and source write denied with PermissionError; inside write allowed.
This qualifies selector semantics, not published-run token coverage, benchmark efficacy, or a supported
installation. Owned scratch was removed after retaining the evidence.

## Existing TeaPrompt Contract Mapping (closest lines, not gaps)

- `governed-delivery/SKILL.md`: oracle split (authoritative oracles read-only in-run; developer tests may be
  added; prompt text cannot seal — host must); decorrelated verification channels; evidence ledger; envelope
  budgets; acceptance by named accepter, never execution success alone.
- `reflective-implement/SKILL.md`: acceptance/invariant/security oracles read-only during a run; wrong oracle →
  stop + Human Review proposal; OUTCOME_UNKNOWN preserved for ambiguous post-dispatch outcomes.
- `flow-loop-harness/SKILL.md`: exactly one deterministic verifier decides; anti-reward-hacking (no weakening
  tests/thresholds from inside the loop); distinct exits 0/2/3/4; run state ≠ project memory.
- `reflective-research` State Ledger: verified covers only what was actually checked; load-bearing absence = zero
  count with named population + known-present control (XM-11); `reflective-review` Evidence Tiers: vendor numbers
  are attributed claims; four-dimension split (existence/number/attribution/extrapolation).
- `ROUTING_CONTRACT.md` R8 holdout-before-tune: fixture-addition timing, not a statistical untouched-final-test
  guarantee. `04-agent/workflow-recipes.md` DR-5: distilled directional guidance can shrink parallel search —
  prefer replayable evidence; disjoint slices, not coordinator direction.
- ECT-2 (coordinate-codex record): noise/headroom preflight + stochastic-build control + failure categorization
  before another mutation — record-only adjacent. ECT-4: untouched final test separate from selection validation
  — record-only adjacent. RS-4: generic hidden-oracle sentence rejected; visible red-first tests intentional;
  reopen only for a hidden-evaluation acceptance task. FM3/JL-9: private-fixture floor / judge-record boundaries
  unchanged. XM-3/XM-12: lock-escape probe widening held. RS-6 precedent (RSIAgent): learning-loop roles,
  wave/memory consolidation are non-goals — run state is never project memory.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence | Falsifier / trigger |
| --- | --- | --- | --- | --- |
| RRSI-1 | Annealed L0 edit budget as a prompt sentence | No change 2026-09-30 | No bundled-edit learning loop exists; flow packs pick smallest topology; minimality ladder sizes thickness to risk. Formula stays study material | A TeaPrompt-run iterative editor bundles unrelated changes and misattributes gains; smallest repair at its owning surface |
| RRSI-2 | Evidence-aware credit / full-history conditioning + attribution scoreboard | No change 2026-09-30 | Implement State Ledger + handoff-retro memory gate cover in-task evidence; RS-6: run state never becomes project memory; no falsified-hypothesis recurrence observed | Observed re-testing of a locally falsified hypothesis across runs with cost; repair the ledger surface, not the formula |
| RRSI-3 | Stall→untried-component reserved exploration slots | No change 2026-09-30 | Strictness ladder covers escalation; DR-5 bounds distilled guidance; no measured stall signal collected | A loop demonstrably collapses onto one edit family while a measured stall signal exists; then consider a surface-local directive |
| RRSI-4 | Critic regex+LLM leakage screen before evaluation | No change 2026-09-30 | RS-4: delivery oracles visible by design; governed-delivery seals via host, not prompt; screen is benchmark integrity for evolve-measured loops, not safety/generalization | A named hidden-evaluation acceptance task reopens RS-4 at that scope with host read-boundary evidence |
| RRSI-5 | Calibrated noise floor δ (repeated base evals / bootstrap, z=2) | Record-only, adjacent to ECT-2 2026-09-30 | ECT-2 already records the portable diagnostic recipe; RRSI δ is a per-instance tuned constant, not a prompt sentence | A named local eval mistakes noise for improvement; smallest in-place repair at that harness surface |
| RRSI-6 | Cost rule (β0+β1ΔS) + within-band shaped rule + structural novelty admission term | Record-only, adjacent 2026-09-30 | Local budgets are envelope/minimality constraints, not this numeric formula; novelty may admit a slightly lower score within the floor; missing cost becomes neutral ΔC, so the rule is not a fail-closed cost guarantee | A local numeric selection loop admits costlier-without-gain or unmeasured-cost winners; repair that loop's rule |
| RRSI-7 | Structural pruning B_t deletion targets | No change 2026-09-30 | No retained harness accumulates machinery across rounds; minimality delete-before-add + debt ledger cover intentional retention | A durable TeaPrompt surface accumulates unearning machinery across runs; prune that surface |
| RRSI-8 | Non-compensatory eng guards (valid −0.03 / no-payload +0.02) | No change 2026-09-30 | Thresholds are EngDesign-specific; governed-delivery gates already non-compensatory in shape | A local domain gains a metric that masks validity collapse; add a local guard with measured thresholds |
| RRSI-9 | Worktree-per-candidate + fast-forward + harness-tree hash + readjudicate/reevaluate lifecycle | No change 2026-09-30 | Host git operationalization; TeaPrompt methodology-side (flow packs: stub dry run, resume conventions, stale-output clearing RS-1) | A host-run loop needs the lifecycle; it ships with the host adapter, not a skill sentence |
| RRSI-10 | Missing-trial-0 with full reward denominator + invalid-missing gate | Record-only distinction 2026-09-30 | Benchmark pass-rate convention + reward-missingness gate, not token-coverage validation; no tokens → C=None → neutral ΔC. Local rule stays "unscored is unknown, never zero" (RSIAgent C5, GLOSSARY) | A local benchmark adopts the convention; record reward and cost coverage separately, never as a general missing-data rule |
| RRSI-11 | Fresh final data vs repeatedly-selected validation (evolve reuse; held-out/OOD never in selection; S* trajectory) | Record-only, adjacent to ECT-4 2026-09-30 | ECT-4 already records untouched-final separation; RRSI evolve scores must never be cited as final-gain claims | A named local optimization needs a reportable final gain; pre-register selection/final separation then |
| RRSI-12 | "Regularization improves transfer" as a safety/robustness claim | Record-only clarification 2026-09-30 | Measured task-domain tradeoff with smaller evolve gain + lighter tokens; deterministic-grading arms rule out judge-gaming for those suites, not safety in general | Safety-critical use would need its own hazard analysis; this record grants none |

Generic skill-update direction fires only this review's candidates (direction-scope rule); RS-4/FM3/JL-9/XM-3
and all unrelated named holds are untouched. No upstream vocabulary copied into operational artifacts
(clean-room: transferable patterns only, none landed).

## Falsifiability

- The mechanism table is wrong if a pinned code path or reachable probe contradicts a row (rerun the named
  file/function at `be50316e`; the smoke probe is disposable and recorded above).
- Any no-change mapping is wrong if an installed skill is later shown to lack the credited rule (coverage rows
  cite file + clause; re-grep them) or if a TeaPrompt-run loop exhibits the named failure (ledger trigger fires).
- Record-only ECT-adjacents (RRSI-5/6/11) are wrong if ECT-2/ECT-4's recorded distinction fails on a named local
  eval run — then the smallest in-place repair lands at that surface under fresh direction. RRSI-10 (benchmark
  missing-data distinction) and RRSI-12 (transfer-tradeoff clarification) are record-only without an ECT-adjacency claim.
- Author-claimed numbers stand or fall with upstream data/releases; the tracking points name what to re-check.
- The smoke proves only the exercised pure paths; any efficacy/transfer/cost reading beyond them is `[INFERENCE]`.

## Residual Risks / Unknowns

- Provider/benchmark paths unverified here: proposer/analyst/critic LLM behavior, repair-round dynamics,
  harbor/Docker determinism, Harvey judge variance, EngDesign gateway/flakiness, OOD script environments.
- Upstream volatility: post-pin commits, paper revisions, trajectory-explorer data, third-party harness drift.
- Within-band weights (esp. coding w_s=0) and guard thresholds are instance-tuned; porting numbers across
  domains would be cargo-cult, not adoption.
- Missing cost is treated as neutral relative cost; the supplemental pure-selector probe admitted gainers
  with either side's C=None. Whether published runs contain such measurements is unverified.
- The 30% abstract and 36% headline token claims have unresolved aggregation/context; Table 2 supports
  only the explicit workspace comparison. The proposer template's "DIFFERENT model" is not the main
  experiment's setup (all four roles use Claude Opus 4.8), and distinct roles do not prove decorrelation.
- L0/L1/L2 framing is analogy by the authors' own Appendix C statement — do not cite as optimization theory.
- No runtime, permission or security-logic change; public offline inspection and bounded local documentation repair only.

## Citations (checked 2026-09-30; code pinned)

- [Pin commit](https://github.com/google-research/rrsi/commit/be50316e1db05914068a973f322770ef08ed7ba1) (checked 2026-09-30).
- [Overview, results and license notes](https://github.com/google-research/rrsi/blob/be50316e1db05914068a973f322770ef08ed7ba1/README.md) (checked 2026-09-30).
- [Core source tree](https://github.com/google-research/rrsi/tree/be50316e1db05914068a973f322770ef08ed7ba1/rrsi): selection, evaluate, critic, history, components, schedule, calibrate, config, domain, gitops, loop and propose modules (checked 2026-09-30).
- [Selector](https://github.com/google-research/rrsi/blob/be50316e1db05914068a973f322770ef08ed7ba1/rrsi/selection.py), [scoring and relative cost](https://github.com/google-research/rrsi/blob/be50316e1db05914068a973f322770ef08ed7ba1/rrsi/evaluate.py), [evaluation lifecycle](https://github.com/google-research/rrsi/blob/be50316e1db05914068a973f322770ef08ed7ba1/rrsi/loop.py), [proposer template](https://github.com/google-research/rrsi/blob/be50316e1db05914068a973f322770ef08ed7ba1/rrsi/propose.py) (checked 2026-09-30).
- [Domain adapters and configs](https://github.com/google-research/rrsi/tree/be50316e1db05914068a973f322770ef08ed7ba1/domains), [workspace selection constants](https://github.com/google-research/rrsi/blob/be50316e1db05914068a973f322770ef08ed7ba1/domains/workspace/rrsi.json) (checked 2026-09-30).
- [Upstream core tests](https://github.com/google-research/rrsi/blob/be50316e1db05914068a973f322770ef08ed7ba1/tests/test_core.py), read but not run (checked 2026-09-30).
- [Root license](https://github.com/google-research/rrsi/blob/be50316e1db05914068a973f322770ef08ed7ba1/LICENSE); third-party license paths and blob identities are recorded in Source Identity (checked 2026-09-30).
- [Paper abstract](https://arxiv.org/abs/2609.24972), [versioned PDF v2](https://arxiv.org/pdf/2609.24972v2) (checked 2026-09-30).
- [Project page](https://regularized-rsi.com/) (checked 2026-09-30).

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Source pinned, license + third-party boundary verified | done | API commit object + LICENSE reads + blob SHAs above |
| Paper + site read for mechanism/evidence claims | done | §§1–6, App. A–E, site sections 01–05 |
| Core modules compared at pin (proposal/selection/scoring/history/critic/components/configs/adapters) | done | Mechanism Map M1–M13 |
| Missing reward, missing cost and infrastructure validity separated | done | M6–M9 + RRSI-10; supplemental unknown-cost admission controls |
| Evolve / held-out / OOD / repeatedly-selected data separated; performance and token-saving scopes qualified | done | M13 + Reported Performance; abstract/headline vs workspace Table 2 |
| Meaningful offline smoke of real pinned modules + adversarial/error boundary | done | Initial 34/34 PASS and boundary control; supplemental 5 selection + 5 sandbox controls, both exit 0; unsupported-interpreter limit explicit |
| Per-candidate local coverage + adoption/falsifier decisions (RRSI-1–12) | done | Candidate Adoption Ledger |
| No RRSI mechanism promoted; no invented benchmark replication | done | Twelve candidate dispositions; local recipe repair separately recorded as AF841-M1 |
| Scratch cleanup | done | Initial `/tmp/rrsi-smoke-Ku3IM5` removed; supplemental `/private/tmp/teaprompt-rrsi-selection-Q2XceG` removed and verified absent; both outside-write sentinels absent, 2026-09-30; evidence retained before removal |
