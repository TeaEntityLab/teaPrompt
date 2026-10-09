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
- Validate before reserving: require four fresh, distinct, non-nested outputs using resolved paths plus conservative NFC/case folding; unresolved identity refuses, never falls back to lexical identity. Finish config, candidate-path and scorer-argv preflight before creating `blinded/`, so a preflight refusal reserves nothing and its correction may reuse the namespace. This covers those checked alias classes, not racing actors or filesystem-specific aliases; failures after extraction starts retain partial artifacts and require a fresh namespace.

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

- `eval-harness/run_blinded_eval.py` (stdlib only; emitted scaffold, §Emitted Scaffold).
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
- Missing required config key, malformed arm_dirs/candidates/oracle, an oracle missing the `{CAND}` placeholder, an unsubstituted `{CAND}`, duplicate/nested output paths (including case or Unicode-normalization aliases), or unresolved output identity → exit 4 before any output path is created.
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

`eval-harness/run_blinded_eval.py` (Python stdlib only; host-executed):

```python
#!/usr/bin/env python3
"""Paired-arm blinded eval scaffold. By-construction blinding only; no observed runs yet.
Usage: run_blinded_eval.py <config.json>  (see CONFIG below)
config: {pairs: [{id, candidates: [relpaths], oracle: [argv...]}],
          arms: ["control", "treatment"], order: {pair: [arm...]},
          arm_dirs: {pair: {arm: path}}, blinded: path, sealed_map: path,
          results: path, run_note: path,
          scorer_code: [trusted code argv entries]|omit,
          scoring_seed: str|omit (absent: harness-derived, recorded in sealed map),
          noise_floor_basis: str|omit, failure_categorization: str|omit,
          selection_vs_final: str|omit,
          discarded: [{pair, arm, cause, receipt, rerun}]|omit,
          caps: {pair: {arm: {calls, time_s, cost}}}|omit,
          hold: {pair, exit, dispatched, verdict}|omit}
Public execution order (order) is provenance only. Extraction iterates arms in
sorted canonical order and scoring walks a private shuffled schedule recorded
in the sealed map, never in the run note. Oracle argv uses {CAND} for the
blinded candidate path. argv[0] of each oracle plus scorer_code entries are
trusted scorer code; every other argv entry is candidate data and must resolve
inside blinded/. argv lint is not filesystem isolation: keeping the sealed
map, arm dirs, and config off the scorer's read path is a host precondition.
"""
import hashlib, json, os, random, secrets, shutil, subprocess, sys, unicodedata
from contextlib import ExitStack
from pathlib import Path

ARM_TOKENS = ("control", "treatment")
SCORER_TIMEOUT_S = 300

REQUIRED_KEYS = ("pairs", "arms", "order", "arm_dirs", "blinded",
                 "sealed_map", "results", "run_note")


def sha256_dir(root: Path) -> str:
    h = hashlib.sha256()
    for p in sorted(root.rglob("*")):
        if p.is_file():
            h.update(p.relative_to(root).as_posix().encode())
            h.update(p.read_bytes())
    return h.hexdigest()


def _fail(msg: str) -> int:
    print(msg, file=sys.stderr)
    return 4


def _within(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
    except (ValueError, OSError):
        return False
    return True


def _fold(path: Path) -> tuple:
    # Strictly resolve existing ancestors; only missing suffixes are allowed.
    suffix = []
    while True:
        try:
            parts = path.resolve(strict=True).parts + tuple(reversed(suffix))
            break
        except FileNotFoundError:
            if path.is_symlink() or path.parent == path:
                raise
            suffix.append(path.name)
            path = path.parent
    return tuple(unicodedata.normalize("NFC", p).casefold() for p in parts)


def _nested(child: tuple, parent: tuple) -> bool:
    return child[:len(parent)] == parent


def _string_list(value) -> bool:
    return isinstance(value, list) and all(
        isinstance(item, str) and item and "\0" not in item for item in value)


def main(cfg_path: str) -> int:
    try:
        cfg = json.loads(Path(cfg_path).read_text())
    except (OSError, ValueError) as exc:
        return _fail(f"unreadable config: {exc}")
    if not isinstance(cfg, dict):
        return _fail("config must be a JSON object")
    for key in REQUIRED_KEYS:
        if key not in cfg:
            return _fail(f"missing required config key: {key}")
    if not isinstance(cfg["pairs"], list) or not cfg["pairs"]:
        return _fail("pairs must be a nonempty list")
    if not _string_list(cfg["arms"]) or sorted(cfg["arms"]) != sorted(ARM_TOKENS):
        return _fail("arms must name control and treatment exactly once")
    if not isinstance(cfg["order"], dict) or not isinstance(cfg["arm_dirs"], dict):
        return _fail("order and arm_dirs must be objects")
    if any(not isinstance(per, dict) or
           any(not isinstance(d, str) or not d or "\0" in d for d in per.values())
           for per in cfg["arm_dirs"].values()):
        return _fail("arm_dirs must map pairs to arm path strings")
    for key in ("blinded", "sealed_map", "results", "run_note"):
        if not isinstance(cfg[key], str) or not cfg[key] or "\0" in cfg[key]:
            return _fail(f"{key} must be a nonempty path string")
    if not _string_list(cfg.get("scorer_code", [])):
        return _fail("scorer_code must be a list of strings")
    blinded = Path(cfg["blinded"])
    sealed_map = Path(cfg["sealed_map"])
    results_path = Path(cfg["results"])
    run_note_path = Path(cfg["run_note"])
    outputs = (("blinded", blinded), ("sealed_map", sealed_map),
               ("results", results_path), ("run_note", run_note_path))
    for label, path in outputs:
        if path.exists() or path.is_symlink():
            return _fail(f"run artifact already exists; use a fresh output namespace: {path}")
    try:
        folded = {label: _fold(path) for label, path in outputs}
    except (OSError, RuntimeError) as exc:
        return _fail(f"cannot resolve run output: {exc}")
    # Host metadata must stay outside even a case/normalization alias of blinded/.
    for label, path in outputs[1:]:
        if _nested(folded[label], folded["blinded"]):
            return _fail(f"host-held {label} inside scorer-visible blinded/: {path}")
    # Equal or ancestor outputs would overwrite or block another receipt.
    for i, (label, path) in enumerate(outputs):
        for other_label, other in outputs[i + 1:]:
            if (_nested(folded[label], folded[other_label]) or
                    _nested(folded[other_label], folded[label])):
                return _fail(f"output paths must be distinct and non-nested: {label} vs {other_label}")
    # Finish every preflight check before reserving the namespace.
    discarded = cfg.get("discarded", [])
    if not isinstance(discarded, list):
        return _fail("discarded must be a list")
    hold = cfg.get("hold")
    if "hold" in cfg:
        if not isinstance(hold, dict):
            return _fail("hold must be an object")
        if hold.get("dispatched"):
            return _fail("hold fixture dispatched work")
        if (not isinstance(hold.get("pair"), str) or not hold["pair"] or
                type(hold.get("exit")) is not int or hold["exit"] != 4 or
                hold.get("dispatched") is not False or hold.get("verdict") != "stale"):
            return _fail("hold must record a named pair, stale exit 4, and dispatched false")
    for entry in discarded:
        if not isinstance(entry, dict) or not isinstance(entry.get("receipt"), str) or not entry["receipt"]:
            return _fail("discarded invocation missing raw receipt")
    hold_id = hold["pair"] if hold else None
    seed = cfg.get("scoring_seed")
    if seed is None:
        seed = secrets.token_hex(8)
        seed_source = "derived"
    else:
        seed = str(seed)
        seed_source = "ticket"
    trusted = set(cfg.get("scorer_code", []))
    arm_dir_strs = [str(Path(d)) for per in cfg["arm_dirs"].values()
                    for d in per.values()]
    sensitive = [cfg_path, cfg["sealed_map"], cfg["results"],
                 cfg["run_note"]] + arm_dir_strs
    sensitive_forms = []
    for s in sensitive:
        sensitive_forms.append(s)
        try:
            sensitive_forms.append(str(Path(s).resolve()))
        except OSError:
            pass
    sensitive_files = set()
    for s in (cfg_path, cfg["sealed_map"], cfg["results"], cfg["run_note"]):
        try:
            sensitive_files.add(str(Path(s).resolve()))
        except OSError:
            sensitive_files.add(s)
    arm_roots = []
    for d in arm_dir_strs:
        try:
            arm_roots.append(str(Path(d).resolve()))
        except OSError:
            arm_roots.append(d)
    # Validate the whole configuration and all source paths before copying or
    # dispatching anything. A late-pair defect must not score an early pair.
    seen = set()
    for pair in cfg["pairs"]:
        if not isinstance(pair, dict):
            return _fail("each pair must be an object")
        pid = pair.get("id")
        if (not isinstance(pid, str) or not pid or "\0" in pid or
                Path(pid).name != pid or pid in (".", "..") or pid in seen):
            return _fail("pair ids must be unique filename components")
        seen.add(pid)
        if pid == hold_id:
            continue
        order_arms = cfg["order"].get(pid)
        if not _string_list(order_arms) or sorted(order_arms) != sorted(cfg["arms"]):
            return _fail(f"order for pair {pid} must be a permutation of arms {cfg['arms']}")
        if pid not in cfg["arm_dirs"] or any(a not in cfg["arm_dirs"][pid] for a in cfg["arms"]):
            return _fail(f"arm_dirs for pair {pid} must name every arm")
        if (not _string_list(pair.get("candidates")) or not pair["candidates"] or
                not _string_list(pair.get("oracle")) or not pair["oracle"]):
            return _fail(f"pair {pid} needs candidate and oracle string lists")
        if not any("{CAND}" in a for a in pair["oracle"]):
            return _fail(f"oracle for pair {pid} missing {{CAND}} placeholder")
        for cand in pair["candidates"]:
            rel = Path(cand)
            if rel.is_absolute() or ".." in rel.parts:
                return _fail(f"candidate must be arm-relative: {pid}/{cand}")
            for arm in cfg["arms"]:
                root = Path(cfg["arm_dirs"][pid][arm])
                source = root / rel
                if not _within(source, root) or not source.is_file():
                    return _fail(f"candidate missing or outside arm dir: {pid}/{arm}/{cand}")
    # Plan the extraction and lint every scorer argv before creating anything.
    sealed, final_state_hashes, planned, extraction = {}, {}, {}, []
    for pair in cfg["pairs"]:
        pid = pair["id"]
        if pid == hold_id:
            continue
        # Final-state provenance only; start-state equality is caller-owned.
        final_state_hashes[pid] = {arm: sha256_dir(Path(cfg["arm_dirs"][pid][arm]))
                                   for arm in cfg["arms"]}
        # Canonical extraction order: sorted arms, never the public execution
        # order, so creation sequence carries no provenance.
        for arm in sorted(cfg["arms"]):
            for cand in pair["candidates"]:
                dest = blinded / f"{pid}-{secrets.token_hex(6)}{Path(cand).suffix}"
                sealed[dest.name] = {"pair": pid, "arm": arm, "file": cand}
                extraction.append((pid, arm, cand, dest))
    # Blinding assertion: no arm token anywhere in the scorer-visible surface.
    for name in sealed:
        if any(t in name.lower() for t in ARM_TOKENS):
            return _fail(f"label leak: {name}")
    # Validate all scorer argv before extraction: declared code is trusted;
    # all other entries must be blinded candidate data, not host-held paths.
    for pair in cfg["pairs"]:
        if pair["id"] == hold_id:
            continue
        for name, meta in sealed.items():
            if meta["pair"] != pair["id"]:
                continue
            cand_str = str(blinded / name)
            argv = [a.replace("{CAND}", cand_str) for a in pair["oracle"]]
            flat = " ".join(argv)
            if "{CAND}" in flat:
                return _fail("unsubstituted {CAND} in oracle argv")
            # Specific path containment first: an arm-dir path always embeds an
            # arm token, so the generic token check would mask its message.
            if any(d and d in flat for d in arm_dir_strs + arm_roots):
                return _fail(f"scorer argv references arm dir: {flat}")
            if any(t in flat.lower() for t in ARM_TOKENS):
                return _fail(f"arm label in scorer argv: {flat}")
            if any(s and s in flat for s in sensitive_forms):
                return _fail(f"scorer argv references host-held path: {flat}")
            for a in argv[1:]:
                if a in trusted or a == cand_str:
                    continue
                try:
                    a_res = str(Path(a).resolve())
                except OSError:
                    return _fail(f"cannot resolve scorer data: {a}")
                if a_res in sensitive_files:
                    return _fail(f"scorer data references host-held path: {a}")
                if any(a_res == r or a_res.startswith(r + os.sep) for r in arm_roots):
                    return _fail(f"scorer argv references arm dir: {a}")
                if not _within(Path(a), blinded):
                    return _fail(f"scorer data outside blinded/: {a}")
            planned[name] = argv
    # Preflight passed; only now reserve blinded/ and extract.
    blinded.mkdir(parents=True)
    for pid, arm, cand, dest in extraction:
        root = Path(cfg["arm_dirs"][pid][arm])
        try:
            source = root / cand
            if not _within(source, root) or not source.is_file():
                return _fail(f"candidate outside arm dir: {pid}/{arm}/{cand}")
            shutil.copyfile(source, dest)
        except OSError as exc:
            return _fail(f"cannot extract {pid}/{arm}/{cand}: {exc}")
    # Private scoring schedule: shuffled here, recorded only in the sealed map.
    # The public execution order never influences this order, so an
    # ordinal-only predictor reading public order guesses at chance.
    rng = random.Random(seed)
    schedule = [name for name in sealed]
    rng.shuffle(schedule)
    scores, scorer_error = [], None
    with ExitStack() as outputs:
        for path in (sealed_map, results_path, run_note_path):
            path.parent.mkdir(parents=True, exist_ok=True)
        sealed_output, scores_output, note_output = (
            outputs.enter_context(path.open("x"))
            for path in (sealed_map, results_path, run_note_path))
        for name in schedule:
            try:
                r = subprocess.run(planned[name], capture_output=True, text=True,
                                   timeout=SCORER_TIMEOUT_S)
            except (OSError, subprocess.TimeoutExpired) as exc:
                out, err = getattr(exc, "stdout", None), getattr(exc, "stderr", None)
                out = out.decode(errors="replace") if isinstance(out, bytes) else out or ""
                err = err.decode(errors="replace") if isinstance(err, bytes) else err or ""
                scores.append({"candidate": name, "exit": None, "error": type(exc).__name__,
                               "stdout": out, "stderr": err})
                scorer_error = f"scorer execution failed: {exc}"
                break
            scores.append({"candidate": name, "exit": r.returncode,
                           "stdout": r.stdout, "stderr": r.stderr})
        sealed_doc = {"candidates": sealed, "scoring_order": schedule,
                      "scoring_seed": seed, "scoring_seed_source": seed_source}
        sealed_output.write(json.dumps(sealed_doc, indent=2))
        scores_output.write("".join(json.dumps(s) + "\n" for s in scores))
        repair_ids = [p["id"] for p in cfg["pairs"] if p["id"] != hold_id]
        note = {"order": cfg["order"], "final_state_hashes": final_state_hashes,
                "scoring": "private shuffled schedule in sealed map; ordinal carries no arm information",
                "scorer_isolation": ("host-precondition: argv lint only; filesystem/network "
                                     "isolation of the scorer from arm dirs, config, and the "
                                     "sealed map is enforced by the host, not by this scaffold"),
                "caps": cfg.get("caps") or "not declared",
                "discarded": discarded,
                "hold": hold,
                "denominator": {"repair_pairs": len(repair_ids),
                                "note": "discarded + hold excluded"},
                "noise_floor_basis": cfg.get("noise_floor_basis") or "missing",
                "failure_categorization": cfg.get("failure_categorization") or "unresolved",
                "selection_vs_final": cfg.get("selection_vs_final") or "not-a-final-claim",
                "disclosure": "by-construction blinding only; zero observed blinded runs yet"}
        if scorer_error:
            note["scorer_error"] = scorer_error
        note_output.write(json.dumps(note, indent=2))
    # Captured-output label audit: caller checks scores.jsonl for ARM_TOKENS.
    return _fail(scorer_error) if scorer_error else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(_fail("Usage: run_blinded_eval.py <config.json>"))
    try:
        sys.exit(main(sys.argv[1]))
    except (OSError, ValueError) as exc:
        sys.exit(_fail(f"harness file error: {exc}"))
```

