# MengTo/Skills Source Survey — Designer Skill Library and Workflow Skills (2026-11-22)

Language: English

> **Status:** source-qualified reference record (`MTS-DOC1`); no Skill, prompt-body, operating-rule, or runtime change. The owner asked to survey `MengTo/Skills`. This record pins the tree that was read, checks the repository's own counts, and maps its workflow-category mechanisms onto existing TeaPrompt contracts. It does not install a skill, copy a script, register a marketplace entry, or authorize a demo/screenshot pipeline.

## Research Question and Direct Recommendation

Which mechanisms in the MengTo skills library are worth borrowing, and do they expose a TeaPrompt Docs or Skill gap?

**Record the boundaries; do not adopt a library or add a Skill.** The library is 213 designer-facing skills: ten categories of which eight (3d, web-design, illustration, game-combat, game-development, media, ui, video-editing) are visual/design domain packs outside TeaPrompt's product surface. The transferable substance lives in `agent-skills/workflow/` (4 skills) and parts of `agent-skills/codex/` (verification, extraction, audit). Those mechanisms — external verification gates, maker/judge separation, measured-bytes delivery, evidence-graded explanation — are already required by TeaPrompt contracts at the prompt level, or they are host/product behaviors (session-management tools, live-site publish, changelog pages) this repository does not own.

## Evidence Used and Date Context

