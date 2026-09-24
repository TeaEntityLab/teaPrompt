#!/usr/bin/env python3
"""
Skill Examples Validator (deterministic, CI-safe)

Ensures every core workflow skill and registered domain-pack skill has a
matching worked example under skills/examples/. Round 11 panel compromise:
gate example parity without adding new skill surface area. Domain packs were
registered by the 2026-07-11 flow-control pack panel (Option B): CORE_SKILLS
stays the frozen nine; DOMAIN_PACK_SKILLS is the only other legitimate set of
SKILL.md directories under skills/.
"""

import sys
from pathlib import Path

CORE_SKILLS = [
    "reflective-dispatch",
    "reflective-brief",
    "reflective-spec-plan",
    "reflective-implement",
    "reflective-minimality",
    "reflective-review",
    "reflective-research",
    "reflective-risk",
    "reflective-handoff-retro",
]

# Registered domain packs: host-invoked script/artifact-generation skills. Not
# core routing surface; not selectable by reflective-dispatch route rows. See
# plans/flow-control-pack-panel-record-2026-07-11.md,
# plans/agent-governance-scaffold-adoption-2026-07-17.md, and
# plans/governed-delivery-adoption-2026-09-03.md before extending.
# Admission checklist for a new pack (each is a guarded surface — the 2026-09-23
# verification-map-generator registration touched all of them):
#   SKILL.md + skills/examples/<name>.examples.md; this registry;
#   skills/skill-map.md pack table; SKILL_TRIGGER_CHEATSHEET.md + .zh-TW.md
#   appendices; SKILL_INSTALLATION.md install_domain_packs_{copy,symlink} loops;
#   plans/flow-pack-usage-log.md row; cardinality pins in
#   test_ga_skills_coverage_panel_record.py and
#   test_installed_skills_general_lessons_record.py.
DOMAIN_PACK_SKILLS = [
    "flow-control-generator",
    "flow-loop-harness",
    "agent-governance-scaffold",
    "governed-delivery",
    "verification-map-generator",
]

MIN_EXAMPLE_CHARS = 200

# Every registered pack must appear on each of these surfaces — the 2026-09-23
# constraint review found pack admission was convention-driven (each surface
# updated by hand) rather than registry-driven, so the fifth pack shipped with
# gaps (zh-TW install guide still said four packs). This manifest makes the
# checklist executable: add a pack to DOMAIN_PACK_SKILLS and every surface
# below must name it.
PACK_SURFACES = [
    "reflective-prompt-library/skills/skill-map.md",
    "reflective-prompt-library/skills/SKILL_TRIGGER_CHEATSHEET.md",
    "reflective-prompt-library/skills/SKILL_TRIGGER_CHEATSHEET.zh-TW.md",
    "reflective-prompt-library/SKILL_INSTALLATION.md",
    "reflective-prompt-library/SKILL_INSTALLATION.zh-TW.md",
    "reflective-prompt-library/plans/flow-pack-usage-log.md",
]


def main() -> int:
    repo_root = Path(__file__).parent.parent.parent
    skills_dir = repo_root / "reflective-prompt-library" / "skills"
    examples_dir = skills_dir / "examples"

    print(f"Validating skill examples in: {repo_root}")
    print("=" * 60)

    errors = []

    if not examples_dir.is_dir():
        print(f"\n❌ Missing examples directory: {examples_dir.relative_to(repo_root)}")
        return 1

    for skill in CORE_SKILLS + DOMAIN_PACK_SKILLS:
        skill_file = skills_dir / skill / "SKILL.md"
        example_file = examples_dir / f"{skill}.examples.md"

        if not skill_file.is_file():
            errors.append(f"Missing skill contract: {skill_file.relative_to(repo_root)}")
            continue
        if not example_file.is_file():
            errors.append(f"Missing example file: {example_file.relative_to(repo_root)}")
            continue

        content = example_file.read_text(encoding="utf-8").strip()
        if len(content) < MIN_EXAMPLE_CHARS:
            errors.append(
                f"{example_file.relative_to(repo_root)}: too short "
                f"({len(content)} chars; minimum {MIN_EXAMPLE_CHARS})"
            )

        pointer = f"<skills-root>/examples/{skill}.examples.md"
        skill_text = skill_file.read_text(encoding="utf-8")
        if pointer not in skill_text:
            errors.append(
                f"{skill_file.relative_to(repo_root)}: missing installed examples "
                f"pointer {pointer!r}"
            )

    # Registry-driven surface coverage: every pack on every required surface.
    for surface in PACK_SURFACES:
        surface_path = repo_root / surface
        if not surface_path.is_file():
            errors.append(f"Missing pack surface: {surface}")
            continue
        surface_text = surface_path.read_text(encoding="utf-8")
        for pack in DOMAIN_PACK_SKILLS:
            if pack not in surface_text:
                errors.append(f"{surface}: does not name pack {pack!r}")

    # Cardinality self-check: the loops above iterate the lists themselves, so
    # a dropped entry passes this script unless asserted here. The pytest pins
    # (test_ga_skills_coverage_panel_record.py) also catch it; this keeps the
    # validator correct when run standalone. Nine core is the frozen invariant;
    # five packs is the current registered cardinality — a pack admission or
    # demotion updates the list AND this pin in one change.
    if len(CORE_SKILLS) != 9:
        errors.append(
            f"CORE_SKILLS has {len(CORE_SKILLS)} entries, expected 9 "
            "(frozen nine; a tenth core skill needs the promotion gate)"
        )
    if len(set(CORE_SKILLS)) != len(CORE_SKILLS):
        errors.append("CORE_SKILLS contains duplicates")
    if len(DOMAIN_PACK_SKILLS) != 5:
        errors.append(
            f"DOMAIN_PACK_SKILLS has {len(DOMAIN_PACK_SKILLS)} entries, "
            "expected 5 (update this pin in the same change as a pack "
            "admission or demotion)"
        )
    if len(set(DOMAIN_PACK_SKILLS)) != len(DOMAIN_PACK_SKILLS):
        errors.append("DOMAIN_PACK_SKILLS contains duplicates")

    if errors:
        print(f"\n❌ {len(errors)} skill example violation(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(
        f"\n✅ All {len(CORE_SKILLS)} core + {len(DOMAIN_PACK_SKILLS)} "
        "domain-pack skills have example files"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
