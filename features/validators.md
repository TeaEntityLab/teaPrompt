---
feature: standalone validators
source_commit: c1cdf14
last_verified_at: 2026-09-23
verification_status: passing
---

# Standalone validators

## Entry points

Eight scripts in `reflective-prompt-library/plans/`, each runnable solo:

```bash
P=reflective-prompt-library/plans
python3 $P/validate_links.py              # ref_file/ref_snippet/md links/frontmatter
python3 $P/lint_skills.py                 # prompt/skill lint (see quirk below)
python3 $P/validate_governance.py         # skill governance metadata
python3 $P/validate_project_knowledge.py  # PK authority boundary
python3 $P/validate_record_hygiene.py     # plans/ record hygiene
python3 $P/validate_benchmark_fixture.py  # benchmark-tasks.json sync
python3 $P/validate_skill_examples.py     # core+pack registry, example files
python3 $P/validate_route_fixture.py      # ROUTE-002/003 minimum counts
```

## Observable outcomes

- Every script exits 0 and prints a ✅-style success line.
- `lint_skills.py` exits 0 with **one known warning**
  (`agent-governance-scaffold` body length, accepted R10 debt). A *second*
  warning or any error is a finding.

## Failure paths

- `validate_links` errors → doc drift or a broken rename (classify by whether
  the target file actually moved).
- `validate_project_knowledge` failure → authority-boundary violation:
  project-judgement file prescribing agent behavior. Product regression.
- `validate_skill_examples` failure → registry/surface drift. Product
  regression unless the change was an approved pack admission.
- `validate_route_fixture` failure → holdout/adversarial fixture shrank below
  floor. Product regression (fixtures only grow per R8).

## Evidence

Script name, exit code, and the error block.
