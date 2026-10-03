"""Guard the 2026-10-03 Superpowers v6.4.2 adoption: SP-1 decision-only
planning pinned once on reflective-spec-plan §Planning Fidelity; SP-2 named
coverage/disposition pinned on reflective-review (Never rules + step 8 +
Output Shape heading + example); record linked from Decision Index and the
case ledger; no other surface carries the adopted wording."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "superpowers-v6.4-adoption-2026-10-03.md"
SPEC_PLAN = library_skills_dir() / "reflective-spec-plan" / "SKILL.md"
REVIEW = library_skills_dir() / "reflective-review" / "SKILL.md"
REVIEW_EXAMPLES = library_skills_dir() / "examples" / "reflective-review.examples.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

PIN = "8ca22dba9a94f28898bce59f2537ff4d87c747d7"

SP1_ANCHOR = (
    "An implementation plan is the set of decisions the executor cannot recover alone"
)
SP1_OPPOSITE = 'a line that decides nothing ("handle edge cases"'

SP1_DOD_BULLET = (
    "Each task carries the decisions the executor cannot recover, and the plan stays "
    "proportional to them — no transcript-shaped bodies, no lines that decide nothing"
)


SP2_SILENCE = (
    "Do not treat the spec's silence on an input as permission for that input "
    "to break the software"
)
SP2_NODROP = (
    "Do not silently drop considered behaviors: anything declined as out of scope "
    "is listed in `Declined to Judge` with a reason"
)
SP2_FLOW = (
    "Record coverage: list each checked area or criterion that produced no finding, "
    "and every behavior considered but declined as outside scope"
)
SP2_HEADING = "## Declined to Judge"

CANDIDATE_STATUS = {
    "SP-1": "Adopted in place 2026-10-03 — `reflective-spec-plan` §Planning Fidelity",
    "SP-2": "Adopted in place 2026-10-03 — `reflective-review` Output / Never / Review Flow step 8 / Output Shape",
    "SP-3": "Rejected",
    "SP-4": "Rejected",
    "SP-5": "Rejected",
    "SP-6": "Rejected",
}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _section(text: str, heading: str) -> str:
    return text.split(heading, 1)[1]


def test_source_identity_pinned():
    text = _read(RECORD)
    assert PIN in text, "record lost the pinned v6.4.2 commit"
    assert "v6.4.2" in text
    assert "skills-and-spec-systems-research-2026-06-25.md" in text


def test_candidate_ledger_dispositions():
    text = _read(RECORD)
    ledger = _section(text, "## Candidate Adoption Ledger").split("\n## ", 1)[0]
    rows = [
        [cell.strip() for cell in line.split("|")[1:-1]]
        for line in ledger.splitlines()
        if re.match(r"^\| SP-\d \|", line)
    ]
    assert {row[0] for row in rows} == set(CANDIDATE_STATUS)
    for row in rows:
        assert len(row) == 5, row
        assert row[2] == CANDIDATE_STATUS[row[0]], row
        assert row[3], f"missing evidence: {row[0]}"


def test_sp1_pinned_once_on_spec_plan():
    text = _read(SPEC_PLAN)
    assert "### Planning Fidelity" in text
    section = _section(text, "### Planning Fidelity")
    assert SP1_ANCHOR in section
    assert SP1_OPPOSITE in section
    assert "**Review Focus**" in section
    assert SP1_DOD_BULLET in text, "SP-1 DoD proportion bullet missing from step 5"
    # The adopted contract must not leak to other skills.
    for other in ["reflective-review", "reflective-implement", "reflective-brief"]:
        assert SP1_ANCHOR not in _read(
            library_skills_dir() / other / "SKILL.md"
        ), f"SP-1 wording duplicated on {other}"


def test_sp2_pinned_on_review_surfaces():
    text = _read(REVIEW)
    assert SP2_SILENCE in text
    assert SP2_NODROP in text
    assert SP2_FLOW in text
    flow = _section(text, "## Review Flow")
    steps = re.findall(r"^(\d+)\. ", flow, re.MULTILINE)
    assert steps == [str(n) for n in range(1, 10)], f"flow numbering drifted: {steps}"
    assert "stays `unverifiable` in the Claims Ledger" in text, (
        "unverifiable-vs-declined distinction missing from coverage step"
    )
    output = _section(text, "## Output Shape")
    assert SP2_HEADING in output
    contract = _section(text, "Output:")
    assert "`Declined to Judge`" in contract.split("Never:", 1)[0]


def test_sp2_example_shape_updated():
    text = _read(REVIEW_EXAMPLES)
    assert SP2_HEADING in text, "example output shape lost the section"


def test_sp2_heading_absent_from_other_skills():
    for skill_dir in library_skills_dir().iterdir():
        skill = skill_dir / "SKILL.md"
        if not skill.exists() or skill_dir.name == "reflective-review":
            continue
        assert SP2_HEADING not in _read(skill), (
            f"Declined to Judge leaked into {skill_dir.name}"
        )



def test_indexes_link_the_record():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert f"[record](plans/{RECORD.name})" in knowledge
    state = _read(CASE_STUDIES).split("## State Ledger", 1)[1].split("\n## ", 1)[0]
    assert RECORD.name in state
    comparison = _read(CASE_STUDIES).split("## Case Comparison", 1)[1].split(
        "\n## ", 1)[0]
    assert f"[record]({RECORD.name})" in comparison, (
        "Case Comparison table missing the 2026-10-03 row"
    )
