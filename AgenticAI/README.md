# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-01 Daily Scan

Today's implementation rule is to keep adaptation inspectable. Harness evolution, memory selection, and workflow routing should emit versioned evidence while evaluation and promotion remain external.

### Evolve harnesses from self-improvement episodes

Summary: SelfSearch carries reasoning, tool actions, local checks, and outcomes from earlier self-modification attempts into later generations. Population-mean success improved in all six model-benchmark settings, with individual gains up to 11.2 points on Terminal-Bench 2.1.

Analysis: [daily analysis](2026-10-01/reasoning.md#evolve-harnesses-from-self-improvement-episodes)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Agent Self-Improvement Governance](../Strategy/agent-self-improvement-governance/agent-self-improvement-governance.md)
Core source: [SelfSearch v2](https://arxiv.org/abs/2609.37968v2)
Tools and methodologies worth exploring now: versioned episode records, editable agent copies, frozen evaluation packs, sandbox replay, external promotion gates
Implementability score: 0.62

### Persist context dependencies instead of rewriting history

Summary: RECAP stores attention-derived importance and dependency links, then combines them with request relevance to select original messages. It reports about 95% lower estimated compaction and cold-restoration latency than summarization, but its linked repository is currently empty.

Analysis: [daily analysis](2026-10-01/reasoning.md#persist-context-dependencies-instead-of-rewriting-history)
Durable topics: [Context Economy](context-economy/context-economy.md), [Memory Systems](memory-systems/memory-systems.md)
Core sources: [RECAP paper](https://arxiv.org/abs/2609.40118v1), [announced repository](https://github.com/UCSB-NLP-Chang/ReCAP)
Tools and methodologies worth exploring now: immutable event logs, persistent context graphs, dependency expansion, full-history controls, task-level token and latency accounting
Implementability score: 0.56

### Route workflows, not only models

Summary: HydraFusion now runs in Visual Studio Code and the GitHub Copilot app. It selects a single, cascade, or cross-family critique workflow, accounts for every leg, isolates critics, and applies no patch after cancellation or failed validation.

Analysis: [daily analysis](2026-10-01/reasoning.md#route-workflows-not-only-models)
Durable topic: [Model Router Governance](../Strategy/model-router-governance/model-router-governance.md)
Core sources: [September 30 release](https://github.blog/changelog/2026-09-30-hydrafusion-in-vs-code-and-the-github-copilot-app/), [research and benchmarks](https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/)
Tools and methodologies worth exploring now: HydraFusion preview, rules-based single/cascade/critique routes, read-only critics, full workflow accounting, validation-gated patch application
Implementability score: 0.84

## Current implication

Treat every adaptive layer as a versioned runtime component. Preserve raw evidence and keep evaluation, hard policy, and promotion outside the component being optimized.

Latest roundup: [2026-10-01](../roundups/2026-10-01.md).
