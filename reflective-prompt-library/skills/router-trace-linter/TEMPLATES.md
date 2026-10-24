# `router-trace-linter` Templates

Portable sibling to `SKILL.md` in this directory; this file carries the moved scaffold section byte-for-byte, not a second copy. Read `SKILL.md` for the Module Contract, Verification, Honest Limits, Examples and provenance; those rules govern the body here. Emit the template below verbatim; re-copy from this file rather than patching a drifted copy.

## Template: lint_route_trace.py (Python, stdlib only)

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
