# Five-Layer Agent SOP Reference Record — 2026-07-04

## Purpose

Preserve the useful concepts and review decisions from the temporary root-level `five_layer_agent*` delivery artifacts before those artifacts are removed. This record is a reference and memory artifact, not an operating rule, not a new workflow skill, and not a runtime commitment.

## Source Artifacts

The reviewed source set was temporary and expected to be removed from the repository root:

- `five_layer_agent_sop_v6_rc_mother.md`
- `five_layer_agent_sop_blog_public.md`
- `five_layer_agent_sop_memo_full.md`
- `five_layer_agent_sop_manifest.json`

A bundle artifact, `five_layer_agent_sop_v6_rc_bundle.zip`, was created during review because the source delivery checklist required it. This reference record does not depend on that bundle remaining present.

## Review 1: Delivery Artifact Check

### Finding

The mother document and memo both declared the delivery should include a bundle zip, but the bundle was absent at first review.

### Action Taken

Created `five_layer_agent_sop_v6_rc_bundle.zip` containing:

- `five_layer_agent_sop_v6_rc_mother.md`
- `five_layer_agent_sop_blog_public.md`
- `five_layer_agent_sop_memo_full.md`
- `five_layer_agent_sop_manifest.json`

### Verification Performed

- Manifest-listed document hashes matched the manifest for bytes, line counts, md5, and sha256.
- Blog and memo were regenerated from the mother document's `SLICE:BLOG+MEMO` / `SLICE:MEMO` sections and matched the checked-in files.
- Blog forbidden terms were absent: `產品假說 H1`, `H1`, `Heddle`, `Mini Ledger`, `Final gate`.
- Archive integrity passed with `unzip -t`.
- Bundle SHA-256 observed after creation: `3368b7c500af856635e24cf80255b0018fd850a8bd128c20dcba62804fc9dced`.

### Residual Note

The manifest anchors the three generated documents, not the zip itself. The manifest was left unchanged because embedding the bundle hash into a manifest that is bundled into the zip creates a self-reference problem.

## Review 2: Prompt / Skill Promotion Decision

### Direct Decision

No TeaPrompt prompt or skill should be changed from this artifact alone.

Reasons:

- The reviewed material is a single reference artifact, not local recurrence evidence.
- TeaPrompt already has nine frozen workflow skills; adding a tenth skill requires recurrence-gated evidence and explicit human approval.
- Many concepts are already covered by existing TeaPrompt prompts and skills.
- Several strong mechanisms are runtime/operationalization-layer ideas, while TeaPrompt intentionally remains a prompt and methodology library rather than an agent runtime.

## Worthy Concepts Preserved

| Concept | Transferable Value | TeaPrompt Coverage / Decision |
| --- | --- | --- |
| Five-layer control plane: α flow gates, β formal SOP, γ durable execution, δ adversarial evaluation, ε governance/standards, ζ memory/identity integrity | Useful taxonomy for thinking about agent risk controls by layer. | Concept only. Existing `04-agent/runtime-trust-boundary.md`, `04-agent/agent-selection.md`, and `reflective-risk` cover the nearby methodology surfaces. Do not create a new taxonomy prompt yet. |
| Risk routing with an irreversible-action tier (`L3-Irr`) | Separates ordinary high-risk work from irreversible external effects. | Already mostly covered by `reflective-risk` and runtime trust-boundary Human Review gates. Do not add another strictness ladder. |
| Effect outbox + commit gate + idempotency key | Strong runtime pattern for irreversible side effects: stage effects, validate, require approval, then commit exactly once. | Runtime candidate only. TeaPrompt can cite the pattern in future runtime design reviews, but should not implement or promise it as prompt text. |
| Third-party skill supply-chain gates: provenance, scan, sandbox trial, permission minimization, signing | Good operational checklist for onboarding untrusted skills or agent scaffolds. | Partly covered by scaffold provenance and trust-boundary prompts. Keep as concept only unless local skill-adoption work recurs. |
| Memory write whitelist and identity-file write protection | Frames long-term memory and identity files as policy surfaces, not ordinary notes. | Runtime / host-enforcement concept. Useful for future trust-boundary reviews; no prompt or skill change from one artifact. |
| High-volatility fact discipline | Dates, standards status, versions, prices, and schedules need check-date, recency caveat, and a tracking point. | Candidate in-place refinement for `reflective-research` if it recurs. Current `research.md` already says to mark items needing fresh verification, but this concept names the fact class more sharply. |
| Number semantic discipline | Keep terms like flawed, critical, and malicious distinct; trace numbers to body tables or primary data, not titles. | Already covered by evidence mapping, claims ledgers, and critical-thinking checks. Preserve as reference example. |
| Maturity three-way split: landed / in-progress / research-stage | Prevents proposal-stage standards or prototypes from being described as mature deployments. | Mostly covered by evidence-strength categories. Useful research phrasing, not a new artifact. |
| Four-dimensional evidence ledger: existence, number-text, attribution/process, extrapolation | More precise than a binary source-supported flag; separates source existence from data generation and extrapolation validity. | Candidate in-place refinement for `reflective-review` or `reflective-research` if repeated. No promotion yet. |
| Domain-specific fallacy list | Captures agent-risk research mistakes: title anchoring, maturity inflation, scanner-solutionism, vendor-narrative overtrust, false convergence, and infrastructure-as-correctness. | Useful reference examples. Existing fallacy scans are general enough; do not add the full list to core prompts. |
| Hypothesis/evidence separation with falsifiers and lock rules | Keeps product hypotheses out of public narrative until validated. | Already covered by `01-thinking/falsifiability.md` and `reflective-research`. |
| Empty-source rule | Missing, unreadable, hash-mismatched, or marker-missing sources are unknown; never fill gaps from context. | Already covered by runtime trust-boundary missing-data discipline and research unknown handling. |
| Delivery anchoring by file presence, line counts, hashes, and sentinel searches | Good anti-fabrication pattern for artifact delivery claims. | Useful for delivery reviews. Not a general TeaPrompt prompt change. |
| Slice-based mother document strategy | Single source of truth with public and memo slices avoids drift between public and internal versions. | Useful documentation pattern. Not needed as a TeaPrompt core rule without recurrence. |
| `evidence-calibrated-revision` v1.2 procedure | Composite procedure for revising research docs under review: source existence, hard-error review, number tracing, maturity split, credibility ledger, volatility scan, hypothesis separation, delivery verification. | Do not create a tenth workflow skill. Treat as a composite of `reflective-research` + `reflective-review` unless repeated local demand justifies a prompt lens. |

