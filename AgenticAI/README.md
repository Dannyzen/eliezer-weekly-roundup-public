# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-06

### Skill use needs process rubrics, not final verifier wins

Summary: SkillCoach shows that final task success is too coarse for skill-using agents. A trajectory can pass after selecting distractor skills, skipping required steps, composing workflows incorrectly, or omitting final checks. Skill quality needs process rubrics for selection, following, composition, and reflection.

Analysis: [daily reasoning analysis](2026-07-06/reasoning.md#skill-use-needs-process-rubrics-not-final-verifier-wins)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [SkillCoach](https://arxiv.org/abs/2607.01874v1)
Implementable now:
- log retrieved skill IDs, loaded body hashes, selected skills, rejected skills, validation checks, and final verifier results
- score skill selection, following, composition, and reflection separately
- keep final success as outcome evidence, not a proxy for process quality
- evolve rubrics from real rollouts, then review rubric changes before they become gates
Tools, repos, and methodologies worth exploring:
- SkillCoach-style rubrics, per-skill validators, registry dashboards for distractor selection and omitted checks
Implementability score: 0.70

### Multi-turn coding agents need regression gates

Summary: Regression Accumulation shows that coding chat reliability is stateful. Across six models on 8-turn requirement-evolution chains, 40 to 73 percent of tasks lose previously correct behavior. The robust mitigation is Verification Gate: replay earlier tests on every later turn, then rollback and retry when old behavior breaks.

Analysis: [daily reasoning analysis](2026-07-06/reasoning.md#multi-turn-coding-agents-need-regression-gates)
Durable topics: [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Sessionful Agent Loops](sessionful-agent-loops/sessionful-agent-loops.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [Regression Accumulation](https://arxiv.org/abs/2607.01855v1), [artifact repository](https://anonymous.4open.science/r/multi-turn-llm-regression-E73E), [bug taxonomy](https://anonymous.4open.science/r/multiturn-code-bugs)
Implementable now:
- store accepted requirements as session contracts
- convert prior requirements into replayable tests or invariants
- run prior tests plus new tests on every turn
- rollback and retry when prior behavior fails
- record the turn that introduced each regression and the gate that caught it
Tools, repos, and methodologies worth exploring:
- Verification Gate policy, turn-indexed requirement ledgers, patch-stack rollback, multi-turn regression taxonomies
Implementability score: 0.84

### Coding-agent steerability belongs in the substrate

Summary: Steerability via constraints argues that coding agents should be governed by the engineering substrate: access control, network policy, typed boundaries, strict conventions, layered docs, and deterministic tools. In a controlled backdoor-review experiment, constrained substrate plus a small docs CLI improved reviewer recall from 54.5 percent to 90.9 percent.

Analysis: [daily reasoning analysis](2026-07-06/reasoning.md#coding-agent-steerability-belongs-in-the-substrate)
Durable topics: [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Agent Static Analysis](agent-static-analysis/agent-static-analysis.md), [Strategy Runtime Governance](../Strategy/runtime-governance/runtime-governance.md)
Core source: [Steerability via constraints](https://arxiv.org/abs/2607.02389v1)
Implementable now:
- default coding agents into constrained workspaces
- enforce style, type, dependency, and architecture constraints with tools
- maintain repo-local docs and code-map surfaces for reviewer agents
- compare reviewer quality under constrained and unconstrained substrates
Tools, repos, and methodologies worth exploring:
- linters, type checkers, protected paths, network-deny defaults, architecture tests, local docs CLI surfaces
Implementability score: 0.78

## Supporting recent AgenticAI context

The 2026-07-05 scan added selective state: memory influence, reasoning budget, test evolution, and skill composition need evidence gates. The 2026-07-06 scan adds process preservation: the agent stack has to prove that skills, code changes, and oversight paths preserved the right commitments before granting more authority.
