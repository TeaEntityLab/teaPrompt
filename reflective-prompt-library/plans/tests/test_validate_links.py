"""Pytest mirrors for validate_links.py (Round 77 anti-drift)."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from validate_links import LinkValidator  # noqa: E402

REPO_ROOT = Path(__file__).parent.parent.parent.parent


@pytest.fixture(scope="module")
def link_results():
    return LinkValidator(str(REPO_ROOT)).validate_all()


def test_live_repo_has_no_link_errors(link_results):
    assert link_results["total_errors"] == 0, {
        "ref_file": link_results["ref_file_errors"],
        "ref_snippet": link_results["ref_snippet_errors"],
        "markdown": link_results["markdown_link_errors"],
        "frontmatter": link_results["frontmatter_errors"],
    }


def test_broken_markdown_link_is_detected(tmp_path):
    bad_file = tmp_path / "broken.md"
    bad_file.write_text("[missing](does-not-exist.md)\n", encoding="utf-8")
    results = {
        "ref_file_errors": [],
        "ref_snippet_errors": [],
        "markdown_link_errors": [],
        "frontmatter_errors": [],
        "total_files": 0,
        "total_errors": 0,
    }
    LinkValidator(str(tmp_path)).validate_markdown_links(
        bad_file.read_text(encoding="utf-8"),
        bad_file,
        bad_file.relative_to(tmp_path),
        results,
    )
    assert results["markdown_link_errors"]


def test_skill_frontmatter_requires_name_description_and_license(tmp_path):
    skill_dir = tmp_path / "reflective-prompt-library" / "skills" / "reflective-dispatch"
    skill_dir.mkdir(parents=True)
    skill_file = skill_dir / "SKILL.md"
    skill_file.write_text(
        """---
---
# Missing name, description, and license
""",
        encoding="utf-8",
    )
    results = {
        "ref_file_errors": [],
        "ref_snippet_errors": [],
        "markdown_link_errors": [],
        "frontmatter_errors": [],
        "total_files": 0,
        "total_errors": 0,
    }
    LinkValidator(str(tmp_path)).validate_skill_frontmatter(
        skill_file.read_text(encoding="utf-8"),
        skill_file,
        skill_file.relative_to(tmp_path),
        results,
    )
    errors = [item["error"] for item in results["frontmatter_errors"]]
    assert any("Missing required field: name" in err for err in errors)
    assert any("Missing required field: description" in err for err in errors)
    assert any("Missing required field: license" in err for err in errors)


def _empty_results():
    return {
        "ref_file_errors": [],
        "ref_snippet_errors": [],
        "markdown_link_errors": [],
        "frontmatter_errors": [],
        "total_files": 0,
        "total_errors": 0,
    }


def _frontmatter_errors(tmp_path, skill_dir_name, frontmatter):
    skill_dir = tmp_path / "reflective-prompt-library" / "skills" / skill_dir_name
    skill_dir.mkdir(parents=True)
    skill_file = skill_dir / "SKILL.md"
    skill_file.write_text(f"---\n{frontmatter}\n---\n# Test\n", encoding="utf-8")
    results = _empty_results()
    LinkValidator(str(tmp_path)).validate_skill_frontmatter(
        skill_file.read_text(encoding="utf-8"),
        skill_file,
        skill_file.relative_to(tmp_path),
        results,
    )
    return [item["error"] for item in results["frontmatter_errors"]]


def test_skill_frontmatter_rejects_spec_unknown_top_level_fields(tmp_path):
    """Agent Skills spec: governance fields must live under metadata, not top level."""
    errors = _frontmatter_errors(
        tmp_path,
        "reflective-dispatch",
        "name: reflective-dispatch\ndescription: test\nlicense: MIT\nrisk_level: low",
    )
    assert any("Spec-unknown top-level field: risk_level" in err for err in errors)


def test_skill_frontmatter_accepts_metadata_nested_governance_fields(tmp_path):
    """Canonical post-migration form validates cleanly."""
    errors = _frontmatter_errors(
        tmp_path,
        "reflective-dispatch",
        "name: reflective-dispatch\ndescription: test\nlicense: MIT\n"
        "metadata:\n  risk_level: low\n  human_review_required: false\n"
        "  external_io: false\n  context_load: low",
    )
    assert errors == []


def test_skill_frontmatter_name_must_match_directory_and_spec_regex(tmp_path):
    errors = _frontmatter_errors(
        tmp_path,
        "reflective-dispatch",
        "name: Reflective--Dispatch\ndescription: test\nlicense: MIT",
    )
    assert any("Spec-invalid name" in err for err in errors)
    assert any("must match skill directory" in err for err in errors)


def test_skill_frontmatter_description_length_capped(tmp_path):
    long_description = "x" * 1025
    errors = _frontmatter_errors(
        tmp_path,
        "reflective-dispatch",
        f"name: reflective-dispatch\ndescription: {long_description}\nlicense: MIT",
    )
    assert any("description exceeds spec cap" in err for err in errors)
