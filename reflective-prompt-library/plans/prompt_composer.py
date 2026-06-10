#!/usr/bin/env python3
"""
Prompt Composer for TeaPrompt

Composes prompt files from the reflective-prompt-library by slug.
Reads index.json to map slugs to file paths, then concatenates
the corresponding markdown files in category order.

Usage:
  python plans/prompt_composer.py core-full spec-writer
  python plans/prompt_composer.py --template engineering-task
  python plans/prompt_composer.py core-full --task "Build a CLI tool" --output composed.md
  python plans/prompt_composer.py --list-slugs
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional


CATEGORY_ORDER = [
    "00-core",
    "01-thinking",
    "02-engineering",
    "03-context",
    "04-agent",
    "05-domain",
    "06-repo",
]

TEMPLATES: Dict[str, List[str]] = {
    "engineering-task": [
        "core-full",
        "task-start",
        "spec-writer",
        "usage-first",
        "task-slicer",
        "implementation-agent",
        "test-designer",
        "code-reviewer",
    ],
    "long-research": [
        "core-full",
        "research",
        "large-context",
        "context-handoff",
    ],
}


class PromptComposer:
    """Composes prompt files from the reflective-prompt-library by slug."""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root.resolve()
        self.index_path = self.repo_root / "reflective-prompt-library" / "index.json"
        self.prompts_dir = self.repo_root / "reflective-prompt-library"
        self._index: Optional[Dict] = None
        self._slug_to_path: Optional[Dict[str, str]] = None

    @property
    def index(self) -> Dict:
        if self._index is None:
            if not self.index_path.exists():
                raise FileNotFoundError(
                    f"Index file not found: {self.index_path}\n"
                    f"Run generate_index.py first."
                )
            with open(self.index_path, "r", encoding="utf-8") as f:
                self._index = json.load(f)
        return self._index

    @property
    def slug_map(self) -> Dict[str, str]:
        if self._slug_to_path is None:
            self._slug_to_path = self._build_slug_map()
        return self._slug_to_path

    def _build_slug_map(self) -> Dict[str, str]:
        """Build a mapping from slugs to file paths.

        Supports two forms:
        - Simple slug: "core-full" → first match found
        - Category-prefixed slug: "00-core/core-full" → exact match
        """
        mapping: Dict[str, str] = {}
        categories = self.index.get("categories", {})
        prompt_lib = categories.get("prompt-library", {})
        subcategories = prompt_lib.get("subcategories", {})

        for subcat, data in subcategories.items():
            subcat_path = data.get("path", "")
            for filename in data.get("files", []):
                slug = Path(filename).stem
                rel_path = f"{subcat_path}/{filename}"
                if slug not in mapping:
                    mapping[slug] = rel_path
                mapping[f"{subcat}/{slug}"] = rel_path

        return mapping

    def resolve_slug(self, slug: str) -> str:
        """Resolve a slug to a file path. Raises ValueError for unknown slugs."""
        if slug in self.slug_map:
            return self.slug_map[slug]

        available = sorted(self.slug_map.keys())
        simple_slugs = sorted(k for k in available if "/" not in k)
        raise ValueError(
            f"Unknown slug: '{slug}'\n"
            f"Available slugs ({len(simple_slugs)}):\n"
            + self._format_slug_list(simple_slugs)
        )

    def resolve_slugs(self, slugs: List[str]) -> List[str]:
        paths = []
        for slug in slugs:
            paths.append(self.resolve_slug(slug))
        return paths

    def _format_slug_list(self, slugs: List[str], columns: int = 4) -> str:
        if not slugs:
            return "  (none)"
        max_width = max(len(s) for s in slugs) + 2
        lines = []
        for i in range(0, len(slugs), columns):
            row = slugs[i : i + columns]
            lines.append("  " + "".join(s.ljust(max_width) for s in row))
        return "\n".join(lines)

    def list_slugs(self) -> str:
        """Return a formatted listing of all available slugs grouped by category."""
        categories = self.index.get("categories", {})
        prompt_lib = categories.get("prompt-library", {})
        subcategories = prompt_lib.get("subcategories", {})

        lines = ["Available slugs by category:\n"]

        for cat in CATEGORY_ORDER:
            if cat in subcategories:
                data = subcategories[cat]
                files = data.get("files", [])
                if files:
                    slugs = sorted(Path(f).stem for f in files)
                    lines.append(f"[{cat}]")
                    for slug in slugs:
                        lines.append(f"  {cat}/{slug}")
                    lines.append("")

        uncategorized = [c for c in subcategories if c not in CATEGORY_ORDER]
        if uncategorized:
            lines.append("[other]")
            for cat in sorted(uncategorized):
                data = subcategories[cat]
                files = data.get("files", [])
                slugs = sorted(Path(f).stem for f in files)
                for slug in slugs:
                    lines.append(f"  {cat}/{slug}")
            lines.append("")

        lines.append("Templates:")
        for name, members in TEMPLATES.items():
            lines.append(f"  {name}: {', '.join(members)}")

        return "\n".join(lines)

    def read_prompt(self, rel_path: str) -> str:
        full_path = self.repo_root / rel_path
        if not full_path.exists():
            raise FileNotFoundError(f"Prompt file not found: {full_path}")
        return full_path.read_text(encoding="utf-8")

    def _strip_examples(self, content: str) -> str:
        """Strip fenced code blocks and placeholder lines for low-token mode."""
        content = re.sub(r"```[\s\S]*?```", "", content)
        content = re.sub(r"^\s*\{[^}]*\}\s*$", "", content, flags=re.MULTILINE)
        content = re.sub(r"\n{3,}", "\n\n", content)
        lines = [line.rstrip() for line in content.split("\n")]
        return "\n".join(lines)

    def _build_header(self, slugs: List[str], low_token: bool) -> str:
        header = (
            f"# Composed Prompt\n\n"
            f"Generated from {len(slugs)} prompt(s): {', '.join(slugs)}"
        )
        if low_token:
            header += " (low-token mode)"
        return header + "\n"

    def _build_prompt_section(
        self, slug: str, path: str, index: int, low_token: bool
    ) -> str:
        try:
            content = self.read_prompt(path)
        except FileNotFoundError as e:
            print(f"Warning: {e}", file=sys.stderr)
            return ""

        if low_token:
            content = self._strip_examples(content)

        return (
            f"\n---\n"
            f"## Prompt {index + 1}: {slug}\n"
            f"<!-- source: {path} -->\n\n"
            f"{content}\n"
        )

    def compose(
        self,
        slugs: List[str],
        task_text: Optional[str] = None,
        low_token: bool = False,
    ) -> str:
        """Compose prompt files from slugs into a single output."""
        paths = self.resolve_slugs(slugs)
        sections = [self._build_header(slugs, low_token)]

        if task_text:
            sections.append(f"\n---\n## Task\n\n{task_text}\n")

        for i, (slug, path) in enumerate(zip(slugs, paths)):
            section = self._build_prompt_section(slug, path, i, low_token)
            if section:
                sections.append(section)

        return "".join(sections)

    def expand_template(self, template_name: str) -> List[str]:
        """Expand a named template into its slug list."""
        if template_name not in TEMPLATES:
            available = ", ".join(TEMPLATES.keys())
            raise ValueError(
                f"Unknown template: '{template_name}'\n"
                f"Available templates: {available}"
            )
        return list(TEMPLATES[template_name])


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compose prompt files from the reflective-prompt-library by slug.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  %(prog)s core-full spec-writer\n"
            "  %(prog)s --template engineering-task\n"
            "  %(prog)s core-full --task 'Build a CLI tool' --output composed.md\n"
            "  %(prog)s --list-slugs\n"
        ),
    )

    parser.add_argument(
        "slugs",
        nargs="*",
        help="Prompt slugs to compose (e.g., core-full, spec-writer, 00-core/core-full)",
    )
    parser.add_argument(
        "--template",
        choices=list(TEMPLATES.keys()),
        help="Use a built-in template instead of listing slugs individually",
    )
    parser.add_argument(
        "--task",
        help="Task description text to include in the composed output",
    )
    parser.add_argument(
        "--low-token",
        action="store_true",
        help="Strip extended examples; keep only prompt template and core rules",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output file path (default: stdout)",
    )
    parser.add_argument(
        "--list-slugs",
        action="store_true",
        help="List all available slugs grouped by category and exit",
    )

    return parser.parse_args()


def main():
    args = _parse_args()
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent
    composer = PromptComposer(repo_root)

    if args.list_slugs:
        print(composer.list_slugs())
        return 0

    if args.template:
        try:
            slugs = composer.expand_template(args.template)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    elif args.slugs:
        slugs = args.slugs
    else:
        print("Error: no slugs or template specified", file=sys.stderr)
        return 1

    try:
        output = composer.compose(
            slugs=slugs,
            task_text=args.task,
            low_token=args.low_token,
        )
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(output, encoding="utf-8")
        print(f"Composed prompt written to: {out_path}")
    else:
        print(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
