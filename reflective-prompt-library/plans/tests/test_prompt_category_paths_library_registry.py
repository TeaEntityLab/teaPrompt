"""Cross-category prompt category path registry anti-drift."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_CATEGORIES,
    PROMPT_LIBRARY_ROOT,
    category_prompt_dir,
    sorted_category_prompts,
    assert_library_wide_unique_basenames,
    assert_registry_matches_library_glob,
)
from test_agent_prompts_eval_harness import AGENT_DIR, AGENT_PROMPTS  # noqa: E402
from test_context_prompts_eval_harness import CONTEXT_DIR, CONTEXT_PROMPTS  # noqa: E402
from test_core_prompts_eval_harness import CORE_DIR, CORE_PROMPTS  # noqa: E402
from test_domain_prompts_eval_harness import DOMAIN_DIR, DOMAIN_PROMPTS  # noqa: E402
from test_engineering_prompts_eval_harness import ENGINEERING_DIR, ENGINEERING_PROMPTS  # noqa: E402
from test_repo_prompts_eval_harness import REPO_DIR, REPO_PROMPTS  # noqa: E402
from test_thinking_prompts_eval_harness import THINKING_DIR, THINKING_PROMPTS  # noqa: E402

CATEGORY_PATH_REGISTRY = (
    ("00-core", CORE_DIR, CORE_PROMPTS),
    ("01-thinking", THINKING_DIR, THINKING_PROMPTS),
    ("02-engineering", ENGINEERING_DIR, ENGINEERING_PROMPTS),
    ("03-context", CONTEXT_DIR, CONTEXT_PROMPTS),
    ("04-agent", AGENT_DIR, AGENT_PROMPTS),
    ("05-domain", DOMAIN_DIR, DOMAIN_PROMPTS),
    ("06-repo", REPO_DIR, REPO_PROMPTS),
)


def test_category_path_registry_lists_all_prompt_categories():
    assert tuple(cat for cat, *_ in CATEGORY_PATH_REGISTRY) == PROMPT_LIBRARY_CATEGORIES


@pytest.mark.parametrize(
    "category,category_dir,prompts",
    CATEGORY_PATH_REGISTRY,
    ids=[row[0] for row in CATEGORY_PATH_REGISTRY],
)
def test_category_path_registry_uses_shared_helpers(
    category: str,
    category_dir: Path,
    prompts: tuple[Path, ...],
):
    assert category_dir == category_prompt_dir(category)
    assert prompts == sorted_category_prompts(category)
    assert category_dir.parent == PROMPT_LIBRARY_ROOT
    assert len(prompts) > 0, f"{category}: empty prompt tuple"


def test_category_path_registry_library_wide_unique_filenames():
    registry_paths = [p for _category, _category_dir, prompts in CATEGORY_PATH_REGISTRY for p in prompts]
    assert_library_wide_unique_basenames(registry_paths)


def test_category_path_registry_matches_library_glob():
    registry_paths = [p for _category, _category_dir, prompts in CATEGORY_PATH_REGISTRY for p in prompts]
    assert_registry_matches_library_glob(registry_paths)
