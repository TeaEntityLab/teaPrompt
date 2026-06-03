#!/usr/bin/env python3
"""
ROUTE-001: Paraphrase Routing Eval

Verifies routing fairness across equivalent phrasings.
Tests that same intent groups route to the same canonical workflow.
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, asdict


@dataclass
class IntentGroup:
    """A group of paraphrases representing the same intent."""
    name: str
    canonical_workflow: str
    paraphrases: List[str]
    risk_level: str = "low"
    expected_enhancements: List[str] = None


@dataclass
class RoutingResult:
    """Result of routing a single paraphrase."""
    paraphrase: str
    routed_workflow: str
    confidence: float
    enhancements: List[str]
    matched_canonical: bool
    trace: str


class ParaphraseRouter:
    """Simple keyword-based router for testing."""
    
    def __init__(self):
        # Define routing rules based on keywords
        self.routing_rules = {
            "reflective-brief": [
                "clarify", "goal", "assumption", "scope", "acceptance", "kickoff", 
                "start", "begin", "ambiguous", "unclear"
            ],
            "reflective-spec-plan": [
                "spec", "plan", "ticket", "design", "usage", "documentation",
                "implementation plan", "workflow plan"
            ],
            "reflective-implement": [
                "code", "implement", "refactor", "debug", "fix", "edit",
                "programming", "development"
            ],
            "reflective-review": [
                "review", "critique", "check", "audit", "analyze", "examine"
            ],
            "reflective-research": [
                "research", "documentation", "docs", "investigate", "find",
                "look up", "search", "external"
            ],
            "reflective-risk": [
                "risk", "security", "privacy", "auth", "permission", "production",
                "deployment", "migration", "destructive", "billing"
            ],
            "reflective-handoff-retro": [
                "handoff", "retro", "retrospective", "memory", "context",
                "consolidation", "transfer"
            ],
            "reflective-dispatch": [
                "route", "dispatch", "choose", "select", "apply library",
                "workflow", "which skill"
            ]
        }
    
    def route(self, text: str) -> Tuple[str, float, List[str], str]:
        """Route text to a workflow based on keyword matching."""
        text_lower = text.lower()
        
        # Count matches for each workflow
        scores = {}
        for workflow, keywords in self.routing_rules.items():
            score = sum(1 for kw in keywords if kw in text_lower)
            if score > 0:
                scores[workflow] = score
        
        if not scores:
            return "reflective-dispatch", 0.3, [], "No keywords matched, defaulting to dispatch"
        
        # Return highest scoring workflow
        best_workflow = max(scores, key=scores.get)
        confidence = min(0.9, 0.4 + scores[best_workflow] * 0.1)
        
        # Generate trace
        trace = f"Matched keywords for {best_workflow}: {scores[best_workflow]} matches"
        
        return best_workflow, confidence, [], trace


class ParaphraseEval:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root).resolve()
        self.router = ParaphraseRouter()
        self.results = {
            "intent_groups": [],
            "summary": {
                "total_groups": 0,
                "total_paraphrases": 0,
                "consistency_rate": 0.0,
                "avg_confidence": 0.0,
                "groups_below_threshold": []
            }
        }
    
    def define_intent_groups(self) -> List[IntentGroup]:
        """Define test intent groups with paraphrases."""
        return [
            IntentGroup(
                name="implementation_task",
                canonical_workflow="reflective-implement",
                paraphrases=[
                    "Write a function to parse JSON",
                    "Implement a JSON parser",
                    "Code a function that parses JSON data",
                    "Create a JSON parsing function",
                    "Add JSON parsing to the codebase",
                    "Fix the JSON parser bug",
                    "Refactor the JSON parsing logic"
                ],
                risk_level="low"
            ),
            IntentGroup(
                name="spec_planning",
                canonical_workflow="reflective-spec-plan",
                paraphrases=[
                    "Write a spec for the new feature",
                    "Create an implementation plan",
                    "Design the feature specification",
                    "Plan the development tickets",
                    "Document the feature requirements",
                    "Break down the feature into tasks"
                ],
                risk_level="low"
            ),
            IntentGroup(
                name="code_review",
                canonical_workflow="reflective-review",
                paraphrases=[
                    "Review this pull request",
                    "Check the code for issues",
                    "Audit the implementation",
                    "Analyze the code changes",
                    "Examine the pull request",
                    "Look for bugs in this code"
                ],
                risk_level="low"
            ),
            IntentGroup(
                name="research_task",
                canonical_workflow="reflective-research",
                paraphrases=[
                    "Research the best practices for authentication",
                    "Find documentation on React hooks",
                    "Investigate the latest Python frameworks",
                    "Look up the API documentation",
                    "Search for information about Kubernetes",
                    "Find external resources on this topic"
                ],
                risk_level="low"
            ),
            IntentGroup(
                name="risk_gating",
                canonical_workflow="reflective-risk",
                paraphrases=[
                    "Review the security implications",
                    "Check if this is safe for production",
                    "Assess the privacy risks",
                    "Verify the authentication changes",
                    "Review the deployment plan for risks",
                    "Check the migration safety"
                ],
                risk_level="high"
            ),
            IntentGroup(
                name="clarification",
                canonical_workflow="reflective-brief",
                paraphrases=[
                    "Clarify the requirements",
                    "Define the goals and assumptions",
                    "What should we build?",
                    "Start by defining the scope",
                    "Kick off the project planning",
                    "Begin with goal clarification"
                ],
                risk_level="low"
            )
        ]
    
    def run_eval(self) -> Dict:
        """Run the paraphrase routing evaluation."""
        intent_groups = self.define_intent_groups()
        self.results["summary"]["total_groups"] = len(intent_groups)
        
        total_paraphrases = 0
        total_matches = 0
        total_confidence = 0.0
        
        for group in intent_groups:
            group_result = {
                "name": group.name,
                "canonical_workflow": group.canonical_workflow,
                "paraphrase_results": [],
                "consistency_rate": 0.0,
                "avg_confidence": 0.0
            }
            
            group_matches = 0
            group_confidence = 0.0
            
            for paraphrase in group.paraphrases:
                workflow, confidence, enhancements, trace = self.router.route(paraphrase)
                
                matched = (workflow == group.canonical_workflow)
                if matched:
                    group_matches += 1
                    total_matches += 1
                
                group_confidence += confidence
                total_confidence += confidence
                total_paraphrases += 1
                
                result = RoutingResult(
                    paraphrase=paraphrase,
                    routed_workflow=workflow,
                    confidence=confidence,
                    enhancements=enhancements,
                    matched_canonical=matched,
                    trace=trace
                )
                
                group_result["paraphrase_results"].append(asdict(result))
            
            # Calculate group statistics
            group_result["consistency_rate"] = group_matches / len(group.paraphrases)
            group_result["avg_confidence"] = group_confidence / len(group.paraphrases)
            
            # Check if below 95% threshold
            if group_result["consistency_rate"] < 0.95:
                self.results["summary"]["groups_below_threshold"].append({
                    "group": group.name,
                    "rate": group_result["consistency_rate"]
                })
            
            self.results["intent_groups"].append(group_result)
        
        # Calculate overall statistics
        self.results["summary"]["total_paraphrases"] = total_paraphrases
        self.results["summary"]["consistency_rate"] = total_matches / total_paraphrases if total_paraphrases > 0 else 0
        self.results["summary"]["avg_confidence"] = total_confidence / total_paraphrases if total_paraphrases > 0 else 0
        
        return self.results
    
    def generate_report(self) -> str:
        """Generate a human-readable report."""
        lines = []
        lines.append("=" * 70)
        lines.append("ROUTE-001: Paraphrase Routing Evaluation Report")
        lines.append("=" * 70)
        lines.append("")
        
        # Summary
        summary = self.results["summary"]
        lines.append("📊 Summary")
        lines.append(f"Total intent groups: {summary['total_groups']}")
        lines.append(f"Total paraphrases tested: {summary['total_paraphrases']}")
        lines.append(f"Overall consistency rate: {summary['consistency_rate']:.1%}")
        lines.append(f"Average confidence: {summary['avg_confidence']:.2f}")
        lines.append("")
        
        # Threshold check
        if summary["groups_below_threshold"]:
            lines.append("❌ Groups below 95% consistency threshold:")
            for item in summary["groups_below_threshold"]:
                lines.append(f"  - {item['group']}: {item['rate']:.1%}")
            lines.append("")
        else:
            lines.append("✅ All groups meet 95% consistency threshold")
            lines.append("")
        
        # Per-group details
        lines.append("📋 Per-Group Results")
        lines.append("")
        
        for group in self.results["intent_groups"]:
            lines.append(f"Group: {group['name']}")
            lines.append(f"Canonical workflow: {group['canonical_workflow']}")
            lines.append(f"Consistency: {group['consistency_rate']:.1%}")
            lines.append(f"Avg confidence: {group['avg_confidence']:.2f}")
            lines.append("")
            
            # Show mismatches if any
            mismatches = [r for r in group["paraphrase_results"] if not r["matched_canonical"]]
            if mismatches:
                lines.append("  Mismatches:")
                for mismatch in mismatches:
                    lines.append(f"    - \"{mismatch['paraphrase']}\"")
                    lines.append(f"      Routed to: {mismatch['routed_workflow']}")
                    lines.append(f"      Trace: {mismatch['trace']}")
                lines.append("")
        
        return "\n".join(lines)


def main():
    repo_root = Path(__file__).parent.parent.parent
    
    print(f"Running ROUTE-001 Paraphrase Routing Eval")
    print("=" * 60)
    
    eval = ParaphraseEval(str(repo_root))
    results = eval.run_eval()
    
    # Generate and print report
    report = eval.generate_report()
    print(report)
    
    # Save results to JSON
    output_file = Path(__file__).parent / "route-001-results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Results saved to: {output_file}")
    
    # Exit with appropriate code
    if results["summary"]["consistency_rate"] >= 0.95:
        print("✅ Eval passed: 95% consistency threshold met")
        return 0
    else:
        print(f"❌ Eval failed: {results['summary']['consistency_rate']:.1%} consistency < 95% threshold")
        return 1


if __name__ == "__main__":
    exit(main())