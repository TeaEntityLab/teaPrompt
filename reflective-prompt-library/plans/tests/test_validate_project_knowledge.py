"""Tests for the PROJECT_KNOWLEDGE.md contract validator."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from validate_project_knowledge import ProjectKnowledgeValidator  # noqa: E402

REPO_ROOT = Path(__file__).parent.parent.parent.parent

VALID_DOC = """Language: English

# Project Knowledge — Test

> NON-NORMATIVE. Banner prose may say must and shall freely.

## Governing Principles

> index only

- A principle pointer — see [x](METHODOLOGY_MAP.md)

## Current Direction

### Milestone: Example
- Status: active
- Problem: something
- Non-goals: other things

## Durable Lessons

> only evidence-backed patterns

### Lesson: A real lesson
- Pattern: it happened twice
- Evidence: [plan](plans/some-plan.md)
- Review trigger: a third recurrence

## Decision Index

> map only

- 2026-06-17 A decision → [record](plans/some-plan.md)
"""


def _write(tmp_path: Path, text: str) -> ProjectKnowledgeValidator:
    target_dir = tmp_path / "reflective-prompt-library"
    target_dir.mkdir(parents=True)
    (target_dir / "PROJECT_KNOWLEDGE.md").write_text(text, encoding="utf-8")
    return ProjectKnowledgeValidator(str(tmp_path))


def test_valid_doc_passes(tmp_path):
    result = _write(tmp_path, VALID_DOC).validate()
    assert result["valid"], result["errors"]


def test_missing_file_fails(tmp_path):
    (tmp_path / "reflective-prompt-library").mkdir(parents=True)
    result = ProjectKnowledgeValidator(str(tmp_path)).validate()
    assert not result["valid"]
    assert any("not found" in e for e in result["errors"])


def test_missing_section_fails(tmp_path):
    doc = VALID_DOC.replace("## Decision Index", "## Something Else")
    result = _write(tmp_path, doc).validate()
    assert not result["valid"]
    assert any("Decision Index" in e for e in result["errors"])


def test_binding_language_in_body_fails(tmp_path):
    doc = VALID_DOC.replace(
        "- A principle pointer — see [x](METHODOLOGY_MAP.md)",
        "- Agents must always re-read this file first",
    )
    result = _write(tmp_path, doc).validate()
    assert not result["valid"]
    assert any("binding language" in e.lower() for e in result["errors"])


def test_binding_language_in_blockquote_is_exempt(tmp_path):
    # The banner already contains "must" and "shall"; that must not trip the check.
    result = _write(tmp_path, VALID_DOC).validate()
    assert result["valid"], result["errors"]


def test_lesson_without_evidence_fails(tmp_path):
    doc = VALID_DOC.replace("- Evidence: [plan](plans/some-plan.md)\n", "")
    result = _write(tmp_path, doc).validate()
    assert not result["valid"]
    assert any("Evidence" in e for e in result["errors"])


def test_milestone_with_bad_status_fails(tmp_path):
    doc = VALID_DOC.replace("- Status: active", "- Status: kinda-ongoing")
    result = _write(tmp_path, doc).validate()
    assert not result["valid"]
    assert any("invalid Status" in e for e in result["errors"])


def test_decision_index_without_link_fails(tmp_path):
    doc = VALID_DOC.replace(
        "- 2026-06-17 A decision → [record](plans/some-plan.md)",
        "- 2026-06-17 A decision with no pointer",
    )
    result = _write(tmp_path, doc).validate()
    assert not result["valid"]
    assert any("link pointer" in e for e in result["errors"])


def test_done_milestone_in_current_direction_warns(tmp_path):
    doc = VALID_DOC.replace("- Status: active", "- Status: done")
    result = _write(tmp_path, doc).validate()
    # Reflow is a suggestion, not a hard failure.
    assert result["valid"], result["errors"]
    assert any("reflow" in w.lower() for w in result["warnings"])


def test_active_milestone_produces_no_reflow_warning(tmp_path):
    result = _write(tmp_path, VALID_DOC).validate()
    assert not any("reflow" in w.lower() for w in result["warnings"])


def test_repo_project_knowledge_is_valid():
    """The real committed PROJECT_KNOWLEDGE.md must satisfy the contract."""
    result = ProjectKnowledgeValidator(str(REPO_ROOT)).validate()
    assert result["valid"], result["errors"]
