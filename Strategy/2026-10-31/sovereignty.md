# Strategy Daily Sovereignty: 2026-10-31

## Scope note

ArXiv published no Saturday listing. This is a non-duplicate carry-forward from the Friday, October 30 listing, submitted October 29. The paper and supplementary claim were inspected read-only. No external code was executed.

## 1. Authorize information for its full propagation scope

Task-Graph Contextual Integrity evaluates a disclosure against the recipient's prior disclosures and the downstream agent graph. A locally acceptable transfer can still create cumulative leakage at the recipient or transitive leakage when forwarded to another agent. The proposed runtime binds each released item to an authorized propagation scope.

Why it matters: per-message privacy checks lose the system-level consequence. Multi-agent memory and delegation need authority that travels with the item and expires at the permitted frontier.

Measured evidence: MAPLE-Bench contains 144 cases across four application scenarios, varied task-graph topologies, disclosure histories, and compromised-agent placements. The paper evaluates two enforcement modes: Full-Scope blocks an item when any downstream transfer is inadmissible, while Auto-Region computes the largest admissible rooted region and removes the item at its frontier.

Fit in the strategy: multi-agent privacy, memory authority, information-flow control, and delegated execution.

Implementable now:
- attach subject, information type, source, recipient, purpose, and downstream scope to every sensitive item;
- maintain disclosure history per recipient;
- compute the allowed propagation subgraph before release;
- strip or redact the item at the authorization frontier;
- log graph version, policy version, decision, and every downstream transfer.

Weakest point: the benchmark is synthetic and judgment quality remains policy-model dependent. Start with deterministic data classes and explicit workflow graphs, then use model judgment only for ambiguous contextual rules.

Artifact status: the paper says source code and MAPLE-Bench accompany the submission as supplementary material, but no dedicated public repository resolved in read-only GitHub search.

Implementability score: 0.68

Core source: [Judging Before Propagation v1](https://arxiv.org/abs/2610.39532v1)

## Working conclusion

A privacy decision must bind the full planned route, not only the next hop. Release sensitive information with an explicit propagation scope and enforce the frontier at runtime.
