# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-06

### Recuse signals are cooperative policy, not access control
Summary: In-band access-deny messages can tell compliant agents to withdraw even when credentials technically work. Treat this as a robots.txt-style governance signal for live infrastructure, not as a security boundary.

Analysis: [daily sovereignty analysis](2026-06-06/sovereignty.md#recuse-signals-are-cooperative-policy-not-access-control)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [Will the Agent Recuse Itself?](https://arxiv.org/abs/2606.06460v1), [Recuse repo](https://github.com/mthamil107/Recuse)
Implementable now:
- add SSH banner, database NOTICE, HTTP header, or MCP error-detail recuse canaries in non-production tests;
- measure whether agents stop, ask, or proceed under different operator-authority framings;
- log recuse-signal visibility and model response as policy evidence.
Tools, repos, and methodologies worth exploring:
- Recuse mini-standard, SSH/PAM banners, PostgreSQL NOTICE proxies, gateway issue-time policy, compliance canary suites
Implementability score: 0.61

### Cloud coding agents are becoming programmable workflow resources
Summary: GitHub's Agent tasks REST API and one-click Actions failure repair make cloud coding agents addressable from automation. The control problem shifts from chat UX to task IDs, status, provenance, CI scope, and merge policy.

Analysis: [daily sovereignty analysis](2026-06-06/sovereignty.md#cloud-coding-agents-are-becoming-programmable-workflow-resources)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [Agent tasks REST API changelog](https://github.blog/changelog/2026-06-04-agent-tasks-rest-api-now-available-for-copilot-pro-pro-and-max/), [GitHub Agent tasks REST docs](https://docs.github.com/rest/agent-tasks/agent-tasks?apiVersion=2026-03-10#start-a-task), [Fix with Copilot for failing Actions](https://github.blog/changelog/2026-06-04-fix-with-copilot-for-failing-actions-now-in-pro-pro-and-max/)
Implementable now:
- wrap cloud-agent task creation in an internal queue with repository, branch, issue, CI failure, and budget metadata;
- require task status, trace, diff, test, and approval artifacts before merge;
- restrict which workflows can ask an external cloud agent to mutate code.
Tools, repos, and methodologies worth exploring:
- GitHub Agent tasks REST API, Copilot cloud agent, GitHub Actions failure repair, PR policy gates, task-state ledgers, OpenTelemetry workflow traces
Implementability score: 0.74

## Previous structured update

The prior Friday synthesis for week ending 2026-06-05 focused on identity-bound MCP gateways, tool-surface integrity, runtime contracts, and speculative external observation governance: [2026-06-05 roundup](../roundups/2026-06-05.md).
