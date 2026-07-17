"""Guard adopted agent-governance-scaffold pack contracts at their surfaces.

Mirrors test_flow_pack_adoption_state.py: the adopted Candidate Adoption Ledger
rows (G1-G8 in plans/agent-governance-scaffold-adoption-2026-07-17.md) get
structural, executable-symbol, or stable-protocol checks so drift fails loudly.
Deferred rows would be guarded only for ledger presence, per GLOSSARY Adoption
Guard Closure; every G-row here is Adopted, so each gets a real check.
"""

import json
import re
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
EXAMPLES = library_skills_dir() / "examples" / "agent-governance-scaffold.examples.md"


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


# Core contract tokens must live in the Artifact Set, not merely in provenance
# prose or a panel record. Architecture-only experiment stubs are guarded below.
@pytest.mark.parametrize(
    "token",
    [
        "authorization_id",
        "capability_class",
        "state_predicate",
        "effect_receipt",
        "issued_by",
        "receipt_store",
        "cumulative_effect_key",
        "cross_purpose_budget",
        "reset_requires",
        "checker_profile",
        "constitutional_paths",
        "worker_writable_exclusions",
        "policy_activation",
        "activation_store",
        "activation_epoch",
        "escalate_if",
        "agenda_check",
        "mutation_suite",
        "approver_canary",
        "proposal_state",
        "control_decision",
        "semantic_interface",
        "conformance_suite",
        "ultra_vires_nullification",
        "verification_plan",
        "twin_check",
        "heterogeneous_evidence_reconciliation",
    ],
)
def test_artifact_set_covers_governance_contracts(token: str):
    artifact_set = _read(SKILL).split("## Artifact Set", 1)[1].split(
        "\n## Fifteen-Invariant Checklist", 1
    )[0]
    assert token in artifact_set, f"Artifact Set lost governance contract {token!r}"


# Anti-salami: both lease-local and cross-authorization budgets are explicit.
def test_cumulative_budget_is_lease_keyed_and_aggregate():
    section = _read(SKILL).split("### Cumulative-effect budget", 1)[1].split(
        "\n### Lease semantics", 1
    )[0]
    assert 'reset_requires: "new_out_of_band_authorization"' in section
    assert "cross_purpose_budget:" in section
    assert "max_operations_across_authorizations:" in section
    assert "new_session" not in section


# Broker receipt integrity is asserted in the JSON contract, not global prose.
def test_broker_receipt_contract_is_broker_owned():
    section = _read(SKILL).split("### Broker effect receipt", 1)[1].split(
        "\n### Cumulative-effect budget", 1
    )[0]
    match = re.search(r"```json\n(.*?)\n```", section, re.DOTALL)
    assert match, "broker receipt JSON contract missing"
    receipt = json.loads(match.group(1))["effect_receipt"]
    assert receipt["issued_by"] == "broker"
    assert receipt["receipt_store"] == "broker_owned_append_only"
    assert receipt["integrity_evidence"]


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


# ---------------------------------------------------------------------------
# 2026-07-18 six-lens panel guards (R-ledger in the panel record)
# ---------------------------------------------------------------------------

PANEL = PLANS_DIR / "agent-governance-scaffold-panel-record-2026-07-18.md"


# R5/R12 - canonical invariant vocabulary plus a fillable object mapping.
def test_invariant_checklist_is_canonical_object_mapping():
    section = _read(SKILL).split("## Fifteen-Invariant Checklist", 1)[1].split(
        "\n## Verification", 1
    )[0]
    assert "| emitted_object | invariant(s) | host_enforcer | evidence_now | unwired_obligation |" in section
    assert "Emit one row per emitted object" in section
    assert "`effect_receipt`" in section and "| broker |" in section
    items = re.findall(r"^\d+\. (.+)$", section, re.MULTILINE)
    assert items == [
        "model-output≠effect",
        "approval≠evidence",
        "exec-success≠goal-success",
        "audit≠accountability",
        "rollback≠no-harm",
        "role-sep≠failure-independence",
        "scope-string≠scope",
        "risk-class-is-a-proposal",
        "new-session≠new-auth",
        "review≠evidence",
        "authority-monotone-down-the-chain",
        "subagent-report-is-untrusted",
        "escalation-not-absorbed",
        "authorization-is-a-lease",
        "control-effective-under-full-disclosure",
    ]


