# Jev-vs-Diffusion Eval Survey — X thread by @mmastrac, 2026-09-17 (2026-09-19)

> **Status: decided — record-only; no installed change, no wording adopted.** The object is an author-reported eval thread: Matt Mastracci ran a live battery against Jev and against "DiffusionGemma-as-Jev" — his own vLLM patch serving `google/diffusiongemma-26B-A4B-it` (an open 26B-total / 4B-active MoE **diffusion** language model) through a Jev-style typed-decision interface — and calls it a tie on intelligence with local hardware faster once warm. The two checkable artifacts both verify: the model exists with a large ecosystem, and the patch is real, current, and upstream-first — main PR `vllm-project/vllm#57250` "[Core] structured generation mode … (Jev-like)" (open, 14 commits / 17 files), with five prerequisite PRs split out and **two already merged**. The eval numbers themselves are author-claimed (thread screenshots; no published battery found). The thread's capability finding — both models fail multi-step planning (Towers of Hanoi) even with a pseudo-thinking register; "structured decision models are fast, but they work on what they see in front of them and don't think" — is the strongest external corroboration yet of the installed fast-path/deliberation split. Third Jev-ecosystem survey; the reimplementation family now has a third substrate (diffusion canvas readout, after AR logit scoring and trained NLI heads). Clean-room throughout.

> Refresh pointer (2026-10-22): the "two already merged" snapshot is now "all six merged" — main PR #57250 plus all five prerequisites plus follow-up #58216 (constrained reads) landed in vLLM main; the shipped example grew a `diffusion_constrained` field, a real `/v1/systemone` endpoint, and an N-token think channel. The model revision is unchanged. All 2026-09-19 verdicts stand unless the refresh section says otherwise.

## Research Question

User instruction: "Survey https://x.com/mmastrac/status/2100626206198759558…". Three questions: (1) do the thread's checkable artifacts exist as claimed; (2) what do its findings establish, at what evidence tier; (3) does any concept expose a verified gap on an installed TeaPrompt surface. A bare "survey" carries no adoption direction.

## Direct Recommendation (as of 2026-09-19)

