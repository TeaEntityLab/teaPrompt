# Diagram Design Survey (2026-10-07)

> **Status:** Reference-only, non-authoritative evidence record (English). Upstream `cathrynlavery/diagram-design` pinned at `d1376371965f513d99cc9ec388835d255c5c88d5` (commit 2026-10-06, checked 2026-10-07). No installation, skill/pack adoption, runtime, or verifier change; registry unchanged (9 core + 10 packs).
> **Scope:** The earlier survey mutated no TeaPrompt files and installed, committed, or pushed nothing; its owned browser/server were closed. This recording turn adds documentation and commits the related records, not the upstream skill.

## Research question

What does `cathrynlavery/diagram-design` actually provide, and which mechanisms are useful to TeaPrompt without adopting its runtime or instructions?

Answer in brief: a diagram-authoring skill that pairs nine semantic behavior patterns with 44 layout-type references, strict per-figure complexity budgets, an extract-then-redraw import discipline with an explicit fidelity ledger, an installed self-check for structural/accessibility basics, repository-only geometry checks, a scoped-CSS SVG export procedure, and a static-first motion contract. Useful as adjacent reference mechanisms for bounded, testable creative specs. No verified local structural gap warrants a new TeaPrompt core skill or domain-pack admission.

No third-party instructions are copied here. Upstream file and line pointers are citations, not imports.

## Upstream identity (dated, immutable)

- Repository: [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) (checked 2026-10-07).
- Pin: `d1376371965f513d99cc9ec388835d255c5c88d5`, remotely observed `main`/`HEAD`, commit timestamp `2026-10-06T16:12:49Z`, checked `2026-10-07`.
- Manifest version `2.6.64` (`.claude-plugin/plugin.json`) versus skill frontmatter `metadata.version: "2.6"` (`skills/diagram-design/SKILL.md`). This is a version-label-to-revision split recorded without assuming behavioral divergence.
- Tag/release inventory (dated, mutable): no tag refs were returned by the ref enumeration and the public releases endpoint returned an empty list on `2026-10-07`. The enumeration included known-present `HEAD`/`main` controls, so the empty result is an inventory observation, not a permanent absence claim.
- Count correction: 44 shipped visual types. The filesystem glob over `skills/diagram-design/references/type-*.md` found 44 files, and independent extraction of the `SKILL.md` visual-type guide found the same 44 unique references. A repository-overview figure of 42 is stale metadata, not the shipped set.

All source citations below are pinned to the above commit and checked `2026-10-07`.

## What the source provides

### Semantic pattern before visual type

The skill separates *what a system does* from *how information is arranged*. When behavior, state, enforcement, or risk carries the meaning, the author first selects one primary semantic pattern from `references/semantic-patterns.md`, then uses the nearest visual type only as layout grammar. If no pattern matches, the type is chosen directly (source: `SKILL.md` selection section; `references/semantic-patterns.md` routing table, checked 2026-10-07).

Nine patterns were observed (fan-in queue/bottleneck, stage framework with semantic slots, unstructured-input-to-artifact, paired policy-evaluation traces, secure paved road, governance/control catalog, compensating security layers, traceable block decomposition, lifecycle phase map). Each pattern names required semantic primitives, anti-patterns, and a static fallback; the pattern owns the tighter budget and the type owns layout. A second pattern may supply at most one supporting primitive; fuller treatment splits into two figures.

### Stricter composition budgets

Budgets are per-figure, not per-project. Examples observed in the pinned source: fan-in limited to a handful of sources, queue slots, one bottleneck, and two outcomes with a single-digit primary-node cap; stage frameworks limited to 3–6 stages and a small slot grid; unstructured-input cases limited to a few exchanges, artifact fields, and provenance links. Above roughly nine nodes the standing advice is that the figure is probably two diagrams; only the `faithful` import detail level exempts the base budget, and then only by zoning above nine nodes and splitting above 24. Connector rules do not relax. These are design contracts, not proof of model compliance.

### Import discipline: extract inert structure, redraw, ledger fidelity

