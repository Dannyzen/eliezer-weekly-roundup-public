# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-08

The implementation signal is to move control out of prompts and into measurable harness contracts for time, concurrency, reusable skills, and memory.

### Measure time control in native harnesses

Summary: AgentTime evaluates duration following, runtime forecasting, and retrospective time estimates across 222 tasks from 18 benchmark families. Performance varies sharply by agent, and on-time completion can conceal idle waiting.

Analysis: [dated analysis](2026-10-08/reasoning.md#measure-time-control-in-native-harnesses)
Durable topic: [Sessionful Agent Loops](sessionful-agent-loops/sessionful-agent-loops.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.09944v1), [repository](https://github.com/michaelofengenden/agenttimebench), [transcript dataset](https://huggingface.co/datasets/mofengenden/agenttime-transcripts)
Tools and methodologies worth exploring now: runtime telemetry, scheduler-owned deadlines, active-versus-idle accounting, cancellation, native task graders, timing regression tests
Implementability score: 0.90

### Enable dynamic concurrency selectively

Summary: Across 2,124 coding-agent trajectories, dynamic concurrency did not consistently improve task success and increased mean runtime in 14 of 15 agent-benchmark combinations. Benefits concentrated in difficult, decomposable, long-horizon tasks.

Analysis: [dated analysis](2026-10-08/reasoning.md#enable-dynamic-concurrency-selectively)
Durable topic: [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.10263v1), [trajectory artifact](https://github.com/schwerli/Concurrency-Failures-Trajectory-Artifact)
Tools and methodologies worth exploring now: selective delegation, single-writer ownership, join deadlines, result contracts, parent-owned integration gates, concurrent-versus-sequential bakeoffs
Implementability score: 0.86

### Admit skills through synthesized paired tests

Summary: SkillSandbox creates a novel executable scenario for each skill, then compares executions with and without it. After 500 downstream tasks, 17% to 32% of skills remained unexercised and 45% to 56% lacked five execution opportunities.

Analysis: [dated analysis](2026-10-08/reasoning.md#admit-skills-through-synthesized-paired-tests)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.10088v1), [implementation snapshot](https://anonymous.4open.science/r/skillsandbox-647C/)
Tools and methodologies worth exploring now: synthesized positive and boundary scenarios, paired runs, effect oracles, Keep or Reject receipts, versioned skill lineage
Implementability score: 0.74

### Ground memory in stable artifact identities

Summary: ExperienceIndex stores single-artifact and artifact-pair experience from prior traces. Across seven datasets it reports up to 11.0 points better answer quality and up to 50.5% lower online cost.

Analysis: [dated analysis](2026-10-08/reasoning.md#ground-memory-in-stable-artifact-identities)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [paper v1](https://arxiv.org/abs/2610.10091v1)
Tools and methodologies worth exploring now: stable artifact IDs, source versions, single-artifact claims, pair relations, lineage-aware retrieval, staleness and contradiction tests
Implementability score: 0.65

## Current implication

Treat model outputs as proposals to a harness that owns time, work allocation, skill admission, and memory provenance. The highest leverage comes from adding external contracts before adding more autonomous behavior.

Latest roundup: [2026-10-08](../roundups/2026-10-08.md).
