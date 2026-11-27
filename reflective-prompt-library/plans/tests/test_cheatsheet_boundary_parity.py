"""Routed-surface holdout anti-leak and cheatsheet boundary-rule checks.

A ROUTE-001/002/003 fixture phrase is the eval answer key. ROUTING_CONTRACT R8
forbids that phrase from appearing verbatim in a routed surface: the cheatsheets
or a skill file. These checks keep those surfaces on boundary rules and labels
instead of the answer key.
"""

import sys
from pathlib import Path

import pytest

TESTS = Path(__file__).parent
PLANS = TESTS.parent
sys.path.insert(0, str(PLANS))
sys.path.insert(0, str(TESTS))

from route_paraphrase_eval import load_route_eval_config  # noqa: E402

from prompt_eval_helpers import (  # noqa: E402
    cheatsheet_en_path,
    cheatsheet_zh_tw_path,
)

EN_CHEATSHEET = cheatsheet_en_path()
ZH_CHEATSHEET = cheatsheet_zh_tw_path()

PHRASE_SECTIONS = ("intent_groups", "holdout_sets", "adversarial_sets")
FIXTURE_CONFIGS = (
    "route-001-paraphrase-eval.yaml",
    "route-002-holdout-eval.yaml",
    "route-003-adversarial-eval.yaml",
)

# Rules and labels the cheatsheets teach. None of these are fixture phrases.
EN_BOUNDARY_RULES = (
    "**Brief before plan**",
    "**Plan-only (no code)**",
    "**Plain review (non-production)**",
    "## `reflective-brief`",
    "## `reflective-spec-plan`",
    "## `reflective-review`",
    "## `reflective-minimality`",
    "## `reflective-dispatch`",
    "Catalog questions about which skill owns a library workflow, including handoff or retro, stay here.",
    "extra libraries can be cut",
)

ZH_BOUNDARY_RULES = (
    "**規劃前先釐清**",
    "**僅規劃不寫程式**",
    "**非正式環境審查**",
    "## `reflective-brief`",
    "## `reflective-spec-plan`",
    "## `reflective-review`",
    "## `reflective-minimality`",
    "## `reflective-dispatch`",
    "這個函式庫的 session handoff 由哪個 skill 處理",
    "這個 module 可以移除哪些 dependency",
    "寫 PRD 前先收斂範圍與假設",
    "審查 README 的清晰度，不是安全性",
    "寫 tickets 與驗收條件，但不要動 repo",
    "在紙上比較 API 設計，不要動 repository",
    "檢查 diff 的可讀性，不是 production 部署",
)


@pytest.fixture(scope="module")
def en_cheatsheet_text() -> str:
    assert EN_CHEATSHEET.is_file(), f"missing {EN_CHEATSHEET}"
    return EN_CHEATSHEET.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def zh_cheatsheet_text() -> str:
    assert ZH_CHEATSHEET.is_file(), f"missing {ZH_CHEATSHEET}"
    return ZH_CHEATSHEET.read_text(encoding="utf-8")


def _fixture_phrases() -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for name in FIXTURE_CONFIGS:
        config = load_route_eval_config(PLANS / name)
        for section in PHRASE_SECTIONS:
            for group in config.get(section) or []:
                for phrase in group.get("phrases") or []:
                    if isinstance(phrase, str) and phrase.strip():
                        found.append((name, phrase))
    return found


def test_cheatsheets_exclude_verbatim_fixture_phrases(
    en_cheatsheet_text: str,
    zh_cheatsheet_text: str,
):
    """No ROUTE-001/002/003 fixture phrase is a case-insensitive substring."""
    en_haystack = en_cheatsheet_text.lower()
    zh_haystack = zh_cheatsheet_text.lower()
    leaks: list[str] = []
    for name, phrase in _fixture_phrases():
        needle = phrase.lower()
        if needle in en_haystack:
            leaks.append(f"EN {name}: {phrase}")
        if needle in zh_haystack:
            leaks.append(f"zh-TW {name}: {phrase}")
    assert not leaks, "fixture phrase leaked into a cheatsheet:\n" + "\n".join(leaks)


def test_skill_files_exclude_verbatim_fixture_phrases():
    """R8 covers skill descriptions too: no fixture phrase appears in any SKILL.md."""
    skills = sorted((PLANS.parent / "skills").glob("*/SKILL.md"))
    assert skills, "no skill files found"
    texts = {path.parent.name: path.read_text(encoding="utf-8").lower() for path in skills}
    leaks = [f"{skill} {name}: {phrase}" for name, phrase in _fixture_phrases()
             for skill, text in texts.items() if phrase.lower() in text]
    assert not leaks, "fixture phrase leaked into a skill file:\n" + "\n".join(leaks)


@pytest.mark.parametrize("rule", EN_BOUNDARY_RULES)
def test_english_cheatsheet_teaches_boundary_rules(en_cheatsheet_text: str, rule: str):
    assert rule in en_cheatsheet_text, f"English cheatsheet missing boundary rule: {rule!r}"


@pytest.mark.parametrize("rule", ZH_BOUNDARY_RULES)
def test_zh_tw_cheatsheet_teaches_boundary_rules(zh_cheatsheet_text: str, rule: str):
    assert rule in zh_cheatsheet_text, f"zh-TW cheatsheet missing boundary rule: {rule!r}"
