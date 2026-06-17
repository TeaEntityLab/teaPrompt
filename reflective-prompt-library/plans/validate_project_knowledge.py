#!/usr/bin/env python3
"""
PROJECT_KNOWLEDGE.md Contract Validator

Enforces structural invariants that keep PROJECT_KNOWLEDGE.md a
*non-authoritative project-judgement* layer rather than a second agent
rulebook. Project-design principles may still be normative for product and
architecture choices. Dead-link and markdown-reference checks are intentionally
left to validate_links.py; this validator checks only narrow, observable signals:

1. Required sections exist (Governing Principles, Current Direction,
   Durable Lessons, Decision Index).
2. The preamble declares the authority boundary and points to AGENTS.md / SKILL.md.
3. No explicit agent-directed rules, including inside blockquotes. This is a
   high-precision guardrail, not proof of semantic authority separation.
4. Every Durable Lesson has a non-empty `Evidence:` pointer.
5. Every milestone has a valid `Status:` (active/planned/done).
6. The Decision Index is non-empty and every entry carries a link pointer.

Exit code 0 when valid, 1 when any error is found, so it can gate CI.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List

REQUIRED_SECTIONS = [
    "Governing Principles",
    "Current Direction",
    "Durable Lessons",
    "Decision Index",
]

# These patterns intentionally require an agent-like subject or an operational
# imperative. Generic modal words are valid in project-design principles and do
# not, by themselves, establish authority.
AGENT_DIRECTIVE_PATTERNS = [
    r"\b(?:the\s+)?(?:agent|agents|assistant|assistants|model|models|codex|claude|you)\s+"
    r"(?:must(?:\s+not)?|shall|(?:is|are)\s+required\s+to)\b",
    r"^\s*(?:[-*]\s+|>\s*)?(?:always|never)\s+"
    r"(?:run|execute|invoke|call|read|write|edit|delete|commit|push|deploy|install|use)\b",
]

VALID_STATUSES = {"active", "planned", "done"}


class ProjectKnowledgeValidator:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root).resolve()
        self.target = (
            self.repo_root
            / "reflective-prompt-library"
            / "PROJECT_KNOWLEDGE.md"
        )
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def validate(self) -> Dict:
        if not self.target.exists():
            self.errors.append(f"PROJECT_KNOWLEDGE.md not found at {self.target}")
            return self._result()

        content = self.target.read_text(encoding="utf-8")
        lines = content.splitlines()

        self._check_required_sections(content)
        self._check_authority_boundary(content)
        self._check_no_agent_directives(lines)
        self._check_lessons_have_evidence(content)
        self._check_milestone_status(content)
        self._check_stale_done_milestones(content)
        self._check_decision_index(content)

        return self._result()

    def _check_required_sections(self, content: str) -> None:
        headers = set(re.findall(r"^##\s+(.+?)\s*$", content, re.MULTILINE))
        for section in REQUIRED_SECTIONS:
            if section not in headers:
                self.errors.append(f"Missing required section: ## {section}")

    def _check_authority_boundary(self, content: str) -> None:
        first_section = re.search(r"^##\s+", content, re.MULTILINE)
        preamble = content[: first_section.start()] if first_section else content

        if "NON-AUTHORITATIVE" not in preamble.upper():
            self.errors.append(
                "Authority boundary missing: preamble must declare this file "
                "NON-AUTHORITATIVE"
            )
        if "AGENTS.md" not in preamble or "SKILL.md" not in preamble:
            self.errors.append(
                "Authority boundary incomplete: preamble must point agent operating "
                "rules to both AGENTS.md and SKILL.md"
            )

    def _check_no_agent_directives(self, lines: List[str]) -> None:
        for i, raw in enumerate(lines, start=1):
            for pat in AGENT_DIRECTIVE_PATTERNS:
                m = re.search(pat, raw, re.IGNORECASE)
                if m:
                    self.errors.append(
                        f"Line {i}: explicit agent-directed rule '{m.group(0)}' "
                        f"belongs in AGENTS.md or SKILL.md -> {raw.strip()!r}"
                    )
                    break

    def _check_lessons_have_evidence(self, content: str) -> None:
        blocks = self._split_blocks(content, label="Lesson")
        for name, body in blocks:
            evidence = re.search(r"^-\s*Evidence:\s*(.+?)\s*$", body, re.MULTILINE)
            if not evidence or not evidence.group(1).strip():
                self.errors.append(
                    f"Durable Lesson '{name}' has no non-empty 'Evidence:' pointer"
                )

    def _check_milestone_status(self, content: str) -> None:
        blocks = self._split_blocks(content, label="Milestone")
        for name, body in blocks:
            status = re.search(r"^-\s*Status:\s*(.+?)\s*$", body, re.MULTILINE)
            if not status:
                self.errors.append(f"Milestone '{name}' has no 'Status:' line")
            elif status.group(1).strip().lower() not in VALID_STATUSES:
                self.errors.append(
                    f"Milestone '{name}' has invalid Status "
                    f"'{status.group(1).strip()}' (expected one of {sorted(VALID_STATUSES)})"
                )

    def _check_stale_done_milestones(self, content: str) -> None:
        """A 'done' milestone still living under Current Direction is stale; it
        should be reflowed into the Decision Index (Knowie's redeem-and-retire).
        Reported as a warning, not an error: reflow is a judgement, so we
        propose rather than block — mirroring knowie-judge's boundary."""
        current = self._section_body(content, "Current Direction")
        if current is None:
            return
        for name, body in self._split_blocks(current, label="Milestone"):
            status = re.search(r"^-\s*Status:\s*(.+?)\s*$", body, re.MULTILINE)
            if status and status.group(1).strip().lower() == "done":
                self.warnings.append(
                    f"Milestone '{name}' is done but still under Current Direction; "
                    f"reflow it into the Decision Index and retire it"
                )

    def _check_decision_index(self, content: str) -> None:
        section = self._section_body(content, "Decision Index")
        if section is None:
            return  # already reported as missing section
        entries = [
            ln for ln in section.splitlines()
            if ln.lstrip().startswith("-") and not ln.lstrip().startswith(">")
        ]
        if not entries:
            self.errors.append("Decision Index is empty; it must point to at least one record")
            return
        for entry in entries:
            if not re.search(r"\]\([^)]+\)", entry):
                self.errors.append(
                    f"Decision Index entry lacks a link pointer -> {entry.strip()!r}"
                )

    # --- helpers -----------------------------------------------------------

    def _split_blocks(self, content: str, label: str):
        """Yield (name, body) for each '### <label>: <name>' block."""
        pattern = re.compile(
            rf"^###\s+{re.escape(label)}:\s*(.+?)\s*$", re.MULTILINE
        )
        out = []
        matches = list(pattern.finditer(content))
        for idx, m in enumerate(matches):
            start = m.end()
            end = matches[idx + 1].start() if idx + 1 < len(matches) else len(content)
            # stop at next ## section if it comes first
            next_section = re.search(r"^##\s+", content[start:end], re.MULTILINE)
            if next_section:
                end = start + next_section.start()
            out.append((m.group(1).strip(), content[start:end]))
        return out

    def _section_body(self, content: str, header: str):
        m = re.search(rf"^##\s+{re.escape(header)}\s*$", content, re.MULTILINE)
        if not m:
            return None
        start = m.end()
        nxt = re.search(r"^##\s+", content[start:], re.MULTILINE)
        end = start + nxt.start() if nxt else len(content)
        return content[start:end]

    def _result(self) -> Dict:
        return {
            "errors": self.errors,
            "warnings": self.warnings,
            "valid": len(self.errors) == 0,
        }


def main() -> int:
    repo_root = Path(__file__).parent.parent.parent
    print(f"Validating PROJECT_KNOWLEDGE.md contract in: {repo_root}")
    print("=" * 60)

    validator = ProjectKnowledgeValidator(str(repo_root))
    result = validator.validate()

    if result["warnings"]:
        print(f"\n⚠️  {len(result['warnings'])} reflow suggestion(s):")
        for warn in result["warnings"]:
            print(f"  - {warn}")

    if result["valid"]:
        print("\n✅ PROJECT_KNOWLEDGE.md satisfies the project-judgment contract.")
        return 0

    print(f"\n❌ {len(result['errors'])} contract violation(s):")
    for err in result["errors"]:
        print(f"  - {err}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
