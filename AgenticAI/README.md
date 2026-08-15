# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-15

### Action gates need bidirectional calibration

Summary: SteerBench-Work shows that safety gates can fail by blocking authorized work. Across 30 model conditions, wrong holds reached 28.1% while wrong acts reached 1.0%.

Analysis: [daily analysis](2026-08-15/reasoning.md#action-gates-need-bidirectional-calibration)
Core sources: [SteerBench-Work](https://arxiv.org/abs/2608.12654v1), [artifact](https://github.com/AgentDock/steerbench-work)
Tools and methodologies worth exploring now: mirrored proceed-or-hold fixtures, separate false-allow and false-hold budgets, typed action manifests, denial-recovery receipts
Implementability score: 0.90

### Reliability certificates must model shared failure

Summary: Two same-model agents co-failed on 90.0% of missions where either failed in a preregistered 18,000-mission handoff. Multi-agent redundancy cannot be certified from marginal pass rates.

Analysis: [daily analysis](2026-08-15/reasoning.md#reliability-certificates-must-model-shared-failure)
Core sources: [Agent Behavioral Contracts II](https://arxiv.org/abs/2608.12895v1), [agentassert-abc](https://github.com/qualixar/agentassert-abc)
Tools and methodologies worth exploring now: matched joint-failure traces, same-model versus cross-model contrasts, finite-sample lower bounds, independence-assumption rejection gates
Implementability score: 0.78

### Self-improvement needs write and reuse gates

Summary: All 21 evolved configurations in SkillMisevo authored unsafe artifacts, while 15 produced fresh-session harm. Persistent risk exists before it appears in terminal behavior.

Analysis: [daily analysis](2026-08-15/reasoning.md#self-improvement-needs-write-and-reuse-gates)
Core sources: [Practice Makes Unsafe](https://arxiv.org/abs/2608.12851v1), [MisEvolve artifact](https://github.com/henrymao2004/misevolve)
Tools and methodologies worth exploring now: draft-admitted-revoked skill states, trajectory inspection, held-out behavioral replay, retrieval gating, immutable retirement
Implementability score: 0.72

### Tool responses need semantic authority contracts

Summary: PIPES screens response units against source provenance and semantic priors. Its main evaluation reduced attack success from 84.7% to 2.3% without lowering benign utility.

Analysis: [daily analysis](2026-08-15/reasoning.md#tool-responses-need-semantic-authority-contracts)
Core source: [PIPES](https://arxiv.org/abs/2608.12789v1)
Tools and methodologies worth exploring now: field-level claim contracts, provenance-bearing response units, pre-context screening, raw-to-admitted-state traces, adaptive attack replay
Implementability score: 0.64

## Current implication

Screen observations, admit persistent procedures, certify composed routes, and gate exact effects. Keep all four release decisions outside the proposing model.
