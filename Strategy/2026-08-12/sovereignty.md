# Strategy Daily Sovereignty, 2026-08-12

The strongest strategy finding in the Wednesday batch treats persistent memory as an authority graph, not a semantic cache.

## Shared memory needs provenance-aware admissibility before retrieval and action

MAP-Graph represents agents, sources, memories, claims, and actions in a typed execution graph. It filters permission-ineligible records before ranking, propagates trust through ancestry, and applies an action-sensitive gate before execution.

On 2,700 synthetic tasks per method across three domains, MAP-Graph reports 94.96 percent task success, 72.70 percent exact decision accuracy, and 90.22 percent clean-setting success. It blocked every observed unauthorized read and all 450 revoked cases. The remaining weakness was action-risk sensitivity: 41 of 450 decisions in that group were impermissible Allow outcomes. Across the full method and baselines, the paper records 21,600 main-experiment decision logs, plus 18,900 ablation decisions.

Why it matters: semantic relevance cannot establish whether a memory is admissible for a particular principal or side effect. Authorization must inherit through derivation, revocation must reach descendants, and action risk must be checked after retrieval.

Tools and methodologies worth exploring now:
- typed nodes for principal, source, memory, claim, tool, and action;
- inherited ownership and permission scopes;
- separate hard eligibility filtering from graded trust ranking;
- revocation propagation and descendant marking;
- action-specific thresholds with Redact, Reverify, AskUser, and Allow outcomes;
- receipts that record selected, filtered, and supporting identifiers.

Implementability score: 0.74

Core source: [MAP-Graph](https://arxiv.org/abs/2608.10509v1)

Evidence boundary: the benchmark is synthetic and templated, actions are simulated, and most results are single runs. No exact public implementation repository was verified. The 41 unsafe action-risk decisions show that provenance filtering does not replace an execution gate.

## Working conclusion

Filter memory by inherited authority before semantic ranking, preserve derivation and revocation, then apply a separate action-risk gate.
