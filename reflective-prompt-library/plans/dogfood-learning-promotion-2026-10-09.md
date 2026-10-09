# Dogfooding Learning Promotion — 2026-10-09

> **Status: accepted in-place updates (non-authoritative record).** The user asked to record docs or update skills where dogfooding showed useful lessons. Three narrow amendments land in existing evaluation packs; no new skill, pack, runtime, campaign grant or host qualification follows.

## Goal and scope

Preserve failure-prevention lessons from the dogfood repairs without turning the
session-local reference consumer into a TeaPrompt product. The contracts live
in `SKILL.md`; this record explains their evidence, destination and limits.

In scope: immutable receipts, complete-versus-censored pair accounting and
host-attributed, task-type-preserving scoring. Out of scope: adopting a host,
executing the held campaign, changing historical scores or reading final
holdouts, adding an owned runner, changing routing/registry membership, early
checkpoint outcomes, commits and pushes.

## Evidence Actually Checked

- The [dogfood plan's residual verification](skill-dogfood-test-plan-2026-10-08.md#residual-advisory-verification-2026-10-09) and [source-bound repair report](../../review/final-report.md#dogfooding-residual-advisory-repair-closure-2026-10-09) retain the original measurement limits and current protocol repairs.
- Historical accounting preserves **18 allocated pairs, six completed comparisons and 12 censored/incomplete comparisons**. The separate prospective regression excludes three diagnostic-only arithmetic pairs from scoring; it does not regrade the original model outputs or turn diagnostic holds into failures.
- The session-local audit writer was repaired to exclusive-create a distinct corrected receipt. Its repeat CLI invocation exited 4 with unchanged prior bytes. The emitted blinded scaffold still had the same overwrite pattern: four isolated output-reuse regressions failed before this amendment, returning 0; a seeded historical scores file was replaced by new scorer rows.
- After repair, the extracted blinded CLI completed a fresh run, refused identical reuse with exit 4 and unchanged workspace hashes, and completed a replay in a new namespace. Existing and dangling-symlink output paths refused without scorer dispatch.
- The unchanged source-pinned reference consumer (`5eee3ea7ca2a…`, scorer version `v4-2026-10-09`) and driver (`67f18ea756a2…`) supplied synthetic protocol checks, not an accepted host. A fresh invocation of the saved parent controls passed **49 checks** with a separate receipt. Direct final-verdict calls rejected boolean `True` and float `1.0` for an expected integer `1`, and a wrong unseen answer; these are stronger than admission-only checks.

The fresh learning smoke passed **13 checks**. Its receipts are retained as
`dogfood-learning-smoke-receipt-2026-10-09.json` and
`dogfood-learning-parent-protocol-receipt-2026-10-09.json` in the private session
artifact directory. The disposable smoke script and fixtures are not product
code. No model/provider calls or untrusted candidate dispatches occurred.

These observations prove bounded CLI and synthetic-protocol mechanics. They do
**not** prove protected actual-host oracle execution, hard-memory containment,
worker/capture isolation, comparative skill efficacy or campaign completion.
The source-bound prior repair records remain dated snapshots, not receipts for
these later skill edits.

## Candidate Adoption Ledger

All three candidates are **agent operating rules**, placed in existing skill
contracts rather than the project-judgement prose layer. Human approval is
**already granted** by the user's 2026-10-09 instruction to record or update
skills if worthwhile. The frozen nine core skills and ten domain-pack registry
entries are unchanged.

| ID | Claim / procedure and evidence | Destination / proposed action | Status | Review / retirement trigger |
| --- | --- | --- | --- | --- |
| DFL-1 | Reuse can overwrite audit evidence: both the historical-audit writer and emitted blinded scaffold exposed this failure. Fresh namespaces and exclusive creation preserve prior bytes and stop repeat scoring. | Amend [arm-blinded-eval-harness](../skills/arm-blinded-eval-harness/SKILL.md) and its [replay example](../skills/examples/arm-blinded-eval-harness.examples.md#example-5--replay-preserves-the-first-run); add a behavioral consumer regression. Golden receipt discipline points to the same protection. | Adopted 2026-10-09 | A host artifact store replaces file receipts with equivalent create-once semantics demonstrated against overwrite/reuse; not merely a shorter warning. |
| DFL-2 | Allocations, completed comparisons and censored/incomplete outcomes are different populations. Historical audit and prospective diagnostic-only classification demonstrate why an absent usable score is not a zero score. | Amend [golden-benchmark-runner](../skills/golden-benchmark-runner/SKILL.md) receipt/allocation discipline, output shape and [classification example](../skills/examples/golden-benchmark-runner.examples.md#example-5--complete-failures-are-not-censored-pairs). | Adopted 2026-10-09 | A changed experimental design predeclares a different estimand and accounting policy; old outputs remain tied to their original oracle. |
| DFL-3 | Candidate-authored results or cap words cannot establish host attribution. Strict task types and final-verdict controls distinguish complete candidate failures from oracle, unknown and censored errors. | Amend the golden pack's scoring procedure and scorer checks; keep protected execution/identity/isolation as host prerequisites, not prompt guarantees. | Adopted 2026-10-09 | A task deliberately changes its type/error semantics, or a qualified host changes the protected-oracle protocol; revalidate admission and final scoring separately. |

The smallest sufficient destination is an existing contract plus its companion
example and, for the emitted overwrite defect, a runnable regression. A new
skill would duplicate these triggers; a TeaPrompt-owned host would cross the
standing runtime non-goal. No managed-skill memory was promoted as authority.

## Applied behavior and limits

- **Blinded receipts:** all four configured output paths must be fresh. The
  scaffold checks reuse before extraction/scoring, creates the blinded
  directory without `exist_ok`, and exclusive-opens all three metadata files
  before dispatch. A failed attempt may leave reserved empty files or partial
  extraction; it remains an attempted namespace, not an in-place retry slot
  (narrowed 2026-10-09 by the [review follow-up](#review-follow-up-validate-before-reserving-the-namespace-2026-10-09):
  a rejected configuration now reserves nothing; the residual applies only to
  failures after extraction began).
  This prevents replacement of existing output paths, not unauthorized writes
  by another actor or a guarantee of atomic multi-file publication.
- **Pair accounting:** keep every allocation, label incomplete/censored arms
  unscored (`score: null`), and compute a delta only when both arms completed
  and are scorable. Discards consume their authorized invocation budget but
  are not additional pairs; the expected-preflight-hold fixture is separate.
- **Error and type semantics:** a protected error counts as completed candidate
  failure only with independent host attribution `error_origin='candidate'`
  and explicit boolean `censored=False`. Censored, oracle-side, unknown or
  missing/invalid attribution stays unscored. Text mentioning “budget” cannot
  create censoring. Complete protected failures override diagnostic
  error/timeout, never a blocked/no-dispatch containment hold. Task-declared
  type checks survive into the final verdict; executable scorer identity and
  the named human semantic scorer remain different fields.

## No-change decisions

Physical directory identity, firmlink/Unicode/case alias controls, restricted
spool writes, process cleanup and native-memory limits remain source-bound
host-engineering evidence in the repair record. They are not new portable
skills or proof that a prompt enforces containment. Existing risk, review,
flow and delivery contracts already own the relevant host-precondition and
side-effect gates; this amendment does not redesign them.

The **2026-10-11 checkpoint** remains user-owned and date-gated. Its P6,
G9/AS9, separate H5/H6 and governed-delivery recurrence/demotion rulings are
still the [runbook's agenda](checkpoint-2026-10-11-runbook.md), not outcomes
created by this learning record.

## Test-integrity corrections

Two incidental wording assertions were removed from the existing consumer
suite, not replaced with new text pins:

- `test_run_note_carries_no_scoring_schedule` no longer requires the `scoring`
  prose to start with `"private shuffled schedule"`. It still proves that
  candidate names from the sealed scoring schedule do not enter the run note.
- `test_documented_config_runs_verbatim_and_recovers_planted_pattern` no longer
  pins the denominator's `"discarded + hold excluded"` explanatory text. It
  still checks `repair_pairs == 2`, the discarded receipt and hold outcome,
  the four planted arm outcomes, and exclusion of the private scoring order.

These are assertion removals, not deleted tests or weakened behavioral
contracts. Schedule privacy, repair-pair accounting and actual scorer outcomes
remain independently checked.

## Source-pinned advisory closure

The permanent consumer suite now covers four existing outputs and four
dangling-symlink outputs, plus a successful first run, same-run refusal and
fresh-namespace replay. Both fixture scorers append to a dispatch marker;
refusals preserve the original artifacts and produce no new extraction or
scorer dispatch. Replaying in a distinct namespace retains the first run's
candidate and receipt bytes and recovers the same planted arm outcomes.

The alleged late output-refusal defect is **already fixed**: `main` checks
`exists() or is_symlink()` before creating the blinded directory, extracting
candidates or dispatching a scorer. Nine focused lifecycle checks passed.
No further contract edit was made for that finding.

A separate actual-CLI smoke passed **11 checks**, using only fixed trusted
fixtures. It compared complete workspace snapshots around refusal and retained
`dogfood-learning-advisory-cli-receipt-2026-10-09.json`. All **63** named prior
source/receipt bindings remained unchanged. The later current-source, gate and
render evidence is in `dogfood-learning-advisory-ledger-2026-10-09.json`; the
initial learning-promotion ledger remains a separate historical snapshot.

The [plan's source-pin supersession](skill-dogfood-test-plan-2026-10-08.md#learning-promotion-supersession-and-future-pins-2026-10-09)
and private manifest distinguish the original P0 pin from the updated harness.
Historical pilot evidence stays bound to its old revision and is not pooled
with future runs. Checkpoint measurement snapshots are inputs only; the dated,
user-owned decisions remain held.

## Verification and consumer coverage

| Consumer / criterion | Observed check | Status |
| --- | --- | --- |
| Direct emitted CLI and preserved artifacts | Fresh run → 0; repeat → 4 with unchanged hashes; fresh-namespace replay → 0; dangling outputs refuse without dispatch | Verified; trusted fixed fixtures only |
| Alternate imported `main` and boundary behavior | `python3 -m pytest reflective-prompt-library/plans/tests/test_arm_blinded_eval_consumers.py -q` — 52 passed, including timeout/partial-output, eight existing/dangling-output cases and same-run/fresh-namespace replay | Verified |
| Final scoring consumer | 49 parent protocol controls; direct final-verdict bool/float/unseen-answer negatives; synthetic allocation classification | Verified within synthetic scope, not host qualification |
| Golden generated runner | No runner is emitted or checked into the repo by this skill; procedures/examples updated, host implementation remains required | Not a runtime implementation claim |
| Core routes, registry and install loops | No name, membership or core routing change | Intentionally unchanged |

Repository discovery, cross-links, record hygiene and rendered-document checks
belong to the [learning-promotion completion report](../../review/final-report.md#dogfooding-learning-promotion-2026-10-09). The existing Python consumer suite
is the permanent behavior guard; there are no prose-presence or incidental
wording tests for these amendments.

## Receipt-writer twin sweep (2026-10-09)

The original exact-variable-name search was too narrow to establish the absence
of structurally similar writers. A project-wide, gitignore-respecting search
covered Python truncating writes, literal/variable-path shell redirects and
`tee`, with a supplemental byte/JavaScript-writer search. Private session
artifacts and ignored upstream clones are outside this population.

The count covers candidate, diagnostic, ledger and developer-export writer
locations, not every generated input or fixture. Temporary test setup,
prompt/backlog mutations, HTML interpolation, Markdown blockquotes and
survey-only upstream quotations are excluded. These are similar write
constructs, not 31 additional immutable-receipt defects. Paths below are
relative to `reflective-prompt-library/`; line numbers are bound to commit
`49cff74` and shift with later edits (the blinded-scaffold rows already have).

TWINS: searched `write_text|open(..., w)|single > output redirects|tee` - found 31 other sites: `skills/flow-control-generator/SKILL.md`, `skills/flow-loop-harness/SKILL.md`, `plans/proposals/arm-blinded-eval-harness-proposal.md`, `plans/benchmark_tasks.py`, `plans/eval_harness.py`, `plans/generate_index.py`, `plans/prompt_composer.py`, `plans/route_paraphrase_eval.py`.

| Surface | Writer locations | Classification and decision |
| --- | --- | --- |
| `skills/flow-control-generator/SKILL.md` | 104, 112, 155, 164, 216, 224, 282, 294, 420, 435, 456 | Mutable step/preflight outputs and DAG ledger; unchanged under its host-honored resume convention, not an immutable archive. |
| `skills/flow-loop-harness/SKILL.md` | 95, 105, 144, 183, 191, 269, 276, 319, 368, 377, 387 | Mutable iteration/preflight outputs and latest verifier capture; unchanged. |
| `plans/proposals/arm-blinded-eval-harness-proposal.md` | 186, 187, 190 | Historical admission record; preserve original scaffold. The registered `skills/arm-blinded-eval-harness/SKILL.md` is the live contract. |
| `plans/benchmark_tasks.py` | 409 | Replaceable benchmark-definition export; unchanged. |
| `plans/eval_harness.py` | 607, 618 | Replaceable developer evaluation reports; unchanged. |
| `plans/generate_index.py` | 265 | Deliberately regenerated discovery index; unchanged. |
| `plans/prompt_composer.py` | 326 | Replaceable composed-prompt export; unchanged. |
| `plans/route_paraphrase_eval.py` | 1173 | Fixed-name routing report regenerated by repository checks; unchanged, not a historical receipt archive. |

**Residual risk:** reusing flow/loop `STATE` can replace working output and
diagnostics; copying the old proposal would restore the obsolete overwrite
pattern. None of these surfaces inherits the blinded scaffold's create-once
receipt guarantee. The corrected blinded runner still does not enforce actor
isolation, crash-safe resume or atomic multi-file publication. Archival
preservation for other workflows remains a host responsibility, not an
unimplemented promise added by this repair.

The later instruction to consider, fix and commit authorizes this evidence
correction and the verified repository commit, not a push or held campaign.
Prior private ledgers and CLI receipts remain historical; current search,
source, gate and rendered-document evidence is retained separately in
`dogfood-twins-commit-ledger-2026-10-09.json`.

## Review follow-up: validate before reserving the namespace (2026-10-09)

A post-commit review of `49cff74` probed the extracted scaffold with rejected
configurations (trusted fixtures, no model calls). Finding, graded Medium and
introduced by the create-once change: `main` created `blinded/` before the
host-held-path, hold/discard, pair, candidate and scorer-argv checks finished,
and the `{CAND}` placeholder check ran after extraction despite the "validate
before copying" comment above it. A configuration typo therefore left an empty
or partially extracted `blinded/`, and the corrected re-run with the same paths
refused as "already exists". Two Low findings: duplicate output paths surfaced
only at the exclusive open, after extraction, as an `Errno 17` message; and the
twin-sweep table above pinned line numbers without a revision anchor.

Repair in the live contract, not the historical proposal: the four output
paths must be distinct and non-nested (exit 4 naming both keys); the
placeholder check moved into the pre-copy validation loop; extraction is
planned and every scorer argv linted before `blinded/` is created; the
candidate containment re-check stays at copy time. Six new consumer
regressions (missing placeholder, metadata inside `blinded/`, duplicate
outputs, nested outputs, late-pair boundary violation, dispatched hold) each
refuse with exit 4 and zero scorer dispatch, leave only the test's own inputs in the
workspace, and then run the corrected CONFIG to completion in the same
namespace. All six failed against the pre-fix scaffold and pass after it. The
Methods bullet, failure signal and replay example state the narrowed limit.

**Advisory correction, same day — output aliases.** An advisory on the first
version of this follow-up noted that `Path.resolve()` cannot fold case for a
file that does not exist yet, so the new distinct-path check would pass
`results/Scores.jsonl` beside `results/scores.jsonl` and fail only at the
exclusive open after extraction. A probe on this volume (case-insensitive
**and** normalization-insensitive, both confirmed by creating one name and
testing the other) reproduced that, and found a worse, **pre-existing** gap:
`sealed_map: "Blinded/sealed-map.json"` passed the inside-`blinded/` check
(same `_within` string comparison in `49cff74` and earlier) and the run
**completed with exit 0** with the sealed map — arm map plus scoring schedule —
inside the scorer-visible directory. The NFC/NFD pair behaved like the case
pair. Repair: a conservative `_fold` identity (resolved parts, NFC-normalized,
case-folded) now drives both the inside-`blinded/` and the distinct/non-nested
checks, so these aliases refuse on every volume before anything is reserved;
output names never need to differ only by case or normalization, so
over-refusal on case-sensitive volumes costs nothing. Three more regressions
(case alias, NFC/NFD alias, case alias into `blinded/`) failed against the
unfolded preflight — the third with exit 0 — and pass now; the consumer suite
is 61 passed. The contract text bounds the guarantee to the alias classes the
preflight checks.

Limits: this is a rejected-configuration guarantee bounded to exact,
case-folded, NFC-normalized and nested path identity. An alias the preflight
cannot see (another actor racing it, exotic filesystem short names) and any
run that fails after extraction began (copy error, scorer launch failure or
timeout) still retain partial artifacts and need a new namespace. File
exclusivity is still not actor isolation or atomic multi-file publication.
Scorer-argv checks were not changed: an aliased argv path is already refused
as outside `blinded/`, which is the safe direction. Two de-pinned wording
assertions (§Test-integrity corrections) still pass against the current text;
keeping them removed is the recorded choice, not a repair.

**Closure correction, same day — unresolved parents and evidence.** A live
symlink-loop probe against `cd5f6e5f…` exited 4 only after creating
`blinded/`, `map/` and `results/`. Removing `_fold`'s lexical fallback alone
did not repair it: on the checked Python 3.14.7, non-strict resolution tolerates
loops. Output identity now strictly resolves existing ancestors, permits only
missing suffix components, and refuses loops or dangling symlink ancestors
before reservation. Fold each output once and compare the cached identities.
Two behavioral regressions cover those parents, zero dispatch, an unchanged
namespace and a successful corrected re-run; both have failing-before evidence.
The final consumer suite passes **63 checks** (52 prior + 9 earlier namespace/
alias cases + 2 parent-resolution cases). Diagnostic wording assertions are
removed; exit/state/dispatch/error-receipt checks remain, and corrected runs
must recover all four planted pair/arm outcomes, not merely emit four rows.

The actual extracted CLI and documented CONFIG refuse both unresolved
parents and all three alias cases without reserving outputs, then recover
the planted outcomes in the corrected namespace. Repeating that successful
CONFIG preserves all prior bytes. These are trusted synthetic checks, zero
model calls, not host-isolation or skill-effect evidence. The final current
source is bound in the test plan and private
`dogfood-review-commit-closure-2026-10-09.json`; prior ledgers keep their own
source and receipt bindings.

Provenance correction: `216abaa3…` was an intermediate uncommitted source used
by offline checks, not an approved campaign/model run. It was incorrect to
call it "never a run input". The explicit later **"Fix all and commit"** grants
the scoped repository commit only; it does not grant a host adoption,
campaign, provider call, settings change, push or early checkpoint outcome.

## Falsifiability

This promotion is wrong or incomplete if a repeated extraction dispatches a
scorer or changes prior bytes; a fresh authorized namespace cannot run; a
configuration the preflight rejects creates any output path; a checked
exact/case-folded/NFC-normalized/nested identity lets a host-held output reach
the scorer-visible directory;
censored/unattributed outcome becomes a complete delta; or task-declared type
semantics disappear between oracle admission and final scoring. Synthetic
signed fixtures falsify protocol defects only. Actual-host enforcement and
skill-effect claims need separate evidence and cannot be rescued by these
passes.

## Remaining work and Human Review

No open implementation item in this narrow learning promotion. TEST-001 still
needs a qualified, designated host and independently protected oracle/capture
evidence. Stage-1/TEST-002–004 still need their explicit campaign envelope,
independently enforced budgets, isolated worker/capture profile and named
owners. The current reference cannot execute candidates on any platform as
written. These blockers are unchanged; the campaign remains **BLOCKED**.
