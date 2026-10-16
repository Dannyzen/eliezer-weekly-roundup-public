# AgenticAI

Implementation analysis for agent evaluation, memory, context policy, tools, model routing, and orchestration.

## Latest Structured Update: 2026-10-16 Daily Scan

### Route cheap models by reversible progress

Summary: SpecAgent lets a weak model execute grounded reads and draft a trajectory, then asks a strong model to accept the longest valid prefix before releasing a state-changing action.

Analysis: [weak model drafts, strong model reviews the trajectory](2026-10-16/reasoning.md#weak-model-drafts-strong-model-reviews-the-trajectory)

Core sources: [paper v1](https://arxiv.org/abs/2610.21463v1), [SpecAgent](https://github.com/LARK-AI-Lab/SpecAgent)

Implementable now:
- classify tool effects by reversibility;
- hold the first mutation;
- return prefix acceptance and repair from the reviewer;
- measure quality, strong-model tokens, memory traffic, latency, and effects together.

Implementability score: 0.78

### Grade the memory store directly

Summary: FEB-30 shows that downstream answer quality can hide broken memory or blame correct memory for retrieval and generation failures. The expected memory state needs its own oracle.

Analysis: [inspect memory state, not only final answers](2026-10-16/reasoning.md#inspect-memory-state-not-only-final-answers)

Core source: [paper v1](https://arxiv.org/abs/2610.22209v1)

Implementable now:
- create explicit fact-evolution trajectories;
- assert memory state after each ingestion step;
- separate create, update, reinforce, supersede, retrieval, and generation failures;
- keep intrinsic and end-to-end scores side by side.

Implementability score: 0.66

## Current implication

Route on effect boundaries and test state where it is produced. Final answers and whole-request model selection hide the failures that matter.
