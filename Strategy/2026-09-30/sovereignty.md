# Daily Strategy Research: 2026-09-30

Today's strategic rule is that authority must be bound before the model sees context or releases an effect. Policy attached after generation is too late.

## Authorize effects as typed capabilities

ToolFence compiles a typed authorization blueprint before execution. A deterministic monitor checks concrete calls against tool identity, effect class, parameter provenance, and allowed capability shape. When the blueprint lacks a legitimate capability, a judge grants the reusable capability shape instead of approving each individual call.

### Strategic implication

Tool allowlists are too coarse. An attacker can preserve the permitted tool and replace the recipient, account, file, destination, or query. Authorization has to bind the source and meaning of authority-sensitive arguments. The model may propose an action, but the runtime owns the release decision.

### Control pattern

- resolve tool identity and effect class before dispatch;
- bind sensitive arguments to user-authorized or runtime-owned sources;
- cache capability shapes, never concrete authority-bearing values;
- revalidate each concrete value in the current session;
- route new sensitive targets to explicit approval;
- retain the rejected call, policy version, and grant receipt.

On 629 AgentDojo task pairs with Qwen3-max, ToolFence reduced attack success from 21.20% to 0.20%, with a 3.80 percentage-point clean-utility drop and about 1.6 to 1.9 times runtime overhead. The main residual failure is important: provenance can prove where an allowed value came from without proving that the model chose the value that best matches user intent.

Artifact status: no paper-owned public implementation repository resolved from the primary surfaces. The pattern is implementable, but the reported system is not a drop-in artifact.

Tools and methodologies worth exploring now: typed action manifests, provenance-aware argument validators, Open Policy Agent, Pydantic schemas, capability grants, external-effect receipts

Implementability score: 0.64

Core source: [ToolFence](https://arxiv.org/abs/2609.37196v1)

## Bind memory to the audience before retrieval

Audience-Bound Persistent Memory labels each memory item with the audience present at capture. Derived memories keep the intersection of source audiences, widening requires an explicit object-specific grant, and retrieval admits an item only when every current viewer belongs to an authorized audience. Unknown viewers fail closed to public-only context.

### Strategic implication

A memory store is a disclosure engine. Namespace or tenant separation alone does not protect a fact learned in one private conversation from appearing in another shared context. The permission must travel with the item and its derivations, then be checked against the exact viewer set for every model attempt.

### Control pattern

- capture transport identity and audience on every memory write;
- retain source provenance through derivation and consolidation;
- intersect audiences across combined sources;
- require object-specific grants for any audience widening;
- assemble model context through complete mediation;
- fail unresolved identity to public-only retrieval;
- audit the exact context delivered to the model.

The paper reports a frozen confirmation over 10,000 synthetic multi-party histories. No forbidden item entered the tested flat store, relationship graph, or native runtime context, while unscoped retrieval exposed forbidden items in 82% of contexts. Entitled recall matched policy-equivalent baselines and exceeded unscoped retrieval by 0.30 Recall@5.

Evidence caveat: the guarantee depends on explicit identity, complete provenance, and complete mediation. The study uses an audience overlay on independently authored corpora, and some semantic validation used the same AI judging route rather than an independent human audit. No public implementation repository resolved.

Tools and methodologies worth exploring now: audience labels, provenance-preserving derivation, object-specific grants, context-assembly admission tests, viewer-set receipts

Implementability score: 0.58

Core source: [Audience-Bound Persistent Memory](https://arxiv.org/abs/2609.36373v1)

## Working conclusion

Put authority into typed runtime objects before generation. Bind effects to capability shapes and bind memory to viewer sets. The model can reason over proposals, while the runtime decides what enters context and what reaches the world.