Checked **2026-11-22**. Repository: [MengTo/Skills](https://github.com/MengTo/Skills) (checked 2026-11-22). `git ls-remote` returned `main` at `6a6a368bb94202bcb264716aad48ed77591e5c65` (commit time 2026-11-22 16:35 +0800, message `Add liquid glass, press shaders, workspace lighting and instrument icon skills`) and no tags. The two `codex/*` branches (`build-youtube-companion-runbooks`, `upload-public-skills-2026-08-01`) were not read.

| Item | Identity | What this check covers |
| --- | --- | --- |
| Pin | `main` `6a6a368bb94202bcb264716aad48ed77591e5c65` | Shallow clone at HEAD. Root README, CLAUDE.md, DEMOS.md header, the folder contract, and the skill bodies listed below were read at this revision. |

## What Was Read

- Root `README.md` (523 lines: philosophy, folder contract, category index), `CLAUDE.md` (repo guide: folder contract, style, safety), `DEMOS.md` header.
- `agent-skills/workflow/README.md` and all four skill bodies: `workflow-progress-screenshots` (+ `scripts/capture.mjs` header), `workflow-score-to-target`, `workflow-ship-change`, `workflow-threads-manager`.
- `agent-skills/codex/` bodies: `iterate-until-verified` (read in full), `audit-verify-explain-grade-5`, `audit-reference-originality`, `article-prompts-to-skills`, `web-technique-to-skill`, `performance-profiling`, `video-to-superprompt`. Other codex skills (`daily-ui-inspiration-capture`, `stitched-full-page-capture`, `html-to-interaction-prompts`, `browser-video-recording`, `optimize-web-animations`, `build-daily-inspiration-sites`, `generate-reference-inspired-brand-worlds`, `implement-fog-of-war`, `publish-project-to-github`, `elevenlabs-tts`, `codex-gpt-image-2-5-flare`, `write-like-meng-on-x`, `x-bookmark-quote-posts`) were classified by frontmatter and listing only; bodies not line-audited.
- Category directories under `agent-skills/` enumerated; one `agents/openai.yaml` interface file sampled (`3d-cloth-material`).
- Root `scripts/` listing (`backfill-skill-demos.mjs`, `build-demo-screenshot-gallery.mjs`, `sync-neuform-skill-demos.mjs`, `test-sync-neuform-security.mjs`, `validate-skill-demos.mjs`). Not run.

Not read, so not evidence:

- `SCREENSHOTS.html`, `SCREENSHOTS.md`, `SCREENSHOTS-preview.jpg`, `DEMOS.md` body rows.
- Any `demo/` assets, `demo/index.html`, `demo/PROMPT.md` recreation prompts, or per-skill `REFERENCES.md`/`ARTICLE.md` bodies beyond the sampled files.
- The two `codex/*` branches and any skill folder bodies in the eight visual categories.

## Counts

Two methods over the pinned tree, both 213:

- `find agent-skills -name SKILL.md` → 213 files.
- Per-category totals: web-design 101, 3d 27, game-development 25, codex 20, illustration 14, media 7, ui 7, game-combat 6, workflow 4, video-editing 2 — sums to 213 and matches the README's "ten categories / 213 skills" claim.

No runnable check of skill correctness exists upstream; `scripts/validate-skill-demos.mjs` was inventoried but not executed. A `SKILL.md` count is an inventory, not evidence any skill works.

## Evidence vs Inference

| Mechanism | What the pinned skill says | TeaPrompt surface already checked | Gap |
| --- | --- | --- | --- |
| Iterate until verified | Lock the task contract; convert ambition words into an observable acceptance matrix (gate, method, pass condition, evidence); fan out only independent workstreams; verifier sees task + rubric + candidate but not the implementer's rationale; blind comparison requires real anonymization, not claimed; match proof surface to work type; stop as blocked rather than weaken a gate; a "Compose" mode returns the same contract as a reusable prompt wrapper. | `flow-loop-harness` requires an external deterministic verifier, caps, exit-code discipline, and never trusting model "done". `reflective-brief` fixes acceptance criteria and falsifiability before execution. `reflective-review` is the independent-verdict channel; `golden-benchmark-runner` forbids n=1 proof and composite claims without confounds. `arm-blinded-eval-harness` covers blinded paired evaluation. | The loop machinery is the same contract at prompt level; "Compose mode" is a prompt-wrapping technique, not a missing gate. |
| Score to a numeric target | The user's named bar ("get it to 8") is a standing rule for that work kind; write the rubric first (10–1 anchors), break items into 3–5 criteria at 0–2 points each, measure where measurable, improve round by round with a picture per round, report what is still short. | `flow-loop-harness` iterates until a verifier passes; its gates are binary. `reflective-review` audits claims; `QUALITY_GATES_SUMMARY` and route paraphrase evals score routing, not artifacts. | A numeric-target scoring loop is a rubric variant of the same pattern, not a demonstrated missing contract. Deferred — see MTS-DOC2. |
| Progress screenshots | Send the picture, do not describe it; send unasked after each meaningful pass; capture start / key moment / result with identical framing; look at every image before sending; caption what each proves; label headless captures and phone-sized viewports honestly; if it cannot be captured, say so. | No `screenshot`/visual-evidence rule exists in `skills/` or `04-agent/` (checked 2026-11-22). `reflective-implement` and `verification-map-generator` cover verification generally without a visual-evidence clause. | The one coverage hole in this survey, but it is host-IO behavior (the host owns file-sending and a browser). Recorded as a deferred doc note, not a Skill gap — see MTS-DOC2. |
| Ship a change | Done requires all seven: screenshots, changelog version with pictures, verification (own tests + merged commits' tests + asset checks + full suite on the pushed commit), one cohesive commit of only your files, fast-forward push confirmed on the remote, publish of exactly `origin/main` confirmed live, measured sizes. Guardrails: ask before any upload over 50 MB, never force-push, never publish unmerged work, deploy to a draft URL and verify before promoting. | `governed-delivery` emits a seven-gate contract with oracle manifest and named acceptance; `agent-governance-scaffold` owns effect authority and per-action approval for production; `reflective-risk` gates high-risk operations. TeaPrompt ships no product: changelog pages, live domains and media releases are product rules. | Fast-forward-only, measure-don't-estimate, draft-then-verify-then-promote are operator habits already implied by evidence-before-claim. No local defect. |
| Oversee many threads | Session-management tools (`list_sessions`, `list_events`, `archive_session`) plus scripts to audit changelog coverage, live health, worktree state; triage table for running/done/cut-off/waiting; archive only after captures are saved and work verified; do not edit files another thread owns; a stray branch is not automatically lost work. | `reflective-handoff-retro` and `03-context/context-handoff.md` cover handoff and continuation, not live multi-session supervision. The tools named are one host's session API. | Host runtime capability this harness does not expose. Not adopted. |
| Technique → reusable skill | Write the one-sentence mechanism first — the thing whose removal makes the effect stop working; if you cannot, there is no skill. Sort every part into mechanism (skill), staging (demo), incidental (nowhere). The demo must prove both the mechanism and the reference fidelity. Disclose the verified stack beside the visible name. Re-audit the quality contract on every revision. | `04-agent/workflow-acquisition.md` and `artifact-promotion.md` gate capture → replay → skill/verifier/runner with recurrence evidence; `plans/validate_skill_examples.py` pins skill surface conventions. | The one-sentence mechanism test is a transferable authoring litmus. Deferred as a doc note — see MTS-DOC2. |
| Article → skills | Extraction ledger (source prompt → capability → keep/remove → skill name → demo proof); one skill per independent behavior; name skills after the mechanism, never the source article; demo and validation ship with the skill. | Same acquisition/promotion surfaces as above. | Same deferred note; the ledger format is presentation, not a new gate. |
| Audit, verify, explain | Treat every answer as audit → verify → explain; evidence order tests > running artifact > logs > inspection > labeled inference; never upgrade "should improve" to "measured" without traces; explain in grade-5 language. | `reflective-review` evidence tiers put self-assessment last; report conventions already separate verified/inferred/unknown. | Already required. |
| Originality audit | Build a source registry first; pair every red flag with current-site and reference evidence; keep fact/inference/unknown access separate; audit-only boundary; do not declare legal plagiarism from visual similarity. | `reflective-review` Declined-to-Judge and evidence-separation conventions. | Domain application of an existing method. No gap. |
| Folder contract | `SKILL.md` required; `REFERENCES.md` links only; optional `ARTICLE.md`, `assets/`, `scripts/`, `demo/` (`index.html` + `PROMPT.md`); "Use when…" triggers; prefer defaults and acceptance checks; procedural, not encyclopedic. | TeaPrompt skills use `SKILL.md` + pinned `examples/` surfaces and the nine-skill frozen core; domain packs live beside it. | Structural similarity only. The `demo/` + `PROMPT.md` recreation-proof packaging is a visual-skill convention with no local need. |

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| MTS-DOC1 | This record and its catalogue row | Adopted: documentation only | Bare survey. Refresh when `main` moves past `6a6a368` or a cited skill changes. |
| MTS-DOC2 | Two deferred doc notes: (a) a visual-evidence rule for verification surfaces — send/show the render, label the capture method honestly, say when it cannot be captured; (b) the one-sentence mechanism test for artifact extraction — if removing one thing does not kill the effect, you packaged staging, not a mechanism | Deferred | Promote only when a TeaPrompt task actually verifies visual output (a) or extracts a reusable pattern from working code (b). External presence is not local recurrence. |
| MTS-SK1 | New Skill, or an edit to an existing Skill or prompt contract | No change | No verified local structural gap. The workflow skills restate contracts already in force. |
| MTS-RUN1 | Run `capture.mjs`/`compare.py`/ship/threads-manager scripts, install skills, or invoke host session-management tools | Not adopted | Host runtime is a Standing Non-Goal; the threads-manager tools are one product's session API and do not exist in this harness. |
| MTS-RULE1 | Copy "screenshots unasked", a numeric score target, the 50 MB ask threshold, or changelog-with-pictures as a TeaPrompt acceptance rule | Rejected | Product and host rules from one project's operating agreement; adopting them as universal gates would overclaim. |

Missing local usage data remains `unknown`, not zero demand.

## Falsifiability

- A reproduced local failure where a verified-by-claim report lacked visual evidence a capture would have shown would promote MTS-DOC2(a); a single missing picture or a preference complaint would not.
- A TeaPrompt skill extraction that shipped staging instead of mechanism — with a worked example of the failed skill — would promote MTS-DOC2(b). Neither promotes to a Skill edit by itself; an in-place doc or prompt repair is the smallest change first.
- Reproducing a verifier that accepted an implementer's self-assessment while a gate actually failed would be a miss of the existing evidence-tier rule, not evidence `iterate-until-verified` is needed.
- A later commit, tag, or reorganization of `agent-skills/` changes freshness only after the new identity is pinned; `6a6a368` stays the tree this record describes.
- Unknown here: whether the library's own demo validators pass on the pinned tree; whether the visual skills produce the claimed output; the two unread `codex/*` branches; and whether any part of this library is installed anywhere locally (`unknown`, not zero). The README's claims about portable agent support (Codex, Claude, Cursor, Aura Build) are the project's own description, not a verified compatibility fact.

## Standing Non-Goals

No skill install, no script execution (nothing under `scripts/` or per-skill `scripts/` was run), no marketplace registration, no model call, no visual/demo adoption, no claim that any of the 213 skills works as described. The eight visual domain categories are recorded as out-of-scope product packs, not evaluated. Commit/push remain unauthorized by this record.