- **Study: yes, for two findings.** (a) The planning boundary: a single-pass decision surface — either vendor's — fails recursive multi-step planning even when handed a scratch register; fast typed decisions are judgment points, not planners. (b) The substrate result: a *diffusion* LM serves the same typed-decision contract through fixed canvas positions + logprob readout — the interface is serving-level, not architecture-bound, which sharpens the architecture-underdetermination finding of the 2026-09-19 Jev-architecture survey from "either attention mask" to "even a non-autoregressive denoiser."
- **Reproduce: partially possible, not undertaken.** The patch is public (apply #57250, serve the open model); the battery is not published in the thread, so the headline numbers cannot be re-run as stated. Nothing was executed here.
- **Adopt: nothing.** The evidence-hygiene moves the thread makes (self-disclosed confounds, an imperfect-control caveat) are installed rules; the capability and substrate findings are corroboration; the serving mechanics are host territory.
- **For citers:** "roughly tied" is bounded to this battery (mazes, Hanoi, PII, cross-answer consistency) — it is not frontier-benchmark parity, and the speed comparison is API-vs-local-DGX-Spark with network latency excluded by the author's own framing. The thread and this record both keep that scope.

## Method

Coordinator verification (2026-09-19), no scouts, no panel: the thread fetched via a mirror (post dated 2026-09-17; eight author replies; one third-party reply announcing an independent red-team addition); the model located on HF (`google/diffusiongemma-26B-A4B-it`, ~624k downloads, plus quantized ecosystem variants from four other publishers); the author's vLLM PRs located via the GitHub search API (69 DiffusionGemma-matching PRs repo-wide; five by the author dated 2026-09-17/18); merge state read for the two closed ones (both merged); the main patch's body read (#57250: purpose, mechanism, prerequisite-PR list). Eval screenshots were not independently analyzable; no battery repository was linked.

**Scope / acceptance:** verify the checkable artifacts; tier every claim; map concepts against installed surfaces; land nothing without a verified gap; run `make all` from the repository root.

## What the Thread Claims, and What Checked

| Claim | Verdict | Basis |
| --- | --- | --- |
| A patch exists making the open diffusion model serve a Jev-like interface | **Verified** | `vllm#57250` open, "[Core] structured generation mode for DiffusionGemma model (Jev-like)", 2026-09-16, 14 commits / 17 files / 23 comments |
| The mechanism: fixed canvas positions in the structured output; token + logprobs returned; client derives entropy as confidence; sub-threshold entropy triggers additional sampling | **Verified (PR text)** | #57250 body, read 2026-09-19 |
| Upstream-first split: prerequisite PRs stand on their own merits | **Verified** | Five prerequisites listed in the body; #57414 and #57417 (logprob correctness on committing/converging steps) **merged**; #57416/#57462/#57589 open |
| The model: an open instruction-tuned MoE diffusion LM at 26B/A4B | **Verified** | HF `google/diffusiongemma-26B-A4B-it`; quant ecosystem (GGUF, NVFP4, AWQ) |
| Speed: local DGX Spark beats the API once warm, network excluded | Author-claimed, confound self-disclosed | Thread; different hardware, serving stacks, and network positions — the author names all three |
| Intelligence: "roughly tied" — similar mistake counts, reasonable confidence when wrong, open model "wins a bit" on a PII test | Author-claimed | Thread screenshots; battery unpublished |
| Both fail Towers of Hanoi beyond the trivial case, even with a pseudo-thinking register | Author-claimed | Thread; consistent across both models — the finding is about the surface class, not a vendor |
| Control: a non-diffusion server "started to fall apart" on the simpler battery | Author-claimed, caveated by the author ("not a perfect comparison") | Thread |
| An independent 15k+ red-team eval will add this | Third-party stated intent | Reply in thread; nothing to check yet |

## Concept Map

| ID | Concept (clean-room) | TeaPrompt coverage | Disposition |
| --- | --- | --- | --- |
| C1 | Independent parity challenge with self-disclosed confounds (hardware, warm-up, network, imperfect control) | Evidence-hygiene rules: confound naming, verdict bounded by the check | No change |
| C2 | Planning boundary of single-pass decision surfaces: fast typed decisions judge what is in front of them; multi-step recursive planning fails even with a scratch register | The installed fast-path/deliberation split: Small-Change Fast Path exits on any high-risk signal; strictness ladder escalates on ambiguity; verdict contracts are judgment points, never planners | No change — strongest external corroboration yet of the installed shape |
| C3 | Substrate independence: the typed-decision interface is serving-level — now demonstrated on a diffusion denoiser (canvas-position readout), after stock-AR logit scoring and trained classification heads | The 2026-09-19 architecture survey's underdetermination finding, sharpened | Noted (record-only) |
| C4 | Upstream-first artifact-backed claims: the patch split into independently-meritorious PRs, two merged before the thread | Reporting discipline (claims with public artifacts; figures bound to revisions) | No change |
| C5 | Battery-bounded parity: "tied" on a task-shaped battery is not benchmark parity | Verdict-scope rule | No change |
| C6 | Entropy-derived confidence with threshold-triggered escalation, computed from logprobs — a structural signal, not a self-report | DM-5's family: the rejected candidate was *self-reported* margin; its reopen trigger names exactly this signal class, exposed to a TeaPrompt-run step | Noted (record-only) |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| MV-1 | Confound-disclosure wording | No change 2026-09-19 | C1: installed | None |
| MV-2 | "Fast decision surfaces don't plan" sentence for dispatch/fast-path scoping | No change 2026-09-19 | C2: the installed fast path already exits on risk/ambiguity signals, and no TeaPrompt surface routes planning to a decision-only step; adding would restate | Reopen if a TeaPrompt surface is ever proposed that hands multi-step planning to a single-verdict step |
| MV-3 | Substrate-independence note | Noted 2026-09-19 (record-only) | C3: third open substrate for the decision interface; corroborates the architecture survey without editing it | None |
| MV-4 | Upstream-first reporting rule | No change 2026-09-19 | C4: installed | None |
| MV-5 | Battery-bounded parity wording | No change 2026-09-19 | C5: verdict-scope rule states the general form | None |
| MV-6 | DM-5 trigger-family evidence: an open serving patch now derives confidence from logprob entropy with threshold-triggered escalation — the structural-signal class DM-5's reopen trigger names; three open routes exist (AR logit scoring, trained heads, diffusion canvas readout) | Noted 2026-09-19 (record-only) | #57250 body; JA-7 precedent: tool existence is not host integration — no TeaPrompt-run host exposes such scores; trigger stays unfired, evidence now dated across three substrates | DM-5 reopens per its own row if a host integrates any of the three |

Deterministic guard: `plans/tests/test_jev_diffusion_eval_survey_record.py` (identity, claim-check pins, dispositions, clean-room boundary, index links).

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Thread contents and dates | Observed | Mirror fetch, 2026-09-19 (post 2026-09-17) |
| #57250 title, state, mechanism text, prerequisite list; #57414/#57417 merged | Observed | GitHub API, 2026-09-19 |
| Model identity and ecosystem | Observed | HF API, 2026-09-19 |
| All eval numbers and the tie verdict | Author-claimed | Thread; battery unpublished |
| The Hanoi failure generalizes to the surface class | `[INFERENCE]` (author's and this record's) | Two models, one battery; consistent with the class's single-pass construction |
| "Roughly tied" transfers beyond this battery | Not claimed | Bounded by both the thread and this record |

## Evidence Actually Checked

- Thread via mirror; HF model search; GitHub PR search, two merge-state reads, #57250 body — all 2026-09-19.
- Not done: running the patch, the battery, or either model; reading the 14 commits; the screenshots' numbers were not extractable.

## Falsifiability

- The artifact verifications are pin-checkable (#57250 and merge states are public history).
- MV-2's no-change is wrong if an installed TeaPrompt sentence is found routing planning into a single-verdict step (none found by read; the fast path's exit conditions are quoted in the 2026-09-19 MC-5 landing context).
- C2's corroboration reading fails if the Hanoi failures were battery artifacts (prompt-shape, register design) rather than surface-class limits; the promised third-party red-team results are the tracking point.
- MV-6's non-fire is wrong if a TeaPrompt-run host already integrates one of the three routes; that fires DM-5's own trigger, not a new one.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Checkable artifacts verified (patch, merges, model); mechanism read from the PR | done | What the Thread Claims |
| Six concepts mapped; six candidates decided | done | Concept Map; Candidate Adoption Ledger |
| Cross-record notes recorded without editing prior records (C3→architecture survey; MV-6→DM-5) | done | ledger rows |
| Clean-room boundary on installed surfaces | done | guard vocabulary test |
| Guard written | done | `plans/tests/test_jev_diffusion_eval_survey_record.py` |
| Decision Index row (at head), case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`; `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |

## Latest-version refresh — 2026-10-22

Record-only; no installed change, no wording adopted. All 2026-09-19 dispositions (MV-1..MV-6) stand.

| Project / source | Prior baseline (2026-09-19) | Latest checked (2026-10-22) | Release / branch split |
| --- | --- | --- | --- |
| `vllm-project/vllm#57250` (main patch) | Open, 14 commits / 17 files / 23 comments | **Merged** 2026-09-22 (26 commits, by LucasWilkinson, branch `mmastrac/structured-reads-main` → main) | Landed in main; newest tags `v0.32.0` / `v0.32.1rc0` postdate the merge (release containing it not traced) |
| Prerequisite PRs #57414 / #57417 / #57416 / #57462 / #57589 | 2 merged, 3 open | **All 5 merged** (2+1+4+3+4 commits respectively, all by LucasWilkinson) | Landed in main |
| Follow-up #58216 `diffusion_constrained` | Did not exist | **Merged** 2026-09-24 (9 commits, vllm-bot; author mmastrac, Sep 22): unembedding/sampler/self-conditioning run over the request's `logprob_token_ids` only, logprobs normalized over that set | Landed in main |
| `examples/features/structured_diffusion/` at vLLM main | PR-body prototype (`/v1/systemone` example server) | Shipped in main (README + `structured_server.py` verified at HEAD `7d53359`, HTTP 200): adds `diffusion_constrained` field, real `POST /v1/systemone` (Jev API shapes incl. 0-indexed score legend), per-question `depends_on`/`ask_if`/`alone` staging, image inputs, `"think": N` thought channel with `diagnostics.thought` | Main-branch file state, not a release |
| `google/diffusiongemma-26B-A4B-it` (HF) | ~624k downloads | sha `f7f5b7f5fa82ffc52addd066915886d497f5517b`, modified 2026-07-15 (unchanged — predates the survey), 655,564 downloads, 1,312 likes | Registry revision, frozen |
| X thread (author evidence) | Mirror fetch 2026-09-19 | Original post URL HTTP 200 on 2026-10-22 (availability only; screenshots/battery not re-analyzed) | Publication reference |

Actual meaningful changes:

- **The upstream-first bet paid off in full.** Every PR the record tracked is now merged; the "two already merged" claim-check row reads "all six merged" as of 2026-09-24. The record's C4 (upstream-first artifact-backed claims) is corroborated by the outcome it predicted.
- **The shipped surface exceeds the PR body.** Beyond the surveyed mechanism (seed canvas, read-only converging-step emit, temperature-1 logprobs, `diffusion_canvas_length`): `diffusion_constrained` normalizes logprobs over exactly the label set (fixing the "only 1–8 of 26 options rank in top-k" problem the PR body named); the example server now speaks the actual Jev decision-API shapes; multi-stage question dependencies (`depends_on`/`ask_if`/`alone`) and an N-token think channel (thought shared across a decision's noise draws, returned in diagnostics) push back on the planning-boundary finding's edges — a scratch register plus staged reads is now a shipped pattern, though the Hanoi-failure verdict itself (author-claimed, battery unpublished) is unchanged and unretested here.
- **Open follow-ups (named, not reviewed):** #61480 (one-step reads in a single forward pass, CPU perf, open, author ojeda-e, Oct 13; mmastrac commented Oct 16) and #61669 (stop sampler recompiles during serving, open, author pranavabbott, Oct 14) — both touch the structured-reads path and are the current tracking points.
- **Model frozen.** The DiffusionGemma revision predates the survey; the tie verdict stays bounded to the unpublished battery (MV-5 unchanged); the red-team tracking point (third-party 15k+ eval intent) has no observed outcome — not re-checked beyond noting no battery repository surfaced in the inspected PR surfaces.

Effect on prior findings: Finding (a) planning boundary stands as the record's study recommendation — the think channel is new upstream capability, not a re-run of the Hanoi battery. Finding (b) substrate independence is strengthened: the diffusion route went from "author's open PR" to "merged upstream feature with a Jev-API-compatible server". MV-6's evidence now spans a merged upstream feature rather than a patch, but the trigger analysis is unchanged — no TeaPrompt-run host exposes these scores, so DM-5 stays unfired.

Inspected immutable links: `https://github.com/vllm-project/vllm/pull/57250`, `https://github.com/vllm-project/vllm/pull/57414`, `https://github.com/vllm-project/vllm/pull/57417`, `https://github.com/vllm-project/vllm/pull/57416`, `https://github.com/vllm-project/vllm/pull/57462`, `https://github.com/vllm-project/vllm/pull/57589`, `https://github.com/vllm-project/vllm/pull/58216`, `https://github.com/vllm-project/vllm/pull/61480`, `https://github.com/vllm-project/vllm/pull/61669`, `https://github.com/vllm-project/vllm/tree/main/examples/features/structured_diffusion`, `https://huggingface.co/google/diffusiongemma-26B-A4B-it`, `https://x.com/mmastrac/status/2100626206198759558`.

Untested limits: no execution (patch, server, model, battery); merge states read from rendered PR pages (GitHub REST rate-limited, recorded 2026-10-22); the vLLM release containing the merge not traced; thread screenshots/battery still unpublished and unanalyzed; red-team outcome unknown.
