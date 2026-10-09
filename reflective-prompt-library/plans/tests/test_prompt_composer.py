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


def test_compose_low_token_preserves_primary_instructions(composer):
    """Low-token mode must keep primary fenced/unfenced instructions.

    Regression for the recorded defect where --low-token deleted all fenced
    blocks, including core-short's primary anti-cheating instruction.
    """
    low = composer.compose(["core-short"], low_token=True)

    assert "Inputs / Outputs" in low
    assert "Failure Conditions" in low
    assert "Self-check" in low
    assert "對 AI 產物保持不信任" in low


def test_compose_low_token_preserves_secondary_template(composer):
    """A second primary template keeps safety and acceptance instructions."""
    low = composer.compose(["spec-writer"], low_token=True)

    assert "Acceptance Criteria" in low
    assert "Human Review Required" in low
    assert "Non-goals" in low


def test_strip_examples_removes_marked_examples_only(composer):
    """Only explicitly marked Example sections are removed."""
    content = (
        "# Title\n\n"
        "Primary instruction with ```inline fence``` kept.\n\n"
        "```markdown\nprimary fenced instruction\n```\n\n"
        "## Example 1\n\n"
        "Extended illustration to drop.\n\n"
        "```text\nillustration body\n```\n\n"
        "## Acceptance Criteria\n\n"
        "Must survive compression.\n"
    )
    stripped = composer._strip_examples(content)

    assert "primary fenced instruction" in stripped
    assert "Acceptance Criteria" in stripped
    assert "Must survive compression" in stripped
    assert "Extended illustration" not in stripped
    assert "illustration body" not in stripped


def test_strip_examples_preserves_placeholders(composer):
    """Placeholder slots are not treated as strippable example content."""
    content = "## Inputs\n{貼上需求}\n\n```markdown\n{keep me}\n```\n"
    stripped = composer._strip_examples(content)

    assert "{貼上需求}" in stripped
    assert "{keep me}" in stripped


@pytest.mark.parametrize("fence", ["```", "~~~", "````"])
def test_low_token_keeps_fenced_example_instructions_and_drops_adjacent_examples(composer, fence):
    content = (
        f"{fence}markdown\n"
        "## Examples\nPrimary requirement: explain the evidence.\n"
        f"{fence}\n"
        "## Example 1\nFirst expendable illustration.\n"
        "## Example 2\nSecond expendable illustration.\n"
        "## Acceptance Criteria\nEvidence remains mandatory.\n"
        "    ## Examples\n    Indented primary instruction remains mandatory.\n"
    )

    stripped = composer._strip_examples(content)

    assert "Primary requirement: explain the evidence." in stripped
    assert "Evidence remains mandatory." in stripped
    assert "Indented primary instruction remains mandatory." in stripped
    assert "First expendable illustration." not in stripped
    assert "Second expendable illustration." not in stripped


def test_compose_missing_second_source_raises_only_partial_avoided(composer, monkeypatch):
    """Direct compose with a missing second input publishes nothing partial."""
    output_before = composer.compose(["core-full", "spec-writer"])
    assert "## Prompt 1: core-full" in output_before
    assert "## Prompt 2: spec-writer" in output_before

    real_read = composer.read_prompt

    def fake_read(rel_path: str) -> str:
        if rel_path.endswith("02-engineering/spec-writer.md"):
            raise FileNotFoundError(f"Prompt file not found: {rel_path}")
        return real_read(rel_path)

    monkeypatch.setattr(composer, "read_prompt", fake_read)
    with pytest.raises(FileNotFoundError, match="Prompt file not found"):
        composer.compose(["core-full", "spec-writer"])


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


