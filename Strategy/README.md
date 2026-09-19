# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-19

### Turn review findings into durable release state

Summary: Review comments should survive new commits as typed finding records, while coverage and other objective quality thresholds remain platform-owned policy. Agents discover and explain; the release system owns state transitions and merge authority.

Analysis: [daily strategy analysis](2026-09-19/sovereignty.md#turn-review-findings-into-durable-release-state)
Durable deep dive: [Coding Agent Control Plane](../AgenticAI/coding-agent-control-plane/coding-agent-control-plane.md)
Core sources: [Copilot code review state](https://github.blog/changelog/2026-09-18-copilot-code-review-an-improved-review-experience), [coverage ruleset REST API](https://github.blog/changelog/2026-09-18-manage-the-code-coverage-ruleset-condition-with-the-rest-api)
Tools and methodologies worth exploring now: stable finding IDs, commit-bound evidence, explicit resolution reasons, reopened and previously missed states, GitHub rulesets API, independent test, coverage, security, and approval gates
Implementability score: 0.94

## Current implication

Agent review becomes governable when findings are durable state and merge conditions are deterministic policy. Never let a polished review summary, or a model-generated resolution, become release authority by itself.
