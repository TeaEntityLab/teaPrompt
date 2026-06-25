"""Shared helpers for composable prompt eval_harness anti-drift tests."""

import re
from pathlib import Path

HUMAN_REVIEW_HEADING = re.compile(r"^## Human Review\s*$", re.MULTILINE)

PROMPT_LIBRARY_CATEGORIES = (
    "00-core",
    "01-thinking",
    "02-engineering",
    "03-context",
    "04-agent",
    "05-domain",
    "06-repo",
)

PROMPT_CONTRACT_HEADINGS = (
    "## Purpose",
    "## Scope",
    "## Acceptance Criteria",
    "## Falsifiability",
)

PROMPT_EVAL_MIN_SCORE = 80.0

PROMPT_LIBRARY_REPO_ROOT = str(Path(__file__).resolve().parent.parent.parent.parent)
PROMPT_LIBRARY_ROOT = Path(__file__).resolve().parent.parent.parent


def category_prompt_dir(category: str) -> Path:
    """Resolve a composable prompt category directory under the library root."""
    if category not in PROMPT_LIBRARY_CATEGORIES:
        raise ValueError(f"unknown prompt category: {category}")
    return PROMPT_LIBRARY_ROOT / category


def sorted_category_prompts(category: str) -> tuple[Path, ...]:
    """Return sorted markdown prompt paths for a library category."""
    return tuple(sorted(category_prompt_dir(category).glob("*.md")))


def sorted_all_library_prompts() -> tuple[Path, ...]:
    """Return every composable prompt path across all library categories."""
    paths: list[Path] = []
    for category in PROMPT_LIBRARY_CATEGORIES:
        paths.extend(sorted_category_prompts(category))
    return tuple(paths)


def library_skills_dir() -> Path:
    """Resolve the workflow skills directory under the prompt library root."""
    return PROMPT_LIBRARY_ROOT / "skills"


def glossary_path() -> Path:
    """Resolve GLOSSARY.md under the prompt library root."""
    return PROMPT_LIBRARY_ROOT / "GLOSSARY.md"


def cheatsheet_en_path() -> Path:
    """Resolve the English skill trigger cheatsheet."""
    return library_skills_dir() / "SKILL_TRIGGER_CHEATSHEET.md"


def cheatsheet_zh_tw_path() -> Path:
    """Resolve the Traditional Chinese skill trigger cheatsheet."""
    return library_skills_dir() / "SKILL_TRIGGER_CHEATSHEET.zh-TW.md"


def library_readme_path() -> Path:
    """Resolve reflective-prompt-library/README.md."""
    return PROMPT_LIBRARY_ROOT / "README.md"


def repo_readme_path() -> Path:
    """Resolve TeaPrompt repository root README.md."""
    return Path(PROMPT_LIBRARY_REPO_ROOT) / "README.md"


def methodology_map_en_path() -> Path:
    """Resolve METHODOLOGY_MAP.md under the prompt library root."""
    return PROMPT_LIBRARY_ROOT / "METHODOLOGY_MAP.md"


def methodology_map_zh_tw_path() -> Path:
    """Resolve METHODOLOGY_MAP.zh-TW.md under the prompt library root."""
    return PROMPT_LIBRARY_ROOT / "METHODOLOGY_MAP.zh-TW.md"


def skill_map_path() -> Path:
    """Resolve skills/skill-map.md under the prompt library root."""
    return library_skills_dir() / "skill-map.md"


def assert_library_wide_unique_basenames(
    prompt_paths: tuple[Path, ...] | list[Path],
) -> None:
    """Composable prompt basenames must be unique across all categories."""
    basenames = [p.name for p in prompt_paths]
    assert len(basenames) == len(frozenset(basenames)), (
        "duplicate prompt basenames across categories"
    )


def assert_registry_matches_library_glob(
    registry_paths: tuple[Path, ...] | list[Path],
) -> None:
    """Registry prompt tuples must match sorted_category_prompts across the library."""
    assert sorted(sorted_all_library_prompts()) == sorted(registry_paths)

CATEGORY_EVAL_HARNESS_FIXTURE_MARKER = "_from_category_eval_harness_fixture"


def make_category_eval_harness_fixture(repo_root: str):
    """Return a module-scoped EvalHarness pytest fixture bound to repo_root."""
    import pytest
    from eval_harness import EvalHarness

    @pytest.fixture(scope="module")
    def harness() -> EvalHarness:
        return EvalHarness(repo_root=repo_root)

    setattr(harness, CATEGORY_EVAL_HARNESS_FIXTURE_MARKER, True)
    return harness



def assert_prompt_contract_headings(prompt_path: Path) -> None:
    """Contract headings must appear in preamble outside fenced template blocks."""
    preamble = prompt_preamble(prompt_path)
    for heading in PROMPT_CONTRACT_HEADINGS:
        assert heading in preamble, (
            f"{prompt_path.name} missing {heading} outside template block"
        )


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

SUPPORTING_LENS_PRIMARY_SURFACE_BY_CATEGORY: dict[str, frozenset[str]] = {
    "04-agent": frozenset({"runtime-trust-boundary.md"}),
}


def supporting_lens_exempt_for_category(category: str) -> frozenset[str]:
    """Prompts that declare Supporting lens for instead of Primary workflow surface(s)."""
    return SUPPORTING_LENS_PRIMARY_SURFACE_BY_CATEGORY.get(category, frozenset())


def assert_primary_workflow_surface_preamble(
    prompt_path: Path,
    *,
    category: str,
) -> None:
    """Purpose preambles must declare Primary workflow surface(s) or Supporting lens."""
    preamble = prompt_preamble(prompt_path)
    if prompt_path.name in supporting_lens_exempt_for_category(category):
        assert "Supporting lens for" in preamble, (
            f"{prompt_path.name} Purpose should use Supporting lens for workflow skills"
        )
    else:
        assert "Primary workflow surface" in preamble, (
            f"{prompt_path.name} Purpose should list Primary workflow surface(s)"
        )

def assert_category_workflow_skill_coverage(
    prompts: tuple[Path, ...],
    required_skills: tuple[str, ...],
    category_label: str,
) -> None:
    """Category corpus must mention each required workflow skill at least once."""
    text = "\n".join(p.read_text(encoding="utf-8") for p in prompts)
    for skill in required_skills:
        assert skill in text, f"{category_label} should reference {skill}"


def assert_prompt_references_workflow_skill(prompt_path: Path) -> None:
    """Every composable prompt must mention at least one reflective-* workflow skill in preamble."""
    preamble = prompt_preamble(prompt_path)
    assert "reflective-" in preamble, (
        f"{prompt_path.name} should map to at least one workflow skill"
    )

def assert_prompt_meets_eval_harness_floor(
    prompt_path: Path,
    harness,
    repo_root: str,
    min_score: float = PROMPT_EVAL_MIN_SCORE,
) -> None:
    """Prompt must meet eval_harness score floor (default PROMPT_EVAL_MIN_SCORE)."""
    rel = str(prompt_path.relative_to(repo_root))
    result = harness.evaluate_file(rel)
    assert result["score"] >= min_score, (
        f"{prompt_path.name} eval_harness score {result['score']}% < {min_score}%: "
        f"{[(c['id'], c['result']) for c in result['checks']]}"
    )

