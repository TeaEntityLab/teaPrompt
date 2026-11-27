#!/usr/bin/env python3
"""Verify installed TeaPrompt skills against their recorded pin or the live checkout.

Read-only. For each install root, inspects only TeaPrompt entries:

* live symlinks resolving into this repository's ``reflective-prompt-library/skills``
  directory FAIL unless ``--allow-live``; with the flag they still FAIL when
  dangling or when the target path differs from ``HEAD``.
* dangling TeaPrompt links FAIL.
* pinned entries (names recorded in ``<root>/.teaprompt-pins.tsv``) are
  byte-compared against the recorded commit; added, missing, or modified
  files are FAIL (tamper). The recorded commit's tree for the path is then
  compared with ``HEAD``'s; a difference FAILs as stale unless
  ``--allow-stale``.
* entries that are not TeaPrompt's are ignored.

Exit status is nonzero on any FAIL. Requires Python 3.9+, ``git``. Writes nothing.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

PINS_FILENAME = ".teaprompt-pins.tsv"
SKILLS_PREFIX = "reflective-prompt-library/skills"

DEFAULT_ROOTS = (
    (".agents", "skills"),
    (".cursor", "skills"),
    (".claude", "skills"),
    (".codex", "skills"),
    (".gemini", "antigravity", "skills"),
    (".gemini", "skills"),
    (".grok", "skills"),
)

# (status, kind, name, detail); status is "FAIL" or "OK".
Finding = Tuple[str, str, str, str]
# git path -> (mode, type, oid), as reported by ``git ls-tree -r``.
GitMeta = Tuple[str, str, str]


class VerifyError(Exception):
    """Expected verification failure (git error, malformed manifest)."""


# --- git plumbing ---------------------------------------------------------


def run_git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env["GIT_OPTIONAL_LOCKS"] = "0"  # keep the verifier strictly read-only
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        check=False,
        env=env,
    )
    if check and proc.returncode != 0:
        detail = proc.stderr.decode("utf-8", "replace").strip() or proc.stdout.decode(
            "utf-8", "replace"
        ).strip()
        raise VerifyError(f"git {' '.join(args)} failed: {detail}")
    return proc


def repo_root(script_dir: Path) -> Path:
    proc = run_git(script_dir, "rev-parse", "--show-toplevel", check=False)
    if proc.returncode != 0:
        raise VerifyError(
            "verify_installed_skills.py must live inside the TeaPrompt git "
            "repository (reflective-prompt-library/plans/)"
        )
    return Path(proc.stdout.decode("utf-8", "replace").strip()).resolve()


def parse_ls_tree(data: bytes) -> Dict[str, GitMeta]:
    entries: Dict[str, GitMeta] = {}
    for record in data.split(b"\x00"):
        if not record:
            continue
        meta, _, raw_path = record.partition(b"\t")
        mode, _, rest = meta.decode("ascii", "replace").partition(" ")
        typ, _, oid = rest.partition(" ")
        entries[raw_path.decode("utf-8", "surrogateescape")] = (mode, typ, oid)
    return entries


def git_files(repo: Path, rev: str, source: str) -> Optional[Dict[str, GitMeta]]:
    """Map files under ``rev:source`` keyed by path relative to ``source``.

    A file entry maps to a single ``"."`` key. Returns None when the object
    does not exist at that revision.
    """
    proc = run_git(
        repo, "ls-tree", "-r", "-z", rev, "--", f":(literal){source}", check=False
    )
    if proc.returncode != 0:
        return None
    entries = parse_ls_tree(proc.stdout)
    if not entries:
        return None
    if len(entries) == 1 and next(iter(entries)) == source:
        return {".": entries[source]}
    prefix = source + "/"
    result: Dict[str, GitMeta] = {}
    for path, meta in entries.items():
        if path == source or path.startswith(prefix):
            result[path[len(prefix):] if path.startswith(prefix) else "."] = meta
    return result


def tree_signature(repo: Path, rev: str, source: str) -> Optional[bytes]:
    proc = run_git(
        repo, "ls-tree", "-r", "-z", rev, "--", f":(literal){source}", check=False
    )
    if proc.returncode != 0 or not proc.stdout:
        return None
    return proc.stdout


def cat_blob(repo: Path, oid: str) -> bytes:
    return run_git(repo, "cat-file", "blob", oid).stdout


def is_ignored(repo: Path, rel: str) -> bool:
    proc = run_git(repo, "check-ignore", "-q", "--", rel, check=False)
    return proc.returncode == 0


# --- manifest -------------------------------------------------------------


def load_pins(manifest: Path) -> Dict[str, Tuple[str, str]]:
    pins: Dict[str, Tuple[str, str]] = {}
    try:
        text = manifest.read_text(encoding="utf-8")
    except OSError as exc:
        raise VerifyError(f"cannot read {manifest.name}: {exc}") from exc
    except UnicodeDecodeError as exc:
        raise VerifyError(f"{manifest.name} is not UTF-8 text") from exc
    for lineno, raw in enumerate(text.split("\n"), 1):
        line = raw.rstrip("\r")
        if not line:
            continue
        fields = line.split("\t")
        if len(fields) != 3:
            raise VerifyError(f"{manifest.name}:{lineno}: expected name<TAB>commit<TAB>source")
        name, commit, source = fields
        if not safe_name(name):
            raise VerifyError(f"{manifest.name}:{lineno}: unsafe entry name {name!r}")
        if not safe_commit(commit):
            raise VerifyError(f"{manifest.name}:{lineno}: unsafe commit {commit!r}")
        if not safe_source(source):
            raise VerifyError(f"{manifest.name}:{lineno}: unsafe source path {source!r}")
        if name in pins:
            raise VerifyError(f"{manifest.name}:{lineno}: duplicate entry {name!r}")
        pins[name] = (commit.lower(), source)
    return pins


def pins_of(directory: Path) -> Dict[str, Tuple[str, str]]:
    manifest = directory / PINS_FILENAME
    if manifest.is_symlink() and not manifest.exists():
        raise VerifyError(f"{manifest.name} is a broken symlink")
    if not manifest.exists():
        return {}
    if not manifest.is_file():
        raise VerifyError(f"{manifest.name} is not a regular file")
    return load_pins(manifest)


def safe_name(name: str) -> bool:
    return bool(name) and "/" not in name and name not in (".", "..")


def safe_commit(commit: str) -> bool:
    if len(commit) not in (40, 64):
        return False
    return all(c in "0123456789abcdefABCDEF" for c in commit)


def safe_source(source: str) -> bool:
    if not source or source.startswith(("/", "~")):
        return False
    return all(part not in ("", ".", "..") for part in source.split("/"))

def entry_path(root: Path, name: str) -> Optional[Path]:
    if not safe_name(name):
        return None
    path = root / name
    try:
        Path(os.path.normpath(path)).relative_to(os.path.normpath(root))
    except ValueError:
        return None
    return path


def pin_targeting(repo: Path, resolved: Path) -> Optional[Tuple[str, str]]:
    """Pin for a symlink's final target: <parent>/.teaprompt-pins.tsv[basename]."""
    try:
        return pins_of(resolved.parent).get(resolved.name)
    except VerifyError as exc:
        raise VerifyError(f"pin lookup for {resolved}: {exc}") from exc


