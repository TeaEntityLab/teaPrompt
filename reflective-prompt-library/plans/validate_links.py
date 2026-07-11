#!/usr/bin/env python3
"""
Link + Schema Validation for TeaPrompt

Validates:
- ref_file references (<ref_file file="..." />)
- ref_snippet references (<ref_snippet file="..." lines="..." />)
- Markdown links ([text](url))
- Frontmatter schema for SKILL.md files
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple


class LinkValidator:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root).resolve()
        self.errors = []
        self.warnings = []
        
    def validate_all(self) -> Dict:
        """Run all validations and return results."""
        results = {
            "ref_file_errors": [],
            "ref_snippet_errors": [],
            "markdown_link_errors": [],
            "frontmatter_errors": [],
            "total_files": 0,
            "total_errors": 0
        }
        
        # Find all markdown files
        md_files = list(self.repo_root.rglob("*.md"))
        results["total_files"] = len(md_files)
        
        for md_file in md_files:
            self.validate_file(md_file, results)
            
        results["total_errors"] = (
            len(results["ref_file_errors"]) + 
            len(results["ref_snippet_errors"]) + 
            len(results["markdown_link_errors"]) + 
            len(results["frontmatter_errors"])
        )
        
        return results
    
    def validate_file(self, file_path: Path, results: Dict):
        """Validate a single markdown file."""
        try:
            content = file_path.read_text(encoding='utf-8')
            relative_path = file_path.relative_to(self.repo_root)
            
            # Validate ref_file references
            self.validate_ref_file(content, file_path, relative_path, results)
            
            # Validate ref_snippet references
            self.validate_ref_snippet(content, file_path, relative_path, results)
            
            # Validate markdown links
            self.validate_markdown_links(content, file_path, relative_path, results)
            
            # Validate frontmatter if it's a SKILL.md
            if file_path.name == "SKILL.md":
                self.validate_skill_frontmatter(content, file_path, relative_path, results)
                
        except Exception as e:
            self.errors.append(f"Error reading {file_path}: {e}")
    
    def validate_ref_file(self, content: str, file_path: Path, relative_path: Path, results: Dict):
        """Validate <ref_file> references."""
        pattern = r'<ref_file file="([^"]+)"\s*/>'
        matches = re.findall(pattern, content)
        
        for ref in matches:
            # Convert to absolute path if relative
            if os.path.isabs(ref):
                target_path = Path(ref)
            else:
                # Resolve relative to the repo root
                target_path = self.repo_root / ref
            
            if not target_path.exists():
                results["ref_file_errors"].append({
                    "file": str(relative_path),
                    "reference": ref,
                    "error": "File not found"
                })
    
    def validate_ref_snippet(self, content: str, file_path: Path, relative_path: Path, results: Dict):
        """Validate <ref_snippet> references."""
        pattern = r'<ref_snippet file="([^"]+)" lines="(\d+-\d+)"\s*/>'
        matches = re.findall(pattern, content)
        
        for ref, line_range in matches:
            # Convert to absolute path if relative
            if os.path.isabs(ref):
                target_path = Path(ref)
            else:
                target_path = self.repo_root / ref
            
            if not target_path.exists():
                results["ref_snippet_errors"].append({
                    "file": str(relative_path),
                    "reference": ref,
                    "line_range": line_range,
                    "error": "File not found"
                })
            else:
                # Validate line range
                try:
                    start, end = map(int, line_range.split('-'))
                    total_lines = len(target_path.read_text(encoding='utf-8').splitlines())
                    if start < 1 or end > total_lines or start > end:
                        results["ref_snippet_errors"].append({
                            "file": str(relative_path),
                            "reference": ref,
                            "line_range": line_range,
                            "error": f"Invalid line range (file has {total_lines} lines)"
                        })
                except Exception as e:
                    results["ref_snippet_errors"].append({
                        "file": str(relative_path),
                        "reference": ref,
                        "line_range": line_range,
                        "error": f"Invalid line range format: {e}"
                    })
    
    def validate_markdown_links(self, content: str, file_path: Path, relative_path: Path, results: Dict):
        """Validate markdown links."""
        # Match [text](url) but not [text]: url style
        pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        matches = re.findall(pattern, content)
        
        for text, url in matches:
            # Skip external URLs and anchor links
            if url.startswith(('http://', 'https://', '#', 'mailto:', 'ftp://')):
                continue
                
            # Convert to absolute path if relative
            if os.path.isabs(url):
                target_path = Path(url)
            else:
                # Resolve relative to the current file's directory
                target_path = file_path.parent / url
            
            # Remove fragment if present
            if '#' in str(target_path):
                target_path = Path(str(target_path).split('#')[0])
            
            if not target_path.exists():
                results["markdown_link_errors"].append({
                    "file": str(relative_path),
                    "link_text": text,
                    "target": url,
                    "error": "Target not found"
                })
    
    # Agent Skills spec (agentskills.io/specification, checked 2026-07-11):
    # only these top-level frontmatter fields are defined; extra properties
    # belong under the `metadata:` map. Governance fields (risk_level,
    # human_review_required, external_io, context_load) migrated there
    # 2026-07-11; validate_governance.py reads them via its flattening parser.
    SPEC_TOP_LEVEL_FIELDS = {
        'name', 'description', 'license', 'compatibility', 'metadata', 'allowed-tools',
    }
    SPEC_NAME_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
    SPEC_NAME_MAX = 64
    SPEC_DESCRIPTION_MAX = 1024

    def validate_skill_frontmatter(self, content: str, file_path: Path, relative_path: Path, results: Dict):
        """Validate SKILL.md frontmatter against the Agent Skills spec."""
        def err(message: str):
            results["frontmatter_errors"].append({
                "file": str(relative_path),
                "error": message,
            })

        if not content.startswith('---'):
            err("Missing frontmatter delimiter (---)")
            return

        frontmatter_end = content.find('---', 3)
        if frontmatter_end == -1:
            err("Unclosed frontmatter delimiter")
            return

        # Top-level-aware parse: a top-level key starts at column 0; indented
        # lines belong to the preceding key (e.g. the metadata map).
        top_level: Dict[str, str] = {}
        for line in content[3:frontmatter_end].split('\n'):
            if not line or line.startswith((' ', '\t', '#')):
                continue
            if ':' not in line:
                continue
            key, value = line.split(':', 1)
            top_level[key.strip()] = value.strip()

        for field in ('name', 'description', 'license'):
            if field not in top_level:
                err(f"Missing required field: {field}")

        for field in sorted(set(top_level) - self.SPEC_TOP_LEVEL_FIELDS):
            err(
                f"Spec-unknown top-level field: {field} "
                f"(allowed: {sorted(self.SPEC_TOP_LEVEL_FIELDS)}; "
                "put extra properties under metadata:)"
            )

        name = top_level.get('name', '')
        if name:
            if len(name) > self.SPEC_NAME_MAX or not self.SPEC_NAME_RE.match(name):
                err(
                    f"Spec-invalid name: {name!r} (lowercase alphanumerics and "
                    "single hyphens, no leading/trailing hyphen, max 64 chars)"
                )
            if name != file_path.parent.name:
                err(
                    f"name {name!r} must match skill directory "
                    f"{file_path.parent.name!r}"
                )

        description = top_level.get('description', '').strip('"\'')
        if description and len(description) > self.SPEC_DESCRIPTION_MAX:
            err(
                f"description exceeds spec cap: {len(description)} chars "
                f"(max {self.SPEC_DESCRIPTION_MAX})"
            )


def main():
    repo_root = Path(__file__).parent.parent.parent
    
    print(f"Validating links and schema in: {repo_root}")
    print("=" * 60)
    
    validator = LinkValidator(str(repo_root))
    results = validator.validate_all()
    
    print(f"\n📊 Validation Results")
    print(f"Total files scanned: {results['total_files']}")
    print(f"Total errors: {results['total_errors']}")
    
    # Print errors by category
    if results["ref_file_errors"]:
        print(f"\n❌ ref_file errors ({len(results['ref_file_errors'])}):")
        for error in results["ref_file_errors"]:
            print(f"  {error['file']}: {error['reference']} - {error['error']}")
    
    if results["ref_snippet_errors"]:
        print(f"\n❌ ref_snippet errors ({len(results['ref_snippet_errors'])}):")
        for error in results["ref_snippet_errors"]:
            print(f"  {error['file']}: {error['reference']} ({error['line_range']}) - {error['error']}")
    
    if results["markdown_link_errors"]:
        print(f"\n❌ Markdown link errors ({len(results['markdown_link_errors'])}):")
        for error in results["markdown_link_errors"]:
            print(f"  {error['file']}: [{error['link_text']}]({error['target']}) - {error['error']}")
    
    if results["frontmatter_errors"]:
        print(f"\n❌ Frontmatter errors ({len(results['frontmatter_errors'])}):")
        for error in results["frontmatter_errors"]:
            print(f"  {error['file']}: {error['error']}")
    
    if validator.warnings:
        print(f"\n⚠️  Warnings ({len(validator.warnings)}):")
        for warning in validator.warnings:
            print(f"  {warning}")
    
    if results["total_errors"] == 0:
        print("\n✅ All validations passed!")
        sys.exit(0)
    else:
        print(f"\n❌ Validation failed with {results['total_errors']} errors")
        sys.exit(1)


if __name__ == "__main__":
    main()