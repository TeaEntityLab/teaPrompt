"""Cross-category library registry helper anti-drift."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_CATEGORIES,
    PROMPT_LIBRARY_ROOT,
    assert_library_wide_unique_basenames,
    assert_registry_matches_library_glob,
    category_prompt_dir,
    library_skills_dir,
    sorted_all_library_prompts,
    sorted_category_prompts,
)
from test_agent_prompts_eval_harness import AGENT_PROMPTS  # noqa: E402
from test_context_prompts_eval_harness import CONTEXT_PROMPTS  # noqa: E402
from test_core_prompts_eval_harness import CORE_PROMPTS  # noqa: E402
from test_domain_prompts_eval_harness import DOMAIN_PROMPTS  # noqa: E402
from test_engineering_prompts_eval_harness import ENGINEERING_PROMPTS  # noqa: E402
from test_repo_prompts_eval_harness import REPO_PROMPTS  # noqa: E402
from test_thinking_prompts_eval_harness import THINKING_PROMPTS  # noqa: E402

LIBRARY_REGISTRY_MODULES = (
    "test_human_review_library_registry",
    "test_prompt_category_paths_library_registry",
    "test_prompt_contract_library_registry",
    "test_prompt_eval_harness_fixture_library_registry",
    "test_prompt_eval_harness_score_library_registry",
    "test_prompt_primary_workflow_surface_library_registry",
    "test_prompt_skill_links_library_registry",
    "test_prompt_workflow_skill_reference_library_registry",
    "test_workflow_skill_coverage_library_registry",
)

ALL_CATEGORY_PROMPTS = (
    CORE_PROMPTS,
    THINKING_PROMPTS,
    ENGINEERING_PROMPTS,
    CONTEXT_PROMPTS,
    AGENT_PROMPTS,
    DOMAIN_PROMPTS,
    REPO_PROMPTS,
)


def test_sorted_all_library_prompts_matches_per_category_globs():
    manual: list[Path] = []
    for category in PROMPT_LIBRARY_CATEGORIES:
        manual.extend(sorted_category_prompts(category))
    assert sorted_all_library_prompts() == tuple(manual)


def test_library_skills_dir_resolves_under_prompt_library_root():
    assert library_skills_dir().parent == PROMPT_LIBRARY_ROOT
    assert library_skills_dir().name == "skills"
    assert library_skills_dir().is_dir()


@pytest.mark.parametrize("category", PROMPT_LIBRARY_CATEGORIES)
def test_category_prompt_dir_resolves_markdown_category(category: str):
    category_dir = category_prompt_dir(category)
    assert category_dir.parent == PROMPT_LIBRARY_ROOT
    assert category_dir.name == category
    assert sorted_category_prompts(category) == tuple(
        sorted(category_dir.glob("*.md"))
    )


def test_registry_helpers_cover_all_harness_prompt_tuples():
    registry_paths = [p for prompts in ALL_CATEGORY_PROMPTS for p in prompts]
    assert_library_wide_unique_basenames(registry_paths)
    assert_registry_matches_library_glob(registry_paths)


@pytest.mark.parametrize("module_name", LIBRARY_REGISTRY_MODULES)
def test_library_registry_modules_use_shared_glob_helpers(module_name: str):
    source = (Path(__file__).parent / f"{module_name}.py").read_text(encoding="utf-8")
    assert "LIBRARY_ROOT = Path(__file__).parent.parent.parent" not in source
    assert "assert_library_wide_unique_basenames" in source
    assert "assert_registry_matches_library_glob" in source
    assert "(LIBRARY_ROOT / category).glob" not in source
