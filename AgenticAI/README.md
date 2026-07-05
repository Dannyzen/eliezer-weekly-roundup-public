# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-05

### Memory systems need failure-mode tests, not only recall tests

Summary: MemSyco-Bench and A-TMA show that memory evals must measure downstream decision influence, not only recall. The system has to know when to ignore preference memory, when external evidence wins, and whether a recalled fact is current, historical, transition, conflicting, or scoped personalization.

Analysis: [daily reasoning analysis](2026-07-05/reasoning.md#memory-systems-need-failure-mode-tests-not-only-recall-tests)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Context Economy](context-economy/context-economy.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Strategy Memory Authority](../Strategy/memory-authority-control-plane/memory-authority-control-plane.md)
Core sources: [MemSyco-Bench paper](https://arxiv.org/abs/2607.01071v2), [MemSyco-Bench repo](https://github.com/XMUDeepLIT/MemSyco-Bench), [A-TMA](https://arxiv.org/abs/2607.01935v1)
Implementable now:
- run memory tests where the right behavior is to ignore, scope, or override a recalled memory
- tag memory packets with current, superseded, historical, transition, conflict, and personalization-only state
- evaluate bank maintenance, retrieval, and answer-time resolution separately
- preserve source event and supersession lineage through summaries and derived memories
Tools, repos, and methodologies worth exploring:
- XMUDeepLIT/MemSyco-Bench, ATMA-style state labels, conflict-heavy temporal fixtures, Graphiti-style temporal memory with explicit state roles
Implementability score: 0.76

### Reasoning budgets should be routed before extra tools

Summary: A 90-run coding-agent study found that browser-based testing increased cost without improving reliability, while higher reasoning effort sharply improved first-try perfect runs. The practical routing rule is to classify the failure first, then buy the cheapest knob that addresses it.

Analysis: [daily reasoning analysis](2026-07-05/reasoning.md#reasoning-budgets-should-be-routed-before-extra-tools)
Durable topics: [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Agent Serving Runtime](agent-serving-runtime/agent-serving-runtime.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Strategy Model Router Governance](../Strategy/model-router-governance/model-router-governance.md)
Core sources: [reasoning effort study](https://arxiv.org/abs/2607.02436v1), [Zenodo artifacts](https://doi.org/10.5281/zenodo.21134406)
Implementable now:
- log reasoning effort, tool exposure, per-criterion failures, cost, corrective prompts, and first-run pass status
- raise reasoning effort before broadening tool access when planning and integration failures dominate
- keep browser tools targeted to UI-visible or browser-state defects
- evaluate design prompts separately from functional correctness
Tools, repos, and methodologies worth exploring:
- the Zenodo retrospective-board artifact set, first-try perfect-run metrics, matched A/B harness runs, router policies over reasoning effort versus tool exposure
Implementability score: 0.81

### Live test co-evolution benchmarks expose coding-agent regressions

Summary: TestEvo-Bench evaluates whether agents update tests with code, using executable tasks mined from real repository histories. Prompt Coverage Adequacy adds the metric pressure: tests should cover the requirements in the prompt, not only lines in the code.

Analysis: [daily reasoning analysis](2026-07-05/reasoning.md#live-test-co-evolution-benchmarks-expose-coding-agent-regressions)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md)
Core sources: [TestEvo-Bench](https://arxiv.org/abs/2607.02469v1), [TestEvo-Bench site](https://www.testevo-bench.com/), [Prompt Coverage Adequacy](https://arxiv.org/abs/2607.02057v1)
Implementable now:
- mine internal code-plus-test evolution tasks
- score test generation and test update separately
- record task timestamps to reduce training-cutoff leakage
- add prompt or requirement coverage checks for agent-authored tests
Tools, repos, and methodologies worth exploring:
- TestEvo-Bench's live benchmark methodology, mutation testing, prompt coverage metrics, post-cutoff internal regression packs
Implementability score: 0.68

### Skill composition needs fuzzing before marketplace admission

Summary: SkillFuzz shows that individually benign skills can compose into implicit intents. Skill catalogs need composition tests, planner diffs, and registry-level verdicts before co-activated skills inherit production authority.

Analysis: [daily reasoning analysis](2026-07-05/reasoning.md#skill-composition-needs-fuzzing-before-marketplace-admission)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Strategy Agent Gateway Governance](../Strategy/agent-gateway-governance/agent-gateway-governance.md), [Strategy Runtime Governance](../Strategy/runtime-governance/runtime-governance.md)
Core source: [SkillFuzz](https://arxiv.org/abs/2607.02345v1)
Implementable now:
- extract skill contracts with purpose, preconditions, side effects, and scopes
- compare plans with and without composed skill sets
- prioritize risky combinations with contract-guided search
- store composition verdicts alongside individual skill verdicts
Tools, repos, and methodologies worth exploring:
- contract-guided fuzzing, differential planning oracles, Monte Carlo Tree Search over co-activation graphs, composition deny lists
Implementability score: 0.62

## Supporting recent AgenticAI context

The 2026-07-04 daily scan added preflight control: static agent graphs, proxy evals, permission harnesses, and skill detonation. The 2026-07-05 scan adds the state layer underneath that: memory state, reasoning budget, test evolution, and skill composition all need explicit evidence before the runtime grants more authority.
