"""Guard the governable-autonomy all-skills coverage panel and adopted Never sentences."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402
from validate_skill_examples import CORE_SKILLS, DOMAIN_PACK_SKILLS  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "ga-skills-coverage-panel-2026-09-03.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
SKILLS_DIR = PROMPT_LIBRARY_ROOT / "skills"
EXAMPLES_DIR = SKILLS_DIR / "examples"
HANDOFF = SKILLS_DIR / "reflective-handoff-retro" / "SKILL.md"
RISK = SKILLS_DIR / "reflective-risk" / "SKILL.md"
PACKET_SHA256 = "00c2645ab35f6667979006200212f407ec9f66d71f9dd7de543a15c0e78d3895"
REPO_REVISION = "084852c2a5962c1020bd2c624d460035e1c51ae9"
HANDOFF_SENTENCE = (
    "Do not treat the transcript as the source of record; assemble continuation "
    "state from canonical artifacts (spec, ledger, relevant files); a reset or "
    "compaction must not lose state."
)
RISK_SENTENCE = (
    "Do not assume prompt rules isolate a sink: injection detection has a "
    "non-zero miss rate, so untrusted content must not reach secrets, memory or "
    "skill promotion, permissions, deployment, or outbound communication without "
    "a deterministic host gate or Human Review."
)
FORBIDDEN_SKILL_DIRS = (
    "reflective-autonomy",
    "intent-grill",
    "spec-grill",
    "context-compiler",
    "fault-injection-harness",
    "evidence-ledger",
    "consequence-gateway",
    "knowledge-wiki",
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _ledger_rows() -> dict[str, str]:
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split(
        "## Evidence vs Inference",
        1,
    )[0]
    ids = [f"XS-{n}" for n in range(1, 10)] + ["GS-A", "GS-B", "GS-C"]
    return {
        candidate_id: next(
            line
            for line in ledger.splitlines()
            if line.startswith(f"| {candidate_id} |")
        )
        for candidate_id in ids
    }


def test_panel_shape_identity_and_recovery():
    text = _read(RECORD)
    for heading in (
        "## Research Question",
        "## Panel Consensus",
        "## Required Wording Changes",
        "## Shared Findings",
        "## Socratic Questions and Disposition",
        "## Disagreements / Residual Risks",
        "## Candidate Adoption Ledger",
        "## Evidence vs Inference",
        "## Evidence Actually Checked",
        "## Falsifiability",
        "## Completion Ledger",
    ):
        assert heading in text, f"panel record missing {heading!r}"
    for identity in (PACKET_SHA256, REPO_REVISION):
        assert identity in text, f"panel identity drifted: {identity}"
    assert "**6 of 7** independent lens verdicts" in text
    assert "Original `GSArchitecture` **crashed**" in text
    assert "**tier-3 refan** `GSArchitecture2`" in text
    assert "No provider-specific persona or model routing is claimed" in text
    assert "No extra skill" in text


def test_candidate_ledger_rejects_extra_skills_and_adopts_two_sentences():
    rows = _ledger_rows()
    for rejected in ("XS-1", "XS-2", "XS-5", "XS-6", "XS-7", "XS-9"):
        assert "**Rejected** 2026-09-03" in rows[rejected], rejected
    assert "**Rejected / host-only** 2026-09-03" in rows["XS-3"]
    assert "**Rejected / host-only** 2026-09-03" in rows["XS-4"]
    assert "tenth-core gate" in rows["XS-1"]
    assert "**Adopted (narrowed)** 2026-09-03" in rows["XS-8"]
    assert "**Adopted** 2026-09-03" in rows["GS-A"]
    assert "**Adopted** 2026-09-03" in rows["GS-B"]
    assert "**Rejected** 2026-09-03" in rows["GS-C"]
    assert "5/7 against brief" in rows["GS-C"]


def test_adopted_never_sentences_and_frozen_skill_cardinality():
    assert HANDOFF_SENTENCE in _read(HANDOFF)
    assert RISK_SENTENCE in _read(RISK)
    assert len(CORE_SKILLS) == 9
    # The panel left DOMAIN_PACK_SKILLS at three; the same-day user-directed
    # governed-delivery adoption (plans/governed-delivery-adoption-2026-09-03.md)
    # superseded XS-8/XS-9 and added a fourth pack. Core stays frozen at nine.
    assert len(DOMAIN_PACK_SKILLS) == 4
    assert "governed-delivery" in DOMAIN_PACK_SKILLS
    found = {path.parent.name for path in SKILLS_DIR.glob("*/SKILL.md")}
    assert found == set(CORE_SKILLS) | set(DOMAIN_PACK_SKILLS)
    for name in FORBIDDEN_SKILL_DIRS:
        assert not (SKILLS_DIR / name / "SKILL.md").exists(), name
        assert not (EXAMPLES_DIR / f"{name}.examples.md").exists(), name


def test_indexes_point_to_the_guarded_panel():
    knowledge = _read(PROJECT_KNOWLEDGE)
    decision = next(
        line
        for line in knowledge.splitlines()
        if line.startswith("- 2026-09-03 Governable autonomy × all skills panel")
    )
    for token in (
        "no extra skill",
        "two Never sentences",
        "transcript is not the source of record",
        "prompt rules cannot isolate a sink",
        "tenth-core gate not waived",
        "[record](plans/ga-skills-coverage-panel-2026-09-03.md)",
    ):
        assert token in decision, f"decision index lost {token!r}"

    case_studies = _read(CASE_STUDIES)
    assert "| 2026-09-03 | All 12 TeaPrompt skills vs governable-autonomy possibilities" in case_studies
    assert "[panel record](ga-skills-coverage-panel-2026-09-03.md)" in case_studies
    assert (
        "| Governable autonomy × all skills panel outcome and guarded adoption recorded | done |"
        in case_studies
    )
