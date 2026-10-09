---
name: router-trace-linter
description: Use when a router emits a route trace and you need to check it against the Router Output Contract before accepting the route — required fields present, confidence parseable, downgrade/defer claims carrying explicit rationale (R5), and high-risk routes carrying Human Review (R4/R7). Outputs pass/fail plus a field-level diff.
license: MIT
compatibility: Requires router route-trace artifacts conforming to the Router Output Contract; checks declaration completeness (fields, parseable confidence, downgrade rationale, high-risk Human Review) — cannot judge whether a deferral was justified.
metadata:
  risk_level: low
  human_review_required: false
  external_io: false
  context_load: low
---

# Router Trace Linter

**Type:** Domain-pack skill (verification artifact) — registered in the TeaPrompt source repo's domain-pack registry (`plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS`), not one of the nine frozen core workflow skills, and not selected by `reflective-dispatch` route rows; the host harness may invoke it directly.

## Purpose

Give hosts and reviewers a small deterministic checker that lints a router's emitted route trace against the Router Output Contract, so silent downgrades and missing rationale are caught as lint failures instead of shipped as accepted routes. Evidence: `reflective-prompt-library/plans/ROUTING_CONTRACT.md` §Router Output Contract (ten-field trace shape) with R5 route observability (downgrade/escalation rationale required) and R7 context-load deferral (deferred skills listed under available enhancements with rationale); machine-readable precedent in `plans/route-001-paraphrase-eval.yaml` `trace_required_fields` and `plans/validate_route_fixture.py` `REQUIRED_TRACE_FIELDS`.

## Module Contract

### Trigger

- A router (model, template, or host harness) has emitted a route trace and someone must decide whether to accept the route, release the work, or record the routing run.
- A review, eval sweep, or preflight-style gate needs a pass/fail verdict on trace completeness rather than a judgment on whether the chosen workflow was semantically right.

### Inputs

- One route trace as markdown text, YAML block, or key/value lines (the ten contract fields, in any order/casing). Machine `trace_required_fields` form (`canonical_intent, workflow, confidence, enhancements_enabled, enhancements_available, rationale`) is accepted as an alias subset — absent `Mode`, `Strictness`, and `Next Action` are warnings, not failures, in alias mode. `Human Review` is a warning only when no high-risk signal fired.
- Optional: the pre-route request text (one paragraph), used only to detect claimed-but-unexplained downgrades (e.g. request names tests, trace defers them silently). Never required; absence never fails the lint.

### Methods

**Value normalization:** before any check, field values are stripped of supported quoting/markdown wrapping (`"none"`, `'medium'`, `**none**` all read as their inner token). `false` and `not applicable` (space or hyphen spelling) read as empty alongside `none`/`n/a`/`na`/`tbd`. **Multiline scalars:** a YAML block-scalar header `>` or `|` on a field line is supported — indented continuation lines fold to spaces (`>`) or keep line breaks (`|`) before all checks. Other scalar indicators/decorators (`?`, `!`, `|+`, `>-`, `&`, `*`, flow `[]`/`{}`) are unsupported: the field must be reported `unparseable (unsupported scalar form)` rather than read as the header character, so the representation can never hide field content.

