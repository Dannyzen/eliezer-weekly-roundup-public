# Strategy Daily Analysis — 2026-06-04

## Thesis

The strategic signal today is contract hardening. Agent stacks are being asked to prove that tool descriptions match behavior, that budgets cannot be double-spent, and that hosted agents run inside workflow and sandbox boundaries. The winner is not the agent with the largest tool catalog. It is the runtime that can turn descriptions, budgets, sandboxes, and workflow steps into enforceable contracts.

## MCP descriptions are not contracts unless the gateway checks behavior

The MCP description-code inconsistency paper is a direct warning for agent-platform builders. LLMs choose tools from natural-language descriptions, but the server implementation may behave differently from the description. That mismatch is not documentation debt. It is a security boundary, because the model can be induced to call a tool whose described behavior is narrower or safer than its actual effect.

The strategic lesson is that MCP registries and gateways cannot stop at tool discovery. A server card, README, or description string should not be trusted as the contract. The gateway needs behavior evidence: schema conformance, static checks, dynamic probes, denied-effect tests, provenance, and runtime traces that compare described intent to observed effects.

How it fits:
- Agent gateway governance: descriptions become admission inputs, not authority by themselves.
- Agent network containment: third-party MCP servers need quarantine, risk labeling, and effect testing.
- Runtime governance: tool-call traces should show description, resolved code/version, arguments, observed effect, and policy decision.

Implementable now:
- require MCP server manifests with version, owner, source, tools, schemas, side-effect classes, and data classes;
- run description-code consistency tests before admitting a server to production;
- compare natural-language descriptions against actual argument schemas, file/network/API effects, and observed outputs;
- deny or downgrade tools whose descriptions omit mutation, external observation, credential use, broad data access, or side effects;
- keep a gateway registry that records test evidence and tool-version provenance.

Tools, repos, and methodologies worth exploring:
- MCP gateway registry, schema diffing, static source inspection, dynamic canary probes, Open Policy Agent/Cedar, taint tests, DLP labels, OpenTelemetry tool-call spans

Implementability score: 0.82

Core source:
- [Description-Code Inconsistency in Real-world MCP Servers](https://arxiv.org/abs/2606.04769)

## Budget, workflow, and sandbox controls are becoming runtime contracts

Token Budgets, Microsoft Agent Framework, AWS Step Functions AgentCore reasoning steps, and GitHub Copilot sandboxes all point at the same strategic pattern: agent work needs enforceable runtime contracts around spend, state, execution environment, identity, and final effects.

This is a strategy finding because it changes where governance lives. The control plane is no longer only the model gateway or the chat app. It is the workflow engine, hosted-agent runtime, budget ledger, session state, sandbox, identity boundary, eval pipeline, and trace substrate. Serious agent adoption will route autonomous work through these managed boundaries because unmanaged chat agents cannot supply durable audit, rollback, isolation, or spend control.

How it fits:
- Runtime governance: budgets, reasoning steps, retries, and sandboxes become explicit state, not model advice.
- Local-first agents: local sandboxes keep sensitive tool execution near the developer while still enforcing policy.
- Agent provisioning governance: hosted agents need versioning, deployment, session identity, observability, and rollback like services.

Implementable now:
- define budget authority per workflow, agent, child task, model route, tool, and retry loop;
- make budget delegation explicit, expiring, and non-reusable;
- wrap high-risk agent work in workflow states with input/output contracts, retry policy, timeout, and approval boundaries;
- run tool execution inside local or cloud sandboxes with filesystem, network, and credential policies;
- trace hosted-agent version, session state, sandbox identity, tool calls, approvals, spend events, and final effects.

Tools, repos, and methodologies worth exploring:
- budget ledgers, affine-resource patterns, AWS Step Functions with AgentCore reasoning steps, Microsoft Agent Framework, GitHub Copilot local/cloud sandboxes, OpenTelemetry, CI release gates

Implementability score: 0.72

Core sources:
- [Token Budgets](https://arxiv.org/abs/2606.04056)
- [Microsoft Agent Framework at BUILD 2026](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/)
- [AWS Step Functions adds AgentCore-powered agentic reasoning step](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-step-functions-agentcore/)
- [Cloud and local sandboxes for GitHub Copilot now in public preview](https://github.blog/changelog/2026-06-02-cloud-and-local-sandboxes-for-github-copilot-now-in-public-preview/)
