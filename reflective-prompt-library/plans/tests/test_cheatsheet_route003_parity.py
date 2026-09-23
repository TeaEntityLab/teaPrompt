"""Anti-drift checks for ROUTE-003 adversarial cues in EN/zh-TW cheatsheets."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from test_validate_route_fixture import ROUTE_003_ADVERSARIAL_CHEATSHEET_CUES  # noqa: E402

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
    "plan the approved spec without repo changes": "規劃已核准 spec，但不要更動 repo",
    "keep working until every test in test/auth passes": "持續修到 test/auth 的每個測試都通過",
    "write a bash loop that reruns the agent until the verifier passes": "寫一個 bash 迴圈，重跑 agent 直到 verifier 通過",
    "design a handoff workflow specification without runtime code": "設計 handoff workflow 規格，但不要寫 runtime code",
    "patch the trivial null check in code": "在程式裡修補這個 trivial null check",
    "verify production auth change will not expose secrets": "驗證 production auth 變更不會洩漏 secrets",
    "inspect this patch for regressions before merge": "merge 前檢查這個 patch 有沒有 regression",
    "six-lens debate on whether to merge these skills": "用六個視角辯論是否合併這些 skills",
    "which workflow skill should run for this library task": "這個函式庫任務該由哪個 workflow skill 執行",
    "lessons learned retro after this sprint": "這個 sprint 結束後做 lessons learned retro",
    "compare official docs for both libraries before deciding": "決定前先比較兩個函式庫的官方文件",
    "which reflective workflow skill covers handoff retro": "handoff retro 由哪個 reflective workflow skill 涵蓋",
    "align stakeholders on goals before writing tickets": "寫工單前先對齊 stakeholder 目標",
    "automate the recurring manual release check as a deterministic test in the repo": "把重複的人工 release 檢查自動化成 repo 裡的確定性測試",
}


@pytest.mark.parametrize("cue", ROUTE_003_ADVERSARIAL_CHEATSHEET_CUES)
def test_route_003_cues_present_in_english_cheatsheet(en_cheatsheet_text: str, cue: str):
    haystack = en_cheatsheet_text.lower()
    assert cue.lower() in haystack, f"English cheatsheet missing ROUTE-003 adversarial cue: {cue!r}"


@pytest.mark.parametrize("cue", ROUTE_003_ADVERSARIAL_CHEATSHEET_CUES)
def test_route_003_cues_present_in_zh_tw_cheatsheet(zh_cheatsheet_text: str, cue: str):
    expected = ZH_NATIVE_EQUIVALENTS.get(cue, cue)
    haystack = zh_cheatsheet_text.lower()
    assert expected.lower() in haystack, f"zh-TW cheatsheet missing ROUTE-003 adversarial cue: {expected!r}"
