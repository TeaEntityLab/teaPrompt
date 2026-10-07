# arm-blinded-eval-harness — Examples

Companion examples for the domain-pack skill. These show expected output
shapes — blinded-dir layout, private scoring schedule, boundary refusals,
ledger separation — not proof that a blinded pilot has run. By-construction
guarantees only; zero observed blinded runs yet.

## Example 1 — Blinded extraction layout with private scoring schedule

Input: ticket names pairs `A-code` (candidate `calc.py`, oracle
`fixtures/A-code/oracle.py`) and `B-content` (candidate `report.md`, oracle
`fixtures/B-content/oracle.py`); arms `control` / `treatment`; public
execution order `A-code: control-then-treatment`,
`B-content: treatment-then-control`; omit `scoring_seed` to derive it privately.

Extraction iterates arms in sorted canonical order — never the public
execution order — and each copy gets a random opaque ID:

```text
blinded/
  A-code-a1b2c3.py      # control or treatment — opaque ID, scorer cannot tell
  A-code-d4e5f6.py
  B-content-7a8b9c.md
  B-content-0d1e2f.md
map/sealed-map.json          # host-held; never on the scorer read path
results/scores.jsonl         # per-candidate oracle pass/fail + raw output (scoring order)
results/run-note.json        # public order provenance only — no scoring schedule
```

Unblinding (host only, after scoring) — the scoring schedule lives in the
sealed map, never in the run note:

```json
{
  "candidates": {
    "A-code-a1b2c3.py": {"pair": "A-code", "arm": "control", "file": "calc.py"},
    "A-code-d4e5f6.py": {"pair": "A-code", "arm": "treatment", "file": "calc.py"}
  },
  "scoring_order": ["B-content-0d1e2f.md", "A-code-a1b2c3.py", "A-code-d4e5f6.py", "B-content-7a8b9c.md"],
  "scoring_seed": "<host-private-seed>",
  "scoring_seed_source": "derived"
}
```

For a synthetic order-independence check, use the same host-held replay
`scoring_seed` in two configs, never disclose it to the scorer, and swap public
`order`. This yields the identical sealed scoring arm sequence
while the public order differs, so an ordinal-only predictor reading the
public order (`inferred_arm = order[ordinal]`) cannot be correct in both
runs. One failed or successful guess proves nothing in either direction —
the guarantee is the order-independent schedule, not any predictor's hit
rate. Creation sequence matching the public order in one pair is
irrelevant: scoring walks the shuffled schedule, never creation order.

Planted-difference check: the arm whose `calc.py` passes the A-code oracle
scores pass, the other scores fail; `scores.jsonl` recovers that pattern only
after the host joins through the sealed map. That recovery checks content
reading — the positive control that scoring still distinguishes candidates.
It is not a treatment-effect claim: the run note still names
`noise_floor_basis`, `failure_categorization`, and `selection_vs_final`,
and a score difference is not attributed to treatment while categorization
is unresolved. The scorer's argv, cwd, and captured stdout contain zero arm
tokens (grep the invocation log for `control|treatment`, require zero
matches).

## Example 2 — Label leak refuses before scoring (exit 4)

Input: extraction produced `blinded/A-code-treatment-7a8b9c.py` (arm token in the
scorer-visible filename).

Expected output shape:

```text
$ python3 eval-harness/run_blinded_eval.py config.json
label leak: A-code-treatment-7a8b9c.py
$ echo $?
4
```

No oracle runs; `results/scores.jsonl` is not written. The fix is at
extraction time (opaque IDs, no arm token), never by editing the
assertion. The same exit-4 refusal applies when scorer argv still contains
an unsubstituted `{CAND}` placeholder, when a host-held output
(sealed map, results, run note) resolves inside `blinded/`, or when the
config misses a required key.

## Example 3 — Scorer code/data boundary refusals (exit 4, zero dispatch)

Setup: ticket declares trusted scorer code
`"scorer_code": ["python3", "fixtures/A-code/oracle.py"]`. The oracle is a
sentinel that appends one line to `evidence/dispatch-count.txt` every time
it runs. Each case below must print its refusal on stderr, exit 4, and leave
the sentinel counter untouched — the harness validates every oracle argv for
every candidate BEFORE any scorer dispatch, so a late-pair violation never
scores early pairs first.

Outsider data arg (an extra file outside `blinded/` and outside both arm
dirs, read as `sys.argv[2]`):

```text
$ python3 eval-harness/run_blinded_eval.py config-outsider.json
scorer data outside blinded/: /tmp/scratch/outside-input.txt
$ echo $?
4
```

Arm-dir data arg (a candidate-workdir file smuggled in as argv):

```text
$ python3 eval-harness/run_blinded_eval.py config-armdir.json
scorer argv references arm dir: arms/A-code/control/calc.py
$ echo $?
4
```

Config data arg (the run's own config handed to the oracle):

```text
$ python3 eval-harness/run_blinded_eval.py config-selfref.json
scorer argv references host-held path: ... config-selfref.json ...
$ echo $?
4
```

Sealed-map metadata arg (scoring schedule handed to the oracle):

```text
$ python3 eval-harness/run_blinded_eval.py config-sealedref.json
scorer argv references host-held path: ... map/sealed-map.json ...
$ echo $?
4
```

Undeclared code path: the same oracle without its script in `scorer_code`
refuses too — trust is declared in the ticket, not inferred from file shape.

Clean positive control (declared code + `{CAND}`-only data) scores exit 0
with `repair_pairs: 2` in the run note. And argv lint is not isolation: even
the clean run's note records `scorer_isolation` as a host precondition —
filesystem/network containment of the scorer is enforced by the host
sandbox, never by this argv check.

## Example 4 — Discarded ledger and hold fixture stay out of the denominator

Input: pair `B-content`, treatment arm's first invocation used a wrong CLI
spelling and produced a tool-rejection with no proposal; pair `C-hold` ran its
preflight check.

Expected output shape (`results/run-note.json` fragment):

```json
{
  "order": {"A-code": ["control", "treatment"], "B-content": ["treatment", "control"]},
  "clone_hashes": {"A-code": {"control": "<sha256>", "treatment": "<sha256>"}},
  "scoring": "private shuffled schedule in sealed map; ordinal carries no arm information",
  "scorer_isolation": "host-precondition: argv lint only; filesystem/network isolation of the scorer from arm dirs, config, and the sealed map is enforced by the host, not by this scaffold",
  "discarded": [
    {"pair": "B-content", "arm": "treatment", "cause": "wrong CLI spelling",
     "receipt": "evidence/task005/malformed-1.out", "rerun": true}
  ],
  "hold": {"pair": "C-hold", "exit": 4, "dispatched": false, "verdict": "stale"},
  "denominator": {"repair_pairs": 2, "note": "discarded + hold excluded"},
  "noise_floor_basis": "single-run caveat: no score difference claimed in this note",
  "failure_categorization": "no treatment attribution in this note",
  "selection_vs_final": "not-a-final-claim",
  "disclosure": "by-construction blinding only; zero observed blinded runs yet"
}
```

Repair outcome stays pair-level (n = 2: `A-code`, `B-content`). The malformed
invocation costs budget (decrements the ticket's invocation cap) but never
enters the denominator; a ledger entry without a raw receipt invalidates the
run note. `C-hold` is reported separately — expected `stale` exit 4, zero
dispatch — never merged into `scores.jsonl` or the repair-pair denominator.
