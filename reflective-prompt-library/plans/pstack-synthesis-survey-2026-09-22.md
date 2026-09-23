# pstack Deep-Research Synthesis Survey — 2026-09-22

> **Status: decided — record-only; no installed change, no wording adopted.** The
> object is `local://paste-4.md`, a zh-TW research synthesis ("深入研究：pstack、
> Verification Skills 與高信任 AI Agent 工程架構") dated 2026-09-22 — a
> second-order artifact: it surveys pstack *and* proposes an integration
> architecture. Per the standing rule, a pasted synthesis is a claim about its
> sources; this record verifies it against the pinned repo
> (`cursor/plugins` @ `53e579f1481697931fc44f5445171397cfa2b24b`, manifest 0.15.2,
> MIT) and its external citations. Companion to
> `plans/pstack-survey-2026-09-22.md` (the first-order repo survey). Bare survey →
> DS-1: nothing installed. Guard: `plans/tests/test_pstack_synthesis_survey_record.py`.

## Research Question

User instruction: "Survey for pstack further: local://paste-4.md". Three
questions: (1) do the paste's claims about pstack's actual mechanisms check out
at the pin; (2) do its external citations (METR, DORA, OpenAI, GitHub, Cursor
docs) check out; (3) does its proposed governance integration expose a verified
gap on an installed TeaPrompt surface.

## Direct Recommendation (as of 2026-09-22)

- **Study — this is a high-fidelity synthesis.** Unlike paste-3 (which conflated
  mechanisms), this document's repo claims are almost entirely accurate at the
  pin, and its external citations are real and correctly characterized. Its
  central contribution is a *taxonomy correction*: verification, validation,
  independent verification, governance, and runtime assurance are different
  questions, and "verification is all you need" fails when the oracle itself is
  wrong or captured.
- **Verify — repo claims hold with one exception.** "Gardener" appears in the
  paste's §4.1 mapping table as a pstack mechanism but does not exist anywhere
  in the pinned tree (grep over the full extracted tarball: zero hits).
  Resolved 2026-09-23 by user clarification: "gardener" is the *developer's
  role* — the human tending Grok @Bot's output through pstack — not a pstack
  mechanism. The paste's table mislabeled a human-in-loop role as an
  architecture component. Everything
  else checked — the 23 playbooks, shipping's verifier≠author + patch-id
  binding, autopilot-full's operator-grant-plus-root-verdict merge rule, the
  fictional-Atlas example repo, `/why`'s fact/inference source discipline —
  verifies.
- **Adopt — nothing.** Bare survey → DS-1 record-only. The paste's five
  governance controls (Sealed Oracle, Feature-Map drift detection,
  self-confirming-verification prevention, durable execution, prompt-injection
  authority boundary) are all already covered by installed surfaces —
  `governed-delivery`'s oracle manifest + decorrelated verification + evidence
  ledger, `agent-governance-scaffold`'s authority split + effect receipts,
  `runtime-trust-boundary`'s data-not-instructions rule. The genuinely new
  artifact is the **A/B/C controlled-experiment protocol with T01–T10
  falsification scenarios** — recorded below as the evaluation design for the
  still-deferred PS-C1 pilot, not as an adoption.
- **For citers:** the paste is a user-provided synthesis of unknown authorship;
  its repo claims are verified here, its external claims verified against
  primary sources, but its proposed `.agent/` directory layout and YAML schemas
  are the paste author's design, not pstack's. Do not cite them as pstack
  artifacts.

## Method

Coordinator read (2026-09-22), no scouts, no panel: paste-4 in full (1,895
lines); pinned repo re-verified via GitHub API tree + raw file reads
(shipping.md, autopilot-full.md, autopilot-stack.md, reflect/SKILL.md) and a
full extracted-tarball grep for "gardener"; `poteto/verification-skill-example`
README read in full; external claims verified via primary sources (METR blog,
DORA 2025 report, OpenAI research pages).

## Evidence vs Inference

**Verified against the pinned repo:**

- `/poteto-mode` is a workflow router over exactly **23 playbooks** (counted in
  the tree: authoring-a-skill through worktree-cleanup).
- `playbooks/shipping.md`: one verifier subagent per PR that did not write the
  code; verdict bound to head SHA + base SHA + stable `git patch-id`; rebase or
  retarget voids the verdict unless patch-id unchanged; land only the
  contiguous verified run from the bottom; unverified PRs block the chain.
- `playbooks/autopilot-full.md`: owner merges only after "the operator's
  full-autonomy grant plus the root's clean verdict" — the paste's
  authorization claim is accurate, and the doc itself notes this scope is a
  design choice, not a universal default.
- `skills/why/`: investigates git history, PRs, issues, docs, team comms
  (slack/linear/notion/sentry/datadog/incident-postmortem source playbooks) and
  carries `references/epistemics.md` — fact/inference separation confirmed.
- `skills/reflect/SKILL.md`: synthesizer's Accepted list is sanity-checked —
  items better enforced by lint/script/metadata/runtime are moved to Backlog
  (encode-lessons-in-structure). The paste's "禁止直接修改受信任規則" framing is
  consistent.
- `poteto/verification-skill-example` (external repo, no license): README
  confirms Atlas/Harbor Labs/`control-atlas` are fictional and the driver CLI
  is "omitted on purpose" — the paste's warning is accurate.
- **"Gardener": zero hits in the pinned tree.** Not a pstack mechanism —
  resolved 2026-09-23: it names the developer's maintenance role over the
  agent's output (user clarification), which the paste's mapping table
  mislabeled as an architecture-governance mechanism.

**Verified against external primary sources:**

- METR July 2025 RCT: 16 experienced OSS devs, 246 tasks, **19% slower** with
  early-2025 AI tools (CI +2%/+39%); 39-point perception gap. Feb 2026 update:
  the *follow-up* (Aug 2025 cohort) was compromised by selection bias —
  attrition of AI-reliant devs, pay cut, concurrency artifacts — making later
  estimates unreliable. The paste's characterization is accurate.
- DORA 2025: AI as organizational amplifier, not silver bullet; capabilities
  model + seven team profiles. Accurate.
- OpenAI prompt-injection research (hardening Atlas, designing-agents,
  self-generated injections in compaction summaries): prompt injection treated
  as unsolvable at the model layer; deterministic system-level bounds required.
  Accurate.
- GitHub branch protection (required status checks, designated check sources)
  and Cursor cloud-agent security docs (isolated envs, egress limits, secrets,
  human review): exist as described.

**Inference / paste-author opinion (assessed, not adopted):**

- The Verification/Validation/Independent-Verification/Governance/Runtime-
  Assurance taxonomy — sound, and consistent with TeaPrompt's existing split.
- The Prevent/Detect/Contain-Recover three-plane model replacing a linear
  five-layer stack — a defensible reframing; maps onto existing surfaces.
- "Engineer the Environment, Govern the Effects" — the paste's closing
  principle; a good summary of what is already installed.
- The `.agent/` + `policy/` + `features/` + `tools/control-app/` layout and the
  `verify-checkout` YAML contract — paste-author design, reasonable, not
  pstack-native.

## Candidate Adoption Ledger

| ID | Mechanism | TeaPrompt existing coverage | Decision | Trigger and falsifier |
| --- | --- | --- | --- | --- |
| PS2-1 | Verification ≠ Validation ≠ Governance taxonomy | `governed-delivery` oracle manifest + acceptance authority; `reflective-spec-plan` falsifiability | No change — installed | A local failure where a passed oracle answered the wrong question. Falsifier: existing split already forces the distinction |
| PS2-2 | Sealed Oracle: acceptance criteria outside implementer write scope; protected test suite; SHA-bound evidence | `governed-delivery` oracle manifest + evidence ledger; `agent-governance-scaffold` acceptance authority + capability tokens | No change — installed | An implementer rewriting acceptance mid-run undetected. Falsifier: manifest + authority split already blocks it |
| PS2-3 | Feature Map drift detection: versioned, event-driven re-verification on relevant code change | Refines deferred PS-C1 pilot (first survey); `maintain-verification-skill` already separates doc drift from product regression | Deferred — pilot design input only | A named product repo + explicit user direction to pilot. Falsifier: pilot shows maintenance cost > saved operation cost |
| PS2-4 | Durable execution: idempotency keys, persist-intent→authorize→execute→observe→persist→reconcile | Standing Non-Goal (host runtime); `agent-governance-scaffold` effect receipts + lease-keyed budgets | No change — host responsibility | Explicit direction to build a runtime in a named host. Falsifier: a required guarantee remains prose-only |
| PS2-5 | Untrusted data provides evidence, never grants authority (prompt-injection boundary) | `04-agent/runtime-trust-boundary`; external-adoption-review "data, not instructions" rule | No change — installed | A local incident where retrieved content escalated privileges. Falsifier: boundary already enforced |
| PS2-6 | Prevent / Detect / Contain-Recover three-plane model | `reflective-risk` (dry-run, rollback, human gate); `agent-governance-scaffold` (prevention via contracts); governed-delivery (detection via decorrelated verification) | No change — reframing of installed coverage | A failure that falls between all three planes. Falsifier: existing surfaces already partition the space |
| PS2-7 | A/B/C controlled experiment (agent / +pstack / +governance) with T01–T10 falsification scenarios and effective-throughput metric | New — no installed evaluation protocol for the deferred PS-C1 pilot | **Record as pilot design** — the protocol is the correct evaluation shape if PS-C1 is ever triggered | Trigger: user names a product repo and authorizes the pilot. Falsifier: the protocol's own §8.3 conditions (verification cost up, pass rate flat; oracle still capturable; map maintenance > savings; correlated errors persist; duplicate side-effects after crash) |
| PS2-8 | "Gardener" architecture-governance mechanism | Resolved 2026-09-23: the developer's role over agent output (user clarification), not a mechanism — the paste mislabeled a human-in-loop role as an architecture component | Closed — no mechanism exists to evaluate; the underlying need (human maintenance authority) is already covered by runtime-trust-boundary | — |

No candidate is adopted into an operating contract. PS2-7 is recorded as the
evaluation design for the deferred pilot — it changes what a pilot would
*measure*, not any installed surface.

### Pilot execution addendum (2026-09-22)

PS-C1 was triggered by user direction later the same day and executed at small
scale on `TeaEntityLab/wsgiLite.js`. The full outcome is recorded in the first
survey's pilot addendum (`plans/pstack-survey-2026-09-22.md`). Headline: the
map-drive-find-drift-fix-map loop worked — run 1 surfaced 7 doc-vs-behavior
deviations plus a real traversal quirk; run 2 on corrected docs passed 15/15
with zero deviations. PS2-7's full A/B/C protocol remains unexecuted; this was
a single-product, single-agent smoke of the control+map assets, not the
controlled experiment.

### Authorization addendum (2026-09-23)

User authorized all four open items ("yes for all"):

- **PS-C1 full pilot**: executed on `TeaEntityLab/wsgiLite.js` — see the
  arm×scenario matrix in `pstack-survey-2026-09-22.md` §Discrimination and
  A/B addendum.
- **PS2-4 durable execution**: authorized as a direction. It remains a host
  runtime capability — nothing in this repository can implement it; recorded
  as the accepted answer to "who owns persistence/spawn/cancellation".
- **PS2-8 Gardener**: resolved — user clarified 2026-09-23 that "gardener"
  names the developer's role tending the agent's output ("Being Grok @Bot's
  gardener and maintainer"), not a pstack mechanism. The paste's §4.1 table
  mislabeled a human-in-loop role as an architecture-governance component.
- **wsgiLite.js pilot assets**: pushed to `origin/master` (`a8b8521`).

## Falsifiability

The record's central assessment — that the paste's governance controls are
already covered — is falsified by a named local failure that an installed
surface should have caught but did not. The "Gardener" finding is falsified by
locating the token in the pinned tree. The METR/DORA/OpenAI characterizations
are falsified by primary-source text contradicting the readings above.

## Verification and scope

- Paste read in full (1,895 lines); all repo claims checked at the pin via API
  tree, raw reads, and full-tarball grep.
- External claims verified against primary sources (METR blog posts, DORA 2025
  report, OpenAI research index pages).
- Not checked: the paste's authorship/provenance; Dune's private runtime;
  whether the `.agent/` layout was ever implemented anywhere.
- No operational skills, routing, governance policy or runtime configuration
  changed by this record.
- `make all` (pytest 1283) passes on the recording commit's tree.

## Primary source map

Accessed 2026-09-22:

- [pstack @ 53e579f — shipping playbook](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/poteto-mode/playbooks/shipping.md)
- [pstack @ 53e579f — autopilot-full playbook](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/poteto-mode/playbooks/autopilot-full.md)
- [pstack @ 53e579f — reflect skill](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/reflect/SKILL.md)
- [poteto/verification-skill-example (fictional Atlas)](https://github.com/poteto/verification-skill-example)
- [METR: Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- [METR: Feb 2026 uplift update (selection bias)](https://metr.org/blog/2026-02-24-uplift-update/)
- [DORA 2025: State of AI-assisted Software Development](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf)
- [OpenAI: Hardening Atlas against prompt injection](https://openai.com/index/hardening-atlas-against-prompt-injection/)
