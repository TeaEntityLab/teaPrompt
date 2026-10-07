# arm-blinded-eval-harness — Examples

Companion examples for the domain-pack skill. These show expected output
shapes — blinded-dir layout, refusal behavior, ledger separation — not proof
that a blinded pilot has run. By-construction guarantees only; zero observed
blinded runs yet.

## Example 1 — Blinded extraction layout (two repair pairs)

Input: ticket names pairs `A-code` (candidate `calc.py`, oracle
`fixtures/A-code/oracle.py`) and `B-content` (candidate `report.md`, oracle
`fixtures/B-content/oracle.py`); arms `control` / `treatment`; order
`A-code: control-then-treatment`, `B-content: treatment-then-control`.

Expected output shape:

```text
blinded/
  A-code-a1b2c3.py      # control or treatment — opaque ID, scorer cannot tell
  A-code-d4e5f6.py
  B-content-7a8b9c.md
  B-content-0d1e2f.md
map/sealed-map.json          # host-held; never on the scorer read path
results/scores.jsonl         # per-candidate oracle pass/fail + raw output
results/run-note.json        # order, clone hashes, caps, discarded ledger refs,
                             # noise_floor_basis, failure_categorization, selection_vs_final
```

Unblinding (host only, after scoring):

```json
{
  "A-code-a1b2c3.py": {"pair": "A-code", "arm": "control", "file": "calc.py"},
  "A-code-d4e5f6.py": {"pair": "A-code", "arm": "treatment", "file": "calc.py"}
}
```

Planted-difference check: the arm whose `calc.py` passes the A-code oracle
scores pass, the other scores fail; `scores.jsonl` recovers that pattern only
after the host joins through the sealed map. That recovery checks the harness.
It is not a treatment-effect claim: the run note still names `noise_floor_basis`,
`failure_categorization`, and `selection_vs_final`, and a score difference is
not attributed to treatment while categorization is unresolved. The scorer's
argv, cwd, and captured stdout contain zero arm tokens (grep the invocation
log for `control|treatment`, require zero matches).

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
assertion. The same exit-4 refusal applies when scorer argv references
anything outside `blinded/` (e.g. an arm workdir path) or still contains an
unsubstituted `{CAND}` placeholder.

## Example 3 — Discarded ledger and hold fixture stay out of the denominator

Input: pair `B-content`, treatment arm's first invocation used a wrong CLI
spelling and produced a tool-rejection with no proposal; pair `C-hold` ran its
preflight check.

Expected output shape (`results/run-note.json` fragment):

```json
{
  "order": {"A-code": ["control", "treatment"], "B-content": ["treatment", "control"]},
  "clone_hashes": {"A-code": {"control": "<sha256>", "treatment": "<sha256>"}},
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
