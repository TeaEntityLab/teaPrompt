"""Guard the agent-harness convergence survey's evidence and no-adoption state."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "agent-harness-convergence-survey-2026-08-25.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
METHODOLOGY_MAP = PROMPT_LIBRARY_ROOT / "METHODOLOGY_MAP.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
ROADMAP = PLANS_DIR / "whole-project-roadmap-2026-07-11.md"
TRUST_BOUNDARY = PROMPT_LIBRARY_ROOT / "04-agent" / "runtime-trust-boundary.md"
SKILLS_DIR = PROMPT_LIBRARY_ROOT / "skills"
PACKET_SHA256 = "120dbf79376747e58c73c03202cbd689dfe79e5173c0b9ee3789bbe051aa8abe"
LINEAGE_SOURCE_SHA256 = "b07cb166cd2345e7a04c7b79e922bc0a000f721c6a92b64585db06737fe2c8d9"
LINEAGE_PACKET_SHA256 = "903527f5fe84498f1ce6191402c5292ec2fdc8ac6b4c5c3efa1232b01bdf939d"
ORLEANS_DOC_COMMIT = "a4303ce92aa169102f57793c84aae0603c75c3a3"
TARGET_COMMITS = (
    "dcd461925db2edf69a43c8135db1180d418afd54",
    "3a9824a7ea251c084ed40759b2f74ccac1e215b4",
    "8c2e009bb26595d7cad9c93626d9707074daee3a",
    "29cfcd3e11e61b08fc59706d8aa025e0f33756da",
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _ledger_rows() -> dict[str, str]:
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split(
        "## Shared Findings",
        1,
    )[0]
    rows = {}
    for candidate_id in (
        "AH-1",
        "AH-2",
        "AH-3",
        "AH-4",
        "AH-5",
        "AH-6",
        "AH-7",
        "AH-8",
    ):
        rows[candidate_id] = next(
            line
            for line in ledger.splitlines()
            if line.startswith(f"| {candidate_id} |")
        )
    return rows


def _lineage_addendum() -> str:
    text = _read(RECORD)
    marker = "## 2026-08-25 Technical Lineage Addendum"
    assert marker in text, "technical-lineage addendum missing"
    return text.split(marker, 1)[1]


def _lineage_ledger_rows() -> dict[str, str]:
    addendum = _lineage_addendum()
    ledger = addendum.split("### Technical Lineage Candidate Adoption Ledger", 1)[1].split(
        "### Shared Findings",
        1,
    )[0]
    rows = {}
    for candidate_id in (
        "AH-9",
        "AH-10",
        "AH-11",
        "AH-12",
        "AH-13",
        "AH-14",
        "AH-15",
        "AH-16",
        "AH-17",
        "AH-18",
        "AH-19",
    ):
        rows[candidate_id] = next(
            line
            for line in ledger.splitlines()
            if line.startswith(f"| {candidate_id} |")
        )
    return rows


def test_survey_shape_revisions_and_panel_provenance():
    text = _read(RECORD)
    for heading in (
        "## Panel Consensus",
        "## Required Wording Changes",
        "## Candidate Adoption Ledger",
        "## Shared Findings",
        "## Evidence vs Inference",
        "## Disagreements / Residual Risks",
        "## Evidence Actually Checked",
        "## Falsifiability",
    ):
        assert heading in text, f"survey record missing {heading!r}"
    for commit in TARGET_COMMITS:
        assert commit in text
    assert PACKET_SHA256 in text
    assert "unanimous, **6 of 6 lens verdicts**" in text
    assert "without schema-recovery or refan" in text


def test_record_pins_maturity_and_executed_evidence_boundaries():
    text = _read(RECORD)
    for evidence in (
        "2 files, 135 tests passed",
        "25 runtime tests\n  passed",
        "15 runtime-host tests passed",
        "Elixir toolchain",
        "process death and\n  committed prefixes",
        "Pi full harness execution",
    ):
        assert evidence in text, f"load-bearing evidence drifted: {evidence!r}"
    assert "power-loss" in text
    assert "Real payment/refund/email/publish/delete effects" in text


def test_qualified_conclusion_separates_local_replay_from_external_effects():
    text = _read(RECORD)
    conclusion = text.split("### Exact Qualified Conclusion", 1)[1].split(
        "### Use-Case Recommendation",
        1,
    )[0]
    normalized = " ".join(line.lstrip("> ").strip() for line in conclusion.splitlines())
    for token in (
        "shared durable-state-machine pattern",
        "demonstrated industry consensus",
        "does not guarantee exactly-once external effects",
        "sink-enforced idempotency key or query handle",
        "`unknown → reconcile | compensate | Human",
        "Actor addressing and supervision",
        "orthogonal",
    ):
        assert token in normalized, f"qualified conclusion lost {token!r}"


def test_candidate_ledger_preserves_all_dispositions():
    rows = _ledger_rows()
    assert "Adopted in this record only 2026-08-25" in rows["AH-1"]
    assert "No change 2026-08-25" in rows["AH-2"]
    assert "Deferred / study-only 2026-08-25" in rows["AH-3"]
    assert "Rejected / standing non-goal 2026-08-25" in rows["AH-4"]
    assert "Rejected / no local gap 2026-08-25" in rows["AH-5"]
    assert "Rejected 2026-08-25" in rows["AH-6"]
    assert "No change 2026-08-25" in rows["AH-7"]
    assert "Rejected as a general safety policy 2026-08-25" in rows["AH-8"]
    assert "industry consensus" in rows["AH-1"]
    assert "A/B/C kill-point benchmark" in rows["AH-3"]
    assert "synthetic interrupted tool result" in rows["AH-8"]


def test_no_runtime_or_skill_adoption_and_deployment_is_blocked():
    text = _read(RECORD)
    assert "| `adopt` code/dependencies into TeaPrompt | **no**" in text
    assert "| `deploy` for high-stakes external effects | **blocked on this survey alone**" in text
    assert (
        "No candidate changed a TeaPrompt skill, lens, dependency, runtime, or\n"
        "project-knowledge rule." in text
    )


def test_external_adoption_case_study_links_survey_record():
    text = _read(CASE_STUDIES)
    row = next(
        line
        for line in text.splitlines()
        if "| 2026-08-25 | Pi / Maka / Amplio / Ankole durable harness concepts |" in line
    )
    assert "[survey](agent-harness-convergence-survey-2026-08-25.md)" in row
    assert "shared pattern, not industry consensus" in row
    assert "| Agent harness convergence survey outcome recorded | done |" in text


def test_lineage_addendum_shape_identity_and_panel_provenance():
    addendum = _lineage_addendum()
    for heading in (
        "### Panel Consensus",
        "### Required Wording Changes",
        "### Technical Lineage Candidate Adoption Ledger",
        "### Shared Findings",
        "### Evidence vs Inference",
        "### Disagreements / Residual Risks",
        "### Evidence Actually Checked",
        "### Addendum Falsifiability",
    ):
        assert heading in addendum, f"lineage addendum missing {heading!r}"
    for identity in (
        LINEAGE_SOURCE_SHA256,
        LINEAGE_PACKET_SHA256,
        ORLEANS_DOC_COMMIT,
    ):
        assert identity in addendum
    assert "unanimous, **7 of 7 lens verdicts**" in addendum
    assert "without schema recovery, refan" in addendum


def test_lineage_addendum_preserves_replay_and_effect_boundaries():
    addendum = _lineage_addendum()
    normalized = " ".join(addendum.split())
    for wording in (
        "Workflow replay reuses a recorded Activity result",
        "Activity execution may retry",
        "same database transaction",
        "raw third-party call",
        "cannot recall a request already accepted by an external sink",
        "not a verified minimal stack",
        "multi-axis descriptor candidate",
        "explicit durable disposition",
        "fencing rejects stale commits or messages only where the epoch authority is checked",
    ):
        assert wording in normalized, f"lineage boundary wording drifted: {wording!r}"


def test_lineage_candidate_ledger_preserves_dispositions():
    rows = _lineage_ledger_rows()
    assert "Adopted in this record only 2026-08-25" in rows["AH-9"]
    assert "Rejected as canonical; study-only 2026-08-25" in rows["AH-10"]
    assert "Deferred / study-only 2026-08-25" in rows["AH-11"]
    assert "No change 2026-08-25; AH-2 unchanged" in rows["AH-12"]
    assert "Rejected / host-runtime only 2026-08-25" in rows["AH-13"]
    assert "Deferred / study-only 2026-08-25; AH-3 unchanged" in rows["AH-14"]
    assert "Rejected / no verified local gap 2026-08-25" in rows["AH-15"]
    assert "No change / needs host retention design 2026-08-25" in rows["AH-16"]
    assert "Rejected as universal; use-case-specific 2026-08-25" in rows["AH-17"]
    assert "Adopted 2026-08-25 by explicit user direction" in rows["AH-18"]
    assert "recurrence `unknown`" in rows["AH-18"]
    assert "Adopted 2026-08-25 by explicit user direction" in rows["AH-19"]
    assert "recurrence `unknown`" in rows["AH-19"]


def test_lineage_addendum_creates_no_new_governed_surface():
    addendum = _lineage_addendum()
    assert (
        "No AH-9–AH-19 row creates a new core skill, runtime, dependency, MCP extension,\n"
        "or governing Project Knowledge rule." in addendum
    )
    assert "AH-9 is record-level" in addendum
    assert "AH-19\nis a narrow in-place repair" in addendum


def test_external_adoption_case_study_indexes_lineage_addendum():
    text = _read(CASE_STUDIES)
    row = next(
        line
        for line in text.splitlines()
        if "| 2026-08-25 | Pi / Maka / Amplio / Ankole durable harness concepts |" in line
    )
    assert "Temporal/LangGraph/DBOS/Restate/Orleans/OTP" in row
    assert "7-lens lineage addendum" in row
    assert "| Agent harness technical-lineage addendum recorded | done |" in text


def test_ah18_promotes_only_reference_docs_roadmap_and_decision_pointer():
    methodology = _read(METHODOLOGY_MAP)
    section = methodology.split("## Durable Agent Runtime Reference Addendum", 1)[1].split(
        "## Scaffold Provenance Addendum",
        1,
    )[0]
    normalized_section = " ".join(section.split())
    for token in (
        "**Control-state contract**",
        "**Effect contract**",
        "**Ownership/liveness contract**",
        "not a tenth workflow skill",
        "a TeaPrompt-owned runtime",
        "Fencing rejects only stale commits or messages",
        "Effect behavior is multi-axis",
        "agent-harness-convergence-survey-2026-08-25.md#2026-08-25-technical-lineage-addendum",
    ):
        assert token in normalized_section, f"runtime reference lost {token!r}"

    roadmap = _read(ROADMAP)
    for token in (
        "Durable-runtime reference revalidation",
        "AH-11/AH-15 — multi-axis Effect Contract re-litigation",
        "AH-14 — Harness Reliability Benchmark",
        "AH-10 canonical nine-layer Agent Runtime architecture",
        "AH-13 prompt-level fencing/OTP enforcement",
        "#technical-lineage-candidate-adoption-ledger",
    ):
        assert token in roadmap, f"runtime roadmap lost {token!r}"

    knowledge = _read(PROJECT_KNOWLEDGE)
    decision = next(
        line
        for line in knowledge.splitlines()
        if line.startswith("- 2026-08-25 Durable-agent-runtime reference promotion")
    )
    for token in (
        "explicit user direction",
        "AH-18",
        "No durable lesson, skill, prompt lens, dependency, runtime, or governing rule",
        "recurrence is `unknown`",
    ):
        assert token in decision, f"promotion decision lost {token!r}"


def test_ah19_effect_recovery_contract_is_repaired_in_place():
    trust = _read(TRUST_BOUNDARY)
    for token in (
        "## 4a. External Effect Recovery Boundary",
        "`OUTCOME_UNKNOWN`",
        "`retry_safe: false`",
        "synthetic interrupted/error result",
        "Fencing rejects stale commits only at authorities that check the epoch",
        "Effect Recovery Decision",
    ):
        assert token in trust, f"runtime trust-boundary lost {token!r}"

    risk = _read(SKILLS_DIR / "reflective-risk" / "SKILL.md")
    for token in (
        "## Effect Recovery Decision",
        "process crash after dispatch is not failure evidence",
        "`OUTCOME_UNKNOWN`",
        "retained window with matching parameters",
        "unresolved/abandoned disposition",
        "Fencing protects only commits that consult the epoch authority",
    ):
        assert token in risk, f"reflective-risk lost {token!r}"

    spec = _read(SKILLS_DIR / "reflective-spec-plan" / "SKILL.md")
    for token in (
        "**Control-state contract:**",
        "**Effect contract:**",
        "**Ownership/liveness contract:**",
        "post-dispatch/pre-receipt crash window",
        "machine-readable unknown outcome",
        "sink-observed postconditions",
    ):
        assert token in spec, f"reflective-spec-plan lost {token!r}"

    implement = _read(SKILLS_DIR / "reflective-implement" / "SKILL.md")
    for token in (
        "machine-readable `OUTCOME_UNKNOWN`",
        "observe the sink independently from the local log",
        "stale epochs only at the authority that enforces them",
    ):
        assert token in implement, f"reflective-implement lost {token!r}"

    review = _read(SKILLS_DIR / "reflective-review" / "SKILL.md")
    for token in (
        "Internal replay or a synthetic tool error",
        "Dispatch without a durable outcome receipt is unknown",
        "An operation ID proves retry safety only when",
        "Fencing claims are scoped to the authority that checks the epoch",
        "explicit unresolved disposition",
    ):
        assert token in review, f"reflective-review lost {token!r}"

    handoff = _read(SKILLS_DIR / "reflective-handoff-retro" / "SKILL.md")
    for token in (
        "If an external mutation's outcome is still unknown",
        "operation ID, exact parameter/resource/version binding",
        "Put blind retry",
        "under `Do Not Do`",
        "never summarize `OUTCOME_UNKNOWN`",
    ):
        assert token in handoff, f"reflective-handoff-retro lost {token!r}"

    roadmap = _read(ROADMAP)
    assert "AH-19 — external-effect recovery skill repair" in roadmap
    assert "Adopted 2026-08-25 (user-directed; recurrence `unknown`)" in roadmap

    knowledge = _read(PROJECT_KNOWLEDGE)
    decision = next(
        line
        for line in knowledge.splitlines()
        if line.startswith("- 2026-08-25 External-effect recovery skill repair")
    )
    for token in (
        "AH-19",
        "OUTCOME_UNKNOWN",
        "adapter-specific reconciliation",
        "no new skill, runtime, dependency, MCP extension, or governing rule",
        "recurrence is `unknown`",
    ):
        assert token in decision, f"AH-19 decision lost {token!r}"

def test_ah21_data_sanitized_durable_logging_guards():
    trust = _read(TRUST_BOUNDARY)
    assert "| Data protection | credentials, bearer tokens, and sensitive PII redacted" in trust
    scaffold = _read(SKILLS_DIR / "agent-governance-scaffold" / "SKILL.md")
    assert "Never store raw credentials, plaintext authentication tokens, or unredacted personal data (PII) inside durable intent payloads" in scaffold
    assert "secret scrubbing and data-sanitization before committing contract artifacts" in scaffold
