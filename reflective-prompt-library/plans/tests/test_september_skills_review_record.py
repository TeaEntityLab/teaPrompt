"""Guard the 2026-09-14 September skills review: merges hold, retired
duplicates stay retired, the planning layer keeps its September rows.

Under Adoption Guard Closure the merged sentences are pinned by the adoption
guards that own them (governable-autonomy, governed-delivery); this file pins
the *absence* of the retired copies, the fixes no other guard covers, and the
roadmap/runbook/plan rows the review added.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
SKILLS = library_skills_dir()
RECORD = PLANS_DIR / "september-skills-review-2026-09-14.md"
ROADMAP = PLANS_DIR / "whole-project-roadmap-2026-07-11.md"
PLAN = PLANS_DIR / "whole-project-plan-2026-07-11.md"
RUNBOOK = PLANS_DIR / "checkpoint-2026-10-11-runbook.md"

# Retired duplicate copies: each must not come back beside its merged twin.
RETIRED = {
    "reflective-implement": (
        "return to the ledger, roll back to the last verified state where the host supports it, change strategy, or escalate.",
        "when a signature repeats after a correction, exit by rollback",
    ),
    "reflective-review": (
        "and whether they are independent; a high-risk PASS needs at least one non-model channel.",
        "- Same-model, same-context multi-role review is one epistemic channel",
    ),
    "reflective-research": (
        "- Say which kind of freshness applies:",
        "- Each evidence entry names the claim, the source, the attester, the freshness kind, and the date checked.",
    ),
    "reflective-dispatch": ("Prefer evidence over confidence. Do not claim tool execution",),
    "reflective-minimality": ("- Do not remove trust-boundary validation, auth, privacy, security, data-loss prevention",),
    "reflective-handoff-retro": ("rebuilds from artifacts, not from the transcript", "gate evidence, not from the transcript"),
}

# Each merged rule is stated exactly once in its skill (the distinctive clause).
STATED_ONCE = {
    "reflective-implement": ("never by an identical retry",),
    "reflective-review": ("never solely pass a high-risk claim", "a scope proposal, not authorization to widen"),
    "reflective-research": ("which kind of freshness applies",),
    "reflective-dispatch": ("Prefer evidence over confidence",),
}


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _skill(name: str) -> str:
    return _read(SKILLS / name / "SKILL.md")


def test_retired_duplicates_stay_retired():
    for name, fragments in RETIRED.items():
        text = _skill(name)
        for fragment in fragments:
            assert fragment not in text, f"{name}: retired duplicate returned: {fragment[:60]!r}"


def test_merged_rules_stated_once():
    for name, fragments in STATED_ONCE.items():
        text = _skill(name)
        for fragment in fragments:
            assert text.count(fragment) == 1, f"{name}: {fragment!r} count != 1"


def test_glossary_defines_stale_and_unknown():
    text = _read(glossary_path())
    for heading in ("## Stale / 失效", "## Unknown / 未知"):
        assert heading in text, heading
    assert "freshness transition, not a lowered bar" in text
    assert "never read as zero" in text


def test_example_files_fixed():
    scaffold = _read(SKILLS / "examples" / "agent-governance-scaffold.examples.md")
    assert "authorization_epoch" not in scaffold and "activation_epoch" in scaffold
    generator = _read(SKILLS / "examples" / "flow-control-generator.examples.md")
    example_2 = generator.split("## Example 2", 1)[1].split("## Example 3", 1)[0]
    assert "## Gates" in example_2 and "verify-merged.sh" in example_2


def test_record_ledger_and_dispositions():
    text = _read(RECORD)
    for heading in ("## Panel Consensus", "## Concern Ledger", "## Roadmap Additions", "## Evidence Actually Checked", "## Falsifiability", "## Completion Ledger"):
        assert heading in text, heading
    assert "AGREE WITH CHANGES — 6/6" in text
    for n in range(1, 23):
        assert f"| C{n} |" in text, n
    for fixed in range(1, 15):
        assert "**Fixed**" in text.split(f"| C{fixed} |", 1)[1].split("\n", 1)[0], fixed


def test_planning_layer_carries_september():
    roadmap = _read(ROADMAP)
    for token in (
        "Same-day adoption collision check",
        "Flow-pack size budget",
        "`governed-delivery` recurrence checkpoint",
        "GD↔AGS redundancy-in-use",
        "### Adopted 2026-09-03 → 2026-09-14",
        "| I-1 / A-5 —",
        "| GD-19 —",
        "| GD-16 —",
        "| TK-1 —",
        "| E-5 —",
        "Roadmap self-review 2026-09-14",
        "**fired 2026-09-13**",
    ):
        assert token in roadmap, f"roadmap lost {token!r}"
    plan = _read(PLAN)
    assert "Four registered domain packs outside core routing" in plan
    assert "Fired and reconciled 2026-09-14" in plan
    runbook = _read(RUNBOOK)
    assert "## Agenda item 7 — `governed-delivery` recurrence checkpoint" in runbook
    assert "`## GD outcome`" in runbook
    assert "absence stays `unknown`, never zero" in runbook


def test_agentflow_records_corrected():
    delta = _read(PLANS_DIR / "agentflow-8.2-delta-survey-2026-09-13.md")
    assert "under every wording" not in delta
    assert "0/1 in draft 1" in delta
    survey = _read(PLANS_DIR / "agentflow-survey-2026-09-05.md")
    assert "gate settled: trigger (b) fired, trigger (a) moot" in survey
