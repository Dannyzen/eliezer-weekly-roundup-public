# Strategy Deep Dive, 2026-08-12

## Winner: shared memory needs two policy gates

MAP-Graph is this week's strongest finding because it identifies the control seam between retained context and side effects. Shared memory is not safe when it merely retrieves relevant text. The runtime must first decide whether the requesting principal may use the memory, then separately decide whether that evidence may authorize the proposed effect.

[Read the durable deep dive](../memory-authority-control-plane/memory-authority-control-plane.md#august-12-deep-dive-memory-needs-two-gates-not-one-smarter-retriever)

Core source: [MAP-Graph](https://arxiv.org/abs/2608.10509v1)

Implementability score: 0.74

## Why it won the week

The other finalists were narrower:

- One Recipe, Many Harnesses improves the method for evolving coding harnesses across languages and models.
- REDAgentBench improves safety measurement by grading service receipts and final-state changes.
- Quadrat-IPI makes detector comparison concrete across attack families and false-positive budgets.

MAP-Graph matters more architecturally because it governs the transition that all of those systems eventually feed: retained evidence becomes a proposed action. If memory authority is implicit, better retrieval and longer retention amplify the reach of stale, private, poisoned, or revoked state.

## Evidence that changes the design

The paper evaluates 2,700 synthetic tasks per method across three domains. MAP-Graph reports 94.96 percent task success, 72.70 percent exact decision accuracy, and 90.22 percent clean-setting success. It blocked every observed unauthorized read and all 450 revoked cases.

The decisive ablation removed the hard permission filter. Aggregate task success rose to 96.00 percent and exact accuracy rose to 78.63 percent, but unauthorized access rose from zero to every observed attempt. A relevance-first system can therefore look more useful while destroying its security boundary.

The paper's weakest result is equally important: 41 of 450 high-risk action cases ended in impermissible Allow decisions. Provenance filtering does not replace effect authorization. It makes a separate, stricter action gate possible.

## What to implement now

1. Bind every memory and derived claim to stable principal, source, parent, scope, trust, revocation, and validity fields.
2. Filter permission-ineligible records before semantic or lexical ranking.
3. Preserve inherited restrictions through summaries, embeddings, and handoffs.
4. Grade proposed effects with typed `Allow`, `Block`, `Redact`, `Reverify`, and `AskUser` outcomes.
5. Store a receipt connecting candidate memories, filtered records, selected evidence, effective policy, proposed effect, and final decision.
6. Test clean allow, private ancestry, revoked ancestry, poisoned ancestry, stale evidence, and high-risk actions as separate fixtures.

## Evidence boundary

The benchmark is synthetic and templated, the actions are simulated, and most results are single runs. The v1 paper did not expose a resolvable exact public implementation repository. Treat the architecture as a strong design and test pattern, not deployment proof.

## Sources

- [MAP-Graph abstract, immutable v1](https://arxiv.org/abs/2608.10509v1)
- [MAP-Graph PDF, immutable v1](https://arxiv.org/pdf/2608.10509v1)
- [Governed Shared Memory for Multi-Agent LLM Systems](https://arxiv.org/abs/2606.24535v1)
- [Memory Provenance Laundering](https://arxiv.org/abs/2607.29167v1)
- [SafeCommit](https://arxiv.org/abs/2608.04289v1)
