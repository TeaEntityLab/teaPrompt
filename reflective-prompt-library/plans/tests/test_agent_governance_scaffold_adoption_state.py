"""Guard adopted agent-governance-scaffold pack contracts at their surfaces.

Mirrors test_flow_pack_adoption_state.py: the adopted Candidate Adoption Ledger
rows (G1-G8 in plans/agent-governance-scaffold-adoption-2026-07-17.md) get
structural, executable-symbol, or stable-protocol checks so drift fails loudly.
Deferred rows would be guarded only for ledger presence, per GLOSSARY Adoption
Guard Closure; every G-row here is Adopted, so each gets a real check.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402
from validate_skill_examples import DOMAIN_PACK_SKILLS  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
SKILL = library_skills_dir() / "agent-governance-scaffold" / "SKILL.md"
CONCEPTS = PLANS_DIR / "agent-governance-four-power-concepts-2026-07-17.md"
ADOPTION = PLANS_DIR / "agent-governance-scaffold-adoption-2026-07-17.md"


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


# G1 - registered as a domain pack.
def test_g1_registered_in_domain_pack_registry():
    assert "agent-governance-scaffold" in DOMAIN_PACK_SKILLS


# G1 - self-labels as a domain pack (validate_governance requires this too).
def test_g1_self_labels_as_domain_pack():
    assert "domain-pack" in _read(SKILL).lower()


# G2 - Module Contract with the runtime-boundary Purpose (methodology/operational).
def test_g2_methodology_boundary_in_purpose():
    purpose = _read(SKILL).split("## Purpose", 1)[1].split("\n## ", 1)[0].lower()
    assert "methodology" in purpose and "operational" in purpose
    assert "external-adoption-case-studies-2026-06-20.md" in purpose


# G2 - demotion triggers section present (pack contract convention).
def test_g2_demotion_triggers_section():
    assert "## Demotion Triggers" in _read(SKILL)


# G2 - the load-bearing "no TeaPrompt runtime/enforcement" Never clause.
def test_g2_no_runtime_enforcement_claim_in_never():
    text = _read(SKILL)
    never = text.split("Never:", 1)[1].split("Escalation:", 1)[0].lower()
    assert "enforce" in never
    assert "host" in never


# Core spec objects the scaffold must emit (feature -> artifact map).
@pytest.mark.parametrize(
    "token",
    [
        "AuthorityPolicy",
        "effect_receipt",
        "issued_by",
        "cumulative_effect_key",
        "reset_requires",
        "checker_profile",
        "constitutional_paths",
        "policy_activation",
        "activation_epoch",
        "escalate_if",
        "agenda_check",
        "mutation_suite",
        "approver_canary",
        "proposal_state",
        "control_decision",
        "semantic_interface",
        "conformance_suite",
        "verification_plan",
        "twin_check",
        "heterogeneous_evidence_reconciliation",
        "experiment_protocol",
        "hypotheses_yaml",
        "analysis_plan",
    ],
)
def test_scaffold_emits_core_governance_objects(token: str):
    assert token in _read(SKILL), f"scaffold lost governance object {token!r}"


# Anti-salami: cumulative budget keyed on the lease, not the session.
def test_cumulative_budget_is_lease_keyed_not_session():
    text = _read(SKILL)
    assert "new_out_of_band_authorization" in text
    assert "not the session" in text or "not session-keyed" in text


# Broker issues receipts, not the executor (invariant #2/#4).
def test_broker_issues_receipts_not_executor():
    text = _read(SKILL).lower()
    assert "broker-issued" in text or "issued by the broker" in text


# G7 - concepts record present with the feature->artifact map.
def test_g7_concepts_record_has_feature_map():
    text = _read(CONCEPTS)
    assert "Feature" in text and "Scaffold" in text
    assert "Fifteen Invariants" in text or "fifteen invariant" in text.lower()
    for token in ("Proposal Lifecycle", "Conformance suite", "Twin Check", "H1", "Keyword Glossary", "Heddle Mapping", "Composition, Adversarial Economy", "attributability", "Kerckhoffs"):
        assert token in text, f"concepts record lost {token!r} coverage"


# G3/G4/G5/G6/G8 - adoption ledger rows on record with the required record shape.
def test_adoption_record_shape_and_ledger():
    text = _read(ADOPTION)
    for heading in (
        "## Decision",
        "## Candidate Adoption Ledger",
        "## Evidence Actually Checked",
        "## Disagreements / Residual Risks",
        "## Falsifiability",
    ):
        assert heading in text, f"adoption record missing {heading!r}"
    for row in ("| G1 |", "| G2 |", "| G3 |", "| G4 |", "| G5 |", "| G6 |", "| G7 |", "| G8 |"):
        assert row in text, f"adoption ledger missing row {row!r}"


# G5 - discoverable but never on the core dispatch route table.
def test_g5_absent_from_dispatch_routes():
    dispatch = library_skills_dir() / "reflective-dispatch" / "SKILL.md"
    route = _read(dispatch).split("## Route", 1)[1].split("## Strictness Ladder", 1)[0]
    assert "agent-governance-scaffold" not in route
