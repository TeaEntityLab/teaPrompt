---
feature: skill registry cardinality
source_commit: c1cdf14
last_verified_at: 2026-09-23
verification_status: passing
---

# Skill registry cardinality

## Entry points

- `reflective-prompt-library/plans/validate_skill_examples.py` — `CORE_SKILLS`
  (frozen nine) and `DOMAIN_PACK_SKILLS` (five) lists.
- `reflective-prompt-library/skills/` — directories must match the registry.

## Drive

```bash
find reflective-prompt-library/skills -name SKILL.md -mindepth 2 -maxdepth 2 | wc -l   # expect: 14 (9 core + 5 packs)
python3 reflective-prompt-library/plans/validate_skill_examples.py
```

Expected validator tail: `All 9 core + 5 domain-pack skills have example files`.

## Observable outcomes

- Exactly 9 core skills: reflective-dispatch, reflective-brief,
  reflective-spec-plan, reflective-implement, reflective-minimality,
  reflective-review, reflective-research, reflective-risk,
  reflective-handoff-retro.
- Exactly 5 domain packs: flow-control-generator, flow-loop-harness,
  agent-governance-scaffold, governed-delivery, verification-map-generator.
- Every registered skill has `skills/<name>/SKILL.md` and
  `skills/examples/<name>.examples.md`.

## Failure paths

- A 10th core skill or unregistered `skills/` directory → product regression
  (tenth-core promotion gate is human-approval + recurrence evidence).
- A pack missing from any admission surface (skill-map table, cheatsheet
  appendices, SKILL_INSTALLATION loops, usage-log row, cardinality pins) →
  product regression; the manifest in `validate_skill_examples.py` lists all
  guarded surfaces.

## Evidence

`ls` count, validator output, and the offending directory/file name.
