"""Guard the governed-delivery feature adoption (GD-1..GD-17) at its surfaces.

Mirrors test_agent_governance_scaffold_adoption_state.py: every Adopted row in
plans/governed-delivery-adoption-2026-09-03.md gets a structural check so drift
fails loudly. Anchor sentences are verbatim contracts shared with the core
skills that carry phase-local features.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402
from validate_skill_examples import DOMAIN_PACK_SKILLS  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
SKILLS = library_skills_dir()
PACK = SKILLS / "governed-delivery" / "SKILL.md"
EXAMPLES = SKILLS / "examples" / "governed-delivery.examples.md"
ADOPTION = PLANS_DIR / "governed-delivery-adoption-2026-09-03.md"
LINT_WARNING_CHARS = 20000

ANCHORS = {
    "reflective-brief": (
        "Name what the spec will not capture — tacit constraints, unknown unknowns, and "
        "non-functional expectations — as unknowns with an owner, so intent loss is visible "
        "before planning starts.",
        "Each assumption carries a status — `open`, `confirmed`, `refuted`, or `stale` — and "
        "a change to the goal marks dependent assumptions `stale`.",
    ),
    "reflective-spec-plan": (
        "Oracle manifest: list every acceptance, invariant, and security oracle with its class "
        "(authoritative or developer), owner, host sealing precondition, and change protocol.",
        "The spec carries a version; a mid-task change bumps it and marks every dependent plan "
        "item and ledger entry `stale` before work continues.",
        "Acceptance record: a named accepter closes the delivery against the oracle manifest "
        "and product evidence; execution success alone never closes it.",
    ),
    "reflective-implement": (
        "Work from a task packet — spec version, State Ledger, oracle manifest, relevant files "
        "— and never from the transcript; if the packet is missing an acceptance criterion, "
        "stop and repair the packet.",
        "A failure signature is the failing oracle, the error class, and the touched surface; "
        "when a signature repeats after a correction, exit by rollback to the last verified "
        "ledger state, a strategy change, or escalation — never by an identical retry.",
    ),
    "reflective-review": (
        "Declare the verification channels used — deterministic check, runtime evidence, "
        "external primary source, independent model, self-assessment — and whether they are "
        "independent; a high-risk PASS needs at least one non-model channel.",
    ),
    "reflective-research": (
        "Each evidence entry names the claim, the source, the attester, the freshness kind, "
        "and the date checked.",
    ),
    "reflective-risk": (
        "Sink inventory: list every sink the task can reach — secrets, memory or skill "
        "promotion, permissions, deployment, outbound communication, money — and name the "
        "deterministic host gate or Human Review that fronts each.",
        "Unattended envelope: before any unattended run, record the pre-approved budget, the "
        "per-action pause list, and the kill conditions; a run outside the envelope stops.",
    ),
    "reflective-handoff-retro": (
        "A continuation packet carries the spec version, the State Ledger, oracle manifest "
        "status, open failure signatures, and named unknowns.",
        "Gate retro: record which gates fired, which were bypassed, and which caught nothing; "
        "feed the result into policy change, and keep policy change separate from policy "
        "activation.",
    ),
    "reflective-minimality": (
        "Governance artifacts face the same delete-before-add test: size gate thickness to "
        "risk and remove ceremony that defends no named invariant.",
    ),
}

PACK_NEVER = (
    "Never claim TeaPrompt enforces a gate, seals an oracle, isolates a sink, or persists a "
    "ledger; the contract set is host-run and enforcement is a host precondition.",
    "Never let the executing agent edit the oracle manifest, the verification plan, the "
    "acceptance record, or the envelope; those are constitutional paths changed only "
    "out-of-band by a different owner.",
    "Never auto-release a gate on model self-report; a gate releases on deterministic "
    "evidence, an attester's receipt, or a named human decision.",
    "Never use a universal retry or iteration count; budgets and failure-signature limits are "
    "task-declared in the envelope.",
    "Never treat the transcript as the source of record; every gate reads the task packet and "
    "the ledgers.",
    "Never route this pack from `reflective-dispatch` or present it as a tenth core workflow "
    "skill; it is host-invoked.",
)
GATES = ("intent", "spec", "plan", "execution", "verification", "acceptance", "retro")
TEMPLATES = (
    "intent-record",
    "oracle-manifest",
    "task-packet",
    "failure-log",
    "verification-plan",
    "evidence-ledger",
    "acceptance-record",
    "envelope",
    "gate-retro",
)
CLEAN_ROOM_FORBIDDEN = re.compile(
    r"arXiv:\d|17% F|39/49|\+32%|\bA[0-5]–A[0-5]\b|\bK[0-4]–K[0-4]\b|\bW[0-5]–W[0-5]\b|"
    r"\bG[0-6]–G[0-6]\b|\bP1–P12\b|grill"
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _section(text: str, heading: str) -> str:
    assert heading in text, f"pack lost {heading!r}"
    return text.split(heading, 1)[1].split("\n## ", 1)[0]


def _skill(name: str) -> str:
    return _read(SKILLS / name / "SKILL.md")


# GD-17 - registered, self-labelled, outside dispatch routes.
def test_gd17_registered_self_labelled_and_off_dispatch_routes():
    assert "governed-delivery" in DOMAIN_PACK_SKILLS
    text = _read(PACK)
    assert "domain-pack" in text.lower()
    assert "not selected by `reflective-dispatch` route rows" in text
    dispatch = _skill("reflective-dispatch")
    route = dispatch.split("## Route", 1)[1].split("## Strictness Ladder", 1)[0]
    assert "governed-delivery" not in route


# GD-17 - frontmatter declares the human-review gate and pack metadata.
def test_gd17_frontmatter_declares_review_gate():
    meta = _read(PACK).split("---", 2)[1]
    assert "name: governed-delivery" in meta
    assert "risk_level: high" in meta
    assert "human_review_required: true" in meta
    assert "context_load: medium" in meta


# Pack contract: Purpose boundary, Never set, gates, templates, envelope, refuters.
def test_pack_purpose_states_boundary_and_direct_answer():
    purpose = _section(_read(PACK), "## Purpose").lower()
    assert "methodology" in purpose and "operational" in purpose
    assert "external-adoption-case-studies-2026-06-20.md" in purpose
    assert "bounded, not solved" in purpose


def test_pack_never_block_keeps_every_boundary_bullet():
    never = _read(PACK).split("Never:", 1)[1].split("Escalation:", 1)[0]
    for bullet in PACK_NEVER:
        assert bullet in never, f"pack Never lost {bullet[:60]!r}"


def test_gd12_gate_sequence_has_seven_gates_with_human_only_ends():
    section = _section(_read(PACK), "## Delivery Gate Sequence")
    for gate in GATES:
        assert f"`{gate}`" in section, gate
    intent_row = next(line for line in section.splitlines() if line.startswith("| `intent`"))
    acceptance_row = next(
        line for line in section.splitlines() if line.startswith("| `acceptance`")
    )
    for row in (intent_row, acceptance_row):
        assert row.rstrip().rstrip("|").strip().split("|")[-1].strip().lower().startswith("no"), row


def test_gd13_envelope_adds_no_new_ladder():
    section = _section(_read(PACK), "## Autonomy Envelope")
    assert (
        "This pack adds no new lettered ladder: autonomy is expressed through the existing "
        "strictness ladder (`L1`–`L6`) and Gate 2.0 thickness." in section
    )
    for field in ("budget", "pause", "kill", "failure-signature", "sink", "accepter"):
        assert field in section, field


def test_gd2_to_gd10_contract_set_has_nine_templates():
    section = _section(_read(PACK), "## Contract Set")
    for name in TEMPLATES:
        assert f"### {name}" in section, name


def test_gd14_gd15_invariants_and_host_preconditions():
    text = _read(PACK)
    invariants = _section(text, "## Delivery Invariants").lower()
    for phrase in ("not closing acceptance", "not evidence", "not attestation", "not enforcement", "not the record", "stale"):
        assert phrase in invariants, phrase
    host = _section(text, "## Host Preconditions")
    for phrase in ("write protection", "egress", "durable", "TeaPrompt runs none"):
        assert phrase in host, phrase
    # SS-1 (2026-09-05): the run note is a fixed-field shape; every precondition is written, `unknown` by default.
    for field in ("oracle_sealing", "sink_isolation", "budget_enforcement", "durable_ledger_storage", "human_decision_channel"):
        assert f"{field}: unknown" in host, field
    assert "incomplete, not passing" in host and "an output, not enforcement" in host


def test_gd16_refuters_are_six_and_unknown_until_run():
    section = _section(_read(PACK), "## Adversarial Refuters")
    for n in range(1, 7):
        assert f"- **GDR-{n}**" in section, n
    assert "`unknown`" in section


def test_pack_trailer_sections_and_examples_pointer():
    text = _read(PACK)
    for heading in ("## Verification", "## Demotion Triggers", "## Examples", "## Prompt Sources"):
        assert heading in text, heading
    assert "<skills-root>/examples/governed-delivery.examples.md" in text
    assert "not runtime dependencies" in text
    assert "governed-delivery-adoption-2026-09-03.md" in text
    examples = _read(EXAMPLES)
    assert len(examples.strip()) >= 600
    assert "artifact-complete" in examples


def test_pack_body_stays_under_lint_warning_threshold():
    body = _read(PACK).split("---", 2)[2]
    assert len(body) <= LINT_WARNING_CHARS, len(body)


# GD-1..GD-11 - phase-local anchors present exactly once in the owning core skill.
def test_core_skill_anchors_present_once():
    for name, anchors in ANCHORS.items():
        text = _skill(name)
        for anchor in anchors:
            assert text.count(anchor) == 1, f"{name} anchor count != 1: {anchor[:50]!r}"


# Clean-room: no corpus tokens on any skill surface touched by this adoption.
def test_clean_room_tokens_absent_from_all_skill_surfaces():
    for path in SKILLS.glob("*/SKILL.md"):
        assert not CLEAN_ROOM_FORBIDDEN.search(path.read_text(encoding="utf-8")), path.name


# Small-Change Fast Path survives the deepening.
def test_implement_fast_path_untouched():
    assert "Small-Change Fast Path" in _skill("reflective-implement")


# Adoption record shape and ledger.
def test_adoption_record_shape_and_ledger():
    text = _read(ADOPTION)
    for heading in (
        "## Acceptance provenance",
        "## Reconsidered options",
        "## Feature → destination map",
        "## Candidate Adoption Ledger",
        "## Demotion Triggers",
        "## Evidence Actually Checked",
        "## Falsifiability",
        "## Completion Ledger",
    ):
        assert heading in text, heading
    assert "Composite self-acceptance (disclosed)" in text
    assert "recurrence `unknown`" in text
    for n in range(1, 18):
        assert f"| GD-{n} |" in text, n
    assert "| GD-16 | Adversarial refuters | Adopted 2026-09-03 (contracts only; all six `unknown`)" in text
    assert "| GD-18 | Independent post-land panel | Deferred" in text
    assert "never waives the tenth-core promotion gate" in text
