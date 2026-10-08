# Semantica Survey (2026-10-07)

> **Status:** Reference-only, non-authoritative evidence record (English). Source `semantica-agi/semantica` pinned at `320761de5d040a54a3220acc563223b4a7ffdc51`, checked 2026-10-07. No skill admission, TeaPrompt runtime dependency, upstream fix, or new commit/push authorization. Registry remains nine core skills plus ten domain packs.
> **Scope:** Source architecture and accountability claims, separate release/package identities, and bounded offline execution of real Python APIs. Synthetic fixtures only; no model/provider calls. Earlier repair/delivery advisories were already closed in `f86173b`; those repairs were not replayed.

## Research question

What does Semantica actually implement for decision context, provenance, and changing evidence, and what is useful to TeaPrompt without importing another runtime or treating audit metadata as truth?

## Direct recommendation

Keep Semantica as a reference, not a TeaPrompt dependency or new skill. Its useful mechanisms are explicit decision/lineage records, support-ID-based cascading fact retraction, and snapshot-version checks before returning grounded context. The exercised audit checks have a narrower meaning than “full auditability”: they accept fabricated source/actor assertions and miss changes to stored quotes, locations, and metadata, as well as tail deletion.

[INFERENCE] These mechanisms are relevant to a host product that actually owns a graph-backed evidence store. The current TeaPrompt task establishes no local need for that runtime. Existing handoff, memory-promotion, evidence-separation, and runtime-ownership contracts remain the appropriate local surfaces; no operating instructions are imported from upstream.

## Version / date context

Identity inventory was checked 2026-10-07. Mutable branch, release, and registry claims require a new inventory before installation or adoption; implementation observations below belong only to the immutable main pin.

