"""Guard the LLM-as-a-Judge lifecycle survey record and its adopted wording.

Panel outcome was record-only (AGREE 4/7); a follow-up user direction adopted
three clean-room sentences (JL-2a with a narrowed JL-3 clause, JD-1a, JD-1b).
Adopted rows get presence pins at their surfaces; record-only / rejected rows
are guarded for ledger presence and disposition only (GLOSSARY Adoption Guard
Closure). The loop pack is also pinned under the lint length threshold because
the adoption was paid for by trimming, not by accepting a second warning.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "llm-judge-lifecycle-survey-2026-09-05.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
LOOP_PACK = library_skills_dir() / "flow-loop-harness" / "SKILL.md"
RECIPES = PROMPT_LIBRARY_ROOT / "04-agent" / "workflow-recipes.md"
REVIEW = library_skills_dir() / "reflective-review" / "SKILL.md"
LINT_WARNING_CHARS = 20000
PASTE_SHA256 = "40a3efd15e74793be7148544b7e5c36dc5f8f57d349d15d99db13ef375637b5f"
PACKET_SHA256 = "fe0914e2f3dfa124c10adf9558edd61588a101e076306f713fa953db15796dd9"
REPO_REVISION = "1e4f96078abcb9b076897f7a68f001c407526ae1"
ADOPTED = {
    LOOP_PACK: (
        "Rubric as verifier: request a host permission mode that also excludes "
        "`prompts/critic-rubric.md` from the loop body's editable paths, as Loop Anatomy #5 "
        "does for `checks/`.",
        "Critique fed to the reviser is data, never authority to rewrite that rubric, weaken "
        "`ACCEPT`, or skip the cap; the exclusion does not promote `ACCEPT` above advisory tier.",
        "A rubric reused across unattended runs drifts from the humans it stands in for: "
        "spot-check its verdicts *and reasons* against human review, stop unattended use when "
        "they diverge, and change it only via the human-gated path, keeping the prior version "
        "for rollback.",
    ),
    RECIPES: (
        "Tally reasons, not only verdicts: lenses that agree on a verdict for different reasons "
        "are one uncertain channel, not independent confirmation, and lenses that disagree for "
        "the same reason are one finding; synthesis records the reason split beside the verdict "
        "split.",
    ),
    REVIEW: (
        "Audit the reason, not only the verdict: a check that reaches the right label for a "
        "reason that does not match the criterion is a finding, not a confirmation — a "
        "misaligned reason poisons every revision or decision that consumes it.",
    ),
}
VENDOR_TOKENS = re.compile(r"Netflix|RART|Meta-Judge|Reflector|arXiv:\d|two standard deviations")


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _ledger_rows() -> dict[str, str]:
    ledger = _read(RECORD).split("## Candidate Adoption Ledger", 1)[1].split(
        "## Evidence Used", 1
    )[0]
    ids = ["JL-1", "JL-2a", "JL-2b"] + [f"JL-{n}" for n in range(3, 20)] + ["JD-1", "JD-2"]
    return {
        candidate_id: next(
            line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |")
        )
        for candidate_id in ids
    }


def test_record_shape_identity_and_recovery_disclosure():
    text = _read(RECORD)
    for heading in (
        "## Research Question",
        "## Direct Recommendation (as of 2026-09-05)",
        "## Panel Consensus",
        "## Required Wording Changes (final)",
        "## Shared Findings",
        "### Packet corrections (evidence beat the packet)",
        "## Socratic Questions and Disposition",
        "## Disagreements / Residual Risks",
        "## Candidate Adoption Ledger",
        "## Evidence Used (external source ledger)",
        "## Evidence vs Inference",
        "## Risks / Unknowns",
        "## Evidence Actually Checked",
        "## Falsifiability",
        "## Coordinator Reflection — Judge Harness and Intent Drift (2026-09-05)",
        "## Completion Ledger",
    ):
        assert heading in text, f"survey record missing {heading!r}"
    for identity in (PASTE_SHA256, PACKET_SHA256, REPO_REVISION, "arXiv:2608.18300v3"):
        assert identity in text, f"survey identity drifted: {identity}"
    assert "`AGREE` **4 of 7**" in text and "`AGREE WITH CHANGES` **3 of 7**" in text
    assert "**Unanimous 7/7**" in text
    assert "died at ~324 ms" in text and "refanned on the `task` backend" in text
    assert "no provider persona or model routing is claimed" in text
    assert "Panel outcome: none. **Post-panel user direction (2026-09-05) adopted three sentences**" in text
    assert "**Dissent preserved:**" in text


def test_direct_recommendation_and_stance_boundary():
    text = _read(RECORD)
    answer = text.split("## Direct Recommendation (as of 2026-09-05)", 1)[1].split(
        "## Panel Consensus", 1
    )[0]
    assert "**Study yes; reproduce blocked; adopt no (record-only); deploy blocked.**" in answer
    assert "Neither creates a Trigger that an existing skill fails today." in answer
    assert "the article **serves** on a model-judge pass" in text
    assert "never solely pass high-risk work" in text


def test_ledger_dispositions_preserve_the_split():
    rows = _ledger_rows()
    assert "**Adopted (user-directed)** 2026-09-05 after a 3 adopt / 4 record-only panel" in rows["JL-2a"]
    assert "**Adopted (narrowed, user-directed)** 2026-09-05 over a 7/7 record-only panel" in rows["JL-3"]
    assert "**Adopted (coordinator-minted, user-directed)** 2026-09-05" in rows["JD-1"]
    assert "concordant verdicts" in rows["JD-1"] or "two different reasons" in rows["JD-1"]
    assert "**Adopted (user-directed)** 2026-09-05" in rows["JD-2"]
    for record_only in ("JL-2b", "JL-7", "JL-9"):
        assert "**Record-only" in rows[record_only], record_only
    assert "**No change / record-only** 2026-09-05 (7/7)" in rows["JL-1"]
    for no_change in ("JL-4", "JL-5", "JL-6", "JL-8", "JL-11", "JL-12", "JL-13", "JL-14"):
        assert "**No change** 2026-09-05" in rows[no_change], no_change
    for rejected in ("JL-15", "JL-16", "JL-17", "JL-18"):
        assert "**Rejected** 2026-09-05" in rows[rejected], rejected
    assert "**Applied in this record** 2026-09-05" in rows["JL-19"]
    assert "OW-2" in rows["JL-6"] and "OW-1" not in rows["JL-6"]


def test_adopted_wording_present_once_at_every_surface():
    for path, sentences in ADOPTED.items():
        text = _read(path)
        for sentence in sentences:
            assert text.count(sentence) == 1, f"{path.name} lost or duplicated: {sentence[:48]!r}"


def test_loop_pack_stays_under_lint_length_threshold():
    assert len(_read(LOOP_PACK)) <= LINT_WARNING_CHARS


def test_reflection_records_the_compression_chain_and_boundaries():
    reflection = _read(RECORD).split(
        "## Coordinator Reflection — Judge Harness and Intent Drift (2026-09-05)", 1
    )[1].split("## Completion Ledger", 1)[0]
    for token in (
        "attester with a lifecycle, not an oracle",
        "| Intent → spec |",
        "| Judge → time |",
        "audited by reason rather than outcome",
        "No rater-spread numbers, sample sizes, or cadences in any skill",
        "No change to `governed-delivery`",
    ):
        assert token in reflection, token


def test_skill_surfaces_stay_clean_room():
    for path in library_skills_dir().glob("*/SKILL.md"):
        assert not VENDOR_TOKENS.search(path.read_text(encoding="utf-8")), path.name


def test_indexes_point_to_the_record():
    knowledge = _read(PROJECT_KNOWLEDGE)
    decision = next(
        line
        for line in knowledge.splitlines()
        if line.startswith("- 2026-09-05 LLM-as-a-Judge lifecycle survey")
    )
    for token in (
        "record-only",
        "4 of 7",
        "adopted three clean-room sentences by user direction over the panel split",
        "compression durable lesson",
        "no judge, benchmark store, rater panel, or drift monitor",
        "[record](plans/llm-judge-lifecycle-survey-2026-09-05.md)",
    ):
        assert token in decision, f"decision index lost {token!r}"

    case_studies = _read(CASE_STUDIES)
    assert "| 2026-09-05 | LLM-as-a-Judge lifecycle article" in case_studies
    assert "[survey](llm-judge-lifecycle-survey-2026-09-05.md)" in case_studies
    assert (
        "| LLM-as-a-Judge lifecycle survey recorded; three sentences adopted by user direction "
        "with reflection | done |" in case_studies
    )
    lesson = knowledge.split(
        "### Lesson: Intent lives with humans; every downstream artifact is a lossy compression "
        "read by an optimizer", 1
    )[1].split("\n### ", 1)[0].split("\n## ", 1)[0]
    assert "Label agreement is not confirmation when the reasons differ." in lesson
    assert "llm-judge-lifecycle-survey-2026-09-05.md" in lesson
    assert "Review trigger:" in lesson
