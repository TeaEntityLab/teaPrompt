#!/usr/bin/env python3
"""Record-hygiene validator for TeaPrompt plans records (D4).

Adopted 2026-07-12 as a user-directed exception (recurrence `unknown`) after the
rethink record deferred it convention-only. Enforces the conventions every
2026-07 panel/decision record already follows, so no historical record breaks:

- status banner blockquote near the top,
- an evidence-separation heading OR an explicit [INFERENCE] label,
- fact-check dating on external (http/https) claim lines, outside code fences,
- a Candidate Adoption Ledger heading when the record proposes candidates,
- a Falsifiability heading.

Scope guard (no retroactive failure): only records whose filename date component
is on/after ADOPTION_DATE are enforced. Older records are reported as skipped;
the convention was not machine-enforced when they shipped.
"""

import re
import sys
from datetime import date
from pathlib import Path

ADOPTION_DATE = date(2026, 7, 12)

DATED_RECORD = re.compile(r"(20\d\d)-(\d\d)-(\d\d)\.md$")
STATUS_BANNER = re.compile(r"^>\s+\*\*Status", re.MULTILINE)
EVIDENCE_HEADING = re.compile(
    r"^#{2,4}\s+(?:Evidence|Evidence vs Inference|Evidence Actually Checked)\b",
    re.MULTILINE,
)
FALSIFIABILITY_HEADING = re.compile(r"^#{2,4}\s+Falsif", re.MULTILINE)
LEDGER_HEADING = re.compile(r"^#{2,4}\s+.*Candidate Adoption Ledger", re.MULTILINE)
INFERENCE_TAG = re.compile(r"\[INFERENCE\]")
CANDIDATE_SIGNAL = re.compile(r"Candidate Adoption Ledger|\|\s*Candidate\s*\|")
FENCE = re.compile(r"^```")
DATE_NEAR = re.compile(r"(?:checked|accessed|as of|retrieved)\s+20\d\d-\d\d-\d\d", re.IGNORECASE)


def record_date(path: Path):
    m = DATED_RECORD.search(path.name)
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def _external_claim_lines_missing_date(text: str) -> list[int]:
    """Lines with a bare URL outside code fences and without a nearby access date.

    Heuristic → warning, never a hard error (avoids false positives on link
    references and citations that carry their date on an adjacent line)."""
    missing = []
    in_fence = False
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if FENCE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence or "http://" not in line and "https://" not in line:
            continue
        window = " ".join(lines[max(0, i - 1): i + 2])
        if not DATE_NEAR.search(window):
            missing.append(i + 1)
    return missing


def check_record(path: Path) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []
    head = "\n".join(text.splitlines()[:12])

    if not STATUS_BANNER.search(head):
        errors.append("missing status banner blockquote (`> **Status...`) in first 12 lines")
    if not (EVIDENCE_HEADING.search(text) or INFERENCE_TAG.search(text)):
        errors.append("no evidence-separation heading and no [INFERENCE] label")
    if not FALSIFIABILITY_HEADING.search(text):
        errors.append("missing a Falsifiability/Falsifiers heading")
    if CANDIDATE_SIGNAL.search(text) and not LEDGER_HEADING.search(text):
        errors.append("proposes candidates but has no 'Candidate Adoption Ledger' heading")

    for ln in _external_claim_lines_missing_date(text):
        warnings.append(f"line {ln}: external (http) claim without a nearby access date")
    return errors, warnings


def main() -> int:
    repo_root = Path(__file__).parent.parent.parent
    plans = repo_root / "reflective-prompt-library" / "plans"
    print(f"Validating record hygiene in: {plans}")
    print("=" * 60)

    enforced = 0
    skipped = 0
    total_errors = 0
    total_warnings = 0
    failing: list[str] = []

    for path in sorted(plans.glob("*.md")):
        d = record_date(path)
        if d is None:
            continue
        if d < ADOPTION_DATE:
            skipped += 1
            continue
        enforced += 1
        errors, warnings = check_record(path)
        total_warnings += len(warnings)
        if errors:
            total_errors += len(errors)
            failing.append(path.name)
            print(f"\n❌ {path.name}")
            for e in errors:
                print(f"   - {e}")
        for w in warnings:
            print(f"   ⚠️  {path.name}: {w}")

    print("\n" + "=" * 60)
    print(f"Enforced records (>= {ADOPTION_DATE.isoformat()}): {enforced}")
    print(f"Skipped historical records: {skipped}")
    print(f"Errors: {total_errors} | Warnings: {total_warnings}")

    if total_errors:
        print(f"\n❌ Record-hygiene validation failed: {', '.join(failing)}")
        return 1
    print("\n✅ Record hygiene valid!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
