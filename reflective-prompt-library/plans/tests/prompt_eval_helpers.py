"""Shared helpers for composable prompt eval_harness anti-drift tests."""

import re
from pathlib import Path

HUMAN_REVIEW_HEADING = re.compile(r"^## Human Review\s*$", re.MULTILINE)


def prompt_preamble(prompt_path: Path) -> str:
    return prompt_path.read_text(encoding="utf-8").split("```", 1)[0]


def has_human_review_preamble(prompt_path: Path) -> bool:
    return bool(HUMAN_REVIEW_HEADING.search(prompt_preamble(prompt_path)))


def prompts_with_human_review(prompts: tuple[Path, ...]) -> tuple[Path, ...]:
    return tuple(p for p in prompts if has_human_review_preamble(p))


def assert_human_review_preamble(prompt_path: Path) -> None:
    """Human Review sections must live in preamble and route to reflective-risk."""
    preamble = prompt_preamble(prompt_path)
    assert has_human_review_preamble(prompt_path), (
        f"{prompt_path.name} missing ## Human Review preamble outside template block"
    )
    assert "reflective-risk" in preamble, (
        f"{prompt_path.name} Human Review should route to reflective-risk"
    )


def assert_human_review_required_matches_detection(
    required: frozenset[str],
    prompts: tuple[Path, ...],
) -> None:
    """Frozen required set must match prompts that declare ## Human Review in preambles."""
    detected = {p.name for p in prompts_with_human_review(prompts)}
    assert detected == required, (
        f"detected Human Review preambles {sorted(detected)} "
        f"!= frozen required {sorted(required)}"
    )


def assert_human_review_exempt_have_no_preamble_section(
    exempt: frozenset[str],
    prompts: tuple[Path, ...],
) -> None:
    """Exempt prompts keep Human Review cues in fenced templates only."""
    by_name = {p.name: p for p in prompts}
    for name in sorted(exempt):
        assert not has_human_review_preamble(by_name[name]), (
            f"{name} should not declare ## Human Review in preamble"
        )


def assert_human_review_sets_partition(
    all_names: frozenset[str],
    required: frozenset[str],
    exempt: frozenset[str],
) -> None:
    """Required + exempt sets must cover all prompts without overlap."""
    assert required | exempt == all_names, (
        f"required ∪ exempt {sorted(required | exempt)} != all prompts {sorted(all_names)}"
    )
    assert not required & exempt, "required and exempt Human Review sets must not overlap"
