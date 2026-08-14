# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-14

### Command-path evaluation must separate generation from transport

Summary: QuoteBench’s 56 exact-state Bash tasks show that one added parser can damage the same replies by 55.4 to 73.2 percentage points. Contract-conditioned generation can compensate enough to make a matched score hide the defect.

Analysis: [daily analysis](2026-08-14/reasoning.md#quotebench-command-path-evaluation-must-separate-generation-from-transport)
Core sources: [paper](https://arxiv.org/abs/2608.13547v1), [public artifact](https://github.com/LeonardNJU/quoteBench)
Tools and methodologies worth exploring now: fixed-reply replay, exact final-state validators, transport identity, argv or typed operations, ShellCheck, network-disabled execution fixtures
Implementability score: 0.92

### Long-horizon R&D needs deterministic process metrics

Summary: Seven frontier models, 36 tasks, and 756 rollouts show that reliability separates systems more than peak performance. Experience can improve or degrade later decisions, and harnesses mainly affect stability.

Analysis: [daily analysis](2026-08-14/reasoning.md#beyond-final-scores-evaluate-the-research-loop-as-a-process)
Core source: [Beyond Final Scores](https://arxiv.org/abs/2608.13417v1)
Tools and methodologies worth exploring now: framing-execution-feedback decomposition, avg@N versus best@N, progress-retention metrics, positive and negative experience-transfer tests, harness stability comparisons
Implementability score: 0.70

### Iterative repair needs property-preservation gates

Summary: Across 5,968 IaC repair timelines, the conservative strict security-regression rate is 3.3 percent of scenarios. Regressing transitions carry 2.6 times more code churn and 4.9 times more strict-mode check volatility.

Analysis: [daily analysis](2026-08-14/reasoning.md#iterative-repair-needs-property-preservation-gates)
Core source: [Does Fixing Break Security?](https://arxiv.org/abs/2608.13404v1)
Tools and methodologies worth exploring now: per-check state ledgers, Checkov, Terraform validation, best-state checkpoints, structural-change gates, policy-as-code preservation tests
Implementability score: 0.88

## Current implication

Instrument the path, the process, and the properties that must remain true. Terminal success alone cannot attribute capability or authorize release.
