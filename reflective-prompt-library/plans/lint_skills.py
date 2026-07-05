#!/usr/bin/env python3
"""
Prompt/Skill Linter for TeaPrompt

Checks:
- Acceptance criteria presence
- Human Review triggers
- Dangerous tool behavior patterns
- Skill body length
- Required sections
- Quality signals
"""

import re
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime


class SkillLinter:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root).resolve()
        self.results = {
            "total_files": 0,
            "total_errors": 0,
            "total_warnings": 0,
            "file_results": []
        }
        
        # Patterns for dangerous operations
        self.dangerous_patterns = [
            r'rm\s+-rf',
            r'drop\s+(table|database)',
            r'delete\s+from',
            r'exec\(',
            r'eval\(',
            r'system\(',
            r'shell_exec',
            r'passthru',
            r'--force',
            r'--yes',
            r'--confirm',
        ]
        
        # Patterns that should trigger Human Review
        self.human_review_patterns = [
            r'production',
            r'deploy',
            r'migration',
            r'billing',
            r'payment',
            r'credit.?card',
            r'social.?security',
            r'password',
            r'api.?key',
            r'secret',
            r'token',
            r'auth',
            r'permission',
            r'admin',
            r'root',
            r'sudo',
        ]
    
    def lint_all(self) -> Dict:
        """Run linter on all markdown files."""
        md_files = list(self.repo_root.rglob("*.md"))
        self.results["total_files"] = len(md_files)
        
        for md_file in md_files:
            file_result = self.lint_file(md_file)
            self.results["file_results"].append(file_result)
            
            if file_result["errors"]:
                self.results["total_errors"] += len(file_result["errors"])
            if file_result["warnings"]:
                self.results["total_warnings"] += len(file_result["warnings"])
        
        return self.results
    
    def lint_file(self, file_path: Path) -> Dict:
        """Lint a single file."""
        try:
            content = file_path.read_text(encoding='utf-8')
            relative_path = file_path.relative_to(self.repo_root)
            
            result = {
                "file": str(relative_path),
                "type": self.detect_file_type(file_path, content),
                "errors": [],
                "warnings": [],
                "suggestions": []
            }
            
            # Run checks based on file type
            if result["type"] == "skill":
                self.lint_skill(content, result)
            else:
                self.lint_prompt(content, result)
            
            # Common checks for all files
            self.check_dangerous_patterns(content, result)
            self.check_human_review_triggers(content, result)
            self.check_body_length(content, result)
            
            return result
            
        except Exception as e:
            return {
                "file": str(file_path.relative_to(self.repo_root)),
                "type": "error",
                "errors": [f"Failed to read file: {e}"],
                "warnings": [],
                "suggestions": []
            }
    
    def detect_file_type(self, file_path: Path, content: str) -> str:
        """Detect if file is a skill or prompt."""
        if file_path.name == "SKILL.md":
            return "skill"
        if content.startswith('---') and 'name:' in content[:500]:
            return "skill"
        return "prompt"
    
    def lint_skill(self, content: str, result: Dict):
        """Lint a skill file."""
        # Check for required sections (TeaPrompt uses Module Contract with subsections)
        required_top_level = [
            "Module Contract"
        ]
        
        for section in required_top_level:
            if not re.search(rf'##\s*{re.escape(section)}', content, re.IGNORECASE):
                result["errors"].append(f"Missing required section: {section}")
        
        # Check for key subsections within Module Contract or as separate sections
        key_subsections = [
            "Trigger",
            "Methods", 
            "Output",
            "Never"
        ]
        
        for subsection in key_subsections:
            # Check as subsection (e.g., "Trigger:") or as separate section
            if not re.search(rf'(##\s*{re.escape(subsection)}|^\*?\*?{re.escape(subsection)}:)', content, re.MULTILINE | re.IGNORECASE):
                result["warnings"].append(f"Missing key subsection: {subsection}")
        
        # Check for escalation section (either as subsection or separate)
        if not re.search(r'(##\s*Escalation|^\*?\*?Escalation:)', content, re.MULTILINE | re.IGNORECASE):
            result["suggestions"].append("Consider adding Escalation section for risk gating")
        
        # Check frontmatter
        if not content.startswith('---'):
            result["errors"].append("Missing frontmatter (required for skills)")
        else:
            frontmatter = self.extract_frontmatter(content)
            if 'name' not in frontmatter:
                result["errors"].append("Missing 'name' in frontmatter")
            if 'description' not in frontmatter:
                result["errors"].append("Missing 'description' in frontmatter")
    
    def lint_prompt(self, content: str, result: Dict):
        """Lint a prompt file."""
        # Check for basic structure
        if len(content) < 50:
            result["warnings"].append("Prompt is very short (< 50 chars)")
        
        # Check for clear purpose/intent
        if not re.search(r'(purpose|intent|goal|objective)', content, re.IGNORECASE):
            result["suggestions"].append("Consider adding a clear Purpose or Intent section")
    
    def check_dangerous_patterns(self, content: str, result: Dict):
        """Check for dangerous operation patterns."""
        for pattern in self.dangerous_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                result["warnings"].append(f"Found potentially dangerous pattern: {pattern} ({len(matches)} occurrences)")
    
    def check_human_review_triggers(self, content: str, result: Dict):
        """Check for content that should trigger Human Review."""
        for pattern in self.human_review_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                result["suggestions"].append(f"Found human review trigger pattern: {pattern} (ensure Human Review gate is present)")
    
    def check_body_length(self, content: str, result: Dict):
        """Check if body length is appropriate."""
        line_count = len(content.splitlines())
        char_count = len(content)
        
        if line_count > 500:
            result["warnings"].append(f"Skill body is very long ({line_count} lines). Consider splitting into smaller skills")
        
        if char_count > 20000:
            result["warnings"].append(f"Skill body is very long ({char_count} chars). May impact routing performance")
        
        if line_count < 10 and result["type"] == "skill":
            result["errors"].append(f"Skill body is too short ({line_count} lines). Skills should have substantive content")
    
    def extract_frontmatter(self, content: str) -> Dict:
        """Extract YAML frontmatter."""
        if not content.startswith('---'):
            return {}
        
        try:
            frontmatter_end = content.find('---', 3)
            if frontmatter_end == -1:
                return {}
            
            frontmatter_text = content[3:frontmatter_end].strip()
            return self.parse_simple_yaml(frontmatter_text)
        except Exception:
            return {}
    
    def parse_simple_yaml(self, text: str) -> dict:
        """Simple YAML parser."""
        result = {}
        for line in text.split('\n'):
            line = line.strip()
            if ':' in line and not line.startswith('#'):
                key, value = line.split(':', 1)
                result[key.strip()] = value.strip()
        return result