The default derives a private seed. Supply `scoring_seed` only for host-held
replay or synthetic checks; never publish it to the scorer during a blinded
pilot. A public seed plus canonical extraction order makes scoring predictable.

`CONFIG` (complete runnable form, checked into the pilot ticket, immutable during the run — executes verbatim with relative paths resolved from the run directory):

```json
{
  "pairs": [
    {"id": "A-code", "candidates": ["calc.py"],
     "oracle": ["python3", "fixtures/A-code/oracle.py", "{CAND}"]},
    {"id": "B-content", "candidates": ["report.md"],
     "oracle": ["python3", "fixtures/B-content/oracle.py", "{CAND}"]}
  ],
  "arms": ["control", "treatment"],
  "order": {"A-code": ["control", "treatment"], "B-content": ["treatment", "control"]},
  "arm_dirs": {
    "A-code": {"control": "arms/A-code/control", "treatment": "arms/A-code/treatment"},
    "B-content": {"control": "arms/B-content/control", "treatment": "arms/B-content/treatment"}
  },
  "scorer_code": ["python3", "fixtures/A-code/oracle.py", "fixtures/B-content/oracle.py"],
  "blinded": "blinded",
  "sealed_map": "map/sealed-map.json",
  "results": "results/scores.jsonl",
  "run_note": "results/run-note.json",
  "caps": {
    "A-code": {
      "control": {"calls": 13, "time_s": 600, "cost": "0"},
      "treatment": {"calls": 13, "time_s": 600, "cost": "0"}
    },
    "B-content": {
      "control": {"calls": 13, "time_s": 600, "cost": "0"},
      "treatment": {"calls": 13, "time_s": 600, "cost": "0"}
    }
  },
  "discarded": [
    {"pair": "B-content", "arm": "treatment", "cause": "wrong CLI spelling",
     "receipt": "evidence/task005/malformed-1.out", "rerun": true}
  ],
  "hold": {"pair": "C-hold", "exit": 4, "dispatched": false, "verdict": "stale"},
  "noise_floor_basis": "single-run caveat: no score difference claimed in this note",
  "failure_categorization": "no treatment attribution in this note",
  "selection_vs_final": "not-a-final-claim"
}
```

C-hold is not a scored pair: its acceptance is `stale` exit 4 with zero dispatch, recorded in the run note outside `scores.jsonl` and outside the denominator.

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

- `reflective-prompt-library/plans/proposals/arm-blinded-eval-harness-proposal.md` (historical admission record; the live scaffold is above)
- `reflective-prompt-library/plans/runtime-skills-task001-ticket-2026-10-06.md` (TASK-005 confounds, receipts, invocation cap)
- `reflective-prompt-library/plans/runtime-skills-workflow-spec-2026-10-06.md` (TASK-005 row: per-pair repair outcome, alternated order, blinded deterministic scorer)