# --- filesystem comparison ------------------------------------------------


def kind_of(mode: str) -> str:
    if mode == "120000":
        return "symlink"
    if mode.startswith("100"):
        return "file"
    return "other"


def disk_map(entry: Path) -> Dict[str, Tuple[str, Path]]:
    if entry.is_symlink() or entry.is_file():
        return {".": ("symlink" if entry.is_symlink() else "file", entry)}
    result: Dict[str, Tuple[str, Path]] = {}
    for dirpath, dirnames, filenames in os.walk(entry, followlinks=False):
        base = Path(dirpath)
        pruned = []
        for dirname in dirnames:
            candidate = base / dirname
            if candidate.is_symlink():
                rel = candidate.relative_to(entry).as_posix()
                result[rel] = ("symlink", candidate)
            else:
                pruned.append(dirname)
        dirnames[:] = pruned
        for filename in filenames:
            path = base / filename
            rel = path.relative_to(entry).as_posix()
            result[rel] = ("symlink" if path.is_symlink() else "file", path)
    return result


def same_content(repo: Path, oid: str, disk_path: Path, disk_kind: str) -> bool:
    try:
        blob = cat_blob(repo, oid)
        if disk_kind == "symlink":
            return os.fsencode(os.readlink(disk_path)) == blob
        return disk_path.read_bytes() == blob
    except (OSError, VerifyError):
        return False


def mismatch_detail(
    repo: Path,
    gfiles: Dict[str, GitMeta],
    disk: Dict[str, Tuple[str, Path]],
    check_exec: bool = False,
) -> Optional[str]:
    """Describe the first content/kind difference between git and disk maps."""
    missing = sorted(rel for rel in gfiles if rel not in disk)
    if missing:
        return "missing " + ", ".join(missing[:3])
    added = sorted(rel for rel in disk if rel not in gfiles)
    if added:
        return "added " + ", ".join(added[:3])
    changed = []
    for rel in sorted(gfiles):
        mode, typ, oid = gfiles[rel]
        if typ != "blob":
            return f"unsupported object type {typ} at {rel}"
        gkind = kind_of(mode)
        dkind, disk_path = disk[rel]
        if gkind != dkind:
            changed.append(rel)
            continue
        if not same_content(repo, oid, disk_path, dkind):
            changed.append(rel)
            continue
        if check_exec and gkind == "file":
            git_exec = mode == "100755"
            disk_exec = bool(disk_path.stat().st_mode & 0o111)
            if git_exec != disk_exec:
                changed.append(rel + " (mode)")
    if changed:
        label = "modified content" if changed == ["."] else "modified " + ", ".join(
            changed[:3]
        )
        return label
    return None


