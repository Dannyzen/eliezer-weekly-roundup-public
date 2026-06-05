# Strategy Daily Analysis - 2026-06-05

## Thesis

Today's strategic signal is that tool discovery is becoming a live attack surface. WebMCP lets websites expose tools directly to agents, and that makes origin, lifecycle, metadata, third-party scripts, and traceability part of the security boundary. The strategic winner is not the platform with the biggest tool surface. It is the platform that can prove which dynamic tools were real, authorized, unchanged, and bound to the right origin at the moment of use.

## WebMCP tool-surface poisoning turns tool discovery into a live attack surface

WebMCP Tool Surface Poisoning studies a protocol direction where websites expose tools directly to AI agents. The paper's threat model is useful because it is runtime-shaped, not just registry-shaped. A malicious or compromised third-party script can manipulate the tools visible to an active session. The authors call the broad class Mid-Session Tool Injection and separate it into Tool Hijacking, which changes the visible tool set through mechanisms such as AbortSignal or race conditions, and Tool Framing, which changes how the agent interprets tool metadata such as name, description, readOnlyHint, and inputSchema.

This is the natural continuation of yesterday's MCP description-code inconsistency finding. Yesterday's problem was static mismatch between what a tool says and what it does. Today's problem is dynamic manipulation of what the agent thinks the tool surface is during the session.

How it fits:
- Agent gateway governance: dynamic tool discovery needs origin binding, lifecycle consistency, and metadata integrity.
- Agent network containment: third-party scripts and website-exposed tools need isolation from trusted agent authority.
- Runtime governance: traces must record tool registration, modification, visibility, metadata, origin, and selected-call evidence.

Implementable now:
- bind tool identity to origin and version, not only to a natural-language name;
- require lifecycle consistency from registration through call execution;
- freeze or revalidate the visible tool set at policy checkpoints;
- separate first-party, third-party, read-only, and mutating tools in the gateway policy model;
- treat metadata fields such as description, readOnlyHint, and inputSchema as policy inputs that need integrity checks;
- log registration time, origin, script/source, metadata hash, policy decision, selected tool, arguments, and observed effect.

Tools, repos, and methodologies worth exploring:
- MCP gateway registries, WebMCP canary sites, content security policy, signed tool manifests, metadata hashing, dynamic tool-surface diffing, OPA/Cedar policy checks, OpenTelemetry tool-registration spans, browser isolation

Implementability score: 0.80

Core source:
- [WebMCP Tool Surface Poisoning](https://arxiv.org/abs/2606.06387)

## Watchlist: physical agents are starting to expose remote tool ecosystems

Hugging Face's Reachy Mini post shows a benign version of the same governance pressure. Reachy Mini now supports tool spaces for remote capabilities such as search and weather. Profiles decide which tools are active through `tools.txt`, while robot body tools stay local and trusted.

This did not beat the WebMCP poisoning paper as a top strategic finding, but it is directionally important. When agents leave the browser and enter physical or local devices, profile-level tool enablement becomes a safety boundary. Search and weather are low-risk canaries. Camera, motion, files, credentials, and home or robot controls are not.

Source:
- [Adding MCP Tools to Reachy Mini](https://huggingface.co/blog/adding-mcp-tools-to-reachy-mini)
