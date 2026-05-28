# Strategy Daily Sovereignty: 2026-05-28

Today’s Strategy signal: generated tools should not become callable just because an LLM produced code or a schema. The sovereign control point is admission: intent, implementation, dependency policy, runtime validation, credential binding, lifecycle state, and routing scope must be attached before MCP exposure.

## Findings

### Tool artifacts need validation-carrying governance before MCP exposure

Tool Forge treats a tool as a governed artifact, not a loose function definition. The paper describes capsules containing intent, capability contract, implementation, dependency policy, tests, documentation, runtime validation evidence, lifecycle state, credential bindings, and routing metadata. The accompanying repository frames the implementation as an intent-to-tool generator plus token-optimized MCP router with sandbox validation and a local governed catalog.

Why it matters: the current MCP/tooling rush makes it easy to publish too much tool surface into model context. That creates three strategic failures: prompt-token waste, unreviewed generated code, and broad authority exposure. Tool Forge points toward a better control plane: generate or import tools, validate them, catalog them, then expose only intent-scoped tool sessions.

How it fits into sovereignty: local-first or enterprise agents need their own tool admission process. The agent should not directly decide that newly generated code is now a trusted operational capability. A gateway should require a tool card, test evidence, dependency policy, credential scope, side-effect declaration, and lifecycle approval before the router can advertise the tool.

Implementable now:
- require a `tool_card`-style manifest for every agent-callable tool;
- separate generated, validated, reviewed, approved, deprecated, and revoked lifecycle states;
- run sandbox validation before catalog admission;
- expose intent-scoped tool subsets instead of dumping full schemas into every prompt;
- bind credentials at the gateway, not inside model-written code;
- keep routing logs that include tool version, manifest digest, test status, and selected intent route.

Tools, repos, and methodologies worth exploring:
- [nextmoca/tool-forge](https://github.com/nextmoca/tool-forge) as a read-only reference implementation;
- MCP routers/proxies;
- Open Policy Agent or Cedar for admission rules;
- sandbox validation, dependency pinning, manifest signing, and CI release gates;
- OpenTelemetry spans for route choice, tool admission, and tool execution.

Implementability score: 0.74

Core sources:
- [Tool Forge: A Validation-Carrying Toolchain for Governed Agentic Execution](https://arxiv.org/abs/2605.28000)
- [nextmoca/tool-forge](https://github.com/nextmoca/tool-forge)

## Watchlist

LACUNA is worth tracking as the more formal programming-language direction: typed agent holes where model-filled code is accepted or rejected atomically and tool/data flow is bounded by the surrounding program. It is strategically aligned with the same thesis, but less immediately operational than validation-carrying tool catalogs.

Source:
- [LACUNA: Safe Agents as Recursive Program Holes](https://arxiv.org/abs/2605.28617)
