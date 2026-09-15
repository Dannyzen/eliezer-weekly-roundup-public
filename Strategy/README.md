# Strategy

This index tracks the most recent structured strategy research. Each finding links to the daily analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-15

### Make tool effects transaction-aware

Summary: Eight external-effect anomalies show why successful calls can still leave duplicated, missing, provisional, or aborted residue. In a census of 98,291 MCP tools, standard annotations fully express none of the outcome, compensation, staging, dependency, coordination, or visibility semantics a workflow needs.

Analysis: [daily analysis](2026-09-15/sovereignty.md#require-transactional-contracts-at-every-effect-boundary)
Core sources: [transactional tool-boundary paper](https://arxiv.org/abs/2609.15397v1), [MIT census artifact](https://github.com/flame-stream/mcp-annotation-census)
Tools and methodologies worth exploring now: effect IDs, idempotency keys, authoritative status lookup, compensation preconditions, staged release, dependency identity, ambiguous-outcome holds
Implementability score: 0.78

### Bind MCP admission to an immutable manifest

Summary: In 8,900 multi-version MCP servers, 40.58 percent changed meaning or destination under stable identifiers and 4.16 percent redirected endpoint hosts. The official registry does not version the tool definitions clients actually execute.

Analysis: [daily analysis](2026-09-15/sovereignty.md#pin-mcp-identity-interface-and-endpoint-across-upgrades)
Core source: [MCP silent-drift census](https://arxiv.org/abs/2609.14119v1)
Tools and methodologies worth exploring now: package digests, source revisions, tool-schema hashes, endpoint-origin binding, manifest diffs, approval-gated upgrades, rollback manifests
Implementability score: 0.88

## Current implication

Connectivity is not authority and call success is not workflow correctness. Pin the exact server contract before execution, then require enough effect semantics to resolve retries, compensation, concurrency, and release.
