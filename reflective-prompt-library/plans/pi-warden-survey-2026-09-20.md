# Pi-Warden Survey — `DevMortimer/pi-warden` @ `c9921c3ebc48` + Goals Rethink (2026-09-20)

> **Status: decided — one sentence adopted (PW-1) under a fired reopen trigger plus user direction; otherwise record-only.** The object is a four-day-old MIT TypeScript extension (created 2026-09-16T03:58:46Z, v0.29.1, 86 stars) for the Pi coding-agent family: eight guards on tool-call/stream/settle hooks that steer instead of interrupting, judged by the Jev decision API through `pi-typesafe`, with a deterministic pattern floor the model can only raise. Two things distinguish this survey from the seven before it. First, the load-bearing trigger finally fired with executed evidence: DM-5's reopen condition — real candidate scores exposed to a TeaPrompt-run step — is now true in TeaPrompt's own host family (the host's `judge()` primitive was executed during this survey and returned per-candidate probabilities; pi-warden ships the same decision API as an installed production extension), and the resulting candidate landed as PW-1 under the accompanying direction. Second, the instruction explicitly requested a goals rethink; the verdict is that the north star and the runtime non-goals stand, vindicated — a warden-class enforcement layer was built by the host ecosystem, reading exactly the natural-language policy artifacts TeaPrompt produces, without TeaPrompt owning any runtime.

## Research Question

User instruction, verbatim: "Survey this concept and rethink our goals. Update docs and skills if worthy". Three components under the installed direction-scope rule: the survey itself; an explicitly requested goals rethink (§Goals Rethink); and a generic "if worthy" adoption clause, which fires only this survey's own candidates and no named hold elsewhere. DM-5's reopen is not fired by the direction — it is fired by evidence (an executed host integration); the reopen was conducted inside this survey, making its candidate this survey's candidate; the landing then rests on the direction plus the worth bar. The consideration-is-not-authorization rule is respected: the fired trigger authorized the reconsideration, the user direction authorized the landing.

## Direct Recommendation (as of 2026-09-20)

- **Study: the calibration and authority discipline.** Every enforcement threshold is derived from replayed local sessions with user-reaction labels; unmeasured questions are recorded, never acted on; approval authority is confined to the user's message; project files cannot weaken the floor. This is a governance charter executed at extension scale.
- **Reproduce: not done.** Docs read in full at the pin; `src/` and `tests/` not audited; all numbers author-claimed.
- **Adopt: PW-1 only.** The one-way confidence ratchet, transposed to the installed Confidence recipe row — the reopened DM-5 gap is real on TeaPrompt's surfaces (nothing distinguished self-reported confidence from host-measured scores, and nothing forbade a confidence number lowering rigor). Everything else is covered, host territory, or corroboration.
- **For citers:** CONTRIBUTING bans AI-attribution lines while the latest merge carries model co-author trailers — a stated-rule/practice inconsistency at this pin; the co-maintainer account is named "Mr Jev" (recorded as an account identity, no inference drawn); the deterministic-floor spec documents mechanisms marked not-yet-implemented while other docs describe them as shipped (a design spec kept as a record); four-day-old repo — expect churn.

## Method

Coordinator reads (2026-09-20), no scouts, no panel: GitHub API (repo metadata, commits, tree `0d132763c3b226a9d43331704d26066fe31b662d` at pin `c9921c3ebc48f62348199eb03119c645d98cdb8b`, PGP-verified merges); read in full at the pin — `README.md`, `docs/guards.md` (32KB), `docs/data-handling.md`, `docs/overnight-eval.md`, `CONTRIBUTING.md`, `eval/README.md`, `package.json`; `docs/deterministic-floor-spec.md` lines 1–300 of 421. Dependencies pinned from the manifest: `pi-typesafe` ^0.6.0 (Jev API client); optional peer `@earendil-works/pi-coding-agent`. The host-integration check was executed, not read: the session's own `judge()` primitive was invoked and returned `{choice, probabilities, confidence}` — a TeaPrompt-run host step consumed real per-candidate scores. Goals surfaces re-read for the rethink: the north star and Standing Non-Goals in `PROJECT_KNOWLEDGE.md`.

**Scope / acceptance:** pin the revision; read the governing docs in full; verify the DM-5 trigger by execution before acting on it; decide every candidate with evidence and a trigger; land only what the direction plus worth bar authorize; keep the clean-room boundary; run `make all` from the repository root.

## What the Artifact Is

Eight guards over the Pi extension hooks, default mode **steer** (guidance injected as steering, hidden from the transcript; "Steers never hold."), with confirm and advise modes, a steer budget of three per run, and critical guards exempt from the budget. The Action guard combines a deterministic pattern floor with four Jev questions (irreversible / off-task / mutates / scope) plus an intent-mismatch check against the agent's own stated plan — under a strict authority order: "patterns set the floor and Jev can only raise it, the agent's plan can add a nudge but never remove a hold, and the LLM is never asked to judge itself". The Rules guard judges tool calls against project Markdown rules — from a dedicated rules file when present, else the first of README/CLAUDE/AGENTS-class files: natural-language policy documents are the machine-judged rulebase. Other guards: slop (stubs, restating comments, hedging), security (secrets, injection, stand-in credential demotion), stuck loops, runaway streams (offline repeat detection calibrated on 43k local messages), done-claims (checks-run-after-last-change accounting), subagent wake triage (one batched wake per 120s; a pointer, never a summary), and a cache-preserving context saver. Config authority is fail-closed against the workspace: "a checked-out repo cannot ship itself a hold-free floor or a prompt farm". Approval authority is fail-closed against the transcript: "Approval comes from the user's message only."

**Calibration before enforcement.** Thresholds come from replaying 321 recorded sessions (1,085 labelled turns; 17,160 guarded calls, 14,903 judged) against user-reaction labels; regretted calls were 20 (2% of turns), and the questions' AUC against regret is published per question (mutates 0.74, irreversible 0.71, intent_mismatch 0.57, off_task 0.51). Consequences follow measurement, not intuition: "Off-task alone caused 56 of the 139 replay holds and none of them drew a complaint" — so off-task was demoted to never-hold, then to trace-only until its AUC clears 0.51, with "unclear stays quiet (missing context is not evidence)". The contribution charter generalizes it: "An unmeasured question can be merged as `extra` (recorded, never acted on), not as a rule." Replay cost is disclosed ($3.40 for 32k requests) and dry-run gated. The eval harness measures the guard "against the honest null hypothesis: the same rules handed to the model as prose", and its checker "Shares no code with the guard on purpose: no Jev verdict can influence a score." Headline A/B, author-claimed: "In 150 paired agent runs, the control setup violated the tested project rule **6 times**. With Warden: **0**." Scale claim: "13,952 guard cases across 109 cycles" with max score drift 0.03. The floor-spec's negative-space design is motivated by an approval-fatigue observation about a prior tool (~2,000 prompts/week, ~87% false positives): "prompts that fire this often train the operator to approve reflexively"; "every new mechanism is negative-space".

Claim posture: docs tier, unusually measurement-disciplined, self-consistent except the attribution inconsistency noted for citers; code fidelity not audited.

## Concept Map

Tier is `docs` throughout — `src/` not audited.

| ID | Concept (clean-room) | TeaPrompt coverage | Disposition |
| --- | --- | --- | --- |
| C1 | Steer-vs-interrupt economics: steering costs a turn, budgeted, repeats recorded not delivered, critical guards exempt | Loop-pack turn-economics family; host territory | No change |
| C2 | Measurement-before-enforcement charter: unmeasured questions recorded never acted on; trace-only until AUC clears; thresholds from replayed sessions | R11's fixture-backed tuning duty and the GW-1 lesson are the installed artifact-level form | No change — strongest production corroboration yet |
| C3 | Hold-feedback labeling: the user's next action labels each judgment; precision measured on the project's own sessions | "A stated decision is not an observable" + judge-lifecycle re-anchoring | No change — corroboration |
| C4 | Authority rules: approval only from the user's message; assistant text never approves; workspace files cannot weaken the floor | TeaPrompt authority chain; the GE-1-revert lesson (consideration is not authorization) — independent convergence | No change |
| C5 | One-way confidence ratchet: deterministic floor, model judgment can only raise it, self-assessment can never remove a hold | Gap verified on installed surfaces (dispatch low-confidence rules; Confidence recipe row) — nothing forbade confidence lowering rigor, nothing scoped host-measured scores | **PW-1 adopted** |
| C6 | Negative-space floor design against approval fatigue: indiscriminate gates train reflexive approval | R11's phrase-space lesson is adjacent; no local rubber-stamp instance verified | No change — PW-2 reopen parked |
| C7 | Composition/arming risk: a harmless call arms a catastrophic later one; per-call judgment structurally blind; deterministic session-state capability, operator-declared | `agent-governance-scaffold` cumulative_effect_key / cross_purpose_budget cover the class at pack level | No change — corroboration + specimen |
| C8 | Fail-open advisory layer over a deterministic floor, disclosed posture | Posture choice, host territory; the governance packs' fail-closed applies to effect authority — a different layer | No change |
| C9 | Decorrelated verification: eval checker shares no code with the guard; env leak-drop keeps env dumps from the model | Research second-method rule; governed-delivery decorrelated verification | No change — production corroboration |
| C10 | Cache-preserving newest-result-only context compression with measured recall | Host territory | No change |
| C11 | Cost-gated calibration with disclosed spend and model-choice banner | Reporting-hygiene family | No change |
| C12 | Subagent wake triage: silence for progress, judgment only on trouble, batched wakes, pointer-not-summary | Host harness territory | No change |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| PW-1 | Confidence-ratchet sentence on the `04-agent/workflow-recipes.md` Confidence row, adopted wording: "confidence only raises strictness: low self-reported confidence defaults up, a close call between top candidates on host-measured scores escalates the same way, and no confidence number — self-reported or measured — lowers the rigor risk demands" | Adopted 2026-09-20 (DM-5 reopened; fired trigger + user direction) | DM-5's reopen condition verified by execution: the host's `judge()` returned per-candidate probabilities to a TeaPrompt-run step, and the surveyed extension ships the same decision API in production. Gap verified: dispatch's low-confidence rules and the Confidence row scoped only self-reported confidence and never forbade a confidence number lowering rigor. DM-5's record stays byte-unedited — its rejection of *self-reported* margin stands and the adopted sentence preserves it | Retire: none. DM-5 remains Rejected as written in its record; the measured-score path now has its rule |
| PW-2 | Approval-fatigue sentence for `reflective-risk` Human Review (a gate that fires indiscriminately trains reflexive approval; gate selectively) | No change 2026-09-20 | C6 row: the external measurement (a prior tool's ~87% false-positive prompt stream) is external evidence; no local rubber-stamped gate instance is verified | Reopen on the first TeaPrompt Human Review gate observed rubber-stamped, or approvals given without reading |
| PW-3 | Measurement-before-enforcement wording | No change 2026-09-20 | C2 row: R11 + GW-1 cover it at artifact level | None |
| PW-4 | Composition/arming wording | No change 2026-09-20 | C7 row: covered at pack level | None |
| PW-5 | Goals Rethink outcome: north star and runtime non-goals stand, vindicated; prose-vs-warden A/B noted author-claimed | Noted 2026-09-20 (record-only) | §Goals Rethink — no defect found in goals text, so no goals edit | Reopen if a second measured prose-vs-warden comparison contradicts the first, or project direction changes |
| PW-6 | Ecosystem note: eighth decision-interface survey; the integration DM-5/MV-6/JA-7 awaited now exists in TeaPrompt's own host family (executed `judge()`; production Pi extension); MV-6/JA-7 records stay byte-true as dated statements | Noted 2026-09-20 (record-only) | Executed check; pin | DM-5 bookkeeping completed via PW-1 |
| PW-7 | Citer notes: AI-attribution ban vs trailer practice; "Mr Jev" co-maintainer account identity recorded without inference; floor-spec not-yet-implemented vs docs-shipped mismatch; four-day-old repo | Noted 2026-09-20 (record-only) | Commits and docs at the pin | None |

Deterministic guard: `plans/tests/test_pi_warden_survey_record.py` (identity pins, quote pins, PW-1 pinned once at its surface, dispositions, clean-room boundary, index links).

## Shared Findings

1. **The trigger the ecosystem surveys kept unfired is now fired — by execution, not by reading.** Seven surveys held the line that tool existence is not host integration. The eighth ran the host's own typed-judgment primitive and watched a TeaPrompt-run step consume per-candidate probabilities, while the surveyed extension ships the same decision API into the same harness family in production. The distinction did its job: it fired exactly when the fact changed.
2. **The adopted principle is the artifact's deepest rule, not its headline.** The ratchet — floors rise, self-assessment never lowers them, the judge is never the judged — is what made every other pi-warden mechanism safe to automate. Transposed to TeaPrompt's prompt level: confidence numbers, self-reported or measured, may only raise strictness.
3. **Warden-class enforcement consumed natural-language policy as its rulebase.** The Rules guard judges tool calls against README/CLAUDE/AGENTS-class documents — the artifact class TeaPrompt produces is now the machine-judged input of a host-side enforcement layer. The division of labor the north star names (TeaPrompt writes policy; hosts enforce) is not just intact, it acquired a working seam.
4. **The first measured prose-vs-warden comparison quantifies a known limit without invalidating prose.** Six violations in 150 prose-only runs versus zero with enforcement, on the same ten rules — author-claimed, single-project, and exactly the bound Non-Goal 59 already states: guards on text do not prove agents follow text. The number is recorded; the non-goal needed no edit.
5. **Calibration culture arrived in the extension ecosystem.** Replayed sessions, user-reaction labels, per-question AUC, demote-on-evidence, unmeasured-means-inert, disclosed spend — the measurement discipline TeaPrompt's records enforce editorially now ships as a contribution charter in a four-day-old tool.

## Goals Rethink

Requested explicitly; grounded in the north star ("help humans and host agents choose the right amount of rigor … without operating its own agent runtime") and the Standing Non-Goals on runtime enforcement, operational completeness, host authority, and the reach of repo guards.

1. **The no-owned-runtime boundary is vindicated, not strained.** A warden — the exact side-effect enforcement layer TeaPrompt's non-goals decline to build — was built by the host ecosystem, four days ago, with better calibration data than a methodology project could ever collect, because it sits where the tool calls are. Owning a runtime would have produced a worse warden and a worse prompt library.
2. **TeaPrompt's product category gained a machine consumer.** Natural-language harness policy is no longer read only by models-in-context; wardens judge against it. This raises the value of precise, checkable policy prose — the thing the repository already optimizes — and changes nothing about who enforces.
3. **The prose-limit number (6/150 → 0) is the honest cost of the boundary,** recorded as author-claimed evidence for a bound the non-goals already state. If a second independent measurement lands, PW-5's reopen brings it back.
4. **The decision-interface thread and the goals converge at the seam:** typed judgment reached TeaPrompt's own host family, and the correct response was one prompt-level sentence (PW-1) scoping how measured confidence may move rigor — not a runtime, not a scorer, not a tenth skill.

Verdict: goals stand; no goals-text edit is warranted; this section is the record of the rethink.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Repo identity, dates, license, version, dependency pins, tree | Observed | GitHub API + manifest at the pin, 2026-09-20 |
| Guard mechanics, authority rules, calibration procedure and numbers, eval design | Observed at docs tier | Seven docs read in full at the pin; floor-spec head; `src/` not audited |
| A/B result (6 violations vs 0 in 150 paired runs), 13,952 cases / 109 cycles, AUC figures, live-steer counts | Author-claimed | Repository documentation; nothing reproduced |
| Host `judge()` returns typed per-candidate probabilities to a TeaPrompt-run step | Observed — executed | Invoked during this survey; returned `{choice, probabilities, confidence}` |
| pi-warden integrates the same decision API in production | Observed at docs tier | Manifest dependency + guards.md; the wire integration itself not traced |
| The DM-5 reopen fired | Executed + observed | The two rows above; DM-5's own falsifiability line names this condition |
| Goals verdict (stand, vindicated) | Judgement, evidence-grounded | §Goals Rethink; goals text re-read this session |
| Stated-rule/practice attribution inconsistency | Observed | CONTRIBUTING text vs latest merge trailers at the pin |

## Evidence Actually Checked

- GitHub API: repo metadata, commits, recursive tree at `c9921c3ebc48` — 2026-09-20.
- Read in full at the pin: `README.md`, `docs/guards.md`, `docs/data-handling.md`, `docs/overnight-eval.md`, `CONTRIBUTING.md`, `eval/README.md`, `package.json`; `docs/deterministic-floor-spec.md` lines 1–300 of 421 — 2026-09-20.
- Executed: the host's `judge()` primitive (typed judgment with per-candidate probabilities) — 2026-09-20.
- Goals surfaces re-read: north star and Standing Non-Goals in `PROJECT_KNOWLEDGE.md`; installed Confidence surfaces (`reflective-dispatch` SKILL, `workflow-recipes.md` Confidence row) re-grepped before the PW-1 edit — 2026-09-20.
- Not done: `src/`, `tests/`, remaining docs (configuration, FAQ, examples, commands, CHANGELOG), floor-spec tail; no reproduction of any published number.

## Falsifiability

- All pi-warden numbers are author-claimed at docs tier; code fidelity not audited — a trace-map-style follow-up would settle it.
- The PW-1 gap claim is wrong if an installed surface already forbade confidence lowering rigor; the greps that found none are named in Method, re-runnable.
- The executed `judge()` evidence is session-scoped; if the host removes or reshapes the primitive, PW-6's ecosystem note stays true as dated and PW-1's sentence remains correct on its own terms (it binds prompt-level behavior, not the host API).
- The goals verdict is wrong if a second measured prose-vs-warden comparison shows prose-only policy failing at a rate that makes methodology-without-enforcement misleading as a product category; PW-5 carries that reopen.
- The attribution-inconsistency note is pin-scoped; a later commit may resolve it either way.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Revision pinned; identity, license, dependencies recorded | done | this record |
| Seven docs read in full; floor-spec head; claim posture assessed | done | Method; What the Artifact Is |
| DM-5 reopen verified by execution before landing anything | done | Evidence vs Inference (executed row) |
| Twelve concepts mapped; seven candidates decided with evidence and triggers | done | Concept Map; Candidate Adoption Ledger |
| PW-1 landed once at its recorded surface; DM-5's record left byte-unedited | done | `04-agent/workflow-recipes.md` Confidence row; guard |
| Goals rethink conducted and recorded; goals text unedited — no defect found | done | §Goals Rethink; PW-5 |
| Clean-room boundary on installed surfaces | done | guard vocabulary test |
| Guard written | done | `plans/tests/test_pi_warden_survey_record.py` |
| Decision Index row (at head), case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`; `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |
