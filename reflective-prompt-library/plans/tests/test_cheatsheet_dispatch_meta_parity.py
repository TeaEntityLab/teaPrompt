"""Anti-drift checks for dispatch-meta ROUTE-003 cues in EN/zh-TW cheatsheets."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from test_validate_route_fixture import DISPATCH_META_SKILL_TRAP_PROBES  # noqa: E402

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
# zh-TW cheatsheet cues are zh-native — the 2026-09-23 constraint review
# stopped embedding verbatim English fixture phrases (the eval's answer
# key) into the production routing surface.
ZH_NATIVE_EQUIVALENTS = {
    "which reflective workflow skill fits a routing-only mixed intent": "純路由的混合意圖適合哪個 reflective workflow skill",
    "which reflective workflow skill should handle routing-only mixed intent": "純路由的混合意圖該由哪個 reflective workflow skill 處理",
}



@pytest.mark.parametrize("cue", DISPATCH_META_SKILL_TRAP_PROBES)
def test_dispatch_meta_cues_present_in_english_cheatsheet(en_cheatsheet_text: str, cue: str):
    haystack = en_cheatsheet_text.lower()
    assert cue.lower() in haystack, f"English cheatsheet missing dispatch-meta cue: {cue!r}"


@pytest.mark.parametrize("cue", DISPATCH_META_SKILL_TRAP_PROBES)
def test_dispatch_meta_cues_present_in_zh_tw_cheatsheet(zh_cheatsheet_text: str, cue: str):
    expected = ZH_NATIVE_EQUIVALENTS.get(cue, cue)
    haystack = zh_cheatsheet_text.lower()
    assert expected.lower() in haystack, f"zh-TW cheatsheet missing dispatch-meta cue: {expected!r}"
