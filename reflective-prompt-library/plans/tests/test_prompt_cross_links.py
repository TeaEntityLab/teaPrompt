"""Anti-drift: thinking lenses, core/engineering/agent/context/domain/repo prompts, and workflow skills cross-link."""

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_ROOT,
    category_prompt_dir,
    library_skills_dir,
)

LIBRARY_ROOT = PROMPT_LIBRARY_ROOT
CORE_DIR = category_prompt_dir("00-core")
THINKING_DIR = category_prompt_dir("01-thinking")
ENGINEERING_DIR = category_prompt_dir("02-engineering")
AGENT_DIR = category_prompt_dir("04-agent")
CONTEXT_DIR = category_prompt_dir("03-context")
DOMAIN_DIR = category_prompt_dir("05-domain")
REPO_DIR = category_prompt_dir("06-repo")
SKILLS_DIR = library_skills_dir()

CORE_THINKING_LINKS: dict[str, tuple[str, ...]] = {
    "core-full.md": (
        "01-thinking/why-what-how-done.md",
        "01-thinking/critical-thinking-check.md",
    ),
    "core-minimal.md": ("01-thinking/why-what-how-done.md",),
    "core-short.md": ("01-thinking/why-what-how-done.md",),
    "custom-instruction-en.md": (),
    "custom-instruction-zh.md": (),
    "daily-minimal.md": (
        "01-thinking/falsifiability.md",
        "01-thinking/why-what-how-done.md",
    ),
    "global-controller.md": ("01-thinking/why-what-how-done.md",),
    "important-task-full.md": (
        "01-thinking/socratic-reviewer.md",
        "01-thinking/critical-thinking-check.md",
    ),
    "master-prompt.md": (
        "01-thinking/socratic-reviewer.md",
        "01-thinking/critical-thinking-check.md",
    ),
}

CORE_SKILL_LINKS: dict[str, tuple[str, ...]] = {
    "core-full.md": ("reflective-brief", "reflective-dispatch"),
    "core-minimal.md": ("reflective-brief",),
    "core-short.md": ("reflective-brief", "reflective-dispatch"),
    "custom-instruction-en.md": ("reflective-brief",),
    "custom-instruction-zh.md": ("reflective-brief",),
    "daily-minimal.md": ("reflective-brief",),
    "global-controller.md": ("reflective-dispatch",),
    "important-task-full.md": ("reflective-brief", "reflective-research"),
    "master-prompt.md": ("reflective-brief", "reflective-dispatch"),
}

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

ENGINEERING_SKILL_LINKS: dict[str, tuple[str, ...]] = {
    "code-reviewer.md": ("reflective-review",),
    "implementation-agent.md": ("reflective-implement",),
    "local-feedback.md": ("reflective-implement",),
    "spec-writer.md": ("reflective-spec-plan",),
    "task-slicer.md": ("reflective-spec-plan",),
    "task-start.md": ("reflective-brief",),
    "test-designer.md": ("reflective-spec-plan",),
    "usage-first.md": ("reflective-spec-plan",),
}

SKILL_THINKING_SOURCES: dict[str, tuple[str, ...]] = {
    "reflective-brief": (
        "01-thinking/why-what-how-done.md",
        "01-thinking/falsifiability.md",
    ),
    "reflective-dispatch": ("01-thinking/socratic-reviewer.md",),
    "reflective-handoff-retro": ("01-thinking/socratic-reviewer.md",),
    "reflective-implement": (
        "01-thinking/counterargument.md",
        "01-thinking/critical-thinking-check.md",
    ),
    "reflective-minimality": ("01-thinking/counterargument.md",),
    "reflective-research": (
        "01-thinking/socratic-reviewer.md",
        "01-thinking/critical-thinking-check.md",
    ),
    "reflective-review": (
        "01-thinking/critical-thinking-check.md",
        "01-thinking/counterargument.md",
    ),
    "reflective-risk": ("01-thinking/critical-thinking-check.md",),
    "reflective-spec-plan": (
        "01-thinking/falsifiability.md",
        "01-thinking/why-what-how-done.md",
    ),
}


