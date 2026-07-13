# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-13

### CLI coding-agent failures need three timestamps, not one verdict

Summary: A study of 1,794 complete CLI coding-agent trajectories separates the decisive error, empirical lock-in, and first observable symptom. The median failed run starts the decisive error chain at step 7, loses observed recoverability at step 12, and surfaces at step 16, while 28% of failures never surface externally.

Analysis: [daily reasoning analysis](2026-07-13/reasoning.md#cli-coding-agent-failures-need-three-timestamps-not-one-verdict)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [Failure as a Process](https://arxiv.org/abs/2607.09510v1), [replication package](https://github.com/xz-Sean/cli_trajectory_analysis)
Implementable now:
- add `t_err`, `t_lock`, and `t_obs` to failed-run reviews
- run prefix checks after task interpretation, first edit, first test, and before commit
- preserve task requirements with the trace so specification-relative failures are detectable
Tools, repositories, and methodologies worth exploring:
- `xz-Sean/cli_trajectory_analysis`, Terminal-Bench, OpenHands, MiniSWE, Terminus2, prefix monitors
Implementability score: 0.80

### Selective memory should preserve configuration and discard old reasoning traces

Summary: The architecture persists task specifications, data schemas, tool configurations, and output constraints while keeping old reasoning traces out of the next active context. It also versions artifacts in Git, isolates drafts, applies workspace RBAC, and binds fresh runtime data without another model call.

Analysis: [daily reasoning analysis](2026-07-13/reasoning.md#selective-memory-should-preserve-configuration-and-discard-old-reasoning-traces)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [Shared Selective Persistent Memory for Agentic LLM Systems](https://arxiv.org/abs/2607.09493v1)
Implementable now:
- store task rules, schemas, tool manifests, and output contracts as typed durable objects
- keep episodes as evidence and require explicit promotion into active memory
- separate generated logic from runtime data and version artifacts with promoted memory
Tools, repositories, and methodologies worth exploring:
- Git-backed artifacts, typed memory records, RBAC, event-sourced promotion, no-memory/full-history/selective-memory ablations
Implementability score: 0.68

### Property templates make AI-written tests prove and execute the same intent

Summary: One typed property template produces both a Lean 4 proof and an executable property-based test. The proof checks the formal model, the test checks the real implementation, and disagreement exposes a model-to-runtime gap.

Analysis: [daily reasoning analysis](2026-07-13/reasoning.md#property-templates-make-ai-written-tests-prove-and-execute-the-same-intent)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [Agentic Proof and Property-Based Testing via Property-Templates](https://arxiv.org/abs/2607.09072v1), [browsable artifact](https://anonymous.4open.science/r/AgentLeanDiscprop-1597/)
Implementable now:
- define one recurring invariant as a template with typed holes
- generate a machine-checked proof and a property-based test from the same claim
- preserve proof/test disagreements as first-class defects
Tools, repositories, and methodologies worth exploring:
- Lean 4, Hypothesis, PySpark, property cards, dual verification, the anonymous artifact
Implementability score: 0.72

## Supporting recent AgenticAI context

The July 13 scan moves reliability earlier in the run and lower in the stack. Final outcomes remain useful, but the implementable control points are now failure-stage timestamps, typed memory promotion, and shared proof/test intent artifacts.
