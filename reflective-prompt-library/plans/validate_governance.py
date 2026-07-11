#!/usr/bin/env python3
"""
Governance Metadata Validator

Validates that all SKILL.md files have required governance metadata:
- risk_level (low/medium/high)
- human_review_required (true/false)
- external_io (true/false)
- context_load (low/medium/high)

Canonical position since the 2026-07-11 spec-conformance migration: nested under
the Agent Skills `metadata:` map (agentskills.io allows only name/description/
license/compatibility/metadata/allowed-tools at top level; validate_links.py
enforces that whitelist). This validator's line-based parser flattens the
metadata map, so it reads the fields in either position; spec conformance is
validate_links.py's job, semantics are this validator's job.

Also enforces the skills-directory registry: every SKILL.md under skills/
must be one of the nine frozen CORE_SKILLS or a registered domain-pack skill
(2026-07-11 flow-control pack panel, Option B). Domain packs must self-label
as domain packs and never claim a core context-load row.
"""

import re
from pathlib import Path
from typing import Dict, List

from validate_skill_examples import CORE_SKILLS, DOMAIN_PACK_SKILLS


CANONICAL_CONTEXT_LOAD = {
    "reflective-dispatch": "low",
    "reflective-brief": "low",
    "reflective-minimality": "low",
    "reflective-implement": "medium",
    "reflective-review": "medium",
    "reflective-risk": "medium",
    "reflective-handoff-retro": "medium",
    "reflective-spec-plan": "high",
    "reflective-research": "high",
}


class GovernanceValidator:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root).resolve()
        self.results = {
            "total_skills": 0,
            "valid_skills": 0,
            "invalid_skills": 0,
            "errors": []
        }
    
    def validate_all(self) -> Dict:
        """Validate governance metadata for all skills."""
        skills_dir = self.repo_root / "reflective-prompt-library" / "skills"
        
        if not skills_dir.exists():
            self.results["errors"].append("Skills directory not found")
            return self.results
        
        # Find all SKILL.md files
        skill_files = list(skills_dir.rglob("SKILL.md"))

        registered = set(CORE_SKILLS) | set(DOMAIN_PACK_SKILLS)
        found = {f.parent.name for f in skill_files}
        for name in sorted(found - registered):
            self.results["invalid_skills"] += 1
            self.results["errors"].append({
                "file": f"reflective-prompt-library/skills/{name}/SKILL.md",
                "errors": [
                    "Unregistered skill directory: add to CORE_SKILLS (nine, "
                    "frozen, promotion-gated) or DOMAIN_PACK_SKILLS in "
                    "validate_skill_examples.py with a panel/decision record"
                ],
            })
        self.results["total_skills"] = len(skill_files)
        
        for skill_file in skill_files:
            self.validate_skill(skill_file)
        
        return self.results
    
    def validate_skill(self, skill_file: Path):
        """Validate a single skill file."""
        try:
            content = skill_file.read_text(encoding='utf-8')
            relative_path = skill_file.relative_to(self.repo_root)
            
            # Extract frontmatter
            frontmatter = self.extract_frontmatter(content)
            
            # Check required fields
            required_fields = {
                'risk_level': ['low', 'medium', 'high'],
                'human_review_required': ['true', 'false'],
                'external_io': ['true', 'false'],
                'context_load': ['low', 'medium', 'high'],
            }
            
            skill_errors = []
            
            for field, valid_values in required_fields.items():
                if field not in frontmatter:
                    skill_errors.append(f"Missing required field: {field}")
                else:
                    value = frontmatter[field].lower()
                    if value not in valid_values:
                        skill_errors.append(f"Invalid value for {field}: {frontmatter[field]} (must be one of {valid_values})")
            
            skill_name = skill_file.parent.name
            expected_load = CANONICAL_CONTEXT_LOAD.get(skill_name)
            if expected_load and frontmatter.get("context_load", "").lower() != expected_load:
                skill_errors.append(
                    f"context_load must be {expected_load!r} for {skill_name} (panel table)"
                )

            if skill_name in DOMAIN_PACK_SKILLS:
                if skill_name in CANONICAL_CONTEXT_LOAD:
                    skill_errors.append(
                        f"{skill_name} is a domain pack and must not appear in "
                        "CANONICAL_CONTEXT_LOAD (core table)"
                    )
                if "domain-pack" not in content.lower():
                    skill_errors.append(
                        "Domain-pack skill must self-label: body must state it "
                        "is a domain pack, not one of the nine core workflow "
                        "skills"
                    )

            if skill_errors:
                self.results["invalid_skills"] += 1
                self.results["errors"].append({
                    "file": str(relative_path),
                    "errors": skill_errors
                })
            else:
                self.results["valid_skills"] += 1
                
        except Exception as e:
            self.results["errors"].append({
                "file": str(skill_file.relative_to(self.repo_root)),
                "errors": [f"Failed to read file: {e}"]
            })
            self.results["invalid_skills"] += 1
    
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
    
    print(f"Validating governance metadata in: {repo_root}")
    print("=" * 60)
    
    validator = GovernanceValidator(str(repo_root))
    results = validator.validate_all()
    
    print(f"\n📊 Governance Metadata Validation")
    print(f"Total skills: {results['total_skills']}")
    print(f"Valid skills: {results['valid_skills']}")
    print(f"Invalid skills: {results['invalid_skills']}")
    
    if results["errors"]:
        print(f"\n❌ Errors found:")
        for error in results["errors"]:
            if isinstance(error, dict):
                print(f"  {error['file']}:")
                for err in error["errors"]:
                    print(f"    - {err}")
            else:
                print(f"  {error}")
    else:
        print("\n✅ All skills have valid governance metadata!")
    
    return 0 if results["invalid_skills"] == 0 else 1


if __name__ == "__main__":
    exit(main())