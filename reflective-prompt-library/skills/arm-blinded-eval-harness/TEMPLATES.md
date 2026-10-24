# `arm-blinded-eval-harness` Templates

Portable sibling to `SKILL.md` in this directory; this file carries the moved scaffold sections byte-for-byte, not a second copy. Read `SKILL.md` for the Module Contract, Never, Verification, Honest Limits, and provenance; those rules govern every body here. Emit the scaffold and CONFIG exactly as written below; the private-seed and C-hold notes beside them still apply.

## Contents

- [Emitted scaffold](#emitted-scaffold)
- [Configuration](#configuration)

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
    if ".." in path.parts:
        raise ValueError("run output must not contain parent traversal")
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
    except (OSError, RuntimeError, ValueError) as exc:
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

## Configuration

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
