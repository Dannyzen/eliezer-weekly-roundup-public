# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-28 Daily Scan

### Memory systems need provenance graphs, not just better retrieval
Summary: MemTrace turns memory pipelines into executable evolution graphs so failures can be attributed to concrete operations: information loss, retrieval misalignment, stale merges, or unsafe writeback. Memory needs lineage before more abstraction.

Analysis: [daily reasoning analysis](2026-05-28/reasoning.md#memory-systems-need-provenance-graphs-not-just-better-retrieval)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core sources: [MemTrace paper](https://arxiv.org/abs/2605.28732), [zjunlp/MemTrace](https://github.com/zjunlp/MemTrace)
Implementable now:
- attach provenance IDs to memory writes, summaries, merges, retrievals, and final-use events;
- classify memory failures by operation, not just by bad final answers;
- regression-test consolidation prompts with adversarial memory fixtures.
Tools, repos, and methodologies worth exploring:
- OpenTelemetry spans, append-only memory event logs, graph provenance tables, Mem0/EverMemOS-style baselines, prompt-optimization loops from attributed failures
Implementability score: 0.58

### Search-agent evals need freshness, feasibility, and evidence-dependence controls
Summary: LiveBrowseComp shows that search agents can pass by verifying prior model knowledge. Feasibility-awareness and TASTE add missing controls: tasks where the right move is early abstention, and harder tasks generated from tool-sequence coverage.

Analysis: [daily reasoning analysis](2026-05-28/reasoning.md#search-agent-evals-need-freshness-feasibility-and-evidence-dependence-controls)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [LiveBrowseComp](https://arxiv.org/abs/2605.28721), [Feasibility Awareness](https://arxiv.org/abs/2605.28532), [TASTE](https://arxiv.org/abs/2605.28556)
Implementable now:
- run closed-book baselines before crediting search;
- use fresh-fact questions and evidence-removal ablations;
- add tool-missing tasks where the correct answer is to stop.
Tools, repos, and methodologies worth exploring:
- BrowseComp-style tasks, publication-date-filtered corpora, tool-mask fixtures, trajectory scoring, query-origin labels, abstention metrics
Implementability score: 0.72

### Agent harnesses are moving toward enterprise incidents and pytest-native red teams
Summary: ITBench-AA reports frontier models below 50% on Kubernetes incident-response tasks. RAMPART gives builders a practical pytest-native way to encode adversarial, benign-failure, and harm-category tests for agents.

Analysis: [daily reasoning analysis](2026-05-28/reasoning.md#agent-harnesses-are-moving-toward-enterprise-incidents-and-pytest-native-red-teams)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [ITBench-AA](https://huggingface.co/blog/ibm-research/itbench-aa), [microsoft/RAMPART](https://github.com/microsoft/RAMPART), [RAMPART on PyPI](https://pypi.org/project/RAMPART/)
Implementable now:
- build SRE-style incident fixtures with logs, dependency graphs, and known root causes;
- put agent safety/security assertions into pytest;
- score false positives, turn count, tool count, latency, and cost.
Tools, repos, and methodologies worth exploring:
- ITBench-AA, RAMPART, pytest, Kubernetes incident simulations, OpenTelemetry, chaos/fault-injection fixtures, CI regression gates
Implementability score: 0.82

## Previous structured update

The prior daily scan for 2026-05-27 focused on per-query retrieval configuration and skill lifecycle management: [2026-05-27 reasoning](2026-05-27/reasoning.md).
