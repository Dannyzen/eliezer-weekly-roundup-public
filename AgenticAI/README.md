# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-18

### Capture evidence before outcomes, then replay it

Summary: ForecastGym freezes live search evidence while questions are open, then replays identical evidence across models and memory strategies after settlement.

Analysis: [Daily analysis](2026-11-18/reasoning.md#1-capture-evidence-before-outcomes-then-replay-it)

Core source: [ForecastGym v1](https://arxiv.org/abs/2611.23045v1)

Implementable now:
- timestamped evidence manifests
- provider and rank provenance
- fixed-evidence model comparisons
- separate retrieval, interpretation, and calibration scores

Implementability score: 0.78

### Price context by the whole trajectory

Summary: Context additions and deletions change cache reuse and later agent behavior, so token count alone is not a cost metric.

Analysis: [Daily analysis](2026-11-18/reasoning.md#2-price-context-by-the-whole-trajectory)

Core source: [Context Has a Price v1](https://arxiv.org/abs/2611.22238v1)

Implementable now:
- uncached, cached, and output token accounting
- matched task and seed comparisons
- isolated prefix-cache attribution
- outcome parity gates for cost changes

Implementability score: 0.88

### Preserve conflicts through worker handoffs

Summary: Delegation can retrieve more evidence and still detect fewer conflicts when worker reports remove one side of a contradiction.

Analysis: [Daily analysis](2026-11-18/reasoning.md#3-preserve-conflicts-through-worker-handoffs)

Core sources: [Multi-Agent Memory Inconsistency v1](https://arxiv.org/abs/2611.22245v1), [Surfacing Disagreement Beats Resolving It v1](https://arxiv.org/abs/2611.22461v1)

Implementable now:
- source-linked claim pairs
- conflict-preserving memory records
- evidence-flow stage metrics
- overlapping source access for verification tasks

Implementability score: 0.82

### Regression-test skills, agents, and MCP tools

Summary: GitHub Copilot Evals turns customization changes into approved, repeatable, before-and-after behavioral tests.

Analysis: [Daily analysis](2026-11-18/reasoning.md#4-turn-skills-and-mcp-changes-into-regression-tests)

Core source: [GitHub Copilot Evals public preview](https://github.blog/changelog/2026-11-17-github-copilot-evals-is-now-in-public-preview/)

Implementable now:
- versioned capability fixtures
- outcome and trajectory checks
- explicit approval for side effects
- retained failed traces and comparisons

Implementability score: 0.92

## Current working model

1. Freeze external evidence before the evaluated outcome exists.
2. Measure context changes through total cost and task outcome.
3. Preserve conflicting claims and provenance across worker boundaries.
4. Rerun owned evals after every capability, model, or harness change.
5. Promote only configurations with replayable acceptance receipts.

## Browse

- [Daily roundup](../roundups/2026-11-18.md)
- [Daily analysis](2026-11-18/reasoning.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Context economy](context-economy/context-economy.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Multi-agent orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
