# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-06-01 Daily Scan

### Verified skills are becoming capability governance
Summary: NVIDIA’s skills catalog, verified-skills blog, and physical-AI skills release push skills from prompt snippets into governed capability artifacts with provenance, scanning, signatures, skill cards, scope, and lifecycle state.

Analysis: [daily reasoning analysis](2026-06-01/reasoning.md#verified-skills-are-becoming-capability-governance-not-prompt-decoration)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core sources: [NVIDIA physical-AI skills release](https://nvidianews.nvidia.com/news/nvidia-releases-major-collection-of-open-source-agent-tools-and-skills-for-physical-ai), [NVIDIA skills repository](https://github.com/NVIDIA/skills), [verified skills governance blog](https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/), [Cosmos 3 on Hugging Face](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai)
Implementable now:
- add skill cards with owner, scope, dependencies, allowed tools, limitations, and validation status;
- pin and review third-party skill sources before privileged use;
- log selected skill, loaded body hash, source repo, and validation level in every run;
- build regression fixtures for high-value skills.
Tools, repos, and methodologies worth exploring:
- `NVIDIA/skills`, `skills` CLI, skill cards, cryptographic signing, static risk scanning, semantic fuzzing, provenance manifests, Pydantic contracts, OpenTelemetry trace fields
Implementability score: 0.91

### Long-term memory evals need evolving heterogeneous life logs
Summary: RHELM argues that static dialogue personas are too weak for long-running assistants. Memory evals should synchronize chats with documents, emails, evolving event trajectories, stale facts, and source-specific evidence.

Analysis: [daily reasoning analysis](2026-06-01/reasoning.md#long-term-memory-benchmarks-need-heterogeneous-evolving-life-logs)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [RHELM](https://arxiv.org/abs/2605.31086)
Implementable now:
- create mixed-source memory fixtures with chats, files, emails, and timeline events;
- include supersessions, contradictions, stale evidence, and distractors;
- score profile updates, forgetting, retrieval, and evidence citation separately;
- require source evidence when answers use durable memory.
Tools, repos, and methodologies worth exploring:
- typed memory ledgers, event-sourced memory, pgvector plus exact search, temporal fixtures, profile-state tests, source-span citation, stay/update/isolate gates
Implementability score: 0.66

### Retrieval evals need deterministic oracles and distractor controls
Summary: SPECTRA gives a practical pattern for private-corpus retrieval testing: synthetic corpora with latent topics, deterministic relevance oracles, query intents, metadata controls, and adjustable distractor pressure.

Analysis: [daily reasoning analysis](2026-06-01/reasoning.md#retrieval-evals-need-deterministic-oracles-and-distractor-controls)
Durable topic: [Agentic Search and Retrieval](agentic-search/agentic-search.md)
Core source: [SPECTRA](https://arxiv.org/abs/2605.31575)
Implementable now:
- generate synthetic corpora with known topic and relevance labels;
- vary distractor ratio, metadata noise, stale documents, and near-duplicates;
- compare exact, vector, hybrid, and routed retrieval under one oracle;
- log query route, result set, follow-up reads, and cited evidence.
Tools, repos, and methodologies worth exploring:
- BM25/ripgrep baselines, pgvector, LanceDB/Qdrant, deterministic synthetic corpora, Cranfield/TREC-style evals, nDCG/MRR, property-based corpus generation
Implementability score: 0.84

## Previous structured update

The prior daily scan for 2026-05-31 focused on belief-state gates, proposal-soundness review, production-failure-to-fixture evals, and MCP principal binding: [2026-05-31 roundup](../roundups/2026-05-31.md).
