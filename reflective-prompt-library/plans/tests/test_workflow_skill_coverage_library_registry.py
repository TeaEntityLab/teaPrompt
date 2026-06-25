"""Cross-category workflow skill coverage registry anti-drift."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_CATEGORIES,
    assert_category_workflow_skill_coverage,
    assert_library_wide_unique_basenames,
    assert_registry_matches_library_glob,
)
from test_agent_prompts_eval_harness import (  # noqa: E402
    AGENT_COVER_WORKFLOW_SKILLS,
    AGENT_PROMPTS,
)
from test_context_prompts_eval_harness import (  # noqa: E402
    CONTEXT_COVER_WORKFLOW_SKILLS,
    CONTEXT_PROMPTS,
)
from test_core_prompts_eval_harness import (  # noqa: E402
    CORE_COVER_WORKFLOW_SKILLS,
    CORE_PROMPTS,
)
from test_domain_prompts_eval_harness import (  # noqa: E402
    DOMAIN_COVER_WORKFLOW_SKILLS,
    DOMAIN_PROMPTS,
)
from test_engineering_prompts_eval_harness import (  # noqa: E402
    ENGINEERING_COVER_WORKFLOW_SKILLS,
    ENGINEERING_PROMPTS,
)
from test_repo_prompts_eval_harness import (  # noqa: E402
    REPO_COVER_WORKFLOW_SKILLS,
    REPO_PROMPTS,
)
from test_thinking_prompts_eval_harness import (  # noqa: E402
    THINKING_COVER_WORKFLOW_SKILLS,
    THINKING_PROMPTS,
)


WORKFLOW_COVERAGE_CATEGORY_REGISTRY = (
    ("00-core", CORE_PROMPTS, CORE_COVER_WORKFLOW_SKILLS),
    ("01-thinking", THINKING_PROMPTS, THINKING_COVER_WORKFLOW_SKILLS),
    (
        "02-engineering",
        ENGINEERING_PROMPTS,
        ENGINEERING_COVER_WORKFLOW_SKILLS,
    ),
    ("03-context", CONTEXT_PROMPTS, CONTEXT_COVER_WORKFLOW_SKILLS),
    ("04-agent", AGENT_PROMPTS, AGENT_COVER_WORKFLOW_SKILLS),
    ("05-domain", DOMAIN_PROMPTS, DOMAIN_COVER_WORKFLOW_SKILLS),
    ("06-repo", REPO_PROMPTS, REPO_COVER_WORKFLOW_SKILLS),
)


def test_workflow_coverage_registry_lists_all_prompt_categories():
    assert tuple(cat for cat, *_ in WORKFLOW_COVERAGE_CATEGORY_REGISTRY) == PROMPT_LIBRARY_CATEGORIES


@pytest.mark.parametrize(
    "category,prompts,cover_skills",
    WORKFLOW_COVERAGE_CATEGORY_REGISTRY,
    ids=[row[0] for row in WORKFLOW_COVERAGE_CATEGORY_REGISTRY],
)
def test_workflow_coverage_registry_category_frozen_tuple(
    category: str,
    prompts: tuple[Path, ...],
    cover_skills: tuple[str, ...],
):
    assert isinstance(cover_skills, tuple), f"{category}: cover skills must be tuple"
    if category == "01-thinking":
        assert cover_skills == (), f"{category}: thinking uses consumer graph, not category corpus"
        return
    assert len(cover_skills) > 0, f"{category}: empty cover tuple"
    assert_category_workflow_skill_coverage(prompts, cover_skills, category)


def test_workflow_coverage_registry_library_wide_unique_filenames():
    registry_paths = [p for _category, prompts, _cover_skills in WORKFLOW_COVERAGE_CATEGORY_REGISTRY for p in prompts]
    assert_library_wide_unique_basenames(registry_paths)


def test_workflow_coverage_registry_matches_library_glob():
    registry_paths = [p for _category, prompts, _cover_skills in WORKFLOW_COVERAGE_CATEGORY_REGISTRY for p in prompts]
    assert_registry_matches_library_glob(registry_paths)
