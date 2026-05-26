# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-26 Daily Scan

### MCP tool metadata is now a security boundary
Summary: Tool Description Poisoning hides malicious instructions inside the tool descriptions that agents use for planning. MCP admission has to authenticate, diff, review, and scope descriptions and schemas, not only executable code or OAuth tokens.

Analysis: [daily sovereignty analysis](2026-05-26/sovereignty.md#mcp-tool-metadata-is-now-a-security-boundary)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [When the Manual Lies](https://arxiv.org/abs/2605.24069), [Attested Tool-Server Admission](https://arxiv.org/abs/2605.24248)
Implementable now:
- pin MCP server identity, tool list, schema digest, and description digest;
- review description diffs before production exposure;
- fuzz tool metadata for hidden instructions and misleading examples;
- log metadata version in every tool-call trace.
Tools, repos, and methodologies worth exploring:
- MCP admission registry, OPA/Cedar policy over tool metadata, JSON Schema/OpenAPI diffing, signed tool manifests, semantic-fuzzing fixtures, `modelcontextprotocol/inspector` for review, DataFew Shield as watchlist only
Implementability score: 0.66

## Previous structured update

The prior Strategy daily scan for 2026-05-25 focused on runtime confidence calibration and trajectory guardrails: [2026-05-25 sovereignty](2026-05-25/sovereignty.md).
