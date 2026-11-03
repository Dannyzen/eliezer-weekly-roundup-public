# AgenticAI Daily Analysis: 2026-11-03

## Scope

The Tuesday, November 3 arXiv listing is live. The selected papers were submitted November 2 and first listed November 3. External repositories were inspected read-only through GitHub metadata, README files, and repository trees. No external source code was cloned, installed, built, imported, or executed.

## 1. Audit workflow structure instead of collapsing failure into one task score

What Structurally Breaks an Agent? varies dependency depth, candidate count, active state width, and current-state snapshots while holding required operations fixed. Its primary design contains 49,152 generated tasks and 393,216 reference-controller rollouts. A separately frozen follow-on adds 295,936 rollouts over retention, snapshot cadence, recovery, indexing, and related controls.

Why it matters: one aggregate success number cannot distinguish scheduling pressure, state loss, candidate-selection cost, and missing observability. A diagnostic harness should vary one pressure at a time, record the first failure mechanism, and preserve the controller representation used to produce the result.

The practical pattern is to compile small executable workflow families with fixed operation counts, vary one structural dimension, and compare full history, current-state snapshots, indexed lookup, retries, and recovery. Use those fixtures before changing models.

Evidence limit: the large studies use programmed reference controllers. A 0.5B local model completed none of 256 tasks. One 16-episode, two-seed factorial with a routed model completed half, which is descriptive rather than confirmatory. The authors make no cross-provider capability claim or direct benchmark comparison.

Artifact status: the public repository has a populated main branch, README, manuscript, generators, analysis scripts, protocols, and generated artifacts. It was inspected read-only and not executed.

Implementability score: 0.72

Core sources:
- [Paper v1](https://arxiv.org/abs/2611.03227v1)
- [Read-only repository](https://github.com/Shereen20112003/what-structurally-breaks-an-agent)

## Practical cut

Build a compact structural fault suite before buying a larger model: fixed-work dependency depth, candidate fan-out, mutable state width, snapshot visibility, and retry cost. The test must report the first broken mechanism, not only final success.