For draw.io, Mermaid, and Excalidraw sources the procedure is: run the corresponding local extractor to obtain an inert digest (nodes, edges, containers, hubs, budget flags), set four output dials (format, size, detail, audience) before drawing, discard source coordinates/colors/fonts/shape quirks, redraw the content, and report what was merged, collapsed, or dropped. Source labels, links, directives, and metadata are treated as untrusted data. An import is bounded by its source: no invented components, no silent drops. The ledger requirement is load-bearing because renderer fidelity is explicitly not promised. Mermaid support covers four grammar families (flowchart, sequence, state-v2, ER), not every creation type. Draw.io and Excalidraw extractors were examined as source, not executed, in this run.

### Installed self-check scope versus repository-only checks

The installed helper (`skills/diagram-design/scripts/self_check.py`) covers accessible naming (`role="img"`, `aria-labelledby` naming title then desc, title-first ordering, per-diagram ID prefixes), prohibited remote references/attributes/scripts, single-file safety, and structural motion basics. It does not verify visual layout or rendered fidelity, and it is not a comprehensive security audit.

Repository-only helpers live outside the installed skill directory. The geometry verifier (`scripts/verify-geometry.py`) applies static heuristics such as connector/label-mask overlap and can catch a clipped label mask. The motion/skin verifiers and screenshot-freshness helpers are likewise checkout-only. Browser rendering, text metrics, and cross-host installation behavior were not part of those helpers.

### SVG portability: scoped CSS, namespaced defs, XML normalization

The export procedure keeps the diagram-only `<svg>` node and intentionally drops editorial wrappers (headers, cards, footers). The packaged exporter carries page CSS into the fragment under a per-file root scope, re-scopes root custom properties, namespaces referenceable `defs` IDs (markers, patterns, gradients, filters, clip paths, masks, symbols) with longest-ID-first rewriting of `url(#…)`/`href` references, normalizes `rgba()` presentation attributes for strict SVG 1.1 consumers, XML-normalizes valueless/unquoted attributes, preserves `role`/`aria`/`title`/`desc`, and gates on diagram CSS presence so a fonts-only fragment fails rather than shipping black boxes. Source-authored title/desc IDs remain caller-owned and must already be unique across files. Cross-editor fidelity (Figma, Illustrator, PowerPoint) was not tested in this run.

### Static-first motion

Motion is an optional presentation layer, never a source of meaning. The default mode is `none` (complete stable figure, no script). Sanctioned non-default modes are single-run reveal, stepped semantic states with explicit controls, and one decorative loop token. The contract requires: complete source before enhancement; static capture (`data-frame="static"`, static query, print, no-JS, standalone SVG) exposing the full frame and hiding controls/decorative tokens; CSS-owned presentation with minimal inline script limited to controls/state; one fixed timing scale with a total cap; explicit integer step order; stable complete end state; scoped per-figure state; and failure-safe startup that leaves complete source visible if script binding fails. Reduced-motion and print paths show the complete static frame.

## Preserved helper evidence: 15 of 15 matched (survey run, 2026-10-07)

The following cases were exercised during the earlier survey against the pinned commit; all expected/observed pairs matched. These are preserved receipts, not reruns during this recording turn. No full upstream suite was run.

