"""Tests for prompt_composer.py."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from prompt_composer import CATEGORY_ORDER, TEMPLATES, PromptComposer


@pytest.fixture
def composer():
    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    return PromptComposer(repo_root)


def test_slug_map_contains_all_categories(composer):
    """Index should contain entries for each expected category."""
    slug_map = composer.slug_map
    for cat in CATEGORY_ORDER:
        cat_slugs = [k for k in slug_map if k.startswith(f"{cat}/")]
        assert len(cat_slugs) > 0, f"Category {cat} has no slugs"


def test_resolve_valid_simple_slug(composer):
    """Simple slugs should resolve to a file path."""
    path = composer.resolve_slug("core-full")
    assert "00-core/core-full.md" in path


def test_resolve_valid_prefixed_slug(composer):
    """Category-prefixed slugs should resolve to a file path."""
    path = composer.resolve_slug("00-core/core-full")
    assert "00-core/core-full.md" in path


def test_resolve_unknown_slug_raises(composer):
    """Unknown slugs should raise ValueError with helpful message."""
    with pytest.raises(ValueError, match="Unknown slug"):
        composer.resolve_slug("nonexistent-abcdef")


def test_compose_multiple_slugs(composer):
    """Composing multiple valid slugs should produce combined output."""
    output = composer.compose(["core-full", "spec-writer"])
    assert "## Prompt 1: core-full" in output
    assert "## Prompt 2: spec-writer" in output
    assert "Reflective Engineering Agent" in output
    assert "Spec Writer" in output
    assert "---" in output


def test_compose_with_task(composer):
    """--task flag should inject task section."""
    output = composer.compose(["core-short"], task_text="My custom task")
    assert "## Task" in output
    assert "My custom task" in output
    assert "## Prompt 1: core-short" in output


def test_compose_low_token_strips_examples(composer):
    """Low-token mode should strip fenced code blocks."""
    full = composer.compose(["spec-writer"])
    low = composer.compose(["spec-writer"], low_token=True)

    assert "```" in full
    assert "```" not in low
    assert len(low) < len(full)


def test_template_engineering_task(composer):
    """engineering-task template should expand to 8 slugs."""
    slugs = composer.expand_template("engineering-task")
    assert len(slugs) == 8
    assert "core-full" in slugs
    assert "task-start" in slugs
    assert "code-reviewer" in slugs


def test_template_long_research(composer):
    """long-research template should expand to 4 slugs."""
    slugs = composer.expand_template("long-research")
    assert len(slugs) == 4
    assert "core-full" in slugs
    assert "research" in slugs
    assert "large-context" in slugs
    assert "context-handoff" in slugs


def test_template_unknown_raises(composer):
    """Unknown template names should raise ValueError."""
    with pytest.raises(ValueError, match="Unknown template"):
        composer.expand_template("nonexistent-template")


def test_list_slugs_returns_categories(composer):
    """list_slugs should include all categories from CATEGORY_ORDER."""
    output = composer.list_slugs()
    for cat in CATEGORY_ORDER:
        assert f"[{cat}]" in output
    assert "Templates:" in output


def test_compose_unknown_slug_raises(composer):
    """Composing with an unknown slug should raise ValueError."""
    with pytest.raises(ValueError, match="Unknown slug"):
        composer.compose(["core-full", "nonexistent-xyz"])


def test_resolve_slugs_returns_ordered_paths(composer):
    """resolve_slugs should return paths in the same order as input slugs."""
    paths = composer.resolve_slugs(["core-full", "spec-writer", "code-reviewer"])
    assert len(paths) == 3
    assert "00-core/core-full.md" in paths[0]
    assert "02-engineering/spec-writer.md" in paths[1]
    assert "02-engineering/code-reviewer.md" in paths[2]