## Concept Candidates To Watch

These are the only concepts that may deserve future in-place prompt refinement if they recur in local work:

1. **High-volatility fact discipline** — candidate for `05-domain/research.md` or `skills/reflective-research/SKILL.md` wording if multiple research tasks mishandle volatile dates, standards status, version numbers, pricing, or schedules.
2. **Four-dimensional evidence ledger** — candidate for `reflective-review` / `reflective-research` if simple verified/unverified ledgers repeatedly hide whether the source exists, the number text is supported, the data-generation process is trusted, or the conclusion is over-extrapolated.

Both remain recurrence-gated. They are not new skills.

## Concepts Not Worth Promoting Now

- A new five-layer workflow skill.
- A new strictness ladder competing with TeaPrompt's L1-L6 strictness system.
- Runtime features such as effect outbox, commit gates, idempotency enforcement, memory write ACLs, sandbox execution, signing, or replay logs.
- The full domain-specific fallacy table as a core prompt requirement.
- Delivery-specific slice markers or bundle manifests as general library conventions.

## Decision Ledger

| Claim | Evidence | Unknowns | Counterargument | Decision | Falsifier / Review Trigger |
| --- | --- | --- | --- | --- | --- |
| The temporary files contain useful concepts worth preserving. | Direct review of the mother document, memo, blog, manifest, and delivery checks. | The external research claims inside the memo were not independently reverified in this task. | Temporary docs can become clutter if copied wholesale. | Preserve distilled concepts only; do not preserve raw source files as dependencies. | If future users need raw provenance, add a source-backed research record instead of restoring root temp files. |
| No prompt or skill should be changed now. | Existing TeaPrompt surfaces cover most methodology concepts; project knowledge freezes nine workflow skills and recurrence-gates promotions. | Future recurrence may reveal a sharper local gap. | The high-volatility and 4D-ledger concepts are useful. | Record them as candidates, not edits. | Three independent local recurrences or explicit project decision to update research/review prompts. |
| Runtime mechanisms should not become TeaPrompt commitments. | TeaPrompt's current direction excludes operating its own agent runtime. | A future project direction could add runtime work. | Runtime controls are the most concrete parts of the five-layer memo. | Keep runtime patterns as reference examples only. | Project direction changes to include runtime enforcement. |

## No-Change Record

The reviewed files should not cause immediate edits to:

- `skills/reflective-research/SKILL.md`
- `skills/reflective-review/SKILL.md`
- `skills/reflective-risk/SKILL.md`
- `04-agent/runtime-trust-boundary.md`
- `04-agent/agent-scaffold-provenance.md`
- `05-domain/research.md`

If future work revisits this record, start from the two concept candidates above rather than re-importing the removed root files.

## Human Review

Not required for this reference record. Human approval is required before any future action that creates a new core workflow skill, changes runtime/security gates, or promotes executable knowledge.

## Handoff

After this record exists and the Decision Index points to it, the root-level `five_layer_agent*` files can be removed without losing the TeaPrompt-relevant concepts. Removal itself was not performed in this task.

## 2026-07-05 Promotion Update

The Decision Ledger row "No prompt or skill should be changed now" carried the review trigger "three independent local recurrences or explicit project decision to update research/review prompts". On 2026-07-05 the project owner issued that explicit decision against the v6-RC mother document ("check this and update skills"), firing the trigger.

Scope of the resulting change — the two recurrence-gated candidates only, promoted in place:

1. **High-volatility fact discipline** → `skills/reflective-research/SKILL.md`: new `High-Volatility Facts` section (check date, tracking point, coexisting official/pending values, maturity stage, `stale` downgrade), a Methods bullet, a Never rule, and a `verified`-scope note in the State Ledger.
2. **Four-dimensional evidence ledger** → `skills/reflective-review/SKILL.md`: new `Four Evidence Dimensions` subsection under Claims Ledger (existence, number/text, attribution/process, extrapolation), a Methods bullet, and a Never rule. The research State Ledger points at this table instead of duplicating it.

Everything else in this record keeps its 2026-07-04 status: no new workflow skill, no new strictness ladder, no runtime commitments (effect outbox, commit gates, memory write ACLs, signing), no full fallacy table, no slice/manifest conventions. The `evidence-calibrated-revision` v1.2 procedure remains a composite of `reflective-research` + `reflective-review`; these in-place refinements are that composite treatment, not a tenth skill. The empty-source rule and delivery anchoring stay covered by runtime trust-boundary missing-data discipline and delivery-review practice.
