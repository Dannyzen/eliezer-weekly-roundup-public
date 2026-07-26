# Strategy

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: Sunday, 2026-07-26

### Coding agents need malicious-issue regression gates

Summary: IssueTrojanBench produced 4,176 experiments across six agent-model configurations. It reports 66.5 percent exploit execution, 72.2 percent success for ordinary text channels, and little protection from prompt boundary markers.

Analysis: [daily sovereignty analysis](2026-07-26/sovereignty.md#coding-agents-need-malicious-issue-regression-gates)
Core sources: [paper](https://arxiv.org/abs/2607.20759v1), [artifact](https://doi.org/10.5281/zenodo.19245678), [repository](https://github.com/software-artifacts/IssueTrojanBench)
Implementable now:
- add malicious issue, PDF, website, source-comment, and issue-comment fixtures;
- deny package, network, secret, hook, and persistence effects unless granted;
- check target and effect after generation and before execution.
Tools, repositories, and methodologies:
- IssueTrojanBench, capability brokers, Cedar or OPA, sandboxes, egress controls
Implementability score: 0.82

### GitHub issue approvals are useful UX, not a security boundary

Summary: GitHub Issues can attach confidence and rationale to automation actions and hold suggestions for review. GitHub explicitly says approvals are not a server-side security control.

Analysis: [daily sovereignty analysis](2026-07-26/sovereignty.md#github-issue-approvals-are-useful-ux-not-a-security-boundary)
Core sources: [changelog](https://github.blog/changelog/2026-07-23-agent-automation-controls-in-github-issues-in-public-preview/), [security model](https://docs.github.com/copilot/concepts/agents/cloud-agent/about-automations)
Implementable now:
- enable rationale and suggestions for low-risk metadata automation;
- hold uncertain or high-impact actions for review;
- keep tools least-privilege and preserve mutation receipts.
Tools, repositories, and methodologies:
- GitHub Agentic Workflows, Copilot automations, issue intents, `has:suggestions`, workflow approval
Implementability score: 0.86

## Current implication

Issues are evidence-bearing work objects, not authority tokens. Review signals help people; scoped capabilities and deterministic policy control effects.
