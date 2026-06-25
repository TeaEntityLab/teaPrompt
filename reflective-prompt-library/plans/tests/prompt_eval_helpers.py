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
