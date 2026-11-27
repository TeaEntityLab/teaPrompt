"""Behavioral consumer checks for extracted install helpers (F09 repair).

These tests extract the documented shell helpers from SKILL_INSTALLATION.md
and exercise consumer-visible behavior: failure propagation, destination
handling, and non-symlink refusal. They do not assert prose wording. A later
block covers the pinned-install helper's failure and replacement rules.

WLR-02 also executes the localized copy recipe with the canonical helper
loaded, so restoring an unchecked raw-copy path is a consumer-visible failure.
"""

import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

INSTALLATION_GUIDE = Path(__file__).parent.parent.parent / "SKILL_INSTALLATION.md"
INSTALLATION_GUIDE_ZH = Path(__file__).parent.parent.parent / "SKILL_INSTALLATION.zh-TW.md"


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


@pytest.fixture(scope="module")
def installation_guide_zh_text() -> str:
    assert INSTALLATION_GUIDE_ZH.is_file(), f"missing {INSTALLATION_GUIDE_ZH}"
    return INSTALLATION_GUIDE_ZH.read_text(encoding="utf-8")


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


@pytest.mark.skipif(shutil.which("sh") is None, reason="POSIX sh not available")
@pytest.mark.parametrize("source_kind", ("valid", "no-skill-file"))
def test_localized_copy_recipe_requires_skill_files(
    tmp_path: Path, installation_guide_text: str,
    installation_guide_zh_text: str, source_kind: str,
):
    """WLR-02: execute the advertised path, not merely the helper it names."""
    source_root = tmp_path / "reflective-prompt-library" / "skills"
    if source_kind == "valid":
        _write_nine_core_sources(source_root)
    else:
        incomplete = source_root / "reflective-brief"
        incomplete.mkdir(parents=True)
        (incomplete / "notes.txt").write_text("no skill file\n", encoding="utf-8")
    section = installation_guide_zh_text.split("## Claude Code\n", 1)[1]
    recipe = re.search(r"```bash\n(.*?)```", section, re.DOTALL).group(1)
    helper = _extract_helper(installation_guide_text, "install_core_skills_copy")
    result = subprocess.run(
        ["sh"], input=helper + "\n}\n" + recipe, cwd=tmp_path,
        capture_output=True, text=True, check=False,
    )
    dest = tmp_path / ".claude" / "skills"
    installed = sorted(dest.glob("reflective-*/SKILL.md"))
    if source_kind == "valid":
        assert result.returncode == 0, result.stdout + result.stderr
        assert len(installed) == 9, installed
    else:
        assert result.returncode != 0, result.stdout + result.stderr
        assert not dest.exists(), "rejected source must not publish an installation"


# --- install_skills_pinned --------------------------------------------------


def _extract_pinned_helper(installation_guide_text: str) -> str:
    return _extract_helper(installation_guide_text, "install_skills_pinned")


def _git_env() -> dict:
    env = dict(os.environ)
    env.update(
        GIT_AUTHOR_NAME="TeaPrompt Test",
        GIT_AUTHOR_EMAIL="teaprompt-test@example.com",
        GIT_COMMITTER_NAME="TeaPrompt Test",
        GIT_COMMITTER_EMAIL="teaprompt-test@example.com",
        GIT_CONFIG_COUNT="1",
        GIT_CONFIG_KEY_0="commit.gpgsign",
        GIT_CONFIG_VALUE_0="false",
    )
    return env


def _git(repo: Path, *args: str) -> "subprocess.CompletedProcess":
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        env=_git_env(),
        check=False,
    )


def _pinned_repo(tmp_path: Path) -> Path:
    if shutil.which("git") is None:
        pytest.skip("git not available")
    repo = tmp_path / "repo"
    repo.mkdir()
    result = _git(repo, "init", "-b", "main")
    assert result.returncode == 0, result.stderr
    return repo


def _commit_skills(repo: Path) -> str:
    result = _git(repo, "add", "reflective-prompt-library")
    assert result.returncode == 0, result.stderr
    result = _git(repo, "commit", "-m", "add skills")
    assert result.returncode == 0, result.stderr
    head = _git(repo, "rev-parse", "HEAD")
    assert head.returncode == 0, head.stderr
    return head.stdout.strip()


def _pinned_script_text(
    installation_guide_text: str, args, errexit: bool = False
) -> str:
    quoted = " ".join(shlex.quote(str(arg)) for arg in args)
    mode = "set -e" if errexit else "set +e"
    return (
        "#!/bin/sh\n"
        + mode
        + "\n"
        + _extract_pinned_helper(installation_guide_text)
        + "\n}\ninstall_skills_pinned "
        + quoted
        + "\n"
    )


def _run_pinned_helper(
    tmp_path: Path,
    repo: Path,
    args,
    installation_guide_text: str,
    errexit: bool = False,
) -> "subprocess.CompletedProcess":
    script = tmp_path / "install_skills_pinned.sh"
    script.write_text(
        _pinned_script_text(installation_guide_text, args, errexit),
        encoding="utf-8",
    )
    return subprocess.run(
        ["sh", str(script)], cwd=repo, capture_output=True, text=True, check=False
    )


