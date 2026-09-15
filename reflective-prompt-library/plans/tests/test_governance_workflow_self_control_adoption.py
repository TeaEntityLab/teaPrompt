"""Guard the 2026-09-14 governance / workflow / self-control adoption pass.

GW-1's routing surfaces are guarded in test_validate_route_fixture.py (GD-19
probes and fixture-backing); GW-2 is itself a guard. This file pins the prompt
and record surfaces the pass touched and the dispositions of the held items,
so a held item cannot be adopted silently later (Adoption Guard Closure).
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
SKILLS = library_skills_dir()
RECORD = PLANS_DIR / "governance-workflow-self-control-adoption-2026-09-14.md"


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _ledger_row(text: str, candidate_id: str) -> str:
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split("## Evidence Actually Checked", 1)[0]
    for line in ledger.splitlines():
        if line.startswith(f"| {candidate_id} |"):
            return line
    raise AssertionError(f"ledger row {candidate_id} missing")


def test_gw4_search_before_add_sits_once_on_minimality_beside_og1():
    text = _read(SKILLS / "reflective-minimality" / "SKILL.md")
    og1 = "Apply the same test to prompt text: state each instruction once."
    line = next(ln for ln in text.splitlines() if og1 in ln)
    assert "search that surface for a sentence already carrying the clause" in line
    assert text.count("search that surface for a sentence already carrying the clause") == 1


def test_gw5_implement_traceability_is_one_step_and_steps_are_contiguous():
    text = _read(SKILLS / "reflective-implement" / "SKILL.md")
    workflow = text.split("## Before Editing", 1)[1].split("\n## ", 1)[0]
    step4 = next(ln for ln in workflow.splitlines() if ln.startswith("4. "))
    for clause in ("`Claim`", "`Falsifier / Verification`", "`unknown`, not zero demand", "recurrence gates"):
        assert clause in step4, clause
    numbers = [int(m.group(1)) for m in (re.match(r"^(\d+)\. ", ln) for ln in workflow.splitlines()) if m]
    assert numbers == list(range(1, len(numbers) + 1)), numbers


def test_gw3_status_family_map_in_glossary():
    text = _read(glossary_path())
    assert "## Ledger Status Families / 帳冊狀態對照" in text
    section = text.split("## Ledger Status Families / 帳冊狀態對照", 1)[1].split("\n## ", 1)[0]
    for literal in ("`open`", "`unverified`", "`needs-qualification`", "`pending`", "`asserted`", "`unverifiable`", "`stale`"):
        assert literal in section, literal


def test_gw3_every_skill_status_list_is_pinned():
    """The GLOSSARY map says each skill's status list is guarded; brief and implement
    are pinned by the GD / GA adoption guards, research and review here."""
    research = _read(SKILLS / "reflective-research" / "SKILL.md")
    assert "Status is one of `unverified`, `verified`, `refuted`, `needs-qualification`, `stale`." in research
    review = _read(SKILLS / "reflective-review" / "SKILL.md")
    assert "`asserted` / `verified` / `refuted` / `unverifiable`" in review


def test_gw6_examples_cover_the_four_templates():
    loop = _read(SKILLS / "examples" / "flow-loop-harness.examples.md")
    for token in ("Writer-critic", "floor_ok()", "MAX_ROUNDS=4", "Multi-wave fan-out", "MAX_WAVES=4"):
        assert token in loop, token
    control = _read(SKILLS / "examples" / "flow-control-generator.examples.md")
    for token in ("Orchestrator-workers", "MAX_WORKERS=4 / MAX_TASKS=12", "DAG executor", "exit 4 before any node runs"):
        assert token in control, token
    # Second pass: examples state observed rig results, never mechanisms the templates lack.
    assert "read-only plus a scratch dir" not in control
    assert "per-node gate on output presence" not in control
    for text in (loop, control):
        assert "Rig-tier (run 2026-09-14)" in text


def test_gw7_usage_log_covers_all_registered_packs():
    from validate_skill_examples import DOMAIN_PACK_SKILLS  # noqa: E402

    text = _read(PLANS_DIR / "flow-pack-usage-log.md")
    entries = text.split("## Entries", 1)[1].split("## Template maintenance", 1)[0]
    for pack in DOMAIN_PACK_SKILLS:
        if pack in ("flow-control-generator", "flow-loop-harness"):
            continue  # the original zero-state row covers the two 2026-07-11 packs
        assert f"`{pack}`" in entries, f"usage log has no row for {pack}"
    assert "## Template maintenance (not invocations)" in text
    assert "skill-verification-panel-2026-09-05.md" in text


def test_record_dispositions_and_held_items_stay_held():
    text = _read(RECORD)
    for n in range(1, 8):
        assert "**Adopted 2026-09-14**" in _ledger_row(text, f"GW-{n}"), n
    assert "**Rejected on evidence 2026-09-14**" in _ledger_row(text, "GW-8")
    assert "**Fixed 2026-09-14**" in _ledger_row(text, "GW-15")
    assert "## Second-Pass Review (2026-09-14)" in text
    for n in range(1, 14):
        assert f"| S{n} |" in text, n
    for n, status in ((9, "date-gated"), (10, "date-gated"), (11, "trigger unfired"), (12, "named gates"), (13, "host-only"), (14, "panel-decided")):
        assert f"**Held — {status}**" in _ledger_row(text, f"GW-{n}"), n
    gd = _read(PLANS_DIR / "governed-delivery-adoption-2026-09-03.md")
    assert "| GD-19 |" in gd and "Measured 2026-09-14" in gd
    # The held reserves keep their absence on the skills (their own records guard the wording).
    implement = _read(SKILLS / "reflective-implement" / "SKILL.md")
    assert "extra-work offer from the same run" not in implement, "TK-1 reserve landed without its trigger"
