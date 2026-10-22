# Bespoke Nimble Survey — `bespokelabsai/nimble` @ `d2387fc0b32d` (2026-09-19)

> **Status: decided — record-only; no installed change, no wording adopted.** The object is a one-day-old public repository (created 2026-09-18T09:07:48Z, surveyed the next day) whose tagline is "Data, Model, Recipe for an open Jev": a Jev-class typed-decision stack — answer-token logit readout over a flat schema, a LoRA adapter on a pinned 9B base, a fully documented contrastive-curation recipe, and a 13-subset human-labeled public benchmark suite that reports the project losing to its inspiration. There is no LICENSE at the repository root at this pin (the only LICENSE in the tree belongs to a vendored MIT skill), so the adoption lens's no-license rule applies: concepts only, no copying of text, code, checklists, or file structure. The HF adapter `bespokelabs/Bespoke-Nimble-9B` is separately Apache-2.0. A bare "Survey" carries no adoption direction; per the installed direction-scope rule it can fire only this survey's own candidates, and none met the bar — every concept is covered by an installed rule, host territory, or corroboration.

> Refresh pointer (2026-10-22): upstream moved 15 commits past the day-one pin (`d2387fc` → `4edb070`); still no root LICENSE (NB-6 stays open); training data now published in-repo; v2/v3/v4 model family plus Ollama and hosted-API distribution; README timeline and fitted calibration below. The 2026-09-19 verdicts stand unless the refresh section says otherwise.

## Research Question

User instruction: "Survey https://github.com/bespokelabsai/nimble". Three questions: (1) what the artifact is, at a pinned revision; (2) whether its self-claims cohere at docs tier; (3) whether any concept exposes a verified gap on an installed TeaPrompt surface.

## Direct Recommendation (as of 2026-09-19)

- **Study: the benchmark-suite docs and the curation ablation check.** `docs/PUBLIC_BENCHMARKS.md` is an exemplar of the reporting discipline TeaPrompt's records require — pre-registered frozen instruments, a rejected-datasets table with reasons, a limits section that names its own unrun control, and a headline that reports losing to the inspiration. The curation recipe's ablation check (remove each evidence sentence in turn; the focus fact must become unknown) is the sharpest fixture-validity form seen in these surveys.
- **Reproduce: not done.** The checkpoint is ~18 GB, `data/` is gitignored and absent from the repository, and nothing was executed; every number in this record is author-claimed at docs tier.
- **Adopt: nothing.** Bare survey; ten concepts map to installed rules (minimal-pair fixtures, second-method verification, holdout discipline, pre-registration), host territory (serving, structural leak gates, fail-closed CLIs), or corroboration of installed stances.
- **For citers:** no root LICENSE at this pin — plausibly an omission in a day-old repo, but the boundary holds until it changes; README typos ("it's performance", "Nibmle") present at the pin; the adapter directory keeps a disclosed prior project name (`openjeff-diverse9b-v2`); the merge commit is co-authored by an AI model and the suite PR self-describes as "vibe-coded, offered as-is".

## Method

Coordinator reads (2026-09-19), no scouts, no panel: GitHub API (repo metadata, all three commits, recursive tree at the pin — 1,782 entries, tree `3873bf61d82e7441d03763b19ce3a7a0789ad005`); raw files at pin `d2387fc0b32d1173bfc995395c076a25a2a107c9` — `README.md` (full, 555 lines), `AGENTS.md`, `docs/DATASET.md`, `docs/NIMBLE_TRAINING.md`, `docs/PUBLIC_BENCHMARKS.md` (full, including the rejected-datasets tail), the vendored `.agents/skills/typesafe-ai/SKILL.md` head; HF API for the adapter's card data. Local greps re-verified every coverage citation (`ROUTING_CONTRACT.md` R11 and its holdout line, the research skill's State Ledger bullets).

**Scope / acceptance:** pin the revision; read the primary docs in full; map the concept set against installed surfaces; decide every candidate with evidence and a trigger; land nothing without a verified gap; keep the clean-room boundary; run `make all` from the repository root.

## What the Artifact Is

