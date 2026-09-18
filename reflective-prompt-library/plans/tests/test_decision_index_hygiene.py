"""The Decision Index reads newest-first from the top: on 2026-09-18 two new
survey bullets were appended BELOW the 2026-09-16 run and a same-day review
reported the ordering as clean — the defect class is "new entry not placed at
the head". Guard that class: the maximum bullet date must be the first
bullet's date. The legacy June tail is not monotone and is deliberately out
of scope (re-sorting committed history is churn; the head is what a reader
scans).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


def test_newest_decision_index_entry_is_first():
    text = (PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md").read_text(encoding="utf-8")
    section = text.split("## Decision Index", 1)[1]
    section = re.split(r"\n## ", section, maxsplit=1)[0]
    dates = re.findall(r"^- (\d{4}-\d{2}-\d{2})", section, re.M)
    assert dates, "Decision Index has no dated bullets"
    assert dates[0] == max(dates), (
        f"newest Decision Index entry ({max(dates)}) is not at the head "
        f"(head is {dates[0]}); insert new entries above the current top"
    )
