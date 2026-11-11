# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-11

### Link reusable memory to source trajectories

Summary: WikiTrace lets an agent descend from a concise lesson to the compilation and raw run that produced it. It improved the same-insight baseline by 3.2 points and reduced memory Regression from 6.5 percent to 4.5 percent.

Analysis: [Daily analysis](2026-11-11/reasoning.md#1-link-every-reusable-lesson-to-its-source-trajectory)

Core sources: [paper v1](https://arxiv.org/abs/2611.14320v1), [repository](https://github.com/yukyeongleee/wikitrace)

Implementable now:
- source trajectory IDs and content hashes
- read-only evidence descent
- conflict and failed-source triggers
- separate memory Gain and Regression metrics

Implementability score: 0.88

### Preserve run memory in an ordinary private workspace

Summary: CAMG-II uses Bash and an episode-persistent workspace across context replacement. CAMP-II shows that models can learn file-based memory behavior that transfers to external coding and terminal benchmarks.

Analysis: [Daily analysis](2026-11-11/reasoning.md#2-treat-a-persistent-workspace-as-the-models-memory-interface)

Core source: [paper v1](https://arxiv.org/abs/2611.14009v1)

Implementable now:
- per-run persistent workspaces
- standard note, evidence, plan, and receipt files
- hidden verifiers outside writable state
- content-intervention tests

Implementability score: 0.46

### Grade rendered work products

Summary: MKA evaluates 200 private visual knowledge-work tasks under one open-source harness and rubric, while ten public tasks expose the format. The grader renders files and inspects spreadsheet formulas rather than trusting the transcript.

Analysis: [Daily analysis](2026-11-11/reasoning.md#3-grade-the-rendered-deliverable-not-the-chat-transcript)

Core sources: [Google announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/multimodal-knowledge-agent-benchmark/), [methodology](https://artificialanalysis.ai/articles/google-deepmind-multimodal-knowledge-agent), [public sample](https://huggingface.co/datasets/google/multimodal-knowledge-agent), [Stirrup](https://github.com/ArtificialAnalysis/Stirrup)

Implementable now:
- delivery-surface fixtures
- factual and visual rubric dimensions
- rendered artifact and formula checks
- pinned harness, tools, sandbox, and grader

Implementability score: 0.82

## Current working model

1. Treat memory summaries as claims linked to raw evidence.
2. Preserve run state in private, inspectable workspaces.
3. Keep hidden tests and authority-bearing state outside writable context.
4. Evaluate the delivered artifact under a pinned harness.
5. Measure regressions introduced by memory, not only aggregate gains.

## Browse

- [Latest roundup](../roundups/2026-11-11.md)
- [Latest dated analysis](2026-11-11/reasoning.md)
- [Friday synthesis](2026-11-06/reasoning.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
- [Agent serving runtime](agent-serving-runtime/agent-serving-runtime.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Skills as control](skills-as-control/skills-as-control.md)
- [Multi-agent orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