1. **Field-presence check:** normalize trace keys (case/whitespace/punctuation-insensitive: `Route Confidence` ≡ `confidence`, `Enhancements Available` ≡ `enhancements_available`) and require all ten contract fields — `Mode`, `Strictness`, `Goal`, `Assumptions`, `Workflow`, `Route Confidence`, `Enhancements Enabled`, `Enhancements Available`, `Human Review`, `Next Action`. Missing or blank field = fail with per-field row. **Alias mode** is the machine six-field form (`canonical_intent`, `workflow`, `confidence`, `enhancements_enabled`, `enhancements_available`, `rationale`) when the ten display names are absent. Map `canonical_intent`→`Goal`, `workflow`→`Workflow`, `confidence`→`Route Confidence`, `enhancements_enabled`→`Enhancements Enabled`, `enhancements_available`→`Enhancements Available`, and `rationale`→the rationale seat (it also fills `Assumptions` when that field is absent). Absent `Mode`, `Strictness`, and `Next Action` are warnings, not failures. Absent `Human Review` is a warning unless a high-risk signal fired, in which case R4 still fails.
2. **Confidence-parse check:** strip supported quoting/markdown wrapping, then accept exactly `high | medium | low` (case-insensitive) or a numeric `0..1` float; anything else (blank, `maybe`, `confident`, `80%`, prose sentence) = fail. Rationale: TeaPrompt's standing rule is "evidence over confidence" — the linter checks the value is well-formed and therefore comparable, never that it is calibrated.
3. **Downgrade/defer-rationale check (R5/R7):** when the trace signals reduced rigor, require explicit rationale text (≥1 non-placeholder sentence, >20 characters, not a placeholder such as `n/a`/`none`/`false`/`tbd` in any supported spelling/wrapping). Signals are field-scoped: `Enhancements Available` non-empty (a deferred skill exists); `Workflow` naming `prompt-only` or Fast Path where a workflow was in scope; or a deferral keyword (`downgrade|defer|fallback|default-up|instead of|skipped`) inside `Goal`/`Assumptions`/`Workflow`/enhancement/rationale fields. `Human Review` and `Next Action` never signal deferral: a low-risk `Human Review: skipped` is review status, not a reduced-rigor claim. Rationale may live in `Assumptions`, a `Rationale`/`Reason` line, or in `Enhancements Available` itself when that field is a non-placeholder sentence longer than 20 characters — the linter reports which seat it used. The named must-pass fixture is allowed to keep a short `Assumptions` value; the deferral sentence in `Enhancements Available` is enough.
4. **High-risk-review check (R4):** when the trace signals high risk or irreversible impact — `Workflow` contains `reflective-risk` (case-insensitive), `Strictness` is `L4`/`L5`, or an action-scoped `Goal`/`Assumptions` match on `production|auth|billing|credential|secret|permission|privacy|pii|delet|destruct|irreversib|third-part` with intentional token boundaries — require `Human Review` to be present, non-blank, and not a placeholder/negation (`none`, `false`, `not required`, `not applicable`, `n/a`, `tbd`, markdown-bold or quoted equivalents). Boundaries are intentional: bare `auth`, `authentication`, and `authorize`/`authorise` (plus suffix forms) match, but `author`/`authors`/`authorship`/`coauthor` never do; `-`, `_`, digits, and `-service`-style continuations still attach to `auth`. A negation denies only the hazard it actually modifies: `no auth, billing, or production surface` denies the whole coordinated list, but `No auth changes, deploy to production` still signals because the later action (`deploy`) re-opens the scope. Likewise `Human Review: not required` is a valid low-risk answer only when no action-scoped signal fired; it remains a failure when a real signal did fire. The risk scan covers `Goal`/`Assumptions` only — widening it to `Next Action` was reviewed and declined; a hazard missed there is a stated limit, not a pass endorsement.
5. **Diff output:** emit one row per field (`ok | missing | unparseable | rationale-missing | review-missing`) plus the offending raw line or `<absent>`, so a reviewer can fix the trace without re-reading the contract.

### Output

- Single verdict `pass` or `fail`, followed by the field-level diff table (10 rows, one per contract field) and a one-line reason per failing row naming the rule (R5/R7/R4/presence/parse).
- No routing judgment: the linter never says which workflow *should* have been chosen — only whether the emitted trace satisfies the contract.

### Never

- Never pass a trace with a blank `Route Confidence` or a missing downgrade rationale (the two named must-fail fixtures regress if this happens).
- Never fail a trace that fills all ten fields with well-formed values (the named must-pass fixture regresses if this happens).
- Never state which workflow *should* have been chosen — report only whether the emitted trace satisfies the contract.
- Never present a `pass` as evidence the rationale is true, the confidence is calibrated, or the workflow choice was right: a coherent invented rationale passes the syntax check.
- Never treat a high-risk-keyword miss as a route approval — the underlying R4 duty still binds the router when the heuristic list misses.
- Never fail alias-mode (machine six-field) traces on absent `Mode`, `Strictness`, or `Next Action` — warnings only. Still fail that form when confidence is unparseable, a deferral has no rationale sentence, or a high-risk signal has no `Human Review`. A gate that needs strictness recorded must require the full ten-field form.
- Never invent rationale, confidence, or review text to turn a fail into a pass — return the diff to the router author for a one-line fix.
- Never adjudicate whether the route was semantically correct or whether the work should exist — escalate instead (see Escalation).

### Escalation

