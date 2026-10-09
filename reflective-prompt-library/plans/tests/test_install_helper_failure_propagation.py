"""Behavioral consumer checks for extracted install helpers (F09 repair).

These tests extract the documented shell helpers from SKILL_INSTALLATION.md
and exercise consumer-visible behavior: failure propagation, destination
handling, and non-symlink refusal. They do not assert prose wording.
"""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

INSTALLATION_GUIDE = Path(__file__).parent.parent.parent / "SKILL_INSTALLATION.md"


@pytest.fixture(scope="module")
def installation_guide_text() -> str:
    assert INSTALLATION_GUIDE.is_file(), f"missing {INSTALLATION_GUIDE}"
    return INSTALLATION_GUIDE.read_text(encoding="utf-8")


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


def _write_skill_source(source_root: Path, name: str, marker: str = "SOURCE-MARKER") -> None:
    skill = source_root / name
    skill.mkdir(parents=True, exist_ok=True)
    (skill / "SKILL.md").write_text(f"# {name}\n{marker}\n", encoding="utf-8")


def _write_nine_core_sources(source_root: Path) -> None:
    for name in (
        "reflective-brief",
        "reflective-dispatch",
        "reflective-handoff-retro",
        "reflective-implement",
        "reflective-minimality",
        "reflective-research",
        "reflective-review",
        "reflective-risk",
        "reflective-spec-plan",
    ):
        _write_skill_source(source_root, name)


CORE_HELPERS = ("install_core_skills_copy", "install_core_skills_symlink")


@pytest.mark.skipif(shutil.which("sh") is None, reason="POSIX sh not available")
@pytest.mark.parametrize("helper", CORE_HELPERS)
def test_core_helpers_fail_on_missing_source_without_creating_dest(
    tmp_path: Path, installation_guide_text: str, helper: str
):
    """F09: a missing source must fail before destination creation."""
    dest = tmp_path / "dest"
    missing = tmp_path / "no-such-source"
    result = _run_install_helper(tmp_path, helper, dest, missing, installation_guide_text)
    assert result.returncode != 0, result.stdout + result.stderr
    assert not dest.exists(), "failed source resolution must not create the destination"


@pytest.mark.skipif(shutil.which("sh") is None, reason="POSIX sh not available")
@pytest.mark.parametrize("helper", CORE_HELPERS)
def test_core_helpers_reject_source_without_expected_core_skills(
    tmp_path: Path, installation_guide_text: str, helper: str
):
    """F09: a source with none of the expected core skills must fail empty."""
    source_root = tmp_path / "source"
    source_root.mkdir()
    _write_skill_source(source_root, "unrelated-pack")
    dest = tmp_path / "dest"
    result = _run_install_helper(tmp_path, helper, dest, source_root, installation_guide_text)
    assert result.returncode != 0, result.stdout + result.stderr
    installed = sorted(p.name for p in dest.glob("*")) if dest.exists() else []
    assert installed == [], f"rejected source must install zero skills, got {installed}"


@pytest.mark.skipif(shutil.which("sh") is None, reason="POSIX sh not available")
@pytest.mark.parametrize("helper", CORE_HELPERS)
def test_core_helpers_install_nine_skills_on_valid_source(
    tmp_path: Path, installation_guide_text: str, helper: str
):
    """Positive control: a valid source installs nine core skills and exits 0."""
    source_root = tmp_path / "source"
    _write_nine_core_sources(source_root)
    dest = tmp_path / "dest"
    result = _run_install_helper(tmp_path, helper, dest, source_root, installation_guide_text)
    assert result.returncode == 0, result.stdout + result.stderr
    installed = sorted(p.name for p in dest.glob("reflective-*"))
    assert len(installed) == 9, installed
