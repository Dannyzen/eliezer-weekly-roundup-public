# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-10

### Executable harness contracts move guarantees out of prompts

Summary: From Prompts to Contracts moves source scope, entity routing, trace hygiene, output shape, and recommendation rules into code-owned manifests and validators around a replaceable model boundary. The paper reports that its contract checks held across 270 runs and three hosted models. Prompt-only enforcement leaked violations, while the integrated harness preserved 120/120 utility.

Analysis: [daily reasoning analysis](2026-07-10/reasoning.md#executable-harness-contracts-move-guarantees-out-of-prompts)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [From Prompts to Contracts](https://arxiv.org/abs/2607.08028v1), [enterprise-llm-agent-harness](https://github.com/hammerbaki/enterprise-llm-agent-harness)
Implementable now:
- put load-bearing runtime behavior in schemas and validators outside the model
- add deliberate contract violations as fault-injection fixtures
- rerun a fixed contract pack across model, prompt, retrieval, and scaffold changes
Tools, repos, and methodologies worth exploring:
- `hammerbaki/enterprise-llm-agent-harness`, JSON Schema or Pydantic, deterministic fallbacks, OpenTelemetry-style run manifests
Implementability score: 0.90

### UniClawBench makes framework choice measurable

Summary: UniClawBench packages 400 bilingual tasks in live containers around skill use, exploration, long-context reasoning, multimodal understanding, and cross-platform coordination. Hidden supervisors, user simulation, checkpoint grading, and cross-framework comparisons make the deployed agent system, not only the base model, the evaluation unit.

Analysis: [daily reasoning analysis](2026-07-10/reasoning.md#uniclawbench-makes-the-framework-part-of-the-eval-unit)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [UniClawBench paper](https://arxiv.org/abs/2607.08768v1), [UniClawBench repository](https://github.com/HKU-MMLab/UniClawBench)
Implementable now:
- build a small internal capability pack with live task worlds and hidden checkpoints
- hold the model fixed while comparing two harnesses
- score first-pass completion, recovery, final artifact state, cost, and wall time separately
Tools, repos, and methodologies worth exploring:
- `HKU-MMLab/UniClawBench`, Docker or VM snapshots, hidden verifier services, cross-framework A/B runs
Implementability score: 0.85

### Selective memory intervention beats continuous injection

Summary: Remember When It Matters runs a sidecar memory agent that decides whether grounded execution state should enter the next action context or whether it should remain silent. The paper reports gains on Terminal-Bench 2.0 and tau2-Bench, with selective intervention outperforming passive and always-on variants.

Analysis: [daily reasoning analysis](2026-07-10/reasoning.md#proactive-memory-turns-recall-into-a-selective-intervention-policy)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core sources: [Remember When It Matters](https://arxiv.org/abs/2607.08716v1), [advertised proactive-memory-agent repository](https://github.com/yifannnwu/proactive-memory-agent)
Implementable now:
- maintain typed records for requirements, failed attempts, diagnoses, and open subgoals
- add explicit `inject` and `remain_silent` decisions before action-agent calls
- compare no-memory, passive, always-on, and selective variants on identical trajectories
Tools, repos, and methodologies worth exploring:
- typed memory packets, intervention-effect logs, Terminal-Bench-style fixtures, small classifier or rules-based memory gates
Artifact caveat: the advertised repository had no populated default branch during this scan.
Implementability score: 0.65

## Supporting recent AgenticAI context

The 2026-07-09 scan made trajectory severity and causal slicing operational. The 2026-07-10 scan adds the control surfaces that should consume that evidence: executable contracts, framework-aware benchmark packs, and abstaining memory intervention.
