# Hotline Verification-Redundancy Survey — 2026-09-22

> **Status: decided — record-only; no installed change, no wording adopted.** The
> object is a pasted zh-TW excerpt (user-provided artifact, source unknown —
> apparently the tail of a longer discussion about international institution
> design). Its thesis: mature institutions are not built on "everyone is good" but
> on `assume deception / mistakes / incomplete information / technical failure`,
> then engineered with multiple channels, redundancy, authentication,
> verification, reciprocity, hotlines, inspection, monitoring — closing with
> "Trust is not the architecture. Verification and redundancy are." Its two
> historical claims (1963 hotline telegraph + radio backup; 1971 upgrade driven by
> accident/ambiguity/unauthorized-action risk) verify against primary sources,
> with two precision corrections below. Bare survey → DS-1: nothing installed.
> Guard: `plans/tests/test_hotline_survey_record.py`.

## Research Question

User instruction: "Survey" over the pasted excerpt. Three questions: (1) do the
historical claims about the Moscow–Washington hotline check out; (2) is the
"verification and redundancy, not trust" design philosophy accurately drawn from
them; (3) does any concept expose a **verified gap** on an installed TeaPrompt
surface. A bare survey carries no adoption direction; the standing bar per
candidate is a verified gap on one installed surface, a named failure the change
defends against, a smaller alternative rejected, and a deterministic guard.

## Direct Recommendation (as of 2026-09-22)

- **Study — the failure-mode enumeration as a design primitive.** The paste's
  strongest move is naming the adversarial assumption set *before* the mechanism
  list: deception, mistakes, incomplete information, technical failure. That is
  the arms-control version of a threat model, and it is the correct order —
  mechanisms are justified by the failures they cover, not by their own appeal.
- **Verify — the history holds, with two corrections.** (a) The 1963 MOU did
  establish a duplex wire-telegraph circuit (Washington–London–Copenhagen–
  Stockholm–Helsinki–Moscow) plus a duplex radiotelegraph backup via Tangier —
  the paste's "主要電報線路加無線備援" is accurate. (b) The 1971 upgrade claim
  conflates two same-day agreements: the *Hotline Modernization Agreement*
  (added two satellite circuits — US Intelsat, Soviet Molniya II) and the
  *Accidents Measures Agreement* (whose preamble names "accidental or
  unauthorized use" and whose Articles 2–3 cover unexplained incidents and
  unidentified objects). The accident-risk motivation belongs to the companion
  treaty; the modernization supplied the channel it required. Also: the
  satellite circuits became operational in January 1978, not 1971.
- **Adopt — nothing.** Bare survey → DS-1 record-only. The transferable contract
  (verify over trust, decorrelated channels, evidence before acceptance) is
  already installed: `governed-delivery` carries decorrelated verification, an
  evidence ledger, and failure-signature exits; `agent-governance-scaffold`
  separates proposal/authorization/effect/acceptance authority;
  `04-agent/runtime-trust-boundary` keeps the host as enforcement owner. The
  paste's mechanism list (inspection, monitoring, reciprocity) is treaty-level
  arms control, not hotline engineering — it does not map onto a TeaPrompt
  surface.
- **For citers:** the paste is a user-provided artifact of unknown provenance;
  quote its thesis as opinion, its history only via the primary sources below.
  "You don't need to trust the other side" overstates the case — the hotline
  required mutual cooperation (exchanged teleprinters and encoding devices,
  agreed test traffic). Trust was *minimized and verified*, not eliminated; the
  accurate formulation is the paste's own closing line.

## Method

Coordinator read (2026-09-22), no scouts, no panel: the paste in full; primary
sources — 1971 Accidents Measures Agreement text (Yale Avalon, in full) and the
Arms Control Association hotline-agreements factsheet (in full, which quotes the
1963 MOU circuit topology and the no-voice rationale); corroborating search
results for the 1971 modernization text (state.gov, aerospace.org PDF). Nothing
executed; no code involved.

## Evidence vs Inference

**Verified against primary/official sources:**

- 1963 MOU (signed Geneva, 20 Jun 1963): full-time duplex wire telegraph circuit
  with teletype equipment via London/Copenhagen/Stockholm/Helsinki, plus
  full-time duplex radiotelegraph via Tangier; radio carries traffic if the wire
  circuit is interrupted. Each side installed its own teleprinters on the
  other's territory and encoding devices were exchanged.
- No voice element by design: printed messages chosen over telephone because
  leaders would rely too heavily on rapid translation; text gives clarity and
  time to reflect. The "red phone" is a myth.
- 1971 (30 Sep, Washington): two agreements signed the same day — Hotline
  Modernization (two satellite circuits: US Intelsat, Soviet Molniya II; wire
  retained as backup; radio circuit later terminated; satellites operational
  January 1978) and Accidents Measures (immediate notification of accidental/
  unauthorized/unexplained nuclear incidents; unidentified objects on warning
  systems; advance notice of missile launches toward the other party).
