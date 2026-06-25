"""Anti-drift: thinking lenses, engineering/agent prompts, and workflow skills cross-link."""

from pathlib import Path

import pytest

LIBRARY_ROOT = Path(__file__).parent.parent.parent
THINKING_DIR = LIBRARY_ROOT / "01-thinking"
ENGINEERING_DIR = LIBRARY_ROOT / "02-engineering"
AGENT_DIR = LIBRARY_ROOT / "04-agent"
SKILLS_DIR = LIBRARY_ROOT / "skills"

ENGINEERING_THINKING_LINKS: dict[str, tuple[str, ...]] = {
    "task-start.md": (
        "01-thinking/why-what-how-done.md",
        "01-thinking/falsifiability.md",
    ),
    "spec-writer.md": ("01-thinking/falsifiability.md",),
    "code-reviewer.md": ("01-thinking/critical-thinking-check.md",),
    "implementation-agent.md": ("01-thinking/counterargument.md",),
    "test-designer.md": ("01-thinking/falsifiability.md",),
    "task-slicer.md": ("01-thinking/why-what-how-done.md",),
    "usage-first.md": ("01-thinking/socratic-reviewer.md",),
    "local-feedback.md": ("01-thinking/critical-thinking-check.md",),
}

SKILL_THINKING_SOURCES: dict[str, tuple[str, ...]] = {
    "reflective-implement": (
        "01-thinking/counterargument.md",
        "01-thinking/critical-thinking-check.md",
    ),
    "reflective-spec-plan": (
        "01-thinking/falsifiability.md",
        "01-thinking/why-what-how-done.md",
    ),
    "reflective-handoff-retro": ("01-thinking/socratic-reviewer.md",),
}


AGENT_THINKING_LINKS: dict[str, tuple[str, ...]] = {
    "runtime-trust-boundary.md": (
        "01-thinking/critical-thinking-check.md",
        "01-thinking/counterargument.md",
    ),
    "sop-compiler.md": (
        "01-thinking/falsifiability.md",
        "01-thinking/why-what-how-done.md",
    ),
    "workflow-engine.md": ("01-thinking/falsifiability.md",),
    "agent-selection.md": (
        "01-thinking/socratic-reviewer.md",
        "01-thinking/why-what-how-done.md",
    ),
    "agent-scaffold-provenance.md": ("01-thinking/critical-thinking-check.md",),
    "review-rating-fix.md": (
        "01-thinking/critical-thinking-check.md",
        "01-thinking/counterargument.md",
    ),
    "retro.md": ("01-thinking/socratic-reviewer.md",),
    "memory-consolidation.md": ("01-thinking/falsifiability.md",),
    "workflow-recipes.md": (
        "01-thinking/socratic-reviewer.md",
        "01-thinking/critical-thinking-check.md",
        "01-thinking/why-what-how-done.md",
    ),
}

AGENT_SKILL_LINKS: dict[str, tuple[str, ...]] = {
    "runtime-trust-boundary.md": (
        "reflective-implement",
        "reflective-review",
        "reflective-research",
        "reflective-spec-plan",
        "reflective-risk",
    ),
    "sop-compiler.md": ("reflective-spec-plan",),
    "workflow-engine.md": ("reflective-spec-plan",),
    "agent-selection.md": ("reflective-dispatch",),
    "agent-scaffold-provenance.md": ("reflective-research",),
    "review-rating-fix.md": ("reflective-review",),
    "retro.md": ("reflective-handoff-retro",),
    "memory-consolidation.md": ("reflective-handoff-retro",),
    "workflow-recipes.md": (
        "reflective-dispatch",
        "reflective-brief",
        "reflective-spec-plan",
    ),
}

THINKING_PROMPTS = tuple(sorted(THINKING_DIR.glob("*.md")))
ENGINEERING_PROMPTS = tuple(sorted(ENGINEERING_DIR.glob("*.md")))
AGENT_PROMPTS = tuple(sorted(AGENT_DIR.glob("*.md")))


def _preamble(path: Path) -> str:
    return path.read_text(encoding="utf-8").split("```", 1)[0]


def _prompt_sources_section(skill_path: Path) -> str:
    text = skill_path.read_text(encoding="utf-8")
    marker = "## Prompt Sources"
    assert marker in text, f"{skill_path.parent.name} missing {marker}"
    return text.split(marker, 1)[1].split("##", 1)[0]


@pytest.mark.parametrize("prompt_name,thinking_refs", ENGINEERING_THINKING_LINKS.items())
def test_engineering_prompt_links_thinking_lens(prompt_name: str, thinking_refs: tuple[str, ...]):
    path = ENGINEERING_DIR / prompt_name
    preamble = _preamble(path)
    for ref in thinking_refs:
        assert ref in preamble, f"{prompt_name} preamble should reference {ref}"


def test_all_engineering_prompts_have_thinking_cross_link():
    assert set(ENGINEERING_THINKING_LINKS) == {p.name for p in ENGINEERING_PROMPTS}


@pytest.mark.parametrize("skill_name,thinking_refs", SKILL_THINKING_SOURCES.items())
def test_workflow_skill_lists_thinking_sources(skill_name: str, thinking_refs: tuple[str, ...]):
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"
    section = _prompt_sources_section(skill_path)
    for ref in thinking_refs:
        assert ref in section, f"{skill_name} Prompt Sources should list {ref}"


@pytest.mark.parametrize("prompt_path", THINKING_PROMPTS, ids=lambda p: p.name)
def test_thinking_prompt_maps_to_workflow_skill(prompt_path: Path):
    preamble = _preamble(prompt_path)
    assert "reflective-" in preamble, f"{prompt_path.name} should map to a workflow skill"


def test_thinking_lens_files_exist_for_engineering_links():
    linked = {ref for refs in ENGINEERING_THINKING_LINKS.values() for ref in refs}
    for ref in linked:
        assert (LIBRARY_ROOT / ref).is_file(), f"missing thinking lens file {ref}"

@pytest.mark.parametrize("prompt_name,thinking_refs", AGENT_THINKING_LINKS.items())
def test_agent_prompt_links_thinking_lens(prompt_name: str, thinking_refs: tuple[str, ...]):
    path = AGENT_DIR / prompt_name
    preamble = _preamble(path)
    for ref in thinking_refs:
        assert ref in preamble, f"{prompt_name} preamble should reference {ref}"


def test_all_agent_prompts_have_thinking_cross_link():
    assert set(AGENT_THINKING_LINKS) == {p.name for p in AGENT_PROMPTS}


@pytest.mark.parametrize("prompt_name,skill_refs", AGENT_SKILL_LINKS.items())
def test_agent_prompt_maps_workflow_skill(prompt_name: str, skill_refs: tuple[str, ...]):
    preamble = _preamble(AGENT_DIR / prompt_name)
    for skill in skill_refs:
        assert skill in preamble, f"{prompt_name} preamble should reference {skill}"


def test_thinking_lens_files_exist_for_agent_links():
    linked = {ref for refs in AGENT_THINKING_LINKS.values() for ref in refs}
    for ref in linked:
        assert (LIBRARY_ROOT / ref).is_file(), f"missing thinking lens file {ref}"

