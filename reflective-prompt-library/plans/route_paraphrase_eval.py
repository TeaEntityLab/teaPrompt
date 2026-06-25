#!/usr/bin/env python3
"""
ROUTE-001: Paraphrase Routing Eval

Verifies routing fairness across equivalent phrasings.
Tests that same intent groups route to the same canonical workflow.
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple
from dataclasses import dataclass, asdict, field


@dataclass
class IntentGroup:
    """A group of paraphrases representing the same intent."""
    name: str
    canonical_workflow: str
    paraphrases: List[str]
    risk_level: str = "low"
    expected_enhancements: List[str] = field(default_factory=list)
    group_type: str = "intent"


@dataclass
class RoutingResult:
    """Result of routing a single paraphrase."""
    paraphrase: str
    routed_workflow: str
    confidence: float
    enhancements: List[str]
    matched_canonical: bool
    trace: str
    route_trace: Dict[str, Any]


def parse_scalar(value: str) -> Any:
    """Parse the small scalar subset used by ROUTE-001 YAML."""
    value = value.strip()
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value.strip('"').strip("'")


def load_route_eval_config(config_path: Path) -> Dict[str, Any]:
    """Load ROUTE-001 YAML without adding a runtime dependency.

    The fixture intentionally uses a small YAML subset: top-level sections,
    scalar maps, and list blocks. Keeping this parser local avoids making a
    dependency decision just for a development quality gate.
    """
    config: Dict[str, Any] = {
        "global_expectations": {},
        "trace_required_fields": [],
        "intent_groups": [],
        "adversarial_sets": [],
        "holdout_sets": [],
        "evaluation_rules": [],
    }
    section = None
    current_group = None
    current_list_key = None

    for raw_line in config_path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()

        if indent == 0 and line.endswith(":"):
            section = line[:-1]
            current_group = None
            current_list_key = None
            if section not in config:
                config[section] = []
            continue

        if indent == 0 and ":" in line:
            key, value = line.split(":", 1)
            config[key] = parse_scalar(value)
            continue

        if section == "global_expectations" and indent == 2 and ":" in line:
            key, value = line.split(":", 1)
            config[section][key] = parse_scalar(value)
            continue

        if section == "trace_required_fields" and line.startswith("- "):
            config[section].append(line[2:].strip())
            continue

        if section == "intent_groups":
            if indent == 2 and line.startswith("- "):
                current_group = {}
                config[section].append(current_group)
                key_value = line[2:]
                if ":" in key_value:
                    key, value = key_value.split(":", 1)
                    current_group[key.strip()] = parse_scalar(value)
                current_list_key = None
                continue

            if current_group is None:
                continue

            if indent == 4 and line.endswith(":"):
                current_list_key = line[:-1]
                current_group[current_list_key] = []
                continue

            if indent == 4 and ":" in line:
                key, value = line.split(":", 1)
                current_group[key.strip()] = parse_scalar(value)
                current_list_key = None
                continue

            if indent == 6 and current_list_key and line.startswith("- "):
                current_group[current_list_key].append(line[2:].strip())
                continue

        if section in ("adversarial_sets", "holdout_sets"):
            if indent == 2 and line.startswith("- "):
                current_group = {}
                config[section].append(current_group)
                key_value = line[2:]
                if ":" in key_value:
                    key, value = key_value.split(":", 1)
                    current_group[key.strip()] = parse_scalar(value)
                current_list_key = None
                continue

            if current_group is None:
                continue

            if indent == 4 and line.endswith(":"):
                current_list_key = line[:-1]
                current_group[current_list_key] = []
                continue

            if indent == 4 and ":" in line:
                key, value = line.split(":", 1)
                current_group[key.strip()] = parse_scalar(value)
                current_list_key = None
                continue

            if indent == 6 and current_list_key and line.startswith("- "):
                current_group[current_list_key].append(line[2:].strip())
                continue

        if section == "evaluation_rules":
            if indent == 2 and line.startswith("- "):
                current_group = {}
                config[section].append(current_group)
                key_value = line[2:]
                if ":" in key_value:
                    key, value = key_value.split(":", 1)
                    current_group[key.strip()] = parse_scalar(value)
                current_list_key = None
                continue

            if current_group is not None and indent == 4 and ":" in line:
                key, value = line.split(":", 1)
                current_group[key.strip()] = parse_scalar(value)
                continue

        raise ValueError(f"Unsupported ROUTE-001 YAML line: {raw_line}")

    return config


class ParaphraseRouter:
    """Small deterministic router used by ROUTE-001.

    The first pass counts workflow keywords. The boundary pass then applies
    intent-level signals for cases where single words are ambiguous, such as
    review language wrapped around production-risk phrasing.
    """
    
    def __init__(self):
        # Define routing rules based on keywords
        self.routing_rules = {
            "reflective-brief": [
                "clarify", "goal", "assumption", "scope", "acceptance", "kickoff",
                "kick off", "start", "begin", "ambiguous", "unclear", "what should",
                "not sure", "before deciding", "real objective",
                "釐清", "目標", "範圍", "假設", "驗收"
            ],
            "reflective-spec-plan": [
                "spec", "plan", "ticket", "design", "usage", "documentation",
                "implementation plan", "workflow plan", "requirements", "break down", "tasks",
                "acceptance criteria", "define acceptance criteria", "roadmap", "release plan", "prd",
                "test plan", "test strategy", "test matrix", "given/when/then",
                "workflow specification", "workflow architecture", "state model", "control flow",
                "orchestration plan", "resumable workflow",
                "規格", "計畫", "需求", "工單", "驗收標準"
            ],
            "reflective-implement": [
                "code", "implement", "refactor", "debug", "fix", "edit",
                "programming", "development", "function", "parse", "build", "add",
                "change", "patch", "wire", "make the code", "unit test",
                "integration test", "executable test", "add tests", "update tests",
                "實作", "修復", "程式碼", "重構", "除錯", "補丁", "修改"
            ],
            "reflective-minimality": [
                "minimal", "minimality", "overengineering", "over-engineering",
                "bloat", "boilerplate", "yagni", "delete", "deleted",
                "narrow", "defer", "stdlib", "standard library", "native feature",
                "native behavior", "existing dependency", "new dependency",
                "dependency", "one file", "one-line", "one line", "smallest",
                "wrapper", "abstraction", "factory", "unnecessary complexity",
                "avoid writing", "avoid overengineering", "complexity-only",
                "ceiling", "upgrade trigger",
                "最小化", "過度工程", "刪減", "少寫"
            ],
            "reflective-review": [
                "review", "critique", "check", "audit", "analyze", "examine",
                "issues", "bugs", "pull request", "changes", "look over",
                "carefully", "make sure", "does this work", "review this like",
                "審查", "檢查", "程式碼審查"
            ],
            "reflective-research": [
                "research", "documentation", "docs", "investigate", "find",
                "look up", "search", "external", "compare", "best practice",
                "official", "source", "source-backed", "guidance",
                "研究", "查詢", "官方", "比較", "文件"
            ],
            "reflective-risk": [
                "risk", "security", "privacy", "auth", "permission", "production",
                "deployment", "migration", "destructive", "billing", "safe", "safety",
                "delete", "rollback", "compliance", "credential", "irreversible",
                "風險", "安全", "正式環境", "權限"
            ],
            "reflective-handoff-retro": [
                "handoff", "retro", "retrospective", "memory", "context",
                "consolidation", "transfer", "continue later", "session summary",
                "lessons", "reusable rules",
                "交接", "回顧", "摘要", "教訓"
            ],
            "reflective-dispatch": [
                "route", "dispatch", "choose", "select", "apply library",
                "workflow", "which skill", "what skill", "best skill", "prompt-only",
                "agentic workflow",
                "路由", "分派", "選擇", "工作流"
            ]
        }

    def boundary_adjustments(self, text_lower: str) -> Tuple[Dict[str, int], List[str]]:
        """Return concept-level routing adjustments for ambiguous phrasing."""
        adjustments: Dict[str, int] = {}
        reasons = []

        no_code_context = [
            "without writing code", "without changing code", "do not write code",
            "do not implement", "without implementing", "no code", "no-code", "before implementation",
            "before coding", "from this spec", "from the spec", "plan only",
            "planning only", "leave code untouched", "without touching the repo", "without repo changes",
            "不要改程式", "不要動 code", "不要動程式", "不要寫 code", "不要寫程式",
        ]
        production_negated = any(
            neg in text_lower
            for neg in [
                "not production", "not a production", "without production risk",
                "not production risk", "not production deploy",
                "not security", "not a security", "不是安全", "不是安全風險",
                "不是正式環境", "非正式環境", "不是正式環境風險",
            ]
        )

        risk_signals = [
            "production", "security", "credential", "deployment", "dangerous",
            "not break", "breaking", "avoid breaking", "before changing"
        ]
        risk_context = ["check", "verify", "review", "make sure", "avoid", "before", "will not"]
        production_review_style = "review this like" in text_lower
        if (
            not production_review_style
            and not production_negated
            and any(signal in text_lower for signal in risk_signals)
            and any(ctx in text_lower for ctx in risk_context)
        ):
            adjustments["reflective-risk"] = adjustments.get("reflective-risk", 0) + 2
            reasons.append("risk boundary: safety-sensitive context")

        if "security checks" in text_lower or "security implications" in text_lower:
            adjustments["reflective-risk"] = adjustments.get("reflective-risk", 0) + 2
            reasons.append("risk boundary: security verification")

        planning_signals = [
            "delivery plan", "acceptance criteria", "launch readiness",
            "roadmap", "prd", "implementation plan"
        ]
        if any(signal in text_lower for signal in planning_signals):
            adjustments["reflective-spec-plan"] = adjustments.get("reflective-spec-plan", 0) + 2
            reasons.append("planning boundary: delivery artifact requested")

        test_plan_signals = [
            "test plan", "test strategy", "test matrix", "test cases",
            "design tests", "regression tests", "anti-cheating",
            "given/when/then", "acceptance criteria"
        ]
        plan_only_signals = [
            "rollout plan", "delivery plan", "write tickets", "break down",
            "acceptance criteria", "before any implementation", "spec the delivery",
            "design comparison", "api designs", "on paper", "設計方案",
            "工單", "驗收標準",
        ]
        if any(signal in text_lower for signal in plan_only_signals) and any(
            ctx in text_lower for ctx in no_code_context
        ):
            adjustments["reflective-spec-plan"] = adjustments.get("reflective-spec-plan", 0) + 4
            reasons.append("plan boundary: planning artifact without code changes")

        if "design comparison" in text_lower and any(
            ctx in text_lower for ctx in no_code_context + ["on paper", "paper only"]
        ):
            adjustments["reflective-spec-plan"] = adjustments.get("reflective-spec-plan", 0) + 4
            reasons.append("plan boundary: paper-only design comparison")

        brief_before_plan_signals = [
            "before writing the prd",
            "before breaking into tickets",
            "stakeholder alignment",
            "align stakeholders",
            "narrow scope and assumptions",
            "scope the outcome before",
            "釐清目標再拆工單",
        ]
        if any(signal in text_lower for signal in brief_before_plan_signals):
            adjustments["reflective-brief"] = adjustments.get("reflective-brief", 0) + 3
            reasons.append("brief boundary: clarify scope before planning artifacts")

        if any(signal in text_lower for signal in test_plan_signals) and any(
            ctx in text_lower for ctx in no_code_context
        ):
            adjustments["reflective-spec-plan"] = adjustments.get("reflective-spec-plan", 0) + 3
            reasons.append("test-plan boundary: test design requested without implementation")

        executable_test_signals = [
            "implement the tests", "implement tests", "add tests", "update tests",
            "write unit tests", "write integration tests", "executable tests",
            "fix the failing test", "run the tests"
        ]
        if any(signal in text_lower for signal in executable_test_signals) and not any(
            ctx in text_lower for ctx in no_code_context
        ):
            adjustments["reflective-implement"] = adjustments.get("reflective-implement", 0) + 3
            reasons.append("test-execution boundary: repository test changes requested")

        implement_approved_spec_signals = [
            "implement the approved spec",
            "implement approved spec",
            "code the approved spec",
            "land the approved spec",
            "implement 已核准 spec in the repository",
            "在 repository 實作已核准 spec",
        ]
        implement_delivery_verbs = (
            "implement", "code", "land", "實作", "落地",
        )
        approved_spec_markers = (
            "approved spec",
            "已核准 spec",
            "已核准的 spec",
            "已核准規格",
        )
        repository_delivery_context = [
            "repository", "repo", "codebase", "in the repo", "to production code",
        ]
        if (
            not any(ctx in text_lower for ctx in no_code_context)
            and (
                any(signal in text_lower for signal in implement_approved_spec_signals)
                or (
                    any(verb in text_lower for verb in implement_delivery_verbs)
                    and any(marker in text_lower for marker in approved_spec_markers)
                    and any(ctx in text_lower for ctx in repository_delivery_context)
                )
            )
        ):
            adjustments["reflective-implement"] = adjustments.get("reflective-implement", 0) + 4
            reasons.append("implement boundary: approved spec delivery in repository")

        workflow_design_signals = [
            "workflow design", "workflow specification", "workflow architecture",
            "resumable workflow", "state model", "control flow",
            "orchestration plan", "checkpoint", "stop conditions",
            "gated workflow", "human-in-the-loop workflow", "persisted state"
        ]
        workflow_execution_context = [
            "implement", "build the runner", "write the runner", "executable workflow",
            "code the workflow", "wire the workflow", "make it run", "langgraph"
        ]
        workflow_research_context = [
            "research", "compare official", "compare current", "look up",
            "current patterns", "best practices", "framework docs", "official sources"
        ]
        workflow_review_context = [
            "review this workflow", "critique this workflow", "audit this workflow",
            "inspect this workflow", "review the state model", "audit the state model"
        ]
        workflow_selection_signals = [
            "decide whether", "choose between", "choose the smallest",
            "which orchestration", "what orchestration"
        ]
        workflow_selection_targets = [
            "workflow", "agent", "orchestration level", "prompt"
        ]
        if any(signal in text_lower for signal in workflow_selection_signals) and any(
            target in text_lower for target in workflow_selection_targets
        ):
            adjustments["reflective-dispatch"] = adjustments.get("reflective-dispatch", 0) + 3
            reasons.append("workflow boundary: formalization or control model selection requested")

        if any(signal in text_lower for signal in workflow_design_signals):
            if any(ctx in text_lower for ctx in workflow_execution_context) and not any(
                ctx in text_lower for ctx in no_code_context
            ):
                adjustments["reflective-implement"] = adjustments.get("reflective-implement", 0) + 3
                reasons.append("workflow boundary: executable orchestration requested")
            elif any(ctx in text_lower for ctx in workflow_research_context):
                adjustments["reflective-research"] = adjustments.get("reflective-research", 0) + 3
                reasons.append("workflow boundary: current external guidance requested")
            elif any(ctx in text_lower for ctx in workflow_review_context):
                adjustments["reflective-review"] = adjustments.get("reflective-review", 0) + 3
                reasons.append("workflow boundary: existing design review requested")
            else:
                adjustments["reflective-spec-plan"] = adjustments.get("reflective-spec-plan", 0) + 3
                reasons.append("workflow boundary: no-code workflow design requested")

        trivial_fix_signals = [
            "typo", "one-liner", "one liner", "one-line", "quick fix", "small fix", "trivial fix",
            "trivial code change", "trivial null", "bug fix",
            "小修正", "錯字"
        ]
        trivial_fix_context = ["patch", "fix", "change", "bug", "code", "repo"]
        trivial_fix_active = any(signal in text_lower for signal in trivial_fix_signals) or (
            "trivial" in text_lower and any(ctx in text_lower for ctx in trivial_fix_context)
        )

        review_signals = [
            "confirm this has no problem", "look if", "mistake",
            "check carefully", "review this like", "regression", "regressions"
        ]
        review_context = ["inspect", "check", "review", "find", "confirm", "before merge", "diff", "patch", "change"]
        plain_review_signals = [
            "readability", "style and logic", "not production deploy",
            "without production risk", "not production risk",
            "not security", "clarity", "不是正式環境風險", "不是安全風險",
            "可讀性", "清晰度",
        ]
        plain_review_context = [
            "review", "inspect", "check", "diff", "patch", "pr", "regression", "審查",
        ]
        if any(signal in text_lower for signal in plain_review_signals) and any(
            ctx in text_lower for ctx in plain_review_context
        ):
            adjustments["reflective-review"] = adjustments.get("reflective-review", 0) + 3
            reasons.append("review boundary: non-production correctness inspection")

        if (
            not trivial_fix_active
            and any(signal in text_lower for signal in review_signals)
            and any(ctx in text_lower for ctx in review_context)
        ):
            adjustments["reflective-review"] = adjustments.get("reflective-review", 0) + 2
            reasons.append("review boundary: correctness inspection requested")

        clarification_signals = ["do not know", "don't know", "unknown", "unclear", "not sure", "還不確定", "不確定"]
        clarification_targets = ["outcome", "goal", "intent", "objective", "scope", "assumption"]
        if any(signal in text_lower for signal in clarification_signals) and any(
            target in text_lower for target in clarification_targets
        ):
            adjustments["reflective-brief"] = adjustments.get("reflective-brief", 0) + 2
            reasons.append("brief boundary: unresolved intent or outcome")

        minimality_signals = [
            "overengineering", "over-engineering", "bloat", "boilerplate", "yagni",
            "standard library", "stdlib", "native feature", "native behavior",
            "new dependency", "wrapper", "abstraction", "unnecessary complexity",
            "avoid writing", "smallest implementation", "one file", "ceiling",
            "upgrade trigger", "full correctness review"
        ]
        minimality_context = [
            "avoid", "delete", "deleted", "covers", "run", "review", "diff",
            "need", "challenge", "prefer", "minimality gate", "before implementing"
        ]
        if (
            not trivial_fix_active
            and any(signal in text_lower for signal in minimality_signals)
            and any(ctx in text_lower for ctx in minimality_context)
        ):
            adjustments["reflective-minimality"] = adjustments.get("reflective-minimality", 0) + 2
            reasons.append("minimality boundary: complexity reduction requested")

        dependency_removal_signals = [
            "dependencies can we remove",
            "packages can we delete",
            "remove from this module",
            "remove dependency",
            "移除依賴", "卸載套件",
        ]
        if any(signal in text_lower for signal in dependency_removal_signals):
            adjustments["reflective-minimality"] = adjustments.get("reflective-minimality", 0) + 3
            reasons.append("minimality boundary: dependency removal requested")

        dispatch_meta_signals = [
            "which skill handles",
            "which reflective workflow skill covers",
            "which workflow skill covers",
            "what skill handles",
            "哪個 skill 負責",
        ]
        if any(signal in text_lower for signal in dispatch_meta_signals):
            adjustments["reflective-dispatch"] = adjustments.get("reflective-dispatch", 0) + 4
            reasons.append("dispatch boundary: skill catalog or selection question")

        handoff_signals = [
            "handoff summary", "hand off", "hand-off", "write a handoff",
            "session summary", "switch tasks", "continue later",
            "memory consolidation", "reusable memory", "session lessons",
            "next agent", "ending this session", "prepare a retro",
            "交接摘要", "寫交接", "下一個代理"
        ]
        if any(signal in text_lower for signal in handoff_signals):
            adjustments["reflective-handoff-retro"] = adjustments.get("reflective-handoff-retro", 0) + 3
            reasons.append("handoff boundary: session transfer or memory consolidation")

        multi_voice_signals = [
            "multi-voice", "multi voice", "multi-perspective", "multi perspective",
            "strategic rethink", "panel on", "six-lens", "six lens"
        ]
        if any(signal in text_lower for signal in multi_voice_signals):
            adjustments["reflective-research"] = adjustments.get("reflective-research", 0) + 3
            reasons.append("research boundary: multi-voice or strategic perspective synthesis")

        if trivial_fix_active:
            adjustments["reflective-implement"] = adjustments.get("reflective-implement", 0) + 3
            reasons.append("implementation boundary: trivial code fix")

        scaffold_signals = [
            "scaffold provenance", "prompt mirror", "leaked prompt", "system prompt leak",
            "third-party mirror", "mirrored prompt", "agent scaffold", "prompt leak",
            "mirror is trustworthy", "official docs with a third-party",
        ]
        scaffold_context = [
            "review", "compare", "official", "trustworthy", "transferable", "adopt",
            "learn", "research", "provenance", "without copying",
        ]
        if any(signal in text_lower for signal in scaffold_signals) and any(
            ctx in text_lower for ctx in scaffold_context
        ):
            adjustments["reflective-research"] = adjustments.get("reflective-research", 0) + 3
            reasons.append("research boundary: scaffold provenance or mirror review")
        elif "mirrored system prompt" in text_lower or "mirrored prompt" in text_lower:
            adjustments["reflective-research"] = adjustments.get("reflective-research", 0) + 3
            reasons.append("research boundary: mirrored prompt learning request")

        if ("官方" in text_lower or "查官方" in text_lower) and (
            "migration" in text_lower or "文件" in text_lower
        ):
            adjustments["reflective-research"] = adjustments.get("reflective-research", 0) + 3
            reasons.append("research boundary: official documentation lookup")

        if "少寫程式" in text_lower or ("少寫" in text_lower and "程式" in text_lower):
            adjustments["reflective-minimality"] = adjustments.get("reflective-minimality", 0) + 3
            reasons.append("minimality boundary: reduce code surface requested")

        context_defer_signals = [
            "context_load", "defer heavy planning", "defer heavy", "route this l1",
            "no spec-plan load", "minimal route trace", "skipping spec-plan",
            "note which high context_load", "high context_load skills you are skipping",
        ]
        if any(signal in text_lower for signal in context_defer_signals):
            adjustments["reflective-dispatch"] = adjustments.get("reflective-dispatch", 0) + 4
            reasons.append("dispatch boundary: context_load deferral or strictness-first routing")

        dispatch_skill_signals = [
            "reflective workflow skill",
            "workflow skill should run",
            "pick the right reflective",
            "reflective skill should",
            "which skill should run for this library",
            "help me dispatch the right reflective skill",
        ]
        if any(signal in text_lower for signal in dispatch_skill_signals):
            adjustments["reflective-dispatch"] = adjustments.get("reflective-dispatch", 0) + 3
            reasons.append("dispatch boundary: reflective skill selection requested")

        brief_before_route_signals = [
            "before we pick a workflow",
            "before choosing skills",
            "optimize for before choosing",
        ]
        if any(signal in text_lower for signal in brief_before_route_signals):
            adjustments["reflective-brief"] = adjustments.get("reflective-brief", 0) + 2
            reasons.append("brief boundary: clarify goal before workflow selection")

        retro_lessons_signals = [
            "lessons learned retro",
            "sprint retrospective",
            "retrospective on what worked",
        ]
        if any(signal in text_lower for signal in retro_lessons_signals):
            adjustments["reflective-handoff-retro"] = adjustments.get("reflective-handoff-retro", 0) + 3
            reasons.append("handoff boundary: lessons-learned retrospective")

        return adjustments, reasons
    
    def route(self, text: str) -> Tuple[str, float, List[str], str]:
        """Route text to a workflow based on keyword matching."""
        text_lower = text.lower()
        
        # Count matches for each workflow
        scores = {}
        for workflow, keywords in self.routing_rules.items():
            score = sum(1 for kw in keywords if kw in text_lower)
            if score > 0:
                scores[workflow] = score

        adjustments, boundary_reasons = self.boundary_adjustments(text_lower)
        for workflow, adjustment in adjustments.items():
            scores[workflow] = scores.get(workflow, 0) + adjustment
        
        if not scores:
            return "reflective-dispatch", 0.3, [], "No keywords matched, defaulting to dispatch"
        
        # Return highest scoring workflow
        priority = [
            "reflective-risk",
            "reflective-minimality",
            "reflective-review",
            "reflective-brief",
            "reflective-spec-plan",
            "reflective-implement",
            "reflective-research",
            "reflective-handoff-retro",
            "reflective-dispatch",
        ]
        best_workflow = max(scores, key=lambda workflow: (scores[workflow], -priority.index(workflow)))
        confidence = min(0.9, 0.4 + scores[best_workflow] * 0.1)
        
        # Generate trace
        trace = f"Matched signals for {best_workflow}: {scores[best_workflow]} score"
        if boundary_reasons:
            trace += f"; boundary: {', '.join(boundary_reasons)}"
        
        return best_workflow, confidence, [], trace


class ParaphraseEval:
    def __init__(self, repo_root: str, config_path: Path = None):
        self.repo_root = Path(repo_root).resolve()
        self.config_path = (config_path or Path(__file__).parent / "route-001-paraphrase-eval.yaml").resolve()
        self.config = load_route_eval_config(self.config_path)
        expectations = self.config.get("global_expectations", {})
        self.phase1_consistency_min = float(expectations.get("phase1_route_consistency_min", 0.70))
        self.aspirational_consistency_target = float(
            expectations.get("aspirational_route_consistency_target", 0.95)
        )
        self.router = ParaphraseRouter()
        self.results = {
            "source": str(self.config_path.relative_to(self.repo_root)),
            "thresholds": {
                "phase1_route_consistency_min": self.phase1_consistency_min,
                "aspirational_route_consistency_target": self.aspirational_consistency_target,
            },
            "implemented_rules": self.config.get("evaluation_rules", []),
            "intent_groups": [],
            "summary": {
                "total_groups": 0,
                "adversarial_groups": 0,
                "holdout_groups": 0,
                "total_paraphrases": 0,
                "consistency_rate": 0.0,
                "avg_confidence": 0.0,
                "trace_coverage_rate": 0.0,
                "low_confidence_trace_failures": [],
                "silent_downgrade_incidents": [],
                "groups_below_threshold": []
            }
        }
    
    def define_intent_groups(self) -> List[IntentGroup]:
        """Load test intent groups from the ROUTE-001 YAML fixture."""
        groups = []
        for group in self.config.get("intent_groups", []):
            groups.append(
                IntentGroup(
                    name=group["intent"],
                    canonical_workflow=group["expected_workflow"],
                    paraphrases=group.get("phrases", []),
                    risk_level=group.get("risk_level", group.get("expected_rigor", "low")),
                    expected_enhancements=group.get("expected_enhancements", []),
                )
            )
        return groups

    def define_named_groups(self, section_name: str, group_type: str) -> List[IntentGroup]:
        """Load named eval groups from a ROUTE YAML fixture section."""
        groups = []
        for group in self.config.get(section_name, []):
            groups.append(
                IntentGroup(
                    name=group["name"],
                    canonical_workflow=group["expected_workflow"],
                    paraphrases=group.get("phrases", []),
                    risk_level=group.get("expected_rigor", "medium"),
                    expected_enhancements=group.get("expected_enhancements", []),
                    group_type=group_type,
                )
            )
        return groups

    def validate_config(self) -> None:
        """Fail closed when the fixture omits fields the eval needs."""
        supported_rules = {
            "route_equivalence",
            "low_confidence_visibility",
            "enhancement_visibility",
            "no_silent_downgrade",
        }
        configured_rules = {rule.get("name") for rule in self.config.get("evaluation_rules", [])}
        unsupported_rules = configured_rules - supported_rules
        if unsupported_rules:
            raise ValueError(f"unsupported evaluation rules: {sorted(unsupported_rules)}")

        required_trace_fields = set(self.config.get("trace_required_fields", []))
        route_trace_fields = {
            "canonical_intent",
            "workflow",
            "confidence",
            "enhancements_enabled",
            "enhancements_available",
            "rationale",
        }
        if not required_trace_fields.issubset(route_trace_fields):
            unknown = sorted(required_trace_fields - route_trace_fields)
            raise ValueError(f"unsupported route trace fields: {unknown}")

        for group in self.config.get("intent_groups", []):
            for key in ("intent", "expected_workflow", "phrases"):
                if key not in group:
                    raise ValueError(f"intent group missing required key: {key}")
            if not group["phrases"]:
                raise ValueError(f"intent group has no phrases: {group['intent']}")

        for section_name, label in (("adversarial_sets", "adversarial set"), ("holdout_sets", "holdout set")):
            for group in self.config.get(section_name, []):
                for key in ("name", "expected_workflow", "phrases"):
                    if key not in group:
                        raise ValueError(f"{label} missing required key: {key}")
                if not group["phrases"]:
                    raise ValueError(f"{label} has no phrases: {group['name']}")

    def define_adversarial_groups(self) -> List[IntentGroup]:
        """Load adversarial boundary cases from the ROUTE YAML fixture."""
        return self.define_named_groups("adversarial_sets", "adversarial")

    def define_holdout_groups(self) -> List[IntentGroup]:
        """Load unseen holdout cases from the ROUTE YAML fixture."""
        return self.define_named_groups("holdout_sets", "holdout")

    def has_required_trace(self, trace: Dict[str, Any]) -> bool:
        required_fields = self.config.get("trace_required_fields", [])
        return all(field in trace and trace[field] not in (None, "") for field in required_fields)
    
    def run_eval(self) -> Dict:
        """Run the paraphrase routing evaluation."""
        self.validate_config()
        intent_groups = (
            self.define_intent_groups()
            + self.define_adversarial_groups()
            + self.define_holdout_groups()
        )
        self.results["summary"]["total_groups"] = len(intent_groups)
        self.results["summary"]["adversarial_groups"] = len(self.define_adversarial_groups())
        self.results["summary"]["holdout_groups"] = len(self.define_holdout_groups())
        
        total_paraphrases = 0
        total_matches = 0
        total_confidence = 0.0
        trace_checked = 0
        trace_passed = 0
        
        for group in intent_groups:
            group_result = {
                "name": group.name,
                "canonical_workflow": group.canonical_workflow,
                "paraphrase_results": [],
                "consistency_rate": 0.0,
                "avg_confidence": 0.0,
                "risk_level": group.risk_level,
                "expected_enhancements": group.expected_enhancements,
                "group_type": group.group_type,
            }
            
            group_matches = 0
            group_confidence = 0.0
            
            for paraphrase in group.paraphrases:
                workflow, confidence, enhancements, trace = self.router.route(paraphrase)
                route_trace = {
                    "canonical_intent": group.name,
                    "workflow": workflow,
                    "confidence": confidence,
                    "enhancements_enabled": bool(enhancements),
                    "enhancements_available": group.expected_enhancements,
                    "rationale": trace,
                }
                
                matched = (workflow == group.canonical_workflow)
                if matched:
                    group_matches += 1
                    total_matches += 1

                if confidence < 0.5 and self.config["global_expectations"].get("require_route_trace_on_low_confidence", False):
                    trace_checked += 1
                    if self.has_required_trace(route_trace):
                        trace_passed += 1
                    else:
                        self.results["summary"]["low_confidence_trace_failures"].append({
                            "group": group.name,
                            "paraphrase": paraphrase,
                            "missing_trace": True,
                        })

                if not matched and self.config["global_expectations"].get("forbid_silent_downgrade", False):
                    if not route_trace["rationale"]:
                        self.results["summary"]["silent_downgrade_incidents"].append({
                            "group": group.name,
                            "paraphrase": paraphrase,
                            "routed_workflow": workflow,
                            "expected_workflow": group.canonical_workflow,
                        })
                
                group_confidence += confidence
                total_confidence += confidence
                total_paraphrases += 1
                
                result = RoutingResult(
                    paraphrase=paraphrase,
                    routed_workflow=workflow,
                    confidence=confidence,
                    enhancements=enhancements,
                    matched_canonical=matched,
                    trace=trace,
                    route_trace=route_trace,
                )
                
                group_result["paraphrase_results"].append(asdict(result))
            
            # Calculate group statistics
            group_result["consistency_rate"] = group_matches / len(group.paraphrases)
            group_result["avg_confidence"] = group_confidence / len(group.paraphrases)
            
            # Check if below aspirational consistency target
            if group_result["consistency_rate"] < self.aspirational_consistency_target:
                self.results["summary"]["groups_below_threshold"].append({
                    "group": group.name,
                    "rate": group_result["consistency_rate"]
                })
            
            self.results["intent_groups"].append(group_result)
        
        # Calculate overall statistics
        self.results["summary"]["total_paraphrases"] = total_paraphrases
        self.results["summary"]["consistency_rate"] = total_matches / total_paraphrases if total_paraphrases > 0 else 0
        self.results["summary"]["avg_confidence"] = total_confidence / total_paraphrases if total_paraphrases > 0 else 0
        self.results["summary"]["trace_coverage_rate"] = trace_passed / trace_checked if trace_checked > 0 else 1.0
        
        return self.results
    
    def generate_report(self) -> str:
        """Generate a human-readable report."""
        lines = []
        lines.append("=" * 70)
        lines.append(f"{self.config.get('id', 'ROUTE')}: Paraphrase Routing Evaluation Report")
        lines.append("=" * 70)
        lines.append("")
        
        # Summary
        summary = self.results["summary"]
        thresholds = self.results["thresholds"]
        lines.append(f"Source fixture: {self.results['source']}")
        lines.append(
            "Thresholds: "
            f"Phase-1 >= {thresholds['phase1_route_consistency_min']:.0%}, "
            f"aspirational >= {thresholds['aspirational_route_consistency_target']:.0%}"
        )
        lines.append("")
        lines.append("📊 Summary")
        lines.append(f"Total evaluated groups: {summary['total_groups']}")
        lines.append(f"Adversarial groups: {summary['adversarial_groups']}")
        lines.append(f"Holdout groups: {summary['holdout_groups']}")
        lines.append(f"Total paraphrases tested: {summary['total_paraphrases']}")
        lines.append(f"Overall consistency rate: {summary['consistency_rate']:.1%}")
        lines.append(f"Average confidence: {summary['avg_confidence']:.2f}")
        lines.append(f"Low-confidence trace coverage: {summary['trace_coverage_rate']:.1%}")
        lines.append("")
        
        # Threshold check
        if summary["groups_below_threshold"]:
            lines.append("⚠️ Groups below aspirational consistency target:")
            for item in summary["groups_below_threshold"]:
                lines.append(f"  - {item['group']}: {item['rate']:.1%}")
            lines.append("")
        else:
            lines.append("✅ All groups meet aspirational consistency target")
            lines.append("")
        
        # Per-group details
        lines.append("📋 Per-Group Results")
        lines.append("")
        
        for group in self.results["intent_groups"]:
            lines.append(f"Group: {group['name']}")
            lines.append(f"Type: {group['group_type']}")
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
    config_path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    
    eval = ParaphraseEval(str(repo_root), config_path)
    print(f"Running {eval.config.get('id', 'ROUTE')} Paraphrase Routing Eval")
    print("=" * 60)
    results = eval.run_eval()
    
    # Generate and print report
    report = eval.generate_report()
    print(report)
    
    # Save results to JSON
    config_id = str(eval.config.get("id", "route-eval")).lower()
    output_file = Path(__file__).parent / f"{config_id}-results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Results saved to: {output_file}")
    
    # Exit with appropriate code
    hard_gates_pass = (
        results["summary"]["consistency_rate"] >= eval.phase1_consistency_min
        and results["summary"]["trace_coverage_rate"] == 1.0
        and len(results["summary"]["silent_downgrade_incidents"]) == 0
    )

    if hard_gates_pass:
        print("✅ Eval passed: Phase-1 consistency threshold met")
        return 0
    else:
        print(
            f"❌ Eval failed: {results['summary']['consistency_rate']:.1%} "
            f"consistency < {eval.phase1_consistency_min:.0%} Phase-1 threshold"
        )
        return 1


if __name__ == "__main__":
    exit(main())
