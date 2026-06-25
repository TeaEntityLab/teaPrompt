"""Cross-category eval_harness contract heading registry anti-drift."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_CONTRACT_HEADINGS,
    PROMPT_EVAL_MIN_SCORE,
    PROMPT_LIBRARY_CATEGORIES,
    assert_prompt_contract_headings,
)
from test_agent_prompts_eval_harness import (  # noqa: E402
    AGENT_PROMPTS,
    MIN_SCORE as AGENT_MIN_SCORE,
    REQUIRED_HEADINGS as AGENT_HEADINGS,
)
from test_context_prompts_eval_harness import (  # noqa: E402
    CONTEXT_PROMPTS,
    MIN_SCORE as CONTEXT_MIN_SCORE,
    REQUIRED_HEADINGS as CONTEXT_HEADINGS,
)
from test_core_prompts_eval_harness import (  # noqa: E402
    CORE_PROMPTS,
    MIN_SCORE as CORE_MIN_SCORE,
    REQUIRED_HEADINGS as CORE_HEADINGS,
)
from test_domain_prompts_eval_harness import (  # noqa: E402
    DOMAIN_PROMPTS,
    MIN_SCORE as DOMAIN_MIN_SCORE,
    REQUIRED_HEADINGS as DOMAIN_HEADINGS,
)
from test_engineering_prompts_eval_harness import (  # noqa: E402
    ENGINEERING_PROMPTS,
    MIN_SCORE as ENGINEERING_MIN_SCORE,
    REQUIRED_HEADINGS as ENGINEERING_HEADINGS,
)
from test_repo_prompts_eval_harness import (  # noqa: E402
    REPO_PROMPTS,
    MIN_SCORE as REPO_MIN_SCORE,
    REQUIRED_HEADINGS as REPO_HEADINGS,
)
from test_thinking_prompts_eval_harness import (  # noqa: E402
    MIN_SCORE as THINKING_MIN_SCORE,
    REQUIRED_HEADINGS as THINKING_HEADINGS,
    THINKING_PROMPTS,
)

LIBRARY_ROOT = Path(__file__).parent.parent.parent

CONTRACT_CATEGORY_REGISTRY = (
    ("00-core", CORE_PROMPTS, CORE_HEADINGS, CORE_MIN_SCORE),
    ("01-thinking", THINKING_PROMPTS, THINKING_HEADINGS, THINKING_MIN_SCORE),
    (
        "02-engineering",
        ENGINEERING_PROMPTS,
        ENGINEERING_HEADINGS,
        ENGINEERING_MIN_SCORE,
    ),
    ("03-context", CONTEXT_PROMPTS, CONTEXT_HEADINGS, CONTEXT_MIN_SCORE),
    ("04-agent", AGENT_PROMPTS, AGENT_HEADINGS, AGENT_MIN_SCORE),
    ("05-domain", DOMAIN_PROMPTS, DOMAIN_HEADINGS, DOMAIN_MIN_SCORE),
    ("06-repo", REPO_PROMPTS, REPO_HEADINGS, REPO_MIN_SCORE),
)


def test_contract_registry_lists_all_prompt_categories():
    assert tuple(cat for cat, *_ in CONTRACT_CATEGORY_REGISTRY) == PROMPT_LIBRARY_CATEGORIES


@pytest.mark.parametrize(
    "category,prompts,headings,min_score",
    CONTRACT_CATEGORY_REGISTRY,
    ids=[row[0] for row in CONTRACT_CATEGORY_REGISTRY],
)
def test_contract_registry_category_uses_shared_constants(
    category: str,
    prompts: tuple[Path, ...],
    headings: tuple[str, ...],
    min_score: float,
):
    assert headings is PROMPT_CONTRACT_HEADINGS, f"{category}: headings not shared constant"
    assert min_score == PROMPT_EVAL_MIN_SCORE, f"{category}: MIN_SCORE drift"
    assert len(prompts) > 0, f"{category}: empty prompt tuple"


def test_contract_registry_library_wide_unique_filenames():
    basenames: list[str] = []
    for _category, prompts, _headings, _min_score in CONTRACT_CATEGORY_REGISTRY:
        basenames.extend(p.name for p in prompts)
    assert len(basenames) == len(frozenset(basenames)), (
        "duplicate prompt basenames across categories"
    )


def test_contract_registry_matches_library_glob():
    globbed: list[Path] = []
    for category in PROMPT_LIBRARY_CATEGORIES:
        globbed.extend(sorted((LIBRARY_ROOT / category).glob("*.md")))
    registry_paths = [
        p for _category, prompts, _headings, _min_score in CONTRACT_CATEGORY_REGISTRY for p in prompts
    ]
    assert sorted(globbed) == sorted(registry_paths)


def test_contract_registry_all_prompts_have_preamble_headings():
    for category, prompts, _headings, _min_score in CONTRACT_CATEGORY_REGISTRY:
        for prompt_path in prompts:
            try:
                assert_prompt_contract_headings(prompt_path)
            except AssertionError as exc:
                raise AssertionError(f"{category}/{prompt_path.name}: {exc}") from exc
