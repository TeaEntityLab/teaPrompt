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

The governed-delivery Contract Set is also parsed and checked for required
fields, safe unfilled defaults and version/reference slots (H12-GD). These are
author-side developer checks, not validation of instantiated host records or
proof of gate enforcement. PyYAML is a development dependency only.
"""

import re
from pathlib import Path
from typing import Dict, List

import yaml

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


# Types describe editable slots; literal values protect safety defaults.
# A list of mappings retains at least one specimen so nested slots are exposed.
# Empty lists below forbid pre-granted sinks or pre-claimed product evidence.
_GD_TEMPLATES = {
    "intent-record": {
        "intent_id": str, "goal": str, "out_of_scope": [str],
        "unknowns": [{"item": str, "owner": str}],
        "irreversible_assumptions": [{"item": str, "human_review": "required"}],
        "signed_by": str, "status": "unsigned",
    },
    "oracle-manifest": {
        "spec_version": "",
        "oracles": [{
            "name": str, "class": ("authoritative", "developer"), "owner": str,
            "host_seal": ("write_protection", "protected_branch", "ci_ownership", "none"),
            "change_protocol": "out_of_band",
        }],
    },
    "task-packet": {
        "spec_version": "", "state_ledger_ref": "", "oracle_manifest_ref": "",
        "files": [str], "missing_acceptance": "stop_and_repair",
    },
    "failure-log": {
        "entries": [{
            "oracle": str, "error_class": str, "surface": str,
            "after_correction": False, "exit": ("rollback", "strategy_change", "escalate"),
        }],
    },
    "verification-plan": {
        "channels": [{
            "kind": ("deterministic", "runtime", "external_primary",
                     "independent_model", "self_assessment"),
            "independent": bool,
        }],
        "high_risk_pass_requires_non_model": True,
        "compatibility_bounds": {"tools": str, "models": str, "repos": str},
    },
    "evidence-ledger": {
        "entries": [{
            "claim": str, "source": str, "attester": str,
            "freshness_kind": ("recheck_date", "tracking_event", "immutable_pin"),
            "date_checked": str,
        }],
    },
    "acceptance-record": {
        "spec_version": "", "accepter": str, "oracle_manifest_ref": "",
        "product_evidence_refs": [], "closed": False,
    },
    "envelope": {
        "budget": str, "pause_actions": [str], "kill_conditions": [str],
        "failure_signature_limit": "task_declared", "allowed_sinks": [],
        "accepter": str, "strictness": ("L1", "L2", "L3", "L4", "L5", "L6"),
    },
    "gate-retro": {
        "gates": [{
            "name": ("intent", "spec", "plan", "execution", "verification", "acceptance", "retro"),
            "fired": False, "bypassed": False, "caught_nothing": False,
        }],
        "policy_change": "separate_from_activation",
    },
}


class _TemplateLoader(yaml.SafeLoader):
    """Safe YAML, without duplicate or non-string contract-field ambiguity."""

    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if type(key) is not str or key in result:
                raise yaml.constructor.ConstructorError(
                    None, None, f"duplicate or non-string field: {key!r}", key_node.start_mark,
                )
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def _check_template(value, schema, path: str, errors: List[str]):
    if isinstance(schema, dict):
        if type(value) is not dict:
            errors.append(f"{path}: must be a mapping")
            return
        for key in sorted(value.keys() - schema.keys()):
            errors.append(f"{path}.{key}: unknown field")
        for key, expected in schema.items():
            field = f"{path}.{key}"
            if key not in value:
                errors.append(f"{field}: missing required field")
            else:
                _check_template(value[key], expected, field, errors)
    elif isinstance(schema, list):
        if type(value) is not list:
            errors.append(f"{path}: must be a list")
        elif not schema:
            if value:
                errors.append(f"{path}: must default to an empty list")
        else:
            if isinstance(schema[0], dict) and not value:
                errors.append(f"{path}: missing mapping specimen with required fields")
            for index, item in enumerate(value):
                _check_template(item, schema[0], f"{path}[{index}]", errors)
    elif isinstance(schema, type):
        if type(value) is not schema:
            errors.append(f"{path}: must be {schema.__name__}")
    elif isinstance(schema, tuple):
        if type(value) is not str or value not in schema:
            errors.append(f"{path}: must be one of {schema!r}")
    elif type(value) is not type(schema) or value != schema:
        requirement = "an unbound template slot" if schema == "" else repr(schema)
        errors.append(f"{path}: must default to {requirement}")


def _governed_delivery_template_errors(content: str) -> List[str]:
    errors = []
    blocks = {}
    in_set = False
    section_count = 0
    name = None
    fence_end = None
    body = None
    opener = re.compile(r"^ {0,3}(`{3,}|~{3,})([^`~]*)$")
    for line in content.splitlines():
        if fence_end is not None:
            if fence_end.fullmatch(line):
                if body is not None:
                    blocks[name].append("\n".join(body))
                fence_end, body = None, None
            elif body is not None:
                body.append(line)
            continue
        fence = opener.fullmatch(line)
        if fence:
            marker = fence.group(1)
            fence_end = re.compile(
                r" {0,3}" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}[ \t]*"
            )
            if in_set and name is not None and fence.group(2).strip().lower() == "yaml":
                body = []
            continue
        heading = line.strip()
        if heading == "## Contract Set":
            section_count += 1
            in_set, name = True, None
        elif heading.startswith("## "):
            in_set, name = False, None
        elif in_set and heading.startswith("### "):
            name = heading[4:]
            if name in blocks:
                errors.append(f"{name}: duplicate template heading")
            else:
                blocks[name] = []
    if section_count != 1:
        errors.append("governed-delivery: exactly one Contract Set section is required")
    if body is not None:
        errors.append(f"{name}: unterminated YAML fence")
    for extra in sorted(blocks.keys() - _GD_TEMPLATES.keys()):
        errors.append(f"{extra}: unknown contract template")
    for name, schema in _GD_TEMPLATES.items():
        bodies = blocks.get(name, [])
        if len(bodies) != 1:
            errors.append(f"{name}: exactly one fenced YAML template is required")
            continue
        try:
            data = yaml.load(bodies[0], Loader=_TemplateLoader)
        except yaml.YAMLError as error:
            errors.append(f"{name}: invalid YAML: {error}")
            continue
        prior_errors = len(errors)
        _check_template(data, schema, name, errors)
        if len(errors) != prior_errors:
            continue
        if name == "oracle-manifest":
            for index, oracle in enumerate(data["oracles"]):
                if oracle["class"] == "authoritative" and oracle["host_seal"] == "none":
                    errors.append(f"{name}.oracles[{index}].host_seal: authoritative oracle needs a seal")
            if not any(
                oracle["class"] == "authoritative" and oracle["host_seal"] != "none"
                for oracle in data["oracles"]
            ):
                errors.append(f"{name}.oracles.class: template needs a sealed authoritative oracle")
        elif name == "verification-plan":
            channels = data["channels"]
            for index, channel in enumerate(channels):
                if channel["kind"] == "self_assessment" and channel["independent"]:
                    errors.append(f"{name}.channels[{index}].kind: self-assessment is not independent")
            if not any(
                channel["independent"] and channel["kind"] in
                ("deterministic", "runtime", "external_primary") for channel in channels
            ):
                errors.append(f"{name}.channels: template needs an independent non-model channel")
    return errors


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

            if skill_name == "governed-delivery":
                skill_errors.extend(_governed_delivery_template_errors(content))

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
        print("\n✅ All skills have valid governance metadata and delivery templates!")
    
    return 0 if results["invalid_skills"] == 0 else 1


if __name__ == "__main__":
    exit(main())