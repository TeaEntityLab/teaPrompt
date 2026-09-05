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

ADOPTED = {
    "reflective-brief": (
        "Before an unknown becomes a question to the user, classify it: answerable from "
        "the repository or tools (look), safe to assume (state it with its status), or "
        "the owner's decision (ask); only the last kind is asked.",
    ),
    "reflective-implement": (
        "a broken check is reported as could-not-run and repaired or escalated as a "
        "check, never satisfied by editing the product.",
        "a log line that says success while the process failed, or a run that skipped "
        "the relevant tests, is not a pass.",
        "Every edit after the last verification run, including cosmetic cleanup or "
        "formatting, reopens verification; the reported result is the run against the "
        "final state of the change.",
        "- Do not add a fallback, catch-all, retry, or silent default that hides a "
        "failure instead of fixing its cause; a fallback is legitimate only at an "
        "external or version boundary, documented, preserving the failure evidence, and "
        "tested on both paths.",
        "For a behavior-preserving change (refactor, cleanup, compression), first lock "
        "the current behavior with the narrowest tests that would fail if it changed, "
        "then change one kind of thing per verified pass.",
    ),
    "reflective-review": (
        "An empty findings list is a valid result; never add a finding to make the "
        "review look thorough. Attribute each finding as introduced by the change or "
        "pre-existing; a pre-existing defect is reported, not charged to the change.",
    ),
    "reflective-risk": (
        "- Do not place a credential in a command line, a transcript, or a source file "
        "to make a step work; a step that needs one waits for a secret-store path or the "
        "owner. An exposed credential is revoked or rotated first — removing it from "
        "source or history does not revoke it.",
    ),
    "reflective-research": (
        "- A count, inventory, or catalog the agent generated is checked by a second "
        "method that shares none of the generator's logic — a cruder search, a hash, a "
        "fixture with a known answer; re-running the generator, or agreement between the "
        "generator and its own summary, is not a check.",
    ),
    "flow-control-generator": (
        "When a stage is itself a loop or retries, the composition's worst case is the "
        "product of the caps: declare one total budget (steps or wall-clock) that every "
        "level decrements, and have the outer script pass its remaining budget to the "
        "inner one.",
        "For fan-in, the gate runs over the merged result as well as the branch tally: "
        "branches that each pass can conflict when combined.",
        './checks/verify-merged.sh "$STATE/final.md"          # gate: merged result, '
        "not only the branch tally",
    ),
}

FAN_OUT_TEMPLATE = re.compile(
    r"## Template: Parallel Fan-out/Fan-in \(bash\)\n\n```bash\n(.*?)```", re.S
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _skill_texts() -> dict[str, str]:
    skills = library_skills_dir()
    return {
        p.parent.name: _read(p)
        for p in sorted(skills.glob("*/SKILL.md"))
    }


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


def test_sentences_at_exactly_one_surface():
    texts = _skill_texts()
    assert len(texts) == 13, sorted(texts)
    for skill, sentences in ADOPTED.items():
        for sentence in sentences:
            homes = [name for name, body in texts.items() if sentence in body]
            assert homes == [skill], f"{sentence[:50]!r} found in {homes}, expected only {skill}"


def test_fast_path_and_pinned_neighbours_untouched():
    implement = _skill_texts()["reflective-implement"]
    assert "If verification fails, fix and rerun. If a check cannot run, report why." in implement
    assert "- Do not claim checks passed unless they were run and read." in implement
    assert (
        "see the test fail on the current code before the change and pass after it, so the "
        "test proves the behavior rather than the code." in implement
    )
    brief = _skill_texts()["reflective-brief"]
    assert (
        "4. State assumptions and unknowns; an unresolved high-impact, irreversible "
        "assumption is a Human Review trigger, not a default." in brief
    )


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
    text = _skill_texts()["flow-control-generator"]
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
        env = dict(os.environ, AGENT_CMD=str(stub))
        return subprocess.run(
            ["bash", str(script)], cwd=tmp_path, env=env,
            capture_output=True, text=True, timeout=60,
        )

    ok = run('#!/bin/sh\necho "stub: $1"\n')
    assert ok.returncode == 0, ok.stderr
    assert "stub:" in (tmp_path / "state" / "final.md").read_text(encoding="utf-8")

    rejected = run('#!/bin/sh\necho "CONFLICT $1"\n')
    assert rejected.returncode != 0, "merged gate did not reject a conflicting synthesis"
    branch_outputs = sorted((tmp_path / "state").glob("fan-*.md"))
    assert len(branch_outputs) == 2 and all(p.stat().st_size > 0 for p in branch_outputs), (
        "branches should pass the tally; only the merged gate rejects"
    )
