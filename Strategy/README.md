# Strategy

Governance analysis for identity, authority, execution control, evidence provenance, gateways, containment, and sovereignty.

## Latest Structured Update: 2026-10-22 Daily Scan

### Preserve origin through context compaction

Summary: Context compaction becomes an authority vulnerability when a harness flattens typed messages into plain text. Forged role markers can survive summarization as apparent user instructions after their real origin is discarded.

Analysis: [preserve origin through context compaction](2026-10-22/sovereignty.md#preserve-origin-through-context-compaction)

Durable deep dive: [Context Compaction Provenance](context-compaction-provenance/context-compaction-provenance.md)

Core sources: [Compaction Laundering paper v1](https://arxiv.org/abs/2610.29869v1), [repository](https://github.com/pixee/compaction-laundering)

Implementable now:
- keep message roles and source identities typed through compaction;
- escape role-like labels in untrusted payloads;
- bind compacted claims to source messages;
- reject unsupported user-attributed summary claims;
- require current authorization before a compacted claim can cause an effect.

Artifact caveat: the public MIT-licensed repository is populated and was inspected read-only. The study is author-run against pinned harness versions.

Implementability score: 0.91

## Current implication

A summary may preserve meaning while destroying authority boundaries. Treat compaction as a typed security transform with provenance tests, not as ordinary text compression.