- Failing trace on low-risk work → return the diff to the router author for a one-line fix (usually add rationale or fill a blank field); do not escalate the task itself.
- Failing trace on high-risk work, or a second consecutive fail → route the underlying task through `reflective-risk` before execution; the lint failure is evidence, not a release.
- Dispute about whether the route was semantically correct → `reflective-review` of the artifact; dispute about whether the work should exist → `reflective-minimality`. The linter does not resolve either.

### Failure signals

- Linter passes a trace with a blank `Route Confidence` or a missing downgrade rationale (the two named must-fail fixtures regress).
- Linter fails a complete trace (the named must-pass fixture regresses).
- Two reviewers disagree on whether a verdict was correct given the same trace text (rule ambiguity — fix the rule wording, not the trace).

### Verification

Eight self-contained fixtures, runnable without network or model calls —

1. `complete-trace` (must pass): all ten fields filled, `Route Confidence: medium`, `Enhancements Available: security review after bounded patch (deferred: L2 scope, no auth surface)` — verdict `pass`, zero failing rows.
2. `missing-rationale-downgrade` (must fail): `Enhancements Available: performance review` with `Assumptions` blank and no rationale sentence — verdict `fail`, row `Enhancements Available: rationale-missing (R5/R7)`.
3. `missing-confidence` (must fail): `Route Confidence:` blank — verdict `fail`, row `Route Confidence: unparseable (presence/parse)`. Optional fourth fixture: high-risk route (`Strictness: L4`, production deploy) with `Human Review: none` → `fail`, row `Human Review: review-missing (R4)`.
4. `alias-six-field` (must pass with warnings): only the six machine keys, low-risk wording, a rationale sentence, no un-negated hazard keyword — verdict `pass`, warnings for absent `Mode`, `Strictness`, and `Next Action`. The same trace with `canonical_intent` containing `production` and no `Human Review` — verdict `fail`, row `Human Review: review-missing (R4)`.
5. `r4-contrastive-matrix` (behavioral regressions): the low-risk control trace with substituted `Goal`/`Workflow`/`Human Review` fields — every high-risk bypass denies (`No auth changes, deploy to production` + `not required`; `deploy to production` + `false` / `not applicable` / `tbd` / `**none**` / `"none"`; capitalized `Reflective-Risk` workflow on low-risk wording), while the ordinary low-risk control (`rename a local variable` + `not required`) and production + `none`/`skipped` denials keep their existing verdicts.
6. `quoted-confidence` (must pass): the low-risk control trace with `Route Confidence: "medium"` (also `'medium'`, `**medium**`, `"high"`, `"low"`, `"0.8"`) — verdict `pass`; genuinely unparseable values (`maybe`, `confident`, `80%`, prose) still fail.
7. `folded-scalar-parity` (representation check): `Goal: >` with an indented continuation such as `deploy to production` carries the same review obligation as the inline form (verdict `fail`, `Human Review: review-missing (R4)`); the same folded Goal on low-risk wording passes. A field whose value is only `?`/`!`/other unsupported scalar syntax fails `unparseable (unsupported scalar form)` rather than pretending the header is content.
8. `low-risk-form-parity` (F11 regressions): `credit the original author in the changelog` never fires R4; a six-field alias trace whose `rationale` is short but complete (`copy change only`) passes with warnings and fills `Assumptions`; `Assumptions` carrying a meaningful sentence is a valid rationale seat without deferral keywords; a low-risk `Human Review: skipped` with no deferred enhancement passes.

## Emitted Scaffold

`lint_route_trace.py` (Python stdlib only; host-executed). It implements the verification fixtures plus the RV-04/RV-09 contrastive matrix: supported `>`/`|` block-scalar parsing with explicit refusal of unsupported scalar syntax, intentional hazard token boundaries (`author` never matches; `auth`, `authentication`, `authorize`, `auth-service` still do), field-scoped deferral detection (Human Review/`Next Action` never signal deferral), action-scoped negation, normalized quoting/markdown/placeholder review values, case-insensitive workflow gating, and quoted confidence. A negation denies only the hazard it actually modifies. Normalized `none`/`false`/`not applicable`/`tbd` (including markdown-bold and quoted forms) is a filled value for enhancements and a negated Human Review only when a high-risk signal fired.

