# Lieflat Less AI Tone Source Survey — Empirical AI-Tone Editing (2026-11-06)

Language: English

> **Status: reference documentation adopted (`LT-DOC1`); no Skill, operating-rule or runtime change.** The owner asked to survey `larashero3-dotcom/lieflat-less-ai-tone`. The outcome is a source-bound record plus catalogue row; every transferable mechanism it demonstrates is already covered by existing TeaPrompt contracts, and its novel contribution is a Chinese-prose ruleset, not a harness mechanism. Its CC BY-NC 4.0 license bounds verbatim reuse to non-commercial contexts. No installation, rule import, commit or push is authorized by this record.

## Research Question and Direct Recommendation

Does the repo contain a mechanism worth adopting into TeaPrompt's prompt-library scope?

**No Skill adoption.** The reusable *mechanism* — detect-first reporting gated on user confirmation, closed-label per-item semantic judging, script/model/human tiering, and visibly recorded vetoes — is already covered by existing change-control, review-panel and settled-decision contracts. The novel contribution is an empirically screened **Chinese-prose ruleset** (A/B/C/F/H/X tiers), which is content for a writing domain, not a harness mechanism; no local deliverable needs it today. CC BY-NC 4.0 additionally bounds verbatim reuse to non-commercial contexts.

## Source pins

| Field | Value |
|---|---|
| Repository | <https://github.com/larashero3-dotcom/lieflat-less-ai-tone> |
| Pinned commit | `53160078a04926d98de57a233549612d1b89bdc9` (`main`, pushed 2026-11-05) |
| License | **CC BY-NC 4.0** (`LICENSE`, NOASSERTION) — non-commercial only |
| Contents | `SKILL.md` 27.9 KB, `DETECT.md` 6.9 KB, `RESEARCH.md` 25.0 KB, `references/semantic-criteria.md`, 5 `scripts/*.py`, one worked example (`examples/agent-memory-case/`) with before/after JSON |
| Claimed evidence | two rounds: 629 paired-topic texts (5 models × 60 + 329 human), then 270 same-topic/same-fact pairs + ~430k model semantic judgments; ~5.2M characters total |

## What the artifact is

A Chinese-prose editing skill: script-level detectors (`detect.py`) plus a
closed-criteria semantic layer judged by the in-session model, plus a human
tier for metaphor aptness. Workflow is gated: detect → deliver report with
metrics/exemplars/proposed edits → **wait for user reply** → rewrite → retest
with before/after diff report (`report.py`). Tiered findings:

- **A** mechanical-safe edits (翻案腔 `不是A而是B`, prompt-colon, 起手式)
- **B** suggested restructures (頓號列舉, long preposed attributives, synonym rotation)
- **C** structure/rhythm metrics, report only (sentence/section-length CV, mtld)
- **F** per-model fingerprints (dashes/semicolons/quotes, with direction)
- **H** human-review zone (metaphor aptness; model consensus measured 0–40%)
- **X** **vetoed** rules kept visible in reports so they are not re-edited —
  three v1 rules reversed under paired replication (ordinal headings, 「這意味著」,
  empty-lead colon lists), one re-vetoed 2026-10-13 on symmetric-recheck (概括替代)

## Falsifiability

The dispositions above are testable:

- If a TeaPrompt deliverable ever requires Chinese-prose editing rules,
  `LT-1` becomes re-evaluable as a domain-pack proposal — the license
  (CC BY-NC 4.0) and the corpus-free upstream are the first constraints
  to re-check.
- If the upstream corpus or judgment logs are published, the
  `[INFERENCE]` rows in Evidence vs Inference upgrade to verifiable;
  replication reversals (X tier) are the highest-value rows to re-check.
- If `detect.py` behavior changes under a new pin (e.g. the announced
  v2.1 autocorrelation check), the executed-differential evidence here
  no longer describes upstream — re-pin before citing.
- The English-transferability question is open by construction; any
  adoption claim extending the ruleset beyond Chinese prose needs its
  own corpus evidence.

## Executed verification (this survey)

