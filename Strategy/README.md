# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-07-02

### Theoria makes informal reasoning auditable through licensed state transitions

Summary: Theoria rewrites answers into typed reasoning-state transitions, and every transition must be licensed by a citation, computation, or problem-given fact. The strategic primitive is completeness of change: hidden premises become unlicensed mutations instead of passing through a scalar LLM judge.

Analysis: [daily sovereignty analysis](2026-07-02/sovereignty.md#theoria-makes-informal-reasoning-auditable-through-licensed-state-transitions)
Durable topics: [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md), [Agent Execution Control Plane](agent-execution-control-plane/agent-execution-control-plane.md)
Core sources: [Theoria paper](https://arxiv.org/abs/2607.01223v1), [Theoria repository](https://github.com/zaladbar/theoria)
Implementable now:
- represent high-risk reasoning as state transitions
- require each transition to name its license type and evidence ID
- diff consecutive states for unlicensed mutations
- add hidden-premise, fabricated-citation, stale-source, and unsupported-memory-update fixtures
Tools, repos, and methodologies worth exploring:
- Theoria, typed proof-state schemas, verifier spans, JSONL transition ledgers, citation and computation license fields
Implementability score: 0.56

### Agent skill supply chains are authority graphs

Summary: Skills Are Not Islands shows that skills are not isolated markdown files. They are dependency-bearing artifacts with skill, package, and service edges. Governance has to see the transitive graph before a skill can influence privileged tools, memory, browser sessions, repositories, or external services.

Analysis: [daily sovereignty analysis](2026-07-02/sovereignty.md#agent-skill-supply-chains-are-authority-graphs-not-markdown-folders)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Agent Execution Control Plane](agent-execution-control-plane/agent-execution-control-plane.md), [AgenticAI Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md)
Core source: [Skills Are Not Islands](https://arxiv.org/abs/2607.01136v1)
Implementable now:
- require skill manifests and lockfiles before production admission
- include skill, package, service, tool, credential, browser, memory, and repository authority in the dependency graph
- add CI review when a skill dependency graph changes
- emit runtime risk warnings for transitive shell, network, credential, and external-service authority
Tools, repos, and methodologies worth exploring:
- skill SBOMs, lockfiles, dependency-cluster management, risk-warning audit commands, transitive authority review
Implementability score: 0.73

### Benchmark scores should be admissible evidence packets

Summary: RepoRescue and the performance benchmark audit show that coding-agent benchmark scores need governance fields. A score should say what was editable, whether test edits were blocked, whether source-only replay passed, which machine profile ran the benchmark, which scoring rule applied, and how much each task contributed.

Analysis: [daily sovereignty analysis](2026-07-02/sovereignty.md#coding-agent-benchmark-governance-needs-source-only-and-replayable-score-rules)
Adjacent topics: [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md), [Runtime Governance](runtime-governance/runtime-governance.md), [AgenticAI Agent Harness Architecture](../AgenticAI/agent-harness-architecture/agent-harness-architecture.md)
Core sources: [RepoRescue](https://arxiv.org/abs/2607.01213v1), [performance benchmark audit](https://arxiv.org/abs/2607.01211v1)
Implementable now:
- treat benchmark submissions as evidence packets
- attach edit scope, replay environment, scoring rule, variance, and source-only status
- reject benchmark claims that cannot expose admissibility fields
Tools, repos, and methodologies worth exploring:
- source-only replay, patch-scope ledgers, cross-machine performance replays, per-task score audits
Implementability score: 0.82

## Supporting recent Strategy context

The 2026-07-01 deep dive remains the control-plane foundation: connection is not authority, and privileged actions need execution-control objects. The 2026-07-02 scan adds the proof-artifact layer above that foundation. Reasoning transitions, skill dependency graphs, and benchmark scores now need licenses, manifests, replay fields, and policy-visible evidence before they become trusted inputs to an agent runtime.
