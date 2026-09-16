# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the daily analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-16

### Replace saturated coding-agent ranks with evidence-backed tiers

Summary: An audit of 254 SWE-bench submissions finds the leading two Verified entries tied at 396 of 500 and all 29 examined frontier pairs statistically unresolved. Use tiers first, then deployment-shaped tie-breakers such as cost, latency, recovery, repository fit, and scaffold identity.

Analysis: [daily analysis](2026-09-16/reasoning.md#replace-saturated-coding-agent-ranks-with-evidence-backed-tiers)
Core source: [coding-agent benchmark audit](https://arxiv.org/abs/2609.17394v1)
Tools and methodologies worth exploring now: per-instance verdict matrices, paired separability tests, effective comparison size, tier partitions, frozen scaffold identity, deployment-specific tie-breakers
Implementability score: 0.86

### Treat agent-visible UI as a separate untrusted observation

Summary: Across 546 tasks, 13 Android apps, five mobile-agent frameworks, and three models, pre-deployment UI perturbations achieved 77.9 percent static and 66.9 percent dynamic misleading rates. Human approval must be bound to the exact screenshot, accessibility representation, and widget identity the agent used.

Analysis: [daily analysis](2026-09-16/reasoning.md#treat-agent-visible-ui-as-a-separate-untrusted-observation)
Core source: [UI desynchronization paper](https://arxiv.org/abs/2609.16732v1)
Tools and methodologies worth exploring now: screenshot-accessibility diffs, observation hashes, signed-app allowlists, hidden-widget rejection, human-agent preview parity, desynchronization regression fixtures
Implementability score: 0.62

## Current implication

Do not treat a score or a screen as ground truth. A benchmark must prove it can separate candidates, and an approval surface must prove it matches the representation that drove the agent's action.