def test_cli_stdout_failure_emits_no_success_output(composer, monkeypatch, capsys):
    """A stdout-path compose failure emits no success-shaped partial output."""
    import prompt_composer as composer_module

    real_read = composer.read_prompt

    def fake_read(rel_path: str) -> str:
        if rel_path.endswith("02-engineering/spec-writer.md"):
            raise FileNotFoundError(f"Prompt file not found: {rel_path}")
        return real_read(rel_path)

    monkeypatch.setattr(composer, "read_prompt", fake_read)
    monkeypatch.setattr(composer_module, "PromptComposer", lambda _root: composer)
    monkeypatch.setattr(
        sys,
        "argv",
        ["prompt_composer.py", "core-full", "spec-writer"],
    )
    assert composer_module.main() == 1
    captured = capsys.readouterr()
    assert "Generated from 2 prompts" not in captured.out
    assert "## Prompt 1" not in captured.out
    assert "Prompt file not found" in captured.err


def test_cli_output_write_failure_preserves_existing_file(
    composer, tmp_path, monkeypatch, capsys
):
    """A destination write failure is distinct from missing source input."""
    import prompt_composer as composer_module

    target = tmp_path / "composed.md"
    previous = b"previous complete artifact\n"
    target.write_bytes(previous)
    real_write = Path.write_text

    def denied_write(path, content, *args, **kwargs):
        if path == target:
            raise PermissionError(13, "Permission denied", str(path))
        return real_write(path, content, *args, **kwargs)

    monkeypatch.setattr(Path, "write_text", denied_write)
    monkeypatch.setattr(composer_module, "PromptComposer", lambda _root: composer)
    monkeypatch.setattr(
        sys, "argv",
        ["prompt_composer.py", "core-full", "spec-writer", "--output", str(target)],
    )

    assert composer_module.main() == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert str(target) in captured.err
    assert target.read_bytes() == previous


@pytest.mark.parametrize("output_mode", ["stdout", "fresh", "existing"])
def test_cli_missing_source_does_not_publish_partial_output(
    composer, tmp_path, output_mode
):
    """Exercise the real CLI with an index that still names a missing input."""
    import json
    import shutil
    import subprocess

    library = tmp_path / "reflective-prompt-library"
    plans = library / "plans"
    plans.mkdir(parents=True)
    script = plans / "prompt_composer.py"
    shutil.copyfile(Path(__file__).resolve().parent.parent / script.name, script)
    (library / "index.json").write_text(json.dumps(composer.index), encoding="utf-8")
    for slug in ("core-full", "spec-writer"):
        relative = composer.resolve_slug(slug)
        source = tmp_path / relative
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text(composer.read_prompt(relative), encoding="utf-8")

    command = [sys.executable, str(script), "core-full", "spec-writer"]
    valid = subprocess.run(command, cwd=tmp_path, capture_output=True, text=True, timeout=15)
    assert valid.returncode == 0, valid.stderr
    assert "## Prompt 1: core-full" in valid.stdout
    assert "## Prompt 2: spec-writer" in valid.stdout
    (tmp_path / composer.resolve_slug("spec-writer")).unlink()

    target = tmp_path / "composed.md"
    previous = b"previous complete artifact\n"
    if output_mode == "existing":
        target.write_bytes(previous)
    if output_mode != "stdout":
        command.extend(["--output", str(target)])
    missing = subprocess.run(command, cwd=tmp_path, capture_output=True, text=True, timeout=15)

    assert missing.returncode == 1
    assert missing.stdout == ""
    assert "Prompt file not found" in missing.stderr
    assert "spec-writer" in missing.stderr
    if output_mode == "existing":
        assert target.read_bytes() == previous
    else:
        assert not target.exists()


def test_resolve_slugs_returns_ordered_paths(composer):
    """resolve_slugs should return paths in the same order as input slugs."""
    paths = composer.resolve_slugs(["core-full", "spec-writer", "code-reviewer"])
    assert len(paths) == 3
    assert "00-core/core-full.md" in paths[0]
    assert "02-engineering/spec-writer.md" in paths[1]
    assert "02-engineering/code-reviewer.md" in paths[2]
