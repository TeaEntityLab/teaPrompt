"""Wire the eval proxy router's keyword table to the production routing surface.

The 2026-09-23 constraint review found ParaphraseRouter's keyword table was
hand-maintained and disconnected from the SKILL.md descriptions the host LLM
actually routes on — the eval measured a proxy no production surface consumes.
This guard asserts the two stay aligned: every scope term a SKILL.md
description advertises must exist in that workflow's keyword table, so a
description edit that widens scope fails here until the table follows.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402
from route_paraphrase_eval import ParaphraseRouter  # noqa: E402

SKILLS = library_skills_dir()

# Scope terms each SKILL.md description advertises; each must appear in the
# workflow's keyword table. Derived from the descriptions on 2026-09-23 —
# extend when a description gains scope, never to pin prose wording.
DESCRIPTION_SCOPE_TERMS = {
    "reflective-brief": ("falsifiability", "next step"),
    "reflective-spec-plan": ("no-code", "stateful", "resumable workflow"),
    "reflective-implement": ("coding", "content edits"),
    "reflective-minimality": ("overbuild", "anti-bloat", "complexity audit", "debt ledger"),
    "reflective-review": ("diffs", "specs", "ai outputs", "decisions"),
    "reflective-research": ("deepwiki", "synthesis", "platform comparison"),
    "reflective-risk": ("deletion", "dry-run", "financial", "legal", "medical"),
    "reflective-handoff-retro": ("checklists", "session transfer", "context compaction"),
    "reflective-dispatch": ("convert prompts", "prompt library"),
}


def _description(skill: str) -> str:
    text = (SKILLS / skill / "SKILL.md").read_text(encoding="utf-8")
    m = re.search(r"^description:\s*(.+?)(?=^\w+:|\Z)", text, re.S | re.M)
    assert m, f"{skill}: no frontmatter description"
    return m.group(1).lower()


def test_every_routed_workflow_has_a_skill_description():
    router = ParaphraseRouter()
    for workflow in router.routing_rules:
        desc = _description(workflow)
        assert len(desc) > 40, f"{workflow}: description too thin to route on"


def test_description_scope_terms_exist_in_keyword_table():
    router = ParaphraseRouter()
    for workflow, terms in DESCRIPTION_SCOPE_TERMS.items():
        assert workflow in router.routing_rules, f"{workflow} unrouted"
        table = router.routing_rules[workflow]
        for term in terms:
            assert term in table, (
                f"{workflow}: description scope term {term!r} missing from "
                "keyword table — the eval proxy no longer covers what the "
                "production description advertises"
            )


def test_scope_terms_still_appear_in_descriptions():
    # Reverse direction: a term removed from the description must not linger
    # as a stale requirement here. Full-term match — a first-word stem is
    # nearly vacuous ("ai" survives inside "domain"/"email").
    for workflow, terms in DESCRIPTION_SCOPE_TERMS.items():
        desc = _description(workflow)
        for term in terms:
            assert term in desc, (
                f"{workflow}: pinned scope term {term!r} no longer appears in "
                "the SKILL.md description — update DESCRIPTION_SCOPE_TERMS"
            )