```python
#!/usr/bin/env python3
"""Lint one route trace against the Router Output Contract. Stdlib only."""
import re, sys

FIELDS = [
    "Mode", "Strictness", "Goal", "Assumptions", "Workflow", "Route Confidence",
    "Enhancements Enabled", "Enhancements Available", "Human Review", "Next Action",
]
# Intentional token boundaries: "auth" still attaches to non-letter
# continuations (auth-service, auth2, auth_) and to full hazard words
# (authentication, authorize, authorise), but never to the author family
# (author/authors/authorship/authored/authoring/authorial/authority).
HAZARD = re.compile(
    r"auth(?!or(?:e[ds]|ing|s|ship|ial|ity|itative|itarian)?\b)|production|billing|credential|secret|permission|privacy|pii|delet|destruct|irreversib|third-part",
    re.I,
)
NEG = re.compile(r"\b(?:no|not|without)\b", re.I)
DEFER = re.compile(r"downgrade|defer|fallback|default-up|instead of|skipped", re.I)
KEY = re.compile(r"^(?P<ind>\s*)(?:[-*]\s*)?(?:\*\*)?(?P<key>[A-Za-z][A-Za-z0-9 /_-]*?)(?:\*\*)?\s*:\s*(?P<val>.*)$")
BLOCK = re.compile(r"^[>|]$")
UNSUPPORTED_SCALAR = re.compile(r"^[>|?!&*%@`#\[\]{},:]")
ALIAS = {
    "mode": "mode", "strictness": "strictness", "goal": "goal",
    "assumptions": "assumptions", "workflow": "workflow",
    "routeconfidence": "confidence", "confidence": "confidence",
    "enhancementsenabled": "enabled", "enhancementsavailable": "available",
    "humanreview": "review", "nextaction": "next",
    "canonicalintent": "intent", "rationale": "rationale", "reason": "rationale",
}
EMPTY = {"", "none", "n/a", "na", "tbd", "false", "not applicable", "not-applicable", "notapplicable"}
ACTION = re.compile(
    r"\b(?:deploy|rotate|release|migrate|push|publish|delete|remove|change|update|modify|edit|fix|patch|charge|bill|store|share|expose|send|grant|revoke|run|execute|apply|perform)\b",
    re.I,
)

def norm(key):
    return re.sub(r"[^a-z0-9]", "", key.lower())

def block_scalar(raw_lines, start, base_indent):
    """Collect indented continuation lines after a > or | header."""
    parts = []
    i = start
    while i < len(raw_lines):
        line = raw_lines[i]
        if not line.strip():
            parts.append("")
            i += 1
            continue
        if len(line) - len(line.lstrip()) <= base_indent:
            break
        parts.append(line.strip())
        i += 1
    return parts, i

def join_block(kind, parts):
    body = list(parts)
    while body and body[-1] == "":
        body.pop()
    if kind == "|":
        return "\n".join(body).strip()
    # folded: blank lines mark paragraph breaks; other lines join by space
    text, pending_blanks = [], 0
    for p in body:
        if p == "":
            pending_blanks += 1
            continue
        text.append("\n\n" if pending_blanks else (" " if text else ""))
        text.append(p)
        pending_blanks = 0
    return "".join(text).strip()

def parse(text):
    found, lines, unsupported = {}, {}, set()
    raw = text.splitlines()
    i = 0
    while i < len(raw):
        line = raw[i]
        i += 1
        m = KEY.match(line)
        if not m:
            continue
        slot = ALIAS.get(norm(m.group("key")))
        if not slot or slot in found:
            continue
        value = m.group("val").strip()
        lines[slot] = line.strip()
        if BLOCK.match(value):
            parts, i = block_scalar(raw, i, len(m.group("ind")))
            found[slot] = join_block(value, parts)
        elif UNSUPPORTED_SCALAR.match(value) and not (
            len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'`"
        ) and not value.startswith("**"):
            unsupported.add(slot)
            found[slot] = value
        else:
            found[slot] = value
    return found, lines, unsupported

def clean(value):
    text = (value or "").strip()
    for _ in range(2):
        if len(text) >= 4 and text.startswith("**") and text.endswith("**"):
            text = text[2:-2].strip()
        elif len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'`":
            text = text[1:-1].strip()
        else:
            break
    return text

def blank(value):
    return value is None or clean(value) == ""

def normalized(value):
    return re.sub(r"[\s_-]+", " ", clean(value).lower()).strip()