A typed-decision stack over text plus a flat schema (enum fields with 26 one-token codes, boolean fields): the model reads state and fields, and per-field answer-token logits are read out and softmaxed — no generated JSON, no sampling loop. Two scorers ship: a shared-context-prefill parallel scorer (fields scored in parallel branches, mutually blind) and a full-prompt-per-field CUDA scorer; inputs over 2,048 tokens are rejected, never truncated. The adapter is LoRA (r16, seed 17, one epoch, BF16) on a base revision pinned by SHA; loss is cross-entropy over the allowed candidate logits only, and the docs state it "does not train on generated reasoning or teacher probabilities". "Note that we did not distill from Jev." On calibration the README is blunt: "A probability of 0.9 does not mean that the answer is right 90% of the time."

The training data (2,676 contrastive examples plus 150 blind-reviewed, hashes published, `data/` gitignored) comes from a documented contrastive-curation recipe: minimal pairs where an edit of at most eight words flips one focus fact and therefore the label; labels are computed by code applying model-checked rules to model-checked facts; and each example passes an ablation check — remove each evidence sentence in turn and the focus fact must become unknown, proving no other text leaks the answer. The labels are synthetic and model-checked with zero human review, and the docs name the resulting bound themselves: "Separate calls to the same model can make the same mistake, so the checks can miss some errors." The synthetic holdout (324 examples, six source families, disjoint from the 64 training families) carries a standing rule: "Do not tune hyperparameters or select checkpoints on this holdout; derive any future tuning split from the training families only."

On that synthetic holdout the ladder is monotone in scale (Gemma-3-270M 28.70% → Qwen3.5-0.8B 45.37% → 4B 61.42% → 9B base 66.36% → untuned 27B 84.88%), the tuned 9B reaches 90.12%, and Jev 1.13.0 reaches 93.21% — the tuned 9B beats an untuned model three times its size, and the vendor product still leads by 3.09 points. Because the holdout shares the curation pipeline with training, the project built a second instrument: a 13-subset, 3,880-record public suite converted from human-labeled datasets, "so the scorer can be measured against annotations it had no part in creating", with the scope stated: "These converters measure **agreement with human annotation**, not truth." Suite results: macro 74.8% vs Jev's 76.0%; Jev leads significantly on four subsets, Nimble on one; a paired English→German rerun costs Nimble 3.5 points and Jev 0.5; Jev is better calibrated on 11 of 13. Instruments are pre-registered (criteria written before any model ran, identical wording for both models, "and have not been tuned against any split"), builds are seeded, label-blind, family-complete, and byte-reproducible via manifests; a position-bias shuffle control exists but "No shuffled run has been made yet, so position bias is unmeasured." On comparison provenance the docs state: "No vendor-published public-dataset result for Jev exists."

The repo also carries a vendored MIT `typesafe-ai` skill plus a 333-byte `AGENTS.md` routing agents to it — the co-located repo-skill pattern, second production instance after the five in the MiniMax Code survey. Acknowledgments credit TypeSafe, a decoding-mechanics post, the author of the RLCD parallel-constrained-decoding experiment surveyed here on 2026-09-18 ("for inspiring us"), and MiniCheck as prior art "two years early". Claim posture at docs tier: self-consistent, self-deprecating, and unusually explicit about its own bounds; docs-to-code fidelity was not audited.

## Concept Map

Tier is `docs` throughout — the concepts are read from the repository's documentation at the pin; the package source was not audited.

