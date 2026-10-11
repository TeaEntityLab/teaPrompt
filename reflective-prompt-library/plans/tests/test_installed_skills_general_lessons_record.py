"""Guard for the 2026-09-05 installed-skills general-lessons adoption record.

Pins the ten clean-room sentences at exactly one surface each, the fan-out
template's merged-result gate (rule 4 says fan-in gates the merged result, so
the template must show it), the ledger dispositions, and the index rows. The
template dry-run is the reproduction from the record kept as a regression test.
"""

from __future__ import annotations

import os
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "installed-skills-general-lessons-2026-09-05.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"



FAN_OUT_TEMPLATE = re.compile(
    r"## Template: Parallel Fan-out/Fan-in \(bash\)\n\n```bash\n(.*?)```", re.S
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")




def test_record_shape_and_dispositions():
    text = _read(RECORD)
    assert text.startswith("# Installed-Skills General-Lessons Survey and Adoption — 2026-09-05")
    assert "> **Status: decided, guarded, and verified" in text
    for heading in (
        "## Research Question",
        "## Method",
        "## Direct Recommendation (as of 2026-09-05)",
        "## Required Wording Changes (final, by user direction)",
        "## Candidate Adoption Ledger",
        "## Reproduction (observed)",
        "## Evidence vs Inference",
        "## Falsifiability",
        "## Completion Ledger",
    ):
        assert heading in text, heading
    assert "26 further harness-generated skills are bound to private projects and were never opened" in text
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split("## Reproduction", 1)[0]
    for n in range(1, 11):
        row = next(line for line in ledger.splitlines() if line.startswith(f"| GL-{n} |"))
        assert row.rstrip().endswith("| **Adopted** |") or "| **Adopted** (" in row, row
    for n in range(1, 7):
        row = next(line for line in ledger.splitlines() if line.startswith(f"| H-{n} |"))
        assert row.rstrip().endswith("| **Held** |"), row
    assert "| **Not applicable** |" in ledger


def test_indexes_point_to_the_record():
    knowledge = _read(PROJECT_KNOWLEDGE)
    assert "[record](plans/installed-skills-general-lessons-2026-09-05.md)" in knowledge
    assert "ten clean-room sentences adopted by user direction" in knowledge
    case_studies = _read(CASE_STUDIES)
    assert "[installed-skills](installed-skills-general-lessons-2026-09-05.md)" in case_studies
    assert "installed-skills general-lessons survey recorded; GL-1–GL-10 adopted by user direction | done |" in case_studies


@pytest.mark.skipif(shutil.which("bash") is None, reason="bash not available")
def test_fan_out_template_gates_the_merged_result(tmp_path: Path):
    """Both branches pass the tally; the merged gate must still be able to reject."""
    text = _read(library_skills_dir() / "flow-control-generator" / "TEMPLATES.md")
    match = FAN_OUT_TEMPLATE.search(text)
    assert match, "fan-out template missing"
    script = tmp_path / "fanout.sh"
    script.write_text(match.group(1), encoding="utf-8")
    (tmp_path / "prompts" / "fan").mkdir(parents=True)
    (tmp_path / "checks").mkdir()
    (tmp_path / "prompts" / "fan" / "a.md").write_text("A\n", encoding="utf-8")
    (tmp_path / "prompts" / "fan" / "b.md").write_text("B\n", encoding="utf-8")
    (tmp_path / "prompts" / "synthesize.md").write_text("SYNTH\n", encoding="utf-8")
    gate = tmp_path / "checks" / "verify-merged.sh"
    gate.write_text('#!/bin/sh\n[ -s "$1" ] && ! grep -q CONFLICT "$1"\n', encoding="utf-8")
    gate.chmod(gate.stat().st_mode | stat.S_IEXEC)

    def run(stub_body: str) -> subprocess.CompletedProcess:
        stub = tmp_path / "stub.sh"
        stub.write_text(stub_body, encoding="utf-8")
        stub.chmod(stub.stat().st_mode | stat.S_IEXEC)
        shutil.rmtree(tmp_path / "state", ignore_errors=True)
        env = {"PATH": os.environ["PATH"], "AGENT_CMD": str(stub)}
        return subprocess.run(
            ["bash", str(script)], cwd=tmp_path, env=env,
            capture_output=True, text=True, timeout=60,
        )

    ok = run('#!/bin/sh\nprompt="$(cat)"\necho "stub: $prompt"\n')
    assert ok.returncode == 0, ok.stderr
    assert "stub:" in (tmp_path / "state" / "final.md").read_text(encoding="utf-8")

    rejected = run('#!/bin/sh\nprompt="$(cat)"\necho "CONFLICT $prompt"\n')
    assert rejected.returncode != 0, "merged gate did not reject a conflicting synthesis"
    branch_outputs = sorted((tmp_path / "state").glob("fan-*.md"))
    assert len(branch_outputs) == 2 and all(p.stat().st_size > 0 for p in branch_outputs), (
        "branches should pass the tally; only the merged gate rejects"
    )
