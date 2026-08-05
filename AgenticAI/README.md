# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-05

### Resume behavior needs a conformance contract

Summary: Resume Means Resume defines six persistence properties, checks a TLA+ reference model across 7.4 million states, and applies a 39-cell fault matrix to five workflow frameworks.

Analysis: [daily analysis](2026-08-05/reasoning.md#resume-means-resume-turns-persistence-semantics-into-a-conformance-suite)
Core source: [paper](https://arxiv.org/abs/2608.03836v1)
Implementable now:
- declare checkpoint and resume semantics;
- persist effect IDs and receipts;
- inject faults around dispatch, commit, and recovery.
Tools and methodologies:
- TLA+, TLC, deterministic fault injection, effect ledgers, replay fixtures
Implementability score: 0.64

### Memory updates need executable transaction types

Summary: TARL replaces binary Write/Hold with five actions and evaluates the resulting memory state. Cross-source five-action F1 reaches 0.6036 on HaluMem-hard and 0.4050 on LoCoMo-derived examples.

Analysis: [daily analysis](2026-08-05/reasoning.md#tarl-makes-memory-revision-an-executable-transaction)
Core source: [paper](https://arxiv.org/abs/2608.03699v1)
Implementable now:
- separate append, revise, reject, defer, and ignore;
- retain before state, after state, source, and temporal scope;
- grade next-state correctness and memory pollution separately.
Tools and methodologies:
- append-only ledgers, typed action schemas, temporal validity, transition fixtures
Implementability score: 0.58

### Small local models can become measured agent workers

Summary: LFM2.5-2.6B provides public ungated weights, 128K context, native tool-call formatting, and agentic RL run inside Hermes Agent, OpenClaw, and other harnesses.

Analysis: [daily analysis](2026-08-05/reasoning.md#lfm25-26b-makes-local-agent-routing-practical-at-the-small-model-tier)
Core sources: [Liquid AI release](https://www.liquid.ai/blog/lfm2-5-2-6b), [model](https://huggingface.co/LiquidAI/LFM2.5-2.6B), [license](https://www.liquid.ai/lfm-license)
Implementable now:
- serve an OpenAI-compatible local endpoint;
- run Hermes-specific tool fixtures;
- route narrow work locally and log escalation reasons.
Tools and repositories:
- LFM2.5-2.6B, llama.cpp, MLX, vLLM, SGLang, Hermes Agent
Implementability score: 0.86

## Current implication

Persistence and routing should expose typed decisions. The runtime must show which state transition happened, which model tier performed it, and which evidence makes the result safe to continue from.
