"""Anti-drift tests for README governance surface and skill-count wording."""

import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    cheatsheet_en_path,
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
INSTALLATION_GUIDE = LIBRARY_README.parent / "SKILL_INSTALLATION.md"
INSTALLATION_GUIDE_ZH = LIBRARY_README.parent / "SKILL_INSTALLATION.zh-TW.md"

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


@pytest.fixture(scope="module")
def installation_guide_text() -> str:
    assert INSTALLATION_GUIDE.is_file(), f"missing {INSTALLATION_GUIDE}"
    return INSTALLATION_GUIDE.read_text(encoding="utf-8")


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


def test_methodology_map_en_lists_bounded_core_and_domain_packs(
    methodology_map_en_text: str,
):
    fit_check = methodology_map_en_text.split("## Repo Fit Check", 1)[1]
    assert "nine frozen core workflow skills" in fit_check
    assert "domain packs outside core routing" in fit_check
    on_disk = {p.parent.name for p in library_skills_dir().glob("*/SKILL.md")}
    assert on_disk == set(CORE_SKILLS) | set(DOMAIN_PACK_SKILLS)
    assert len(CORE_SKILLS) == 9
    assert "gated, not never" in methodology_map_en_text


def test_skill_map_lists_bounded_core_skills(skill_map_text: str):
    core = skill_map_text.split("## Core Architecture", 1)[1].split("##", 1)[0]
    assert "bounded" in core
    assert "optimality" in core
    for skill in CORE_SKILLS:
        assert f"`{skill}`" in core
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


def test_installation_defaults_to_core_and_opts_into_registered_packs(
    installation_guide_text: str,
):
    assert all(name.startswith("reflective-") for name in CORE_SKILLS)
    assert 'for skill in "$source_root"/reflective-*/' in installation_guide_text
    assert 'test -f "$skill/SKILL.md"' in installation_guide_text
    assert "install_core_skills_copy()" in installation_guide_text
    assert "install_core_skills_symlink()" in installation_guide_text
    assert "install_domain_packs_copy()" in installation_guide_text
    assert "install_domain_packs_symlink()" in installation_guide_text
    assert "install_skill_examples_copy()" in installation_guide_text
    assert "install_skill_examples_symlink()" in installation_guide_text
    assert "<destination>/examples/<skill-name>.examples.md" in installation_guide_text
    assert "cp -R reflective-prompt-library/skills/*" not in installation_guide_text
    assert "for skill in reflective-prompt-library/skills/*;" not in installation_guide_text

    for helper in ("copy", "symlink"):
        pack_loop = re.search(
            rf"install_domain_packs_{helper}\(\).*?for name in ([^;]+); do",
            installation_guide_text,
            re.DOTALL,
        )
        assert pack_loop, f"domain-pack {helper} helper loop missing"
        assert set(pack_loop.group(1).split()) == set(DOMAIN_PACK_SKILLS)


def _extract_helper(installation_guide_text: str, helper: str) -> str:
    start = installation_guide_text.index(f"{helper}() {{")
    end = installation_guide_text.index("\n}\n", start)
    return installation_guide_text[start:end]


def _run_install_helper(
    tmp_path: Path,
    helper: str,
    dest: Path,
    source_root: Path,
    installation_guide_text: str,
) -> "subprocess.CompletedProcess":
    body = _extract_helper(installation_guide_text, helper)
    script = tmp_path / f"{helper}.sh"
    script.write_text(
        "#!/bin/sh\n" + body + "\n}\n" + helper + ' "$1" "$2"\n',
        encoding="utf-8",
    )
    return subprocess.run(
        ["sh", str(script), str(dest), str(source_root)],
        capture_output=True,
        text=True,
        check=False,
    )


def _write_skill_source(source_root: Path, name: str, marker: str) -> None:
    skill = source_root / name
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text(f"# {name}\n{marker}\n", encoding="utf-8")


def _write_full_source(source_root: Path) -> None:
    _write_skill_source(source_root, "reflective-brief", "SOURCE-MARKER")
    for pack in DOMAIN_PACK_SKILLS:
        _write_skill_source(source_root, pack, "SOURCE-MARKER")