| ID | Concept (clean-room) | TeaPrompt coverage | Disposition |
| --- | --- | --- | --- |
| C1 | Answer-token logit readout over a flat schema; shared-prefill parallel field scoring; reject-don't-truncate input bound | Runtime serving — host territory; mechanism matches the direct-scorer class in the Jev architecture survey | No change |
| C2 | Contrastive minimal-pair curation: a ≤8-word edit flips one focus fact and the label | R11's adversarial-group force and the route-003 trap fixtures are the installed prompt-level form; the fixture-probe lesson ("a stated decision is not an observable") covers the probing side | No change |
| C3 | Ablation validity check: remove each evidence sentence in turn; the focus fact must become unknown — proves the example discriminates on the intended fact | Fixture-curation lessons cover the failure family (a fixture that passes for the wrong reason); no verified local instance of a leaky fixture today | No change — reopen trigger below (NB-2) |
| C4 | Second-method discipline at project scale: a self-checked synthetic holdout is admitted correlated, so an external human-labeled suite measures the scorer against annotations it had no part in creating | The research skill's second-method State Ledger rule and the judge-lifecycle lesson (a model verdict is not a second independent channel) are exactly this | No change — strongest production corroboration yet |
| C5 | Holdout discipline: final reporting only; tuning splits derived from training families | ROUTING_CONTRACT holdout line ("Holdout expansion is maintenance, not proof"), R11, and the holdout-before-tune coverage in the Dream-RSI survey | No change |
| C6 | Artifact-carried contract: the checkpoint ships its schema config with a hash of the scoring-prompt code, and loaders hard-fail on mismatch; checkpoint carries its own inference code, provenance, and checksums | The "seal each compression against the reader" lesson and the record-guard byte-pinning practice are the installed prompt-level form; runtime enforcement is host territory | No change |
| C7 | Pre-registered frozen instrument: criteria written before any model ran, identical for both systems; changing them invalidates the comparison | GW-1 lesson (figures bound to fixture and router revisions) and R11's prohibition on fixture curation | No change |
| C8 | Structural (not textual) reference-leak gate: reject if any reference-bearing key is reachable in the assembled input — string matching is impossible because label strings are legitimate option keys | Dataset-contract engineering, host territory; TeaPrompt's textual clean-room guards remain correct for text artifacts | No change — specimen recorded |
| C9 | Fail-closed CLI semantics: refuse dirty output dirs, refuse resume on manifest mismatch, refuse partial families, fail-loud plugin contracts | Corroborates the governance packs' fail-closed gates; host territory | No change |
| C10 | Reporting hygiene: Wilson intervals, exact McNemar, ECE, limits naming unmeasured controls and unknown contamination, rejected-datasets table with reasons, AI-co-author and "vibe-coded" disclosure, losing-to-inspiration headline | Installed verdict-scope, confound-disclosure, and rejected-alternatives discipline; same class the Jev-vs-diffusion survey recorded | No change — corroboration |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| NB-1 | Minimal-pair fixture wording for R11 or the recipes | No change 2026-09-19 | C2 row: the installed force already requires adversarial groups per token-sharing workflow and recorded probe phrases | Reopen if a router/wording tune passes its fixtures while a one-fact-flip case would have caught the regression |
| NB-2 | Fixture ablation-validity sentence (remove the discriminating fact; the expected answer must become unknown) | No change 2026-09-19 | C3 row: the failure family is covered; no verified local leaky-fixture instance exists to repair | Reopen on the first TeaPrompt fixture found passing for a non-discriminating reason |
| NB-3 | Artifact-carried contract / pre-registration sentences | No change 2026-09-19 | C6/C7 rows: installed as lesson and practice; enforcement is host-owned | None |
| NB-4 | Substrate-count update for the decision-interface ecosystem: fifth open substrate and first company-backed trained full release (Apache adapter, benchmark suite, tracker space); the acknowledgment chain names the author of the RLCD experiment surveyed 2026-09-18 | Noted 2026-09-19 (record-only) | DM-5/MV-6/JA-7 triggers name structural scores exposed to a TeaPrompt-run step — host integration; tool existence is not host integration; the trigger stays unfired, the evidence is re-dated | DM-5 reopens per its own row |
| NB-5 | Co-located repo skill plus router file (second production instance) | Noted 2026-09-19 (record-only) | Pattern corroboration; the MiniMax Code survey already recorded the class | None |
| NB-6 | License-boundary record: unlicensed repo code (concepts only) / Apache-2.0 HF adapter / vendored MIT skill | Noted 2026-09-19 (record-only) | The adoption lens's no-license rule, executed; the split is three-way and each part has its own boundary | Reopen if the repo gains a root LICENSE (day-old repo; plausibly an omission) |

Deterministic guard: `plans/tests/test_nimble_survey_record.py` (identity and tally pins, quote pins, dispositions, clean-room boundary, index links).

## Shared Findings

