# AgenticAI Daily Analysis, 2026-08-09

No new arXiv listing appears on Sunday. These findings are non-duplicate extensions from the Friday, 2026-08-07 listing batch, with v1 submissions dated 2026-08-06.

## Structured document retrieval should expose deterministic operations before embeddings

Beyond Top-K tests a simple claim that most RAG systems skip: fixed chunking is a lossy interface for long, structured, numeric documents. On a 780-page government financial report, 86.8 percent of content lines are table rows. A figure inherits its unit from a header a median of 13 lines above it. Even a table-aware chunker leaves 27 to 30 percent of numeric chunks without a fiscal-year header across tested chunk sizes.

READ replaces the chunk, embed, top-k pipeline with four read-only operations exposed through MCP: normalized lexical search, file listing, heading outlines, and bounded line reads. Every operation returns stable line references, so the retrieval trajectory can be replayed and audited.

On 51 verified questions, READ reached 58.8 percent accuracy against 15.7 percent for the initial dense baseline and 35.3 percent for the best tuned dense configuration. Giving the same agent loop a top-k vector tool reached only 27.5 percent, which attributes the gain to the interface rather than iteration alone. The paper also reports the limiting result: BM25 reached 51.0 percent and was statistically indistinguishable from READ. The evidence supports deterministic, embedding-free access over dense retrieval for this document class. It does not prove that an agent loop beats lexical search.

Why it matters: retrieval should preserve the document's own structure before adding learned similarity. Deterministic operations give reviewers exact evidence spans, expose wasted searches, remove index drift, and make failures reproducible.

Fit in the stack: agentic search, context economy, MCP tool design, evidence provenance, and retrieval evaluation.

Practical tools and methods:
- expose read-only `search`, `list`, `outline`, and bounded `read` operations;
- jail every file operation to an approved root;
- return original line numbers after normalization;
- compare exact search, BM25, dense, hybrid, and agentic interfaces on the same verified questions;
- use paired tests and report benchmark power for null results;
- require final answers to cite the exact spans read.

Artifact status: the paper says READ is released as an MCP server, but no exact public artifact URL was verified from the primary pages in this scan. The method is still straightforward to reproduce from standard file operations.

Implementability score: 0.88

Core source: https://arxiv.org/abs/2608.06305v1

## Cross-scaffold coding evaluation should separate planner, executor, and scaffold

DCAS shows that coding-agent performance is partly installed by the training scaffold, not only by the model. Four fine-tuned 30B to 32B models were evaluated across OpenHands, Claude Code, OpenCode, and mini-swe-agent on SWE-bench Verified. Every fine-tuned model degraded on at least one non-training scaffold. One model fell from 49.7 percent under OpenHands to 20.4 percent under mini-swe-agent. Another reached only 8.4 percent under OpenCode because its tool-call format was incompatible with the parser.

The paper introduces a backend-substitution interception layer that routes one model through multiple CLI scaffolds without modifying them. Holding executor, benchmark, and scaffold fixed, a self-generated plan improved Qwen3-Coder-30B from 42.8 to 48.2 percent Pass@1. A Claude Sonnet 4.5 plan raised it to 57.8 percent. Planning-aware fine-tuning on 576 retained trajectories then transferred to unseen scaffolds: self-plan performance improved by 3.4 points on OpenCode and 7.0 points on mini-swe-agent relative to the base no-plan condition.

Why it matters: a benchmark score is a property of model, scaffold, planner, protocol, and version together. Training under one harness can install hidden conventions that look like model capability until deployment changes the interface.

Fit in the stack: coding-agent control planes, harness portability, planner-executor routing, trajectory collection, and evaluation identity.

Practical tools and methods:
- evaluate each model across at least one non-training scaffold;
- record scaffold name, version, API protocol, tool schema, turn budget, planner identity, and executor identity;
- make explicit plans first-class artifacts with hashes and outcome links;
- test planner-executor calibration rather than routing only by model rank;
- collect planning and execution trajectories separately;
- gate claims on protocol compatibility, not HTTP success alone.

Artifact status: the open Zenodo replication package contains source and reproduction material, and the public Hugging Face dataset exposes planning and execution trajectories. Both resolved read-only. No external code or dataset was downloaded or executed.

Implementability score: 0.72

Core sources:
- https://arxiv.org/abs/2608.06113v1
- https://zenodo.org/records/19930073
- https://huggingface.co/datasets/kishanthan/dcas_glm4.7_distill

## Working conclusion

Two default abstractions are hiding operational failures. Dense top-k retrieval erases document structure, and single-scaffold evaluation erases harness dependence. Expose deterministic read operations, and bind every coding-agent score to the planner, executor, scaffold, protocol, and version that produced it.