@pytest.mark.skipif(shutil.which("sh") is None, reason="POSIX sh not available")
def test_install_symlink_helpers_preserve_real_directory_and_fail(
    tmp_path: Path, installation_guide_text: str
):
    """WR-07: extracted helpers must refuse real-directory collisions."""
    source_root = tmp_path / "source"
    _write_full_source(source_root)
    for helper, name in (
        ("install_core_skills_symlink", "reflective-brief"),
        ("install_domain_packs_symlink", "flow-control-generator"),
    ):
        dest = tmp_path / f"dest-dir-{name}"
        target = dest / name
        target.mkdir(parents=True)
        (target / "SKILL.md").write_text("# old\nOLD-INSTALLED-COPY\n", encoding="utf-8")
        result = _run_install_helper(tmp_path, helper, dest, source_root, installation_guide_text)
        assert result.returncode != 0, result.stdout + result.stderr
        assert not target.is_symlink()
        assert "OLD-INSTALLED-COPY" in (target / "SKILL.md").read_text(encoding="utf-8")


@pytest.mark.skipif(shutil.which("sh") is None, reason="POSIX sh not available")
def test_install_symlink_helpers_preserve_real_file_and_fail(
    tmp_path: Path, installation_guide_text: str
):
    """WR-07: the same guard must refuse pre-existing real files."""
    source_root = tmp_path / "source"
    _write_full_source(source_root)
    for helper, name in (
        ("install_core_skills_symlink", "reflective-brief"),
        ("install_domain_packs_symlink", "flow-control-generator"),
    ):
        dest = tmp_path / f"dest-file-{name}"
        dest.mkdir(parents=True)
        target = dest / name
        target.write_text("OLD-INSTALLED-COPY\n", encoding="utf-8")
        result = _run_install_helper(tmp_path, helper, dest, source_root, installation_guide_text)
        assert result.returncode != 0, result.stdout + result.stderr
        assert not target.is_symlink()
        assert "OLD-INSTALLED-COPY" in target.read_text(encoding="utf-8")


@pytest.mark.skipif(shutil.which("sh") is None, reason="POSIX sh not available")
def test_install_symlink_helpers_replace_existing_links(
    tmp_path: Path, installation_guide_text: str
):
    """WR-07: fresh installs and re-runs over existing symlinks stay valid."""
    source_root = tmp_path / "source"
    _write_full_source(source_root)
    dest = tmp_path / "dest"
    for helper in ("install_core_skills_symlink", "install_domain_packs_symlink"):
        first = _run_install_helper(tmp_path, helper, dest, source_root, installation_guide_text)
        assert first.returncode == 0, first.stdout + first.stderr
        second = _run_install_helper(tmp_path, helper, dest, source_root, installation_guide_text)
        assert second.returncode == 0, second.stdout + second.stderr
    brief = dest / "reflective-brief"
    pack = dest / "flow-control-generator"
    assert brief.is_symlink() and pack.is_symlink()
    assert "SOURCE-MARKER" in (brief / "SKILL.md").read_text(encoding="utf-8")
    assert "SOURCE-MARKER" in (pack / "SKILL.md").read_text(encoding="utf-8")

def test_en_cheatsheet_domain_pack_appendix_lists_registry():
    text = cheatsheet_en_path().read_text(encoding="utf-8")
    section = text.split(
        "## Domain packs (host-invoked; not core routing)", 1
    )[1].split("\n## ", 1)[0]
    for pack in DOMAIN_PACK_SKILLS:
        assert f"`{pack}`" in section, pack
    assert "`reflective-dispatch`" in section


def test_installation_human_review_set_matches_skill_metadata(
    installation_guide_text: str,
):
    review_required = {
        path.parent.name
        for path in library_skills_dir().glob("*/SKILL.md")
        if "human_review_required: true" in path.read_text(encoding="utf-8")
    }
    assert review_required

    en_section = installation_guide_text.split(
        "### Enforcing TeaPrompt's review gates host-side", 1
    )[1].split("\n### ", 1)[0]
    zh_section = INSTALLATION_GUIDE_ZH.read_text(encoding="utf-8").split(
        "## 安全性注意事項", 1
    )[1].split("\n## ", 1)[0]
    for skill in review_required:
        assert f"`{skill}`" in en_section
        assert f"`{skill}`" in zh_section
    assert "`human_review_required: true`" in zh_section
    assert "examples/*.examples.md" in zh_section

    assert "host" in zh_section