def main():
    repo_root = Path(__file__).parent.parent.parent
    
    print(f"Linting skills and prompts in: {repo_root}")
    print("=" * 60)
    
    linter = SkillLinter(str(repo_root))
    results = linter.lint_all()
    
    print(f"\n📊 Linting Results")
    print(f"Total files scanned: {results['total_files']}")
    print(f"Total errors: {results['total_errors']}")
    print(f"Total warnings: {results['total_warnings']}")
    
    # Print files with errors
    error_files = [r for r in results["file_results"] if r["errors"]]
    if error_files:
        print(f"\n❌ Files with errors ({len(error_files)}):")
        for result in error_files:
            print(f"  {result['file']}:")
            for error in result["errors"]:
                print(f"    - {error}")
    
    # Print files with warnings
    warning_files = [r for r in results["file_results"] if r["warnings"]]
    if warning_files:
        print(f"\n⚠️  Files with warnings ({len(warning_files)}):")
        for result in warning_files[:10]:  # Show first 10
            print(f"  {result['file']}:")
            for warning in result["warnings"][:3]:  # Show first 3
                print(f"    - {warning}")
    
    # Print suggestions
    suggestion_files = [r for r in results["file_results"] if r["suggestions"]]
    if suggestion_files:
        print(f"\n💡 Suggestions ({len(suggestion_files)} files):")
        for result in suggestion_files[:5]:  # Show first 5
            print(f"  {result['file']}:")
            for suggestion in result["suggestions"][:2]:  # Show first 2 suggestions
                print(f"    - {suggestion}")
    
    if results["total_errors"] == 0:
        print("\n✅ No linting errors found!")
        if results["total_warnings"] == 0:
            print("✅ No warnings either!")
        else:
            print(f"⚠️  But {results['total_warnings']} warnings found")
        return 0

    print(f"\n❌ Linting failed with {results['total_errors']} errors")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())