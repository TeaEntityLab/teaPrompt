---
name: arm-blinded-eval-harness
description: Use when running a with/without-skill pilot on paired repair fixtures and the scorer must not see arm labels. It emits a paired-arm evaluation scaffold — fixture cloning, alternated arm order, treatment-only artifact exclusion, label-stripped candidate extraction into a blinded dir, deterministic scorer invocation, and a discarded-invocation ledger kept separate from the denominator. By-construction guarantees only; zero observed blinded runs yet.
license: MIT
compatibility: Requires paired repair fixtures and a deterministic scorer; by-construction guarantees only — zero observed blinded runs yet.
metadata:
  risk_level: medium
  human_review_required: true
  external_io: false
  context_load: low
---

# Arm-Blinded Eval Harness

**Type:** Domain-pack skill (evaluation harness) — registered in the TeaPrompt source repo's domain-pack registry (`plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS`), not one of the nine frozen core workflow skills, and not selected by `reflective-dispatch` route rows; the host harness may invoke it directly.

## Purpose

Close the three confounds recorded in the TASK-005 pilot so a future with/without-skill pilot can be read at face value:

1. The scorer saw arm labels at extraction time (arm names in file paths).
2. The arms differed in model *and* guidance (composite, not isolated skill effect).
3. A single run per arm (directional single-case evidence only).

This pack fixes confound 1 by construction (blinded extraction directory plus a sealed arm↔candidate map the scorer never reads). It bounds confound 2 by requiring identical model/CLI/profile/caps across arms and recording every remaining treatment-only difference as a reported factor, not a skill-attributed effect. It does not fix confound 3 — the scaffold runs one pass per arm per pair unless the task ticket predeclares repeats, and the run note keeps the directional-only limit.

## Module Contract

### Trigger

- A with/without-skill pilot on predeclared private repair fixtures plus one expected-preflight-hold fixture, each cloned identically for two arms.
- A deterministic oracle/verifier exists per fixture and runs without model calls.
- The task ticket names the candidate surface per fixture (which file is scored).

### Inputs

- Predeclared fixture seeds + per-fixture candidate file names + deterministic oracle commands (ticket-owned, immutable during the run).
- Same configured model/CLI/profile and equal call/time/cost caps for both arms.
- Named artifact owner and named accepter for the pilot outcome.

### Methods

