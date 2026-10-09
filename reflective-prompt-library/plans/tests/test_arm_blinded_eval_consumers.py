"""Extracted-template behavioral regressions for the arm-blinded-eval scaffold.

Extracts ``eval-harness/run_blinded_eval.py`` from the skill and executes it
with offline stub oracles in isolated workspaces. RV-03/RV-06/RV-07 are
behavioral (order leakage, scorer boundary, runnable config), so these
checks run the template — never the prose.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from prompt_eval_helpers import library_skills_dir  # noqa: E402


def _source() -> str:
    return (library_skills_dir() / "arm-blinded-eval-harness" / "SKILL.md").read_text(
        encoding="utf-8"
    )


def _scaffold() -> str:
    match = re.search(r"```python\n(.*?)```", _source(), re.S)
    assert match, "arm-blinded-eval scaffold fence missing"
    return match.group(1)


def _runner(d: Path) -> Path:
    path = d / "run_blinded_eval.py"
    path.write_text(_scaffold(), encoding="utf-8")
    return path


A_ORACLE = (
    "import runpy, sys\n"
    "add = runpy.run_path(sys.argv[1])['add']\n"
    "sys.exit(0 if add(2, 3) == 5 else 1)\n"
)

B_ORACLE = (
    "import pathlib, sys\n"
    "text = pathlib.Path(sys.argv[1]).read_text()\n"
    "need = ('## Aim', '## Plan', '## Next')\n"
    "sys.exit(0 if all(h in text for h in need) else 1)\n"
)

DISPATCH_MARKER = (
    "import pathlib\n"
    "pathlib.Path('evidence/dispatch-count.txt').parent.mkdir(parents=True, exist_ok=True)\n"
    "with pathlib.Path('evidence/dispatch-count.txt').open('a', encoding='utf-8') as marker:\n"
    "    marker.write('x')\n"
)

EXTRA_ORACLE = DISPATCH_MARKER + (
    "import pathlib, sys\n"
    "p = pathlib.Path(sys.argv[1])\n"
    "extra = pathlib.Path(sys.argv[2]).read_text() if len(sys.argv) > 2 else ''\n"
    "sys.exit(0 if 'return a + b' in p.read_text() + extra else 1)\n"
)


def _fixture(d: Path, *, with_extra: bool = False) -> dict:
    (d / "fixtures" / "A-code").mkdir(parents=True)
    (d / "fixtures" / "B-content").mkdir(parents=True)
    (d / "fixtures" / "A-code" / "oracle.py").write_text(
        EXTRA_ORACLE if with_extra else A_ORACLE, encoding="utf-8"
    )
    (d / "fixtures" / "B-content" / "oracle.py").write_text(
        DISPATCH_MARKER + B_ORACLE if with_extra else B_ORACLE, encoding="utf-8"
    )
    for pair, arm, name, body in (
        ("A-code", "control", "calc.py", "def add(a, b):\n    return a - b\n"),
        ("A-code", "treatment", "calc.py", "def add(a, b):\n    return a + b\n"),
        ("B-content", "control", "report.md", "## Aim\nkeep\n## Plan\nkeep\n## Next\nkeep\n"),
        ("B-content", "treatment", "report.md", "## Aim\nkeep\n## Plan\nkeep\n"),
    ):
        arm_dir = d / "arms" / pair / arm
        arm_dir.mkdir(parents=True, exist_ok=True)
        (arm_dir / name).write_text(body, encoding="utf-8")
    return json.loads(
        re.search(r"(?ms)^```json\n(.*?)^```\s*$", _source()).group(1)
    )


def _run(d: Path, cfg: dict) -> subprocess.CompletedProcess:
    cfg_path = d / "config.json"
    cfg_path.write_text(json.dumps(cfg), encoding="utf-8")
    return subprocess.run(
        [sys.executable, str(_runner(d)), str(cfg_path)],
        cwd=d,
        capture_output=True,
        text=True,
        timeout=60,
    )


def _sealed(d: Path) -> dict:
    return json.loads((d / "map" / "sealed-map.json").read_text(encoding="utf-8"))


def _scores(d: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in (d / "results" / "scores.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def test_documented_config_runs_verbatim_and_recovers_planted_pattern(tmp_path: Path):
    """RV-07 + content positive control: verbatim CONFIG shape scores exit 0."""
    result = _run(tmp_path, _fixture(tmp_path))
    assert result.returncode == 0, result.stderr
    sealed = _sealed(tmp_path)
    by_candidate = sealed["candidates"]
    arms = {name: meta["arm"] for name, meta in by_candidate.items()}
    exits = {
        (by_candidate[row["candidate"]]["pair"], arms[row["candidate"]]): row["exit"]
        for row in _scores(tmp_path)
    }
    # Planted scoreable difference: treatment passes A-code, control fails it;
    # control passes B-content, treatment drops a heading and fails it.
    assert exits[("A-code", "treatment")] == 0
    assert exits[("A-code", "control")] == 1
    assert exits[("B-content", "control")] == 0
    assert exits[("B-content", "treatment")] == 1
    note = json.loads((tmp_path / "results" / "run-note.json").read_text(encoding="utf-8"))
    assert note["denominator"]["repair_pairs"] == 2
    assert len(note["discarded"]) == 1
    assert note["hold"]["verdict"] == "stale"
    assert "scoring_order" not in note


def test_swapped_public_order_keeps_private_scoring_schedule(tmp_path: Path):
    """RV-03: same seed + swapped order => identical sealed scoring arm sequence."""
    cfg = _fixture(tmp_path)
    cfg["scoring_seed"] = "host-private-replay-seed"
    assert _run(tmp_path, cfg).returncode == 0
    first = _sealed(tmp_path)["scoring_order"]
    first_arms = [_sealed(tmp_path)["candidates"][name]["arm"] for name in first]
    other = tmp_path / "swapped"
    other.mkdir()
    cfg2 = _fixture(other)
    cfg2["scoring_seed"] = cfg["scoring_seed"]
    cfg2["order"] = {
        "A-code": ["treatment", "control"],
        "B-content": ["control", "treatment"],
    }
    assert _run(other, cfg2).returncode == 0
    second = _sealed(other)["scoring_order"]
    second_arms = [_sealed(other)["candidates"][name]["arm"] for name in second]
    # Random IDs differ per extraction, but the arm sequence of the private
    # schedule is seed-determined and identical while public order differs —
    # an ordinal-only predictor reading public order cannot match both runs.
    assert first_arms == second_arms




def test_run_note_carries_no_scoring_schedule(tmp_path: Path):
    """RV-03 privacy: run-note provenance must not leak the sealed schedule."""
    assert _run(tmp_path, _fixture(tmp_path)).returncode == 0
    note = json.loads((tmp_path / "results" / "run-note.json").read_text(encoding="utf-8"))
    schedule = _sealed(tmp_path)["scoring_order"]
    blob = json.dumps(note)
    assert not any(name in blob for name in schedule)


@pytest.mark.parametrize(
    "extra_arg",
    [
        "outside-input.txt",
        "missing-outside-input.txt",
        "arms/A-code/control/calc.py",
        "config.json",
        "map/sealed-map.json",
    ],
)
def test_scorer_data_boundary_refuses_before_any_dispatch(
    tmp_path: Path, extra_arg: str
):
    """RV-06: outsider/arm/config/metadata data args refuse with zero dispatch."""
    cfg = _fixture(tmp_path, with_extra=True)
    (tmp_path / "outside-input.txt").write_text("return a + b\n", encoding="utf-8")
    (tmp_path / "evidence" / "task005").mkdir(parents=True, exist_ok=True)
    (tmp_path / "evidence" / "task005" / "malformed-1.out").write_text("receipt\n")
    cfg["pairs"][0]["oracle"] = [
        sys.executable,
        "fixtures/A-code/oracle.py",
        "{CAND}",
        extra_arg,
    ]
    result = _run(tmp_path, cfg)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "evidence" / "dispatch-count.txt").exists()
    assert not (tmp_path / "results" / "scores.jsonl").exists()


def test_undeclared_scorer_code_path_refuses(tmp_path: Path):
    """RV-06: trust is declared in scorer_code, not inferred from file shape."""
    cfg = _fixture(tmp_path)
    cfg["scorer_code"] = [sys.executable, "fixtures/B-content/oracle.py"]
    result = _run(tmp_path, cfg)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "results" / "scores.jsonl").exists()


def test_sealed_map_inside_blinded_refuses(tmp_path: Path):
    """RV-03/06: host-held schedule metadata must stay off the scorer path."""
    cfg = _fixture(tmp_path)
    cfg["sealed_map"] = "blinded/sealed-map.json"
    result = _run(tmp_path, cfg)
    assert result.returncode == 4, result.stderr


def test_missing_required_key_reports_exit_4(tmp_path: Path):
    """RV-07: the scaffold reports its required keys instead of KeyError."""
    cfg = _fixture(tmp_path)
    del cfg["blinded"]
    result = _run(tmp_path, cfg)
    assert result.returncode == 4, result.stderr


def test_discarded_entry_without_receipt_invalidates_run(tmp_path: Path):
    """Preserved contract: receipt-less ledger entries never score."""
    cfg = _fixture(tmp_path)
    cfg["discarded"] = [{"pair": "B-content", "arm": "treatment", "cause": "typo"}]
    result = _run(tmp_path, cfg)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "results" / "scores.jsonl").exists()


def test_dispatched_hold_blocks_scoring(tmp_path: Path):
    """Preserved contract: a dispatched hold fixture is a containment stop."""
    cfg = _fixture(tmp_path)
    cfg["hold"] = {"pair": "C-hold", "exit": 4, "dispatched": True, "verdict": "stale"}
    result = _run(tmp_path, cfg)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "results" / "scores.jsonl").exists()


@pytest.mark.parametrize(
    "key,value",
    [
        ("arm_dirs", []),
        ("arm_dirs", {"A-code": []}),
        ("arm_dirs", {"A-code": {"control": 7, "treatment": "unused"}}),
        ("order", []),
        ("order", {"A-code": [1, "treatment"]}),
        ("arms", ["control", 7]),
        ("arms", ["control", "control"]),
        ("pairs", {}),
        ("pairs", [{}]),
        ("pairs", [{"id": 7}]),
        ("pairs", [{"id": "../outside", "candidates": ["calc.py"], "oracle": ["python3", "{CAND}"]}]),
        ("pairs", [{"id": "A-code", "candidates": [7], "oracle": ["python3", "{CAND}"]}]),
        ("pairs", [{"id": "A-code", "candidates": ["calc.py"], "oracle": [7, "{CAND}"]}]),
        ("scorer_code", [{}]),
        ("blinded", 7),
        ("discarded", {}),
        ("hold", []),
        ("hold", {}),
        ("hold", {"pair": "C-hold", "exit": 0, "dispatched": False, "verdict": "stale"}),
        ("hold", {"pair": "C-hold", "exit": 4, "dispatched": False, "verdict": "passed"}),
        ("hold", {"pair": "C-hold", "exit": 4, "dispatched": 0, "verdict": "stale"}),
    ],
)
def test_malformed_config_refuses_without_dispatch(tmp_path: Path, key, value):
    cfg = _fixture(tmp_path, with_extra=True)
    cfg[key] = value
    result = _run(tmp_path, cfg)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "evidence" / "dispatch-count.txt").exists()
    assert not (tmp_path / "results" / "scores.jsonl").exists()


@pytest.mark.parametrize("path_kind", ["relative", "absolute", "symlink"])
def test_candidate_escape_refuses_without_copying_or_scoring(tmp_path: Path, path_kind: str):
    cfg = _fixture(tmp_path, with_extra=True)
    outside = tmp_path / "arms" / "A-code" / "outside.py"
    outside.write_text("def add(a, b):\n    return a + b\n", encoding="utf-8")
    if path_kind == "relative":
        cfg["pairs"][0]["candidates"] = ["../outside.py"]
    elif path_kind == "absolute":
        cfg["pairs"][0]["candidates"] = [str(outside)]
    else:
        candidate = tmp_path / "arms" / "A-code" / "control" / "calc.py"
        candidate.unlink()
        candidate.symlink_to(outside)
    result = _run(tmp_path, cfg)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "evidence" / "dispatch-count.txt").exists()
    assert not list((tmp_path / "blinded").glob("*"))


def test_missing_scorer_preserves_failure_receipt_not_a_product_score(tmp_path: Path):
    cfg = _fixture(tmp_path)
    cfg["pairs"][0]["oracle"][0] = str(tmp_path / "unavailable-scorer")
    result = _run(tmp_path, cfg)
    assert result.returncode == 4, result.stderr
    failures = [row for row in _scores(tmp_path) if row.get("error")]
    assert len(failures) == 1
    assert failures[0]["exit"] is None
    assert failures[0]["error"] == "FileNotFoundError"
    note = json.loads((tmp_path / "results" / "run-note.json").read_text(encoding="utf-8"))
    assert note["scorer_error"]


def test_scorer_timeout_preserves_partial_output_and_stops(tmp_path: Path, monkeypatch):
    cfg = _fixture(tmp_path)
    (tmp_path / "fixtures" / "A-code" / "oracle.py").write_text(
        "import time\nprint('started', flush=True)\ntime.sleep(2)\n", encoding="utf-8"
    )
    cfg_path = tmp_path / "config.json"
    cfg_path.write_text(json.dumps(cfg), encoding="utf-8")
    namespace = {"__name__": "extracted_blinded_eval"}
    exec(compile(_scaffold(), "run_blinded_eval.py", "exec"), namespace)
    namespace["SCORER_TIMEOUT_S"] = 0.2
    monkeypatch.chdir(tmp_path)
    assert namespace["main"](str(cfg_path)) == 4
    failures = [row for row in _scores(tmp_path) if row.get("error")]
    assert len(failures) == 1
    assert failures[0]["exit"] is None
    assert failures[0]["error"] == "TimeoutExpired"
    assert failures[0]["stdout"].strip() == "started"
    assert len(_scores(tmp_path)) < 4


def test_final_state_hashes_bind_extracted_contents(tmp_path: Path):
    cfg = _fixture(tmp_path)
    result = _run(tmp_path, cfg)
    assert result.returncode == 0, result.stderr
    note = json.loads((tmp_path / "results" / "run-note.json").read_text(encoding="utf-8"))
    final = note["final_state_hashes"]["A-code"]
    assert final["control"] == hashlib.sha256(b"calc.pydef add(a, b):\n    return a - b\n").hexdigest()
    assert final["treatment"] == hashlib.sha256(b"calc.pydef add(a, b):\n    return a + b\n").hexdigest()
    assert final["control"] != final["treatment"]


def test_missing_config_argument_refuses(tmp_path: Path):
    result = subprocess.run(
        [sys.executable, str(_runner(tmp_path))],
        cwd=tmp_path, capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 4, result.stderr


@pytest.mark.parametrize("stream", ["stdout", "stderr"])
def test_scorer_output_retains_early_labels_for_full_output_audit(tmp_path: Path, stream: str):
    cfg = _fixture(tmp_path)
    (tmp_path / "fixtures" / "A-code" / "oracle.py").write_text(
        f"import sys\nprint('control ' + 'x' * 2500, file=sys.{stream})\n", encoding="utf-8"
    )
    result = _run(tmp_path, cfg)
    assert result.returncode == 0, result.stderr
    sealed = _sealed(tmp_path)["candidates"]
    expected_leaks = {
        name for name, meta in sealed.items() if meta["pair"] == "A-code"
    }
    detected_leaks = {
        row["candidate"] for row in _scores(tmp_path)
        if any(token in (row["stdout"] + row["stderr"]).lower()
               for token in ("control", "treatment"))
    }
    assert detected_leaks == expected_leaks


@pytest.mark.parametrize("dangling", [False, True], ids=["existing", "dangling-symlink"])
@pytest.mark.parametrize("key", ["blinded", "sealed_map", "results", "run_note"])
def test_existing_run_artifacts_refuse_before_scoring_and_preserve_bytes(
    tmp_path: Path, key: str, dangling: bool
):
    cfg = _fixture(tmp_path, with_extra=True)
    artifact = tmp_path / cfg[key]
    missing_target = tmp_path / "missing-output"
    historical = b"historical receipt or candidate\n"
    if dangling:
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.symlink_to(missing_target)
    else:
        if key == "blinded":
            artifact.mkdir()
            artifact = artifact / "previous.py"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_bytes(historical)

    result = _run(tmp_path, cfg)

    assert result.returncode == 4, result.stderr
    if dangling:
        assert artifact.is_symlink()
        assert artifact.readlink() == missing_target
        assert not missing_target.exists()
    else:
        assert artifact.read_bytes() == historical
        if key == "blinded":
            assert list(artifact.parent.iterdir()) == [artifact]
    assert not (tmp_path / "evidence" / "dispatch-count.txt").exists()
    for other in ("blinded", "sealed_map", "results", "run_note"):
        if other != key:
            assert not (tmp_path / cfg[other]).exists()
            assert not (tmp_path / cfg[other]).is_symlink()


def _reject(cfg: dict, kind: str) -> dict:
    """Return a copy of CONFIG broken in one way the scaffold must refuse."""
    cfg = json.loads(json.dumps(cfg))
    if kind == "missing-placeholder":
        cfg["pairs"][0]["oracle"] = [a for a in cfg["pairs"][0]["oracle"] if a != "{CAND}"]
    elif kind == "metadata-inside-blinded":
        cfg["sealed_map"] = "blinded/sealed-map.json"
    elif kind == "duplicate-outputs":
        cfg["results"] = cfg["sealed_map"]
    elif kind == "nested-outputs":
        cfg["results"] = "out"
        cfg["blinded"] = "out/blinded"
    elif kind == "case-alias-outputs":
        # Same file on a case-insensitive volume; Path.resolve() of a
        # not-yet-created path does not fold case, so string identity misses it.
        cfg["run_note"] = "results/Scores.jsonl"
    elif kind == "nfc-nfd-alias-outputs":
        cfg["results"] = "r\u00e9sultats/scores.jsonl"
        cfg["run_note"] = "re\u0301sultats/scores.jsonl"
    elif kind == "metadata-inside-blinded-case-alias":
        # On a case-insensitive volume this resolves inside blinded/ at open time.
        cfg["sealed_map"] = "Blinded/sealed-map.json"
    elif kind == "late-pair-boundary":
        cfg["pairs"][1]["oracle"].append("config.json")
    elif kind == "dispatched-hold":
        cfg["hold"] = {"pair": "C-hold", "exit": 4, "dispatched": True, "verdict": "stale"}
    else:
        raise ValueError(kind)
    return cfg


@pytest.mark.parametrize(
    "kind",
    [
        "missing-placeholder",
        "metadata-inside-blinded",
        "duplicate-outputs",
        "nested-outputs",
        "case-alias-outputs",
        "nfc-nfd-alias-outputs",
        "metadata-inside-blinded-case-alias",
        "late-pair-boundary",
        "dispatched-hold",
    ],
)
def test_rejected_config_reserves_nothing_and_corrected_rerun_reuses_namespace(
    tmp_path: Path, kind: str
):
    """A refused CONFIG must not consume the namespace its correction will use."""
    cfg = _fixture(tmp_path, with_extra=True)
    rejected = _reject(cfg, kind)

    result = _run(tmp_path, rejected)

    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "evidence" / "dispatch-count.txt").exists()
    for run in (rejected, cfg):
        for key in ("blinded", "sealed_map", "results", "run_note"):
            assert not (tmp_path / run[key]).exists()
            assert not (tmp_path / run[key]).is_symlink()
    # Only the inputs the test wrote remain: no reserved directory or file.
    assert {p.name for p in tmp_path.iterdir()} == {
        "fixtures", "arms", "config.json", "run_blinded_eval.py"
    }

    corrected = _run(tmp_path, cfg)
    assert corrected.returncode == 0, corrected.stderr
    assert (tmp_path / "evidence" / "dispatch-count.txt").read_bytes() == b"xxxx"
    candidates = _sealed(tmp_path)["candidates"]
    outcomes = {
        (candidates[row["candidate"]]["pair"], candidates[row["candidate"]]["arm"]): row["exit"]
        for row in _scores(tmp_path)
    }
    assert outcomes == {
        ("A-code", "control"): 1,
        ("A-code", "treatment"): 0,
        ("B-content", "control"): 0,
        ("B-content", "treatment"): 1,
    }


@pytest.mark.parametrize("parent_kind", ["loop", "dangling"])
def test_unresolvable_output_parent_refuses_without_reserving_namespace(
    tmp_path: Path, parent_kind: str
):
    cfg = _fixture(tmp_path, with_extra=True)
    (tmp_path / "cycle-a").symlink_to("cycle-b")
    if parent_kind == "loop":
        (tmp_path / "cycle-b").symlink_to("cycle-a")
    initial_names = {p.name for p in tmp_path.iterdir()} | {"config.json", "run_blinded_eval.py"}
    rejected = {**cfg, "run_note": "cycle-a/note.json"}

    result = _run(tmp_path, rejected)

    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "evidence" / "dispatch-count.txt").exists()
    assert {p.name for p in tmp_path.iterdir()} == initial_names
    corrected = _run(tmp_path, cfg)
    assert corrected.returncode == 0, corrected.stderr
    assert (tmp_path / "evidence" / "dispatch-count.txt").read_bytes() == b"xxxx"


def test_same_run_refuses_but_fresh_namespace_replay_preserves_first_run(tmp_path: Path):
    cfg = _fixture(tmp_path, with_extra=True)
    first = _run(tmp_path, cfg)
    assert first.returncode == 0, first.stderr
    marker = tmp_path / "evidence" / "dispatch-count.txt"
    assert marker.read_bytes() == b"xxxx"
    old_paths = [tmp_path / cfg[key] for key in ("sealed_map", "results", "run_note")]
    old_paths.extend((tmp_path / cfg["blinded"]).iterdir())
    original = {path: path.read_bytes() for path in old_paths}

    repeated = _run(tmp_path, cfg)
    assert repeated.returncode == 4, repeated.stderr
    assert marker.read_bytes() == b"xxxx"
    assert all(path.read_bytes() == body for path, body in original.items())

    replay = {
        **cfg,
        "blinded": "replay/blinded",
        "sealed_map": "replay/map/sealed-map.json",
        "results": "replay/results/scores.jsonl",
        "run_note": "replay/results/run-note.json",
    }
    fresh = _run(tmp_path, replay)
    assert fresh.returncode == 0, fresh.stderr
    assert marker.read_bytes() == b"xxxxxxxx"
    assert all(path.read_bytes() == body for path, body in original.items())
    assert set((tmp_path / cfg["blinded"]).iterdir()) == {
        path for path in original if path.parent == tmp_path / cfg["blinded"]
    }
    expected = {
        ("A-code", "control"): 1,
        ("A-code", "treatment"): 0,
        ("B-content", "control"): 0,
        ("B-content", "treatment"): 1,
    }
    for run in (cfg, replay):
        sealed = json.loads((tmp_path / run["sealed_map"]).read_text(encoding="utf-8"))
        scores = [
            json.loads(line)
            for line in (tmp_path / run["results"]).read_text(encoding="utf-8").splitlines()
        ]
        outcomes = {
            (sealed["candidates"][row["candidate"]]["pair"],
             sealed["candidates"][row["candidate"]]["arm"]): row["exit"]
            for row in scores
        }
        assert outcomes == expected
