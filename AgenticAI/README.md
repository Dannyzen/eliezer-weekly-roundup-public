# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-26

### Coding-agent configs need a deterministic control plane

Summary: A repo-scale study argues that coding-agent rules files, IDE markdown, and agent definitions are propagating like undeclared dependencies. The fix is to treat agent configuration as a managed control-plane artifact: content-addressed, permission-bearing, compiled to client targets, and checked for drift.

Analysis: [daily reasoning analysis](2026-06-26/reasoning.md#coding-agent-configs-need-a-deterministic-control-plane)
Durable topics: [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Skills as Control](skills-as-control/skills-as-control.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [A Deterministic Control Plane for LLM Coding Agents](https://arxiv.org/abs/2606.26924v1)
Implementable now:
- hash and lock repo-local agent configuration
- require permission declarations for shell, file, network, and memory authority
- compile one canonical agent definition into client-specific files
- log config hash, target client, permission profile, and drift verdict with each run
Tools, repos, and methodologies worth exploring:
- git-backed config registries, SHA-256 lockfiles, CI config linters, OpenTelemetry spans, policy-as-code, replay packs
Implementability score: 0.64

### MIRROR makes agentic RAG red-teaming cross-surface and novelty-aware

Summary: MIRROR uses memory-guided MCTS plus a deterministic novelty gate to red-team multimodal agentic RAG across text poisoning, image injection, direct-query attacks, and orchestrator-level tool manipulation. The useful correction is that red-team systems must report novelty and duplicate rates, not just attack success.

Analysis: [daily reasoning analysis](2026-06-26/reasoning.md#mirror-makes-agentic-rag-red-teaming-cross-surface-and-novelty-aware)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Agentic Search and Retrieval](agentic-search/agentic-search.md)
Core source: [MIRROR paper](https://arxiv.org/abs/2606.26793v1)
Implementation artifact: [FujitsuResearch/mirror](https://github.com/FujitsuResearch/mirror)
Implementable now:
- add novelty gates to prompt-injection and RAG-poisoning test suites
- red-team retrieval context, image payloads, direct queries, and tool selection together
- report duplicate rates, attack success, novelty-adjusted success, query cost, and cross-surface variance separately
Tools, repos, and methodologies worth exploring:
- MIRROR novelty gate, memory-guided PUCT search, DupBench-style diagnostics, payload-free public artifact patterns
Implementability score: 0.72
