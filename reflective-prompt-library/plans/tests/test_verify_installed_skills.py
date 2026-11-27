"""Behavioral checks for plans/verify_installed_skills.py + install_skills_pinned.

The ``install_skills_pinned`` helper is extracted from SKILL_INSTALLATION.md
(the single maintained implementation) and executed inside a temporary git
repository. The verifier script is copied into that repository and run as a
subprocess against temporary install roots. No host directories are touched:
default roots are only exercised through ``default_roots`` with a tmp home.
"""

import importlib.util
import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import pytest

INSTALLATION_GUIDE = Path(__file__).resolve().parent.parent.parent / "SKILL_INSTALLATION.md"
VERIFIER_SOURCE = Path(__file__).resolve().parent.parent / "verify_installed_skills.py"
SKILLS_PREFIX = "reflective-prompt-library/skills"
PINS_NAME = ".teaprompt-pins.tsv"


@pytest.fixture(scope="module")
def installation_guide_text() -> str:
    assert INSTALLATION_GUIDE.is_file(), f"missing {INSTALLATION_GUIDE}"
    return INSTALLATION_GUIDE.read_text(encoding="utf-8")


def _extract_helper(guide: str, helper: str) -> str:
    start = guide.index(f"{helper}() {{")
    end = guide.index("\n}\n", start)
    return guide[start:end]


def _git_env() -> Dict[str, str]:
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


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        env=_git_env(),
        check=False,
    )


def _git_show(repo: Path, rev: str, path: str) -> bytes:
    proc = subprocess.run(
        ["git", "-C", str(repo), "show", f"{rev}:{path}"],
        capture_output=True,
        env=_git_env(),
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    return proc.stdout


def _make_repo(tmp_path: Path) -> Path:
    if shutil.which("git") is None:
        pytest.skip("git not available")
    repo = tmp_path / "repo"
    repo.mkdir()
    result = _git(repo, "init", "-b", "main")
    assert result.returncode == 0, result.stderr
    verifier = repo / "plans" / VERIFIER_SOURCE.name
    verifier.parent.mkdir(parents=True)
    shutil.copyfile(VERIFIER_SOURCE, verifier)
    return repo


def _write_skill(repo: Path, name: str, marker: str = "SOURCE-MARKER") -> Path:
    skill = repo / SKILLS_PREFIX / name
    (skill / "notes").mkdir(parents=True, exist_ok=True)
    (skill / "SKILL.md").write_text(f"# {name}\n{marker}\n", encoding="utf-8")
    (skill / "notes" / "extra.md").write_text(f"extra {marker}\n", encoding="utf-8")
    return skill


def _commit_skills(repo: Path, message: str = "add skills") -> str:
    result = _git(repo, "add", "reflective-prompt-library")
    assert result.returncode == 0, result.stderr
    result = _git(repo, "commit", "-m", message)
    assert result.returncode == 0, result.stderr
    head = _git(repo, "rev-parse", "HEAD")
    assert head.returncode == 0, head.stderr
    return head.stdout.strip()


def _run_pinned(
    repo: Path,
    tmp_path: Path,
    guide: str,
    dest: Path,
    rev: str,
    *entries: str,
) -> subprocess.CompletedProcess:
    if shutil.which("sh") is None:
        pytest.skip("POSIX sh not available")
    body = _extract_helper(guide, "install_skills_pinned")
    quoted = " ".join(shlex.quote(str(arg)) for arg in (dest, rev, *entries))
    script = tmp_path / "install_skills_pinned.sh"
    script.write_text(
        "#!/bin/sh\nset +e\n" + body + "\n}\ninstall_skills_pinned " + quoted + "\n",
        encoding="utf-8",
    )
    return subprocess.run(
        ["sh", str(script)], cwd=repo, capture_output=True, text=True, check=False
    )


def _run_verify(repo: Path, root: Path, *extra: str) -> subprocess.CompletedProcess:
    script = repo / "plans" / VERIFIER_SOURCE.name
    return subprocess.run(
        [sys.executable, str(script), "--root", str(root), *extra],
        capture_output=True,
        text=True,
        check=False,
    )


def _pins(dest: Path) -> List[List[str]]:
    manifest = dest / PINS_NAME
    assert manifest.is_file(), f"missing {manifest}"
    return [
        line.split("\t")
        for line in manifest.read_text(encoding="utf-8").splitlines()
        if line
    ]


def _snapshot(root: Path) -> Dict[str, bytes]:
    snap: Dict[str, bytes] = {}
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root).as_posix()
        if path.is_symlink():
            snap[rel] = b"LINK:" + os.readlink(path).encode()
        elif path.is_file():
            snap[rel] = path.read_bytes()
    return snap


