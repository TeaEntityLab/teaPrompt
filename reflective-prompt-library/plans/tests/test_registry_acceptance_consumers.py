"""Execute the locked registry checks as a fresh verification consumer would.

A healthy admission registry must not leave the independent acceptance surface
expecting an obsolete count. These checks do not modify the protected oracle.
"""
from __future__ import annotations

import json
import re
import shlex
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]


@pytest.mark.parametrize("check_id", ["core-skill-cardinality", "domain-pack-cardinality"])
def test_locked_registry_check_matches_its_runnable_observation(check_id: str):
    spec = (ROOT / "acceptance.yaml").read_text(encoding="utf-8")
    match = re.search(
        rf"(?m)^  - id: {re.escape(check_id)}\n((?:    [^\n]*\n)+)",
        spec,
    )
    assert match is not None, f"Missing acceptance check: {check_id}"
    fields = dict(line.strip().split(":", 1) for line in match.group(1).splitlines())
    result = subprocess.run(
        shlex.split(fields["verify"].strip()), cwd=ROOT,
        capture_output=True, text=True, timeout=15,
    )
    assert result.returncode == 0, result.stderr
    expected = json.loads(fields["expect"].strip())
    assert result.stdout.strip() == expected, (
        f"{check_id}: locked expectation {expected!r} differs from "
        f"runnable observation {result.stdout.strip()!r}"
    )