1. **The decision-interface ecosystem crossed from pastes to a funded release, and the chains connect.** After the AR logit-scoring paste, the trained-heads card, the diffusion canvas readout, and the frozen-weight direct scorer, this is the fifth open substrate and the first with a company behind it — Apache adapter, published recipe, public benchmark suite, and a reproductions-tracker space referencing it. Its acknowledgments name the same experiment author whose card the 2026-09-18 decision-model paste cited. None of this fires DM-5: no TeaPrompt-run host integrates a structural-score step; the trigger's evidence is simply re-dated, again.
2. **The project's central verification move is the installed second-method rule executed at project scale.** It generated its own labels, checked them with the same model class, admitted the correlation in one sentence, and then built a separate human-labeled instrument so the scorer is "measured against annotations it had no part in creating". This is the strongest production corroboration yet recorded for the research skill's second-method rule and the judge-lifecycle lesson.
3. **Independent-eval provenance is stated, not implied.** The docs record that no vendor-published public-dataset result exists for the compared product, that the vendor's own figures average two frontier models rather than human labels, and that the only prior independent eval was a 77-request pilot — the provenance posture TeaPrompt's records require, applied by an external project to its own comparison.
4. **The losing headline is the credibility signal.** The suite reports the inspiration ahead on macro, micro, significance counts, calibration, and cross-lingual robustness, and publishes anyway, with the unrun position-bias control named. A benchmark built to flatter would look different; this corroborates the installed stance that verdict scope and disclosed limits, not favorable numbers, carry the evidentiary weight.
5. **Day-old artifacts demand dated identity.** Repo created the day before the survey, suite merged hours before the pin, "vibe-coded, offered as-is", AI co-author disclosed, typos in place, license missing at root. Every claim here is bounded to `d2387fc0b32d`; churn is expected and NB-6 names the likeliest change.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Repo identity, creation date, tree, no root LICENSE, three commits | Observed | GitHub API, 2026-09-19 |
| Adapter is Apache-2.0, PEFT LoRA on the pinned base, with contract/provenance files | Observed (card data) | HF API at sha `594dfdcfb6f94e3d0c0db7535180d3c71689169a`, 2026-09-19 |
| Scoring mechanism, curation recipe, data hygiene, suite construction rules | Observed at docs tier | Five docs read raw at the pin; package source not audited |
| Holdout ladder (90.12% / 93.21%) and suite results (74.8% / 76.0%, significance, ECE, latency) | Author-claimed | Repository documentation; nothing executed, nothing reproduced |
| Ablation check runs as documented; verify pipeline enforces what it describes | Not verified | Code not audited — the same docs-tier bound the MiniMax Code survey stated |
| "Fifth open substrate; first company-backed trained release" | `[INFERENCE]` (count) | Bounded to substrates recorded across the four prior Jev-ecosystem surveys |
| Benchmark contamination status of either model | Unknown — correctly so | The repo's own limits section says it cannot rule contamination out for either |

## Evidence Actually Checked

- GitHub API: repo metadata, commits (all three), recursive tree at the pin — 2026-09-19.
- Raw at `d2387fc0b32d`: `README.md` (full), `AGENTS.md`, `docs/DATASET.md`, `docs/NIMBLE_TRAINING.md`, `docs/PUBLIC_BENCHMARKS.md` (full), vendored skill head — 2026-09-19.
- HF API: `bespokelabs/Bespoke-Nimble-9B` card data — 2026-09-19.
- Installed-surface greps for every coverage citation and for the survey vocabulary — 2026-09-19.
- Not done: execution or reproduction of any number; `nimble/` package source; the remaining linked docs (`TRY_NIMBLE`, Modal/comparison/parallel-scoring/training-eval guides); the two acknowledged X posts; the HF README prose; the tracker space contents.

## Falsifiability

- Every quantitative claim is author-claimed at docs tier; the record is wrong about the artifact if the code diverges from its docs — the slice a trace-map-style follow-up would settle, as it did for MiniMax Code.
- "No root LICENSE" is a pin-scoped fact in a day-old repo; NB-6 carries the reopen.
- The substrate count is bounded to the recorded surveys; a missed public substrate renumbers Finding 1 without changing the unfired-trigger conclusion.
- Coverage rows cite installed surfaces re-grepped this session; a row is wrong if its cited rule is not found where claimed.
- Finding 4's reading (losing headline as credibility signal) is interpretive; the underlying numbers and disclosures are quoted and pinned.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Revision pinned; identity, license split, and tree recorded | done | this record |
| Five primary docs read in full at the pin; claim posture assessed | done | Method; What the Artifact Is |
| Ten concepts mapped; six candidates decided with evidence and triggers | done | Concept Map; Candidate Adoption Ledger |
| Direction-scope rule applied: bare survey, nothing named fired | done | Research Question |
| Clean-room boundary on installed surfaces | done | guard vocabulary test |
| Guard written | done | `plans/tests/test_nimble_survey_record.py` |
| Decision Index row (at head), case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`; `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |
| Same-day generic direction re-ran the six candidates; none fired; rows unchanged | done | Direction Addendum |

