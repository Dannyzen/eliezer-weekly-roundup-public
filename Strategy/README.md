# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Latest structured update: 2026-11-14

### Govern local inference as a runtime lifecycle

Summary: llama.cpp v1.0.0 removes deprecated APIs and changes speculative decoding, cache, MoE, model, server, test, and packaging surfaces. Sovereign adoption needs workload replay, source identity, and rollback.

Analysis: [Daily strategy](2026-11-14/sovereignty.md#1-treat-local-inference-releases-as-governed-api-migrations)

Core sources: [llama.cpp v1.0.0 release](https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0), [release overview](https://huggingface.co/blog/ggml-org/llama-cpp-v1)

Implementable now:
- pinned binary, model, flags, and client contract
- production-shaped replay across tool calls and long context
- latency, memory, cache, validity, and failure measurements
- prior-version rollback package

Implementability score: 0.93

## Current strategic model

1. Evidence informs authority without becoming authority.
2. Persistent state changes begin as quarantined proposals.
3. Local execution still requires identity, policy, observability, and rollback.
4. Major runtime upgrades are migrations, not package refreshes.
5. Promotion follows representative replay against an exact source identity.

## Browse

- [Daily roundup](../roundups/2026-11-14.md)
- [Daily strategy](2026-11-14/sovereignty.md)
- [Local-first agents](local-first-agents/local-first-agents.md)
- [Runtime governance](runtime-governance/runtime-governance.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
