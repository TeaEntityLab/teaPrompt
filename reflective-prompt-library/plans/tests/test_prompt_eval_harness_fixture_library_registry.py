"""Cross-category eval_harness fixture registry anti-drift."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from prompt_eval_helpers import (  # noqa: E402
    CATEGORY_EVAL_HARNESS_FIXTURE_MARKER,
    PROMPT_LIBRARY_CATEGORIES,
    PROMPT_LIBRARY_REPO_ROOT,
    assert_registry_matches_library_glob,
    assert_library_wide_unique_basenames,
    assert_registry_matches_library_glob,
)
from test_agent_prompts_eval_harness import (  # noqa: E402
    AGENT_PROMPTS,
    REPO_ROOT as AGENT_REPO_ROOT,
    harness as agent_harness,
)
from test_context_prompts_eval_harness import (  # noqa: E402
    CONTEXT_PROMPTS,
    REPO_ROOT as CONTEXT_REPO_ROOT,
    harness as context_harness,
)
from test_core_prompts_eval_harness import (  # noqa: E402
    CORE_PROMPTS,
    REPO_ROOT as CORE_REPO_ROOT,
    harness as core_harness,
)
from test_domain_prompts_eval_harness import (  # noqa: E402
    DOMAIN_PROMPTS,
    REPO_ROOT as DOMAIN_REPO_ROOT,
    harness as domain_harness,
)
from test_engineering_prompts_eval_harness import (  # noqa: E402
    ENGINEERING_PROMPTS,
    REPO_ROOT as ENGINEERING_REPO_ROOT,
    harness as engineering_harness,
)
from test_repo_prompts_eval_harness import (  # noqa: E402
    REPO_PROMPTS,
    REPO_ROOT as REPO_CATEGORY_REPO_ROOT,
    harness as repo_harness,
)
from test_thinking_prompts_eval_harness import (  # noqa: E402
    THINKING_PROMPTS,
    REPO_ROOT as THINKING_REPO_ROOT,
    harness as thinking_harness,
)

HARNESS_FIXTURE_CATEGORY_REGISTRY = (
    ("00-core", CORE_PROMPTS, CORE_REPO_ROOT, core_harness),
    ("01-thinking", THINKING_PROMPTS, THINKING_REPO_ROOT, thinking_harness),
    ("02-engineering", ENGINEERING_PROMPTS, ENGINEERING_REPO_ROOT, engineering_harness),
    ("03-context", CONTEXT_PROMPTS, CONTEXT_REPO_ROOT, context_harness),
    ("04-agent", AGENT_PROMPTS, AGENT_REPO_ROOT, agent_harness),
    ("05-domain", DOMAIN_PROMPTS, DOMAIN_REPO_ROOT, domain_harness),
    ("06-repo", REPO_PROMPTS, REPO_CATEGORY_REPO_ROOT, repo_harness),
)


def test_harness_fixture_registry_lists_all_prompt_categories():
    assert (
        tuple(cat for cat, *_ in HARNESS_FIXTURE_CATEGORY_REGISTRY)
        == PROMPT_LIBRARY_CATEGORIES
    )


@pytest.mark.parametrize(
    "category,prompts,repo_root,harness_fixture",
    HARNESS_FIXTURE_CATEGORY_REGISTRY,
    ids=[row[0] for row in HARNESS_FIXTURE_CATEGORY_REGISTRY],
)
def test_harness_fixture_registry_category_uses_shared_constants(
    category: str,
    prompts: tuple[Path, ...],
    repo_root: str,
    harness_fixture,
):
    assert repo_root is PROMPT_LIBRARY_REPO_ROOT, f"{category}: REPO_ROOT drift"
    assert getattr(harness_fixture, CATEGORY_EVAL_HARNESS_FIXTURE_MARKER, False), (
        f"{category}: harness not from make_category_eval_harness_fixture"
    )
    assert len(prompts) > 0, f"{category}: empty prompt tuple"


def test_harness_fixture_registry_library_wide_unique_filenames():
    registry_paths = [p for _category, prompts, _repo_root, _harness_fixture in HARNESS_FIXTURE_CATEGORY_REGISTRY for p in prompts]
    assert_library_wide_unique_basenames(registry_paths)


def test_harness_fixture_registry_matches_library_glob():
    registry_paths = [
        p
        for _category, prompts, _repo_root, _harness_fixture
        in HARNESS_FIXTURE_CATEGORY_REGISTRY
        for p in prompts
    ]
    assert_registry_matches_library_glob(registry_paths)
