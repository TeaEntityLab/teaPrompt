"""Anti-drift checks for boundary quick-cue summary in EN/zh-TW cheatsheets."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from test_validate_route_fixture import (  # noqa: E402
    BOUNDARY_QUICK_CUE_EN_MARKERS,
    BOUNDARY_QUICK_CUE_PROBE_SNIPPETS_EN,
    BOUNDARY_QUICK_CUE_PROBE_SNIPPETS_ZH,
    BOUNDARY_QUICK_CUE_ZH_MARKERS,
)

SKILLS = Path(__file__).parent.parent.parent / "skills"
EN_CHEATSHEET = SKILLS / "SKILL_TRIGGER_CHEATSHEET.md"
ZH_CHEATSHEET = SKILLS / "SKILL_TRIGGER_CHEATSHEET.zh-TW.md"
DISPATCH_HEADER = "## `reflective-dispatch`"


def _boundary_quick_cues_block(text: str, header: str) -> str:
    start = text.find(header)
    assert start != -1, f"missing boundary quick-cue header: {header!r}"
    end = text.find(DISPATCH_HEADER, start)
    assert end != -1, f"missing {DISPATCH_HEADER!r} after boundary quick-cue header"
    return text[start:end]


@pytest.fixture(scope="module")
def en_boundary_quick_cues() -> str:
    return _boundary_quick_cues_block(EN_CHEATSHEET.read_text(encoding="utf-8"), BOUNDARY_QUICK_CUE_EN_MARKERS[0])


@pytest.fixture(scope="module")
def zh_boundary_quick_cues() -> str:
    return _boundary_quick_cues_block(ZH_CHEATSHEET.read_text(encoding="utf-8"), BOUNDARY_QUICK_CUE_ZH_MARKERS[0])


@pytest.mark.parametrize("marker", BOUNDARY_QUICK_CUE_EN_MARKERS)
def test_boundary_quick_cues_present_in_english_summary(en_boundary_quick_cues: str, marker: str):
    assert marker in en_boundary_quick_cues, f"English boundary quick-cue summary missing: {marker!r}"


@pytest.mark.parametrize("marker", BOUNDARY_QUICK_CUE_ZH_MARKERS)
def test_boundary_quick_cues_present_in_zh_tw_summary(zh_boundary_quick_cues: str, marker: str):
    assert marker in zh_boundary_quick_cues, f"zh-TW boundary quick-cue summary missing: {marker!r}"

@pytest.mark.parametrize("snippet", BOUNDARY_QUICK_CUE_PROBE_SNIPPETS_EN)
def test_boundary_quick_cue_probe_snippets_in_english_summary(en_boundary_quick_cues: str, snippet: str):
    assert snippet.lower() in en_boundary_quick_cues.lower(), (
        f"English boundary quick-cue summary missing probe snippet: {snippet!r}"
    )


@pytest.mark.parametrize("snippet", BOUNDARY_QUICK_CUE_PROBE_SNIPPETS_ZH)
def test_boundary_quick_cue_probe_snippets_in_zh_tw_summary(zh_boundary_quick_cues: str, snippet: str):
    assert snippet.lower() in zh_boundary_quick_cues.lower(), (
        f"zh-TW boundary quick-cue summary missing probe snippet: {snippet!r}"
    )


def test_boundary_quick_cue_probe_snippet_counts_match_markers():
    assert len(BOUNDARY_QUICK_CUE_PROBE_SNIPPETS_EN) == len(BOUNDARY_QUICK_CUE_EN_MARKERS) - 1
    assert len(BOUNDARY_QUICK_CUE_PROBE_SNIPPETS_ZH) == len(BOUNDARY_QUICK_CUE_ZH_MARKERS) - 1

