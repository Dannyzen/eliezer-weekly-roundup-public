# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-07

The strongest implementation signal is that long agent runs need source-linked observability, while harness security needs paired utility and attack-effect tests.

### Preserve observability across long-horizon evaluation

Summary: Transect aligns events, token use, sub-agent activity, structural signals, and judge labels on one turn-based timeline. The demonstration covers an almost 13-million-token run and preserves links from labels back to source turns.

Analysis: [daily analysis](2026-10-07/reasoning.md#retain-reviewable-observability-across-long-agent-runs)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.08364v1), [Transect repository](https://github.com/AI-Safety-Institute/transect)
Tools and methodologies worth exploring now: Transect, Inspect AI, structural scanners, judge cohorts, source-turn provenance, independent expert validation
Implementability score: 0.88

### Test harness controls against utility and attack effects

Summary: HarnessSecurity-Bench runs paired control tests with separate deterministic utility and attack oracles. Across 2,500 trials, auto-approve raised attack success from 29.2 percent to 95.6 percent, while alternative execution paths exposed coverage gaps.

Analysis: [daily analysis](2026-10-07/reasoning.md#test-harness-security-with-separate-utility-and-attack-oracles)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.07639v1), [benchmark repository](https://github.com/TsingPig/HarnessSecurity-Benchmark)
Tools and methodologies worth exploring now: paired control trials, deterministic effect oracles, alternative-path fixtures, effective-setting receipts, utility-versus-security curves
Implementability score: 0.81

## Current implication

A useful evaluation must preserve the path from verdict to source event and from security setting to realized system effect. Add semantic summaries only after those evidence paths exist.

Latest roundup: [2026-10-07](../roundups/2026-10-07.md).
