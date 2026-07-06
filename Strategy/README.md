# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-06

### Oversight should constrain the substrate, not inspect unconstrained work

Summary: Steerability via constraints moves coding-agent oversight into the workspace substrate. Constrained files, network, dependencies, docs, type checks, architecture checks, and deterministic inspection tools make bad work harder to produce and easier to catch.

Analysis: [daily sovereignty analysis](2026-07-06/sovereignty.md#oversight-should-constrain-the-substrate-not-inspect-unconstrained-work)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Execution Control Plane](agent-execution-control-plane/agent-execution-control-plane.md), [AgenticAI Coding Agent Control Plane](../AgenticAI/coding-agent-control-plane/coding-agent-control-plane.md), [AgenticAI Agent Static Analysis](../AgenticAI/agent-static-analysis/agent-static-analysis.md)
Core source: [Steerability via constraints](https://arxiv.org/abs/2607.02389v1)
Implementable now:
- treat workspace constraints as governance controls
- default coding agents to least-privilege file, network, package, and command surfaces
- compile conventions into linters, type checks, architecture checks, and protected-path rules
- give reviewer agents deterministic repo-inspection tools and local docs
Tools, repos, and methodologies worth exploring:
- OPA or Cedar policy, protected paths, architecture tests, repo-local docs CLIs, security fixtures with inserted flaws
Implementability score: 0.74

### Approved enterprise tasks should compile into budgeted database sessions

Summary: SessionBound turns enterprise approval into short-lived, budgeted, auditable database sessions. Signed task tokens bind safe views, row scope, denied fields, operation limits, query budgets, disclosure budgets, and receipts before agent-generated SQL executes.

Analysis: [daily sovereignty analysis](2026-07-06/sovereignty.md#approved-enterprise-tasks-should-compile-into-budgeted-database-sessions)
Durable topics: [Agent Execution Control Plane](agent-execution-control-plane/agent-execution-control-plane.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core sources: [SessionBound paper](https://arxiv.org/abs/2607.00751v1), [SessionBound repo](https://github.com/SessionBound/sessionbound)
Implementable now:
- define task templates before agents touch data
- bind approval to principal, task, data scope, operation class, query budget, disclosure budget, expiry, and receipt sink
- enforce row, column, operation, and budget limits at the database or gateway runtime
- log denied queries as audit evidence
Tools, repos, and methodologies worth exploring:
- SessionBound reference repo, database views, row-level security, column masking, signed task tokens, receipts
Implementability score: 0.61

### Skill rubrics are governance evidence, not only training signals

Summary: SkillCoach implies that skill registries should store process verdicts. A platform should know whether a skill was selected correctly, followed correctly, composed safely, and verified before final submission. Passing the final task is not enough.

Analysis: [daily sovereignty analysis](2026-07-06/sovereignty.md#skill-rubrics-are-governance-evidence-not-only-training-signals)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Community Governance](agent-community-governance/agent-community-governance.md), [AgenticAI Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md)
Core source: [SkillCoach](https://arxiv.org/abs/2607.01874v1)
Implementable now:
- add process-rubric scores to skill registry records
- separate final verifier success from skill-use quality
- track distractor skill selection and omitted validation checks as registry health metrics
- quarantine, rewrite, or retire skills that repeatedly fail process rubrics
Tools, repos, and methodologies worth exploring:
- SkillCoach-style rubrics, registry utility dashboards, trace queries over skill hash and validator outcomes
Implementability score: 0.66

### Verification gates are conversational memory policy for code

Summary: Multi-turn coding chat creates commitments. Regression Accumulation shows those commitments need to become executable tests or invariants, because later turns can satisfy the newest request while breaking earlier requirements.

Analysis: [daily sovereignty analysis](2026-07-06/sovereignty.md#verification-gates-are-conversational-memory-policy-for-code)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md), [AgenticAI Coding Agent Control Plane](../AgenticAI/coding-agent-control-plane/coding-agent-control-plane.md)
Core sources: [Regression Accumulation](https://arxiv.org/abs/2607.01855v1), [artifact repository](https://anonymous.4open.science/r/multi-turn-llm-regression-E73E)
Implementable now:
- convert accepted requirements into tests, assertions, or invariant checks
- preserve checks across turns and subagent handoffs
- rollback changes that break prior commitments
- store regression evidence in traces and PR history
Tools, repos, and methodologies worth exploring:
- Verification Gate policy, turn-indexed requirement ledgers, patch-stack rollback, multi-turn regression taxonomy
Implementability score: 0.79

## Supporting recent Strategy context

The 2026-07-01 Deep Dive remains the foundation: connection is not authority. The 2026-07-06 scan extends that rule from tool connections to process authority. Skills, coding sessions, workspace constraints, and database sessions should all become policy-bearing evidence objects before they influence real effects.
