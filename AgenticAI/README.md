# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-06-05 Daily Scan

### Search-time contamination makes deep-research evals leaky
Summary: Deep-research agents can search the web during inference and retrieve benchmark metadata, question context, or explicit answers. Search logs and contamination labels now belong inside the eval harness.

Analysis: [daily reasoning analysis](2026-06-05/reasoning.md#search-time-contamination-makes-deep-research-evals-leaky)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md#june-5-update-search-enabled-agent-evals-need-contamination-controls)
Core source: [Search-Time Contamination in Deep Research Agents](https://arxiv.org/abs/2606.05241)
Implementable now:
- run no-search baselines before crediting web-search trajectories;
- store queries, retrieved URLs, snippets, and evidence paths;
- isolate benchmark metadata and answer keys from the agent's search corpus.
Tools, repos, and methodologies worth exploring:
- network-isolated eval sandboxes, browser/search proxies, leakage classifiers, canary benchmark artifacts, OpenTelemetry traces
Implementability score: 0.74

### Domain-specific skills and voice-tool scenarios are becoming the agent eval substrate
Summary: SciVisAgentSkills and EVA-Bench Data 2.0 show that serious agent evaluation needs domain tool grammars, backend state, expected final state, and reusable skill fixtures, not generic tool-use prompts.

Analysis: [daily reasoning analysis](2026-06-05/reasoning.md#domain-specific-skills-and-voice-tool-scenarios-are-becoming-the-agent-eval-substrate)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md#june-5-update-domain-skills-need-stateful-fixtures)
Core sources: [SciVisAgentSkills paper](https://arxiv.org/abs/2606.05525), [SciVisAgentSkills repository](https://github.com/KuangshiAi/SciVisAgentSkills), [EVA-Bench Data 2.0](https://huggingface.co/blog/ServiceNow-AI/eva-bench-data), [ServiceNow-AI/eva-bench](https://huggingface.co/datasets/ServiceNow-AI/eva-bench)
Implementable now:
- package one internal domain workflow as a skill plus fixture;
- define initial state, allowed tools, expected final state, and negative cases;
- score task completion, tool-call correctness, authentication, final state, and trace quality separately.
Tools, repos, and methodologies worth exploring:
- SciVisAgentSkills, ServiceNow EVA-Bench, SyGra-style scenario generation, Pydantic schemas, verifier-guided review, domain-specific tool simulators
Implementability score: 0.68

### Headroom turns context compression into local-first agent middleware
Summary: Headroom packages context compression as a library, proxy, MCP server, and agent wrapper for tool outputs, logs, files, RAG chunks, and conversation history. The claims need local smoke testing, but the middleware shape is useful now.

Analysis: [daily reasoning analysis](2026-06-05/reasoning.md#headroom-turns-context-compression-into-local-first-agent-middleware)
Durable topic: [Context Economy](context-economy/context-economy.md#june-5-update-context-compression-is-becoming-local-middleware)
Core source: [chopratejas/headroom](https://github.com/chopratejas/headroom)
Implementable now:
- measure token reduction and answer preservation on real tool outputs and logs;
- keep originals outside the prompt and retrieve on demand;
- add before/after context-token counters to traces.
Tools, repos, and methodologies worth exploring:
- Headroom, MCP compression tools, reversible compression, content-aware routers, token-category telemetry, answer-preservation regression tests
Implementability score: 0.86

## Previous structured update

The prior daily scan for 2026-06-04 focused on MCP description consistency, token-budget leases, state-grounded web-agent skills, and AutoLab-style artifact-loop benchmarks: [2026-06-04 roundup](../roundups/2026-06-04.md).
