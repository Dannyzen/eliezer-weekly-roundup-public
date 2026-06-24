# Agent Authority Manifests

Last updated: 2026-06-24

Core sources:
- AgentRiskBOM: A Risk-Scoping Security Bill of Materials for Agentic AI Systems: https://arxiv.org/abs/2606.21877v1
- Lingering Authority: Revocable Resource-and-Effect Capabilities for Coding Agents: https://arxiv.org/abs/2606.22504v1
- Securing LLM-Agent Long-Term Memory Against Poisoning: https://arxiv.org/abs/2606.24322v1

Related deep dive:
- [Memory Authority Control Plane](../memory-authority-control-plane/memory-authority-control-plane.md)

## Core thesis

Agent governance needs a deployable authority artifact.

Prompts, policy documents, and generic security reviews are too vague for autonomous systems. A serious agent workflow should ship with a machine-readable manifest that says what the agent can access, remember, change, delegate, and prove, plus runtime mechanics that prevent temporary permissions from lingering after the task episode that justified them.

The durable pattern is:

1. Declare authority before deployment.
2. Mediate authority during execution.
3. Revoke authority when the subtask closes.
4. Preserve proof after the run.

## Why this topic now

AgentRiskBOM and Lingering Authority arrive from different angles but point at one control plane.

AgentRiskBOM says existing SBOM, AIBOM, and MLBOM artifacts do not cover runtime authority. An agent can retrieve private context, call tools, write files, coordinate with other agents, and take external actions. Those capabilities need a structured bill of materials.

Lingering Authority says even a well-justified capability becomes unsafe when it remains exposed after the justifying episode ends. The PORTICO reference monitor turns this into revocable, epoch-bound handles compiled from task contracts.

Together, they move governance from static prose to authority engineering.

## Authority manifest fields

A minimum viable manifest should include:

- agent or workflow identity;
- autonomy level;
- allowed tools and tool effects;
- memory read and write scopes;
- credential scopes;
- data classes and source boundaries;
- external action capabilities;
- approval gates;
- delegation rights;
- inter-agent communication rules;
- sandbox and network boundaries;
- audit signals and trace fields;
- revocation rules and closure predicates;
- control mapping for each high-risk capability.

The point is not paperwork. The point is to make authority diffable.

## Runtime mechanics

Authority manifests are useful only if the runtime enforces them.

Practical mechanics:

1. Compile the manifest into policy rules before the run.
2. Expose only the active tool surface to the planner.
3. Issue opaque capability handles for temporary grants.
4. Bind handles to principal, workflow, resource, effect, and epoch.
5. Remove closed handles from the next planner interface.
6. Reject stale handle replay before side effects occur.
7. Log grant, invoke, close, deny, approval, and stale-replay events.
8. Diff authority manifests across deployments.

## How it fits into the stack

- Runtime governance: the manifest is the pre-run declaration of allowed behavior.
- Agent gateway governance: the gateway enforces manifest-derived discovery and execution policy.
- Evidence provenance: traces prove which authority was used and which controls fired.
- Coding-agent safety: file, git, network, and package-manager effects become scoped grants rather than ambient permissions.
- Procurement and compliance: reviewers can inspect capabilities instead of reading only vendor claims.

## Implementability

Implementability score: 0.80

The thin version is implementable now with JSON Schema, policy-as-code, gateway middleware, and trace logging. The hard version requires end-to-end authority propagation across subagents, memory writes, generated artifacts, delegated tasks, and external systems.

## What to build now

- Define a JSON Schema authority manifest for every internal agent workflow.
- Fail CI when new tools, credentials, memory scopes, external effects, or delegation rights appear without review.
- Put privileged tools behind a reference monitor that evaluates principal, workflow, task stage, resource, effect, and approval state.
- Emit OpenTelemetry spans for authority grant, invoke, close, deny, and stale-replay events.
- Add regression fixtures where an agent correctly uses a capability, closes the subgoal, then tries to reuse the stale capability.
- Store authority manifests next to workflow code, not in a separate governance wiki.

## What remains hard

- Authority through summaries, embeddings, screenshots, and generated files.
- Recursive delegation across subagents with different identities and tool surfaces.
- UI for operators to understand authority without reading raw JSON.
- Calibration of risk scores and thresholds.
- Preventing policy sprawl when many workflows have slightly different manifests.
- Keeping the manifest in sync with actual runtime exposure.

## Strategic implication

The winning agent platform will not only advertise more tools. It will show a diffable map of what each agent can do, why that authority exists, when it expires, and which trace proves enforcement. Authority manifests are the missing bridge between agent demos and governed deployment.


## June 24 update: memory authority must be origin-bound

Securing LLM-Agent Long-Term Memory Against Poisoning extends authority manifests into the memory layer. A memory record can steer future action, so its authority cannot be inferred from content or fragile lineage alone. It has to be bound at write time to origin, scope, and elevation rules that survive summarization, embeddings, retrieval, and tool echoes.

Practical lesson:
- add memory-authority fields to workflow manifests: origin principal, source event, authority tier, scope, expiration, and elevation rule;
- prevent summaries from upgrading an untrusted memory into trusted guidance;
- treat trusted-tool echoes as derived evidence, not as independent authority;
- require independent corroboration before a memory is promoted into action-authorizing context;
- test memory laundering through summarization, echo, and repeated mentions.

Source:
- [Securing LLM-Agent Long-Term Memory Against Poisoning](https://arxiv.org/abs/2606.24322)
