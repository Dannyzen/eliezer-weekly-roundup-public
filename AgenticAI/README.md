# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-10

### Fault injection should test agent recovery at the LLM API boundary

Summary: AgentChaos injects crash, omission, and value faults into content and tool-call fields at runtime. Across 65 fault configurations, pass@1 fell by up to 50 percentage points, while existing diagnosis stayed below 53 percent accuracy for fault type and below 56 percent for fault step.

Analysis: [daily analysis](2026-08-10/reasoning.md#agent-reliability-needs-runtime-fault-injection-at-the-shared-api-boundary)
Core sources: [paper](https://arxiv.org/abs/2608.06790v1), [GitHub artifact](https://github.com/IntelligentDDS/AgentChaos), [Zenodo artifact](https://zenodo.org/records/21823973)
Tools and methodologies worth exploring now: HTTP-boundary fault injection, trigger verification, malformed tool-call tests, retry and propagation traces, duplicate-effect oracles
Implementability score: 0.90

### Deterministic monitors should decide when coding agents need LLM advice

Summary: LivePlan separates judgment from advice. Deterministic trajectory rules trigger a bounded advisor only after drift is detected, improving issue resolution by 9.9 percent on average and up to 15.2 percent with low added cost.

Analysis: [daily analysis](2026-08-10/reasoning.md#coding-agent-steering-should-separate-deterministic-judgment-from-llm-advice)
Core source: [LivePlan paper](https://arxiv.org/abs/2608.06701v1)
Tools and methodologies worth exploring now: explicit plan phases, stagnation detectors, skipped-validation blocks, selective advisor escalation, intervention replay suites
Implementability score: 0.83

## Current implication

Exercise failure recovery at the shared transport boundary, then keep intervention authority outside the advisor model. Deterministic runtime signals should decide when an LLM is allowed to steer the trajectory.
