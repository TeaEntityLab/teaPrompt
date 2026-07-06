# Skills Runtime Legitimacy Panel Record — 2026-07-06

## Purpose

Record the parallel-lens decision for the question: **「Skills 的 Runtime 什麼時候才合法？安全性及自動化之間」**.

This record is governance / methodology evidence. It is not legal advice, a compliance certification, a runtime implementation, or approval for any specific host runtime.

## Panel Packet

The panel reviewed the current TeaPrompt boundary after commit `9874a8e` (`Record five-layer concept verification`). The packet separated observed repository evidence from user-provided framing and unverified claims.

Observed inputs included:

- `PROJECT_KNOWLEDGE.md`: TeaPrompt uses composable prompt layers and nine workflow skills as natural-language harness policy, without owning an agent runtime.
- `runtime-trust-boundary.md`: if a required gate cannot be deterministically enforced, default to Human Review, stop, or documented no-go; do not silently omit the gate.
- `artifact-promotion.md`: runtime promotion requires guarantees prompt-only or skill-only artifacts cannot provide.
- `workflow-acquisition.md`: path is no-change → SOP → skill draft → skill plus verifier → runner; prompt/skill cannot guarantee persistence, replay, cancellation, idempotency, role isolation, or side-effect enforcement until runtime code and tests exist.
- `reflective-risk`: high-risk automation requires threat model, authority boundary, dry-run, rollback, bounded execution, audit log, Human Review, and Go / No-go.
- `five-layer-agent-sop-reference-record-2026-07-04.md`: 5+1 is reference-only; TeaPrompt does not implement runtime durability, enforcement, memory ACLs, replay, signing, outbox, or commit gates.

No concrete runtime spec, side-effect inventory, data classification, authority map, rollback design, production workflow, or legal/compliance standard was supplied. The panel therefore defined legitimacy gates; it did not approve a specific runtime.

## Panel Lenses

Usable reviewer outputs:

- Risk governance lens: `AGREE WITH CHANGES`
- Runtime automation architecture lens: `AGREE WITH CHANGES`
- Artifact promotion / minimality lens: `AGREE WITH CHANGES`
- Security / provenance lens: `AGREE WITH CHANGES`
- Reproducibility / verification lens: `AGREE WITH CHANGES`
- Replacement operator strategy lens: `AGREE WITH CHANGES`

One initial operator lens returned a placeholder response and was discarded; the replacement lens supplied the operator-facing synthesis.

## Panel Consensus

**Decision:** `AGREE WITH CHANGES`

**Use-case recommendation:**

| Use case | Recommendation | Runtime legitimacy |
| --- | --- | --- |
| `study` | Read and compare runtime mechanisms as reference material. | Legitimate as reference; no adoption. |
| `reproduce` | Run isolated / sandbox reproduction. | Legitimate as smoke evidence; not deploy evidence. |
| `adopt` | Fold the mechanism into SOP, prompt lens, or skill plus deterministic verifier. | Legitimate when triggers, outputs, failure signals, and verification are stable. |
| `deploy` | Build or depend on runner / runtime / hook / persisted orchestration. | Legitimate only after L4 gates, host-runtime enforcement proof, and accepted risk gate. |

Canonical decision:

> Skills runtime is legitimate only when a workflow needs a guarantee that prompt, SOP, skill, and deterministic verifier cannot provide; host runtime code and tests can deterministically enforce that guarantee; high-risk side effects have Human Review, rollback proof, bounded execution, and auditability; and explicit human / project approval accepts the automation risk.

## Required Wording Changes

### Contract / enforcement split

TeaPrompt specifies required runtime guarantees and legitimacy gates. Host runtime or separately accepted runtime modules enforce them. A skill may declare required runtime guarantees as preconditions; it does not provide them until runtime code and tests exist.

### Skill → verifier → runtime path

The minimum legitimate path is:

```text
L0 no change
→ L1 SOP / checklist
→ L2 skill draft
→ L3 skill + deterministic verifier
→ L4 runner / runtime
```

L3 verifier must be deterministic code, schema, test, static check, replay diff, or equivalent executable check. A single prompt, self-reflection, or model judge is not sufficient as the only gate.

### Runtime necessity

Runtime is necessary only for guarantees that prompt text cannot provide, such as:

- persistence
- replay
- cancellation
- idempotency
- role isolation against prompt injection
- enforced transitions
- side-effect gating
- durable audit trail
- memory / identity ACLs

If prompt, SOP, skill, deterministic verifier, or host-native features can provide the needed guarantee, runtime is overengineering.

### Runtime proof

Runtime legitimacy requires proof, not prose:

