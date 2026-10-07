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

- Fixture cloning: copy each fixture once per arm from a read-only seed; record seed hash per clone. Arms never share a workdir.
- Alternated arm order: pair A runs control-then-treatment, pair B runs treatment-then-control (or the ticket's declared alternation); order is written to the run note as observed sequence, not as a canceled effect.
- Treatment-only artifact exclusion: only the ticket-named candidate files are extracted for scoring. Skill guidance, workflow scripts, ledgers, and inspectable state stay out of the blinded dir — they are reported factors, not scored surface.
- Label-stripped extraction: each final candidate is copied to `blinded/<pair>-<id>.ext` (random opaque IDs, no arm token and no sequential order leakage); the arm↔ID map is written to a host-held file outside the scorer's read path.
- Deterministic scorer invocation: the oracle runs with argv pointing only into `blinded/`; scorer stdout/stderr is captured per candidate. No scorer input path may contain an arm label — the harness asserts this before scoring and refuses (exit 4) if any blinded path leaks one.
- Discarded-invocation ledger: malformed or environment-incomplete invocations (wrong CLI spelling, tool-rejection with no proposal) are logged with raw receipts and re-run; they never enter the pair denominator. The denominator stays fixture-pair level (n = number of repair pairs).

### Never

- Never let a blinded path or scorer input contain an arm label (`control`, `treatment` — the ARM_TOKENS tuple) — refuse with exit 4 before scoring; arm *indices* are not tokens (digits false-positive everywhere) and are prevented by not appearing in candidate filenames.
- Never let scorer argv reference anything outside `blinded/` — refuse with exit 4.
- Never count a discarded invocation in the pair denominator; a ledger entry without a raw receipt invalidates the run note — do not score.
- Never merge the hold fixture into the repair-pair denominator — it is reported separately (expected `stale` exit 4, zero dispatch).
- Never present arms that ran different models/CLIs/profiles as a skill-effect comparison — that output is composite; record it as a pilot defect.
- Never claim alternated order cancels order effects — report order as observed sequence; two pairs cannot separate order effects from fixture-order interaction.
- Never present by-construction path-shape assertions as observed blinding evidence — every run note carries the zero-observed-runs disclosure until a real pilot lands.
- Never launder candidate content — content that names its arm is out of scope for the harness; the ticket must forbid arm-identifying content in candidates.
- Never let a run note attribute a score difference to the treatment without a named noise-floor basis (repeated-baseline spread, or an explicit single-run caveat) and without ruling out noise, grader error, harness failure, and task impossibility.
- Never cite a score used to select a winner as a reportable final gain — selection and final measurements are separate populations; a final claim needs an untouched final evaluation.

### Output

- `eval-harness/run_blinded_eval.py` (stdlib only; emitted scaffold, §Emitted Scaffold).
- `blinded/` (label-free candidates), `map/sealed-map.json` (host-held arm map), `results/scores.jsonl` (per-candidate oracle pass/fail + raw output), `results/run-note.json` (order, clone hashes, declared caps, discarded ledger refs, declared `noise_floor_basis`, `failure_categorization` verdict, `selection_vs_final` flag).
- C-hold pair reported separately: expected `stale` exit 4, zero dispatch — never merged into the repair-pair denominator.

### Escalation

- Model/CLI/profile differ between arms → stop: composite, not a skill-effect reading; record as pilot defect, do not score as comparison.
- Oracle needs judgment (no deterministic pass/fail) → this harness does not apply; route to an LLM-judge design with its own blinding.
- Hold fixture dispatches work → containment finding; route to host owner, not to an oracle edit (ticket falsifiability rule).
- Missing acceptance criterion or unsigned intent → hold, `stop_and_repair`.

### Failure signals

- Any blinded path contains an arm label (`control`, `treatment`) → exit 4 before scoring.
- Scorer argv references anything outside `blinded/` → exit 4.
- Seed hash mismatch between clones (caller-side clone check) → exit 4 (clones not identical); do not score.
- Discarded invocation missing raw receipt → run note incomplete; do not score.
- A score difference is attributed to treatment with `noise_floor_basis` missing or `failure_categorization` unresolved → measurement misreport; do not score, repair the run note.

### Verification

- Run the emitted harness on two synthetic arms where the scoreable difference is planted (e.g. one candidate passes the A-code oracle, the other fails it; one B-content report keeps all three headings, the other drops one).
- Check the scorer's argv, cwd, and captured stdout contain no arm labels: grep the full scorer invocation log for the arm tokens and require zero matches.
- Check `results/scores.jsonl` recovers the planted pass/fail pattern after unblinding via the sealed map, and the discarded ledger holds the planted malformed invocation outside the denominator.

## Emitted Scaffold

`eval-harness/run_blinded_eval.py` (Python stdlib only; host-executed):

```python
#!/usr/bin/env python3
"""Paired-arm blinded eval scaffold. By-construction blinding only; no observed runs yet.
Usage: run_blinded_eval.py <config.json>  (see CONFIG below)
config: {pairs: [{id, seed, candidates: [relpaths], oracle: [argv...]}],
          arms: ["control", "treatment"], order: {pair: [arm...]},
          arm_dirs: {pair: {arm: path}}, blinded: path, sealed_map: path,
          results: path, run_note: path,
          noise_floor_basis: str|omit, failure_categorization: str|omit,
          selection_vs_final: str|omit,
          discarded: [{pair, arm, cause, receipt, rerun}]|omit,
          caps: {pair: {arm: {calls, time_s, cost}}}|omit,
          hold: {pair, exit, dispatched, verdict}|omit}
Oracle argv uses {CAND} for the blinded candidate path. Scorer never sees arm dirs.
"""
import hashlib, json, secrets, shutil, subprocess, sys
from pathlib import Path

ARM_TOKENS = ("control", "treatment")

def sha256_dir(root: Path) -> str:
    h = hashlib.sha256()
    for p in sorted(root.rglob("*")):
        if p.is_file():
            h.update(p.relative_to(root).as_posix().encode())
            h.update(p.read_bytes())
    return h.hexdigest()

def main(cfg_path: str) -> int:
    cfg = json.loads(Path(cfg_path).read_text())
    blinded = Path(cfg["blinded"]); blinded.mkdir(parents=True, exist_ok=True)
    sealed, scores = {}, []
    discarded = list(cfg.get("discarded") or [])
    hold = cfg.get("hold") if isinstance(cfg.get("hold"), dict) else None
    if hold and hold.get("dispatched"):
        print("hold fixture dispatched work", file=sys.stderr)
        return 4
    for entry in discarded:
        if not isinstance(entry, dict) or not entry.get("receipt"):
            print("discarded invocation missing raw receipt", file=sys.stderr)
            return 4
    hold_id = hold.get("pair") if hold else None
    clone_hashes = {}
    for pair in cfg["pairs"]:
        pid = pair["id"]
        if pid == hold_id:
            continue
        order_arms = cfg["order"].get(pid, [])
        if sorted(order_arms) != sorted(cfg["arms"]) or len(order_arms) != len(cfg["arms"]):
            print(f"order for pair {pid} must be a permutation of arms {cfg['arms']}", file=sys.stderr)
            return 4
        # Provenance only: these are *final* arm states, expected to differ as
        # the arm effect. Start-state clone equality is checked at clone time
        # by the caller (exit 4 on mismatch); the hashes are recorded here.
        clone_hashes[pid] = {arm: sha256_dir(Path(cfg["arm_dirs"][pid][arm]))
                             for arm in cfg["arms"]}
        for arm in cfg["order"][pid]:
            for cand in pair["candidates"]:
                cand_id = secrets.token_hex(6)
                dest = blinded / f"{pid}-{cand_id}{Path(cand).suffix}"
                shutil.copyfile(Path(cfg["arm_dirs"][pid][arm]) / cand, dest)
                sealed[dest.name] = {"pair": pid, "arm": arm, "file": cand}
    # Blinding assertion: no arm token anywhere in the scorer-visible surface.
    for p in blinded.iterdir():
        if any(t in p.name.lower() for t in ARM_TOKENS):
            print(f"label leak: {p.name}", file=sys.stderr)
            return 4
    arm_dir_strs = [str(Path(d)) for per in cfg["arm_dirs"].values()
                    for d in per.values()]
    for pair in cfg["pairs"]:
        if pair["id"] == hold_id:
            continue
        if not any("{CAND}" in str(a) for a in pair["oracle"]):
            print(f"oracle for pair {pair['id']} missing {{CAND}} placeholder", file=sys.stderr)
            return 4
        for name, meta in sealed.items():
            if meta["pair"] != pair["id"]:
                continue
            argv = [a.replace("{CAND}", str(blinded / name)) for a in pair["oracle"]]
            flat = " ".join(argv)
            if "{CAND}" in flat:
                print("unsubstituted {CAND} in oracle argv", file=sys.stderr)
                return 4
            if any(t in flat.lower() for t in ARM_TOKENS):
                print(f"arm label in scorer argv: {flat}", file=sys.stderr)
                return 4
            if any(d in flat for d in arm_dir_strs):
                print(f"scorer argv references arm dir: {flat}", file=sys.stderr)
                return 4
            r = subprocess.run(argv, capture_output=True, text=True, timeout=300)
            scores.append({"candidate": name, "exit": r.returncode,
                           "stdout": r.stdout[-2000:], "stderr": r.stderr[-2000:]})
    for path in (cfg["sealed_map"], cfg["results"], cfg["run_note"]):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(cfg["sealed_map"]).write_text(json.dumps(sealed, indent=2))
    Path(cfg["results"]).write_text("".join(json.dumps(s) + "\n" for s in scores))
    repair_ids = [p["id"] for p in cfg["pairs"] if p["id"] != hold_id]
    note = {"order": cfg["order"], "clone_hashes": clone_hashes,
            "caps": cfg.get("caps") or "not declared",
            "discarded": discarded,
            "hold": hold,
            "denominator": {"repair_pairs": len(repair_ids),
                            "note": "discarded + hold excluded"},
            "noise_floor_basis": cfg.get("noise_floor_basis") or "missing",
            "failure_categorization": cfg.get("failure_categorization") or "unresolved",
            "selection_vs_final": cfg.get("selection_vs_final") or "not-a-final-claim",
            "disclosure": "by-construction blinding only; zero observed blinded runs yet"}
    Path(cfg["run_note"]).write_text(json.dumps(note, indent=2))
    # Scorer-log label audit: caller greps results + invocation log for ARM_TOKENS.
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
```

`CONFIG` (checked into the pilot ticket, immutable during the run):

```json
{
  "pairs": [
    {"id": "A-code", "candidates": ["calc.py"],
     "oracle": ["python3", "fixtures/A-code/oracle.py", "{CAND}"]},
    {"id": "B-content", "candidates": ["report.md"],
     "oracle": ["python3", "fixtures/B-content/oracle.py", "{CAND}"]}
  ],
  "arms": ["control", "treatment"],
  "order": {"A-code": ["control", "treatment"], "B-content": ["treatment", "control"]}
}
```

C-hold is not a scored pair: its acceptance is `stale` exit 4 with zero dispatch, recorded in the run note outside `scores.jsonl` and outside the denominator.

## Honest Limits

- **Disclosure (required in every run note):** the emitted harness guarantees are by-construction only — path-shape assertions plus a scorer argv confined to `blinded/`. Zero observed blinded runs exist yet; the first real pilot is the first evidence, and its receipts may reveal leaks this scaffold does not catch (e.g. candidate *content* that names its arm — content laundering is out of scope; the ticket must forbid arm-identifying content in candidates).
- Same-model requirement is a stop gate, not a repair: if the arms ran different models (as in the 2026-10-06 pilot: `devin swe-2-max` vs `ollama qwen2.5-coder:1.5b`), the output is a composite reading, and this harness refuses to present it as a skill effect.
- One pass per arm per pair unless the ticket predeclares repeats: directional single-case evidence only. Alternated order is reported, not claimed canceled — two pairs cannot separate order effects from fixture-order interaction.
- Provider invocations in the pilot ran host-side; a sandboxed *model* worker has zero containment evidence.
- Discarded-invocation re-runs cost budget: each re-run decrements the ticket's declared invocation cap. Ledger entries without raw receipts invalidate the run note.

## Examples

Companion examples live in the installed `<skills-root>/examples/arm-blinded-eval-harness.examples.md` tree when examples are co-installed. They show the blinded-dir shape, the label-leak refusal, and the discarded-ledger/hold separation, not proof that a blinded pilot has run.

## Prompt Sources

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill is self-contained.*

- `reflective-prompt-library/plans/proposals/arm-blinded-eval-harness-proposal.md` (admission record; scaffold source)
- `reflective-prompt-library/plans/runtime-skills-task001-ticket-2026-10-06.md` (TASK-005 confounds, receipts, invocation cap)
- `reflective-prompt-library/plans/runtime-skills-workflow-spec-2026-10-06.md` (TASK-005 row: per-pair repair outcome, alternated order, blinded deterministic scorer)
