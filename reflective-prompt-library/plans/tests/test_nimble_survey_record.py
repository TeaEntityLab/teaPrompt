"""Guard the Bespoke Nimble survey: record identity and tally pins, the quoted
admissions held byte-exact, six dispositions, the clean-room boundary, and the
index links.

Jev/TypeSafe/vLLM vocabulary is deliberately not in this guard's token set:
the decision-model, Jev-architecture, and Jev-diffusion survey guards already
police those tokens over the same surfaces; duplicating the regex is weightless.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "nimble-survey-2026-09-19.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

PIN = "d2387fc0b32d1173bfc995395c076a25a2a107c9"
TREE = "3873bf61d82e7441d03763b19ce3a7a0789ad005"
HF_SHA = "594dfdcfb6f94e3d0c0db7535180d3c71689169a"
CREATED = "2026-09-18T09:07:48Z"

QUOTES = (
    "Note that we did not distill from Jev.",
    "A probability of 0.9 does not mean that the answer is right 90% of the time.",
    "Separate calls to the same model can make the same mistake, so the checks can miss some errors.",
    "Do not tune hyperparameters or select checkpoints on this holdout; derive any future tuning split from the training families only.",
    "so the scorer can be measured against annotations it had no part in creating",
    "These converters measure **agreement with human annotation**, not truth.",
    "No shuffled run has been made yet, so position bias is unmeasured.",
    "No vendor-published public-dataset result for Jev exists.",
)
CANDIDATE_STATUS = {
    "NB-1": "No change 2026-09-19",
    "NB-2": "No change 2026-09-19",
    "NB-3": "No change 2026-09-19",
    "NB-4": "Noted 2026-09-19 (record-only)",
    "NB-5": "Noted 2026-09-19 (record-only)",
    "NB-6": "Noted 2026-09-19 (record-only)",
}
# The project's vocabulary and its dataset/product names stay in the record.
SURVEY_TOKENS = re.compile(
    r"Nimble|bespokelabsai|Bespoke|MiniCheck|\bNoul\b|VitaminC|MASSIVE|BoolQ|SummEval|"
    r"HelpSteer|Aegis2|PubMedQA|BANKING77|openjeff|contrastive data curation",
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


def test_record_identity_and_tally_pins():
    text = _read(RECORD)
    assert re.search(r"^> \*\*Status: decided — record-only; no installed change", "\n".join(text.splitlines()[:12]), re.M)
    for pin in (PIN, TREE, HF_SHA, CREATED):
        assert pin in text, pin
    assert "no LICENSE at the repository root" in text
    assert "Apache-2.0" in text
    for tally in ("90.12", "93.21", "74.8", "76.0"):
        assert tally in text, tally
    for heading in (
        "Research Question", "Direct Recommendation", "Method", "What the Artifact Is",
        "Concept Map", "Candidate Adoption Ledger", "Shared Findings", "Evidence vs Inference",
        "Evidence Actually Checked", "Falsifiability", "Completion Ledger",
    ):
        assert f"## {heading}" in text, heading
    concept_map = text.split("## Concept Map", 1)[1].split("\n## ", 1)[0]
    assert re.findall(r"^\| (C\d+) \|", concept_map, re.M) == [f"C{i}" for i in range(1, 11)]


def test_quoted_admissions_pinned():
    text = _read(RECORD)
    for quote in QUOTES:
        assert quote in text, quote


def test_candidate_ledger_preserves_dispositions():
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split("\n## ", 1)[0]
    rows = [
        [cell.strip() for cell in line.split("|")[1:-1]]
        for line in ledger.splitlines() if re.match(r"^\| NB-\d \|", line)
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
