"""Guard the 2026-09-16 all-skills review: record shape and counts, the backlog
template repair (dry-run on the landed bytes), and the loop pack's budget.

Interpretive paragraphs are not pinned. The example, documentation, record, and
guard fixes the review landed are guarded where they live (their own tests were
re-pinned or strengthened in the same commit).
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "skills-september-concepts-review-2026-09-16.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
LINT_WARNING_CHARS = 20000
CANDIDATE_STATUS = {
    "H1": "Held 2026-09-16",
    "H2": "Held 2026-09-16",
    "H3": "Held 2026-09-16",
    "H4": "Held 2026-09-16",
    "H5": "Held 2026-09-16",
    "H6": "Held 2026-09-16",
    "H7": "Held 2026-09-16",
    "H8": "Held 2026-09-16",
    "H9": "No change 2026-09-16",
    "H10": "No change 2026-09-16",
    "H11": "No change 2026-09-16",
    "H12": "Held 2026-09-16",
}
BACKLOG_TEMPLATE = re.compile(
    r"## Template: Task-Ledger Backlog Loop \(bash, ralph-style\)\n.*?```bash\n(.*?)\n```\n", re.S
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def test_record_shape_and_dispositions():
    text = _read(RECORD)
    assert re.search(r"^> \*\*Status:.*AGREE WITH CHANGES.*6/6", "\n".join(text.splitlines()[:12]), re.M)
    for heading in (
        "Research Question", "Direct Answer", "Method", "Findings", "Coordinator Rig Results",
        "Landed Fixes", "Candidate Adoption Ledger", "Evidence vs Inference",
        "Evidence Actually Checked", "Falsifiability", "Completion Ledger",
    ):
        assert f"## {heading}" in text, heading
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split("\n## ", 1)[0]
    rows = [
        [cell.strip() for cell in line.split("|")[1:-1]]
        for line in ledger.splitlines() if re.match(r"^\| H\d+ \|", line)
    ]
    assert {row[0] for row in rows} == set(CANDIDATE_STATUS)
    for row in rows:
        assert len(row) == 5, row
        assert row[2] == CANDIDATE_STATUS[row[0]], row
        assert row[3] and row[4], row[0]
    findings = text.split("## Findings", 1)[1].split("\n## ", 1)[0]
    assert "| C1 |" in findings and "Fixed (F1)" in findings
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert f"[record](plans/{RECORD.name})" in knowledge


def test_loop_pack_stays_under_budget_after_the_backlog_repair():
    assert len(_read(library_skills_dir() / "flow-loop-harness" / "SKILL.md")) <= LINT_WARNING_CHARS


def _run_backlog(tmp_path: Path, script: str, *, agent_body: str, git: bool, verify_ec: int = 0, max_iter: str = "20") -> tuple[int, str]:
    d = tmp_path / ("git" if git else "plain")
    (d / "checks").mkdir(parents=True)
    (d / "TASKS.md").write_text("task one\ntask two\ntask three\n", encoding="utf-8")
    verify = d / "checks" / "verify.sh"
    verify.write_text(f"#!/bin/sh\nexit {verify_ec}\n", encoding="utf-8")
    verify.chmod(0o755)
    if git:
        g = ["git", "-c", "user.email=t@x", "-c", "user.name=t"]
        subprocess.run(g + ["init", "-q"], cwd=d, check=True)
        subprocess.run(g + ["add", "."], cwd=d, check=True)
        subprocess.run(g + ["commit", "-qm", "init"], cwd=d, check=True)
    stub = tmp_path / "stub.sh"
    stub.write_text("#!/bin/sh\n" + agent_body, encoding="utf-8")
    stub.chmod(0o755)
    (tmp_path / "loop.sh").write_text(script, encoding="utf-8")
    env = dict(os.environ, AGENT_CMD=str(stub), STATE="./state", MAX_ITER=max_iter)
    r = subprocess.run(["bash", str(tmp_path / "loop.sh")], cwd=d, env=env, capture_output=True, text=True, timeout=120)
    ledger = d / "state" / "ledger.md"
    return r.returncode, ledger.read_text(encoding="utf-8") if ledger.is_file() else ""


@pytest.mark.skipif(shutil.which("git") is None or shutil.which("bash") is None, reason="git/bash not available")
def test_backlog_template_never_retires_untouched_work(tmp_path: Path):
    """2026-09-16 review, C1: with a globally green verifier the backlog loop retired
    every task for a no-op agent and for a crashing agent (exit 0, "backlog empty").
    A task is retired only when the verifier passes AND the workspace changed; the
    check is skipped outside git, where there is no change signal."""
    script = BACKLOG_TEMPLATE.search(_read(library_skills_dir() / "flow-loop-harness" / "SKILL.md")).group(1) + "\n"
    cases = {
        "noop": ('echo "stub: done"\n', 3, "no change: task one"),
        "crash": ("echo boom >&2; exit 1\n", 3, "no change: task one"),
        "state-only": ('touch "state/junk-$$"\n', 3, "no change: task one"),
        "real-work": ('touch "work-$$-$(date +%s%N)"\n', 0, "- done: task three"),
    }
    for name, (body, want_exit, want_ledger) in cases.items():
        code, ledger = _run_backlog(tmp_path / name, script, agent_body=body, git=True)
        assert code == want_exit, (name, code, ledger)
        assert want_ledger in ledger, (name, ledger)
    code, ledger = _run_backlog(tmp_path / "cap", script, agent_body='touch "w-$$-$(date +%s%N)"\n', git=True, max_iter="2")
    assert code == 2 and "cap 2 exhausted" in ledger, ledger
    code, ledger = _run_backlog(tmp_path / "red", script, agent_body='echo x\n', git=True, verify_ec=1)
    assert code == 3 and "preflight" in ledger, ledger
    # Outside git there is no change signal: the check is skipped, not failed.
    code, _ = _run_backlog(tmp_path / "nogit", script, agent_body='echo "stub: done"\n', git=False)
    assert code == 0
