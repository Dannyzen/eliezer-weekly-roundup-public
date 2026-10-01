# Daily Agent Research: 2026-10-01

The October 1 signal is that agent performance is moving into the harness, memory controller, and workflow router. The useful systems keep those layers inspectable and hold evaluation outside the component being improved.

## Evolve harnesses from self-improvement episodes

SelfSearch lets an agent edit its own instructions, tools, and execution procedures while carrying forward records of earlier modification attempts. It does not use downstream benchmark rewards during search. Evaluation and candidate selection remain separate.

Across two model settings and three benchmarks, population-mean success improved over the initial agent in all six settings. Individual gains reached 11.2 percentage points on Terminal-Bench 2.1. On SWE-bench Multilingual, one evolved agent gained 5.0 points while cutting execution cost by 38.5% on tasks solved by both the original and evolved agents. A $4.03 search produced a DeepSeek V4 Flash harness that solved 82.0% of Terminal-Bench 2.1 under a public nine-harness comparison.

### Why it matters

The transferable object is the modification episode, not only the winning diff. Failed edits, incomplete observations, and awkward inspection steps can expose missing agent-computer interfaces. The paper reports that later agents reused tools developed during self-improvement on downstream tasks.

### Fit in the stack

This is an agent-harness evolution layer above version control and below promotion. The editable agent may propose and test local changes. A separate control plane must freeze evaluation tasks, select candidates, detect regressions, constrain authority changes, and approve promotion.

### Practical methods worth exploring

- store each self-improvement episode with parent version, reasoning trace, tool actions, local checks, outcome, and produced diff;
- keep benchmark tasks, model settings, resource limits, and promotion policy outside the editable repository;
- replay each candidate on frozen regressions, no-change controls, and another model family;
- treat new tools and skills as authority changes that need static checks, sandbox replay, and rollback proof;
- compare episode-guided search with evaluation-guided search under the same total budget.

Artifact status: the paper includes implementation details, prompts, configurations, and task-selection rules, but no paper-owned public repository was resolved. The method was not reproduced in this scan.

Implementability score: 0.62

Core source: [SelfSearch v2](https://arxiv.org/abs/2609.37968v2)

## Persist context dependencies instead of rewriting history

RECAP stores attention-derived message importance and dependency links in a persistent context graph. When a new request arrives, it combines those stored signals with request relevance, follows dependency links, and selects original message blocks without another model call for selection.

The paper reports about 95% lower estimated compaction and cold-restoration latency than Codex's summarization-based compaction on Qwen3-Coder and gpt-oss. It roughly halves historical context on SWE-Together at comparable quality and improves Lost-in-Conversation code-task accuracy over full history by 19.8 and 41.2 points across the two model families.

### Why it matters

Summaries turn evidence into model-authored state. A persistent context graph can reduce prompt size while retaining original messages as the selected payload. It also separates three jobs that summaries blur together: historical importance, dependency preservation, and current-request relevance.

### Fit in the stack

RECAP is a memory-selection layer between the raw event log and active model context. The raw messages remain canonical. The graph is a derived index that can be rebuilt, inspected, and compared against full-history and summarization controls.

### Practical methods worth exploring

- retain raw messages and tool outputs as immutable source records;
- persist importance, dependency, supersession, and protected-context edges separately;
- combine stored importance with current-request relevance at retrieval time;
- log selected block IDs, omitted dependencies, token count, latency, cache state, and task outcome;
- test full history, summary, fixed window, and graph retrieval on the same trajectories.

Artifact status: the paper links [UCSB-NLP-Chang/ReCAP](https://github.com/UCSB-NLP-Chang/ReCAP), but the public repository was empty when inspected on 2026-10-01. Treat the code claim as announced, not available.

Implementability score: 0.56

Core source: [Persistent Context Graphs for Efficient Memory Compaction in LLM Agents](https://arxiv.org/abs/2609.40118v1)

## Route workflows, not only models

GitHub expanded HydraFusion from Copilot CLI to Visual Studio Code and the GitHub Copilot app on September 30. The router chooses one of three workflows: a single model, a cascade with an acceptance gate, or a draft plus an independent read-only critic from another model family followed by one revision.

The underlying September research reports, relative to Claude Opus 5, 67% lower estimated cost and 4.9 points higher verified quality on TerminalBench 2.1, 36% lower cost and 1.5 points lower quality on DeepSWE, and 65% lower cost and 0.1 points lower quality on an internal CheckpointBench. GitHub states that every workflow leg is included in cost accounting.

### Why it matters

The routing decision is larger than model selection. It includes workflow shape, critic isolation, escalation, retries, cancellation, fallback, and repository application. HydraFusion's useful pattern is the complete run contract around those legs.

### Fit in the stack

This is the model-router and harness boundary. The router may optimize quality, cost, and latency, while hard privacy, authority, budget, and effect rules remain invariant across routes.

### Practical tools and methods worth exploring

- try the HydraFusion research preview on bounded, non-production coding tasks;
- reproduce single, cascade, and critique routes with auditable rules before learning a router;
- keep critics read-only and tool-less;
- record role, model, outcome, cost, latency, fallback reason, and validation result for every leg;
- apply no patch when a route is cancelled or fails validation.

Caveat: HydraFusion is a closed research preview with no SLA and is not intended for production workloads. The September 30 event is a deployment-surface extension, not a new architecture or independent replication.

Implementability score: 0.84

Core sources:
- [HydraFusion in VS Code and the GitHub Copilot app](https://github.blog/changelog/2026-09-30-hydrafusion-in-vs-code-and-the-github-copilot-app/)
- [Project HydraFusion research and benchmarks](https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/)
- [HydraFusion documentation](https://docs.github.com/en/early-access/copilot/hydrafusion)

## Working conclusion

Treat harness evolution, memory compaction, and model routing as versioned runtime components. Keep raw evidence, evaluation, hard policy, and promotion authority outside the component being optimized.
