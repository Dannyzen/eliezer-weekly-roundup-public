# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-13 Daily Scan

The current governance signal is effect-path proof with minimum necessary telemetry. Agents cross service boundaries, while observability systems must avoid collecting every sensitive payload by default.

### Red-team complete cross-service effect paths

Summary: X-AgentRed builds tool-dependency graphs from preconditions and effects, then uses execution feedback to discover harmful multi-service paths. Across four frontier agents, it reports 1.77 times the harmful path rate and 2.99 times the average tool coverage of the strongest comparison.

Analysis: [daily strategy analysis](2026-10-13/sovereignty.md#x-agentred-red-team-the-path-across-services)
Durable topic: [Harness Security Effect Verification](../AgenticAI/harness-security-effect-verification/harness-security-effect-verification.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.13886v1), [project page](https://yeonsungjung.github.io/projects/x-agentred/)
Tools and methodologies worth exploring now: precondition-effect graphs, path generation, destination-aware state oracles, blocked-step refinement, incident-to-regression conversion
Implementability score: 0.69

### Separate identity telemetry from content capture

Summary: GitHub Copilot enterprise controls can now export user, OS-account, and host identity independently from prompts, responses, tool arguments, tool output, and policy detail. Every capture class is off by default.

Analysis: [daily strategy analysis](2026-10-13/sovereignty.md#github-copilot-telemetry-make-identity-and-content-capture-separate-controls)
Durable topic: [Agent Fleet Monitoring Control Plane](agent-fleet-monitoring-control-plane/agent-fleet-monitoring-control-plane.md)
Core sources: [GitHub release note](https://github.blog/changelog/2026-10-12-client-telemetry-user-attribution-and-configurable-capture), [managed settings](https://docs.github.com/copilot/reference/enterprise-administrators/enterprise-managed-settings), [VS Code OTel guide](https://code.visualstudio.com/docs/agents/guides/monitoring-agents)
Tools and methodologies worth exploring now: OTel identity attribution, approved collectors, content-class deny-by-default, investigation expiry, trace-to-effect receipts
Implementability score: 0.93

## Current implication

Prove who acted and what changed without turning routine monitoring into a copy of every prompt, file, command, and tool result.

Latest roundup: [2026-10-13 daily scan](../roundups/2026-10-13.md).
