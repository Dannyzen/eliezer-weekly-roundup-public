# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Daily addendum: 2026-10-31

### Make verification an evidence-gathering agent, then certify the test environment

Summary: verify persisted outcomes through bounded exploration, and prove the evaluation mutation, observation path, feasibility, and scorer before blaming the model.

Analysis: [Daily analysis](2026-10-31/reasoning.md#1-make-verification-an-evidence-gathering-agent-then-certify-the-test-environment)

Core sources: [VeriCUA](https://arxiv.org/abs/2610.40578v1), [EnvOS](https://arxiv.org/abs/2610.40246v1)

Implementable now:
- requirement-level evidence rubrics
- GUI plus persisted-state checks
- explicit abstention
- pre-run intervention and scorer certification
- separate authoritative-state and model-observation logs

Implementability score: 0.86

### Keep episodic and relational memory as complementary projections

Summary: preserve narrative sequence and compact relationships in separate source-linked projections, then consolidate offline rather than rewriting canonical history.

Analysis: [Daily analysis](2026-10-31/reasoning.md#2-keep-episodic-and-relational-memory-as-complementary-projections)

Core source: [Long-Term Agent Memory through Complementary Curation and Consolidation](https://arxiv.org/abs/2610.39790v1)

Implementable now:
- canonical event log
- episodic and relational projections
- shared retrieval budget
- versioned asynchronous consolidation
- contradiction and supersession tests

Implementability score: 0.74

## Latest structured week: 2026-10-30

### Gate tool calls before execution and grade every executable prefix

Summary: validate current environment state before dispatch, then score the whole trajectory for schema validity, state preconditions, dependencies, recovery, and final success.

Analysis: [Weekly analysis](2026-10-30/reasoning.md#1-gate-tool-calls-before-execution-and-grade-every-executable-prefix)

Core sources: [StateMirror](https://arxiv.org/abs/2610.32648v1), [Prefix Executability](https://arxiv.org/abs/2610.40444v1)

Implementable now:
- JSON Schema or Pydantic tool validation
- environment-state predicates
- append-only trajectory events
- first-error depth and prefix-survival metrics

Implementability score: 0.88

### Fault-inject the harness and test the full work arc

Summary: model scale does not substitute for a resilient harness, and one-shot success hides inherited defects across evolving work.

Analysis: [Weekly analysis](2026-10-30/reasoning.md#2-fault-inject-the-harness-and-test-the-full-work-arc)

Core sources: [MCP fault study](https://arxiv.org/abs/2610.32555v1), [FeatureArc](https://arxiv.org/abs/2610.37434v1), [REGATTA](https://arxiv.org/abs/2610.30924v1)

Implementable now:
- seeded MCP fault campaigns
- model-harness release matrices
- multi-stage regression fixtures
- fault detection and recovery scoring

Implementability score: 0.87

### Compile evidence into decision state, then preserve it across handoffs

Summary: retrieving facts is insufficient. Long-running work needs a source-linked projection of governing state plus typed handoffs for decisions, constraints, effects, open scopes, and verification status.

Analysis: [Weekly analysis](2026-10-30/reasoning.md#3-compile-evidence-into-decision-state-then-preserve-it-across-handoffs)

Core sources: [SciValidityBench](https://arxiv.org/abs/2610.34767v1), [HSC-Bench](https://arxiv.org/abs/2610.36523v1), [Spine](https://arxiv.org/abs/2610.37224v1)

Implementable now:
- source-linked decision-state projections
- structured handoff schemas
- nested work scopes with immutable completion results
- counterfactual state tests

Implementability score: 0.80

### Test generated tests for behavioral adequacy

Summary: passing generated tests are weak release evidence unless they reject seeded wrong implementations and cover the requirement's observable behavior.

Analysis: [Weekly analysis](2026-10-30/reasoning.md#4-test-generated-tests-for-behavioral-adequacy)

Core source: [Req2Test-Bench](https://arxiv.org/abs/2610.36584v1)

Implementable now:
- mutation testing
- requirement-to-behavior maps
- independent release oracles
- kill-completeness gates

Implementability score: 0.81

## Current working model

1. Compile current state before choosing an action.
2. Validate the action before dispatch.
3. Verify persisted outcomes against explicit requirements.
4. Certify dynamic test environments before attributing failures.
5. Preserve source evidence and derive fit-for-purpose memory projections.
6. Grade the full work arc and preserve state across handoffs.

## Browse

- [Daily roundup](../roundups/2026-10-31.md)
- [Latest dated analysis](2026-10-31/reasoning.md)
- [Weekly synthesis](../roundups/2026-10-30.md)
- [Decision-state compilation](decision-state-compilation/decision-state-compilation.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Skills as control](skills-as-control/skills-as-control.md)
- [Multi-agent orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
