"""Cross-category Primary workflow surface / thinking-lens link registry anti-drift."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_CATEGORIES  # noqa: E402
from test_prompt_cross_links import (  # noqa: E402
    AGENT_PROMPTS,
    AGENT_SKILL_LINKS,
    AGENT_THINKING_LINKS,
    CONTEXT_PROMPTS,
    CONTEXT_SKILL_LINKS,
    CONTEXT_THINKING_LINKS,
    CORE_PROMPTS,
    CORE_SKILL_LINKS,
    CORE_THINKING_LINKS,
    DOMAIN_PROMPTS,
    DOMAIN_SKILL_LINKS,
    DOMAIN_THINKING_LINKS,
    ENGINEERING_PROMPTS,
    ENGINEERING_SKILL_LINKS,
    ENGINEERING_THINKING_LINKS,
    REPO_PROMPTS,
    REPO_SKILL_LINKS,
    REPO_THINKING_LINKS,
    THINKING_LENS_SKILL_CONSUMERS,
    THINKING_PROMPTS,
)

LIBRARY_ROOT = Path(__file__).parent.parent.parent

CROSS_LINK_CATEGORY_REGISTRY = (
    ("00-core", CORE_PROMPTS, CORE_SKILL_LINKS, CORE_THINKING_LINKS),
    (
        "02-engineering",
        ENGINEERING_PROMPTS,
        ENGINEERING_SKILL_LINKS,
        ENGINEERING_THINKING_LINKS,
    ),
    (
        "03-context",
        CONTEXT_PROMPTS,
        CONTEXT_SKILL_LINKS,
        CONTEXT_THINKING_LINKS,
    ),
    ("04-agent", AGENT_PROMPTS, AGENT_SKILL_LINKS, AGENT_THINKING_LINKS),
    (
        "05-domain",
        DOMAIN_PROMPTS,
        DOMAIN_SKILL_LINKS,
        DOMAIN_THINKING_LINKS,
    ),
    ("06-repo", REPO_PROMPTS, REPO_SKILL_LINKS, REPO_THINKING_LINKS),
)


def test_cross_link_registry_lists_composable_categories_except_thinking():
    assert tuple(cat for cat, *_ in CROSS_LINK_CATEGORY_REGISTRY) == tuple(
        c for c in PROMPT_LIBRARY_CATEGORIES if c != "01-thinking"
    )


@pytest.mark.parametrize(
    "category,prompts,skill_links,thinking_links",
    CROSS_LINK_CATEGORY_REGISTRY,
    ids=[row[0] for row in CROSS_LINK_CATEGORY_REGISTRY],
)
def test_cross_link_registry_category_dicts_cover_prompts(
    category: str,
    prompts: tuple[Path, ...],
    skill_links: dict[str, tuple[str, ...]],
    thinking_links: dict[str, tuple[str, ...]],
):
    prompt_names = {p.name for p in prompts}
    assert set(skill_links) == prompt_names, f"{category}: SKILL_LINKS keys != prompts"
    assert set(thinking_links) == prompt_names, (
        f"{category}: THINKING_LINKS keys != prompts"
    )


def test_cross_link_registry_library_wide_unique_filenames():
    basenames: list[str] = []
    for _category, prompts, _skill_links, _thinking_links in CROSS_LINK_CATEGORY_REGISTRY:
        basenames.extend(p.name for p in prompts)
    basenames.extend(p.name for p in THINKING_PROMPTS)
    assert len(basenames) == len(frozenset(basenames)), (
        "duplicate prompt basenames across categories"
    )


def test_cross_link_registry_matches_library_glob():
    globbed: list[Path] = []
    for category in PROMPT_LIBRARY_CATEGORIES:
        globbed.extend(sorted((LIBRARY_ROOT / category).glob("*.md")))
    registry_paths = [
        p
        for _category, prompts, _skill_links, _thinking_links in CROSS_LINK_CATEGORY_REGISTRY
        for p in prompts
    ]
    registry_paths.extend(THINKING_PROMPTS)
    assert sorted(globbed) == sorted(registry_paths)


def test_thinking_lenses_tracked_in_consumer_map():
    expected = {f"01-thinking/{path.name}" for path in THINKING_PROMPTS}
    assert set(THINKING_LENS_SKILL_CONSUMERS) == expected