def worktree_dirty(repo: Path, resolved: Path, rel: str) -> bool:
    gfiles = git_files(repo, "HEAD", rel)
    if gfiles is None:
        return True  # path absent at HEAD but present on disk: uncommitted
    disk = disk_map(resolved)
    missing = any(rel_key not in disk for rel_key in gfiles)
    if missing:
        return True
    extras = [
        rel_key
        for rel_key in disk
        if rel_key not in gfiles
        and not is_ignored(repo, disk[rel_key][1].relative_to(repo).as_posix())
    ]
    if extras:
        return True
    overlapping = {rel: gfiles[rel] for rel in gfiles if rel in disk}
    trimmed = {rel: disk[rel] for rel in overlapping}
    return mismatch_detail(repo, overlapping, trimmed, check_exec=True) is not None


# --- symlink chains -------------------------------------------------------


def lexical_is_under(path: Path, parent: Path) -> bool:
    try:
        Path(os.path.normpath(path)).relative_to(os.path.normpath(parent))
        return True
    except ValueError:
        return False


def walk_chain(entry: Path, skills_dir: Path) -> Tuple[str, Path, bool]:
    """Follow symlinks without requiring existence.

    Returns (status, final_path, under_skills): status is "resolved",
    "dangling", or "loop"; under_skills means the final path — or the first
    dangling target — lies under the skills directory.
    """
    path = Path(os.path.normpath(os.path.abspath(entry)))
    seen = {str(path)}
    for _ in range(32):
        if not path.is_symlink():
            status = "resolved" if path.exists() else "dangling"
            return status, path, lexical_is_under(path, skills_dir)
        try:
            raw = os.readlink(path)
        except OSError:
            return "dangling", path, lexical_is_under(path, skills_dir)
        target = Path(raw)
        if not target.is_absolute():
            target = Path(os.path.normpath(path.parent / target))
        if str(target) in seen:
            return "loop", target, lexical_is_under(target, skills_dir)
        seen.add(str(target))
        path = target
    return "loop", path, lexical_is_under(path, skills_dir)


# --- classification -------------------------------------------------------


def judge_pinned(
    repo: Path, resolved: Path, name: str, commit: str, source: str, allow_stale: bool
) -> Finding:
    gfiles = git_files(repo, commit, source)
    if gfiles is None:
        return (
            "FAIL",
            "tamper",
            name,
            f"pin commit/path missing in repository ({commit[:12]}:{source})",
        )
    try:
        detail = mismatch_detail(repo, gfiles, disk_map(resolved))
    except VerifyError as exc:
        detail = str(exc)
    if detail is not None:
        return "FAIL", "tamper", name, detail
    recorded = tree_signature(repo, commit, source)
    head = tree_signature(repo, "HEAD", source)
    if recorded is None:
        return "FAIL", "tamper", name, "pin source missing at recorded commit"
    if recorded != head:
        if allow_stale:
            return "OK", "pinned", name, "stale (allowed)"
        return "FAIL", "stale", name, "entry differs at HEAD"
    return "OK", "pinned", name, ""


def judge_live(repo: Path, resolved: Path, name: str, allow_live: bool) -> Finding:
    if not allow_live:
        return "FAIL", "live", name, "live symlink into the repository checkout"
    try:
        rel = resolved.relative_to(repo).as_posix()
    except ValueError:
        return "FAIL", "dirty", name, "live target outside the repository"
    if worktree_dirty(repo, resolved, rel):
        return "FAIL", "dirty", name, "uncommitted changes under the target path"
    return "OK", "live", name, ""


