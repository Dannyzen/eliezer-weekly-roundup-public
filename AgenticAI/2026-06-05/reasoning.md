# Agentic AI Daily Analysis - 2026-06-05

## Thesis

Today's scan says the next useful agent stack is not just larger context or more tools. It is leak-aware evaluation, domain-specific skill and tool fixtures, and local middleware that controls what reaches the model. The pattern is practical: isolate search-enabled evals, turn domain workflows into reproducible tool scenarios, package skills as tested artifacts, and compress context before it becomes reasoning debt.

## Search-time contamination makes deep-research evals leaky

Search-Time Contamination in Deep Research Agents names a failure mode that standard LLM benchmark hygiene does not cover. A deep-research agent can search the web during inference and retrieve benchmark metadata, question context, or explicit answers. The paper defines three contamination types: Benchmark Metadata Leakage, Question-Context Leakage, and Explicit Answer Leakage. It reports that contamination is widespread across six public benchmarks and can inflate measured performance by up to 4%.

That matters because web-enabled agents are evaluated in the same medium where benchmark artifacts, blog posts, solution discussions, leaderboards, and answer keys may already live. If the evaluator only sees a final answer, it cannot tell whether the model reasoned or retrieved the benchmark itself.

How it fits:
- Trajectory-aware evaluation: search queries, clicked results, retrieved snippets, and evidence paths become grading artifacts.
- Agentic search: retrieval is not automatically valid evidence when the query space includes benchmark leakage.
- Runtime governance: eval sandboxes need network policy, logging, and controlled corpus access.

Implementable now:
- run a no-search baseline before crediting a web-search trajectory;
- keep transparent search logs and retrieved-result URLs with every eval result;
- create deny lists or isolated corpora for benchmark metadata, public answer keys, and evaluation pages;
- add canary benchmark items that are visible only through controlled channels;
- score contamination separately from answer accuracy;
- require agents to cite evidence that was not benchmark metadata or answer leakage.

Tools, repos, and methodologies worth exploring:
- network-isolated eval sandboxes, browser/search proxies, OpenTelemetry traces for queries and retrieved URLs, leakage classifiers, canary benchmark artifacts, benchmark access-control manifests

Implementability score: 0.74

Core source:
- [Search-Time Contamination in Deep Research Agents](https://arxiv.org/abs/2606.05241)

## Domain-specific skills and voice-tool scenarios are becoming the agent eval substrate

Two current sources point at the same useful direction. SciVisAgentSkills packages reusable skills for ParaView, napari, VMD, and TTK, then evaluates them with SciVisAgentBench across 108 expert-designed multi-step scientific visualization tasks. ServiceNow's EVA-Bench Data 2.0 expands enterprise voice-agent evaluation to three domains, 121 tools, and 213 scenarios, with reproducible user goals, backend state, and expected final database state.

The shared lesson is that generic tool-use benchmarks are becoming too shallow. Serious agents need domain tool grammars, realistic backend state, expected state transitions, and reproducible scenario generation. A skill is only useful if the harness can prove it improved the right domain workflow without hiding tool misuse, authentication mistakes, or invalid final state.

How it fits:
- Skills as Control: skills should encode environment assumptions, tool usage patterns, and domain heuristics, not just prose advice.
- Agent harness architecture: benchmarks need backend state, expected final state, and validators, not only natural-language tasks.
- Trajectory-aware evaluation: domain-specific tasks should score intermediate tool use and final state.

Implementable now:
- create small domain skill packs for one internal workflow before building a broad skill marketplace;
- pair each skill with a fixture that has initial state, allowed tools, expected final state, and negative cases;
- require every generated scenario to pass schema checks and consistency validation;
- score task completion, tool-call correctness, authentication handling, final database state, and trace quality separately;
- run skill/no-skill and wrong-skill baselines so the benchmark detects overbroad skill loading.

Tools, repos, and methodologies worth exploring:
- SciVisAgentSkills, ServiceNow EVA-Bench, SyGra-style scenario generation, Pydantic state schemas, verifier-guided scenario review, Claude Code/Codex skill packaging, domain-specific tool simulators

Implementability score: 0.68

Core sources:
- [SciVisAgentSkills paper](https://arxiv.org/abs/2606.05525)
- [SciVisAgentSkills repository](https://github.com/KuangshiAi/SciVisAgentSkills)
- [EVA-Bench Data 2.0](https://huggingface.co/blog/ServiceNow-AI/eva-bench-data)
- [ServiceNow-AI/eva-bench dataset](https://huggingface.co/datasets/ServiceNow-AI/eva-bench)
- [ServiceNow/eva repository](https://github.com/ServiceNow/eva)

## Headroom turns context compression into local-first agent middleware

Headroom is a practical tooling signal from GitHub Trending: it positions context compression as a library, proxy, MCP server, and agent wrapper for tool outputs, logs, files, RAG chunks, and conversation history. The README claims 60-95% fewer tokens, local-first operation, reversible compression, content-specific routing, and MCP tools for compression, retrieval, and stats.

Do not treat the compression-quality claims as proven until a local smoke test runs in a sandbox. The useful architectural signal is still real: context economy is becoming middleware. Instead of asking every agent prompt to be concise, put a measured compression and retrieval layer between noisy evidence and the model.

How it fits:
- Context economy: active context should be compressed, routed, measured, and reversible when possible.
- Agent harness architecture: compression needs regression tests so answer quality does not silently degrade.
- Runtime governance: compressed context should preserve original evidence IDs for audit and replay.

Implementable now:
- measure token reduction and answer preservation on real logs, tool outputs, JSON payloads, and RAG chunks;
- keep originals outside the prompt and retrieve them on demand;
- add before/after context-token counters to traces;
- gate compression by content type, because logs, code, JSON, and prose need different reducers;
- run a local sandboxed smoke test before admitting any third-party compression middleware to production.

Tools, repos, and methodologies worth exploring:
- Headroom, MCP compression tools, reversible compression, content-aware routers, answer-preservation regression tests, token-category telemetry, local-first context stores

Implementability score: 0.86

Core source:
- [chopratejas/headroom](https://github.com/chopratejas/headroom)

## Watchlist

Memory is Reconstructed, Not Retrieved proposes graph memory with active reconstruction for long-horizon agents. LatentSkill moves skills from prompt text into LoRA-style weight-space adapters. Both are strategically relevant, but they are less immediately deployable than today's eval, skill-fixture, and compression findings.

Sources:
- [Memory is Reconstructed, Not Retrieved](https://arxiv.org/abs/2606.06036)
- [LatentSkill](https://arxiv.org/abs/2606.06087)
