"""Guard the 2026-09-10 OpenAI model guidance survey.

Pins:
- the record's required shape and the nine surveyed model identifiers
- each adopted sentence present exactly once at its single surface, and OG-2
  seated as a Definition-of-Done check (not a step after "Stop")
- no vendor model or company name on any durable surface (clean-room)
- the copy boundary: no landed sentence shares more than four consecutive
  words with the vendor sentence it restates (quoted in the record only)
- the Decision Index and case-study rows point at the record
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "openai-model-guidance-survey-2026-09-10.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
AGENT_DOCS = PROMPT_LIBRARY_ROOT / "04-agent"
SKILLS = library_skills_dir()

# Vendor model and company names: never on a durable surface. Bare "codex" is
# excluded on purpose — it names a TeaPrompt source file (06-repo/codex-opencode.md).
VENDOR_TOKENS = re.compile(r"\bGPT-?[0-9]|\bgpt-?[0-9]|\bOpenAI\b|\bopenai\b|\bAstra\b|\bastra\b")

# Vendor sentences each adoption restates. They are quoted in the record's
# candidate rows; the copy boundary keeps them out of every skill.
SOURCE = {
    "OG-1": "State each instruction once. Removing repeated instructions and examples and simplifying tool descriptions can improve task performance and token efficiency.",
    "OG-2": "Reduce or remove detailed step-by-step process guidance. Let the model choose the path unless the product requires that path.",
    "OG-3": "Do not write tests for reversible, low-impact changes that mirror the implementation. If you do choose to verify your work with tests, make sure that the tests are meaningful and necessary.",
    "OG-4": "Do not search again to improve phrasing, add examples, cite nonessential details, or support wording that can safely be made more generic.",
}
# The landed sentences, pinned in full at their single surfaces.
LANDED = {
    "OG-1": "Apply the same test to prompt text: state each instruction once. A rule repeated across sections adds tokens, invites wording drift between copies, and can over-weight the instruction or spend reasoning reconciling near-duplicates.",
    "OG-2": "Requirements name the destination — outcome and acceptance criteria — not the route; a prescribed step sequence appears only where the product itself fixes it",
    "OG-3": "Scale verification depth to the risk and reversibility of the change; a test that merely mirrors the implementation proves nothing at any risk level. For a reversible, low-impact edit, the narrowest check that would fail if the change were wrong is enough — still run and read — then stop once the claim is proven.",
    "OG-4": "A passed gate is not reopened for polish: no further retrieval to reword a claim, find a nicer example, or attach a citation the decision does not need; if a sentence needs more support than the ledger holds, generalize the sentence rather than fetch more.",
}
SURFACE = {
    "OG-1": SKILLS / "reflective-minimality" / "SKILL.md",
    "OG-2": SKILLS / "reflective-spec-plan" / "SKILL.md",
    "OG-3": SKILLS / "reflective-implement" / "SKILL.md",
    "OG-4": SKILLS / "reflective-research" / "SKILL.md",
}
MAX_SHARED_RUN = 4

MODELS = ("gpt-4.1", "gpt-5", "gpt-5.1", "gpt-5.2", "gpt-5.3-codex", "gpt-5.4", "gpt-5.5", "gpt-5.6", "gpt-6-astra")


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _durable_surfaces() -> list[Path]:
    # Prompt-level surfaces only. The install guide is excluded on purpose: it
    # identifies hosts by vendor (a Codex config path, a skills-repository URL),
    # which is host naming, not surveyed guidance text.
    return sorted(SKILLS.glob("*/SKILL.md")) + [glossary_path()] + sorted(AGENT_DOCS.glob("*.md"))


def _tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9'-]+", text.lower())


def _longest_shared_run(a: str, b: str) -> int:
    ta, tb = _tokens(a), _tokens(b)
    best = 0
    for i in range(len(ta)):
        for j in range(len(tb)):
            n = 0
            while i + n < len(ta) and j + n < len(tb) and ta[i + n] == tb[j + n]:
                n += 1
            best = max(best, n)
    return best


def test_survey_record_shape():
    text = _read(RECORD)
    assert text.splitlines()[2].startswith("> **Status:")
    for heading in (
        "## Source",
        "## Cross-Model Themes",
        "## Candidate Adoption Ledger",
        "## Panel Verdicts",
        "## Adopted Wording",
        "## Post-Review Revisions",
        "## Evidence Separation",
        "## Falsifiability",
    ):
        assert heading in text, heading
    assert "[INFERENCE]" in text
    assert "License: not determined" in text and "Copy boundary" in text
    for model in MODELS:
        assert f"`{model}`" in text, model
    for candidate, source in SOURCE.items():
        assert source in text, f"{candidate} source quote missing from record"


def test_verdicts_recorded():
    text = _read(RECORD)
    verdicts = text.split("## Panel Verdicts", 1)[1].split("## Adopted Wording", 1)[0]
    for candidate in ("OG-1", "OG-2", "OG-3", "OG-4"):
        assert re.search(rf"^\| {candidate} \| \*\*Adopted\*\* \|", verdicts, re.M), candidate
    for candidate in ("OG-5", "OG-6", "OG-7"):
        assert re.search(rf"^\| {candidate} \| \*?\*?Rejected", verdicts, re.M), candidate
    assert "already implicit" in verdicts.lower()


def test_each_adopted_sentence_present_once_at_its_surface():
    for candidate, sentence in LANDED.items():
        assert _read(SURFACE[candidate]).count(sentence) == 1, candidate
        for other, path in SURFACE.items():
            if other != candidate:
                assert sentence not in _read(path), f"{candidate} wording also on {path.name}"


def test_og2_is_a_definition_of_done_check_not_a_step_after_stop():
    text = _read(SKILLS / "reflective-spec-plan" / "SKILL.md")
    workflow = text.split("## Workflow", 1)[1].split("## Test Plan Mode", 1)[0]
    assert re.search(r"^   - " + re.escape(LANDED["OG-2"]) + r"$", workflow, re.M)
    assert not re.search(r"^7\. ", workflow, re.M), "workflow gained a step after 'Stop'"
    assert workflow.rstrip().endswith("6. Stop at the smallest plan that can be executed and reviewed.")


def test_og3_scopes_depth_not_the_mirroring_prohibition():
    text = _read(SKILLS / "reflective-implement" / "SKILL.md")
    assert "proves nothing at any risk level" in text
    assert "mirror the implementation for reversible" not in text
    # A-7a and OG-3 are separate paragraphs, not a fused block.
    assert "did not make.\n\nScale verification depth" in text


def test_no_vendor_tokens_on_durable_surfaces():
    surfaces = _durable_surfaces()
    assert len(surfaces) >= 20, "surface set unexpectedly small"
    for path in surfaces:
        hits = VENDOR_TOKENS.findall(_read(path))
        assert not hits, f"{path.name}: {hits}"


def test_copy_boundary_no_long_verbatim_run_with_vendor_source():
    for candidate, sentence in LANDED.items():
        run = _longest_shared_run(SOURCE[candidate], sentence)
        assert run <= MAX_SHARED_RUN, f"{candidate}: {run}-word run shared with the vendor sentence"


def test_indexes_point_to_the_record():
    knowledge = _read(PROJECT_KNOWLEDGE)
    assert "[record](plans/openai-model-guidance-survey-2026-09-10.md)" in knowledge
    assert re.search(r"^- 2026-09-10 OpenAI model guidance survey", knowledge, re.M)
    assert '"survey these model guidance differences"' not in knowledge, "paraphrase must not be quoted as user text"
    case_studies = _read(CASE_STUDIES)
    assert case_studies.count("openai-model-guidance-survey-2026-09-10.md") >= 2  # comparison row + state ledger row
