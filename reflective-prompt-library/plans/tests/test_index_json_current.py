"""The committed discovery surface must describe the tree it ships with.

`index.json` is a committed generated artifact that `make validate` does not
regenerate; twice on 2026-09-13/14 it went stale in a single session because a
record landed after the last regeneration. This guard compares the committed
index against an in-memory run of the generator: same file set, same
line counts, or the index is stale. It never writes.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from generate_index import IndexGenerator  # noqa: E402
from prompt_eval_helpers import PROMPT_LIBRARY_REPO_ROOT, PROMPT_LIBRARY_ROOT  # noqa: E402

INDEX = PROMPT_LIBRARY_ROOT / "index.json"


def _entries(index: dict) -> dict[str, dict]:
    """Whole entries keyed by path; every field is content-derived (the only
    timestamp, `generated_at`, is top-level and ignored)."""
    return {entry["path"]: entry for entry in index.get("prompts", []) + index.get("skills", [])}


def test_committed_index_matches_generator_over_current_tree():
    assert INDEX.is_file(), "index.json missing; run plans/generate_index.py"
    committed_index = json.loads(INDEX.read_text(encoding="utf-8"))
    live_index = IndexGenerator(PROMPT_LIBRARY_REPO_ROOT).generate()
    committed = _entries(committed_index)
    live = _entries(live_index)

    missing = sorted(set(live) - set(committed))
    extra = sorted(set(committed) - set(live))
    assert not missing and not extra, (
        f"index.json is stale — run `python3 reflective-prompt-library/plans/generate_index.py`; "
        f"not indexed: {missing}; no longer on disk: {extra}"
    )
    changed = sorted(p for p in live if live[p] != committed[p])
    assert not changed, (
        "index.json is stale — entries differ (frontmatter, headings, links, or size) for: "
        f"{changed[:8]}{' …' if len(changed) > 8 else ''}; run generate_index.py"
    )
    assert committed_index["categories"] == live_index["categories"], "index.json category file lists are stale"
    assert committed_index["total_files"] == live_index["total_files"]