def placeholder(value):
    return blank(value) or normalized(value) in EMPTY

def sentence(value):
    if placeholder(value):
        return False
    return len(clean(value)) > 20

def hazard(text):
    for clause in re.split(r"[.;\n]", text or ""):
        for m in HAZARD.finditer(clause):
            if clause[:m.start()].endswith("non-"):
                continue  # directly prefixed (e.g. non-destructive, non-production)
            before = clause[:m.start()]
            neg = None
            for nm in NEG.finditer(before):
                neg = nm  # nearest preceding negation word wins
            if neg is None:
                return True
            between = before[neg.end():]
            # A negation denies only the hazard it actually modifies. A new
            # action verb between the negation and the keyword ("No auth
            # changes, deploy to production") ends the negation's scope, so
            # the keyword is a fresh claim. Otherwise the denial stands on
            # its own comma segment ("without credentials or billing") or as
            # a coordinated list ("no auth, billing, or production"); a bare
            # comma ends the scope.
            if ACTION.search(between):
                return True
            seg_start = before.rfind(",") + 1
            if NEG.search(before[seg_start:]):
                continue  # same comma-segment negation ("without credentials or billing")
            if seg_start and NEG.search(before[:seg_start]):
                # comma item of an earlier negation: a real list only when the
                # chain is completed by an or/and item ("no auth, billing, or
                # production"); a bare comma ends the negation's scope
                seg_rest = clause[seg_start:]
                if re.match(r"\s*(?:or|and)\b", seg_rest) or re.search(
                    r",\s*(?:or|and)\b", seg_rest
                ):
                    continue
            return True
    return False

def review_negated(value):
    text = normalized(value)
    if text in EMPTY or text in {"no", "not required", "not needed", "not necessary"}:
        return True
    return bool(re.match(
        r"(none|n/a|na|tbd|false|not applicable|no|not required|not needed|not necessary|waived|skipped)\b",
        text,
    ))

def source_line(lines, *slots):
    for slot in slots:
        if slot in lines:
            return lines[slot]
    return "<absent>"

FIELD_SLOTS = {
    "Mode": ("mode",),
    "Strictness": ("strictness",),
    "Goal": ("goal", "intent"),
    "Assumptions": ("assumptions", "rationale"),
    "Workflow": ("workflow",),
    "Route Confidence": ("confidence",),
    "Enhancements Enabled": ("enabled",),
    "Enhancements Available": ("available",),
    "Human Review": ("review",),
    "Next Action": ("next",),
}

def lint(text):
    raw, lines, unsupported = parse(text)
    alias = "intent" in raw and "mode" not in raw and "goal" not in raw
    goal = raw.get("goal") or raw.get("intent") or ""
    assumptions = raw.get("assumptions") or ""
    rationale = raw.get("rationale") or ""
    if alias and blank(assumptions) and not placeholder(rationale):
        assumptions = rationale
    values = {
        "Mode": raw.get("mode") or "",
        "Strictness": raw.get("strictness") or "",
        "Goal": goal,
        "Assumptions": assumptions,
        "Workflow": raw.get("workflow") or "",
        "Route Confidence": raw.get("confidence") or "",
        "Enhancements Enabled": raw.get("enabled") or "",
        "Enhancements Available": raw.get("available") or "",
        "Human Review": raw.get("review") or "",
        "Next Action": raw.get("next") or "",
    }
    high = (
        "reflective-risk" in values["Workflow"].lower()
        or bool(re.search(r"\bL[45]\b", values["Strictness"], re.I))
        or hazard(values["Goal"]) or hazard(values["Assumptions"])
    )
    # Deferral signals are field-scoped: Human Review status words such as
    # "skipped" and Next Action text never claim reduced rigor.
    defer_fields = [
        values["Goal"], values["Assumptions"], values["Workflow"],
        values["Enhancements Enabled"], values["Enhancements Available"],
        rationale,
    ]
    defer = (
        not placeholder(values["Enhancements Available"])
        or "prompt-only" in values["Workflow"].lower()
        or "fast path" in values["Workflow"].lower()
        or any(DEFER.search(v) for v in defer_fields)
    )
    seat = ""
    if sentence(values["Enhancements Available"]):
        seat = "Enhancements Available"
    elif sentence(rationale):
        seat = "Rationale"
    elif sentence(values["Assumptions"]):
        seat = "Assumptions"
    warn_fields = {"Mode", "Strictness", "Next Action"}
    if not high:
        warn_fields.add("Human Review")
    rows, warnings = [], []
    for field in FIELDS:
        value = values[field]
        status, detail = "ok", ""
        supplied = next((s for s in FIELD_SLOTS[field] if s in lines), None)
        if supplied in unsupported:
            status, detail = "unparseable", "unsupported scalar form"
        elif field == "Route Confidence" and not re.fullmatch(
            r"high|medium|low|0(?:\.\d+)?|1(?:\.0+)?|0?\.\d+", clean(value), re.I
        ):
            status, detail = "unparseable", "presence/parse"
        elif field == "Enhancements Available" and defer and not seat:
            status, detail = "rationale-missing", "R5/R7"
        elif field == "Human Review" and high and (blank(value) or review_negated(value)):
            status, detail = "review-missing", "R4"
        elif blank(value):
            if alias and field in warn_fields:
                status = "warning"
                warnings.append(field)
            else:
                status, detail = "missing", "presence"
        rows.append({
            "field": field,
            "status": status,
            "detail": detail,
            "raw": source_line(lines, *FIELD_SLOTS[field]),
        })
    failing = [r for r in rows if r["status"] not in {"ok", "warning"}]
    return {
        "verdict": "fail" if failing else "pass",
        "rows": rows,
        "warnings": warnings,
        "rationale_seat": seat,
        "alias": alias,
    }

