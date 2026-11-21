# Code Quality Survey — What a Type Can Rule Out (2026-11-20)

Language: English

> **Status:** reference case (`CQM-DOC1`); no new Skill, review gate or runtime. Decision: use the order example to review one invariant, not to score a codebase. Given a stated domain rule, we can check exactly which states a representation admits or excludes. That does not tell us whether the program takes the right action, how quickly it responds, or what the next change will cost.

## What the authors actually said

| Source checked November 20 | What it supports |
| --- | --- |
| [Brian Cardarella, November 14](https://x.com/bcardarella/status/2121702736643178522) ([text via mirror](https://api.fxtwitter.com/status/2121702736643178522)) | Calls code quality subjective; asks what ships, whether it works, performs and stays stable. Says the benefit to human intervention depends on familiarity with the codebase. Those are his criteria, not measured effects. The post does not prescribe human audit as the final safeguard. |
| [工業聚, November 15](https://x.com/guyingjie129/status/2121944762765001001) ([text and quote metadata](https://api.fxtwitter.com/status/2121944762765001001)) | Quotes Cardarella. The body describes **cardinalities** and writes `Diff = Expected - Actual`. It extends the claim to correctness by construction and agent-written code. |
| [Attached diagram, media ID 2121944748839825408](https://pbs.twimg.com/media/HXKpgauacAAFzb1.jpg?name=orig) | The image itself uses the **symmetric difference**, warns that equal counts do not guarantee equal states, and limits its conclusion to a finite model, a shared domain interpretation and the encoded invariants. It explicitly calls for validation at external boundaries. These qualifications are not inventions of the supplied digest. |
| Replies and editorial synthesis in the supplied packet | The digest attributes the maintenance-effort definition to Robert C. Martin. No reply permalink or complete ranked thread was recovered: exact wording, attribution, “most liked” and the other reported comments remain unverified. The suggested metrics are the digest writer’s proposals, not results reported by either author. |

The two post bodies were available through FxTwitter, not a live X discussion export; the linked image was inspected directly. The relationship between the posts is supported by the quote ID, not just by their similar topics.

## Count the states, not just their sizes

Fix a shared meaning for `(paid, shipped)`. Let `E` be the states permitted by the independently stated rule **shipped implies paid**. Let `A` be the states the code can represent, mapped into those same terms. Otherwise we would be comparing enum names with Boolean pairs rather than comparing what they mean.

The diagram’s `D = |E ∖ A| + |A ∖ E|` counts missing legal states and admitted illegal states separately. `A ⊆ E` is enough to exclude illegal states; `E ⊆ A` means no legal state was lost. `D = 0` requires both. The body’s signed subtraction can be negative; reading it instead as one-sided set difference misses errors in the opposite direction.

| Representation (`paid` is the first bit) | Signed size difference | Missing legal states | Admitted illegal states | D |
| --- | ---: | --- | --- | ---: |
| Independent flags: `00, 01, 10, 11` | −1 | None | `01` | 1 |
| `Unpaid, Paid, PaidAndShipped`: `00, 10, 11` | 0 | None | None | 0 |
| Same size, wrong meanings: `00, 01, 11` | 0 | `10` | `01` | 2 |

**Check performed:** `python3` enumerated `itertools.product((0, 1), repeat=2)`, filtered by `not shipped or paid`, and compared each row by set subtraction and symmetric difference. The resulting `E` matched the diagram’s three legal rows. [Programming Language Foundations in Agda](https://plfa.github.io/Connectives/) explains why independent fields multiply and disjoint alternatives add. For unbounded domains use the inclusion claims and witnesses or proofs rather than subtracting infinite cardinalities. Even in a finite model the count weights every mismatch equally; it says nothing about reachability, frequency or severity.

## A compiler check and its limit

This Rust counterexample adds a **transition** requirement: a shipping request must leave a previously unpaid order unchanged. That requirement is not the same as the diagram’s constraint on a single snapshot.

```rust
#[derive(Debug, PartialEq, Eq)]
enum Order { Unpaid, Paid, PaidAndShipped }
fn ship(_: Order) -> Order { Order::PaidAndShipped }
fn main() {
    #[cfg(bad_value)] let _ = Order::UnpaidAndShipped;
    assert_eq!(ship(Order::Paid), Order::PaidAndShipped);
    assert_eq!(ship(Order::Unpaid), Order::Unpaid, "shipping without prior payment must leave this order unchanged");
}
```

On `rustc 1.97.1`, compiling the snippet from stdin with `rustc --edition=2021 --crate-name order -o order - --cfg bad_value` rejected the nonexistent variant (`E0599`, exit 1). Without `--cfg bad_value` it compiled. Running the binary passed the paid case and failed the unpaid assertion: actual `PaidAndShipped`, expected `Unpaid` (exit 101). No payment or shipment occurred. A constructor can exclude a contradictory label; it cannot attest that the payment provider confirmed a charge. Decode and validate incoming records, and enforce the transition where payment evidence is authoritative.

[Curry–Howard](https://softwarefoundations.cis.upenn.edu/lf-current/CurryHoward.html) relates propositions to types and proofs to terms in a specified formal system. It neither discovers the business rule nor proves that the chosen encoding expresses it. [Type soundness](https://softwarefoundations.cis.upenn.edu/plf-current/StlcProp.html) concerns progress and preservation: in the stated calculus a closed, well-typed term is a value or can step, and a step preserves its type. It is not a promise of the right business outcome. The compiler applies the same check regardless of authorship; the example measured neither human nor agent defect rates.

## Output, maintenance and the TeaPrompt decision

Cardarella’s output questions and the diagram answer different decisions. For a release, test behavior, latency and reliability against the agreed workload. For a risky data shape, identify a concrete invalid value and the boundary that rules it out. For maintainability, compare a specified follow-up change: time to accepted behavior, reviewer effort and regressions, accounting for task difficulty and familiarity. These are proposed measurements, not survey results. More compiler rejections can mean more attempts; fewer runtime checks can mean someone removed validation.

The public [ISO/IEC 25010:2023 abstract](https://www.iso.org/standard/78176.html) describes product quality using multiple characteristics, not one score. [Sawada et al.](https://arxiv.org/abs/2605.06464) (original abstract inspected) observed file changes and who made them across agent- and human-authored files. Change frequency is not effort for the same task; the study does not test this type redesign. Neither the posts nor the local example establishes a productivity effect or explains an industry-wide formal-methods trend.

[Code Reviewer](../02-engineering/code-reviewer.md) already distinguishes a reachable defect or violated invariant from a maintainability judgment. The [MAGE survey](mage-source-survey-2026-11-17.md) distinguishes checking a model from checking an implementation and accepting a product. **Reference only:** no new Skill, review gate or runtime. Revisit the attribution with an actual reply permalink, the state model if the domain permits exceptions, and the maintenance claim with comparable change-task evidence.

## Evidence vs Inference

- **Verified (local run):** `rustc 1.97.1` rejected the nonexistent variant (`E0599`) and the binary's paid case passed while the unpaid case produced `PaidAndShipped` — a constructor bound, not a payment attestation.
- **Verified (sources):** the Curry–Howard and type-soundness citations as quoted; the ISO/IEC 25010:2023 abstract's multi-characteristic quality model; the Sawada et al. abstract as described.
- **Inference (this record):** the mapping of the order example onto Cardarella's output questions and onto maintainability decisions.
- **Unknown:** the authors' reply to the attribution request; whether the domain permits exceptions the state model cannot express; any industry-wide formal-methods productivity effect.

## Falsifiability

`CQM-DOC1` fails if the compiler example is rerun and accepts the contradictory variant without `--cfg bad_value`, if a cited source is shown to claim the opposite of the quoted position, or if a comparable change-task measurement demonstrates the state-model refactor costed more accepted-behavior time than the alternative.
