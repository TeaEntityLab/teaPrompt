"""Cross-category workflow skill reference registry anti-drift."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_CATEGORIES,
    assert_prompt_references_workflow_skill,
    assert_library_wide_unique_basenames,
    assert_registry_matches_library_glob,
)
from test_agent_prompts_eval_harness import AGENT_PROMPTS  # noqa: E402
from test_context_prompts_eval_harness import CONTEXT_PROMPTS  # noqa: E402
from test_core_prompts_eval_harness import CORE_PROMPTS  # noqa: E402
from test_domain_prompts_eval_harness import DOMAIN_PROMPTS  # noqa: E402
from test_engineering_prompts_eval_harness import ENGINEERING_PROMPTS  # noqa: E402
from test_repo_prompts_eval_harness import REPO_PROMPTS  # noqa: E402
from test_thinking_prompts_eval_harness import THINKING_PROMPTS  # noqa: E402


REFERENCE_CATEGORY_REGISTRY = (
    ("00-core", CORE_PROMPTS),
    ("01-thinking", THINKING_PROMPTS),
    ("02-engineering", ENGINEERING_PROMPTS),
    ("03-context", CONTEXT_PROMPTS),
    ("04-agent", AGENT_PROMPTS),
    ("05-domain", DOMAIN_PROMPTS),
    ("06-repo", REPO_PROMPTS),
)


def test_reference_registry_lists_all_prompt_categories():
    assert tuple(cat for cat, _ in REFERENCE_CATEGORY_REGISTRY) == PROMPT_LIBRARY_CATEGORIES


@pytest.mark.parametrize(
    "category,prompts",
    REFERENCE_CATEGORY_REGISTRY,
    ids=[row[0] for row in REFERENCE_CATEGORY_REGISTRY],
)
def test_reference_registry_category_has_prompts(category: str, prompts: tuple[Path, ...]):
    assert len(prompts) > 0, f"{category}: empty prompt tuple"


def test_reference_registry_library_wide_unique_filenames():
    registry_paths = [p for _category, prompts in REFERENCE_CATEGORY_REGISTRY for p in prompts]
    assert_library_wide_unique_basenames(registry_paths)


def test_reference_registry_matches_library_glob():
    registry_paths = [p for _category, prompts in REFERENCE_CATEGORY_REGISTRY for p in prompts]
    assert_registry_matches_library_glob(registry_paths)


def test_reference_registry_all_prompts_mention_workflow_skill():
    for category, prompts in REFERENCE_CATEGORY_REGISTRY:
        for prompt_path in prompts:
            try:
                assert_prompt_references_workflow_skill(prompt_path)
            except AssertionError as exc:
                raise AssertionError(f"{category}/{prompt_path.name}: {exc}") from exc
