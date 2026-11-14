# Strategy Daily Sovereignty: Local Runtime Stability Is a Control Surface

Date: 2026-11-14

## 1. Treat local inference releases as governed API migrations

llama.cpp v1.0.0 is a meaningful local-first milestone because it removes deprecated public APIs while promoting the NextN speculative interface, adds FP8 KV-cache support, host-memory MoE expert caching, external shard loading, additional model architectures, server hardening, and broader test and packaging work.

Why it matters: sovereign inference depends on an operable runtime, not only downloadable weights. A major local runtime release changes public APIs, cache behavior, model support, serving behavior, and deployment artifacts at once. Production adoption should therefore be treated as a source-bound migration with workload replay and rollback, not an automatic binary replacement.

Fit in the strategy stack: local-first inference, runtime governance, capacity planning, and release control.

Implementable now:
- pin the current binary, model files, GGUF metadata, launch flags, and API contract;
- replay representative tool-call, long-context, multimodal, concurrency, and cancellation workloads against v1.0.0;
- measure latency, memory use, cache behavior, output validity, and server failure modes;
- test clients against removed APIs before promotion;
- retain the prior binary and configuration for rollback.

Artifact status: the MIT-licensed `ggml-org/llama.cpp` repository and v1.0.0 release were inspected read-only. No source was cloned, downloaded, built, imported, or executed.

Implementability score: 0.93

Core sources: [llama.cpp v1.0.0 release](https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0), [release overview](https://huggingface.co/blog/ggml-org/llama-cpp-v1)

## Working conclusion

Local inference is now mature enough that runtime lifecycle discipline is the limiting control. Pin identity, replay real workloads, and promote through evidence before adopting a major release.
