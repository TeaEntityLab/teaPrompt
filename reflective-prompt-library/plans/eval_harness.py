#!/usr/bin/env python3
"""
Prompt Eval Harness for TeaPrompt

Checks prompt file quality against a rubric of structural and content criteria.
Scans markdown prompt files and evaluates completeness and quality via static analysis.

Supports:
- Single file evaluation
- Batch evaluation (all prompts from index.json)
- Custom rubric files
- JSON report output
- Verbose per-check output
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

DEFAULT_RUBRIC: Dict = {
    "version": "1.0",
    "checks": [
        {
            "id": "has-acceptance-criteria",
            "name": "Has Acceptance Criteria",
            "description": "Prompt should include acceptance criteria section",
            "severity": "error",
            "patterns": [
                r"## Acceptance",
                r"## Acceptance Criteria",
                r"## Verification",
                r"## 驗收",
            ],
            "match": "heading",
        },
        {
            "id": "has-falsifiability",
            "name": "Has Falsifiability Section",
            "description": "Prompt should include falsifiability or stop conditions",
            "severity": "warning",
            "patterns": [
                r"## Falsifiability",
                r"## Falsifiability",
                r"## Stop Conditions",
                r"## Failure",
                r"## Failure Conditions",
                r"## Failure Modes",
            ],
            "match": "heading",
        },
        {
            "id": "no-weak-language",
            "name": "No Weak Language",
            "description": "Avoid non-observable instructions like 'be careful', 'think deeply'",
            "severity": "warning",
            "patterns": [
                r"be careful",
                r"think deeply",
                r"act like an expert",
                r"use your best judgment",
                r"do your best",
                r"try your hardest",
            ],
            "match": "content_inverted",
        },
        {
            "id": "has-scope",
            "name": "Has Scope Section",
            "description": "Prompt should define scope boundaries",
            "severity": "warning",
            "patterns": [
                r"## Scope",
                r"## Scope In",
                r"## In Scope",
                r"## Scope Out",
                r"## 範圍",
            ],
            "match": "heading",
        },
        {
            "id": "has-goal",
            "name": "Has Goal Section",
            "description": "Prompt should state its goal",
            "severity": "error",
            "patterns": [
                r"## Goal",
                r"## Purpose",
                r"# .*Prompt",
                r"## 目標",
                r"## 任務",
            ],
            "match": "heading",
        },
        {
            "id": "defined-placeholders",
            "name": "Defined Placeholders",
            "description": "Template placeholders should be clearly marked",
            "severity": "warning",
            "patterns": [
                r"\{[^}]+\}",
                r"<[^>]+>",
            ],
            "match": "placeholder_check",
        },
        {
            "id": "has-human-review",
            "name": "Has Human Review Trigger",
            "description": "High-risk prompts should have human review gate",
            "severity": "error",
            "patterns": [
                r"Human Review",
                r"human review",
                r"Human Review Gate",
                r"Human Review Required",
                r"人工審查",
                r"人工確認",
            ],
            "match": "content",
            "condition": "risk_level == 'high'",
        },
    ],
}

class EvalHarness:
    SCORE_MAP = {"pass": 100.0, "warn": 50.0, "fail": 0.0}

    def __init__(
        self,
        repo_root: str,
        rubric: Optional[Dict] = None,
        verbose: bool = False,
    ):
        self.repo_root = Path(repo_root).resolve()
        self.rubric = rubric or DEFAULT_RUBRIC
        self.verbose = verbose
        self.checks = self.rubric.get("checks", [])

    def evaluate_file(self, file_path: str) -> Dict:
        fpath = self._resolve_path(file_path)
        content = fpath.read_text(encoding="utf-8")
        rel_path = str(fpath.relative_to(self.repo_root))

        results = self._run_checks(content, rel_path)
        score = self._calculate_score(results)

        return {
            "file": rel_path,
            "checks": results,
            "score": score,
            "summary": self._summarize(results),
        }

    def evaluate_batch(self) -> Dict:
        index_path = self.repo_root / "reflective-prompt-library" / "index.json"
        if not index_path.exists():
            print(
                f"Warning: index.json not found at {index_path}, "
                f"falling back to glob search"
            )
            return self._evaluate_batch_glob()

        index = json.loads(index_path.read_text(encoding="utf-8"))
        prompts = index.get("prompts", [])

        file_results = []
        for entry in prompts:
            if entry.get("type") != "prompt":
                continue
            subcat = entry.get("subcategory", "")
            if subcat in ("skills", "plans"):
                continue

            fpath = self.repo_root / entry["path"]
            if not fpath.exists():
                continue

            result = self.evaluate_file(str(fpath))
            file_results.append(result)

        return self._build_batch_summary(file_results)

    def _run_checks(self, content: str, file_path: str) -> List[Dict]:
        results = []
        risk_level = self._detect_risk_level(content, file_path)

        for check in self.checks:
            result = self._execute_check(check, content, risk_level)
            results.append(result)
            if self.verbose:
                self._print_check_result(result, file_path)

        return results

    def _execute_check(
        self, check: Dict, content: str, risk_level: str
    ) -> Dict:
        check_id = check["id"]
        check_name = check["name"]
        severity = check.get("severity", "warning")
        patterns = check.get("patterns", [])
        match_type = check.get("match", "heading")
        condition = check.get("condition")

        base = {
            "id": check_id,
            "name": check_name,
            "severity": severity,
            "match_type": match_type,
        }

        # Evaluate condition gate
        if condition:
            if not self._evaluate_condition(condition, risk_level):
                base["result"] = "skip"
                base["message"] = (
                    f"Condition '{condition}' not met "
                    f"(detected risk_level='{risk_level}')"
                )
                return base

        # Dispatch to match handler
        if match_type == "heading":
            return self._check_heading(base, content, patterns)
        elif match_type == "content":
            return self._check_content(base, content, patterns)
        elif match_type == "content_inverted":
            return self._check_content_inverted(base, content, patterns)
        elif match_type == "placeholder_check":
            return self._check_placeholders(base, content, patterns)
        else:
            base["result"] = "skip"
            base["message"] = f"Unknown match type: {match_type}"
            return base

    def _check_heading(
        self, base: Dict, content: str, patterns: List[str]
    ) -> Dict:
        heading_pattern = re.compile(r"^#{1,6}\s+", re.MULTILINE)
        headings: List[str] = []
        for line in content.split("\n"):
            if heading_pattern.match(line):
                headings.append(line.strip())

        for pattern in patterns:
            regex = re.compile(pattern, re.IGNORECASE)
            for heading in headings:
                if regex.search(heading):
                    base["result"] = "pass"
                    base["message"] = (
                        f"Found heading matching '{pattern}'"
                    )
                    return base

        severity = base["severity"]
        base["result"] = "fail" if severity == "error" else "warn"
        base["message"] = "No matching heading found"
        return base

    def _check_content(
        self, base: Dict, content: str, patterns: List[str]
    ) -> Dict:
        for pattern in patterns:
            regex = re.compile(pattern, re.MULTILINE | re.DOTALL)
            if regex.search(content):
                base["result"] = "pass"
                base["message"] = f"Found content matching '{pattern}'"
                return base

        severity = base["severity"]
        base["result"] = "fail" if severity == "error" else "warn"
        base["message"] = "No matching content found"
        return base

    def _check_content_inverted(
        self, base: Dict, content: str, patterns: List[str]
    ) -> Dict:
        matches: List[str] = []
        for pattern in patterns:
            regex = re.compile(pattern, re.IGNORECASE | re.MULTILINE)
            found = regex.findall(content)
            matches.extend(found)

        if matches:
            display = matches[:5]
            msg = f"Found {len(matches)} weak phrase(s)"
            if self.verbose:
                msg += f" — {', '.join(repr(m) for m in display)}"
            base["result"] = "warn"
            base["message"] = msg
            base["details"] = {"count": len(matches), "matches": display}
        else:
            base["result"] = "pass"
            base["message"] = "No weak language found"

        return base

    def _check_placeholders(
        self, base: Dict, content: str, patterns: List[str]
    ) -> Dict:
        placeholders: List[str] = []
        for pattern in patterns:
            regex = re.compile(pattern)
            found = regex.findall(content)
            placeholders.extend(found)

        if placeholders:
            unique = list(dict.fromkeys(placeholders))
            display = unique[:10]
            msg = (
                f"Found {len(unique)} unique placeholder(s)"
            )
            if self.verbose:
                msg += f" — {', '.join(repr(p) for p in display)}"
            base["result"] = "warn"
            base["message"] = msg
            base["details"] = {"count": len(unique), "placeholders": display}
        else:
            base["result"] = "skip"
            base["message"] = "No template placeholders found"

        return base

    def _detect_risk_level(self, content: str, file_path: str) -> str:
        high_risk_keywords = [
            r"high.?risk",
            r"高風險",
            r"production",
            r"deploy",
            r"migration",
            r"billing",
            r"payment",
            r"credit.?card",
            r"password",
            r"api.?key",
            r"secret",
            r"token",
            r"auth",
            r"permission",
            r"admin",
            r"root",
            r"sudo",
            r"destructive",
            r"irreversible",
            r"Human Review",
            r"人工審查",
        ]

        path_lower = file_path.lower()
        if "high-risk" in path_lower or "security" in path_lower:
            return "high"

        for kw in high_risk_keywords:
            if re.search(kw, content, re.IGNORECASE):
                return "high"

        return "low"

    def _evaluate_condition(self, condition: str, risk_level: str) -> bool:
        try:
            match = re.match(
                r"risk_level\s*==\s*['\"]([^'\"]+)['\"]", condition
            )
            if match:
                return risk_level == match.group(1)
            return False
        except Exception:
            return False

    def _calculate_score(self, results: List[Dict]) -> float:
        relevant = [
            r for r in results if r.get("result") not in ("skip", None)
        ]
        if not relevant:
            return 100.0

        total = 0.0
        for r in relevant:
            result = r.get("result", "skip")
            total += self.SCORE_MAP.get(result, 0.0)

        return round(total / len(relevant), 1)

    def _summarize(self, results: List[Dict]) -> Dict:
        counts = {"pass": 0, "warn": 0, "fail": 0, "skip": 0}
        for r in results:
            result = r.get("result", "skip")
            counts[result] = counts.get(result, 0) + 1
        return counts

    def _build_batch_summary(self, file_results: List[Dict]) -> Dict:
        scores = [r["score"] for r in file_results]
        avg_score = round(sum(scores) / len(scores), 1) if scores else 0.0

        min_file = None
        max_file = None
        if file_results:
            min_file = min(file_results, key=lambda r: r["score"])
            max_file = max(file_results, key=lambda r: r["score"])

        total_pass = sum(r["summary"]["pass"] for r in file_results)
        total_warn = sum(r["summary"]["warn"] for r in file_results)
        total_fail = sum(r["summary"]["fail"] for r in file_results)
        total_skip = sum(r["summary"]["skip"] for r in file_results)

        return {
            "total_files": len(file_results),
            "average_score": avg_score,
            "lowest": {
                "file": min_file["file"] if min_file else None,
                "score": min_file["score"] if min_file else None,
            },
            "highest": {
                "file": max_file["file"] if max_file else None,
                "score": max_file["score"] if max_file else None,
            },
            "aggregate": {
                "pass": total_pass,
                "warn": total_warn,
                "fail": total_fail,
                "skip": total_skip,
            },
            "file_results": file_results,
        }

    def _evaluate_batch_glob(self) -> Dict:
        prompt_root = self.repo_root / "reflective-prompt-library"
        md_files = [
            p
            for p in prompt_root.rglob("*.md")
            if "skills/" not in str(p)
            and "plans/" not in str(p)
            and "SKILL.md" not in p.name
            and p.name not in ("README.md", "METHODOLOGY_MAP.md",
                               "LANGUAGE_POLICY.md",
                               "SKILL_INSTALLATION.md",
                               "SKILL_TRIGGER_CHEATSHEET.md",
                               "SKILL_TRIGGER_CHEATSHEET.zh-TW.md")
        ]

        file_results = []
        for fpath in sorted(md_files):
            result = self.evaluate_file(str(fpath))
            file_results.append(result)

        return self._build_batch_summary(file_results)

    def _resolve_path(self, file_path: str) -> Path:
        fpath = Path(file_path)
        if not fpath.is_absolute():
            candidate = self.repo_root / fpath
            if candidate.exists():
                return candidate
            if fpath.exists():
                return fpath.resolve()
        return fpath.resolve()

    def _print_check_result(self, check: Dict, file_path: str):
        label_map = {
            "pass": "PASS",
            "warn": "WARN",
            "fail": "FAIL",
            "skip": "SKIP",
        }
        label = label_map.get(check.get("result", "?"), "???")
        cid = check.get("id", "?")
        msg = check.get("message", "")

        print(f"  {label:5s} {cid}: {msg}")

    def print_report(self, result: Dict):
        file_path = result.get("file", "unknown")
        checks = result.get("checks", [])
        score = result.get("score", 0.0)
        summary = result.get("summary", {})

        print("\nEval Harness Report")
        print("=" * 60)
        print(f"File: {file_path}")

        for check in checks:
            self._print_check_line(check)

        print(f"\nResults: {summary.get('pass', 0)} pass, "
              f"{summary.get('warn', 0)} warn, "
              f"{summary.get('fail', 0)} fail"
              f"{', ' + str(summary.get('skip', 0)) + ' skip' if summary.get('skip') else ''}")
        print(f"Score: {score}%")

    def print_batch_report(self, batch_result: Dict):
        total = batch_result.get("total_files", 0)
        avg = batch_result.get("average_score", 0.0)
        lo = batch_result.get("lowest", {})
        hi = batch_result.get("highest", {})
        agg = batch_result.get("aggregate", {})

        print("\nEval Harness — Batch Report")
        print("=" * 60)
        print(f"Prompts evaluated: {total}")
        print(f"Average Score: {avg}%")

        if lo.get("file"):
            print(f"Lowest:  {lo['file']} ({lo['score']}%)")
        if hi.get("file"):
            print(f"Highest: {hi['file']} ({hi['score']}%)")

        print(f"\nAggregate: {agg.get('pass', 0)} pass, "
              f"{agg.get('warn', 0)} warn, "
              f"{agg.get('fail', 0)} fail"
              f"{', ' + str(agg.get('skip', 0)) + ' skip' if agg.get('skip') else ''}")

        if self.verbose:
            print(f"\n{'File':<55} {'Score':>6}  {'P':>3} {'W':>3} {'F':>3}")
            print("-" * 72)
            for fr in batch_result.get("file_results", []):
                s = fr.get("summary", {})
                print(
                    f"{fr['file']:<55} {fr['score']:>5.1f}% "
                    f"{s.get('pass', 0):>3} "
                    f"{s.get('warn', 0):>3} "
                    f"{s.get('fail', 0):>3}"
                )

    @staticmethod
    def _print_check_line(check: Dict):
        label_map = {
            "pass": "PASS",
            "warn": "WARN",
            "fail": "FAIL",
            "skip": "SKIP",
        }
        label = label_map.get(check.get("result", "?"), "???")
        cid = check.get("id", "?")
        msg = check.get("message", "")

        print(f"{label:5s} {cid}: {msg}")


def main():
    parser = argparse.ArgumentParser(
        description="Eval Harness — prompt quality evaluation tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s reflective-prompt-library/00-core/core-full.md
  %(prog)s --all
  %(prog)s --all --verbose
  %(prog)s --all --output report.json
  %(prog)s my-prompt.md --rubric custom_rubric.json
        """,
    )

    parser.add_argument(
        "file",
        nargs="?",
        help="Path to a prompt markdown file to evaluate",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Evaluate all prompt files from index.json",
    )
    parser.add_argument(
        "--rubric",
        type=str,
        default=None,
        help="Path to a custom rubric JSON file (default: built-in)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Path to save JSON report",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed per-check output",
    )

    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent.parent

    rubric = DEFAULT_RUBRIC
    if args.rubric:
        rubric_path = Path(args.rubric)
        if not rubric_path.exists():
            print(f"Error: rubric file not found: {args.rubric}", file=sys.stderr)
            sys.exit(1)
        rubric = json.loads(rubric_path.read_text(encoding="utf-8"))

    harness = EvalHarness(
        repo_root=str(repo_root),
        rubric=rubric,
        verbose=args.verbose,
    )

    if args.all:
        result = harness.evaluate_batch()
        harness.print_batch_report(result)

        if args.output:
            output_path = Path(args.output)
            output_path.write_text(
                json.dumps(result, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            print(f"\nReport saved to: {args.output}")
    elif args.file:
        result = harness.evaluate_file(args.file)
        harness.print_report(result)

        if args.output:
            output_path = Path(args.output)
            output_path.write_text(
                json.dumps(result, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            print(f"\nReport saved to: {args.output}")
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