AGENT_THINKING_LINKS: dict[str, tuple[str, ...]] = {
    "artifact-promotion.md": (
        "01-thinking/falsifiability.md",
        "01-thinking/why-what-how-done.md",
    ),
    "external-adoption-review.md": (
        "01-thinking/critical-thinking-check.md",
        "01-thinking/counterargument.md",
    ),
    "runtime-trust-boundary.md": (
        "01-thinking/critical-thinking-check.md",
        "01-thinking/counterargument.md",
    ),
    "sop-compiler.md": (
        "01-thinking/falsifiability.md",
        "01-thinking/why-what-how-done.md",
    ),
    "workflow-engine.md": ("01-thinking/falsifiability.md",),
    "workflow-acquisition.md": (
        "01-thinking/falsifiability.md",
        "01-thinking/why-what-how-done.md",
    ),
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
    "artifact-promotion.md": (
        "reflective-dispatch",
        "reflective-handoff-retro",
    ),
    "external-adoption-review.md": (
        "reflective-dispatch",
        "reflective-minimality",
        "reflective-research",
        "reflective-risk",
    ),
    "runtime-trust-boundary.md": (
        "reflective-implement",
        "reflective-review",
        "reflective-research",
        "reflective-spec-plan",
        "reflective-risk",
    ),
    "sop-compiler.md": ("reflective-spec-plan",),
    "workflow-engine.md": ("reflective-spec-plan",),
    "workflow-acquisition.md": (
        "reflective-handoff-retro",
        "reflective-implement",
        "reflective-spec-plan",
    ),
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

CONTEXT_THINKING_LINKS: dict[str, tuple[str, ...]] = {
    "context-engineering.md": (
        "01-thinking/falsifiability.md",
        "01-thinking/why-what-how-done.md",
    ),
    "context-handoff.md": (
        "01-thinking/why-what-how-done.md",
        "01-thinking/socratic-reviewer.md",
    ),
    "gemini-long-document.md": (
        "01-thinking/critical-thinking-check.md",
        "01-thinking/falsifiability.md",
    ),
    "large-context.md": (
        "01-thinking/falsifiability.md",
        "01-thinking/critical-thinking-check.md",
    ),
    "low-token.md": (
        "01-thinking/critical-thinking-check.md",
        "01-thinking/why-what-how-done.md",
    ),
    "medium-context.md": (
        "01-thinking/why-what-how-done.md",
        "01-thinking/falsifiability.md",
    ),
    "small-context.md": (
        "01-thinking/critical-thinking-check.md",
        "01-thinking/why-what-how-done.md",
    ),
}

CONTEXT_SKILL_LINKS: dict[str, tuple[str, ...]] = {
    "context-engineering.md": ("reflective-dispatch", "reflective-research"),
    "context-handoff.md": ("reflective-handoff-retro",),
    "gemini-long-document.md": ("reflective-research",),
    "large-context.md": ("reflective-research", "reflective-spec-plan"),
    "low-token.md": ("reflective-dispatch", "reflective-brief"),
    "medium-context.md": ("reflective-spec-plan", "reflective-brief"),
    "small-context.md": ("reflective-brief", "reflective-dispatch"),
}


CORE_PROMPTS = tuple(sorted(CORE_DIR.glob("*.md")))
THINKING_PROMPTS = tuple(sorted(THINKING_DIR.glob("*.md")))
ENGINEERING_PROMPTS = tuple(sorted(ENGINEERING_DIR.glob("*.md")))
AGENT_PROMPTS = tuple(sorted(AGENT_DIR.glob("*.md")))

DOMAIN_THINKING_LINKS: dict[str, tuple[str, ...]] = {
    "business-strategy.md": (
        "01-thinking/counterargument.md",
        "01-thinking/falsifiability.md",
        "01-thinking/socratic-reviewer.md",
    ),
    "creative-template.md": (
        "01-thinking/falsifiability.md",
        "01-thinking/why-what-how-done.md",
    ),
    "deep-analysis.md": (
        "01-thinking/critical-thinking-check.md",
        "01-thinking/counterargument.md",
        "01-thinking/socratic-reviewer.md",
    ),
    "high-risk.md": (
        "01-thinking/critical-thinking-check.md",
        "01-thinking/counterargument.md",
        "01-thinking/falsifiability.md",
    ),
    "learning-coach.md": (
        "01-thinking/falsifiability.md",
        "01-thinking/why-what-how-done.md",
    ),
    "research.md": (
        "01-thinking/falsifiability.md",
        "01-thinking/critical-thinking-check.md",
        "01-thinking/counterargument.md",
    ),
    "writing-article.md": (
        "01-thinking/counterargument.md",
        "01-thinking/critical-thinking-check.md",
        "01-thinking/socratic-reviewer.md",
    ),
}

DOMAIN_SKILL_LINKS: dict[str, tuple[str, ...]] = {
    "business-strategy.md": ("reflective-brief", "reflective-research"),
    "creative-template.md": ("reflective-spec-plan",),
    "deep-analysis.md": ("reflective-research", "reflective-spec-plan"),
    "high-risk.md": ("reflective-risk", "reflective-review"),
    "learning-coach.md": ("reflective-brief",),
    "research.md": ("reflective-research",),
    "writing-article.md": ("reflective-brief", "reflective-review"),
}

DOMAIN_PROMPTS = tuple(sorted(DOMAIN_DIR.glob("*.md")))

REPO_THINKING_LINKS: dict[str, tuple[str, ...]] = {
    "AGENTS.md": (
        "01-thinking/why-what-how-done.md",
        "01-thinking/critical-thinking-check.md",
        "01-thinking/socratic-reviewer.md",
    ),
    "cursor-rules.md": (
        "01-thinking/critical-thinking-check.md",
        "01-thinking/falsifiability.md",
    ),
    "codex-opencode.md": (
        "01-thinking/why-what-how-done.md",
        "01-thinking/falsifiability.md",
    ),
    "PROJECT_KNOWLEDGE.template.md": (
        "01-thinking/socratic-reviewer.md",
        "01-thinking/falsifiability.md",
    ),
}

REPO_SKILL_LINKS: dict[str, tuple[str, ...]] = {
    "AGENTS.md": (
        "reflective-dispatch",
        "reflective-implement",
        "reflective-spec-plan",
    ),
    "cursor-rules.md": ("reflective-implement", "reflective-review"),
    "codex-opencode.md": ("reflective-implement", "reflective-dispatch"),
    "PROJECT_KNOWLEDGE.template.md": ("reflective-handoff-retro", "reflective-brief"),
}

REPO_PROMPTS = tuple(sorted(REPO_DIR.glob("*.md")))

CONTEXT_PROMPTS = tuple(sorted(CONTEXT_DIR.glob("*.md")))


def _preamble(path: Path) -> str:
    return path.read_text(encoding="utf-8").split("```", 1)[0]



def _primary_workflow_surfaces_skills(preamble: str) -> tuple[str, ...]:
    """Skills named on the Purpose Primary workflow surfaces line only."""
    purpose = preamble.split("## Scope", 1)[0]
    match = re.search(r"Primary workflow surfaces?:(.*)", purpose, re.DOTALL)
    assert match, "missing Primary workflow surfaces line in Purpose preamble"
    line = match.group(1).split("\n", 1)[0]
    return tuple(sorted(set(re.findall(r"`(reflective-[a-z-]+)`", line))))


def _supporting_lens_skills(preamble: str) -> tuple[str, ...]:
    """Skills named on the Purpose Supporting lens line (no Primary workflow surface)."""
    purpose = preamble.split("## Scope", 1)[0]
    match = re.search(r"Supporting lens for(.*)", purpose, re.DOTALL)
    assert match, "missing Supporting lens for line in Purpose preamble"
    line = match.group(1).split("\n", 1)[0]
    return tuple(sorted(set(re.findall(r"`(reflective-[a-z-]+)`", line))))


def _prompt_sources_section(skill_path: Path) -> str:
    text = skill_path.read_text(encoding="utf-8")
    marker = "## Prompt Sources"
    assert marker in text, f"{skill_path.parent.name} missing {marker}"
    return text.split(marker, 1)[1].split("##", 1)[0]



@pytest.mark.parametrize("prompt_name,thinking_refs", CORE_THINKING_LINKS.items())
def test_core_prompt_links_thinking_lens(prompt_name: str, thinking_refs: tuple[str, ...]):
    path = CORE_DIR / prompt_name
    preamble = _preamble(path)
    for ref in thinking_refs:
        assert ref in preamble, f"{prompt_name} preamble should reference {ref}"


def test_all_core_prompts_have_thinking_cross_link():
    assert set(CORE_THINKING_LINKS) == {p.name for p in CORE_PROMPTS}


def test_all_core_prompts_have_skill_link():
    assert set(CORE_SKILL_LINKS) == {p.name for p in CORE_PROMPTS}


@pytest.mark.parametrize("prompt_name,skill_refs", CORE_SKILL_LINKS.items())
def test_core_prompt_maps_workflow_skill(prompt_name: str, skill_refs: tuple[str, ...]):
    preamble = _preamble(CORE_DIR / prompt_name)
    for skill in skill_refs:
        assert skill in preamble, f"{prompt_name} preamble should reference {skill}"


@pytest.mark.parametrize("prompt_name,skill_refs", CORE_SKILL_LINKS.items())
def test_core_prompt_primary_surfaces_match_skill_links(
    prompt_name: str, skill_refs: tuple[str, ...]
):
    preamble = _preamble(CORE_DIR / prompt_name)
    listed = _primary_workflow_surfaces_skills(preamble)
    assert listed == tuple(sorted(skill_refs)), (
        f"{prompt_name} Primary workflow surfaces {listed} != {skill_refs}"
    )


def test_thinking_lens_files_exist_for_core_links():
    linked = {ref for refs in CORE_THINKING_LINKS.values() for ref in refs}
    for ref in linked:
        assert (LIBRARY_ROOT / ref).is_file(), f"missing thinking lens file {ref}"


@pytest.mark.parametrize("prompt_name,thinking_refs", ENGINEERING_THINKING_LINKS.items())
def test_engineering_prompt_links_thinking_lens(prompt_name: str, thinking_refs: tuple[str, ...]):
    path = ENGINEERING_DIR / prompt_name
    preamble = _preamble(path)
    for ref in thinking_refs:
        assert ref in preamble, f"{prompt_name} preamble should reference {ref}"


def test_all_engineering_prompts_have_thinking_cross_link():
    assert set(ENGINEERING_THINKING_LINKS) == {p.name for p in ENGINEERING_PROMPTS}


def test_all_engineering_prompts_have_skill_link():
    assert set(ENGINEERING_SKILL_LINKS) == {p.name for p in ENGINEERING_PROMPTS}


@pytest.mark.parametrize("prompt_name,skill_refs", ENGINEERING_SKILL_LINKS.items())
def test_engineering_prompt_primary_surfaces_match_skill_links(
    prompt_name: str, skill_refs: tuple[str, ...]
):
    preamble = _preamble(ENGINEERING_DIR / prompt_name)
    listed = _primary_workflow_surfaces_skills(preamble)
    assert listed == tuple(sorted(skill_refs)), (
        f"{prompt_name} Primary workflow surface {listed} != {skill_refs}"
    )


@pytest.mark.parametrize("skill_name,thinking_refs", SKILL_THINKING_SOURCES.items())
def test_workflow_skill_lists_thinking_sources(skill_name: str, thinking_refs: tuple[str, ...]):
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"
    section = _prompt_sources_section(skill_path)
    for ref in thinking_refs:
        assert ref in section, f"{skill_name} Prompt Sources should list {ref}"


def test_all_workflow_skills_have_thinking_cross_link():
    from validate_skill_examples import CORE_SKILLS  # noqa: WPS433

    assert set(SKILL_THINKING_SOURCES) == set(CORE_SKILLS)


def test_thinking_lens_files_exist_for_skill_links():
    linked = {ref for refs in SKILL_THINKING_SOURCES.values() for ref in refs}
    for ref in linked:
        assert (LIBRARY_ROOT / ref).is_file(), f"missing thinking lens file {ref}"


def _invert_skill_thinking_sources() -> dict[str, tuple[str, ...]]:
    consumers: dict[str, set[str]] = {}
    for skill, lenses in SKILL_THINKING_SOURCES.items():
        for lens in lenses:
            consumers.setdefault(lens, set()).add(skill)
    return {lens: tuple(sorted(skills)) for lens, skills in sorted(consumers.items())}


THINKING_LENS_SKILL_CONSUMERS = _invert_skill_thinking_sources()

def test_all_thinking_lenses_tracked_in_consumer_map():
    """Every 01-thinking file cited by a skill must appear in the reciprocal map."""
    expected = {f"01-thinking/{path.name}" for path in THINKING_PROMPTS}
    assert set(THINKING_LENS_SKILL_CONSUMERS) == expected


@pytest.mark.parametrize("lens_ref,consumer_skills", THINKING_LENS_SKILL_CONSUMERS.items())
def test_thinking_lens_preamble_lists_consumer_skills(lens_ref: str, consumer_skills: tuple[str, ...]):
    """Reciprocal anti-drift: lenses name every workflow skill that cites them."""
    preamble = _preamble(THINKING_DIR / Path(lens_ref).name)
    for skill in consumer_skills:
        assert skill in preamble, f"{lens_ref} preamble should reference consumer {skill}"




@pytest.mark.parametrize("lens_ref,consumer_skills", THINKING_LENS_SKILL_CONSUMERS.items())
def test_thinking_lens_primary_surfaces_match_consumer_graph(
    lens_ref: str, consumer_skills: tuple[str, ...]
):
    """Primary workflow surfaces must list exactly the skills that cite this lens."""
    preamble = _preamble(THINKING_DIR / Path(lens_ref).name)
    listed = _primary_workflow_surfaces_skills(preamble)
    assert listed == consumer_skills, (
        f"{lens_ref} Primary workflow surfaces {listed} != graph {consumer_skills}"
    )

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


def test_all_agent_prompts_have_skill_link():
    assert set(AGENT_SKILL_LINKS) == {p.name for p in AGENT_PROMPTS}


@pytest.mark.parametrize("prompt_name,skill_refs", AGENT_SKILL_LINKS.items())
def test_agent_prompt_maps_workflow_skill(prompt_name: str, skill_refs: tuple[str, ...]):
    preamble = _preamble(AGENT_DIR / prompt_name)
    for skill in skill_refs:
        assert skill in preamble, f"{prompt_name} preamble should reference {skill}"


@pytest.mark.parametrize(
    "prompt_name,skill_refs",
    [
        (name, refs)
        for name, refs in AGENT_SKILL_LINKS.items()
        if name != "runtime-trust-boundary.md"
    ],
)
def test_agent_prompt_primary_surfaces_match_skill_links(
    prompt_name: str, skill_refs: tuple[str, ...]
):
    preamble = _preamble(AGENT_DIR / prompt_name)
    listed = _primary_workflow_surfaces_skills(preamble)
    assert listed == tuple(sorted(skill_refs)), (
        f"{prompt_name} Primary workflow surface {listed} != {skill_refs}"
    )


def test_runtime_trust_boundary_supporting_lens_lists_skills():
    preamble = _preamble(AGENT_DIR / "runtime-trust-boundary.md")
    listed = _supporting_lens_skills(preamble)
    expected = AGENT_SKILL_LINKS["runtime-trust-boundary.md"]
    assert listed == tuple(sorted(expected)), f"Supporting lens {listed} != {expected}"


def test_thinking_lens_files_exist_for_agent_links():
    linked = {ref for refs in AGENT_THINKING_LINKS.values() for ref in refs}
    for ref in linked:
        assert (LIBRARY_ROOT / ref).is_file(), f"missing thinking lens file {ref}"

@pytest.mark.parametrize("prompt_name,thinking_refs", CONTEXT_THINKING_LINKS.items())
def test_context_prompt_links_thinking_lens(prompt_name: str, thinking_refs: tuple[str, ...]):
    path = CONTEXT_DIR / prompt_name
    preamble = _preamble(path)
    for ref in thinking_refs:
        assert ref in preamble, f"{prompt_name} preamble should reference {ref}"


def test_all_context_prompts_have_thinking_cross_link():
    assert set(CONTEXT_THINKING_LINKS) == {p.name for p in CONTEXT_PROMPTS}


def test_all_context_prompts_have_skill_link():
    assert set(CONTEXT_SKILL_LINKS) == {p.name for p in CONTEXT_PROMPTS}


@pytest.mark.parametrize("prompt_name,skill_refs", CONTEXT_SKILL_LINKS.items())
def test_context_prompt_maps_workflow_skill(prompt_name: str, skill_refs: tuple[str, ...]):
    preamble = _preamble(CONTEXT_DIR / prompt_name)
    for skill in skill_refs:
        assert skill in preamble, f"{prompt_name} preamble should reference {skill}"


@pytest.mark.parametrize("prompt_name,skill_refs", CONTEXT_SKILL_LINKS.items())
def test_context_prompt_primary_surfaces_match_skill_links(
    prompt_name: str, skill_refs: tuple[str, ...]
):
    preamble = _preamble(CONTEXT_DIR / prompt_name)
    listed = _primary_workflow_surfaces_skills(preamble)
    assert listed == tuple(sorted(skill_refs)), (
        f"{prompt_name} Primary workflow surface {listed} != {skill_refs}"
    )


def test_thinking_lens_files_exist_for_context_links():
    linked = {ref for refs in CONTEXT_THINKING_LINKS.values() for ref in refs}
    for ref in linked:
        assert (LIBRARY_ROOT / ref).is_file(), f"missing thinking lens file {ref}"

@pytest.mark.parametrize("prompt_name,thinking_refs", DOMAIN_THINKING_LINKS.items())
def test_domain_prompt_links_thinking_lens(prompt_name: str, thinking_refs: tuple[str, ...]):
    path = DOMAIN_DIR / prompt_name
    preamble = _preamble(path)
    for ref in thinking_refs:
        assert ref in preamble, f"{prompt_name} preamble should reference {ref}"


def test_all_domain_prompts_have_thinking_cross_link():
    assert set(DOMAIN_THINKING_LINKS) == {p.name for p in DOMAIN_PROMPTS}


def test_all_domain_prompts_have_skill_link():
    assert set(DOMAIN_SKILL_LINKS) == {p.name for p in DOMAIN_PROMPTS}


@pytest.mark.parametrize("prompt_name,skill_refs", DOMAIN_SKILL_LINKS.items())
def test_domain_prompt_maps_workflow_skill(prompt_name: str, skill_refs: tuple[str, ...]):
    preamble = _preamble(DOMAIN_DIR / prompt_name)
    for skill in skill_refs:
        assert skill in preamble, f"{prompt_name} preamble should reference {skill}"


@pytest.mark.parametrize("prompt_name,skill_refs", DOMAIN_SKILL_LINKS.items())
def test_domain_prompt_primary_surfaces_match_skill_links(
    prompt_name: str, skill_refs: tuple[str, ...]
):
    preamble = _preamble(DOMAIN_DIR / prompt_name)
    listed = _primary_workflow_surfaces_skills(preamble)
    assert listed == tuple(sorted(skill_refs)), (
        f"{prompt_name} Primary workflow surface {listed} != {skill_refs}"
    )


def test_thinking_lens_files_exist_for_domain_links():
    linked = {ref for refs in DOMAIN_THINKING_LINKS.values() for ref in refs}
    for ref in linked:
        assert (LIBRARY_ROOT / ref).is_file(), f"missing thinking lens file {ref}"

@pytest.mark.parametrize("prompt_name,thinking_refs", REPO_THINKING_LINKS.items())
def test_repo_prompt_links_thinking_lens(prompt_name: str, thinking_refs: tuple[str, ...]):
    path = REPO_DIR / prompt_name
    preamble = _preamble(path)
    for ref in thinking_refs:
        assert ref in preamble, f"{prompt_name} preamble should reference {ref}"


def test_all_repo_prompts_have_thinking_cross_link():
    assert set(REPO_THINKING_LINKS) == {p.name for p in REPO_PROMPTS}


def test_all_repo_prompts_have_skill_link():
    assert set(REPO_SKILL_LINKS) == {p.name for p in REPO_PROMPTS}


@pytest.mark.parametrize("prompt_name,skill_refs", REPO_SKILL_LINKS.items())
def test_repo_prompt_maps_workflow_skill(prompt_name: str, skill_refs: tuple[str, ...]):
    preamble = _preamble(REPO_DIR / prompt_name)
    for skill in skill_refs:
        assert skill in preamble, f"{prompt_name} preamble should reference {skill}"


@pytest.mark.parametrize("prompt_name,skill_refs", REPO_SKILL_LINKS.items())
def test_repo_prompt_primary_surfaces_match_skill_links(
    prompt_name: str, skill_refs: tuple[str, ...]
):
    preamble = _preamble(REPO_DIR / prompt_name)
    listed = _primary_workflow_surfaces_skills(preamble)
    assert listed == tuple(sorted(skill_refs)), (
        f"{prompt_name} Primary workflow surface {listed} != {skill_refs}"
    )


def test_thinking_lens_files_exist_for_repo_links():
    linked = {ref for refs in REPO_THINKING_LINKS.values() for ref in refs}
    for ref in linked:
        assert (LIBRARY_ROOT / ref).is_file(), f"missing thinking lens file {ref}"
