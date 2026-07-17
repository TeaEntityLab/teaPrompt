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
# plans/flow-control-pack-panel-record-2026-07-11.md and
# plans/agent-governance-scaffold-adoption-2026-07-17.md before extending.
DOMAIN_PACK_SKILLS = [
    "flow-control-generator",
    "flow-loop-harness",
    "agent-governance-scaffold",
]

MIN_EXAMPLE_CHARS = 200


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
