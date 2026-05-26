# Strategy Daily Analysis: 2026-05-26

Today’s strategy signal: MCP governance cannot stop at executable code, OAuth, or tool RBAC. The tool description itself is now part of the trusted computing base. If the manual lies, the agent’s planner can be compromised before any traditional security control sees a dangerous payload.

## MCP tool metadata is now a security boundary

When the Manual Lies introduces Tool Description Poisoning: malicious instructions hidden in tool metadata rather than executable code. That matters because an LLM agent does not merely call a tool; it reads the tool description as planning evidence. In an MCP-style ecosystem, a malicious or compromised server can steer the agent through the cognitive layer by changing the “manual” the agent trusts.

The companion governance direction is visible in Attested Tool-Server Admission. MCP standardizes interaction, but not trust. The host still needs to decide which servers are admitted, which tools are in scope, what sensitivity level applies, and whether the server’s declared metadata matches an approved contract.

### Why it matters

MCP makes tools portable. It also makes tool metadata portable attack surface. A gateway that scans binaries, validates OAuth, and checks tool names can still fail if the agent is allowed to ingest unreviewed descriptions that alter planning, approvals, data handling, or stop conditions.

This is a strategic boundary for Danny’s stack. Local-first agents, cloud coding agents, and enterprise agent gateways all need metadata integrity. The right question is no longer “can this tool execute safely?” It is “is the declaration that shapes the agent’s plan authenticated, versioned, reviewed, scoped, and tested against malicious semantics?”

### How it fits into the strategy stack

- Agent gateway governance: tool descriptions and schemas become policy inputs, not untrusted prose blobs.
- Runtime governance: the gateway should preserve metadata digest, server identity, selected tool, denied tool, and final effect in one trace.
- Agent network containment: third-party MCP servers should not be able to influence planning outside their approved capability envelope.
- Local-first agents: local MCP servers need the same metadata admission discipline as remote servers because local authority is often higher.

### Implementable now

- Pin MCP server identity, version, tool list, schema digest, and description digest before exposing tools to an agent.
- Treat changes to tool descriptions like code changes: diff, review, test, and approve before production use.
- Add policy checks that compare declared tool purpose, allowed data classes, side effects, and approval requirements.
- Run semantic poisoning fixtures that hide instructions inside descriptions, examples, parameter docs, and error messages.
- Keep a gateway-owned allowlist of admitted tool servers and tool subsets per agent workflow.
- Log metadata digest and description version in every tool-call trace.

### Tools, repos, and methodologies worth exploring

- MCP gateway/admission registry
- OPA or Cedar policy over tool metadata
- JSON Schema and OpenAPI diffing
- signed tool manifests
- semantic-fuzzing fixtures for tool descriptions
- modelcontextprotocol/inspector for manual review, not as a full control plane
- DataFew Shield as a watchlist execution-safety layer, pending independent validation

### Implementability score

0.66

The basic controls are straightforward: digest, diff, review, allowlist, and trace. The harder part is semantic validation: proving that a natural-language description does not smuggle planning instructions, privilege escalation, or misleading constraints.

### Core sources

- When the Manual Lies: A Realistic Benchmark to Evaluate MCP Poisoning Attacks for LLM Agents: https://arxiv.org/abs/2605.24069
- Attested Tool-Server Admission: A Security Extension to the Model Context Protocol: https://arxiv.org/abs/2605.24248
