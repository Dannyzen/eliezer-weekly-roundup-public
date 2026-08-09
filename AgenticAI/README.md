# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-09

### Deterministic document operations before dense retrieval

Summary: READ exposes normalized search, structural navigation, and bounded line reads over MCP. On 51 verified questions it reached 58.8 percent accuracy versus 35.3 percent for tuned dense retrieval, while remaining statistically indistinguishable from BM25.

Analysis: [daily analysis](2026-08-09/reasoning.md#structured-document-retrieval-should-expose-deterministic-operations-before-embeddings)
Core source: [Beyond Top-K](https://arxiv.org/abs/2608.06305v1)
Tools and methodologies worth exploring now: root-jailed read-only MCP tools, exact search, BM25, line citations, paired retrieval tests, explicit power analysis
Implementability score: 0.88

### Coding-agent planning must transfer across scaffolds

Summary: DCAS routes one backend model through multiple CLI scaffolds. Planning-aware fine-tuning on 576 retained trajectories improved unseen-scaffold SWE-bench performance by 3.4 points on OpenCode and 7.0 points on mini-swe-agent.

Analysis: [daily analysis](2026-08-09/reasoning.md#cross-scaffold-coding-evaluation-should-separate-planner-executor-and-scaffold)
Core sources: [paper](https://arxiv.org/abs/2608.06113v1), [replication package](https://zenodo.org/records/19930073), [trajectory dataset](https://huggingface.co/datasets/kishanthan/dcas_glm4.7_distill)
Tools and methodologies worth exploring now: backend-substitution proxies, planner-executor calibration, cross-scaffold evaluation matrices, protocol compatibility tests, planning-aware trajectory collection
Implementability score: 0.72

## Current implication

Prefer interfaces that expose what the agent actually read and which harness conventions produced the result. Deterministic retrieval beats opaque evidence paths, and cross-scaffold evaluation prevents harness-specific behavior from masquerading as model capability.
