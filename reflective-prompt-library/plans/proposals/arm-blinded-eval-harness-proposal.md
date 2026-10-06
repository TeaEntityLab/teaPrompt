---
name: arm-blinded-eval-harness
description: Use when running a with/without-skill pilot on paired repair fixtures and the scorer must not see arm labels. It emits a paired-arm evaluation scaffold — fixture cloning, alternated arm order, treatment-only artifact exclusion, label-stripped candidate extraction into a blinded dir, deterministic scorer invocation, and a discarded-invocation ledger kept separate from the denominator. By-construction guarantees only; zero observed blinded runs yet.
license: MIT
metadata:
  risk_level: medium
  human_review_required: true
  external_io: false
  context_load: low
---

# Arm-Blinded Eval Harness (proposal — inert until admission review)

**Status:** ADOPTED 2026-10-06 — registered domain pack; live contract at `skills/arm-blinded-eval-harness/SKILL.md`. This file is the admission record.

**Status:** Proposal artifact. NOT a registered skill; NOT listed in any skill map.
Admission review decides whether this becomes a domain pack. Until then, copy the
scaffold below by hand; no runner auto-discovers it.

## Purpose

Close the three confounds recorded in the TASK-005 pilot so a future pilot can be
read at face value:

1. Scorer saw arm labels at extraction time (arm names in file paths).
2. Arms differed in model *and* guidance (composite, not isolated skill effect).
3. Single run per arm (directional single-case evidence only).

This proposal fixes confound 1 by construction (blinded extraction directory plus a
sealed arm↔candidate map the scorer never reads). It bounds confound 2 by requiring
identical model/CLI/profile/caps across arms and recording every remaining
treatment-only difference as a reported factor, not a skill-attributed effect. It
does not fix confound 3 — the scaffold still runs one pass per arm per pair unless
the task ticket predeclares repeats; the run note must keep the directional-only
limit.

Evidence: `reflective-prompt-library/plans/runtime-skills-task001-ticket-2026-10-06.md`
TASK-005 section lines 79–87 (result 2/2 vs 1/2, n=2 repair pairs; confounds;
discarded invocations kept in `evidence/task005/`); pilot fixtures at
`/tmp/teaprompt-dryrun/host-task/fixtures/` (`A-code/` arithmetic oracle,
`B-content/` section+substance oracle, `C-hold/` stale-binding zero-dispatch).
Spec binding: `runtime-skills-workflow-spec-2026-10-06.md` TASK-005 row —
per-pair repair outcome on the final candidate only, pair-level denominator (n=2),
alternated arm order reported not claimed canceled, blinded deterministic scorer.

## Module Contract

Trigger:

- A with/without-skill pilot on predeclared private repair fixtures plus one
  expected-preflight-hold fixture, each cloned identically for two arms.
- A deterministic oracle/verifier exists per fixture and runs without model calls.
- The task ticket names the candidate surface per fixture (which file is scored).

Methods:

- Fixture cloning: copy each fixture once per arm from a read-only seed; record
  seed hash per clone. Arms never share a workdir.
