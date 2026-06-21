# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-21

### Probe-tuned repository guidance beats static AGENTS.md

Summary: Probe-and-Refine treats repository guidance as a tested artifact. Synthetic bug-fix probes diagnose missing repo knowledge, then single-shot refinement patches the guidance file before the coding agent uses it.

Analysis: [daily reasoning analysis](2026-06-21/reasoning.md#probe-tuned-repository-guidance-beats-static-agentsmd)
Durable topics: [Ticket-Native Agent Orchestration](ticket-native-agent-orchestration/ticket-native-agent-orchestration.md), [Context Economy](context-economy/context-economy.md), [Skills as Control](skills-as-control/skills-as-control.md)
Core source: [Probe-and-Refine Tuning of Repository Guidance for Coding Agents](https://arxiv.org/abs/2606.20512v1)
Implementable now:
- create concise repo guidance for subsystem map, test commands, forbidden changes, and known wrong paths
- generate synthetic bug-fix probes that test file localization and validation behavior
- patch guidance from failed probes and track evaluable-patch rate separately from precision
Tools, repos, and methodologies worth exploring:
- repository-root `AGENTS.md`, SWE-bench-style fixtures, `git worktree`, devcontainers, single-shot LLM critique of failed probe traces
Implementability score: 0.78

### Phoenix makes issue-to-PR automation a state-machine problem

Summary: Phoenix coordinates six issue-resolution agents through a label-based GitHub webhook state machine, baseline-aware test comparison, and layered safety controls before PR creation.

Analysis: [daily reasoning analysis](2026-06-21/reasoning.md#phoenix-shows-issue-to-pr-agents-need-an-explicit-safety-state-machine)
Durable topics: [Ticket-Native Agent Orchestration](ticket-native-agent-orchestration/ticket-native-agent-orchestration.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Gateway Governance](../Strategy/agent-gateway-governance/agent-gateway-governance.md)
Core source: [Phoenix](https://arxiv.org/abs/2606.20243v1)
Implementable now:
- route issue work through labels, role-specific agents, baseline tests, post-patch comparison, and branch protection
- record WAF filtering, token expiry, permission denial, flaky CI, and planner localization failure as explicit states
- require zero pass-to-pass regressions before opening a generated PR
Tools, repos, and methodologies worth exploring:
- GitHub webhooks, issue fields, Checks API, GitHub Actions, SWE-bench Lite, CODEOWNERS, OpenTelemetry spans for PR automation
Implementability score: 0.72