# R5/R13 - L0 stays an integrity gate, never the acceptor.
def test_acceptance_ladder_l0_through_l5_semantics():
    ladder = _read(SKILL).split("### Acceptance ladder", 1)[1].split("\n### ", 1)[0]
    for i in range(6):
        assert f"L{i} " in ladder, f"ladder lost L{i}"
    l0 = next(line for line in ladder.splitlines() if line.startswith("L0 "))
    assert "Artifact integrity" in l0
    assert "gate only" in l0


# R5/R13 - full host-run interface signature and its non-shell distinction.
def test_run_interface_full_signature_contract():
    text = _read(SKILL)
    assert re.search(
        r"run-<cli>\.sh <read-only\|workspace-write> <workdir> "
        r"<prompt-file> \[model\] \[effort\]",
        text,
    ), "run interface signature changed"
    assert "interface signature, not executable shell" in text


# R6 - adoption record carries provenance, honest evidence tier, and triggers.
def test_r6_adoption_record_provenance_and_triggers():
    text = _read(ADOPTION)
    assert "## Acceptance provenance" in text
    assert "## Demotion Triggers" in text
    assert "| G9 |" in text
    assert "file presence" in text and "not example↔output parity" in text
    assert "author-claimed" in text
    assert "Class fit `[INFERENCE]`" in text
    assert "R1–R16" in text and "R17 fired-partial" in text and "runtime rig deferred" in text
    assert "lite-ad" in text or "first lite-ad" in text


# R15/G9 - silence cannot defer collision measurement forever.
def test_g9_deferral_has_checkpoint_review_hook():
    row = next(
        line for line in _read(ADOPTION).splitlines() if line.startswith("| G9 |")
    )
    assert "2026-10-11" in row
    assert "checkpoint" in row.lower()


# Panel record exists with the protocol sections and a closed R-ledger.
def test_panel_record_shape():
    text = _read(PANEL)
    for heading in (
        "## Panel Consensus",
        "## Required Wording Changes",
        "## Candidate Adoption Ledger",
        "## Disagreements / Residual Risks",
        "## Evidence Actually Checked",
        "## Falsifiability",
        "## Post-Remediation Verification Panel",
        "## Closure Readiness Verification Panel",
    ):
        assert heading in text, f"panel record missing {heading!r}"
    for n in range(1, 25):
        assert f"| R{n} |" in text, f"panel record missing row R{n}"
    assert "| G9 |" in text
    r17 = next(line for line in text.splitlines() if line.startswith("| R17 |"))
    assert "Fired-partial 2026-07-17" in r17
    assert "runtime rig deferred" in r17



# R1/R3/R14 - static scaffolding cannot claim host enforcement.
def test_runtime_boundary_and_examples_name_unwired_bypass():
    skill = _read(SKILL)
    examples = _read(EXAMPLES)
    assert "artifact presence or narrated host preconditions" in skill
    assert "do not claim four-power compliance" in skill
    assert "## Residual risk if unwired" in examples
    assert "direct Slack/tool call" in examples
    assert examples.count("artifact-complete, not") >= 2
    assert examples.count("enforcement-proven") >= 2
    assert ".agent/hooks/**" in examples and ".agent/evidence-schema/**" in examples
    assert "## Example 3" in examples
    assert "Governance status:** artifact-complete" in examples
    assert "direct_<cli>_exec_via_hook" in examples
    assert "emitted_object | invariant(s) | host_enforcer | evidence_now | unwired_obligation" in examples



# R2 - every high-risk escalation category adopted by the first panel remains.
def test_escalation_categories_remain_complete():
    escalation = _read(SKILL).split("Escalation:", 1)[1].split(
        "\n## Four-Power Split", 1
    )[0]
    for phrase in (
        "security-sensitive logic",
        "database migrations",
        "public API changes",
        "ambiguous requirements that affect architecture",
        "Human Review",
    ):
        assert phrase in escalation


