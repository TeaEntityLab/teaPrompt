"""Cross-category eval_harness score floor registry anti-drift."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from eval_harness import EvalHarness  # noqa: E402
from prompt_eval_helpers import (  # noqa: E402
    PROMPT_EVAL_MIN_SCORE,
    PROMPT_LIBRARY_CATEGORIES,
    PROMPT_LIBRARY_REPO_ROOT,
    assert_prompt_meets_eval_harness_floor,
    make_category_eval_harness_fixture,
    assert_library_wide_unique_basenames,
    assert_registry_matches_library_glob,
)
from test_agent_prompts_eval_harness import (  # noqa: E402
    AGENT_PROMPTS,
    MIN_SCORE as AGENT_MIN_SCORE,
)
from test_context_prompts_eval_harness import (  # noqa: E402
    CONTEXT_PROMPTS,
    MIN_SCORE as CONTEXT_MIN_SCORE,
)
from test_core_prompts_eval_harness import (  # noqa: E402
    CORE_PROMPTS,
    MIN_SCORE as CORE_MIN_SCORE,
)
from test_domain_prompts_eval_harness import (  # noqa: E402
    DOMAIN_PROMPTS,
    MIN_SCORE as DOMAIN_MIN_SCORE,
)
from test_engineering_prompts_eval_harness import (  # noqa: E402
    ENGINEERING_PROMPTS,
    MIN_SCORE as ENGINEERING_MIN_SCORE,
)
from test_repo_prompts_eval_harness import (  # noqa: E402
    MIN_SCORE as REPO_MIN_SCORE,
    REPO_PROMPTS,
)
from test_thinking_prompts_eval_harness import (  # noqa: E402
    MIN_SCORE as THINKING_MIN_SCORE,
    THINKING_PROMPTS,
)

REPO_ROOT = PROMPT_LIBRARY_REPO_ROOT

SCORE_CATEGORY_REGISTRY = (
    ("00-core", CORE_PROMPTS, CORE_MIN_SCORE),
    ("01-thinking", THINKING_PROMPTS, THINKING_MIN_SCORE),
    (
        "02-engineering",
        ENGINEERING_PROMPTS,
        ENGINEERING_MIN_SCORE,
    ),
    ("03-context", CONTEXT_PROMPTS, CONTEXT_MIN_SCORE),
    ("04-agent", AGENT_PROMPTS, AGENT_MIN_SCORE),
    ("05-domain", DOMAIN_PROMPTS, DOMAIN_MIN_SCORE),
    ("06-repo", REPO_PROMPTS, REPO_MIN_SCORE),
)


harness = make_category_eval_harness_fixture(REPO_ROOT)

def test_score_registry_lists_all_prompt_categories():
    assert tuple(cat for cat, *_ in SCORE_CATEGORY_REGISTRY) == PROMPT_LIBRARY_CATEGORIES


@pytest.mark.parametrize(
    "category,prompts,min_score",
    SCORE_CATEGORY_REGISTRY,
    ids=[row[0] for row in SCORE_CATEGORY_REGISTRY],
)
def test_score_registry_category_uses_shared_min_score(
    category: str,
    prompts: tuple[Path, ...],
    min_score: float,
):
    assert min_score == PROMPT_EVAL_MIN_SCORE, f"{category}: MIN_SCORE drift"
    assert len(prompts) > 0, f"{category}: empty prompt tuple"


def test_score_registry_library_wide_unique_filenames():
    registry_paths = [p for _category, prompts, _min_score in SCORE_CATEGORY_REGISTRY for p in prompts]
    assert_library_wide_unique_basenames(registry_paths)


def test_score_registry_matches_library_glob():
    registry_paths = [p for _category, prompts, _min_score in SCORE_CATEGORY_REGISTRY for p in prompts]
    assert_registry_matches_library_glob(registry_paths)


def test_score_registry_all_prompts_meet_floor(harness: EvalHarness):
    for category, prompts, min_score in SCORE_CATEGORY_REGISTRY:
        for prompt_path in prompts:
            try:
                assert_prompt_meets_eval_harness_floor(
                    prompt_path, harness, REPO_ROOT, min_score
                )
            except AssertionError as exc:
                raise AssertionError(
                    f"{category}/{prompt_path.name}: {exc}"
                ) from exc
