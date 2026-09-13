"""Guard the versioned delta and record-to-skill adoption parity.

Paragraphs belong to the dated decision record, not duplicated Python pins.
This is an author-side structural guard, never agent-behavior enforcement.
"""

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402

RECORD_NAME = "agentflow-8.2-delta-survey-2026-09-13.md"
RECORD = PROMPT_LIBRARY_ROOT / "plans" / RECORD_NAME
ADOPTIONS = {
    "AF82-1": ("reflective-dispatch", "Route"),
    "AF82-2": ("reflective-minimality", "Safety Floor"),
    "AF82-9": ("reflective-implement", "Module Contract"),
    "AF82-14": ("reflective-implement", "During Editing"),
}


def test_delta_identity_and_ledger_dispositions():
    text = RECORD.read_text(encoding="utf-8")
    assert "b2935f5381d6469243440e080b43d0092a591663" in text
    assert "fcb6878be0b2316cdba5a111f040655f161bfe03" in text
    assert "[2026-09-05 survey](agentflow-survey-2026-09-05.md)" in text
    ledger = text.split("## Candidate Adoption Ledger\n", 1)[1].split("## Adopted Wording\n", 1)[0]
    rows = re.findall(r"^\| (AF82-\d+) \| [^|]+ \| \*\*([^*]+)\*\* \|", ledger, re.M)
    assert dict(rows) == {
        "AF82-1": "Adopted",
        "AF82-2": "Adopted",
        "AF82-3": "No change",
        "AF82-4": "No change",
        "AF82-5": "No change",
        "AF82-6": "Record-only",
        "AF82-7": "Rejected",
        "AF82-8": "No change",
        "AF82-9": "Adopted",
        "AF82-10": "No change",
        "AF82-11": "Record-only",
        "AF82-12": "Record-only",
        "AF82-13": "No change",
        "AF82-14": "Adopted",
    }
    assert len(rows) == len(dict(rows)), "duplicate candidate IDs"


@pytest.mark.parametrize("candidate", ADOPTIONS)
def test_adoption_matches_its_record_at_one_named_surface(candidate):
    skill, section = ADOPTIONS[candidate]
    record = RECORD.read_text(encoding="utf-8")
    heading = f"### {candidate} — {skill} / {section}"
    assert record.count(heading) == 1
    block = record.split(heading + "\n", 1)[1].split("\n##", 1)[0]
    paragraphs = re.findall(r"^> (.+)$", block, re.M)
    assert len(paragraphs) == 1, "adoption needs one recorded paragraph"
    paragraph = paragraphs[0]
    skills = library_skills_dir()
    target = skills / skill / "SKILL.md"
    text = target.read_text(encoding="utf-8")
    owned_section = text.split(f"## {section}\n", 1)[1].split("\n## ", 1)[0]
    assert owned_section.count(paragraph) == 1, candidate
    occurrences = {
        path: path.read_text(encoding="utf-8").count(paragraph)
        for path in skills.glob("*/SKILL.md")
    }
    assert {path: count for path, count in occurrences.items() if count} == {target: 1}


def test_delta_is_indexed_without_replacing_the_prior_survey():
    knowledge = (PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md").read_text(encoding="utf-8")
    cases = (PROMPT_LIBRARY_ROOT / "plans" / "external-adoption-case-studies-2026-06-20.md").read_text(encoding="utf-8")
    assert f"(plans/{RECORD_NAME})" in knowledge
    assert cases.count(RECORD_NAME) >= 2
    for text in (knowledge, cases):
        assert "agentflow-survey-2026-09-05.md" in text


def test_second_pass_lessons_and_procedure_steps_are_recorded():
    knowledge = (PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md").read_text(encoding="utf-8")
    cases = (PROMPT_LIBRARY_ROOT / "plans" / "external-adoption-case-studies-2026-06-20.md").read_text(encoding="utf-8")
    for heading in (
        "### Lesson: A duty seated inside a prohibition list is dropped by the reader",
        "### Lesson: A stated decision is not an observable",
    ):
        assert knowledge.count(heading) == 1, heading
        lesson = knowledge.split(heading, 1)[1].split("\n### ", 1)[0].split("\n## ", 1)[0]
        assert f"(plans/{RECORD_NAME})" in lesson
        assert "- Review trigger:" in lesson
    procedure = cases.split("## The Recurring Evaluation Procedure", 1)[1].split("\n## ", 1)[0]
    assert "10. **Own every changed file family.**" in procedure
    assert "11. **Probe drafted wording against state, not statements, before landing.**" in procedure
    record = RECORD.read_text(encoding="utf-8")
    assert record.count("## Coordinator Reflections (2026-09-13)") == 1
