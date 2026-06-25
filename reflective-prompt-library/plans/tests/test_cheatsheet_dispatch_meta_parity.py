"""Anti-drift checks for dispatch-meta ROUTE-003 cues in EN/zh-TW cheatsheets."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from test_validate_route_fixture import DISPATCH_META_SKILL_TRAP_PROBES  # noqa: E402

SKILLS = Path(__file__).parent.parent.parent / "skills"
EN_CHEATSHEET = SKILLS / "SKILL_TRIGGER_CHEATSHEET.md"
ZH_CHEATSHEET = SKILLS / "SKILL_TRIGGER_CHEATSHEET.zh-TW.md"


@pytest.fixture(scope="module")
def en_cheatsheet_text() -> str:
    assert EN_CHEATSHEET.is_file(), f"missing {EN_CHEATSHEET}"
    return EN_CHEATSHEET.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def zh_cheatsheet_text() -> str:
    assert ZH_CHEATSHEET.is_file(), f"missing {ZH_CHEATSHEET}"
    return ZH_CHEATSHEET.read_text(encoding="utf-8")


@pytest.mark.parametrize("cue", DISPATCH_META_SKILL_TRAP_PROBES)
def test_dispatch_meta_cues_present_in_english_cheatsheet(en_cheatsheet_text: str, cue: str):
    haystack = en_cheatsheet_text.lower()
    assert cue.lower() in haystack, f"English cheatsheet missing dispatch-meta cue: {cue!r}"


@pytest.mark.parametrize("cue", DISPATCH_META_SKILL_TRAP_PROBES)
def test_dispatch_meta_cues_present_in_zh_tw_cheatsheet(zh_cheatsheet_text: str, cue: str):
    haystack = zh_cheatsheet_text.lower()
    assert cue.lower() in haystack, f"zh-TW cheatsheet missing dispatch-meta cue: {cue!r}"