| # | Case | Expected / observed |
|---|---|---|
| 1 | `visual_type_inventory` | 44 type-reference files; 44 selection-guide rows; matched. |
| 2 | `static_example_self_check` (shipped architecture example) | Exit 0 / 0; `OK` stdout. |
| 3 | `motion_example_self_check` (shipped animated policy trace) | Exit 0 / 0; `OK` stdout. |
| 4 | `generated_fixture_self_check` (synthetic probe) | Exit 0 / 0; `OK` stdout. |
| 5 | `unsafe_remote_and_script_refusal` (remote image + executable attribute + missing motion root) | Exit 1 / 1; refused with executable-attribute, remote-reference, script-attribute, and motion-root findings. |
| 6 | `broken_accessible_name_refusal` (SVG whose labelledby does not name title then desc) | Exit 1 / 1; refused with accessible-name finding. |
| 7 | `mermaid_inert_extraction` (two-node flowchart fixture) | Exit 0 / 0; digest reported 2 drawable nodes, 1 labeled edge, no cycles, no dangling edges. |
| 8 | `mermaid_semantics_preserved` | Labels `User`/`API` and edge `A → B` labeled `request` preserved; 1 style directive and 1 click handler counted and discarded; matched. |
| 9 | `unsupported_mermaid_refusal` (`pie` grammar) | Exit 2 / 2; refused as unsupported (supported: flowchart, sequence, state-v2, ER). |
| 10 | `probe-a_svg_export` | Exit 0 / 0; SVG written. |
| 11 | `probe-b_svg_export` | Exit 0 / 0; SVG written. |
| 12 | `defs_namespaced_between_exports` | Expected no shared IDs / none shared; arrow/root IDs disjoint per file; title/desc IDs caller-owned and noted as a uniqueness obligation. |
| 13 | `exported_css_and_xml_preserved` | `true` / `true`; both synthetic exports parsed as XML, preserved carried CSS and alpha handling. |
| 14 | `shipped_architecture_geometry` (shipped architecture example) | Exit 0 / 0; `0 finding(s)`. |
| 15 | `clipped_label_mask_refusal` (synthetic later-painted node overlapping a label mask) | Exit 1 / 1; one finding naming the clipped mask rectangle, overlapping node, overlap size, and remediation direction. |

The probe set is narrow: it does not establish full-catalog correctness or model compliance with the source contracts.

## Preserved browser evidence: real Chromium (survey run, 2026-10-07)

Exercised on the shipped animated policy-trace example and the shipped architecture example; one example each, not the full catalog.

- Controls path: initial status at step 0 of 5; Next advanced step 0 to step 1; keyboard End advanced to step 5 with all five rows visible and the completed status text naming the divergence outcome.
- Static query path: all rows visible, controls hidden, web-font requests to `fonts.googleapis.com` and `fonts.gstatic.com` observed.
- Reduced-motion path: all rows visible, controls hidden.
- No-JS path (JavaScript-disabled reload): all rows visible, controls hidden, with an on-page explanation that animation controls require JavaScript and the complete trace is shown.
- SVG render equivalence (synthetic probe): HTML and standalone-SVG rendering of the tested fill (`rgb(235, 108, 54)`), stroke (`rgb(45, 49, 66)`), and system font matched.
- Font-cache qualification: an initial restricted-domain probe retained cached fonts (37 font faces, correct serif family applied, all rows visible) and was explicitly not counted as offline proof. A follow-up run with browser cache disabled and the font stylesheet request intercepted showed the stylesheet blocked, zero font faces, and all policy rows still visible. Fallback readability was observed for that one example only; pixel/typography equivalence is not guaranteed.
- Mobile architecture case: 390px viewport produced a 900px SVG inside a 932px document with no local scroller (`localScroller: false`, `svgLeft: 32`, `svgRight: 932`, title `Content site · Architecture`). This violates the skill's own local-scroll contract for that file only; it is not a statement that all templates fail on mobile.

## Network dependence and explicit non-proofs

- Google Fonts network dependence: generated diagrams, templates, and standalone SVG exports load fonts from `fonts.googleapis.com`/`fonts.gstatic.com` at view time; PNG export renders in a host-provisioned headless browser making the same requests (source: `PRIVACY.md` data-recipients section; `references/export.md` font-import and portability caveat; browser receipts above; all pinned and checked 2026-10-07). Offline or non-fetching import paths substitute typography; the source recommends PNG for pixel-stable portability.
- PNG export was not executed: the procedure requires host-provisioned Playwright plus a compatible browser and the source forbids automatic dependency installation. Browser screenshots in this run are not claimed as that procedure's output.
- Not proven in this run: full upstream suite passage; quality across the full 44-type catalog; effect on model-generated diagram quality (no controlled with/without-skill evaluation); import coverage beyond the exercised Mermaid subset; cross-host installation behavior; cross-editor SVG/PNG fidelity; profile-write containment and concurrency behavior. Unknowns do not justify installation or adoption.

## Candidate Adoption Ledger

