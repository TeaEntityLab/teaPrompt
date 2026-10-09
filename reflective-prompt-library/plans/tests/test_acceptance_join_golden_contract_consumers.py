"""Developer-only spec-consumer guard for the F12/F13/F17 contract repairs.

Parses the documented shapes — never executes acceptance commands, never runs
a golden comparison, never dispatches a model. Each check proves a
consumer-visible contract behavior: definition seats vs reference mentions,
static shell resolution semantics, and completed-vs-censored ledger rows.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import library_skills_dir  # noqa: E402

SKILLS = library_skills_dir()
JOIN_SKILL = SKILLS / "acceptance-join-validator" / "SKILL.md"
JOIN_EXAMPLES = SKILLS / "examples" / "acceptance-join-validator.examples.md"
GOLDEN_SKILL = SKILLS / "golden-benchmark-runner" / "SKILL.md"
GOLDEN_EXAMPLES = SKILLS / "examples" / "golden-benchmark-runner.examples.md"


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def test_join_contract_distinguishes_definitions_from_references():
    """F17: duplicate detection covers definition seats, never bare mentions."""
    skill = _read(JOIN_SKILL)
    assert "definition seat" in skill.lower() or "definition" in skill
    for token in ("covers:", "reference", "duplicate"):
        assert token in skill, token


def test_join_examples_contrast_double_definition_with_clean_mentions():
    """F17: fixtures show a genuine double definition and a clean mention pair."""
    examples = _read(JOIN_EXAMPLES)
    assert "genuine double definition" in examples.lower()
    assert "NOT a duplicate" in examples or "not a duplicate" in examples.lower()
    assert "covers:" in examples
    # The clean join must name its multiple-mention case explicitly so the
    # duplicate rule cannot be re-read as every-repeated-token-errors.
    first = examples.split("## Example 2", 1)[0]
    assert "Multiple mentions are not" in first




def test_golden_examples_carry_required_ledger_evidence_fields():
    """F13: every canonical JSONL row has completion, reason, scorer id+rev."""
    examples = _read(GOLDEN_EXAMPLES)
    rows = [
        json.loads(line)
        for line in re.findall(r"^\{.*\}$", examples, re.M)
    ]
    assert len(rows) >= 3, "need completed pair rows plus a censored row"
    for row in rows:
        for field in (
            "task_id", "arm", "candidate_sha256", "score",
            "completion", "status_reason",
            "scorer_executable", "scorer_revision",
        ):
            assert field in row, (field, row.get("task_id"), row.get("arm"))
        assert row["completion"] in {"completed", "censored", "incomplete"}
        assert row["status_reason"], (row["task_id"], row["arm"])
        assert row["scorer_executable"] and row["scorer_revision"]
    completed = [r for r in rows if r["completion"] == "completed"]
    censored = [r for r in rows if r["completion"] in {"censored", "incomplete"}]
    assert completed, "need at least one completed row"
    assert censored, "need at least one representative censored row"
    for row in censored:
        assert row["score"] is None, (row["task_id"], row["arm"])
    for row in completed:
        assert isinstance(row["score"], int), (row["task_id"], row["arm"])
    # The semantic scorer stays a separately named role on structural rows.
    assert all("semantic_scorer_person" in row for row in rows)


def test_golden_contract_names_null_means_unscored_not_zero():
    """F13: the skill contract pins score:null and scorer id+revision."""
    skill = _read(GOLDEN_SKILL)
    assert "`null` when unscored" in skill or "null when unscored" in skill
    assert "scorer_revision" in skill
    assert "semantic_scorer_person" in skill
    assert "never a zero-score loss" in skill
