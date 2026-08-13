# Strategy Daily Sovereignty, 2026-08-13

The strongest governance signal today is that portable capability packages and generated adversarial environments are arriving together. Distribution is becoming cheap. Admission, runtime containment, and evidence have to become explicit before the same package spreads across clients.

## A portable plugin is a cross-client authority object

Agent Plugins 1.0 packages skills and MCP servers once for use across compatible agent clients. GitHub made support generally available on 2026-08-12 in VS Code, Copilot CLI, the Copilot SDK, and the Copilot app. The open specification includes a manifest, versioned schemas, diagnostics, and client namespaces for non-portable behavior.

That portability is useful, but it widens the blast radius of a bad package. A skill changes model behavior; an MCP server exposes effects; hooks and client extensions can add further authority. Installation therefore needs one admission record that binds package digest, publisher, component inventory, requested effects, network destinations, secret scopes, supported clients, and verification results.

Choose portable packaging, but do not let portability imply portable trust. A package should be independently admitted for each client and policy profile.

Practical controls:
- validate the 1.0 manifest and schemas before install;
- enumerate skills, MCP servers, hooks, commands, and namespaced extensions separately;
- assign least-privilege grants per component;
- pin package and dependency digests;
- require startup diagnostics and component health receipts;
- revoke one package identity across every client from a central inventory.

Artifact status: the 1.0.0 specification and schemas are publicly inspectable. GitHub's implementation is GA, but broader ecosystem compatibility remains an empirical client-by-client claim.

Implementability score: 0.90

Core sources:
- https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/
- https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md

## Security evaluation needs executable hostile worlds

ToolHazard generates stateful tool environments, long-horizon tasks, injection points, payloads, and deterministic attack checks. That is a better governance substrate than a list of malicious prompts because the security claim is tied to a world state and a resulting effect.

The runtime contract should preserve the complete evaluation object: environment version, initial state, principal, task, tool catalog, attack placement, policy, trajectory, final-state diff, unauthorized-effect verdict, and cleanup receipt. Those objects can become release gates for plugin, gateway, or tool-interface changes.

The weakest point is generated realism. ToolHazard uses LLM synthesis, and broad domain counts do not prove production fidelity. The mitigation is to admit generated cases only after schema validation, deterministic execution, and a review that maps each case to a real authority boundary.

Practical controls:
- run hostile cases in isolated service doubles;
- classify attacks by carrier, placement, timing, and effect;
- require deterministic final-state adjudication;
- promote production incidents into fixed regression fixtures;
- gate releases on both utility and unauthorized-effect budgets.

Artifact status: the public MIT repository contains populated environment, task, attack, and result trees. It was inspected read-only and not executed.

Implementability score: 0.78

Core sources:
- https://arxiv.org/abs/2608.11878v1
- https://github.com/MurrayTom/ToolHazard

## Working conclusion

Portable packages should accelerate distribution, not trust. Admit the exact package, grant each component separately, and test it inside executable hostile worlds before it can mint effects.