- Repository: [semantica-agi/semantica](https://github.com/semantica-agi/semantica), checked 2026-10-07.
- Executed source: main/HEAD `320761de5d040a54a3220acc563223b4a7ffdc51`, commit `2026-10-07T22:02:41+08:00`, subject `fix(context): restore duplicate guard in add_causal_relationship (#1921)`.
- Release: [v0.7.0](https://github.com/semantica-agi/semantica/releases/tag/v0.7.0), published `2026-09-22T11:18:03Z`, checked 2026-10-07; resolved tag commit `2a9afec685fe6f4a18350834caed3d6a9affb27a`, not the main pin.
- Published package: [PyPI semantica 0.7.0](https://pypi.org/project/semantica/0.7.0/), checked 2026-10-07; wheel `semantica-0.7.0-py3-none-any.whl`, uploaded `2026-09-22T11:17:39.963315Z`; downloaded bytes matched the registry SHA-256:
  `faf27d6259ae813ddb44c5213e2f8867592f27e6e3d6b47cea10f1844513799f`.
- Main manifest and installed distribution both report `0.7.0`; this does not make their source identities interchangeable. The isolated environment installed the published wheel's dependencies, while `PYTHONPATH` selected the pinned main checkout. The probe asserted that `semantica.__file__` was that checkout's `semantica/__init__.py`. No claim is made that the release wheel has the main-only behavior observed here.
- Main declares Python `>=3.10,<3.14`; the executed interpreter was `3.13.12`. MIT license was checked in source `LICENSE` and manifest. Other supported interpreters/platforms were not exercised.
- Dependency-count cross-check: TOML parsing of main `[project].dependencies` and independent installed-wheel `Requires-Dist` metadata filtering (non-extra requirements) each produced **22 direct declarations**, with matching dependency names. Matching names/counts do not establish matching version bounds. The release's historical “44 to 22” and “4x lighter” statements were not remeasured as footprint, install-time, or performance improvements.

## What the source provides

### Broad graph/data framework, not merely an agent prompt library

The architecture describes ingestion → parsing/normalization/splitting → extraction/conflict handling/deduplication → knowledge graph → ontology/reasoning/provenance/context → storage/export/services. The inspected Python modules implement graph records, provenance stores, and deterministic truth-maintenance operations. This survey did not execute that entire pipeline, hosted services, vector/graph database integrations, NLP extraction, or model-backed GraphRAG.

Source: [architecture](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/ARCHITECTURE.md#L7-L68), checked 2026-10-07. The diagram's service/connector counts are upstream descriptions, not independently measured inventories in this survey.

### Decision records and caller-asserted causal links

`ContextGraph.record_decision()` validates record shape and stores a decision node in an in-process graph. Its policy check is a separate operation. A synthetic decision with confidence `0.1`, outcome `unsupported_outcome`, and no decision maker was stored; `check_decision_rules()` subsequently returned `compliant: false` with those three violations. By contrast, NaN confidence was rejected with `ValueError` before graph mutation.

`add_causal_relationship()` normalizes relation vocabulary, rejects missing endpoints, and skips duplicates. The exercised three-decision chain preserved oldest-first upstream ordering, with two causal edges after a duplicate insertion attempt. These are caller-asserted links; recording them does not establish empirical causality.

`ContextGraph.save_to_file()` followed by `load_from_file()` in another process restored graph ID, decision IDs, scenario, and causal chain. This is explicit local-file recovery, not automatic persistence, crash-window safety, concurrent-writer safety, or authenticated acceptance. The separate `DecisionRecorder` interface accepts optional provenance managers and evaluators; inspection found those paths conditional on configuration, not a universal automatic evidence gate.

Sources: [ContextGraph](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/semantica/context/context_graph.py#L3900-L3972) and [DecisionRecorder](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/semantica/context/decision_recorder.py#L97-L143), checked 2026-10-07; observed cases 2–5 below.

### Provenance persistence and PROV-O projection

A default `ProvenanceManager()` used `InMemoryStorage`; a second manager did not recover the first manager's record. Explicit `storage_path` selected `SQLiteStorage`; a separate process restored source, quote, actor, role, and metadata. The default is therefore not a permanent record simply because `track_entity()` returned successfully.

`export_prov(format="turtle")` produced RDF that `rdflib` parsed with the expected `prov:Entity` and `prov:wasDerivedFrom` triples. This proves the exercised vocabulary projection and parseability, not formal conformance certification, source authenticity, or legal compliance. The upstream usage guide explicitly disclaims regulatory certification and legal compliance guarantees.

Sources: [manager/storage selection](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/semantica/provenance/manager.py#L127-L167), [PROV export](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/semantica/provenance/manager.py#L1238-L1413), and [compliance qualification](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/semantica/provenance/provenance_usage.md#L1169-L1179), checked 2026-10-07.

### Audit-integrity boundaries: verified counterexamples

The threat model here is a caller that supplies assertions, or a writer that can modify the synthetic provenance SQLite file. It is not an unauthenticated remote exploit or a claim about deployments with additional controls.

- **Source/actor assertions are not authentication.** `track_entity()` accepted source `NOT-AN-EXISTING-SOURCE`, an invented quote, actor `asserted-human`, and role `approver`; both the checksum and `check()` returned valid. The source file was not supplied or verified.
- **Persisted is not integrity-covered.** Direct SQL updates to `source_quote`, `source_location`, and metadata changed the evidence returned by a fresh manager, while `verify_checksum()`, `verify_chain()["valid"]`, and lineage `integrity_verified` all remained true. `compute_checksum()` omits those fields. A control update to covered `source_document` was detected as `checksum_mismatch`.
- **Hash-chain continuity is not completeness.** Deleting the interior event in a three-event chain was detected as `chain_break`; deleting the last event left a two-event chain that passed verification. No external expected-tail commitment was provided to that verifier.
- **Unambiguous encoding is separate from SHA-256 strength.** The checksum input directly concatenates field strings. Changing `(entity_type, activity_id)` from `("a", "bc")` to `("ab", "c")`, while also relabeling the deliberately unhashed `entity_id`, retained a valid unchanged checksum. This is input-encoding ambiguity, not a cryptographic SHA-256 collision.

Sources: [checksum field coverage/encoding](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/semantica/provenance/integrity.py#L27-L116), [lineage verification](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/semantica/provenance/manager.py#L753-L817), and [chain verification](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/semantica/provenance/manager.py#L1440-L1521), checked 2026-10-07; observed cases 9–13 below.

### Truth maintenance: support identity, cascading retraction, snapshot freshness

`TruthMaintenanceSession` is a deterministic fact/rule mechanism. The inspected validator restricts implication rules to confidence `1.0` and rejects predicate-dependency cycles. It is not an LLM truth judge.

In the exercised fixture, `Evidence(alpha)` derived `Eligible(alpha)` and then `Publishable(alpha)`. Two support IDs backed the starting fact. Retracting one preserved the whole derivation; retracting the last removed all three facts. Attempting to rebind a previously registered support ID to `Evidence(beta)` raised `ValidationError` without changing the committed facts or version.

`TruthMaintenanceContextFilter` checked declared facts, support IDs, and session identity against a snapshot. It excluded an unsupported candidate and a wrong-session candidate. A formerly accepted candidate was excluded after its required support was retracted, even though another support still kept the fact true. Reusing the old snapshot raised `ProcessingError` for staleness.

`ContextRetriever.retrieve()` refused a supplied truth filter in each of `global`, `drift`, and `hybrid` modes; the integration is restricted to `local`. The direct filtering and mode-refusal paths were exercised. Actual local retrieval/ranking, global/DRIFT synthesis, embedding behavior, cross-process truth-session recovery, and retrieval races under concurrent threads were not exercised.

Sources: [session](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/semantica/reasoning/truth_maintenance.py), [rule constraints](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/semantica/reasoning/_truth_maintenance_validation.py#L94-L111), [filter](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/semantica/context/truth_maintenance_filter.py#L111-L203), and [retrieval mode guard](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/semantica/context/context_retriever.py#L226-L253), checked 2026-10-07.

### Trust tiers are heuristics, not independent-source verification

`TierCalculator.calculate(count, confidence)` operates on caller-supplied values. Observed pairs `(2, 0.85)`, `(2, 1.0)`, `(1, 0.85)`, `(0, 0.85)`, and `(0, None)` returned `gold`, `silver`, `silver`, `bronze`, and `quarantine`, respectively. Placeholder confidence `1.0` is treated as missing and degrades the tier. No source records were supplied to the calculator, so these outputs do not authenticate publishers or establish source independence.

Source: [tier calculation](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/semantica/context/tiers.py#L132-L246), checked 2026-10-07.

### Upstream CI is a qualified regression gate

The workflow constructs `pytest --deselect` arguments from `.github/full-suite-known-failures.txt`. Entries marked `windows-only` apply on Windows; other listed entries apply unconditionally. Two integration directories are omitted from this particular step and have separate steps. The source comments explicitly say the gate measures new breakage beyond known baseline defects and that stale deselection node IDs are no-ops.

This is source inspection of the workflow, not a live CI result or a count of current failing tests. No full upstream suite was run; failure populations depend on OS, extras, caches, and the pinned dependency environment.

Source: [CI baseline policy](https://github.com/semantica-agi/semantica/blob/320761de5d040a54a3220acc563223b4a7ffdc51/.github/workflows/ci.yml#L155-L208), checked 2026-10-07.

## Evidence actually checked: bounded offline API execution

The upstream wheel/dependencies were installed only in the private survey environment, using binary wheels; no TeaPrompt dependency/configuration changed. Execution used native `sandbox-exec`, a cleared environment, private HOME/TMPDIR, source-pinned `PYTHONPATH`, and disabled user-site/bytecode writes. The profile denied network operations, data reads below `/Users` and `/private/var/folders`, and writes outside the private survey directory (except `/dev/null`). Four controls matched: repository-content read denied, outside-directory write denied, network connection denied, and private-directory roundtrip allowed. The profile was not a container, used `allow default` for other capabilities, and does not establish general hostile-code escape resistance.

Final real-API run: **18/18 expected outcomes matched**, exit 0. “Matched” includes demonstrated audit limitations; it does not mean 18 safety checks passed. `ContextGraph` fixtures used `advanced_analytics=False`; model calls were zero.

| # | Probe / input | Observed outcome |
|---|---|---|
| 1 | Main manifest, installed distribution metadata, downloaded wheel bytes, module origin | Both versions `0.7.0`; 22 direct declarations by each metadata method; names matched; wheel hash matched; main checkout executed under Python `3.13.12`. |
| 2 | Decision confidence `0.1`, unsupported outcome, missing maker | Record stored; separate policy check returned false and three violations. |
| 3 | Decision confidence NaN | `ValueError`; graph unchanged. |
| 4 | Three decisions, normalized causal relation, duplicate, nonexistent endpoint | Two edges; oldest-first upstream scenarios preserved; duplicate and nonexistent endpoint skipped. |
| 5 | Explicit graph JSON save in one process and load in another | Fresh graph initially lacked the IDs; graph ID, decision IDs, scenario, and causal chain restored. |
| 6 | Default manager record, then fresh default manager | `InMemoryStorage`; first manager had the record, fresh manager did not. |
| 7 | Explicit SQLite path, record with quote/actor/role/metadata, separate reader process | Fields recovered; chain valid with one entry. |
| 8 | Parent/derived provenance records exported as Turtle | RDF parsed; expected entity type and derivation triple present; lineage sources recovered. |
| 9 | Nonexistent source string and asserted human/approver identity | Record accepted; checksum and structural check both valid. |
| 10 | SQL mutation of stored quote, page location, and approval metadata | Fresh reader saw changed values; checksum, chain, and lineage-integrity booleans remained true. |
| 11 | SQL mutation of covered source-document field | Checksum false; chain invalid with `checksum_mismatch`. |
| 12 | Delete interior event versus tail event from separate three-event chains | Interior deletion invalid with `chain_break`; tail deletion valid; each remaining population had two entries. |
| 13 | Relabel entity ID and redistribute checksum fields `a`/`bc` → `ab`/`c` | Unchanged checksum still valid; field-boundary encoding ambiguity demonstrated. |
| 14 | Two supports for `Evidence(alpha)`; two chained rules; successive retractions | First retraction kept all three facts; last removed Evidence, Eligible, and Publishable; versions 1 → 2 → 3. |
| 15 | Rebind support ID to a different fact | `ValidationError`; committed facts/version unchanged. |
| 16 | Grounded, unsupported, wrong-session candidates; retract required support; reuse old snapshot | Only grounded candidate initially retained; required-support retraction excluded it despite another fact support; old snapshot refused as stale. |
| 17 | Truth filter supplied to global, drift, and hybrid retrieval | All three raised `ValidationError` for non-local use. |
| 18 | Five caller-supplied count/confidence pairs listed above | Gold/silver/silver/bronze/quarantine; no source authentication input. |

Initial execution matched 15/18. The retained initial receipt identifies unmatched cases **2** (`record_is_not_policy_gate`), **5** (`explicit_graph_save_load_process_restart`), and **8** (`prov_o_rdf_roundtrip`). The survey harness used object-style access for `find_node()` dictionary results (`type`, `metadata`) in cases 2/5 and `sources` instead of `get_lineage()`'s `source_documents` in case 8. Case 5's initial receipt reports a failed reader subprocess, not its inner stderr. Correcting the dictionary/lineage accesses without changing the SDK or behavioral expectations produced the final 18/18 run; these are harness corrections, not upstream repairs.

Exact command executed (the paths are run provenance, not TeaPrompt runtime configuration):

```bash
sandbox-exec -f /tmp/teaprompt-semantica-survey.pYXSo8/isolation.sb \
  /usr/bin/env -i HOME=/tmp/teaprompt-semantica-survey.pYXSo8/home \
  TMPDIR=/tmp/teaprompt-semantica-survey.pYXSo8/scratch PATH=/usr/bin:/bin \
  PYTHONNOUSERSITE=1 PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH=/tmp/teaprompt-semantica-survey.pYXSo8/upstream \
  /tmp/teaprompt-semantica-survey.pYXSo8/venv/bin/python \
  /tmp/teaprompt-semantica-survey.pYXSo8/smoke.py
```

`shasum -a 256` bound the final harness (`7b6b8a0053133cfed9d46d78a181fa29e4215e56fa09114e8cd228214ff5df31`), profile (`aa50a240bb79bf05581a22f178aaa7cf5f3ce72fe952a34229d41691d4bbc35e`), and result JSON (`85a3284deae7a52104c3eacb48fe064f87fbd085fb0c81c128955cf909b71b3c`). The inputs and observations needed to interpret the decision are embedded above; temporary paths are not required for that interpretation.

## State ledger

| Claim | Evidence / attester | Status / freshness | Remaining constraint |
|---|---|---|---|
| Main/release/package identities are distinct despite shared version label | Ref/checkout receipts, release API, PyPI metadata, module-origin assertion; host survey | Verified, checked 2026-10-07; implementation pin immutable | Re-inventory mutable identities before reuse; release behavior not inferred from main. |
| “4x lighter” release claim | Upstream release wording; direct counts cross-checked by source TOML and wheel metadata | Needs qualification, checked 2026-10-07 | Historical population, footprint, speed, and install-time comparison unmeasured. |
| Recording a decision is a policy/acceptance gate | Real record followed by policy check (case 2); host survey | Refuted for exercised `ContextGraph` path, immutable pin | Configured `DecisionRecorder` evaluators were inspected, not exercised. |
| Successful recording guarantees permanence | Fresh-memory manager (case 6), explicit graph/SQLite process roundtrips (cases 5/7); host survey | Refuted as a blanket claim; explicit recovery verified | Crash recovery, concurrent writes, backups, and retention untested. |
| Provenance integrity booleans cover evidence truth/completeness | Fabricated assertions, field mutation, covered-field control, deletion pair (cases 9–13); host survey | Refuted as a blanket claim, immutable pin | Additional deployment controls were not assessed. |
| Support retraction invalidates dependent facts and stale context | Real rule/session/filter operations (cases 14–17); host survey | Verified for declared fixture and direct filtering paths | Local ranking, non-local synthesis, concurrency, and persistence untested. |
| Trust tier establishes source independence | Calculator with integers/confidence only (case 18); host survey | Refuted for calculator path, immutable pin | A caller's source-count derivation was not evaluated. |
| Green upstream CI means zero known defects | Workflow deselection logic and explanatory comments; upstream source | Needs qualification, checked 2026-10-07 | No upstream suite/CI execution or current failure count claimed. |
| TeaPrompt needs a new graph/runtime skill | Existing local ownership/handoff/promotion contracts plus surveyed mechanisms | Unknown local demand; reference-only judgment | Requires a named local failure and destination-specific promotion/admission approval. |

## Candidate Adoption Ledger

| ID | Mechanism | Disposition / existing TeaPrompt surface | Concrete reopen trigger |
|---|---|---|---|
| SEM-1 | Typed decision → evidence → consequence links | Reference-only; [context handoff](../03-context/context-handoff.md), [reflective handoff/retro](../skills/reflective-handoff-retro/SKILL.md) already preserve decisions, sources, state, and unknowns. No graph runtime adopted. | A named host workflow loses decision-to-evidence links across handoffs and a bounded graph-backed comparison repairs that consumer-visible loss. |
| SEM-2 | Stable support identity, cascading invalidation, snapshot freshness | Adjacent runtime reference; [memory consolidation](../04-agent/memory-consolidation.md) already separates live state, changeable facts, and promotion evidence. Prompt text cannot implement the SDK's set/version operations. | A reproduced local stale-evidence incident requiring host-owned dependency retraction, with explicit source authentication and recovery requirements. |
| SEM-3 | Distinguish stored fields, integrity-covered fields, source authentication, and log completeness | Reference-only counterexample evidence for [runtime trust boundary](../04-agent/runtime-trust-boundary.md); no contract edit or new verifier needed for this survey. | A proposed local audit guarantee incorrectly equates checksum validity or a lineage record with evidence truth or completeness. |
| SEM-4 | Degrade unknown/default confidence instead of treating it as measured certainty | Reference-only; [reflective research](../skills/reflective-research/SKILL.md) and [memory consolidation](../04-agent/memory-consolidation.md) already distinguish observations, assumptions, and changeable facts. No trust-tier calculator adopted. | A named local ranking/acceptance consumer promotes unmeasured confidence or duplicate/colluding sources, and independent evidence-quality validation changes its outcome. |

Alternatives declined:

- **Whole Semantica runtime/dependency adoption:** no named TeaPrompt runtime requirement was demonstrated; this would add graph/data lifecycle ownership outside its natural-language harness scope. This is a TeaPrompt fit decision, not a claim that the SDK is useless to graph-owning products.
- **New core skill or domain pack:** no verified local structural gap or admission decision. Nine core skills remain frozen; a tenth needs the recurrence gate and explicit human approval. Pack admission has its own registry/decision gate.
- **Audit-grade, certified-compliance, or truth guarantees from PROV-O/checksum outputs:** contradicted or not established by the bounded probes. The upstream compliance disclaimer is preserved; this survey is not a legal-compliance determination.
- **Upstream fixes or reporting changes:** user requested a survey, not a Semantica patch. Findings are recorded with pin, inputs, and limits; no upstream code was changed.

## Evidence vs Inference

Evidence (checked 2026-10-07): pinned source/manifest/license and separately identified release/wheel; downloaded wheel digest; direct-dependency name/count cross-check; successful pinned imports; four isolation controls; 18 real-API cases above; three corrected harness access mistakes; conditional evaluator/provenance configuration; restricted deterministic rule validation; explicit upstream compliance disclaimer and CI deselection policy. No Semantica installation or operational instruction was added to TeaPrompt.

[INFERENCE] Reference-only retention is the smallest adequate local result. Decision/evidence links and support-based invalidation are useful design references, while a graph-owning host would need explicit authentication, integrity-field coverage, tail commitments, storage lifecycle, and recovery requirements before stronger audit claims. Those deployment requirements are not verified features of this run.

Unknowns: whole-pipeline correctness; extraction/GraphRAG quality; local retrieval ranking; model/provider utility; comparative improvement over existing TeaPrompt workflows; regulatory acceptance; crash-window/power-loss safety; concurrent/distributed storage behavior; release-wheel behavior; cross-platform support; adversarial sandbox escape resistance. No unknown is treated as a failed feature or as zero demand.

## Falsifiability and sufficiency gate

The scoped evidence is sufficient: identity and exercised mechanisms have source/command receipts; accountability claims have concrete counterexamples and positive controls; unexecuted paths are explicit unknowns; local fit is traceable to unchanged TeaPrompt contracts. The source exposes competing concerns—rich graph/query functionality, audit/identity guarantees, and changing-evidence consistency. This survey addresses the latter two with offline probes; live retrieval quality and operational deployment remain the blind spots, not implied successes.

This record is falsified by a contrary result at the same commit, interpreter/dependency environment, configuration, and declared inputs: e.g. quote mutation fails integrity checks, tail deletion is detected without an external anchor, or the last-support retraction retains unsupported derived facts. Such a result requires resolving the source/fixture/environment difference, not rewriting an expectation to claim passage. A later upstream revision is new evidence, not a retroactive correction to this pin.

The no-adoption judgment reopens for a demonstrated local consumer failure with a named host owner and bounded evaluation. External popularity, successful installation, or a reference-only record does not supply promotion/admission authority.

## Handoff and recording checks

- Source pin, model-free fixture inputs, expected/observed boundaries, decision, and unknowns are embedded in this record. Temporary smoke code is disposable; it is not a new TeaPrompt harness or permanent test suite.
- The session evidence ledger retains raw API results and artifact bindings. [Final report](../../review/final-report.md#semantica-reference-survey-2026-10-07) records the survey alongside, not in place of, prior repair receipts.
- Recording verification uses the actual Markdown renderer and a real Chromium tab, then regenerates `index.json` after final documentation edits and runs `make all`. Those local documentation/gate receipts are separate from the upstream API probe and do not establish SDK efficacy or safety.
- No implementation/admission decision or new commit/push was authorized. Any later reuse needs fresh mutable identity/dependency checks and the target host's own trust, recovery, and acceptance tests.

## Recording-turn consumer evidence (2026-10-07)

The actual Markdown was rendered with CommonMark plus table support. Independent HTML parsing recovered three survey tables, all 18 numbered probe rows with three cells each, nine state-ledger rows with four cells each, and SEM-1–SEM-4 with four cells each. The final-report section and decision-index pointer were present.

Real Chromium loaded that generated local surface at a 1280px viewport. DOM checks recovered the same probe/candidate IDs and column shapes, the scope/unknown qualifiers, the report, and the pointer; document width was 1280px, with no horizontal overflow. A viewport screenshot showed the readable probe-table body, not the entire document or an upstream product UI. This is local recording/rendering evidence only; full repository gate results are kept in the session ledger and delivery receipt.
