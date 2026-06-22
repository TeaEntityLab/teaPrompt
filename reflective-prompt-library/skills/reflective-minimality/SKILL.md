---
name: reflective-minimality
description: Use this as a Minimality Gate or anti-bloat review before implementation, during refactoring, or when an agent may overbuild. It challenges whether code should exist, prefers deletion, standard library, platform-native features, existing dependencies, one-line or one-file solutions, and requires intentional shortcuts to carry explicit ceiling and upgrade triggers.
license: MIT
risk_level: low
human_review_required: false
external_io: false
---

# Reflective Minimality

**Type:** Prompt-level workflow

## Purpose

Prevent unnecessary code, abstractions, dependencies, files, and prose while preserving explicit requirements and safety-critical behavior.

It is inspired by the Ponytail-style "lazy senior developer" pattern, but in this library it is a narrow gate: it does not replace spec, risk, implementation, or review workflows.

## Module Contract

Trigger:

- The task risks overengineering, speculative abstraction, dependency sprawl, wrapper layers, or scaffolding "for later."
- The user asks for minimality, YAGNI, anti-bloat, "do less," "can this be deleted," "avoid overengineering," or a Ponytail-like pass.
- A proposed change introduces a new dependency, new framework, new interface, new factory, new config surface, or multiple files for a small requirement.
- A code review needs complexity-only findings before or alongside correctness review.
- A repo-wide complexity audit or intentional shortcut/debt ledger is requested.

Methods:

- Existence challenge: ask whether the thing needs to exist at all.
- Scope reduction: delete, narrow, or defer before adding.
- Capability ladder: prefer standard library, platform-native behavior, existing dependencies, then one-line or one-file solutions before custom code.
- Safety floor: identify behavior that must not be simplified away.
- Debt marker: when intentionally deferring robustness, record a ceiling and an observable upgrade trigger.
- Debt ledger: collect intentional shortcut markers and flag entries without upgrade triggers.
- Complexity audit: scan for one-implementation abstractions, avoidable dependencies, wrapper-only delegation, dead flags, and hand-rolled standard library behavior.
- Runnable check: keep one minimal check for non-trivial logic.

### Output

- Minimality decision: skip, delete, reuse, shrink, or implement minimum.
- Cut list: unnecessary files, abstractions, dependencies, flags, wrappers, or prose.
- Allowed work: the smallest change that still satisfies acceptance criteria.
- Safety floor: validation, security, data-loss, accessibility, compatibility, and explicit requirements that must remain.
- Verification: the smallest runnable check that proves non-trivial logic.
- Debt markers: only when an intentional shortcut has a known ceiling and upgrade trigger.
- Debt ledger: grouped marker list with no-trigger risks when requested.

### Never

- Do not use minimality to avoid explicit acceptance criteria.
- Do not remove trust-boundary validation, auth, privacy, security, data-loss prevention, required accessibility, compatibility constraints, or required tests.
- Do not add a new dependency when standard library, platform-native behavior, existing dependency, or small local code is enough.
- Do not add an abstraction for one implementation, a factory for one product, or config for a value that does not vary.
- Do not mark a shortcut without both a ceiling and an observable upgrade trigger.

### Escalation

- If the goal or acceptance criteria are unclear, route to `reflective-brief` or `reflective-spec-plan`.
- If simplification touches high-risk behavior, route to `reflective-risk`.
- If implementation is required after the gate, route to `reflective-implement`.
- If reviewing an existing diff, combine with `reflective-review` for correctness and test adequacy.

## Minimality Ladder

Stop at the first rung that satisfies the requirement:

1. Does this need to exist?
2. Can the request be deleted, narrowed, or deferred?
3. Does the standard library already solve it?
4. Does the platform or native feature already solve it?
5. Does an installed dependency already solve it?
6. Can the solution be one line or one file?
7. Only then write the minimum code that satisfies the acceptance criteria.

When two options are equally small, choose the one that is more correct on edge cases.

## Safety Floor

Minimal does not mean careless. Never simplify away:

- Trust-boundary validation.
- Error handling that prevents data loss.
- Security, privacy, authentication, and authorization controls.
- Accessibility required by the product or user.
- Hardware, time, locale, or platform calibration that the real environment needs.
- Explicit user requirements.
- One minimal runnable check for non-trivial logic.

## Debt Marker

If a shortcut is intentional and has a known ceiling, record it near the code:

```text
ponytail: ceiling=<known limit>; upgrade_when=<observable trigger>
```

Acceptable markers name both the limit and the trigger. Vague "TODO later" comments are not enough.

## Complexity-Only Review Format

For a diff or file review, use one line per finding:

```text
<file>:L<line>: <delete|stdlib|native|existing-dep|yagni|shrink|debt>: <what to cut>. <replacement>.
```

End with:

```text
net: -N lines, -M deps possible.
```

If there is nothing meaningful to cut:

```text
Lean already. Ship.
```

For a repo-wide audit, rank the largest cuts first and use the same tags.

For a debt ledger, scan intentional shortcut markers and flag any entry that lacks a ceiling or upgrade trigger.

## Prompt Sources

- `01-thinking/counterargument.md`
- `02-engineering/code-reviewer.md`
- `04-agent/runtime-trust-boundary.md`
- `02-engineering/implementation-agent.md`