| ID | Candidate mechanism | Status | TeaPrompt pointer | Reopen trigger (concrete local failure) |
|---|---|---|---|---|
| DD-1 | Semantic-pattern-before-layout selection (behavior first, type as layout grammar; one primary pattern per figure) | Reference-only | `05-domain/creative-template.md` scope/acceptance (verifiable creative specs, preview gates); `PROJECT_KNOWLEDGE.md` governing principles (minimality, evidence over confidence) | Recurring local consumer failures where creative specs confuse behavior with layout and a controlled demonstration shows the pattern table resolves them. |
| DD-2 | Per-figure complexity budgets with split-not-shrink rule | Reference-only | `skills/reflective-minimality/SKILL.md` (prefer deletion; smallest useful); `05-domain/creative-template.md` falsifiability | Recurring local diagram-bearing specs exceed readability limits, and a controlled check shows that budget caps repair the failure. Destination-specific promotion approval still applies. |
| DD-3 | Extract-inert-structure, redraw, and explicit fidelity ledger for imports | Reference-only | `04-agent/runtime-trust-boundary.md` (instruction/data separation; untrusted source data); `01-thinking/falsifiability.md` | A reproduced local incident where a redraw silently dropped or invented content that a ledger check would have caught. |
| DD-4 | Installed structural self-check shape (accessible naming, prohibited references/scripts, motion basics; no layout proof) | Reference-only | `06-repo/AGENTS.md` harness-policy guards; `05-domain/creative-template.md` validation rules/failure cases | Recurring local creative-spec failures of exactly this structural class, shown by a controlled check to be caught without importing the upstream runtime. |
| DD-5 | Static geometry heuristic shape (e.g. clipped-mask detection as author-side lint, not browser proof) | Reference-only | `plans/` author-side validator precedent (e.g. link/knowledge validators bind authors, not sessions) | A reproduced local defect class where static overlap heuristics catch real authoring errors at acceptable false-positive rates. |
| DD-6 | Scoped-CSS + namespaced-defs + XML-normalized SVG export shape | Reference-only | `05-domain/creative-template.md` fallback paths; runtime trust boundary (host owns operational guarantees) | A local host workflow that inlines multiple exported figures and hits ID/CSS leakage fixed by this namespacing shape. |
| DD-7 | Static-first motion contract (complete static/no-JS/reduced-motion frame; motion never carries meaning) | Reference-only | `05-domain/creative-template.md` animation-as-testable-fields plus fallback; `PROJECT_KNOWLEDGE.md` standing non-goal on runtime guarantees | A local animated-spec failure where missing static fallback or reduced-motion handling caused a real acceptance miss. |

Alternatives explicitly declined:

- Copying the whole skill, design system, or brand-onboarding gate (default paper/ink/accent tokens, Instrument Serif/Geist typography, first-diagram customization pause), or importing its "no Mermaid" aesthetic preference. Reason: specialized authoring choices are not neutral TeaPrompt-wide contracts; borrow a mechanism only for a named host need.
- New core skill or new domain pack. Reason: nine-core freeze and binding admission rule apply; no verified local structural gap was found. Design judgment recorded in evidence: progressive disclosure, minimality, testable creative specs, and preview/fallback gates already exist in TeaPrompt; visualization-specific mechanisms are adjacent reusable references.
- Adopting upstream aesthetic taste rules (editorial coral discipline, density targets, typography ramps) or scope-exclusion rules (unicode sketches, tables-instead-of-diagrams, one-shape sentences) as TeaPrompt rules. Reason: useful review heuristics for diagram authors, not promotion-grade TeaPrompt contracts; no local recurrence demonstrated.
- Runtime guarantees from source instructions. TeaPrompt specifies preconditions; host-runtime code and tests remain the authority for operational guarantees per `PROJECT_KNOWLEDGE.md` standing non-goals. Source instructions alone warrant nothing at runtime, and host-invoked future reuse of a reference mechanism is not TeaPrompt adoption.

## Evidence vs Inference

