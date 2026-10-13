# Strategy Daily Sovereignty: 2026-10-13

## Scope

This scan covers the arXiv batch first listed Monday, October 12, 2026, and GitHub's October 12 Copilot telemetry release. External artifacts were inspected read-only. No external source was cloned, installed, built, imported, or executed.

## Thesis

Cross-service agents need effect-path testing and privacy-scoped telemetry. Tool-by-tool permissions miss harmful compositions, while unrestricted observability can create a second sensitive-data system.

## X-AgentRed: red-team the path across services

X-AgentRed models each tool by its execution preconditions, effects, and possible harms, then builds a HarmFlow dependency graph. It samples cross-service tool paths from that graph, executes the resulting scenarios, substitutes tools around discovered harms, and refines preconditions at blocked steps.

### Why it matters

A benign billing request can become a privacy incident only after data moves through payment, commerce, ticketing, and messaging services. Testing each connector alone does not expose the combined path. The control unit must be the full effect chain.

Across four frontier agents and 250 candidate scenarios per target, the paper reports 1.77 times the harmful path rate of STAC and 2.99 times the average tool coverage. The evaluation spans 914 tools. The authors manually inspected all 192 trajectories labeled harmful and report no reward-hacking evidence in those cases.

### Strategy fit

Primary layer: harness security effect verification.

Adjacent layers: gateway governance, stateful effect governance, tool-catalog admission, and incident replay testing.

### Practical tools and methods worth exploring

- Record each tool's preconditions, effects, principals, data classes, and destinations.
- Build edges where one tool's effect satisfies another tool's precondition.
- Generate benign user goals that traverse high-consequence edges.
- Verify the final external state, recipient, resource, and data class with deterministic oracles.
- Preserve blocked steps and refine only the missing precondition.
- Turn every confirmed harmful chain into a release regression fixture.

### Evidence and caveat

The paper publishes a project page and detailed method, but no paper-owned code or dataset repository was identified. Harm confirmation depends on two LLM judges plus manual review, and the service environment is simulated. The authors also identify graph maintenance cost as tools change.

Implementability score: **0.69**

Core sources:
- [X-AgentRed paper v1](https://arxiv.org/abs/2610.13886v1)
- [X-AgentRed project page](https://yeonsungjung.github.io/projects/x-agentred/)

Duplicate status: extension of harness security effect verification. The new control is dependency-guided generation of multi-service harm paths.

## GitHub Copilot telemetry: make identity and content capture separate controls

GitHub now exposes enterprise-managed Copilot telemetry controls that can attribute agent activity without collecting prompts, responses, or tool content. The optional identity fields are `user.name`, `process.user.name`, and `host.name`. Five separate content classes cover prompts, responses, tool arguments, tool output, and policy details. Every capture class is off by default, and managed values override local configuration.

### Why it matters

Fleet incident review needs a durable principal, host, and session. It does not need every prompt, source file, command, or tool result by default. Separating identity from content lets operators answer who acted and where while keeping sensitive payload collection behind an explicit investigation decision.

### Strategy fit

Primary layer: agent fleet monitoring control plane.

Adjacent layers: observability, privacy governance, incident response, retention, and evidence provenance.

### Practical tools and methods worth exploring

- Enable identity attribution only after documenting the approved operational purpose.
- Export OTel to an approved collector and preserve session, model, tool, policy, and outcome IDs.
- Keep all five content classes off during the baseline phase.
- Enable one content class for a bounded investigation, with expiry, access, and deletion controls.
- Join traces to deterministic external-state receipts before closing incidents.
- Verify effective managed settings from every supported client surface.

### Availability and caveat

This is shipping product functionality, not a research prototype. It requires supported Copilot clients, enterprise-managed settings, and an OTel-compatible backend. Content capture can include source code, commands, tool outputs, filesystem paths, and user-profile paths, so over-collection creates material privacy and security risk.

Implementability score: **0.93**

Core sources:
- [GitHub release note](https://github.blog/changelog/2026-10-12-client-telemetry-user-attribution-and-configurable-capture)
- [GitHub enterprise managed settings](https://docs.github.com/copilot/reference/enterprise-administrators/enterprise-managed-settings)
- [VS Code agent OpenTelemetry guide](https://code.visualstudio.com/docs/agents/guides/monitoring-agents)

Duplicate status: extension of the September 23 OTel control-plane finding. The new delta is explicit identity attribution plus independent content capture classes.

## Strategic decision

Model the complete effect path, but collect only the telemetry needed to prove it. Use identity and effect receipts as the baseline. Escalate into payload capture only for a bounded investigation.
