"""Guard the pi-warden survey: record identity pins, the quoted charter lines
held byte-exact, the PW-1 confidence-ratchet sentence pinned exactly once on
the workflow-recipes Confidence row and off every other installed surface,
seven dispositions, the executed-trigger evidence line, the clean-room
boundary, and the index links.

Jev/TypeSafe vocabulary is deliberately not in this guard's token set: the
sibling decision-interface survey guards already police those tokens over the
same surfaces; duplicating the regex is weightless.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "pi-warden-survey-2026-09-20.md"
RECIPES = PROMPT_LIBRARY_ROOT / "04-agent" / "workflow-recipes.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

PIN = "c9921c3ebc48f62348199eb03119c645d98cdb8b"
TREE = "0d132763c3b226a9d43331704d26066fe31b662d"
CREATED = "2026-09-16T03:58:46Z"

PW1_SENTENCE = (
    "confidence only raises strictness: low self-reported confidence defaults up, a close call "
    "between top candidates on host-measured scores escalates the same way, and no confidence "
    "number — self-reported or measured — lowers the rigor risk demands"
)
QUOTES = (
    "patterns set the floor and Jev can only raise it, the agent's plan can add a nudge but never remove a hold, and the LLM is never asked to judge itself",
    "An unmeasured question can be merged as `extra` (recorded, never acted on), not as a rule.",
    "Steers never hold.",
    "Approval comes from the user's message only.",
    "against the honest null hypothesis: the same rules handed to the model as prose",
    "prompts that fire this often train the operator to approve reflexively",
    "a checked-out repo cannot ship itself a hold-free floor or a prompt farm",
    "In 150 paired agent runs, the control setup violated the tested project rule **6 times**. With Warden: **0**.",
    "Shares no code with the guard on purpose: no Jev verdict can influence a score.",
)
CANDIDATE_STATUS = {
    "PW-1": "Adopted 2026-09-20 (DM-5 reopened; fired trigger + user direction)",
    "PW-2": "No change 2026-09-20",
    "PW-3": "No change 2026-09-20",
    "PW-4": "No change 2026-09-20",
    "PW-5": "Noted 2026-09-20 (record-only)",
    "PW-6": "Noted 2026-09-20 (record-only)",
    "PW-7": "Noted 2026-09-20 (record-only)",
}
# The project's vocabulary and identifier names stay in the record.
SURVEY_TOKENS = re.compile(
    r"pi-warden|pi-typesafe|DevMortimer|MrJev|Gapac|earendil|steerBudget|"
    r"armingRules|pathRules|commandRules",
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _durable_surfaces() -> list[Path]:
    return (
        sorted(library_skills_dir().glob("*/SKILL.md"))
        + sorted(library_skills_dir().glob("examples/*.md"))
        + sorted(PROMPT_LIBRARY_ROOT.glob("SKILL_INSTALLATION*.md"))
        + [glossary_path()]
        + sorted((PROMPT_LIBRARY_ROOT / "04-agent").glob("*.md"))
    )


def test_record_identity_pins_and_shape():
    text = _read(RECORD)
    assert re.search(r"^> \*\*Status: decided — one sentence adopted \(PW-1\)", "\n".join(text.splitlines()[:12]), re.M)
    for pin in (PIN, TREE, CREATED, "MIT", "0.29.1", "pi-typesafe"):
        assert pin in text, pin
    assert "Survey this concept and rethink our goals. Update docs and skills if worthy" in text
    assert "a TeaPrompt-run host step consumed real per-candidate scores" in text
    for heading in (
        "Research Question", "Direct Recommendation", "Method", "What the Artifact Is",
        "Concept Map", "Candidate Adoption Ledger", "Shared Findings", "Goals Rethink",
        "Evidence vs Inference", "Evidence Actually Checked", "Falsifiability", "Completion Ledger",
    ):
        assert f"## {heading}" in text, heading
    concept_map = text.split("## Concept Map", 1)[1].split("\n## ", 1)[0]
    assert re.findall(r"^\| (C\d+) \|", concept_map, re.M) == [f"C{i}" for i in range(1, 13)]


def test_quoted_charter_lines_pinned():
    text = _read(RECORD)
    for quote in QUOTES:
        assert quote in text, quote


def test_pw1_pinned_once_on_confidence_row():
    recipes = _read(RECIPES)
    assert recipes.count(PW1_SENTENCE) == 1
    row = next(l for l in recipes.splitlines() if PW1_SENTENCE in l)
    assert row.startswith("| Confidence"), "PW-1 must sit on the Confidence recipe row"
    assert PW1_SENTENCE in _read(RECORD)
    for path in _durable_surfaces():
        if path == RECIPES:
            continue
        assert PW1_SENTENCE not in _read(path), path


def test_candidate_ledger_preserves_dispositions():
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split("\n## ", 1)[0]
    rows = [
        [cell.strip() for cell in line.split("|")[1:-1]]
        for line in ledger.splitlines() if re.match(r"^\| PW-\d \|", line)
    ]
    assert {row[0] for row in rows} == set(CANDIDATE_STATUS)
    for row in rows:
        assert len(row) == 5, row
        assert row[2] == CANDIDATE_STATUS[row[0]], row
        assert row[3], f"missing evidence: {row[0]}"


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    surfaces = _durable_surfaces()
    assert len(surfaces) >= 20, "surface set unexpectedly small"
    for path in surfaces:
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_existing_indexes_link_the_survey_decision():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert f"[plans/{RECORD.name}](plans/{RECORD.name})" in knowledge
    state = _read(CASE_STUDIES).split("## State Ledger", 1)[1].split("\n## ", 1)[0]
    assert RECORD.name in state
