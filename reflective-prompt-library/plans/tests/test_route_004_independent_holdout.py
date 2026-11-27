"""ROUTE-004 independent holdout guards (RFT-3, 2026-11-27).

ROUTE-004 was authored by an agent that saw only the nine core skill descriptions and labeled
blind by a second agent. It is a measurement, not a tuning set, so these guards check:
- the fixture keeps one balanced group per core workflow;
- held-out accuracy never falls below the baseline measured before any tuning (35/63);
- no ROUTE-004 phrase has leaked into a routed surface, the router or another fixture —
  a leaked phrase is no longer held out.
"""

import re
import sys
from pathlib import Path

PLANS = Path(__file__).resolve().parent.parent
LIBRARY = PLANS.parent
sys.path.insert(0, str(PLANS))

from route_paraphrase_eval import ParaphraseEval, load_route_eval_config  # noqa: E402
from validate_route_fixture import VALID_WORKFLOWS  # noqa: E402

ROUTE_004 = PLANS / "route-004-independent-holdout-eval.yaml"
BASELINE_MATCHES, BASELINE_TOTAL = 35, 63
CJK = re.compile(r"[\u4e00-\u9fff]")


def _groups():
    return load_route_eval_config(ROUTE_004)["holdout_sets"]


def _phrases():
    return [p for g in _groups() for p in g["phrases"]]


def test_route_004_has_one_balanced_group_per_core_workflow():
    groups = _groups()
    assert sorted(g["expected_workflow"] for g in groups) == sorted(VALID_WORKFLOWS)
    for group in groups:
        assert len(group["phrases"]) == 7, group["name"]
        assert sum(bool(CJK.search(p)) for p in group["phrases"]) >= 3, group["name"]
    assert len(set(_phrases())) == BASELINE_TOTAL


def test_route_004_accuracy_never_drops_below_pre_tuning_baseline():
    results = ParaphraseEval(str(LIBRARY.parent), ROUTE_004).run_eval()
    summary = results["summary"]
    assert summary["total_paraphrases"] == BASELINE_TOTAL
    assert summary["consistency_rate"] >= BASELINE_MATCHES / BASELINE_TOTAL


def test_route_004_phrases_stay_out_of_routed_surfaces_router_and_other_fixtures():
    surfaces = {
        "SKILL_TRIGGER_CHEATSHEET.md": LIBRARY / "skills" / "SKILL_TRIGGER_CHEATSHEET.md",
        "SKILL_TRIGGER_CHEATSHEET.zh-TW.md": LIBRARY / "skills" / "SKILL_TRIGGER_CHEATSHEET.zh-TW.md",
        "route_paraphrase_eval.py": PLANS / "route_paraphrase_eval.py",
        "route-001": PLANS / "route-001-paraphrase-eval.yaml",
        "route-002": PLANS / "route-002-holdout-eval.yaml",
        "route-003": PLANS / "route-003-adversarial-eval.yaml",
    }
    for skill in sorted((LIBRARY / "skills").glob("*/SKILL.md")):
        surfaces[str(skill.relative_to(LIBRARY))] = skill
    texts = {name: path.read_text(encoding="utf-8").lower() for name, path in surfaces.items()}
    leaks = [(phrase, name) for phrase in _phrases() for name, text in texts.items() if phrase.lower() in text]
    assert leaks == []
