"""Guard the product/runtime ownership panel record and adopted wording."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "product-runtime-ownership-panel-2026-08-25.md"
TRUST_BOUNDARY = PROMPT_LIBRARY_ROOT / "04-agent" / "runtime-trust-boundary.md"
SPEC_PLAN = PROMPT_LIBRARY_ROOT / "skills" / "reflective-spec-plan" / "SKILL.md"
RISK = PROMPT_LIBRARY_ROOT / "skills" / "reflective-risk" / "SKILL.md"
METHODOLOGY_MAP = PROMPT_LIBRARY_ROOT / "METHODOLOGY_MAP.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
SOURCE_SHA256 = "d2e50ad46463dac1eae302acd9a5503dde25e1fb4f811a3f78ef3a76b3600164"
PACKET_SHA256 = "75719b81196ca0659933fc587ef044f44fbe9659e821c69b024b9877f49cf768"
REPO_REVISION = "ce42045a9f8adeebc3c9913345a66dcccc7f4081"


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _ledger_rows() -> dict[str, str]:
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split(
        "## Evidence Actually Checked",
        1,
    )[0]
    return {
        candidate_id: next(
            line
            for line in ledger.splitlines()
            if line.startswith(f"| {candidate_id} |")
        )
        for candidate_id in (f"OW-{number}" for number in range(1, 10))
    }


def test_panel_shape_identity_and_recovered_verdicts():
    text = _read(RECORD)
    for heading in (
        "## Panel Consensus",
        "## Required Wording Changes",
        "## Shared Findings",
        "## Socratic Questions and Disposition",
        "## Disagreements / Residual Risks",
        "## Candidate Adoption Ledger",
        "## Evidence Actually Checked",
        "## Falsifiability",
        "## Completion Ledger",
    ):
        assert heading in text, f"panel record missing {heading!r}"
    for identity in (SOURCE_SHA256, PACKET_SHA256, REPO_REVISION):
        assert identity in text, f"panel identity drifted: {identity}"
    assert "unanimous, **7 of 7 lens verdicts**" in text
    assert "tier-1 DM-wake" in text
    assert "No provider-specific persona or model routing is claimed" in text


def test_candidate_ledger_preserves_bounded_dispositions():
    rows = _ledger_rows()
    assert "**Adopted** 2026-08-25 by explicit user direction" in rows["OW-1"]
    assert "**Adopted** 2026-08-25" in rows["OW-2"]
    assert "**Adopted as a design checklist** 2026-08-25" in rows["OW-3"]
    assert "**Adopted** 2026-08-25" in rows["OW-4"]
    assert "**Partial** 2026-08-25" in rows["OW-5"]
    assert "**Partial** 2026-08-25" in rows["OW-6"]
    assert "**Deferred / blocked** 2026-08-25" in rows["OW-7"]
    assert "**Adopted as a required host precondition** 2026-08-25" in rows["OW-8"]
    assert "**Deferred / study-only** 2026-08-25" in rows["OW-9"]
    assert "named stages remain study-only" in rows["OW-5"]
    assert "do not copy the external checklist verbatim" in rows["OW-6"]
    assert "explicit project-direction change" in rows["OW-7"]


def test_ownership_and_durability_are_guarded_in_trust_boundary():
    text = _read(TRUST_BOUNDARY)
    for wording in (
        "## 2a. Product / Runtime Ownership Boundary",
        "Agent runtime | execution truth",
        "Host product | authentication and tenant scope",
        "Infrastructure adapters | transactions",
        "Execution Success ≠ Business Acceptance",
        "Durability is record-specific, not boolean",
        "A subscriber disconnect ends observation, not business intent",
        "one owner controls the run lifecycle and one terminal outcome",
        "must not receive ambient product-database credentials",
        "authenticated tenant scope",
        "`OUTCOME_UNKNOWN`",
    ):
        assert wording in text, f"trust-boundary wording drifted: {wording!r}"


def test_spec_and_risk_contracts_preserve_host_acceptance_preconditions():
    spec = _read(SPEC_PLAN)
    for wording in (
        "**Product-truth contract:**",
        "lowest user-visible promise",
        "Durability is record-specific",
        "optional reference vocabulary, not a maturity ladder",
        "A client subscription lifecycle is not the execution lifecycle",
        "one absorbing terminal outcome",
        "commit-before-success",
        "cross-tenant replay denial",
    ):
        assert wording in spec, f"reflective-spec-plan lost {wording!r}"

    risk = _read(RISK)
    for wording in (
        "Runtime completion is a proposal, not business acceptance",
        "current resource version (or an equivalent decisive precondition)",
        "A client transport disconnect ends observation only",
        "explicit authenticated command",
        "must not receive ambient product-database credentials",
        "authenticated tenant scope and invocation-bound capabilities",
        "`OUTCOME_UNKNOWN`",
    ):
        assert wording in risk, f"reflective-risk lost {wording!r}"


def test_reference_and_judgement_surfaces_point_to_the_guarded_record():
    methodology = _read(METHODOLOGY_MAP)
    for wording in (
        "Treat product truth as an orthogonal boundary",
        "Runtime `COMPLETED` records execution truth",
        "Durability claims are record-specific rather than",
        "subscriber disconnect ends observation",
        "product-runtime-ownership-panel-2026-08-25.md",
    ):
        assert wording in methodology, f"methodology map lost {wording!r}"

    knowledge = _read(PROJECT_KNOWLEDGE)
    assert "### Lesson: Runtime execution truth is not product acceptance" in knowledge
    assert "- 2026-08-25 Product/runtime ownership boundary" in knowledge
    assert "adopted OW-1–OW-4 and OW-8" in knowledge
    assert "TeaPrompt still owns no runtime, dependency, persistence adapter, or tenth core skill" in knowledge

    case_studies = _read(CASE_STUDIES)
    assert "| 2026-08-25 | Heddle / SlideX product-runtime ownership article" in case_studies
    assert "Product/runtime ownership panel outcome and guarded adoption recorded | done" in case_studies
    assert "[panel record](product-runtime-ownership-panel-2026-08-25.md)" in case_studies


def test_panel_preserves_runtime_and_evidence_boundaries():
    text = _read(RECORD)
    for wording in (
        "no Heddle dependency, hosted execution service, persistence adapter, replay engine, or tenth core workflow skill",
        "`deploy` — **blocked on this review alone**",
        "did not inspect a pinned Heddle repository, package tarball, license, provenance attestation",
        "Product revision checks complement that rule but do not resolve a remote effect",
        "The adopted wording is a clean-room conceptual restatement",
        "host code and tests",
    ):
        assert wording in text, f"panel boundary drifted: {wording!r}"
