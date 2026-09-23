"""Guard the verification-map-generator pack adoption at its surfaces.

Registered 2026-09-23 after the four-product recurrence gate (wsgiLite.js,
fpGo, fpEs, fpRust). This file exists because the pack shipped with zero
content pins — the other four packs each had an adoption-state guard and this
one did not (found by the 2026-09-23 constraint review).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402
from validate_skill_examples import DOMAIN_PACK_SKILLS  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
SKILLS = library_skills_dir()
PACK = SKILLS / "verification-map-generator" / "SKILL.md"
EXAMPLES = SKILLS / "examples" / "verification-map-generator.examples.md"
PK = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
IMPLEMENT = SKILLS / "reflective-implement" / "SKILL.md"
LINT_WARNING_CHARS = 20000

# The four failure classes are the pack's canonical contract. Spellings differ
# per surface — the pack table uses "Doc drift"/"Spec/oracle error" while
# reflective-implement writes "doc/map drift"/"spec/oracle error" — so each
# surface is pinned against its own wording, and the class *set* is the
# invariant.
PACK_CLASSES = ("Product regression", "Doc drift", "Spec/oracle error", "Harness failure")
IMPLEMENT_CLASSES = ("product regression", "doc/map drift", "spec/oracle error", "harness failure")

PACK_NEVER = (
    "Do not write the map from memory of the API",
    "Do not label seeded bugs",
    "Do not let the map describe behavior the product does not have",
    "Do not add driver/test files inside the product repo",
    "Do not treat a green run as proof the map is right",
)

def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _section(text: str, heading: str) -> str:
    assert heading in text, f"pack lost {heading!r}"
    return text.split(heading, 1)[1].split("\n## ", 1)[0]


# Registered, self-labelled, outside dispatch routes.
def test_registered_self_labelled_and_off_dispatch_routes():
    assert "verification-map-generator" in DOMAIN_PACK_SKILLS
    text = _read(PACK)
    assert "Domain-pack skill" in text
    assert "not one of the nine frozen core workflow skills" in text
    route = _read(SKILLS / "reflective-dispatch" / "SKILL.md")
    assert "verification-map-generator" not in route


def test_absent_from_route_fixtures():
    for fixture in (
        "route-001-paraphrase-eval.yaml",
        "route-002-holdout-eval.yaml",
        "route-003-adversarial-eval.yaml",
    ):
        assert "verification-map-generator" not in _read(PLANS_DIR / fixture), fixture


def test_frontmatter_declares_pack_metadata():
    meta = _read(PACK).split("---", 2)[1]
    assert "name: verification-map-generator" in meta
    assert "human_review_required: false" in meta
    assert "context_load: medium" in meta


# The canonical four-way classification table.
def test_pack_canonical_classification_table_has_four_classes():
    section = _section(_read(PACK), "## Failure Classification")
    for cls in PACK_CLASSES:
        assert cls in section, f"pack table lost class {cls!r}"
    assert "Oracles read-only" in section


# The same four classes must survive in reflective-implement's paragraph —
# the second copy of the canonical contract (found unpinned 2026-09-23).
def test_implement_classification_paragraph_keeps_four_classes():
    text = _read(IMPLEMENT)
    assert "classify the failure's owning surface" in text
    for cls in IMPLEMENT_CLASSES:
        assert cls in text, f"reflective-implement lost class {cls!r}"
    # Oracles stay read-only in the implement copy too.
    assert "oracles are read-only" in text


def test_pack_never_block_keeps_every_boundary_bullet():
    never = _section(_read(PACK), "## Never")
    for bullet in PACK_NEVER:
        assert bullet in never, f"pack Never lost {bullet[:60]!r}"


def test_generation_procedure_and_maintenance_rule_present():
    text = _read(PACK)
    assert "## Generation Procedure" in text
    assert "## Maintenance Rule" in text
    assert "Event-driven, not calendar-driven" in text
    assert "verification_status: failed" in text


def test_examples_pointer_and_file_exist():
    text = _read(PACK)
    assert "verification-map-generator.examples.md" in text
    examples = _read(EXAMPLES)
    assert len(examples) >= 200


# Adoption evidence: the PK durable lesson records the recurrence gate and
# the promotion to this pack.
def test_project_knowledge_records_adoption_evidence():
    pk = _read(PK)
    assert "verification-map-generator" in pk
    assert "Review trigger" in pk
    assert "registered 2026-09-23" in pk


def test_pack_body_stays_under_lint_warning_threshold():
    body = _read(PACK).split("---", 2)[2]
    assert len(body) <= LINT_WARNING_CHARS, len(body)
