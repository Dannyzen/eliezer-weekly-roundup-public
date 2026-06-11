# Strategy Daily Analysis: 2026-06-11

Today's strategy signal is that agent governance is becoming a runtime composition problem. Per-tool approvals and static policy engines are too small for agents that delegate, accumulate state, call tools, and transform business processes over time.

## Runtime governance needs a five-plane control plane, not per-tool approvals

A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents is the strongest Strategy finding today. The paper argues that enterprise security was built for data boundaries, while production agents move risk into workflows. A sequence of individually permitted actions can still create a business process no one authorized.

The proposed architecture decomposes governance into a reasoning plane plus four enforcement planes: network, identity, endpoint, and data. The reasoning plane adjudicates intent against the composite principal and session state. The enforcement planes realize that decision through existing enterprise controls. A composed evidence record binds the decision and its realizations.

Why it matters: serious agent systems will not be governed by one allow/deny check at the tool boundary. They need stateful evaluation against delegation chains, attenuated authority, intermediate intent, data sensitivity, endpoint posture, network route, and audit requirements.

How it fits into the stack: this extends the enterprise MCP orchestration thesis from the 2026-06-10 deep dive. A BeeSpec-style run contract scopes the worker before action. A five-plane runtime control plane adjudicates and enforces the work as it unfolds.

Practical tools, repos, and methodologies worth exploring now:
- composite principals for user, agent, subagent, tool, tenant, and delegated authority;
- stop-anywhere mediation at planning, retrieval, tool selection, tool call, effect commit, memory write, and audit emission;
- a policy vocabulary richer than allow/deny: allow, deny, redact, require approval, defer, isolate, or request more evidence;
- enforcement adapters for identity provider, network egress, endpoint sandbox, data access, and tool gateway;
- one composed evidence record per material action tying policy decision, principal, context, tool, data, endpoint, and final effect.

Implementability score: 0.67

Core source:
- [A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents](https://arxiv.org/abs/2606.12320v1)

## Skill probes and deterministic layer tests are governance surfaces

The AgenticAI findings have strategic weight too. Runtime Skill Audit shows that static skill review is not enough when malicious behavior depends on local assets, persistent state, and multi-step tool use. Layer-Isolated Evaluation shows that aggregate agent success can hide local scaffold regressions. Together, they imply that governance must test the runtime substrate itself, not only the final answer or the generated code.

Why it matters: regulated or high-value deployments will need evidence that the agent platform can localize regressions, audit skills under realistic triggers, and show which layer failed. This is an operating requirement, not a research nicety.

Practical tools, repos, and methodologies worth exploring now:
- risk-based runtime probes for skills before production admission;
- no-LLM CI suites for routing, memory, safety, escalation, and tool-boundary layers;
- trace evidence that connects skill hash, sandbox context, probe result, policy decision, and final verdict;
- platform controls such as CodeQL, dependency advisory scans, secret scanning, and Snyk Agent Scan around agent-generated or skill-mediated work.

Implementability score: 0.74

Core sources:
- [Runtime Skill Audit](https://arxiv.org/abs/2606.11671v1)
- [Layer-Isolated Evaluation](https://arxiv.org/abs/2606.11686v1)
- [snyk/agent-scan](https://github.com/snyk/agent-scan)

## Strategic readout

The governance layer is converging on one model: bind authority before work starts, mediate each material transition, and preserve evidence as runtime state. That means the durable product surface is a governed execution record, not a prettier chat transcript.
