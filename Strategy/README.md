# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-11 Daily Scan

Today's governance signal is explicit capability activation. Installed or configured tools should remain inactive until the session deliberately enables them under a bounded policy.

### Treat MCP startup as capability activation

Summary: Copilot for JetBrains can now disable automatic MCP server startup for Copilot and Claude. Enterprise administrators can also select a default agent model, although users retain the model picker.

Analysis: [daily strategy analysis](2026-10-11/sovereignty.md#treat-mcp-startup-as-capability-activation)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [GitHub release](https://github.blog/changelog/2026-10-10-new-controls-and-chat-improvements-in-copilot-for-jetbrains)
Tools and methodologies worth exploring now: startup-disabled MCP, session capability receipts, installed-configured-started-authorized-invoked states, explicit server activation, honest model-default labeling
Implementability score: 0.96

## Current implication

Treat startup as an authority transition. Log it, bind it to policy, and keep an installed server inert until the session needs it.

Latest roundup: [2026-10-11 daily scan](../roundups/2026-10-11.md).