- rollback plan is not rollback proof;
- idempotency spec is not idempotency proof;
- runtime design is not runtime guarantee;
- mock / sandbox success is not production approval;
- runtime passing proves execution discipline, not task correctness.

Required proof may include durable state restart checks, replay diffs, idempotency under retry / crash, cancellation honored by the host, outbox / commit-gate tests, and audit-log verification.

### Safety and no-go gates

Any runtime touching tools, memory / identity, credentials, production, billing, external communication, destructive actions, privacy-sensitive data, or irreversible effects requires:

- Human Review gate;
- threat model;
- authority / tool boundary;
- data classification and data-not-instruction separation;
- side-effect inventory;
- dry-run;
- rollback proof;
- bounded execution;
- audit log;
- Go / No-go decision;
- supply-chain provenance and license boundary;
- memory / identity write gate when durable state changes future interpretation, authority, identity, preference, or policy.

If any required gate cannot be deterministically enforced, default to Human Review, stop, or documented no-go. Do not silently omit the gate or replace it with prompt wording.

### Under-automation guard

Minimality must prevent both errors:

- runtime too early: overengineering;
- runtime refused despite required prompt-impossible guarantee: fake safety.

A skill whose contract requires persistence, replay, cancellation, idempotency, role isolation, or side-effect enforcement must either declare that guarantee as an unproven runtime precondition, depend on a host/runtime that proves it, or be downgraded to advisory lens.

### Retirement / demotion trigger

A runtime remains legitimate only while it supplies a needed guarantee not supplied elsewhere. Demote or retire it when:

- host runtime natively provides the guarantee;
- local recurrence stops;
- a replay or adversarial test falsifies the guarantee;
- the workflow can be handled by skill plus deterministic verifier.

## Shared Findings

1. Runtime legitimacy comes from a concrete guarantee gap, not from automation appetite.
2. Runtime solves execution reliability; it does not prove the goal, evidence, conclusion, or policy judgment is correct.
3. L3 verifier must be deterministic; otherwise an L4 runner enforces a probabilistic prompt gate.
4. L4 proof must include data-plane evidence, not only recurrence and risk review.
5. Role isolation against prompt injection becomes a runtime necessity when retrieved or external content can influence a side-effectful action path.
6. Refusing runtime forever is unsafe when the required guarantee is physically impossible in prompt text.
7. Missing runtime spec, authority map, rollback proof, supply-chain provenance, or memory-write gate means unknown / no-go, not safe-by-default.

## Socratic Checks For Future Runtime Proposals

- Which guarantee is missing from prompt / SOP / skill / deterministic verifier?
- Can the host runtime provide it natively before TeaPrompt introduces anything heavier?
- Is the verifier deterministic, or only another model judgment?
- What exact failure proves the workflow is unsafe without runtime?
- What exact replay proves the runtime guarantee works after retry, crash, cancellation, or rollback?
- Which action path touches credentials, production, billing, external communication, destructive operations, privacy-sensitive data, or durable memory?
- If a required gate cannot be deterministically enforced, where is the Human Review / stop / no-go record?
- What demotes this runtime back to skill plus verifier?

## Final Rule

```text
Prompt can express intent.
Skill can shape workflow.
Verifier can check objective outcomes.
Runtime can enforce stateful guarantees.

Use the lightest layer that actually provides the needed guarantee.
Do not use runtime for prestige.
Do not use prompt text as fake runtime enforcement.
```

Chinese operator wording:

> Skills 的 Runtime 何時才合法？——當且僅當某個 workflow 真正需要 prompt / SOP / skill / deterministic verifier 無法提供的保證，例如 persistence、replay、cancellation、idempotency、role isolation、enforced transitions、side-effect gating、audit trail 或 memory ACL；且該 workflow 已有穩定 trigger、inputs、outputs、客觀 failure signals，並已通過 deterministic verifier；且 runtime code + tests 實際證明所需保證；且高風險 action 已通過 reflective-risk、Human Review、rollback proof、bounded execution、audit log 與 Go / No-go gate。
>
> TeaPrompt 只定義這些合法性門檻與 required runtime guarantees，不提供、不擁有、不背書具體 runtime enforcement。Skill 可以要求 runtime，但不能假裝自己提供 runtime。若 host runtime 無法確定性強制某 required gate，預設 Human Review、停止或 documented no-go，絕不靜默省略。
>
> Runtime 通過驗證只證明「執行被管控」，不證明「任務判斷正確」。結論正確性仍需 evidence、tests、review、δ 異質評估與 Human Review。安全性與自動化之間的界線不是「要不要自動化」，而是：所需保證是否只能由可測試的 deterministic runtime code 提供。
