"""Cross-category Primary workflow surface preamble registry anti-drift."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_CATEGORIES,
    SUPPORTING_LENS_PRIMARY_SURFACE_BY_CATEGORY,
    assert_primary_workflow_surface_preamble,
    supporting_lens_exempt_for_category,
)
from test_agent_prompts_eval_harness import AGENT_PROMPTS  # noqa: E402
from test_context_prompts_eval_harness import CONTEXT_PROMPTS  # noqa: E402
from test_core_prompts_eval_harness import CORE_PROMPTS  # noqa: E402
from test_domain_prompts_eval_harness import DOMAIN_PROMPTS  # noqa: E402
from test_engineering_prompts_eval_harness import ENGINEERING_PROMPTS  # noqa: E402
from test_repo_prompts_eval_harness import REPO_PROMPTS  # noqa: E402
from test_thinking_prompts_eval_harness import THINKING_PROMPTS  # noqa: E402

LIBRARY_ROOT = Path(__file__).parent.parent.parent

PRIMARY_SURFACE_CATEGORY_REGISTRY = (
    ("00-core", CORE_PROMPTS, supporting_lens_exempt_for_category("00-core")),
    ("01-thinking", THINKING_PROMPTS, supporting_lens_exempt_for_category("01-thinking")),
    (
        "02-engineering",
        ENGINEERING_PROMPTS,
        supporting_lens_exempt_for_category("02-engineering"),
    ),
    ("03-context", CONTEXT_PROMPTS, supporting_lens_exempt_for_category("03-context")),
    ("04-agent", AGENT_PROMPTS, supporting_lens_exempt_for_category("04-agent")),
    ("05-domain", DOMAIN_PROMPTS, supporting_lens_exempt_for_category("05-domain")),
    ("06-repo", REPO_PROMPTS, supporting_lens_exempt_for_category("06-repo")),
)


def test_primary_surface_registry_lists_all_prompt_categories():
    assert tuple(cat for cat, *_ in PRIMARY_SURFACE_CATEGORY_REGISTRY) == PROMPT_LIBRARY_CATEGORIES


@pytest.mark.parametrize(
    "category,prompts,supporting_exempt",
    PRIMARY_SURFACE_CATEGORY_REGISTRY,
    ids=[row[0] for row in PRIMARY_SURFACE_CATEGORY_REGISTRY],
)
def test_primary_surface_registry_category_exempt_subset(
    category: str,
    prompts: tuple[Path, ...],
    supporting_exempt: frozenset[str],
):
    prompt_names = {p.name for p in prompts}
    assert supporting_exempt <= prompt_names, (
        f"{category}: supporting-lens exempt {sorted(supporting_exempt)} not in prompts"
    )
    assert supporting_exempt == supporting_lens_exempt_for_category(category), (
        f"{category}: registry exempt != SUPPORTING_LENS_PRIMARY_SURFACE_BY_CATEGORY"
    )


def test_primary_surface_registry_supporting_lens_map_keys_are_categories():
    assert set(SUPPORTING_LENS_PRIMARY_SURFACE_BY_CATEGORY) <= set(PROMPT_LIBRARY_CATEGORIES)


def test_primary_surface_registry_library_wide_unique_filenames():
    basenames: list[str] = []
    for _category, prompts, _supporting_exempt in PRIMARY_SURFACE_CATEGORY_REGISTRY:
        basenames.extend(p.name for p in prompts)
    assert len(basenames) == len(frozenset(basenames)), (
        "duplicate prompt basenames across categories"
    )


def test_primary_surface_registry_matches_library_glob():
    globbed: list[Path] = []
    for category in PROMPT_LIBRARY_CATEGORIES:
        globbed.extend(sorted((LIBRARY_ROOT / category).glob("*.md")))
    registry_paths = [
        p for _category, prompts, _supporting_exempt in PRIMARY_SURFACE_CATEGORY_REGISTRY for p in prompts
    ]
    assert sorted(globbed) == sorted(registry_paths)


def test_primary_surface_registry_all_prompts_have_preamble_line():
    for category, prompts, _supporting_exempt in PRIMARY_SURFACE_CATEGORY_REGISTRY:
        for prompt_path in prompts:
            try:
                assert_primary_workflow_surface_preamble(prompt_path, category=category)
            except AssertionError as exc:
                raise AssertionError(f"{category}/{prompt_path.name}: {exc}") from exc
