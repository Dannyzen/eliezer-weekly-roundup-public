# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-27 Daily Scan

### Per-query retrieval configuration beats fixed RAG pipelines
Summary: BRANE routes the whole retrieval-agent configuration per query — model, retriever, document count, hop count, and synthesis strategy — instead of applying one fixed RAG setup to every request. The practical win is lower cost without blindly sacrificing answer quality.

Analysis: [daily reasoning analysis](2026-05-27/reasoning.md#per-query-retrieval-configuration-beats-fixed-rag-pipelines)
Durable topic: [Agentic Search and Retrieval](agentic-search/agentic-search.md)
Core source: [Natural Language Query to Configuration for Retrieval Agents](https://arxiv.org/abs/2605.27361)
Implementable now:
- define a retrieval configuration catalog;
- log cost, latency, evidence count, selected route, and answer verdict;
- start with cheapest-first escalation and graduate to a lightweight correctness predictor.
Tools, repos, and methodologies worth exploring:
- BM25/ripgrep, vector/hybrid retrieval, rerankers, LangGraph/LlamaIndex pipelines, LiteLLM cost telemetry, OpenTelemetry route traces, FinanceBench/BrowseComp-style held-out tasks
Implementability score: 0.84

### Skill systems need lifecycle management, not just skill files
Summary: MUSE-Autoskill makes skills a lifecycle problem: create, store, select, test, refine, and transfer skills across agents. This is the control-plane answer to skill-library bloat and wrong-skill selection.

Analysis: [daily reasoning analysis](2026-05-27/reasoning.md#skill-systems-need-lifecycle-management-not-just-skill-files)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core source: [MUSE-Autoskill](https://arxiv.org/abs/2605.27366)
Implementable now:
- add per-skill validators, fixtures, and failure memories;
- log selected and rejected skills plus loaded hashes;
- promote skill edits only after held-out improvement.
Tools, repos, and methodologies worth exploring:
- Git-backed skill folders, `SKILL.md` metadata, semantic fuzzing, contract validators, no-skill/thin-skill/full-library baselines, rollbackable skill patches
Implementability score: 0.70

## Previous structured update

The prior daily scan for 2026-05-26 focused on personalized memory storage gates, skill-selection shadowing, and verifiable computer-use environments: [2026-05-26 reasoning](2026-05-26/reasoning.md).
