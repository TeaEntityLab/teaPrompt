---
feature: skill registry cardinality
source_commit: 13fc95c
last_verified_at: 2026-10-07
verification_status: passing
---

# Skill registry cardinality

Human-reviewed RV-05 migration approved 2026-10-07: ten admitted domain packs,
nine core skills, and nineteen installed skill contracts. `source_commit` names
the pre-repair base; this migration is currently a working-tree change.

## Entry points

- `reflective-prompt-library/plans/validate_skill_examples.py` — `CORE_SKILLS`
  (frozen nine) and `DOMAIN_PACK_SKILLS` (ten) lists.
- `reflective-prompt-library/skills/` — directories must match the registry.

## Drive

```bash
find reflective-prompt-library/skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l   # expect: 19 (9 core + 10 packs)
python3 reflective-prompt-library/plans/validate_skill_examples.py
```

Expected validator tail: `All 9 core + 10 domain-pack skills have example files`.

## Observable outcomes

- Exactly 9 core skills: reflective-dispatch, reflective-brief,
  reflective-spec-plan, reflective-implement, reflective-minimality,
  reflective-review, reflective-research, reflective-risk,
  reflective-handoff-retro.
- Exactly 10 domain packs: flow-control-generator, flow-loop-harness,
  agent-governance-scaffold, governed-delivery, verification-map-generator,
  headless-agent-cli-contract, arm-blinded-eval-harness,
  acceptance-join-validator, golden-benchmark-runner, router-trace-linter.
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

`find` count, validator output, and the offending directory/file name.