def inspect_one(
    root: Path,
    repo: Path,
    skills_dir: Path,
    name: str,
    pins: Dict[str, Tuple[str, str]],
    allow_live: bool,
    allow_stale: bool,
) -> Optional[Finding]:
    path = entry_path(root, name)
    if path is None:
        return ("FAIL", "manifest", name, "unsafe entry name") if name in pins else None
    local_pin = pins.get(name)
    if path.is_symlink():
        try:
            status, resolved, under = walk_chain(path, skills_dir)
        except OSError as exc:
            return "FAIL", "dangling", name, f"cannot read link: {exc}"
        if status != "resolved":
            if under or local_pin is not None:
                return "FAIL", "dangling", name, "unresolvable link"
            try:
                foreign_pin = pin_targeting(repo, resolved)
            except VerifyError:
                foreign_pin = None
            if foreign_pin is not None:
                return "FAIL", "dangling", name, "unresolvable link"
            return None  # a foreign broken link is not ours
        if lexical_is_under(resolved, skills_dir):
            return judge_live(repo, resolved, name, allow_live)
        try:
            foreign_pin = pin_targeting(repo, resolved)
        except VerifyError as exc:
            return "FAIL", "manifest", name, str(exc)
        if foreign_pin is not None:
            commit, source = foreign_pin
            return judge_pinned(repo, resolved, name, commit, source, allow_stale)
        if local_pin is not None:
            return (
                "FAIL",
                "tamper",
                name,
                "pinned name is a symlink outside the repository and pins",
            )
        return None
    if not path.exists():
        if local_pin is not None:
            return "FAIL", "tamper", name, "entry missing"
        return None
    if local_pin is None:
        return None
    commit, source = local_pin
    return judge_pinned(repo, path, name, commit, source, allow_stale)


def check_root(
    root: Path,
    repo: Path,
    skills_dir: Path,
    allow_live: bool,
    allow_stale: bool,
) -> Tuple[List[Finding], int]:
    """Return (findings, ignored_count) for one install root."""
    if root.is_symlink() or not root.is_dir():
        return [("FAIL", "root", str(root), "not a directory")], 0
    try:
        pins = pins_of(root)
    except VerifyError as exc:
        return [("FAIL", "manifest", PINS_FILENAME, str(exc))], 0
    names = set()
    try:
        for child in root.iterdir():
            if child.name != PINS_FILENAME:
                names.add(child.name)
    except OSError as exc:
        return [("FAIL", "root", str(root), f"cannot list: {exc}")], 0
    names.update(pins)
    findings: List[Finding] = []
    ignored = 0
    for name in sorted(names):
        try:
            finding = inspect_one(
                root, repo, skills_dir, name, pins, allow_live, allow_stale
            )
        except VerifyError as exc:
            finding = ("FAIL", "error", name, str(exc))
        if finding is None:
            ignored += 1
        else:
            findings.append(finding)
    return findings, ignored


# --- reporting / CLI ------------------------------------------------------


def default_roots(home: Path) -> List[Path]:
    return [home.joinpath(*parts) for parts in DEFAULT_ROOTS]


def emit(root: Path, findings: List[Finding], ignored: int) -> int:
    fails = 0
    oks = 0
    for status, kind, name, detail in findings:
        line = f"{status} {kind} {name}"
        if detail:
            line += f": {detail}"
        print(line)
        if status == "FAIL":
            fails += 1
        else:
            oks += 1
    print(f"SUMMARY {root}: FAIL {fails}, OK {oks}, ignored {ignored}")
    return fails


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Verify installed TeaPrompt skills: live symlinks into this "
            "checkout and entries pinned via .teaprompt-pins.tsv. Read-only."
        )
    )
    parser.add_argument(
        "--root",
        action="append",
        nargs="+",
        metavar="DIR",
        help=(
            "install root(s) to check; repeatable. Default: every existing "
            "directory among ~/.agents/skills, ~/.cursor/skills, "
            "~/.claude/skills, ~/.codex/skills, ~/.gemini/antigravity/skills, "
            "~/.gemini/skills, ~/.grok/skills."
        ),
    )
    parser.add_argument(
        "--allow-live",
        action="store_true",
        help=(
            "permit live symlinks into this checkout; they still fail when "
            "dangling or when the target path has uncommitted changes vs HEAD."
        ),
    )
    parser.add_argument(
        "--allow-stale",
        action="store_true",
        help=(
            "permit pinned entries whose recorded commit's tree for the "
            "entry path differs from HEAD's (stale pins)."
        ),
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        repo = repo_root(Path(__file__).resolve().parent)
    except VerifyError as exc:
        print(f"FAIL repo: {exc}", file=sys.stderr)
        return 2
    skills_dir = repo / SKILLS_PREFIX
    if args.root:
        roots = [Path(item) for group in args.root for item in group]
    else:
        home = Path(os.path.expanduser("~"))
        roots = [path for path in default_roots(home) if path.is_dir()]
    total_fails = 0
    if not roots:
        print("SUMMARY: no install roots found")
    for root in roots:
        findings, ignored = check_root(
            root, repo, skills_dir, args.allow_live, args.allow_stale
        )
        total_fails += emit(root, findings, ignored)
    return 1 if total_fails else 0


if __name__ == "__main__":
    sys.exit(main())