def test_pinned_install_passes_and_installs_committed_bytes(
    tmp_path: Path, installation_guide_text: str
):
    repo = _make_repo(tmp_path)
    _write_skill(repo, "reflective-brief", "PIN-ONE")
    sha = _commit_skills(repo)
    # A dirty worktree must never leak into a pinned install.
    (repo / SKILLS_PREFIX / "reflective-brief" / "SKILL.md").write_text(
        "WORKTREE-DIRTY\n", encoding="utf-8"
    )
    dest = tmp_path / "dest"
    result = _run_pinned(
        repo, tmp_path, installation_guide_text, dest, "HEAD", "reflective-brief"
    )
    assert result.returncode == 0, result.stdout + result.stderr
    installed = dest / "reflective-brief"
    assert installed.is_dir() and not installed.is_symlink()
    committed = _git_show(repo, sha, f"{SKILLS_PREFIX}/reflective-brief/SKILL.md")
    assert (installed / "SKILL.md").read_bytes() == committed
    assert (installed / "notes" / "extra.md").read_bytes() == _git_show(
        repo, sha, f"{SKILLS_PREFIX}/reflective-brief/notes/extra.md"
    )
    assert _pins(dest) == [
        ["reflective-brief", sha, f"{SKILLS_PREFIX}/reflective-brief"]
    ]
    result = _run_verify(repo, dest)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "OK pinned reflective-brief" in result.stdout
    assert not any(line.startswith("FAIL ") for line in result.stdout.splitlines())
    # The verifier is read-only: pinned bytes and the manifest are untouched.
    assert (installed / "SKILL.md").read_bytes() == committed
    assert _pins(dest) == [
        ["reflective-brief", sha, f"{SKILLS_PREFIX}/reflective-brief"]
    ]


def test_pinned_entry_tamper_fails_even_with_allow_stale(
    tmp_path: Path, installation_guide_text: str
):
    repo = _make_repo(tmp_path)
    _write_skill(repo, "reflective-brief")
    _commit_skills(repo)
    dest = tmp_path / "dest"
    assert (
        _run_pinned(
            repo, tmp_path, installation_guide_text, dest, "HEAD", "reflective-brief"
        ).returncode
        == 0
    )
    (dest / "reflective-brief" / "SKILL.md").write_text("TAMPERED\n", encoding="utf-8")
    result = _run_verify(repo, dest, "--allow-stale")
    assert result.returncode != 0, result.stdout
    assert "FAIL tamper reflective-brief" in result.stdout
    # An added file is tamper too.
    (dest / "reflective-brief" / "SKILL.md").write_bytes(
        _git_show(repo, "HEAD", f"{SKILLS_PREFIX}/reflective-brief/SKILL.md")
    )
    (dest / "reflective-brief" / "intruder.md").write_text("x\n", encoding="utf-8")
    result = _run_verify(repo, dest)
    assert result.returncode != 0, result.stdout
    assert "FAIL tamper reflective-brief" in result.stdout
    assert "added" in result.stdout


def test_pinned_entry_becomes_stale_after_new_commit(
    tmp_path: Path, installation_guide_text: str
):
    repo = _make_repo(tmp_path)
    _write_skill(repo, "reflective-brief", "V1")
    _commit_skills(repo, "v1")
    dest = tmp_path / "dest"
    assert (
        _run_pinned(
            repo, tmp_path, installation_guide_text, dest, "HEAD", "reflective-brief"
        ).returncode
        == 0
    )
    assert _run_verify(repo, dest).returncode == 0
    _write_skill(repo, "reflective-brief", "V2")
    _commit_skills(repo, "v2")
    result = _run_verify(repo, dest)
    assert result.returncode != 0, result.stdout
    assert "FAIL stale reflective-brief" in result.stdout
    result = _run_verify(repo, dest, "--allow-stale")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "stale" in result.stdout


def test_live_symlink_flagged_unless_allowed_and_clean(
    tmp_path: Path, installation_guide_text: str
):
    repo = _make_repo(tmp_path)
    _write_skill(repo, "reflective-brief")
    _commit_skills(repo)
    dest = tmp_path / "dest"
    dest.mkdir()
    (dest / "reflective-brief").symlink_to(repo / SKILLS_PREFIX / "reflective-brief")
    result = _run_verify(repo, dest)
    assert result.returncode != 0, result.stdout
    assert "FAIL live reflective-brief" in result.stdout
    result = _run_verify(repo, dest, "--allow-live")
    assert result.returncode == 0, result.stdout + result.stderr
    # Uncommitted changes under the target path still fail with the flag.
    (repo / SKILLS_PREFIX / "reflective-brief" / "SKILL.md").write_text(
        "DIRTY\n", encoding="utf-8"
    )
    result = _run_verify(repo, dest, "--allow-live")
    assert result.returncode != 0, result.stdout
    assert "FAIL dirty reflective-brief" in result.stdout


