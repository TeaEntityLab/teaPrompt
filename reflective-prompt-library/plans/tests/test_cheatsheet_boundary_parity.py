"""Anti-drift checks for ROUTE-002 boundary cues in EN/zh-TW cheatsheets."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from test_validate_route_fixture import BOUNDARY_CHEATSHEET_CUES  # noqa: E402

from prompt_eval_helpers import (  # noqa: E402
    cheatsheet_en_path,
    cheatsheet_zh_tw_path,
)

EN_CHEATSHEET = cheatsheet_en_path()
ZH_CHEATSHEET = cheatsheet_zh_tw_path()


@pytest.fixture(scope="module")
def en_cheatsheet_text() -> str:
    assert EN_CHEATSHEET.is_file(), f"missing {EN_CHEATSHEET}"
    return EN_CHEATSHEET.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def zh_cheatsheet_text() -> str:
    assert ZH_CHEATSHEET.is_file(), f"missing {ZH_CHEATSHEET}"
    return ZH_CHEATSHEET.read_text(encoding="utf-8")
# zh-TW cheatsheet cues are zh-native where a translation exists — the
# 2026-09-23 constraint review stopped embedding verbatim English fixture
# phrases (the eval's answer key) into the production routing surface.
# Cues not listed here are asserted verbatim (zh/mixed probes already
# written in zh-TW).
ZH_NATIVE_EQUIVALENTS = {
    "narrow scope and assumptions before writing the PRD": "寫 PRD 前先收斂範圍與假設",
    "what dependencies can we remove from this module": "這個 module 可以移除哪些 dependency",
    "which skill handles session handoff in this library": "這個函式庫的 session handoff 由哪個 skill 處理",
    "review the README for clarity not security": "審查 README 的清晰度，不是安全性",
    "write tickets and acceptance criteria without touching the repo": "寫 tickets 與驗收條件，但不要動 repo",
    "check the diff for readability not production deploy": "檢查 diff 的可讀性，不是 production 部署",
    "compare API designs on paper without touching the repository": "在紙上比較 API 設計，不要動 repository",
    "compare API design options on paper without touching the repository": "在紙上比較 API 設計選項，不要動 repository",
}



@pytest.mark.parametrize("cue", BOUNDARY_CHEATSHEET_CUES)
def test_boundary_cues_present_in_english_cheatsheet(en_cheatsheet_text: str, cue: str):
    haystack = en_cheatsheet_text.lower()
    assert cue.lower() in haystack, f"English cheatsheet missing ROUTE-002 boundary cue: {cue!r}"


@pytest.mark.parametrize("cue", BOUNDARY_CHEATSHEET_CUES)
def test_boundary_cues_present_in_zh_tw_cheatsheet(zh_cheatsheet_text: str, cue: str):
    expected = ZH_NATIVE_EQUIVALENTS.get(cue, cue)
    haystack = zh_cheatsheet_text.lower()
    assert expected.lower() in haystack, f"zh-TW cheatsheet missing ROUTE-002 boundary cue: {expected!r}"
