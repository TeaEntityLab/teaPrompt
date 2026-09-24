# features/ — TeaPrompt verification map

Companion to `../VERIFY.md`. One file per feature area; each carries
`source_commit` / `last_verified_at` / `verification_status` metadata.

| File | Area | Drive surface |
| --- | --- | --- |
| `test-suite.md` | Governance pytest suite | `plans/tests/` (1290 tests at `7147e91`) |
| `validators.md` | Standalone gate scripts | 7 `validate_*.py` + `lint_skills.py` (8 scripts) |
| `route-evals.md` | Routing paraphrase evals | 3 YAML fixtures via `route_paraphrase_eval.py` |
| `registry.md` | Skill registry cardinality | `validate_skill_examples.py` lists |

Maintenance rule: event-driven. Re-verify a feature file when its covered
source changes; bump `source_commit` / `last_verified_at`. A
`verification_status: failed` means the repo changed — classify before
editing the map.
