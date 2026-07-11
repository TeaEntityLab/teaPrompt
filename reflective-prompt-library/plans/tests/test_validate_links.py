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
