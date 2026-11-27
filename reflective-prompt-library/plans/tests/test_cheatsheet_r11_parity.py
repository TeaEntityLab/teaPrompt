"""Anti-drift checks for approved-spec delivery rules in EN/zh-TW cheatsheets."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))


from prompt_eval_helpers import (  # noqa: E402
    cheatsheet_en_path,
    cheatsheet_zh_tw_path,
)

EN_CHEATSHEET = cheatsheet_en_path()
ZH_CHEATSHEET = cheatsheet_zh_tw_path()

EN_APPROVED_SPEC_IMPLEMENT_RULES = (
    "**Approved spec delivery**",
    "Land the approved spec into the codebase.",
    "Code the accepted specification into the repo.",
)

EN_PLAN_ONLY_APPROVED_SPEC_RULES = (
    "**Plan-only (no code)**",
    "leave the repo untouched",
    "Open tickets from an already accepted specification and stop before coding.",
)

# zh-TW cues are boundary guidance, not ROUTE-003 fixture phrases.
ZH_APPROVED_SPEC_IMPLEMENT_CUES = (
    "把已核准的規格寫進 repo",
    "實作已核准 spec 到 repository",
    "把已核准規格合併進程式庫",
)

ZH_PLAN_ONLY_APPROVED_SPEC_CUES = (
    "從已核准 spec 開 tickets，但不要實作",
    "規劃已核准 spec，但不要更動 repo",
    "從已核准 spec 草擬 rollout plan，但不要編輯 repo",
)


@pytest.fixture(scope="module")
def en_cheatsheet_text() -> str:
    assert EN_CHEATSHEET.is_file(), f"missing {EN_CHEATSHEET}"
    return EN_CHEATSHEET.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def zh_cheatsheet_text() -> str:
    assert ZH_CHEATSHEET.is_file(), f"missing {ZH_CHEATSHEET}"
    return ZH_CHEATSHEET.read_text(encoding="utf-8")


@pytest.mark.parametrize("rule", EN_APPROVED_SPEC_IMPLEMENT_RULES)
def test_approved_spec_rules_present_in_english_cheatsheet(en_cheatsheet_text: str, rule: str):
    assert rule in en_cheatsheet_text, f"English cheatsheet missing approved-spec rule: {rule!r}"


@pytest.mark.parametrize("cue", ZH_APPROVED_SPEC_IMPLEMENT_CUES)
def test_approved_spec_cues_present_in_zh_tw_cheatsheet(zh_cheatsheet_text: str, cue: str):
    assert cue in zh_cheatsheet_text, f"zh-TW cheatsheet missing approved-spec cue: {cue!r}"


@pytest.mark.parametrize("rule", EN_PLAN_ONLY_APPROVED_SPEC_RULES)
def test_plan_only_approved_spec_rules_present_in_english_cheatsheet(
    en_cheatsheet_text: str, rule: str
):
    assert rule in en_cheatsheet_text, (
        f"English cheatsheet missing plan-only approved-spec rule: {rule!r}"
    )


@pytest.mark.parametrize("cue", ZH_PLAN_ONLY_APPROVED_SPEC_CUES)
def test_plan_only_approved_spec_cues_present_in_zh_tw_cheatsheet(zh_cheatsheet_text: str, cue: str):
    haystack = zh_cheatsheet_text.lower()
    assert cue.lower() in haystack, f"zh-TW cheatsheet missing zh-native plan-only cue: {cue!r}"