@pytest.mark.skipif(shutil.which("sh") is None, reason="POSIX sh not available")
@pytest.mark.parametrize("errexit", (False, True))
def test_pinned_helper_unknown_entry_returns_nonzero_without_partial_entry(
    tmp_path: Path, installation_guide_text: str, errexit: bool
):
    """An unknown entry fails before anything is written, errexit or not."""
    repo = _pinned_repo(tmp_path)
    source_root = repo / "reflective-prompt-library" / "skills"
    _write_skill_source(source_root, "reflective-brief")
    _commit_skills(repo)
    dest = tmp_path / "dest"
    result = _run_pinned_helper(
        tmp_path,
        repo,
        (dest, "HEAD", "reflective-brief", "no-such-skill"),
        installation_guide_text,
        errexit=errexit,
    )
    assert result.returncode != 0, result.stdout + result.stderr
    assert "unknown" in (result.stdout + result.stderr)
    assert not dest.exists(), "a failed entry must leave no partial install"


@pytest.mark.skipif(shutil.which("sh") is None, reason="POSIX sh not available")
@pytest.mark.parametrize("kind", ("dir", "file"))
def test_pinned_helper_refuses_unpinned_real_path_and_preserves_bytes(
    tmp_path: Path, installation_guide_text: str, kind: str
):
    """An unpinned real file/directory is never overwritten."""
    repo = _pinned_repo(tmp_path)
    source_root = repo / "reflective-prompt-library" / "skills"
    _write_skill_source(source_root, "reflective-brief")
    _commit_skills(repo)
    dest = tmp_path / "dest"
    target = dest / "reflective-brief"
    if kind == "dir":
        target.mkdir(parents=True)
        (target / "SKILL.md").write_text("LOCAL-BYTES\n", encoding="utf-8")
    else:
        dest.mkdir(parents=True)
        target.write_text("LOCAL-BYTES\n", encoding="utf-8")
    result = _run_pinned_helper(
        tmp_path, repo, (dest, "HEAD", "reflective-brief"), installation_guide_text
    )
    assert result.returncode != 0, result.stdout + result.stderr
    assert "refusing" in (result.stdout + result.stderr)
    if kind == "dir":
        assert (target / "SKILL.md").read_text(encoding="utf-8") == "LOCAL-BYTES\n"
    else:
        assert target.read_text(encoding="utf-8") == "LOCAL-BYTES\n"
    assert not (dest / ".teaprompt-pins.tsv").exists()


@pytest.mark.skipif(shutil.which("sh") is None, reason="POSIX sh not available")
def test_pinned_helper_replaces_symlink_without_touching_target(
    tmp_path: Path, installation_guide_text: str
):
    """Replacing a symlink must not delete the directory it pointed at."""
    repo = _pinned_repo(tmp_path)
    source_root = repo / "reflective-prompt-library" / "skills"
    _write_skill_source(source_root, "reflective-brief")
    _commit_skills(repo)
    elsewhere = tmp_path / "elsewhere" / "reflective-brief"
    elsewhere.mkdir(parents=True)
    (elsewhere / "keep.md").write_text("KEEP-TARGET\n", encoding="utf-8")
    dest = tmp_path / "dest"
    dest.mkdir()
    (dest / "reflective-brief").symlink_to(elsewhere)
    result = _run_pinned_helper(
        tmp_path, repo, (dest, "HEAD", "reflective-brief"), installation_guide_text
    )
    assert result.returncode == 0, result.stdout + result.stderr
    installed = dest / "reflective-brief"
    assert installed.is_dir() and not installed.is_symlink()
    assert (installed / "SKILL.md").is_file()
    assert (elsewhere / "keep.md").read_text(encoding="utf-8") == "KEEP-TARGET\n"
    pins = (dest / ".teaprompt-pins.tsv").read_text(encoding="utf-8").splitlines()
    assert len(pins) == 1 and pins[0].split("\t")[0] == "reflective-brief"


@pytest.mark.skipif(shutil.which("sh") is None, reason="POSIX sh not available")
def test_pinned_helper_repins_keep_one_line_per_name(
    tmp_path: Path, installation_guide_text: str
):
    """Re-pinning updates the commit and keeps one manifest line per name."""
    repo = _pinned_repo(tmp_path)
    source_root = repo / "reflective-prompt-library" / "skills"
    _write_skill_source(source_root, "reflective-brief", "V1")
    examples = source_root / "examples"
    examples.mkdir(parents=True)
    (examples / "demo.md").write_text("demo\n", encoding="utf-8")
    first = _commit_skills(repo)
    dest = tmp_path / "dest"
    result = _run_pinned_helper(
        tmp_path,
        repo,
        (dest, "HEAD", "reflective-brief", "examples"),
        installation_guide_text,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    _write_skill_source(source_root, "reflective-brief", "V2")
    second = _commit_skills(repo)
    assert first != second
    result = _run_pinned_helper(
        tmp_path, repo, (dest, "HEAD", "reflective-brief"), installation_guide_text
    )
    assert result.returncode == 0, result.stdout + result.stderr
    pins = [
        line.split("\t")
        for line in (dest / ".teaprompt-pins.tsv").read_text(encoding="utf-8").splitlines()
        if line
    ]
    assert [row[0] for row in pins] == ["examples", "reflective-brief"]
    assert [row[1] for row in pins] == [first, second]
    assert "V2" in (dest / "reflective-brief" / "SKILL.md").read_text(encoding="utf-8")