def test_dangling_teaprompt_link_fails_foreign_dangling_ignored(
    tmp_path: Path, installation_guide_text: str
):
    repo = _make_repo(tmp_path)
    _write_skill(repo, "reflective-brief")
    _commit_skills(repo)
    dest = tmp_path / "dest"
    dest.mkdir()
    (dest / "ghost").symlink_to(repo / SKILLS_PREFIX / "ghost-skill")
    (dest / "foreign-broken").symlink_to(tmp_path / "no-such-dir")
    result = _run_verify(repo, dest, "--allow-live")
    assert result.returncode != 0, result.stdout
    assert "FAIL dangling ghost" in result.stdout
    assert "foreign-broken" not in result.stdout


def test_non_teaprompt_entries_are_ignored(
    tmp_path: Path, installation_guide_text: str
):
    repo = _make_repo(tmp_path)
    _write_skill(repo, "reflective-brief")
    _commit_skills(repo)
    dest = tmp_path / "dest"
    other = dest / "other-tool-skill"
    other.mkdir(parents=True)
    (other / "SKILL.md").write_text("# not ours\n", encoding="utf-8")
    before = _snapshot(dest)
    result = _run_verify(repo, dest)
    assert result.returncode == 0, result.stdout + result.stderr
    assert _snapshot(dest) == before


def test_file_entry_pins_and_verifies(
    tmp_path: Path, installation_guide_text: str
):
    repo = _make_repo(tmp_path)
    cheat = repo / SKILLS_PREFIX / "SKILL_TRIGGER_CHEATSHEET.md"
    cheat.parent.mkdir(parents=True, exist_ok=True)
    cheat.write_text("CHEATSHEET-V1\n", encoding="utf-8")
    sha = _commit_skills(repo)
    dest = tmp_path / "dest"
    result = _run_pinned(
        repo, tmp_path, installation_guide_text, dest, sha, "SKILL_TRIGGER_CHEATSHEET.md"
    )
    assert result.returncode == 0, result.stdout + result.stderr
    installed = dest / "SKILL_TRIGGER_CHEATSHEET.md"
    assert installed.is_file() and not installed.is_symlink()
    assert installed.read_bytes() == b"CHEATSHEET-V1\n"
    assert _pins(dest) == [
        [
            "SKILL_TRIGGER_CHEATSHEET.md",
            sha,
            f"{SKILLS_PREFIX}/SKILL_TRIGGER_CHEATSHEET.md",
        ]
    ]
    result = _run_verify(repo, dest)
    assert result.returncode == 0, result.stdout + result.stderr
    installed.write_text("EDITED\n", encoding="utf-8")
    result = _run_verify(repo, dest)
    assert result.returncode != 0, result.stdout
    assert "FAIL tamper SKILL_TRIGGER_CHEATSHEET.md" in result.stdout


def test_symlink_chains_follow_live_and_pinned_targets(
    tmp_path: Path, installation_guide_text: str
):
    repo = _make_repo(tmp_path)
    _write_skill(repo, "reflective-brief")
    _commit_skills(repo)
    # A chain that ends inside the checkout is still a live link.
    live_root = tmp_path / "live-root"
    inner = live_root / "inner"
    inner.mkdir(parents=True)
    (inner / "reflective-brief").symlink_to(
        repo / SKILLS_PREFIX / "reflective-brief"
    )
    (live_root / "reflective-brief").symlink_to(inner / "reflective-brief")
    result = _run_verify(repo, live_root)
    assert result.returncode != 0, result.stdout
    assert "FAIL live reflective-brief" in result.stdout
    assert _run_verify(repo, live_root, "--allow-live").returncode == 0
    # A chain that ends at a pinned entry verifies the pinned bytes.
    pinned_root = tmp_path / "pinned-root"
    assert (
        _run_pinned(
            repo,
            tmp_path,
            installation_guide_text,
            pinned_root,
            "HEAD",
            "reflective-brief",
        ).returncode
        == 0
    )
    alias_root = tmp_path / "alias-root"
    alias_root.mkdir()
    (alias_root / "alias-brief").symlink_to(pinned_root / "reflective-brief")
    result = _run_verify(repo, alias_root)
    assert result.returncode == 0, result.stdout + result.stderr
    (pinned_root / "reflective-brief" / "SKILL.md").write_text(
        "TAMPERED\n", encoding="utf-8"
    )
    result = _run_verify(repo, alias_root)
    assert result.returncode != 0, result.stdout
    assert "FAIL tamper alias-brief" in result.stdout


def test_default_roots_cover_existing_dirs_only(tmp_path: Path):
    spec = importlib.util.spec_from_file_location(
        "verify_installed_skills", VERIFIER_SOURCE
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    home = tmp_path / "home"
    (home / ".claude" / "skills").mkdir(parents=True)
    (home / ".grok" / "skills").mkdir(parents=True)
    roots = module.default_roots(home)
    existing = [path for path in roots if path.is_dir()]
    assert len(roots) == 7
    assert set(existing) == {
        home / ".claude" / "skills",
        home / ".grok" / "skills",
    }
