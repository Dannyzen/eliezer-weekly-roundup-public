# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-13

### A portable plugin is a cross-client authority object

Summary: Agent Plugins 1.0 reduces packaging duplication across GitHub agent clients, but the package may combine behavioral skills, MCP effects, hooks, commands, and client extensions. Portability increases the need for package identity, per-component grants, and cross-client revocation.

Analysis: [daily strategy](2026-08-13/sovereignty.md#a-portable-plugin-is-a-cross-client-authority-object)
Core sources: [GitHub release](https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/), [1.0.0 specification](https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md)
Tools and methodologies worth exploring now: package digests, component inventories, least-privilege grants, client-specific admission, startup diagnostics, central revocation
Implementability score: 0.90

### Security evaluation needs executable hostile worlds

Summary: ToolHazard turns indirect prompt injection into stateful environment tests with attack placement, long-horizon tasks, and deterministic effect checks. These environment objects can become release gates for plugins, gateways, and tool interfaces.

Analysis: [daily strategy](2026-08-13/sovereignty.md#security-evaluation-needs-executable-hostile-worlds)
Core sources: [paper](https://arxiv.org/abs/2608.11878v1), [public MIT repository](https://github.com/MurrayTom/ToolHazard)
Tools and methodologies worth exploring now: isolated service doubles, environment manifests, final-state adjudication, unauthorized-effect budgets, incident-to-fixture promotion
Implementability score: 0.78

## Current implication

Portable packaging should accelerate distribution, not trust. Admit the exact package, grant each component separately, and test it inside executable hostile worlds before it can mint effects.