## Direction Addendum (2026-09-19, generic direction)

Same-day follow-up direction: "If worth it then update doca ans skills" (sic) — generic, naming no survey family. Per the installed direction-scope rule it fires only this survey's own candidates; no named hold elsewhere was touched (DM-5/MV-6/JA-7 keep their host-integration triggers).

All six rows re-ran at the worth bar with direction present; none meets the worth bar, and the ledger rows above are byte-unchanged:

- **NB-1** — no verified local gap: R11 already forces one adversarial group per token-sharing workflow with every probed phrase recorded; a minimal-pair sentence would restate the installed force.
- **NB-2** — the ablation move already exists in executed form where TeaPrompt runs fixtures that could leak: the pack guards' stub dry-runs drive a toggling verifier through each gate path (a gate whose outcome does not change when the verifier flips is the defect), and R11 governs route-fixture tunes. No leaky route fixture or vacuous guard has been observed locally; adopting the sentence now would be adoption on external elegance, which §5 Signal Accounting forbids ("external tool exists — no").
- **NB-3** — covered as lesson and byte-pinning practice; enforcement stays host-owned.
- **NB-4/NB-5/NB-6** — record-only notes whose triggers name their own conditions (host integration; an upstream root LICENSE); a generic direction does not fire them.

Direction outcome recorded so it is not re-litigated; the reopen triggers stand as written.

## Latest-version refresh — 2026-10-22

Record-only; no installed change, no wording adopted. All 2026-09-19 dispositions (NB-1..NB-6) stand, including the Direction Addendum outcome.

