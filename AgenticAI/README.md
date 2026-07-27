# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: Monday, 2026-07-27

### Ground-truth-first memory evaluation exposes tenure crossovers

Summary: A truth-first synthetic benchmark shows that memory rankings can invert between three and nine weeks. Veracium provides a populated MIT-licensed implementation, but the long-horizon comparison covers six users and 108 questions.

Analysis: [daily reasoning analysis](2026-07-27/reasoning.md#ground-truth-first-memory-evaluation-exposes-tenure-crossovers)
Core sources: [paper](https://arxiv.org/abs/2607.21962v1), [repository](https://github.com/veracium-ai/Veracium), [PyPI](https://pypi.org/project/veracium/)
Implementable now:
- generate source facts before rendered conversations;
- test as-of-date recall at multiple tenure checkpoints;
- preserve provenance, validity intervals, write quality, and read cost.
Tools, repositories, and methodologies:
- Veracium, SQLite, MCP, truth-first corpus generation, fixed answerer and judge versions
Implementability score: 0.78

### Protocol-validity audits must prove what a benchmark measured

Summary: HackDetect audits 2,385 traces across 15 agent benchmarks and separates artifact exposure, agent use, and score distortion. It turns benchmark validity into a trace-backed claim.

Analysis: [daily reasoning analysis](2026-07-27/reasoning.md#protocol-validity-audits-must-prove-what-a-benchmark-measured)
Core source: [paper](https://arxiv.org/abs/2607.22368v1)
Implementable now:
- declare the capability that must remain necessary;
- isolate evaluation artifacts and reset mutable state;
- trace alternate score paths and calculate exploit inflation.
Tools, repositories, and methodologies:
- hidden fixtures, immutable snapshots, contamination scans, trace audits, Mislead gap
Implementability score: 0.70

### Skills need paired gain-and-regression accounting

Summary: Nearly 6,000 condition runs show that skills can break tasks the same agent solved without them. Average pass-rate gains hide these regressions.

Analysis: [daily reasoning analysis](2026-07-27/reasoning.md#skills-need-paired-gain-and-regression-accounting)
Core source: [paper](https://arxiv.org/abs/2607.22520v1)
Implementable now:
- pair no-skill and skill-enabled trials;
- report gains, regressions, residual failures, and net effect;
- test context-only influence, grounding, and verification obligations.
Tools, repositories, and methodologies:
- paired A/B harnesses, McNemar tests, trace labels, release regression budgets
Implementability score: 0.62

## Current implication

A useful agent intervention must survive a matched counterfactual. Test memory across tenure, benchmarks against alternate success paths, and skills against the tasks they newly break.
