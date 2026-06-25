"""Cross-category Human Review registry anti-drift for composable prompt library."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_CATEGORIES,
    prompts_with_human_review,
    assert_library_wide_unique_basenames,
    assert_registry_matches_library_glob,
)
from test_agent_prompts_eval_harness import (  # noqa: E402
    AGENT_HUMAN_REVIEW_EXEMPT,
    AGENT_HUMAN_REVIEW_REQUIRED,
    AGENT_PROMPTS,
)
from test_context_prompts_eval_harness import (  # noqa: E402
    CONTEXT_HUMAN_REVIEW_EXEMPT,
    CONTEXT_HUMAN_REVIEW_REQUIRED,
    CONTEXT_PROMPTS,
)
from test_core_prompts_eval_harness import (  # noqa: E402
    CORE_HUMAN_REVIEW_EXEMPT,
    CORE_HUMAN_REVIEW_REQUIRED,
    CORE_PROMPTS,
)
from test_domain_prompts_eval_harness import (  # noqa: E402
    DOMAIN_HUMAN_REVIEW_EXEMPT,
    DOMAIN_HUMAN_REVIEW_REQUIRED,
    DOMAIN_PROMPTS,
)
from test_engineering_prompts_eval_harness import (  # noqa: E402
    ENGINEERING_HUMAN_REVIEW_EXEMPT,
    ENGINEERING_HUMAN_REVIEW_REQUIRED,
    ENGINEERING_PROMPTS,
)
from test_repo_prompts_eval_harness import (  # noqa: E402
    REPO_HUMAN_REVIEW_EXEMPT,
    REPO_HUMAN_REVIEW_REQUIRED,
    REPO_PROMPTS,
)
from test_thinking_prompts_eval_harness import (  # noqa: E402
    THINKING_HUMAN_REVIEW_EXEMPT,
    THINKING_HUMAN_REVIEW_REQUIRED,
    THINKING_PROMPTS,
)


HUMAN_REVIEW_CATEGORY_REGISTRY = (
    ("00-core", CORE_PROMPTS, CORE_HUMAN_REVIEW_REQUIRED, CORE_HUMAN_REVIEW_EXEMPT),
    (
        "01-thinking",
        THINKING_PROMPTS,
        THINKING_HUMAN_REVIEW_REQUIRED,
        THINKING_HUMAN_REVIEW_EXEMPT,
    ),
    (
        "02-engineering",
        ENGINEERING_PROMPTS,
        ENGINEERING_HUMAN_REVIEW_REQUIRED,
        ENGINEERING_HUMAN_REVIEW_EXEMPT,
    ),
    (
        "03-context",
        CONTEXT_PROMPTS,
        CONTEXT_HUMAN_REVIEW_REQUIRED,
        CONTEXT_HUMAN_REVIEW_EXEMPT,
    ),
    ("04-agent", AGENT_PROMPTS, AGENT_HUMAN_REVIEW_REQUIRED, AGENT_HUMAN_REVIEW_EXEMPT),
    (
        "05-domain",
        DOMAIN_PROMPTS,
        DOMAIN_HUMAN_REVIEW_REQUIRED,
        DOMAIN_HUMAN_REVIEW_EXEMPT,
    ),
    ("06-repo", REPO_PROMPTS, REPO_HUMAN_REVIEW_REQUIRED, REPO_HUMAN_REVIEW_EXEMPT),
)


def test_human_review_registry_lists_all_prompt_categories():
    assert tuple(cat for cat, *_ in HUMAN_REVIEW_CATEGORY_REGISTRY) == PROMPT_LIBRARY_CATEGORIES


@pytest.mark.parametrize(
    "category,prompts,required,exempt",
    HUMAN_REVIEW_CATEGORY_REGISTRY,
    ids=[row[0] for row in HUMAN_REVIEW_CATEGORY_REGISTRY],
)
def test_human_review_registry_category_partition(
    category: str, prompts: tuple[Path, ...], required: frozenset[str], exempt: frozenset[str]
):
    all_names = frozenset(p.name for p in prompts)
    assert required | exempt == all_names, f"{category}: required ∪ exempt != all prompts"
    assert not required & exempt, f"{category}: required and exempt overlap"


def test_human_review_registry_library_wide_unique_filenames():
    registry_paths = [p for _category, prompts, _required, _exempt in HUMAN_REVIEW_CATEGORY_REGISTRY for p in prompts]
    assert_library_wide_unique_basenames(registry_paths)


def test_human_review_registry_matches_library_glob():
    registry_paths = [p for _category, prompts, _required, _exempt in HUMAN_REVIEW_CATEGORY_REGISTRY for p in prompts]
    assert_registry_matches_library_glob(registry_paths)


def test_human_review_registry_required_union_matches_detection():
    detected: set[str] = set()
    for category, prompts, required, _exempt in HUMAN_REVIEW_CATEGORY_REGISTRY:
        category_detected = {p.name for p in prompts_with_human_review(prompts)}
        assert category_detected == required, (
            f"{category}: detected HR preambles {sorted(category_detected)} "
            f"!= frozen required {sorted(required)}"
        )
        detected |= category_detected
    assert len(detected) > 0
