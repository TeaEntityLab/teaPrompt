"""Adoption-state guards for the 2026-07-12 skill scenario panel.

Each test pins one adopted Candidate Adoption Ledger row from
`plans/skill-scenario-panel-record-2026-07-12.md` to its named surface, so a
silent revert flips the gate red instead of drifting.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_ROOT,
    cheatsheet_en_path,
    cheatsheet_zh_tw_path,
    library_skills_dir,
)

PLANS = Path(__file__).parent.parent
RECORD = PLANS / "skill-scenario-panel-record-2026-07-12.md"


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _skill(name: str) -> str:
    return _read(library_skills_dir() / name / "SKILL.md")


# ---------------------------------------------------------------------------
# SOLO-2 / SOLO-3 — proportionality at the implement/dispatch surfaces
# ---------------------------------------------------------------------------


def test_solo2_implement_small_change_fast_path_present():
    text = _skill("reflective-implement")
    assert "## Small-Change Fast Path" in text
    assert "Never collapse verification itself" in text
    assert "exits the fast path back to the full contract" in text


def test_solo3_dispatch_ladder_direct_to_implement_note_present():
    text = _skill("reflective-dispatch")
    assert "small, clear change routes directly to `reflective-implement`" in text
    assert "Small-Change Fast Path" in text


# ---------------------------------------------------------------------------
# DOC-1 / DOC-2 — repository doc/content edits route to implement
# ---------------------------------------------------------------------------


def test_doc1_implement_trigger_covers_doc_edits():
    text = _skill("reflective-implement")
    assert text.count("including repository documentation and content edits") >= 2, (
        "doc-edit scope must appear in both frontmatter description and Trigger"
    )


def test_doc2_cheatsheet_doc_edit_cue_present_in_both_languages():
    en = _read(cheatsheet_en_path())
    zh = _read(cheatsheet_zh_tw_path())
    assert "**Doc edit not review**" in en
    assert "**文件修訂不是審查**" in zh


# ---------------------------------------------------------------------------
# GREEN-1 / GREEN-2 — spike/exploration framing
# ---------------------------------------------------------------------------


def test_green1_brief_spike_framing_present():
    text = _skill("reflective-brief")
    assert "Spike / exploration framing" in text
    assert "timebox" in text
    assert "disposable" in text


def test_green2_cheatsheet_spike_cue_present_in_both_languages():
    en = _read(cheatsheet_en_path())
    zh = _read(cheatsheet_zh_tw_path())
    assert "**Prototype/spike (criteria emerge by building)**" in en
    assert "**原型／spike（標準邊做邊浮現）**" in zh


def test_boundary_cues_stay_inside_quick_cue_block():
    """New cues live in the quick-cue block, before the dispatch section."""
    for path, cue in (
        (cheatsheet_en_path(), "**Doc edit not review**"),
        (cheatsheet_en_path(), "**Prototype/spike (criteria emerge by building)**"),
        (cheatsheet_zh_tw_path(), "**文件修訂不是審查**"),
        (cheatsheet_zh_tw_path(), "**原型／spike（標準邊做邊浮現）**"),
    ):
        text = _read(path)
        dispatch = text.index("## `reflective-dispatch`")
        assert text.index(cue) < dispatch, f"{cue!r} escaped the quick-cue block in {path.name}"


# ---------------------------------------------------------------------------
# ENT-2 — risk egress trigger + M7 packet-handling cross-link
# ---------------------------------------------------------------------------


def test_ent2_risk_egress_trigger_references_packet_lens():
    text = _skill("reflective-risk")
    assert "data egress" in text
    assert "external-adoption-review.md" in text


def test_ent2_external_adoption_review_lists_risk_surface():
    prompt = _read(PROMPT_LIBRARY_ROOT / "04-agent" / "external-adoption-review.md")
    purpose = prompt.split("## Scope", 1)[0]
    assert "`reflective-risk`" in purpose


# ---------------------------------------------------------------------------
# LONG-1 — handoff ledger bridge
# ---------------------------------------------------------------------------


def test_long1_handoff_ledger_bridge_present():
    text = _skill("reflective-handoff-retro")
    assert "instead of re-deriving state from the transcript" in text
    assert "flow-loop-harness" in text


# ---------------------------------------------------------------------------
# HOST-1 — installation fallback for hosts without Agent Skills
# ---------------------------------------------------------------------------


def test_host1_installation_fallback_section_present():
    text = _read(PROMPT_LIBRARY_ROOT / "SKILL_INSTALLATION.md")
    assert "## No Agent Skills support?" in text
    assert "## Prompt Sources" in text


# ---------------------------------------------------------------------------
# Record integrity — ledger rows and honesty note
# ---------------------------------------------------------------------------


def test_panel_record_ledger_rows_match_adopted_state():
    text = _read(RECORD)
    assert "## Candidate Adoption Ledger" in text
    for candidate_id in (
        "SOLO-2",
        "SOLO-3",
        "DOC-1",
        "DOC-2",
        "ZH-1",
        "ENT-2",
        "GREEN-1",
        "GREEN-2",
        "LONG-1",
        "HOST-1",
    ):
        assert f"| {candidate_id} |" in text, f"missing adopted ledger row {candidate_id}"
        row = next(line for line in text.splitlines() if line.startswith(f"| {candidate_id} |"))
        assert "**adopted 2026-07-12**" in row, f"{candidate_id} row must record adoption"
    for deferred_id in ("ENT-1", "LONG-2", "ZH-2"):
        row = next(line for line in text.splitlines() if line.startswith(f"| {deferred_id} |"))
        assert "**deferred**" in row, f"{deferred_id} row must stay deferred"


def test_panel_record_declares_single_host_execution():
    text = _read(RECORD)
    assert "## Execution mode (honesty note)" in text
    assert "resource_exhausted" in text
    assert "sequentially by one agent" in text
