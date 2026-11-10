# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-10

### Grade evidence sufficiency before answer accuracy

Summary: two readers produced concrete answers on 196 and 182 of 203 certified-insufficient trajectory prefixes. Correct-looking answers therefore do not prove that visible memory supports them.

Analysis: [Daily analysis](2026-11-10/reasoning.md#1-grade-evidence-sufficiency-before-answer-accuracy)

Core source: [paper v1](https://arxiv.org/abs/2611.11840v1)

Implementable now:
- compatible-history witness pairs
- separate support, correctness, and abstention labels
- deterministic checks before LLM judges
- source-bound evaluation receipts

Implementability score: 0.86

### Measure orchestration with fixed executors

Summary: WorkflowArena records executable delegation across 145 long-horizon tasks and uses fixed executors to separate workflow quality from worker strength.

Analysis: [Daily analysis](2026-11-10/reasoning.md#2-measure-orchestration-as-its-own-capability)

Core sources: [paper v1](https://arxiv.org/abs/2611.12856v1), [repository](https://github.com/Einsia/WorkflowArena)

Implementable now:
- shared planning and execution budgets
- delegation and dependency traces
- fixed-executor transfer tests
- hidden integrated-deliverable verifiers

Implementability score: 0.74

### Interpose before optimizing agent cost

Summary: Agency places deterministic context and tool optimizations between existing harnesses and model providers. The paper reports up to 35 percent savings, but no public implementation resolved.

Analysis: [Daily analysis](2026-11-10/reasoning.md#3-put-cost-optimization-in-a-harness-interposition-layer)

Core source: [paper v1](https://arxiv.org/abs/2611.12122v1)

Implementable now:
- call-level cost decomposition
- repeated-context and redundant-tool analysis
- reversible feature-flagged transforms
- same-task cost, success, latency, and failure-shape gates

Implementability score: 0.62

## Current working model

1. Certify that visible evidence supports the answer.
2. Evaluate workflow quality separately from worker capability.
3. Charge planning, delegation, and execution to one budget.
4. Optimize cost only behind reversible accuracy gates.
5. Preserve typed traces and independent effect verifiers.

## Browse

- [Latest roundup](../roundups/2026-11-10.md)
- [Latest dated analysis](2026-11-10/reasoning.md)
- [Friday synthesis](2026-11-06/reasoning.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
- [Agent serving runtime](agent-serving-runtime/agent-serving-runtime.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Skills as control](skills-as-control/skills-as-control.md)
- [Multi-agent orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
