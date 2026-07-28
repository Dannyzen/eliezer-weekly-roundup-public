# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: Tuesday, 2026-07-28

### Query-conditioned memory misses implicit associations

Summary: InMind separates storage, bridge knowledge, target recall, and final application. Six memory systems reach at most 14.4 percent on indirect application despite direct recall up to 100 percent.

Analysis: [daily reasoning analysis](2026-07-28/reasoning.md#query-conditioned-memory-misses-facts-that-require-world-knowledge)
Core sources: [paper](https://arxiv.org/abs/2607.24368v1), [repository](https://github.com/imlrz/InMind), [project](https://keep-it-inmind.github.io/)
Implementable now:
- add indirect application queries beside direct recall tests;
- preserve critical user constraints in typed visible state;
- compare retrieval, proactive routing, and always-in-state profiles.
Tools, repositories, and methodologies:
- InMind, paired controls, target-recall instrumentation, typed profiles, retrieval-routing A/B tests
Implementability score: 0.82

### Containment needs stage-stratified trace evidence

Summary: ContainmentBench shows that identical zero-harm endpoints can hide major differences in propagation and authorized utility. Its 17,640-rollout study makes containment a trajectory property.

Analysis: [daily reasoning analysis](2026-07-28/reasoning.md#endpoint-security-scores-hide-containment-and-utility-failures)
Core source: [paper](https://arxiv.org/abs/2607.23999v1)
Implementable now:
- trace untrusted observation, proposal, memory, delegation, authorization, and commit;
- report endpoint harm and authorized utility separately;
- preserve stage composition and denominator choice.
Tools, repositories, and methodologies:
- structured event logs, positive controls, matched active-tainted pairs, policy-visible denominators
Implementability score: 0.68

### Coding-agent verification must name the exact code state

Summary: More revision can increase ever-correct while lowering final correctness. Stale traces harmed 34 of 135 correct starts versus 4 of 135 with current evidence in a controlled replication.

Analysis: [daily reasoning analysis](2026-07-28/reasoning.md#coding-agent-evidence-must-be-bound-to-the-exact-code-state)
Core source: [paper](https://arxiv.org/abs/2607.24604v1)
Implementable now:
- hash candidate states before verification;
- bind evidence to code, fixtures, verifier, and environment;
- preserve verified checkpoints and require fresh completion evidence.
Tools, repositories, and methodologies:
- content digests, immutable test receipts, checkpoint preservation, typed admission contracts
Implementability score: 0.72

## Current implication

Evidence is useful only when the runtime can prove which state it describes and whether that state survived to the final effect. Build memory, containment, and coding-agent evaluation around state-bound receipts.
