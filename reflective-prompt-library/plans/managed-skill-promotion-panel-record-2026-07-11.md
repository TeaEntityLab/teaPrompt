# Managed-Skill Promotion Panel Record (2026-07-11)

Six-lens parallel adversarial review of the host agent's 27 managed skills (`~/.omp/agent/managed-skills/*/SKILL.md` — agent-authored from session memory, not human-reviewed, not repo artifacts) against one question: which of them (or which parts) deserve promotion into TeaPrompt's governed surfaces, under the repo's own promotion gates. Protocol: `parallel-lens-review-packet` (sixth documented in-repo use). Temporary packet `review-packet-managed-skill-promotion-2026-07-11.md` at repo root, deleted after synthesis.

Baseline: branch `main`, `make all` green at 762 tests before this panel's changes.

## Panel Packet

Inventory clustered A (4 TeaPrompt-targeted: parallel-lens-review-packet, teaprompt-project-primer, teaprompt-artifact-promotion, teaprompt-panel-round), B (2 generic methodology minted in other repos: redacted-external-review-panel, external-doc-internalization), C (21 other-project operational skills). Constraints carried: frozen nine core, DOMAIN_PACK_SKILLS registry precedent, Standing Non-Goal (host mechanics stay host-side), signal accounting (external/other-repo use ≠ local recurrence), §4 memory-write gate, adoption-ledger discipline (A1), D1 structural-guard preference, P14 cross-reference-not-duplicate.

## Lenses (all six: AGREE WITH CHANGES)

| Lens | Angle | Key output |
| --- | --- | --- |
| RecurrenceAuditor | three-recurrence gate, repo-native evidence only | parallel-lens protocol: **gate-met** (5 explicit protocol uses in plans/ records 07-06→07-11, +1 partial early instance); every other candidate gate-unmet (0–1 uses) |
| OverlapCartographer | line-level delta vs owning repo surfaces | protocol-gap matrix: packet field list, verdict vocabulary, output-shape headings, ledger hook, use-case buckets absent from recipe; primer/artifact-promotion = near-total duplication |
| HostBoundaryReviewer | host-specific vs host-agnostic; §4(c) provenance; authority laundering | per-line KEEP-HOST-SIDE/RESHAPE inventory; provenance stanza spec; laundering chain named (memory → managed skill → 04-agent → read-as-canonical) with 9 preventive wording rules. NOTE: lens returned a 226-byte stub as final output; full deliverable recovered via IRC follow-up per protocol guardrail — synthesized from the recovered full text, not the preview |
| MinimalityVetoer | veto perimeter; Cluster C | blanket-reject Cluster C (11 spot-checked); preferred promotion set EMPTY, fallback = guardrail bullets inside existing recipe section only; meta:product ratio objection |
| LandingDesigner | exact insertion points, guards, rejected alternatives | recipes §Parallel Lens Review subsection (not new file/skill); artifact-promotion Evidence-rules bullet; README Orientation proposed (panel deferred); guard-module design mirroring test_flow_pack_adoption_state.py |
| DriftReconciler | reverse audit: managed skills stale vs repo truth | 12 drifts incl. 2 actively wrong (panel-round personas; "don't touch router when fixtures pass" vs holdout-before-tune R8); correction drafts for all five Cluster-A/B managed skills |

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES` (6/6). Promotion is warranted for exactly TWO surgical extracts; everything else is no-change, deferred, or rejected. The repo's promotion gates were applied to the agent's own artifacts with no exception: recurrence counted locally, smallest destination, host mechanics quarantined.
- **Use-case:** `adopt` M1+M2; `study` (managed-skill side) the drift corrections; `reject` the rest for repo surfaces.

## Candidate Adoption Ledger

| # | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| M1 | Parallel-lens protocol hardening: "### Packet and verdict contract" subsection in `04-agent/workflow-recipes.md` §Parallel Lens Review (packet fields + evidence taxonomy, lens deliverable + verdict vocabulary, anti-persona rule, synthesis headings + use-case buckets, adoption-ledger requirement, host-wrapper quarantine sentence, own falsifier) + fix of the misleading `local://` Expected-artifacts line | Adopted 2026-07-11 | Recipe section; guard `plans/tests/test_managed_skill_promotion_adoption_state.py`; recurrence: 5 protocol uses (RecurrenceAuditor) | none |
| M2 | Memory-derived-source rule: managed skills / session memories = data, promotion needs §4 gate + provenance + authority class — one bullet in `04-agent/artifact-promotion.md` §2 Evidence rules | Adopted 2026-07-11 | Evidence-rules bullet; same guard module | none |
| M3 | teaprompt-project-primer / teaprompt-artifact-promotion → repo | No-change | OVL/HBR/REC/MIN concur: repo surfaces own the content (README, PK, METHODOLOGY_MAP, GLOSSARY, skill-map, artifact-promotion.md, workflow-acquisition.md); promotion = V-16 duplication + third-authority-layer risk | Managed-skill drift corrections instead (M5) |
| M4 | external-doc-internalization deltas (ephemeral-source workflow, sentinel-fact verification, no-temp-links rule) → `workflow-acquisition.md` | Deferred | Genuine delta (OVL-6) but recurrence gate-unmet: 1 strict local use (five-layer record) | Adopt on third documented local occurrence |
| M5 | Managed-skill corrections (agent-side, not repo): parallel-lens-review-packet packet-path + ledger refs; primer domain-packs + authority chain + 06-repo read-first; artifact-promotion §4(c)/domain-pack/ledger; redacted-panel repo-scope banner + other-repo prefixes; RETIRE teaprompt-panel-round (personas actively wrong, cadence superseded by GLOSSARY playbook) | Adopted 2026-07-11 (host-side) | DriftReconciler tables DRF-PL/TP/AP/PR/RE; managed-skills dir state | Re-audit on next governance panel |
| M6 | README "## Orientation" section (primer extract) | Deferred | LandingDesigner LND-06 vs MIN-SQ02 third-authority-layer + E4 fold-pressure objections; 4/6 lenses no-change | Adopt only if newcomer-orientation gap recurs in future session records |
| M7 | Redaction methodology (leakage scans, packet hashing, execution metadata) → `external-adoption-review.md` | Deferred | HBR-SUM-05: method sound, zero TeaPrompt-local recurrence; TeaPrompt evidence is not sensitive operational data today | Adopt on first TeaPrompt-local sensitive-evidence external review |
| M8 | Cluster C (21 other-project skills) → repo | Rejected | Blanket: V-01/V-17 other-repo operational domain knowledge; 11 spot-checked by MinimalityVetoer; zero TeaPrompt recurrence | none — re-litigate only with a TeaPrompt-local recurrence claim |

