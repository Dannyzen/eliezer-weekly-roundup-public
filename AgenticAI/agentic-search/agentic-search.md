# Agentic Search and Retrieval

Agentic search is no longer just “put embeddings in front of the model.” In a real agent loop, search quality is shaped by the harness: exact search versus vector retrieval, how tool outputs are presented, whether large results are written to files, whether the model performs follow-up reads, how much irrelevant history surrounds the relevant evidence, and whether the trace records what actually influenced the answer.

## Why this topic now

The May 2026 paper `Is Grep All You Need? How Agent Harnesses Reshape Agentic Search` makes the practical point directly. It compares grep and vector retrieval on a 116-question LongMemEval sample using both a custom Chronos harness and provider-native CLI harnesses including Claude Code, Codex, and Gemini CLI. It also compares inline tool outputs against file-backed results that the model reads separately. Across the studied harnesses, grep often performs better than vector retrieval, while final scores still depend strongly on the harness and tool-calling style.

Core source:
- https://arxiv.org/abs/2605.15184

## Core thesis

Retrieval is an agent-runtime behavior, not a database feature.

The right question is not only “which retriever has the best recall?” The better questions are:
- which search primitive did the agent use first?
- how much output entered context automatically?
- did the model deliberately inspect files or passively receive snippets?
- did exact terms matter more than semantic neighbors?
- how did the harness handle irrelevant surrounding history?
- which retrieved evidence was actually cited or used?
- can the run be replayed with the same search/read path?

## Practical design pattern

### 1. Start with exact search as the baseline

Use `grep`, `ripgrep`, SQL predicates, file names, symbols, IDs, and other exact signals before assuming a vector store is necessary. For code, logs, transcripts, and many memory tasks, lexical anchors are often the most reliable entry point.

### 2. Treat vector retrieval as a complement, not the default religion

Vector retrieval is still useful for fuzzy recall, paraphrase, and concept matching. But it should be measured against exact search on the same tasks. If exact search wins, do not hide that result because the architecture diagram expected embeddings.

### 3. Make output handoff explicit

Inline tool results and file-backed artifacts are different agent interfaces. Inline results can be fast but can also flood context. File-backed results force a deliberate read step and can create a cleaner audit trail.

### 4. Trace search, read, and citation events together

A useful trace should include:
- search query;
- search method;
- index or corpus version;
- result count and result size;
- output handoff mode;
- follow-up file reads;
- discarded candidates;
- final citations or evidence use.

### 5. Test under distraction

Search evals should inject irrelevant history, outdated files, similar names, duplicate snippets, stale memories, and near-miss documents. Clean retrieval tasks overstate production performance.

## What to build now

- Add a grep/ripgrep baseline to every repo-search or memory-search eval.
- Run identical tasks through the local harness and provider-native CLIs under consideration.
- Compare inline search snippets against file-backed result sets.
- Log retrieval path and citation use as first-class trace fields.
- Add eval cases with irrelevant surrounding history and near-duplicate false positives.
- Route retrieval by task: exact search first for named entities, code symbols, IDs, file paths, logs, and configuration; vector search for fuzzy conceptual recall.

## What to avoid

- Treating embeddings as the default before proving exact search is insufficient.
- Dumping large search outputs directly into context without a read path.
- Scoring retrieval outside the actual agent loop.
- Ignoring provider-harness differences when comparing models.
- Counting a retrieval as successful when the answer did not actually use or cite it.

## May 18 update: deep research should dispatch missing evidence pieces

Argus adds a useful orchestration pattern to this topic. It argues that scaling deep research by launching many independent ReAct rollouts creates redundant evidence and context bloat. The better unit of parallelism is the missing evidence piece.

The practical pattern is a Navigator/Searcher split:
- the Navigator owns the question decomposition, evidence graph, and missing-slot checklist;
- Searchers collect source-grounded evidence for one sub-query at a time;
- the Navigator verifies which evidence slots are still missing or contradictory;
- synthesis happens from evidence nodes, not from raw worker transcripts;
- each final claim links back to the evidence nodes that supported it.

This complements the grep-vs-vector lesson. Agentic search quality is a runtime behavior: query formulation, exact search, result handoff, evidence graph maintenance, dispatch policy, and citation use all matter. The target product shape is a research agent that knows what it still has not proven.

Source:
- [Argus: Evidence Assembly for Scalable Deep Research Agents](https://arxiv.org/abs/2605.16217)

## May 21 update: deep research needs derivation and calibration traces

DeepWeb-Bench adds a useful correction to agentic search. Its headline is not merely that deep research benchmarks are getting harder. The important result is that retrieval is not the dominant failure mode. The paper reports retrieval failures at only 12-14% of errors, while derivation and calibration dominate.

That changes the build target. A research agent should not be judged by whether it fetched enough links. It should be judged by whether it can preserve source provenance, reconcile conflicting sources, compute derived answers, abstain when precision is not available, and show which evidence supported which claim.

Practical lesson:
- score retrieval, derivation, reasoning, and calibration separately;
- keep a claim -> evidence -> derivation graph instead of only final citations;
- snapshot sources and attach cited spans to generated claims;
- track hallucinated precision as a distinct calibration failure;
- use DeepWeb-Bench tasks as regression cases for research-agent workflows.

Sources:
- [DeepWeb-Bench](https://arxiv.org/abs/2605.21482v1)
- [DeepWeb-Bench project page](https://sixiongxie1001-dot.github.io/deep-research-benchmark2.0)
- [DeepWeb-Bench dataset](https://huggingface.co/datasets/deepweb-bench-anon/deepweb-bench)

## Related durable topics

- [Agent Harness Architecture](../agent-harness-architecture/agent-harness-architecture.md)
- [Context Economy for Agents](../context-economy/context-economy.md)
- [Memory Systems](../memory-systems/memory-systems.md)
- [File-as-Bus Workspaces](../file-as-bus-workspaces/file-as-bus-workspaces.md)

## Current implementability

Implementability score: 0.88

This is one of the most straightforward build moves in the stack. It can be started with standard search tools, trace logging, and a small eval harness. The hard part is not implementation; it is resisting the impulse to add vector infrastructure before measuring the simple baseline.