Evidence (checked 2026-10-07, pinned commit above): research question and decision; manifest/skill version split; dated tag/release inventory; 44-file glob plus 44-row guide agreement; pattern-first selection and budget wording; inert-extract/redraw/ledger wording; self-check acceptance/refusal exits and messages; geometry pass/refusal exits and messages; export CSS/defs/XML behavior on two synthetic probes plus Chromium HTML/SVG equivalence on tested properties; motion controls/static/reduced/no-JS states on one shipped example; cache-disabled blocked-font run with zero font faces and preserved rows; 390/932/900 mobile measurements with no local scroller; PNG non-execution; no TeaPrompt file edits, installs, commits, or pushes.

Inference (design judgment, not upstream proof): no verified local gap warrants core/pack admission; reference-only reuse is sufficient; listed reopen triggers are the falsifiable path to revisit. Unknowns (model-output efficacy, full-catalog quality, cross-host/cross-editor/containment behavior) are recorded as unknowns and do not support adoption.

## Falsifiability

This record is falsified by contrary evidence at the same pinned revision and declared inputs: different version labels; disagreement between the two 44-type inventories; a mismatched helper outcome; a missing static/reduced-motion/no-JS state; or a local scroller in the measured mobile example. Font-fallback comparisons also require the stated empty-cache and blocked-request conditions. Adoption is reconsidered only for a demonstrated local structural gap with the destination's approval gate: a tenth core skill requires three recurrences and explicit human approval; a domain pack requires a registry-admission decision. Neither external popularity nor host-side reuse grants either approval.

## Provenance and citations

- [Pinned upstream tree](https://github.com/cathrynlavery/diagram-design/tree/d1376371965f513d99cc9ec388835d255c5c88d5), commit `2026-10-06T16:12:49Z`, checked 2026-10-07.
- [Skill selection/import contract](https://github.com/cathrynlavery/diagram-design/blob/d1376371965f513d99cc9ec388835d255c5c88d5/skills/diagram-design/SKILL.md), [semantic patterns](https://github.com/cathrynlavery/diagram-design/blob/d1376371965f513d99cc9ec388835d255c5c88d5/skills/diagram-design/references/semantic-patterns.md), and [SVG/PNG export procedure](https://github.com/cathrynlavery/diagram-design/blob/d1376371965f513d99cc9ec388835d255c5c88d5/skills/diagram-design/references/export.md) (checked 2026-10-07).
- [Installed self-check](https://github.com/cathrynlavery/diagram-design/blob/d1376371965f513d99cc9ec388835d255c5c88d5/skills/diagram-design/scripts/self_check.py), [Mermaid extractor](https://github.com/cathrynlavery/diagram-design/blob/d1376371965f513d99cc9ec388835d255c5c88d5/skills/diagram-design/scripts/mermaid_extract.py), [SVG exporter](https://github.com/cathrynlavery/diagram-design/blob/d1376371965f513d99cc9ec388835d255c5c88d5/skills/diagram-design/scripts/export_svg.py), and [checkout-only geometry verifier](https://github.com/cathrynlavery/diagram-design/blob/d1376371965f513d99cc9ec388835d255c5c88d5/scripts/verify-geometry.py) (checked 2026-10-07).
- [Architecture example](https://github.com/cathrynlavery/diagram-design/blob/d1376371965f513d99cc9ec388835d255c5c88d5/skills/diagram-design/assets/example-architecture.html), [animated policy example](https://github.com/cathrynlavery/diagram-design/blob/d1376371965f513d99cc9ec388835d255c5c88d5/skills/diagram-design/assets/example-policy-trace-animated.html), and [font/privacy boundary](https://github.com/cathrynlavery/diagram-design/blob/d1376371965f513d99cc9ec388835d255c5c88d5/PRIVACY.md) (checked 2026-10-07).
- Existing TeaPrompt contracts, unchanged: [project judgment](../PROJECT_KNOWLEDGE.md), [creative-spec acceptance/fallbacks](../05-domain/creative-template.md), [runtime trust boundary](../04-agent/runtime-trust-boundary.md). The [review handoff](recent-changes-review-handoff-2026-10-07.md) tracks unresolved local defects separately from this no-adoption survey.
- Temporary survey paths used during the run are provenance only; this record embeds the values needed to continue without them.