def main(argv):
    text = sys.stdin.read() if len(argv) < 2 else open(argv[1], encoding="utf-8").read()
    result = lint(text)
    print(result["verdict"])
    for row in result["rows"]:
        extra = f" ({row['detail']})" if row["detail"] else ""
        shown = "<absent>" if row["raw"] == "<absent>" else "`" + row["raw"] + "`"
        print(f"{row['field']}: {row['status']}{extra} | {shown}")
    for field in result["warnings"]:
        print(f"warning: {field} absent")
    if result["rationale_seat"]:
        print(f"rationale seat: {result['rationale_seat']}")
    return 0 if result["verdict"] == "pass" else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

## Honest Limits

- Syntax, not semantics: the linter proves the trace *says* something well-formed, not that the rationale is true or the workflow choice is right. A coherent invented rationale passes.
- Scalar support is bounded, stdlib-only: `>` and `|` block scalars fold into the field value before checks; other scalar indicators (`?`, `!`, `>-`, `|+`, anchors, flow collections) are refused as `unparseable (unsupported scalar form)` rather than silently read or dropped — this is a refusal, not a YAML guarantee.
- Confidence is uncalibrated by design: `high` from a chat model is self-report with no calibration evidence. The linter checks comparability only.
- High-risk keyword list is heuristic English-first (`production|auth|billing|…`); non-English or novel hazard phrasing can miss the review check. Misses are linter gaps, not route approvals — the underlying R4 duty still binds the router.
- Alias mode (machine six-field form) warns instead of failing on absent `Mode`, `Strictness`, and `Next Action`. It still fails closed on a bad confidence value, a deferral without a rationale sentence, or a high-risk signal with no `Human Review`. A gate that needs strictness recorded should require the full ten-field form.
- Recurrence evidence is still thin: at registration the linter had zero observed misroute catches. Record real failing traces caught pre-release, plus a no-false-positive run over the existing `reflective-dispatch.examples.md` traces, before treating early passes as established practice.

## Examples

Companion examples live at `<skills-root>/examples/router-trace-linter.examples.md` when co-installed. They show pass/fail verdict shapes and field-level diff rows, not a judgment that any route was semantically correct.

## Prompt Sources

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill is self-contained.*

- `reflective-prompt-library/plans/ROUTING_CONTRACT.md` (§Router Output Contract ten-field shape; R4/R5/R7 duties)
- `reflective-prompt-library/plans/route-001-paraphrase-eval.yaml` (`trace_required_fields` + eval rules `low_confidence_visibility`, `enhancement_visibility`, `no_silent_downgrade`)
- `reflective-prompt-library/plans/validate_route_fixture.py` (`REQUIRED_TRACE_FIELDS`, `REQUIRED_EVAL_RULES`)
- `reflective-prompt-library/skills/examples/reflective-dispatch.examples.md` (confidence vocabulary as emitted; no-false-positive corpus)
