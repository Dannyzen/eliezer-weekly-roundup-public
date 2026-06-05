# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Week ending 2026-06-05

### Skills should be governed capability artifacts, not prompt decorations
Summary: Skills are becoming the procedural capability layer for agents. This week’s sources show the optimistic path, reusable verified skills, and the risk path, lifecycle attacks and permission failures. Treat skills as reviewed software artifacts, not context snippets.

Analysis: [weekly reasoning analysis](2026-06-05/reasoning.md#skills-should-be-governed-capability-artifacts-not-prompt-decorations)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core sources: [NVIDIA skills](https://github.com/NVIDIA/skills), [NVIDIA-Verified Agent Skills](https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/), [SkillHarm](https://arxiv.org/abs/2606.02540v1), [SkillGuard](https://arxiv.org/abs/2606.03024v1), [State-Grounded Dynamic Retrieval](https://arxiv.org/abs/2606.04391)
Implementable now:
- require a skill card with owner, version, hash, scope, permissions, tests, fixtures, and retirement criteria;
- gate skill loading by task fit, current state, access scope, and risk class;
- log retrieved, loaded, rejected, and executed skills with outcomes.
Tools, repos, and methodologies worth exploring:
- NVIDIA skills, SkillGuard-style permission manifests, state-grounded retrieval, Pydantic schemas, signed skill manifests, OpenTelemetry skill-selection traces
Implementability score: 0.80

### Agent evals need trajectory, process, state, and contamination evidence
Summary: Final-answer scoring is no longer enough. Agent evals now need traces, search logs, backend state, verifier outputs, process labels, repeated trials, and contamination controls.

Analysis: [weekly reasoning analysis](2026-06-05/reasoning.md#agent-evals-need-trajectory-process-state-and-contamination-evidence)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Agentic Search and Retrieval](agentic-search/agentic-search.md)
Core sources: [How Coding Agents Fail Their Users](https://arxiv.org/abs/2605.29442v1), [SoundnessBench](https://arxiv.org/abs/2605.30329v1), [AWS AgentCore dataset management](https://aws.amazon.com/blogs/machine-learning/build-a-test-suite-that-grows-with-your-agent-with-dataset-management-in-amazon-bedrock-agentcore/), [AutoLab](https://arxiv.org/abs/2606.05080), [Search-Time Contamination](https://arxiv.org/abs/2606.05241)
Implementable now:
- preserve tool traces, search queries, retrieved URLs, backend state, intermediate artifacts, and verifier outputs;
- run no-search, no-skill, wrong-skill, and repeated-trial baselines;
- score process quality, contamination, and final-state correctness separately.
Tools, repos, and methodologies worth exploring:
- OpenTelemetry traces, browser/search proxies, LangSmith datasets, Amazon Bedrock AgentCore, canary benchmark artifacts, artifact-loop benchmarks
Implementability score: 0.76

### Memory and context systems should preserve evidence before compressing it
Summary: Belief updates, retrieval, pruning, and compression are converging into one rule: preserve raw evidence and provenance before summarizing or shrinking context. Compression is useful only if originals remain auditable.

Analysis: [weekly reasoning analysis](2026-06-05/reasoning.md#memory-and-context-systems-should-preserve-evidence-before-compressing-it)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Context Economy](context-economy/context-economy.md)
Core sources: [BeliefTrack](https://arxiv.org/abs/2605.30219v1), [RHELM](https://arxiv.org/abs/2605.31086), [SPECTRA](https://arxiv.org/abs/2605.31575), [DMF](https://arxiv.org/abs/2606.03463v1), [Headroom](https://github.com/chopratejas/headroom)
Implementable now:
- preserve raw episodes, traces, and source evidence before promoting facts or summaries;
- classify memory decisions as stay, update, or isolate;
- test context compression against answer preservation and link compressed material back to original evidence IDs.
Tools, repos, and methodologies worth exploring:
- belief-state gates, deterministic retention/pruning, retrieval-oracle fixtures, Headroom, pgvector or local vector stores, answer-preservation regression suites
Implementability score: 0.79

### Multi-agent coding should be dependency-wave orchestration, not broadcast chat
Summary: More agents are not automatically better. This week’s multi-agent evidence points toward dependency DAGs, ready-wave dispatch, interface contracts, coherence checks, and process-quality scoring.

Analysis: [weekly reasoning analysis](2026-06-05/reasoning.md#multi-agent-coding-should-be-dependency-wave-orchestration-not-broadcast-chat)
Durable topic: [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
Core sources: [Locally Coherent, Globally Incoherent](https://arxiv.org/abs/2605.30335v1), [SPOQ](https://arxiv.org/abs/2606.03115v1), [AgentLens](https://arxiv.org/abs/2605.12925v3)
Implementable now:
- decompose tasks into dependency DAGs before assigning agents;
- dispatch only ready waves and require typed interface contracts;
- run coherence checks at merge points and label process defects separately from final success.
Tools, repos, and methodologies worth exploring:
- DAG-based planners, kanban dependency gates, typed subclaims, merge validators, process-defect rubrics, trace-backed subagent summaries
Implementability score: 0.64

## Previous structured update

The prior Friday synthesis for week ending 2026-05-29 focused on admission-controlled runtimes: [2026-05-29 roundup](../roundups/2026-05-29.md).
