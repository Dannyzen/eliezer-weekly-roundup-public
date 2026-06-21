# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-21

### Agentic Resource Discovery makes capability discovery governable

Summary: GitHub Agent Finder and the ARD specification turn MCP servers, skills, tools, agents, APIs, and workflows into discoverable resources. The strategic control point is not only what the agent can call, but what it can find.

Analysis: [daily sovereignty analysis](2026-06-21/sovereignty.md#agentic-resource-discovery-makes-capability-discovery-a-governed-plane)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Discovery](../AgenticAI/agent-discovery/agent-discovery.md)
Core sources: [GitHub Agent Finder](https://github.blog/changelog/2026-06-17-agent-finder-for-github-copilot-now-available/), [ARD specification](https://commandline.microsoft.com/agentic-resource-discovery-specification-ard/), [GitHub Agent Finder docs](https://docs.github.com/en/copilot/concepts/mcp-management#agent-finder), [huggingface/hf-discover](https://github.com/huggingface/hf-discover)
Implementable now:
- create a private registry of approved MCP servers, skills, agents, and workflows
- scope discovery by principal, tenant, repo, workflow, and risk tier
- log discovery query, returned capability IDs, selected resource, publisher, media type, and install decision
Tools, repos, and methodologies worth exploring:
- GitHub Agent Finder, `ards-project/connectors`, `huggingface/hf-discover`, MCP registries, allowlist enforcement, OpenTelemetry discovery spans
Implementability score: 0.84

### Least-privilege tool choice needs explicit evaluation and routing policy

Summary: ToolPrivBench shows that agents often choose or escalate to higher-privilege tools even when lower-privilege alternatives are enough. General safety alignment and prompt controls do not reliably solve least-privilege tool routing.

Analysis: [daily sovereignty analysis](2026-06-21/sovereignty.md#least-privilege-tool-choice-is-not-solved-by-general-safety-alignment)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Network Containment](agent-network-containment/agent-network-containment.md)
Core sources: [ToolPrivBench paper](https://arxiv.org/abs/2606.20023v1), [AISafetyHub/agent-tool-selection-bias](https://github.com/AISafetyHub/agent-tool-selection-bias)
Implementable now:
- split tools into read, limited-write, broad-write, admin, and external-effect tiers
- require escalation justification when lower-privilege tools are available
- test transient-failure paths because failures amplify privilege escalation
Tools, repos, and methodologies worth exploring:
- ToolPrivBench-style paired tool tests, OPA or Cedar policy, gateway traces with lower-privilege alternatives and escalation reason
Implementability score: 0.77

### Phoenix reinforces host-state policy for coding autonomy

Summary: Phoenix's issue-to-PR system shows that coding autonomy should sit behind labels, baseline tests, state transitions, permission boundaries, and PR review, not inside an unconstrained agent loop.

Analysis: [daily sovereignty analysis](2026-06-21/sovereignty.md#phoenix-reinforces-that-coding-autonomy-belongs-behind-host-state-policy)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Ticket-Native Agent Orchestration](../AgenticAI/ticket-native-agent-orchestration/ticket-native-agent-orchestration.md)
Core source: [Phoenix](https://arxiv.org/abs/2606.20243v1)
Implementable now:
- gate generated PRs through labels, issue fields, baseline/post-patch tests, branch protection, and CODEOWNERS
- preserve operational failure states such as WAF filtering, token expiry, permission denial, and flaky CI
- use generated PR review queues rather than silent merge paths
Tools, repos, and methodologies worth exploring:
- GitHub webhooks, issue fields, GitHub Actions, Checks API, SWE-bench Lite, CODEOWNERS, branch protection
Implementability score: 0.72