- Fixture cloning: the caller copies each fixture once per arm from a read-only seed, records seed hashes, and verifies identical start states before dispatch (exit 4 on mismatch). Arms never share a workdir. The extraction scaffold records `final_state_hashes` after the arms ran; these are not clone-equality evidence.
- Alternated arm order: pair A runs control-then-treatment, pair B runs treatment-then-control (or the ticket's declared alternation); order is written to the run note as observed execution provenance only — it never influences extraction or scoring order, and claiming it cancels order effects is forbidden.
- Treatment-only artifact exclusion: only the ticket-named candidate files are extracted for scoring. Skill guidance, workflow scripts, ledgers, and inspectable state stay out of the blinded dir — they are reported factors, not scored surface.
- Label-stripped extraction: each final candidate is copied to `blinded/<pair>-<id>.ext` (random opaque IDs, no arm token); extraction iterates arms in sorted canonical order, never the public execution order, so creation sequence carries no provenance. The arm↔ID map is written to a host-held file outside the scorer's read path.
- Private scoring schedule: scoring walks a shuffled candidate order drawn from `scoring_seed` (ticket-declared, or harness-derived and recorded when omitted). The schedule is stored in the sealed map only — never in the run note, scores, or any scorer-visible path — so an ordinal-only predictor reading the public order guesses at chance by construction.
- Deterministic scorer invocation with a code/data boundary: each oracle's `argv[0]` plus the ticket-declared `scorer_code` entries are trusted scorer code; every other argv entry is candidate data. After `{CAND}` substitution the harness validates every oracle argv for every candidate BEFORE any scorer dispatch and refuses (exit 4) when any entry names an arm label, an arm dir, the config, sealed/results/run-note paths, or anything outside `blinded/`. Fixed options belong in the trusted scorer script, not undeclared data argv. argv lint is not filesystem isolation (see Honest Limits).
- Discarded-invocation ledger: malformed or environment-incomplete invocations (wrong CLI spelling, tool-rejection with no proposal) are logged with raw receipts and re-run; they never enter the pair denominator. The denominator stays fixture-pair level (n = number of repair pairs).
- Immutable run artifacts: use a fresh `blinded/` directory and fresh sealed-map, score and run-note files. Existing paths refuse with exit 4 before extraction or scoring; metadata files are exclusive-created before scorer dispatch. A replay or corrected audit uses a new output namespace and retains the original receipts.
- Validate before reserving: require four fresh, distinct, non-nested outputs without parent-traversal components, using resolved paths plus conservative NFC/case folding; unresolved identity refuses, never falls back to lexical identity. Finish config, candidate-path and scorer-argv preflight before creating `blinded/`, so a preflight refusal reserves nothing and its correction may reuse the namespace. This covers those checked alias classes, not racing actors or filesystem-specific aliases; failures after extraction starts retain partial artifacts and require a fresh namespace.

### Never

- Never let a blinded path or scorer input contain an arm label (`control`, `treatment` — the ARM_TOKENS tuple) — refuse with exit 4 before scoring; arm *indices* are not tokens (digits false-positive everywhere) and are prevented by not appearing in candidate filenames.
- Never derive extraction order or scoring order from the public execution order — extraction is sorted-canonical, scoring is seed-shuffled; the run note records the public order as provenance only.
- Never record the scoring schedule outside the sealed map — no scoring order in the run note, scores, or scorer-visible paths; host-held outputs (sealed map, results, run note) must not resolve inside `blinded/` (exit 4).
- Never dispatch any scorer before every oracle argv for every candidate passes the code/data boundary — a late-pair violation must not score early pairs first.
- Never let scorer argv reference anything outside `blinded/` except declared trusted code (`argv[0]` plus `scorer_code`) — refuse with exit 4.
- Never treat argv lint as scorer isolation — filesystem/network containment of the scorer is a host precondition, not a scaffold guarantee.
- Never count a discarded invocation in the pair denominator; a ledger entry without a raw receipt invalidates the run note — do not score.
- Never merge the hold fixture into the repair-pair denominator — it is reported separately (expected `stale` exit 4, zero dispatch).
- Never present arms that ran different models/CLIs/profiles as a skill-effect comparison — that output is composite; record it as a pilot defect.
- Never claim alternated order cancels order effects — report order as observed sequence; two pairs cannot separate order effects from fixture-order interaction.
- Never present by-construction path-shape assertions as observed blinding evidence — every run note carries the zero-observed-runs disclosure until a real pilot lands.
- Never launder candidate content — content that names its arm is out of scope for the harness; the ticket must forbid arm-identifying content in candidates.
- Never let a run note attribute a score difference to the treatment without a named noise-floor basis (repeated-baseline spread, or an explicit single-run caveat) and without ruling out noise, grader error, harness failure, and task impossibility.
- Never cite a score used to select a winner as a reportable final gain — selection and final measurements are separate populations; a final claim needs an untouched final evaluation.

### Output

- `eval-harness/run_blinded_eval.py` (stdlib only; emitted scaffold, §Emitted Scaffold in `TEMPLATES.md`).
- `blinded/` (label-free candidates), `map/sealed-map.json` (host-held: `candidates` arm map + private `scoring_order` + `scoring_seed`/`scoring_seed_source`), `results/scores.jsonl` (per-candidate oracle pass/fail + captured output, in scoring order; scorer execution errors have `exit: null` and an `error` class, not a product-failure score), `results/run-note.json` (public execution-order provenance, `final_state_hashes`, declared caps, discarded ledger refs, declared `noise_floor_basis`, `failure_categorization` verdict, `selection_vs_final` flag, scorer-isolation precondition, and `scorer_error` if scoring stopped).
- C-hold pair reported separately: expected `stale` exit 4, zero dispatch — never merged into the repair-pair denominator.

### Escalation

- Model/CLI/profile differ between arms → stop: composite, not a skill-effect reading; record as pilot defect, do not score as comparison.
- Oracle needs judgment (no deterministic pass/fail) → this harness does not apply; route to an LLM-judge design with its own blinding.
- Hold fixture dispatches work → containment finding; route to host owner, not to an oracle edit (ticket falsifiability rule).
- Missing acceptance criterion or unsigned intent → hold, `stop_and_repair`.

### Failure signals

- Any blinded path contains an arm label (`control`, `treatment`) → exit 4 before scoring.
- Any oracle argv entry (after `{CAND}` substitution) names an arm label, an arm dir, the config, sealed/results/run-note paths, or any existing path outside `blinded/` — unless it is `argv[0]` or declared `scorer_code` — → exit 4 before ANY scorer dispatch.
- A host-held output (sealed map, results, run note) resolves inside `blinded/`, including by a case or normalization alias such as `Blinded/sealed-map.json` → exit 4 (schedule metadata must stay off the scorer read path).
- Missing required config key, malformed arm_dirs/candidates/oracle, an oracle missing the `{CAND}` placeholder, an unsubstituted `{CAND}`, parent-traversing output paths, duplicate/nested output paths (including case or Unicode-normalization aliases), or unresolved output identity → exit 4 before any output path is created.
- Absolute, parent-traversing, missing, or symlink-escaping candidate paths, or a hold record other than `stale` exit 4 with `dispatched: false` → exit 4 before extraction/scoring.
- Scorer launch failure or timeout → exit 4; preserve completed rows and the execution-error receipt, halt further scoring, and never interpret incomplete scoring as product failure.
- Seed hash mismatch between clones (caller-side clone check) → exit 4 (clones not identical); do not score.
- Discarded invocation missing raw receipt → run note incomplete; do not score.
- A score difference is attributed to treatment with `noise_floor_basis` missing or `failure_categorization` unresolved → measurement misreport; do not score, repair the run note.

### Verification

- Content-reading positive control: run the emitted harness on the documented CONFIG verbatim with a planted scoreable difference (one arm's `calc.py` passes the A-code oracle, the other fails it; one B-content report keeps all three headings, the other drops one). `results/scores.jsonl` must recover the planted pass/fail pattern after host unblinding via the sealed map, with denominator `repair_pairs: 2` and the discarded ledger + C-hold outside it.
- Order-independence (by construction, not a chance guess): run twice with the same `scoring_seed` and swapped public `order`; the sealed `scoring_order` arm sequence must be identical across runs while the public order differs, so an ordinal-only predictor reading public order cannot be correct in both runs. The run note must not contain the scoring schedule.
- Boundary negatives: outsider-file, arm-dir, config-file, and sealed-map data args each refuse with exit 4 and zero scorer dispatch (the oracle sentinel never runs); an undeclared scorer-code path refuses; the declared clean CONFIG scores exit 0.
- Audit captured stdout/stderr in the emitted `results/scores.jsonl` for arm tokens and require zero matches. Argv is checked before dispatch; cwd/filesystem/network isolation requires separate host evidence, not a nonexistent invocation log.

## Emitted Scaffold

Emit `eval-harness/run_blinded_eval.py` plus its runnable `CONFIG` from the
co-installed `TEMPLATES.md` in this skill's package directory (installed at
`<skills-root>/arm-blinded-eval-harness/TEMPLATES.md` when the package is
copied); it travels with `SKILL.md` outside the TeaPrompt checkout. Read that
sibling when the pilot needs the scaffold or CONFIG; emit both exactly as
written there, with the private-seed and C-hold notes beside them still
applying.

## Honest Limits

- **Disclosure (required in every run note):** the emitted harness guarantees are by-construction only — path-shape assertions plus a scorer argv confined to `blinded/` plus a seed-shuffled private scoring schedule. Zero observed blinded runs exist yet; the first real pilot is the first evidence, and its receipts may reveal leaks this scaffold does not catch (e.g. candidate *content* that names its arm — content laundering is out of scope; the ticket must forbid arm-identifying content in candidates).
- **Scorer isolation is a host precondition, not a scaffold guarantee:** argv lint refuses declared-shape leaks (arm labels, arm dirs, config/metadata paths, outside-`blinded/` files) before dispatch, but it cannot seal filesystem access — an oracle running with a permissive cwd can still open the sealed map, arm dirs, or the network. The run note records this precondition; a containment claim needs host sandbox evidence.
- Same-model requirement is a stop gate, not a repair: if the arms ran different models (as in the 2026-10-06 pilot: `devin swe-2-max` vs `ollama qwen2.5-coder:1.5b`), the output is a composite reading, and this harness refuses to present it as a skill effect.
- One pass per arm per pair unless the ticket predeclares repeats: directional single-case evidence only. Alternated order is reported, not claimed canceled — two pairs cannot separate order effects from fixture-order interaction.
- A single ordinal guess is evidence of nothing in either direction: one failed or successful ordinal-only prediction is not blinding proof — the guarantee is the order-independent scoring schedule, verified by the swapped-order run, not by any predictor's hit rate.
- Provider invocations in the pilot ran host-side; a sandboxed *model* worker has zero containment evidence.
- Discarded-invocation re-runs cost budget: each re-run decrements the ticket's declared invocation cap. Ledger entries without raw receipts invalidate the run note.

## Examples

Companion examples live in the installed `<skills-root>/examples/arm-blinded-eval-harness.examples.md` tree when examples are co-installed. They show the blinded-dir shape, the private scoring schedule, the code/data boundary refusals, and the discarded-ledger/hold separation, not proof that a blinded pilot has run.

## Prompt Sources

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill is self-contained.*

- `reflective-prompt-library/plans/proposals/arm-blinded-eval-harness-proposal.md` (historical admission record; the live scaffold is in `TEMPLATES.md`)
- `reflective-prompt-library/plans/runtime-skills-task001-ticket-2026-10-06.md` (TASK-005 confounds, receipts, invocation cap)
- `reflective-prompt-library/plans/runtime-skills-workflow-spec-2026-10-06.md` (TASK-005 row: per-pair repair outcome, alternated order, blinded deterministic scorer)