## Shared Findings

1. **The strongest candidate was the protocol reviewing itself.** parallel-lens-review-packet is the only managed skill with repo-native recurrence (5 explicit uses in 5 days, all producing plans/ records) — and its promotion correctly lands as recipe enrichment under P14, not a new skill (June reflective-panel reject upheld).
2. **Authority laundering is the central risk of memory→repo promotion.** The chain "session memory → managed skill → 04-agent doc → future agent reads as canonical" bypasses human review unless every promoted extract carries provenance, authority class, and evidence-vs-instruction tags. M2 turns that from packet-constraint into a governed Evidence rule.
3. **Managed skills drift faster than governed surfaces.** Primer silent on domain packs (registered the same day); panel-round frozen at a pre-holdout governance state with persona simulation the July protocol explicitly bans; redacted-panel hardcodes another repo's docs tree. Governed surfaces have validators; managed skills have none — which is the argument for keeping repo-side content canonical and slimming managed skills to pointers.
4. **Host-wrapper quarantine works.** The three genuinely new operational lessons (packet reachability for sub-reviewers, shared-worktree safety, truncated-output follow-up) entered the recipe as ONE generic host-wrapper sentence — acknowledged without encoding `task`/IRC/`local://` mechanics into prompt docs (Standing Non-Goal upheld; DRF-Q4 vs HBR tension resolved).

## Disagreements / Residual Risks

- **MinimalityVetoer preferred an EMPTY promotion set** (managed skills as zero-cost agent-side cache; repo meta:product ratio ~2.45:1 already high). Overruled for M1/M2 on recurrence evidence + laundering-prevention value; preserved here as the strongest standing dissent. Trigger honoring it: M1's own falsifier line — if future panel records satisfy the contracts without the subsection, fold it back.
- **LandingDesigner's README Orientation (M6) deferred, not rejected** — the newcomer-orientation gap is real but unproven; watch future sessions.
- **DriftReconciler wanted git-safety/quota/terse-output promoted as content (DRF-Q4-01..03)**; HBR/OVL/MIN quarantined them as host mechanics. Resolved via the host-wrapper sentence; residual risk: a future host without these safeguards re-learns them the hard way — accepted, since TeaPrompt cannot enforce host behavior (runtime-trust-boundary).
- HBR's stub-output incident (full deliverable only via IRC) is itself evidence for the terse-output guardrail staying in the managed skill.

## Evidence Actually Checked

- **Executed (this panel):** six read-only `task` lenses; one IRC follow-up round (4 messages) to recover HBR's full deliverable; `make all` before (762) and after adoption (see below).
- **Read:** all 27 managed SKILL.md files (6 in full by synthesizer + lenses; 11 Cluster-C spot-checked by MinimalityVetoer; remainder classified by frontmatter/description); owning repo surfaces (workflow-recipes, artifact-promotion, workflow-acquisition, external-adoption-review, PK, GLOSSARY playbook, skill-map, cheatsheet, QUALITY_GATES, ROUTING_CONTRACT); five prior panel records for recurrence.
- **[INFERENCE]:** Cluster-C blanket classification for the 10 non-spot-checked skills rests on name/description + family precedent, not full reads — accepted risk recorded in M8's re-litigation clause.

## Falsifiability

- Wrong if a managed skill with repo-native recurrence ≥3 was left unpromoted and undocumented here (missed-coverage against this panel).
- Wrong if M1's subsection proves ceremony (its inline falsifier fires) and is not folded back.
- M4/M6/M7 deferrals are live: their triggers moving without ledger movement is the drift failure this protocol exists to catch.
- Guard: `plans/tests/test_managed_skill_promotion_adoption_state.py`; ledger lives in this record (M1–M8).
