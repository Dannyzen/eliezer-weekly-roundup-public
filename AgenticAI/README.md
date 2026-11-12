# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-12

### Compile repeated agent traces into planner-free workflows

Summary: ReTrace turns an SOP and evidence-bearing agent traces into a portable rule document and executable workflow where code selects the next step. It traded several points of task success for large runtime and cost reductions, then recovered performance through failure-driven repair.

Analysis: [Daily analysis](2026-11-12/reasoning.md#1-compile-repeated-agent-traces-into-planner-free-workflows)

Durable topic: [Decision-state compilation](decision-state-compilation/decision-state-compilation.md)

Core source: [ReTrace paper v1](https://arxiv.org/abs/2611.14492v1)

Implementable now:
- typed rule documents with guards and completion checks
- source links from rules to traces
- held-out and counterfactual workflow tests
- failure-driven repair fixtures
- explicit escape paths for novel cases

Implementability score: 0.72

### Test research agents in inherited workspaces

Summary: ARE-bench replays real researcher sessions and complete in-progress workspaces to the exact request boundary. Models that passed about 69 percent under immediate-contract grading fell to 28.4 to 40.0 percent when historical and material workspace requirements were included.

Analysis: [Daily analysis](2026-11-12/reasoning.md#2-test-research-agents-in-inherited-workspaces)

Core source: [ARE-bench paper v1](https://arxiv.org/abs/2611.14364v1)

Implementable now:
- request-boundary workspace snapshots
- stale and failed artifacts in test fixtures
- separate current, historical, material, and norm checklists
- critical-item pass gates
- clean-room versus inherited-state comparisons

Implementability score: 0.79

## Current working model

1. Use agents for variable and novel paths.
2. Compile stable recurring behavior into evidence-linked deterministic workflows.
3. Preserve an escape path when inputs exceed the compiled contract.
4. Evaluate agents and workflows inside inherited project state.
5. Grade critical historical constraints separately from immediate task completion.

## Browse

- [Latest roundup](../roundups/2026-11-12.md)
- [Latest dated analysis](2026-11-12/reasoning.md)
- [Friday synthesis](2026-11-06/reasoning.md)
- [Decision-state compilation](decision-state-compilation/decision-state-compilation.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
- [Agent serving runtime](agent-serving-runtime/agent-serving-runtime.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Evidence-linked memory](evidence-linked-memory/evidence-linked-memory.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Skills as control](skills-as-control/skills-as-control.md)
- [Multi-agent orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