- Alternated arm order: pair A runs control-then-treatment, pair B runs
  treatment-then-control (or the ticket's declared alternation); order is written
  to the run note as observed sequence, not as a canceled effect.
- Treatment-only artifact exclusion: only the ticket-named candidate files are
  extracted for scoring. Skill guidance, workflow scripts, ledgers, and
  inspectable state stay out of the blinded dir — they are reported factors, not
  scored surface.
- Label-stripped extraction: each final candidate is copied to
  `blinded/<pair>-<seq>.ext` (sequential IDs, no arm token); the arm↔ID map is
  written to a host-held file outside the scorer's read path.
- Deterministic scorer invocation: the oracle runs with argv pointing only into
  `blinded/`; scorer stdout/stderr is captured per candidate. No scorer input path
  may contain an arm label — the harness asserts this before scoring and refuses
  (exit 4) if any blinded path leaks one.
- Discarded-invocation ledger: malformed or environment-incomplete invocations
  (wrong CLI spelling, tool-rejection with no proposal) are logged with raw
  receipts and re-run; they never enter the pair denominator. The denominator
  stays fixture-pair level (n = number of repair pairs).

Output:

- `eval-harness/run_blinded_eval.py` (stdlib only; emitted scaffold, §Scaffold).
- `blinded/` (label-free candidates), `map/sealed-map.json` (host-held arm map),
  `results/scores.jsonl` (per-candidate oracle pass/fail + raw output),
  `results/run-note.json` (order, seed hashes, caps, discarded ledger refs).
- C-hold pair reported separately: expected `stale` exit 4, zero dispatch — never
  merged into the repair-pair denominator.

Escalation:

- Model/CLI/profile differ between arms → stop: composite, not a skill-effect
  reading; record as pilot defect, do not score as comparison.
- Oracle needs judgment (no deterministic pass/fail) → this harness does not
  apply; route to an LLM-judge design with its own blinding.
- Hold fixture dispatches work → containment finding; route to host owner, not to
  an oracle edit (ticket falsifiability rule).
- Missing acceptance criterion or unsigned intent → hold, `stop_and_repair`.

Inputs:

- Predeclared fixture seeds + per-fixture candidate file names + deterministic
  oracle commands (ticket-owned, immutable during the run).
- Same configured model/CLI/profile and equal call/time/cost caps for both arms.
- Named artifact owner and named accepter for the pilot outcome.

Failure signals:

- Any blinded path contains an arm token (`control`, `treatment`, arm index) →
  exit 4 before scoring.
- Scorer argv references anything outside `blinded/` → exit 4.
- Seed hash mismatch between clones → exit 4 (clones not identical).
- Discarded invocation missing raw receipt → run note incomplete; do not score.

Verification:

- Run the emitted harness on two synthetic arms where the scoreable difference is
  planted (e.g. one candidate passes the A-code oracle, the other fails it; one
  B-content report keeps all three headings, the other drops one).
- Check the scorer's argv, cwd, and captured stdout contain no arm labels: grep
  the full scorer invocation log for the arm tokens and require zero matches.
- Check `results/scores.jsonl` recovers the planted pass/fail pattern after
  unblinding via the sealed map, and the discarded ledger holds the planted
  malformed invocation outside the denominator.

## Scaffold

`eval-harness/run_blinded_eval.py` (Python stdlib only; host-executed):

```python
#!/usr/bin/env python3
"""Paired-arm blinded eval scaffold. By-construction blinding only; no observed runs yet.
Usage: run_blinded_eval.py <config.json>  (see CONFIG below)
config: {pairs: [{id, seed, candidates: [relpaths], oracle: [argv...]}],
          arms: ["control", "treatment"], order: {pair: [arm...]},
          arm_dirs: {pair: {arm: path}}, blinded: path, sealed_map: path}
Oracle argv uses {CAND} for the blinded candidate path. Scorer never sees arm dirs.
"""
import hashlib, json, shutil, subprocess, sys
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
    sealed, scores, discarded = {}, [], []
    seq = 0
    for pair in cfg["pairs"]:
        hashes = {}
        for arm in cfg["arms"]:
            src = Path(cfg["arm_dirs"][pair["id"]][arm])
            hashes[arm] = sha256_dir(src)
        if len(set(hashes.values())) != 1:
            # Start-state equality is checked at clone time by the caller; differing
            # *final* states are the expected arm effect. Clone check lives in run-note.
            pass
        for arm in cfg["order"][pair["id"]]:
            src = Path(cfg["arm_dirs"][pair["id"]][arm])
            for cand in pair["candidates"]:
                seq += 1
                dest = blinded / f"{pair['id']}-{seq}{Path(cand).suffix}"
                shutil.copyfile(src / cand, dest)
                sealed[dest.name] = {"pair": pair["id"], "arm": arm, "file": cand}
    # Blinding assertion: no arm token anywhere in the scorer-visible surface.
    for p in blinded.iterdir():
        low = p.name.lower()
        assert not any(t in low for t in ARM_TOKENS), f"label leak: {p.name}"
    for pair in cfg["pairs"]:
        for name, meta in sealed.items():
            if meta["pair"] != pair["id"]:
                continue
            argv = [a.replace("{CAND}", str(blinded / name)) for a in pair["oracle"]]
            assert all(cfg["arm_dirs"][p][a] not in a
                       for p in cfg["arm_dirs"] for a in cfg["arm_dirs"][p]
                       for a in [a]), "scorer argv must reference blinded/ only"
            r = subprocess.run(argv, capture_output=True, text=True, timeout=300)
            scores.append({"candidate": name, "exit": r.returncode,
                           "stdout": r.stdout[-2000:], "stderr": r.stderr[-2000:]})
    Path(cfg["sealed_map"]).parent.mkdir(parents=True, exist_ok=True)
    Path(cfg["sealed_map"]).write_text(json.dumps(sealed, indent=2))
    Path(cfg["results"]).write_text("".join(json.dumps(s) + "\n" for s in scores))
    note = {"order": cfg["order"], "discarded": discarded,
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

C-hold is not a scored pair: its acceptance is `stale` exit 4 with zero dispatch,
recorded in the run note outside `scores.jsonl` and outside the denominator.

## Honest limits

- **Disclosure (required in every run note):** the emitted harness guarantees are
  by-construction only — path-shape assertions plus a scorer argv confined to
  `blinded/`. Zero observed blinded runs exist yet; the first real pilot is the
  first evidence, and its receipts may reveal leaks this scaffold does not catch
  (e.g. candidate *content* that names its arm — content laundering is out of
  scope; the ticket must forbid arm-identifying content in candidates).
- Same-model requirement is a stop gate, not a repair: if the arms ran different
  models (as in the 2026-10-06 pilot: `devin swe-2-max` vs `ollama
  qwen2.5-coder:1.5b`), the output is a composite reading, and this harness
  refuses to present it as a skill effect.
- One pass per arm per pair unless the ticket predeclares repeats: directional
  single-case evidence only (spec §7). Alternated order is reported, not claimed
  canceled — two pairs cannot separate order effects from fixture-order
  interaction.
- Provider invocations in the pilot ran host-side (seatbelt denies their egress);
  a sandboxed *model* worker has zero containment evidence. Unchanged from the
  ticket's post-acceptance lens findings.
- Discarded-invocation re-runs cost budget: each re-run decrements the ticket's
  declared invocation cap (spec: at most 13 host-agent invocations for the first
  pilot). Ledger entries without raw receipts invalidate the run note.