- Daily test traffic from August 1963; first message was a teletype
  all-keys test ("The quick brown fox…"); first real use was the Kennedy
  assassination, then heavy use during the 1967 Six-Day War.

**Inference / opinion (the paste's, assessed):**

- "Trust is not the architecture" — accurate as a design philosophy for
  *channels and verification*, inaccurate if read as "no cooperation required."
  The hotline is a cooperative artifact between adversaries: shared endpoints,
  exchanged crypto material, agreed test procedures. The correct reading is
  *trust minimized and continuously verified*, with redundancy covering
  technical failure and text covering ambiguity — not zero trust.
- The mechanism list mixes layers: hotlines/redundancy/authentication are
  channel engineering; inspection/monitoring/reciprocity are treaty-level
  verification regimes (e.g., later NRRCs, INF on-site inspection). Both belong
  to the same design family, but they are different instruments.

## Candidate Adoption Ledger

| ID | Mechanism | TeaPrompt existing coverage | Decision | Trigger and falsifier |
| --- | --- | --- | --- | --- |
| HL-1 | Enumerate adversarial failure modes (deception, mistakes, incomplete info, technical failure) before choosing mechanisms | `reflective-risk` gate sequence and dry-run; `reflective-spec-plan` falsifiability step; `agent-governance-scaffold` adversarial checks | No change — covered as judgment pattern; the four-item list is a checklist instance, not a new contract | A named local failure that the existing risk gate missed because deception/incomplete-info was not enumerated. Falsifier: adding the checklist changes no decision on a real case |
| HL-2 | Multiple decorrelated channels + redundancy for verification | `governed-delivery` decorrelated verification + evidence ledger; `runtime-trust-boundary` host-owned enforcement | No change — installed | A verification path where a single channel's failure produced a false accept. Falsifier: existing decorrelation already covers the channel set |
| HL-3 | Text-over-voice: prefer typed, inspectable artifacts over synchronous free-form exchange | `04-agent` artifact-promotion (durable artifacts over chat); typed-decision survey lineage (Jev family) | No change — installed as methodology | A recurring case where synchronous negotiation replaced an inspectable artifact and caused a wrong acceptance. Falsifier: no such case observed |
| HL-4 | Exchanged encoding devices: shared schemas/equipment between mutually suspicious parties | `agent-governance-scaffold` contract templates (capability tokens, broker receipts) are exactly shared schemas between distrusting components | No change — installed | A cross-boundary interface lacking a shared schema. Falsifier: existing contract templates already cover it |
| HL-5 | Treaty-level instruments (inspection, monitoring, reciprocity) | None — and none needed: TeaPrompt has no counterpart to on-site inspection of a sovereign | No change — out of scope | Would require a multi-party governance deployment; no such surface exists |

No candidate is adopted. Local recurrence is unknown; the paste is a single
external artifact and counts as inspiration only per Signal Accounting.

## Falsifiability

The record's central assessment — that the paste's transferable content is
already covered — is falsified by a named local failure traceable to a missing
failure-mode enumeration or a single-channel verification path. The historical
corrections are falsified by primary-source text contradicting the Avalon/ACA
readings above.

## Verification and scope

- Paste read in full; thesis and mechanism list assessed as opinion.
- Historical claims verified against: Yale Avalon full text of the 1971
  Accidents Measures Agreement; Arms Control Association factsheet (quoting the
  1963 MOU annex topology and the no-voice rationale); corroborating official
  sources for the 1971 modernization (state.gov archive, aerospace.org PDF).
- Not checked: the paste's original source/conversation context (unavailable);
  the full 1963 MOU annex text beyond the factsheet's quotation.
- No operational skills, routing, governance policy or runtime configuration
  changed by this record.
- `make all` (pytest 1278) passes on the recording commit's tree.

## Primary source map

Accessed 2026-09-22:

- [Agreement on Measures to Reduce the Risk of Outbreak of Nuclear War (1971), full text — Yale Avalon](https://avalon.law.yale.edu/20th_century/sov001.asp)
- [Hotline Agreements factsheet — Arms Control Association](https://www.armscontrol.org/factsheets/hotline-agreements)
- [1963 MOU text — US State Department archive](https://2009-2017.state.gov/t/isn/4785.htm)
- [1971 Hotline Modernization Agreement — US State Department archive](https://2009-2017.state.gov/t/isn/4787.htm)
- [Agreement on Improvement of US-USSR Communications Link (1971) — aerospace.org PDF](https://csps.aerospace.org/sites/default/files/2021-08/Agreement%20on%20Improvement%20of%20US-USSR%20Comm%20Link%20Sep71.pdf)