# R4/R13 - no separate AuthorityPolicy schema regresses through the example.
def test_capability_token_has_no_separate_authoritypolicy_schema():
    four_power = _read(SKILL).split("## Four-Power Split", 1)[1].split(
        "\n## Gate 2.0", 1
    )[0]
    example_one = _read(EXAMPLES).split("## Example 2", 1)[0]
    assert "AuthorityPolicy" not in four_power
    assert "authority-policy.json" not in example_one
    assert "capability-token.json" in example_one


# R7 - experiment files remain architecture references, never default emits.
def test_experiment_protocol_is_reference_only():
    section = _read(SKILL).split("### Experiment protocol", 1)[1].split(
        "\n### Wrapper-agent contract", 1
    )[0]
    for token in ("experiment_protocol", "hypotheses_yaml", "analysis_plan"):
        assert token in section
    assert "not a default emit" in section
    assert "never as part of a first-task scaffold" in section


# R12/R14 - template evidence must not masquerade as formal schema/runtime proof.
def test_templates_do_not_claim_formal_schema_or_unbrokered_fallback():
    skill = _read(SKILL)
    examples = _read(EXAMPLES)
    assert "object schemas" not in skill
    assert "parseability is not JSON Schema validation" in skill
    assert ".schema.json" not in examples
    assert "falls back in-process if" not in skill
    assert "identical host broker and policy gates" in skill
    assert "direct_<cli>_exec_via_hook" in skill
    assert "**Governance status:** artifact-complete" in skill



def test_conformance_and_checker_profile_are_evidence_tier_labeled():
    skill = _read(SKILL)
    conformance = skill.split("### Semantic interface + conformance suite", 1)[1].split(
        "### Verification plan", 1
    )[0]
    checker = skill.split("### Checker profile", 1)[1].split(
        "### Broker effect receipt", 1
    )[0]
    assert "host-run spec" in conformance
    assert "artifact presence does not prove conformance passed" in conformance
    assert "illustrative placeholders" in checker
    assert "not calibrated benchmark scores" in checker



# R14 - constitutional ownership and compliance-status bindings stay explicit.
def test_host_owned_security_bindings_remain():
    skill = _read(SKILL)
    for token in (
        "worker_writable_exclusions",
        "same_transaction_as_policy_change: false",
        "worker_may_write_activation_record: false",
        "issued_out_of_band: true",
        "minimum_before_compliance_claim",
        "artifact-complete",
        "enforcement-proven",
    ):
        assert token in skill
    section = skill.split("constitutional_paths:", 1)[1].split("policy_activation:", 1)[0]
    paths = re.findall(r'- "([^"]+)"', section.split("worker_writable_exclusions:", 1)[0])
    deny = re.search(r"deny_write:\s*\[(.*?)\]", section, re.S).group(1)
    for path in paths:
        assert path in deny, f"constitutional path {path!r} missing from deny_write"
    assert ".agent/hooks/**" in deny and ".agent/evidence-schema/**" in deny

# R18 - Output menu language and Four-Power conditional markers stay aligned.
def test_output_menu_and_four_power_conditional_alignment():
    skill = _read(SKILL)
    output = skill.split("Output:", 1)[1].split("Never:", 1)[0]
    assert "menu, not a mandatory file count" in output
    assert "are conditional" in output
    assert "Four-Power Split table" in output
    four = skill.split("## Four-Power Split", 1)[1].split("## Gate 2.0", 1)[0]
    assert "when agenda/goal risk requires it" in four
    assert "when the host wires them" in four


# R20 - interim context_load honesty until R10 shrink.
def test_context_load_is_high_until_r10_shrink():
    meta = _read(SKILL).split("---", 2)[1]
    assert "context_load: high" in meta


# R12 - Module Contract Output conditional menu cannot silently revert.
def test_module_contract_output_keeps_conditional_menu():
    output = _read(SKILL).split("Output:", 1)[1].split("Never:", 1)[0]
    assert "external-effect governance scaffold" in output
    assert "Artifact Set is a menu, not a mandatory file count" in output