| Project | Prior baseline (2026-09-19) | Latest checked (2026-10-22) | Release / registry split |
| --- | --- | --- | --- |
| `bespokelabsai/nimble` (branch) | `d2387fc0b32d1173bfc995395c076a25a2a107c9` (2026-09-19, 3 commits) | `4edb0703a2e75d0170c3a45645a1961f4d1a2867` (2026-10-14, Nimble-v3 timeline link, PR #22) | Branch HEAD; no git tags exist (`git ls-remote` tags empty); no GitHub releases queried (API rate-limited) |
| `bespokelabs/Bespoke-Nimble-9B` (HF) | sha `594dfdcfb6f94e3d0c0db7535180d3c71689169a` | sha `bd792f44ec8e265be861bfcdf4e05967ffe0e858`, modified 2026-09-24, 5,366 downloads, 242 likes; tags `original-2676` (first release, `fe33f82`) and `v3-12026`; Apache-2.0 | Registry revision; "v2/v3/v4" are separate models/repos, not tags |
| Nimble model family (HF, new) | Single v1 adapter | `Bespoke-Nimble-9B-v2` (Apache-2.0, 2026-09-23, Ollama-shipped), `Bespoke-Nimble-9B-v3` (CC-BY-NC-4.0, 2026-09-30), `Bespoke-Nimble-27B-v3` (CC-BY-NC-4.0, 2026-10-09), `Nimble-v4-max` (CC-BY-NC-4.0, Qwen3.8-27B finetune, 2026-10-18); v4-9B announced API-only (no public weights found) | License split: v1/v2 Apache-2.0, v3/v4 CC-BY-NC-4.0 |

Actual meaningful changes since the baseline (15 commits, 45 files, +26,362/−282; delta inspected via bare-clone diff; nothing executed):

- **License boundary unchanged (NB-6 stays open).** Root tree at `4edb070` is still `AGENTS.md`-less with no LICENSE file: `.claude-plugin/`, `.gitignore`, `README.md`, `assets`, `data`, `deploy`, `docs`, `examples`, `nimble`, `plugins`, `requirements`, `tests`. The only LICENSE in the tree moved with the skill swap (below). The no-license rule still applies to repo text/code; the HF v1/v2 adapters remain the Apache-2.0 parts.
- **Co-located skill swapped, pattern corroborated twice (NB-5).** The vendored `typesafe-ai` skill and 333-byte `AGENTS.md` router are gone (PR #18); in their place `plugins/nimble/skills/nimble/SKILL.md` (287 lines, MIT, Bespoke-copyrighted) documents the hosted Nimble API (up to 64 typed questions per call: noul/choice/score). The co-located repo-skill pattern the record noted now has two successive instances in one repo; the skill advertises a `score` (ordered-scale) question type the v1 flat schema did not have.
- **Training data published (the record's "absent `data/`" gap closed).** PR #5 (2026-09-20) committed the 2,676 training examples plus the frozen 324-example holdout (`data/train.jsonl`, `data/eval.jsonl`, `data/manifest.json`) — "inadvertently left out earlier". The curation recipe's hashes are now checkable against the actual rows; the ablation-check claim remains docs-tier (verify pipeline not audited here).
- **Serving contract widened.** Prompt limit 2,048 → 8,192 tokens per question (PR #4, trained ≤2,048 so shorter remains better-tested); up to 255 choices per enum field via `nimble/scoring/extended_schema.py` (single-token uppercase code mining; legacy ≤26-choice prompts byte-identical); `serving_schema.py` and release-contract additions; fitted probability temperature (`calibration.py`: T=2.179 for the exact published checkpoint, ECE 0.128 → 0.066, answers unchanged) with `tests/test_calibration.py` — a calibration move on the project's own terms, still host-side mechanism, no effect on DM-6.
- **README timeline (author-claimed ladder, nothing reproduced).** 2026-09-18 v1 → 2026-09-29 Ollama ships v2 (`ollama pull nimble`; registry page HTTP 200, ~30.6k downloads) → 2026-10-06 v3 "#1 open model under 25B on the Decision Index" (54.7 vs Jev 60.1 reference, next open Nace.AI Drex v1.5 at 50.8) → 2026-10-13 v4-9B + v4-max-27B launched on the hosted API with self-run Decision Index public-suite scores (v4-max 68.46 #1 overall; v4-9B 63.70 #1 of 104 under 25B; Jev 1.13 at 57.96; Perplexity Decider v1.1 at 62.25; "not yet on the dashboard"). The record's losing-to-inspiration headline now has a winning successor claimed by the same author on a newer instrument — both author-claimed, both bounded to their batteries.
- **Curation/serving maintenance.** Requesty transport for curation runs, Unicode-separator preservation in training JSONL, checkpoint-default preservation across loaders, CUDA-eval dependency bumps.

Effect on prior findings: Finding 1's "fifth open substrate / first company-backed release" count is now a family (v1→v4, local → Ollama → hosted API) but the DM-5 trigger analysis is unchanged — no TeaPrompt-run host integrates a structural-score step, so tool existence still is not host integration. Finding 4's losing headline stands as a dated 2026-09-19 fact; the v4 winning claim is new author-claimed evidence on a different battery, not a revision of the old numbers. NB-2's reopen (a locally observed leaky fixture) stays unfired.

Inspected immutable links: `https://github.com/bespokelabsai/nimble/commit/4edb0703a2e75d0170c3a45645a1961f4d1a2867`, `https://github.com/bespokelabsai/nimble/commit/d2387fc0b32d1173bfc995395c076a25a2a107c9`, `https://huggingface.co/bespokelabs/Bespoke-Nimble-9B`, `https://huggingface.co/bespokelabs/Bespoke-Nimble-9B-v2`, `https://huggingface.co/bespokelabs/Bespoke-Nimble-9B-v3`, `https://huggingface.co/bespokelabs/Nimble-v4-max`, `https://registry.ollama.com/library/nimble:latest`, `https://console.bespokelabs.ai/`.

Untested limits: no execution (suite, scorers, calibration, Ollama pull); GitHub REST metadata/releases/star counts unavailable (API rate limit, recorded 2026-10-22); Decision Index dashboard not read (scores are README-claimed); v4-9B weights/API behavior not inspected; `nimble/` package source still unaudited beyond the named new files' heads.
