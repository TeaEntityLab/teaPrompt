"""Guard the governable-autonomy survey record and its adopted in-place wording."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "governable-autonomy-survey-2026-09-03.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
AGENTS = PROMPT_LIBRARY_ROOT / "06-repo" / "AGENTS.md"
TRUST_BOUNDARY = PROMPT_LIBRARY_ROOT / "04-agent" / "runtime-trust-boundary.md"
WORKFLOW_RECIPES = PROMPT_LIBRARY_ROOT / "04-agent" / "workflow-recipes.md"
ARTIFACT_PROMOTION = PROMPT_LIBRARY_ROOT / "04-agent" / "artifact-promotion.md"
CONTEXT_ENGINEERING = PROMPT_LIBRARY_ROOT / "03-context" / "context-engineering.md"
SKILLS_DIR = PROMPT_LIBRARY_ROOT / "skills"
SOURCE_SHA256 = "36e09db964d01e73bf48e22b958da9e4b2e43e6e3406bcb414e39feff7362dbf"
PACKET_SHA256 = "d6cefa0224b40cbaaacf2e7ed2c591b69b3c9ad89502b5816a1c16d034b54824"
REPO_REVISION = "5e4c5b0ded25ee5d32a85b0ba7b70f266423e1ee"
ARXIV_ID = re.compile(r"arXiv:\d{4}\.\d{4,5}")

ADOPTED_WORDING = {
    AGENTS: (
        "- edit an acceptance, invariant, or security oracle so a run passes; if the oracle is wrong, "
        "stop and propose an oracle change for Human Review",
        "prompt text cannot seal an oracle — host write protection or CI ownership must",
    ),
    SKILLS_DIR / "reflective-implement" / "SKILL.md": (
        "Acceptance, invariant, and security oracles are read-only during a run; if one is wrong, "
        "stop and propose an oracle change for Human Review. Developer tests may be added freely. "
        "Prompt text cannot seal an oracle — the host must (write protection, protected branch, CI ownership).",
        "`pending` / `done` / `verified` / `failed` / `stale`",
        "mark every dependent ledger item `stale`, re-plan only the affected slice, and re-verify; "
        "never absorb the change as an informal note",
        "If the same failure signature recurs after a correction, do not keep retrying inside the "
        "polluted context",
        "Retry budgets are task-declared, never unbounded; a prompt cannot clear its own context — a host must.",
    ),
    SKILLS_DIR / "reflective-spec-plan" / "SKILL.md": (
        "- Oracle class: authoritative (sealed during runs; changes need Human Review) / developer",
    ),
    CONTEXT_ENGINEERING: (
        "Task context is assembled from canonical artifacts (spec, ledger, relevant files) and covers "
        "every acceptance criterion and constraint the task depends on; the transcript is not the "
        "source of record, so a reset or compaction must not lose state.",
    ),
    WORKFLOW_RECIPES: (
        "Reviewers read a bounded packet, not the full transcript: review and monitor accuracy degrade "
        "as transcript length grows.",
        "Lenses run on one model family share failure modes; count them as one epistemic channel "
        "unless deterministic or runtime evidence backs the verdict.",
    ),
    SKILLS_DIR / "reflective-review" / "SKILL.md": (
        "Rank evidence: deterministic checks, then runtime evidence, then external primary sources, "
        "then independent model judgment, then generator self-assessment.",
        "Same-model, same-context multi-role review is one epistemic channel, not independent "
        "verification; model judgment may block or warn but never solely pass a high-risk claim.",
    ),
    SKILLS_DIR / "reflective-research" / "SKILL.md": (
        "Say which kind of freshness applies: a date to recheck, a tracking event that invalidates it, "
        "or an immutable pin (digest, commit, or published text).",
        "A tool result or measurement the agent triggered is evidence; the agent's own summary of it is not.",
    ),
    TRUST_BOUNDARY: (
        "Assume injection detection has a non-zero miss rate; design so untrusted content cannot reach "
        "secrets, memory or skill promotion, permissions, deployment, or outbound communication without "
        "a deterministic host gate or Human Review — prompt rules cannot isolate a sink; the host must.",
    ),
    ARTIFACT_PROMOTION: (
        "For every `workflow skill` or `prompt lens` candidate, also answer:",
        "- Compatibility bounds: which tool, framework, model, or repository versions the guidance "
        "assumes; for a workflow skill, the paired with/without check that shows it helps — "
        "version-mismatched guidance can reduce outcomes.",
    ),
    SKILLS_DIR / "reflective-brief" / "SKILL.md": (
        "4. State assumptions and unknowns; an unresolved high-impact, irreversible assumption is a "
        "Human Review trigger, not a default.",
    ),
    SKILLS_DIR / "reflective-handoff-retro" / "SKILL.md": (
        "Do not treat the transcript as the source of record; assemble continuation state from canonical artifacts (spec, ledger, relevant files); a reset or compaction must not lose state.",
    ),
    SKILLS_DIR / "reflective-risk" / "SKILL.md": (
        "Do not assume prompt rules isolate a sink: injection detection has a non-zero miss rate, so untrusted content must not reach secrets, memory or skill promotion, permissions, deployment, or outbound communication without a deterministic host gate or Human Review.",
    ),
}


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _ledger_rows() -> dict[str, str]:
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split(
        "## Reproduction Contracts",
        1,
    )[0]
    return {
        candidate_id: next(
            line
            for line in ledger.splitlines()
            if line.startswith(f"| {candidate_id} |")
        )
        for candidate_id in (f"GA-{number}" for number in range(1, 21))
    }


def test_survey_shape_identity_and_panel_provenance():
    text = _read(RECORD)
    for heading in (
        "## Research Question",
        "## Direct Recommendation (as of 2026-09-03)",
        "## Panel Consensus",
        "## Required Wording Changes (final, adopted 2026-09-03)",
        "## Shared Findings",
        "## Socratic Questions and Disposition",
        "## Disagreements / Residual Risks",
        "## Candidate Adoption Ledger",
        "## Reproduction Contracts (host-only; refuters)",
        "## Evidence Used (external source ledger)",
        "## Evidence vs Inference",
        "## Risks / Unknowns",
        "## Evidence Actually Checked",
        "## Falsifiability",
        "## Completion Ledger",
    ):
        assert heading in text, f"survey record missing {heading!r}"
    for identity in (SOURCE_SHA256, PACKET_SHA256, REPO_REVISION):
        assert identity in text, f"survey identity drifted: {identity}"
    assert "unanimous, **7 of 7 lens verdicts**" in text
    assert "No provider-specific persona or model routing is claimed" in text


def test_direct_answer_keeps_bounded_not_solved_and_verified_magnitudes_in_record_only():
    text = _read(RECORD)
    answer = text.split("## Direct Recommendation (as of 2026-09-03)", 1)[1].split(
        "## Panel Consensus",
        1,
    )[0]
    for wording in (
        "cannot be trusted without human intent sign-off and deterministic host containment",
        "Intent drift and context rot are not solved; they are bounded.",
        "**Solved enough to rely on (mechanism level):**",
        "**Controlled, not solved:**",
        "**Unsolved:**",
        "17% false-negative rate on real overeager actions, n=52",
        "`Execution Success ≠ Business Acceptance`",
        "not declared an anti-pattern",
    ):
        assert wording in answer, f"direct answer lost {wording!r}"
    for unverified in ("+32%–170%", "2×–30×", "93% blind approval", "`N=2` hard reset"):
        assert unverified in text, f"unverified magnitude must stay quarantined in the record: {unverified!r}"
    assert "were not verified against source bodies and were kept out of every adopted sentence" in text


def test_candidate_ledger_preserves_all_dispositions():
    rows = _ledger_rows()
    assert "**Adopted (narrowed)** 2026-09-03 by explicit user direction" in rows["GA-1"]
    for narrowed in ("GA-2", "GA-3", "GA-4", "GA-6", "GA-8"):
        assert "**Adopted (narrowed)** 2026-09-03" in rows[narrowed], narrowed
    for adopted in ("GA-5", "GA-7"):
        assert "**Adopted** 2026-09-03" in rows[adopted], adopted
    assert "**Adopted (trigger only)** 2026-09-03" in rows["GA-9"]
    assert "Hyperplan 2026-06-21 no-change on ledgers preserved" in rows["GA-9"]
    assert "**Rejected** 2026-09-03" in rows["GA-10"]
    assert "**Rejected / Standing Non-Goal** 2026-09-03" in rows["GA-11"]
    assert "**No change** 2026-09-03" in rows["GA-12"]
    assert "**Deferred / host-only** 2026-09-03" in rows["GA-13"]
    assert "**No change** 2026-09-03" in rows["GA-14"]
    assert "**Rejected** 2026-09-03" in rows["GA-15"]
    assert "ATT-7 (2026-08-12)" in rows["GA-15"]
    assert "**No change** 2026-09-03" in rows["GA-16"]
    assert "**No change / record-only** 2026-09-03" in rows["GA-17"]
    assert "**No change** 2026-09-03" in rows["GA-18"]
    assert "**Rejected** 2026-09-03" in rows["GA-19"]
    assert "**Rejected** 2026-09-03" in rows["GA-20"]
    assert "risk-scaled stance retained" in rows["GA-20"]


def test_adopted_wording_is_present_at_every_named_surface():
    for path, phrases in ADOPTED_WORDING.items():
        text = _read(path)
        for phrase in phrases:
            assert phrase in text, f"{path.name} lost adopted wording: {phrase!r}"


def test_durable_surfaces_carry_no_survey_citations_or_universal_retry_number():
    for path in ADOPTED_WORDING:
        text = _read(path)
        assert not ARXIV_ID.search(text), f"{path.name} must not embed arXiv identifiers"
        assert "17% FNR" not in text and "17% false" not in text, f"{path.name} must not embed vendor figures"
    implement = _read(SKILLS_DIR / "reflective-implement" / "SKILL.md")
    assert "stop after 2 identical failure signatures" not in implement
    assert "N=2" not in implement


def test_record_preserves_disagreements_and_host_ownership():
    text = _read(RECORD)
    for wording in (
        "**GA-9 (3-way split):**",
        "**GA-4 numeric default:**",
        "re-creates the universal threshold ATT-7 rejected",
        "all seven lenses required removing arXiv identifiers and vendor figures from durable prompt surfaces",
        "none of the adopted wording is enforced by TeaPrompt",
        "this survey adds no runtime, context compiler, outbox, sandbox, dependency, directory, pack, or tenth core skill",
        "- **R-1:**",
        "- **R-9:**",
    ):
        assert wording in text, f"survey record lost {wording!r}"


def test_indexes_point_to_the_guarded_record():
    knowledge = _read(PROJECT_KNOWLEDGE)
    decision = next(
        line
        for line in knowledge.splitlines()
        if line.startswith("- 2026-09-03 Governable autonomous delivery survey")
    )
    for token in (
        "explicit user direction",
        "adopted GA-1–GA-9 as narrow clean-room wording",
        "universal `N=2` reset (ATT-7)",
        "drift and context rot are bounded, not solved",
        "no runtime, dependency, or tenth core skill",
        "recurrence is `unknown`",
        "[record](plans/governable-autonomy-survey-2026-09-03.md)",
    ):
        assert token in decision, f"decision index lost {token!r}"

    case_studies = _read(CASE_STUDIES)
    assert "| 2026-09-03 | Governable autonomous delivery corpus" in case_studies
    assert "[survey](governable-autonomy-survey-2026-09-03.md)" in case_studies
    assert (
        "| Governable autonomous delivery survey outcome and guarded adoption recorded | done |"
        in case_studies
    )
