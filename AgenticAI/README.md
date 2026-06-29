# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-29

### Repository-level risk means coding-agent evals have to measure the repo

Summary: Agent-authored pull requests can pass local task checks while the repository accumulates integration friction. The repository, not the individual agent, should become the measurement unit for merge delay, review churn, conflict rate, CI retries, rollbacks, and post-merge defects.

Analysis: [daily reasoning analysis](2026-06-29/reasoning.md#repository-level-risk-means-coding-agent-evals-have-to-measure-the-repo)
Durable topics: [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [Govern the Repository, Not the Agent](https://arxiv.org/abs/2606.28235v1)
Implementable now:
- bind agent run IDs and config hashes to PRs, commits, reviews, CI, and rollbacks
- track repository-level integration friction rather than only task pass rate
- compare agent-authored and human-authored changes by repo and component
- use repo-level risk before expanding autonomy
Tools, repos, and methodologies worth exploring:
- GitHub PR metadata, merge queues, CODEOWNERS, branch protection, CI retry analysis, multilevel models, repository-risk dashboards
Implementability score: 0.70

### Verification-aware harnesses turn architecture work into a checked loop

Summary: NOVA shows the architecture-evolution version of an agent harness: the agent proposes, but verifier cascades check semantics, executability, offline metrics, production constraints, and high-risk handoff before a change advances.

Analysis: [daily reasoning analysis](2026-06-29/reasoning.md#verification-aware-harnesses-turn-agentic-architecture-work-into-a-checked-loop)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md)
Core source: [NOVA](https://arxiv.org/abs/2606.27243v2)
Implementable now:
- define allowed mutation classes for one architecture surface
- build a verifier cascade before promotion
- store proposal, diagnostics, metric delta, and decision for every attempt
- require human approval for high-risk architecture moves
Tools, repos, and methodologies worth exploring:
- project packs, offline-to-online gates, metric regression checks, compatibility checks, trajectory memory, human-attended promotion gates
Implementability score: 0.66

## Supporting recent AgenticAI context

The 2026-06-26 weekly synthesis remains the broadest current map: [weekly reasoning analysis](2026-06-26/reasoning.md). The 2026-06-28 daily scan tightened boundary objects. The new 2026-06-29 scan moves the implementation focus to repository-level coding-agent risk and verifier-owned harness loops.
