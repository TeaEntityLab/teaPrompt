# P15 Frozen-Core Parity Review — 2026-07-11

> **Status: decision record (user-approved execution, 2026-07-11).** Escalated
> review of the two P15 parity items deferred by the
> [flow-coverage panel](flow-coverage-panel-record-2026-07-11.md) (RFM-05),
> fulfilling T1 of the [whole-project plan](whole-project-plan-2026-07-11.md)
> open-work register. Scope is exactly the two named items; no core-skill edit
> was made, so the frozen-surface gate (human approval for `skills/` core edits)
> did not fire.

## Item 1 — `reflective-research` Blind Spots parity with `05-domain/research.md`

### Evidence

- Owning decision: [STORM perspective-discovery reflection](storm-perspective-discovery-reflection-2026-06-18.md)
  §Decision — the sufficiency gate "names the competing perspectives and the
  blind spot **(or states none were found)** — making the mechanism auditable
  and falsifiable."
- `skills/reflective-research/SKILL.md` Sufficiency Gate implements that
  contract verbatim: "names the competing perspectives and the blind spot — or
  states explicitly that none were found." Conformant; expansion stays optional
  for narrow, well-formed questions (also per the STORM record's rejected
  alternative "mandatory perspective expansion").
- `05-domain/research.md` Acceptance Criteria read: "Blind-spot output names at
  least one gap no competing view touched." — **no none-found path**. Stricter
  than the decided contract; on a gap-free scope it forces a fabricated gap,
  which contradicts the project's evidence-honesty principle (missing evidence
  is `unknown`/none-found, never invented).

### Divergence and decision

The divergence is one-sided: the skill matches the STORM decision; the domain
prompt's acceptance criterion overshoots it. The template-vs-workflow layering
difference (research.md keeps Blind Spots as a fixed report section; the skill
makes expansion conditional) is intentional and unchanged — a report template
that asks for the section is fine as long as an honest "none found" satisfies
it.

**Decision: change (prompt-layer).** `research.md` acceptance criterion gains
the none-found clause mirroring the skill's gate, and template item 9 states
the same allowance so template users see it. No edit to
`skills/reflective-research/SKILL.md` (already conformant) — frozen-surface
gate not fired.

## Item 2 — Historical-banner forward pointers in June plans

### Evidence

- [Governance rethink E3](governance-rules-rethink-review-2026-07-11.md)
  applied one uniform historical banner to eleven retired/superseded records:
  it forward-points only at the generic `PROJECT_KNOWLEDGE.md` Decision Index.
- Four of the eleven are the retired whole-project-era **plans**
  (`prompt-library-build-plan.md`, `agent-workflows-plan.md`,
  `code-followups-plan.md`, `runtime-governance-learning-plan-2026-06-11.md`),
  which have a named successor: the
  [whole-project plan](whole-project-plan-2026-07-11.md) (open-work register)
  plus [roadmap](whole-project-roadmap-2026-07-11.md) (scheduling), per the
  plan's own §Why.
- The remaining seven are **reflections/records** with no single successor
  artifact; their decisions live in the Decision Index, which the banner
  already names.

### Decision

**Change (plans-layer) for the four retired plans:** append an open-work
successor pointer to each banner so a reader landing on a retired plan finds
the live register in one hop. **No-change for the seven reflections:** the
Decision Index is their correct forward pointer; per-record successor links
would fabricate a succession relationship that does not exist.

## Candidate Adoption Ledger

| Item | Decision | Surface | Guard / evidence |
| --- | --- | --- | --- |
| P15a acceptance-criterion parity | **Adopted 2026-07-11** | `05-domain/research.md` (Acceptance Criteria + template item 9) | STORM record §Decision quoted above; domain contract/eval-harness/cross-link tests green post-edit |
| P15a skill side | **No-change** | `skills/reflective-research/SKILL.md` | Already conformant; frozen-surface gate not fired |
| P15b successor pointers | **Adopted 2026-07-11** | Banner blockquotes of the four retired plans | `validate_links.py` validates the new links; `make all` green |
| P15b reflection banners | **No-change** | seven reflection records | No single successor exists; generic Decision Index pointer stands |

## Falsifiability

- Wrong if the STORM record's Decision did not contain the none-found clause
  (it is quoted verbatim above), or if a consumer test pinned the old
  research.md acceptance wording (none did — checked `plans/tests/` before the
  edit).
- Stale if `research.md` or the skill's blind-spot wording changes without
  updating the parity claim here.
- The no-change halves are wrong if a reader demonstrably cannot navigate from
  a retired reflection to its owning decision via the Decision Index, or if a
  future record names a single successor for any of the seven reflections.
