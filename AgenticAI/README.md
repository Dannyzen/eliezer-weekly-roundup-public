# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, a link into the detailed analysis, primary sources, practical implementation paths, and an implementability score from 0 to 1.

## Latest Structured Update: Saturday, 2026-07-25

### Guardrails need execution-time structural intervention

Summary: GuardianAgentBench evaluates 580 scenarios across six models and three production frameworks. Structural LlamaIndex guards recover 19.9 percent of failures at a reported 0.5 percent false-positive rate and outperform the tested system-prompt baseline across all six models.

Analysis: [daily reasoning analysis](2026-07-25/reasoning.md#guardrails-need-execution-time-structural-intervention)
Core source: [GuardianAgentBench](https://arxiv.org/abs/2607.20982v1)
Implementable now:
- build a 30-scenario omission, mis-selection, over-call, unsafe-argument, and long-chain suite;
- inspect tool identity, arguments, and effect class before execution;
- score task success, unsafe effect, recovery, false positive, cost, and latency separately.
Tools, repositories, and methodologies:
- LangChain, LlamaIndex, Vectara, policy-as-code, exact-effect checks, OpenTelemetry
Implementability score: 0.72

### Local coding agents need governed-data benchmarks

Summary: RRBench evaluates 20 longitudinal data-preparation tasks that create 102 variables. Open-weight 31B to 35B models reach up to 87.9 percent average task completion, while deterministic artifact grading exposes incomplete and incorrect outputs.

Analysis: [daily reasoning analysis](2026-07-25/reasoning.md#local-coding-agents-need-governed-data-benchmarks)
Core sources: [paper](https://arxiv.org/abs/2607.21482v1), [UCL-ARC/RRBench](https://github.com/UCL-ARC/RRBench)
Implementable now:
- create approved synthetic or de-identified task fixtures;
- compare local models at fixed hardware, prompt, budget, and agent configuration;
- grade exact variables plus downstream analysis effects.
Tools, repositories, and methodologies:
- RRBench, Ollama, R, uv, tabular ground truth, deterministic column matching
Implementability score: 0.84

## Current implication

Agent evaluation should end at an observed effect or exact artifact. Put structural guards before side effects and deterministic local verification after them.
