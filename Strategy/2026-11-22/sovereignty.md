# Strategy Daily Sovereignty: 2026-11-22

## Scope

The strongest uncaptured strategy signal is a 21 November public release that combines organizational search with permission-scoped retrieval. The repository, release, populated tag tree, and README were inspected read-only. No external source was cloned or executed.

## 1. Enforce source permissions before retrieval reaches the model

[Diderot v1.0.0](https://github.com/bluesky-social/diderot/releases/tag/v1.0.0) ingests Slack, Discord, coding-agent sessions, Notion, Linear, Zendesk, and Markdown into a Postgres event log, embeds the corpus in Qdrant, and exposes cited answers through Slack, HTTP, and MCP. Its permission model attaches scope to each event, keeps private Slack channels limited to members, supports owner-only sessions, and filters Qdrant results to chunks the caller may see.

This is the right boundary: access control happens before retrieved text becomes model context. Citations then preserve source identity for the answer. The release is operationally real, with a populated 1,309-entry tag tree, platform binaries, and checksums. It still requires Postgres, Qdrant, embeddings, and a model provider. Retrieval is vector-only, with no keyword index or reranker, and the project warns that API compatibility may change.

Why it matters: an organizational memory layer can leak data even when its answer model follows instructions perfectly. Caller identity, source ACL, retrieval filter, and citation receipt must be one request-bound chain.

Strategic fit: gateway governance, multi-principal memory, evidence provenance, and sovereign organizational search.

Implementable now:
- bind every ingested event to source, tenant, principal scope, and lifecycle state
- resolve caller identity before retrieval
- filter candidate chunks before model context assembly
- return citations with stable source and scope identities
- test revoked membership, private channels, owner-only sessions, and cross-source joins
- keep Postgres as the event truth and treat the vector index as a rebuildable projection

Implementability score: 0.78

Core sources: [Diderot repository](https://github.com/bluesky-social/diderot), [v1.0.0 release](https://github.com/bluesky-social/diderot/releases/tag/v1.0.0)

## Strategic conclusion

Permission-scoped retrieval is an authority boundary. The model should see only chunks authorized for the current principal, and every answer should preserve the source identities that justified it.
