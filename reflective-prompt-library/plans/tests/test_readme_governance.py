"""Anti-drift tests for README governance surface and skill-count wording."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from prompt_eval_helpers import (  # noqa: E402
    library_readme_path,
    library_skills_dir,
    methodology_map_en_path,
    methodology_map_zh_tw_path,
    repo_readme_path,
    skill_map_path,
)
from validate_skill_examples import CORE_SKILLS, DOMAIN_PACK_SKILLS  # noqa: E402

LIBRARY_README = library_readme_path()
ROOT_README = repo_readme_path()
METHODOLOGY_MAP_ZH = methodology_map_zh_tw_path()
METHODOLOGY_MAP_EN = methodology_map_en_path()
SKILL_MAP = skill_map_path()

CURRENT_PANEL_ROUND = "101"
CURRENT_PANEL_OPTIONS = "A–IE"


@pytest.fixture(scope="module")
def library_readme_text() -> str:
    assert LIBRARY_README.is_file(), f"missing {LIBRARY_README}"
    return LIBRARY_README.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def root_readme_text() -> str:
    assert ROOT_README.is_file(), f"missing {ROOT_README}"
    return ROOT_README.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def methodology_map_zh_text() -> str:
    assert METHODOLOGY_MAP_ZH.is_file(), f"missing {METHODOLOGY_MAP_ZH}"
    return METHODOLOGY_MAP_ZH.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def methodology_map_en_text() -> str:
    assert METHODOLOGY_MAP_EN.is_file(), f"missing {METHODOLOGY_MAP_EN}"
    return METHODOLOGY_MAP_EN.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def skill_map_text() -> str:
    assert SKILL_MAP.is_file(), f"missing {SKILL_MAP}"
    return SKILL_MAP.read_text(encoding="utf-8")


def test_library_readme_panel_record_current(library_readme_text: str):
    assert f"Rounds 1–{CURRENT_PANEL_ROUND}" in library_readme_text
    assert f"options {CURRENT_PANEL_OPTIONS}" in library_readme_text
    assert "Rounds 1–20" not in library_readme_text
    assert "options A–AJ" not in library_readme_text


def test_library_readme_requires_make_all_for_claims(library_readme_text: str):
    section = library_readme_text.split("## Governance Panel Record", 1)[1].split("##", 1)[0]
    assert "`make all`" in section


def test_root_readme_has_north_star_and_governance(root_readme_text: str):
    assert "## North Star" in root_readme_text
    assert "## Governance" in root_readme_text
    assert "CONTRIBUTING.md" in root_readme_text
    assert f"Rounds 1–{CURRENT_PANEL_ROUND}" in root_readme_text


def test_methodology_map_zh_tw_lists_nine_skills(methodology_map_zh_text: str):
    assert "9 個" in methodology_map_zh_text
    assert "8 個生命週期技能" not in methodology_map_zh_text


def test_methodology_map_en_lists_nine_frozen_skills(methodology_map_en_text: str):
    fit_check = methodology_map_en_text.split("## Repo Fit Check", 1)[1]
    assert "nine frozen workflow skills" in fit_check
    assert "8 lifecycle skills" not in fit_check
    # Wording must match reality: nine frozen core contracts on disk, plus
    # registered domain packs only (Option B, 2026-07-11 flow-control panel).
    on_disk = {p.parent.name for p in library_skills_dir().glob("*/SKILL.md")}
    assert on_disk == set(CORE_SKILLS) | set(DOMAIN_PACK_SKILLS)
    assert len(CORE_SKILLS) == 9
    # Candidate #1 (2026-07-06): the frozen gloss must accompany the phrase.
    assert "gated, not never" in methodology_map_en_text


def test_skill_map_lists_nine_frozen_skills(skill_map_text: str):
    core = skill_map_text.split("## Core Architecture", 1)[1].split("##", 1)[0]
    assert "nine frozen workflow skills" in core
    assert "eight lifecycle skills" not in core
    assert skill_map_text.count("`reflective-") >= 9
    on_disk = {p.parent.name for p in library_skills_dir().glob("*/SKILL.md")}
    assert on_disk == set(CORE_SKILLS) | set(DOMAIN_PACK_SKILLS)
    assert len(CORE_SKILLS) == 9
    assert "gated, not never" in core


def test_skill_map_lists_domain_packs(skill_map_text: str):
    """2026-07-11 flow-control pack panel: registered packs stay discoverable."""
    assert "## Registered domain packs" in skill_map_text
    section = skill_map_text.split("## Registered domain packs", 1)[1].split("\n## ", 1)[0]
    for pack in DOMAIN_PACK_SKILLS:
        assert f"`{pack}`" in section, pack
    assert "not selected by `reflective-dispatch`" in section
