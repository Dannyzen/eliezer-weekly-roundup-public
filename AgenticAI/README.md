# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-23

### GroundEval makes evidence-path evaluation deterministic

Summary: GroundEval replaces LLM-as-judge scoring for stateful agents with deterministic checks over what the agent searched, fetched, cited, and was allowed to access. It catches plausible answers that are not supported by the actual trace.

Analysis: [daily reasoning analysis](2026-06-23/reasoning.md#groundeval-makes-evidence-path-evaluation-deterministic)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Evidence Provenance Control Plane](../Strategy/evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core source: [GroundEval](https://arxiv.org/abs/2606.22737v1)
Implementable now:
- add `source_id`, `raw_output_ref`, `retrieval_time`, and `access_scope` fields to agent traces
- fail evaluation when a final answer depends on an artifact absent from the trace
- build silence, perspective, and counterfactual tests before relying on judge models
Tools, repos, and methodologies worth exploring:
- JSONL/OpenTelemetry trace exports, deterministic evidence-path evaluators, source-aware claim checks, access-scope tests, absence-claim regression suites
Implementability score: 0.84

### RigorBench measures coding-agent process discipline

Summary: RigorBench scores autonomous coding agents on planning, verification, recovery, abstention, and atomic step integrity, not only whether the final patch passes. It gives teams a rubric for catching reckless successful runs.

Analysis: [daily reasoning analysis](2026-06-23/reasoning.md#rigorbench-measures-how-coding-agents-work-not-only-whether-they-pass)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Skills as Control](skills-as-control/skills-as-control.md)
Core source: [RigorBench](https://arxiv.org/abs/2606.22678v1)
Implementable now:
- add process-rubric checks to coding-agent replay suites
- require explicit plans before non-trivial mutations
- score verification coverage, recovery behavior, doom loops, and abstention quality
Tools, repos, and methodologies worth exploring:
- RigorBench-style rubrics, coding-agent trajectory analysis, CI evidence gates, plan-before-mutation checks, agent-authored-diff review policy
Implementability score: 0.74
