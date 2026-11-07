# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-07

### Consolidate memory offline against source transcripts

Summary: asynchronous consolidation can correct model-written notes and build navigable wikis, but canonical transcripts must remain available as evidence. Anthropic's internal 25-question evaluation showed the wiki improving across 128 sessions, with search plus wiki outperforming search alone.

Analysis: [Daily analysis](2026-11-07/reasoning.md#1-consolidate-memory-offline-against-source-transcripts)

Core sources: [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory), [dreaming cookbook](https://platform.claude.com/cookbook/managed-agents-cma-dreaming-with-a-dynamic-workflow)

Implementable now:
- append-only transcripts or typed source events
- versioned memory projections and promotion diffs
- source citations, contradiction checks, and duplicate merges
- search-only, projection-only, and combined-path regression tests

Implementability score: 0.88

### Grade evidence limits, not only final answers

Summary: BioBasicsBench evaluates whether agents detect bad controls, ambiguous signals, and unsupported conclusions across 100 raw wet-lab tasks. The reusable method is to score evidence sufficiency and justified abstention separately from the final answer.

Analysis: [Daily analysis](2026-11-07/reasoning.md#2-grade-evidence-limits-not-only-final-answers)

Core source: [Measuring how AI agents handle everyday wet-lab science](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science)

Implementable now:
- real ambiguous work products as test fixtures
- raw multimodal inputs and independent expert rubrics
- separate scores for conclusions, evidence, controls, and abstention
- repeated trials with confidence intervals and token cost

Implementability score: 0.78

## Current working model

1. Version the measurement instrument before comparing models.
2. Preserve typed events before compressing evidence.
3. Build memory as rebuildable projections over source events.
4. Grade evidence sufficiency and justified abstention.
5. Keep release oracles deterministic and independent from the acting model.

## Browse

- [Latest roundup](../roundups/2026-11-07.md)
- [Latest dated analysis](2026-11-07/reasoning.md)
- [Friday synthesis](2026-11-06/reasoning.md)
- [Decision-state compilation](decision-state-compilation/decision-state-compilation.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Skills as control](skills-as-control/skills-as-control.md)
- [Multi-agent orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
