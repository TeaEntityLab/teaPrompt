"""Guard the pi-warden survey's quoted charter lines
held byte-exact, the PW-1 confidence-ratchet sentence pinned exactly once on
the workflow-recipes Confidence row and off every other installed surface,
the clean-room boundary, and the index links.

Jev/TypeSafe vocabulary is deliberately not in this guard's token set: the
sibling decision-interface survey guards already police those tokens over the
same surfaces; duplicating the regex is weightless.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir, skill_package_docs  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "pi-warden-survey-2026-09-20.md"
RECIPES = PROMPT_LIBRARY_ROOT / "04-agent" / "workflow-recipes.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

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
        sorted(skill_package_docs())
        + sorted(library_skills_dir().glob("examples/*.md"))
        + sorted(PROMPT_LIBRARY_ROOT.glob("SKILL_INSTALLATION*.md"))
        + [glossary_path()]
        + sorted((PROMPT_LIBRARY_ROOT / "04-agent").glob("*.md"))
    )


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