- Sparse-free full clone at the pin (6.0 MB); `detect.py` runs on stock
  `python3`, no dependencies, no network.
- **Detector differential (real execution):** a crafted ≥500-字 probe loaded
  with 翻案腔 ×4, prompt-colons, 起手式, 頓號 chains, long attributive, dashes
  fired all expected tiers (A: 翻案腔 4 hits / prompt-colon 2 / 起手式 1; B:
  頓號 4, attributive 1; F: dash 4.8/千字; C: CV flags). The plain control of
  the same content fired only one borderline 頓號 hit. Directional claim
  holds at the smoke level.
- **Semantic layer plumbing (real execution):** `--candidates` emitted 20
  typed candidates (`rename 7 / cohesion 6 / colon 7 / iso3 0`) with the
  documented `label/confidence/reason` write-back schema; example artifact
  `数据-语义判读.json` contains real closed-label judgments with reasons.
  Applying labels is in-session model judgment by design — not
  independently checked.
- **Noise floor:** <500 字 inputs are refused ("检测无意义") — a real
  fail-closed minimum-evidence gate.

## Evidence vs inference

| Claim | Status |
|---|---|
| Script tier detects/counts the documented surface patterns | **Verified** by execution (probe differential, candidate schema, length gate) |
| Corpus statistics (ratios, replication reversals, 43 万判斷) | Author-reported; corpora not shipped; not re-run — **[INFERENCE]** |
| Semantic labels from closed criteria reduce stylistic guessing | Plausible mechanism; self-reported 0–40% metaphor consensus supports the human tier split — **[INFERENCE]** |
| Rules generalize beyond Chinese prose / to English | Untested by upstream; criteria and thresholds are Chinese-specific — **[INFERENCE]** |

## Coverage against TeaPrompt

The reusable *mechanism* is already covered — this survey found no local
contract gap:

- Detect-first / rewrite-after-approval gate → existing change-control and
  review-gate rules.
- Closed-label per-item judging without whole-document vibe scores →
  review-panel discipline (independent itemized verdicts).
- Three-layer routing script/model/human → existing tool-vs-model-vs-human
  escalation boundaries.
- Keeping vetoed rules visible (X tier) → settled-decision/pin records and
  Standing Non-Goal practice.
- Corpus-vs-replication correction of v1 rules → prior advisory pattern of
  re-verifying adopted rules under stronger controls.

The novel contribution is **content, not mechanism**: an empirically
screened, Chinese-specific rule set with per-rule evidence status. No
TeaPrompt deliverable is Chinese-prose editing; a registered domain pack
would need a separate adoption decision with a demonstrated local need.

## Risks and constraints

- **License is CC BY-NC 4.0**: non-commercial only. This survey records
  facts, not copied content; any future verbatim reuse (rule tables,
  thresholds, corpus figures) stays inside those terms.
- Self-reported evidence: headline ratios and the 270-pair replication are
  not independently auditable from the repo (no corpus, no judgment logs
  beyond one example case).
- Model-labeled semantic layer inherits judge self-preference despite closed
  criteria; upstream itself marks the rename criterion as weakest
  (single-model, uniterated).
- Heuristic false positives are expected (synonym-rotation hit in the plain
  control) — mitigated by their report-then-confirm design, not by
  automation.

## Decisions

- `LT-DOC1` **adopted**: record this survey, catalogue entry and ledger row.
- `LT-1` **rejected** (register as a Skills domain pack): domain mismatch —
  the library's packs target prompt-engineering harness behavior, not
  prose-editing rulesets; no local gap or repeated need demonstrated.
- `LT-2` **no change** (import rule thresholds into docs): CC BY-NC reuse
  limits verbatim tables; content is outside library scope anyway.
- `LT-3` **no change** (adopt X-tier "vetoed-but-visible" mechanism):
  already covered by settled-decision and pin records.
- Not maintained-status: upstream is active (pushed 2026-11-05) but
  corpus-free; re-pin before any future citation.

## Next Action / Human Review

Complete. Standing reminders only: CC BY-NC 4.0 bounds reuse; corpus claims
are author-reported. No commit or push is performed by this record.
