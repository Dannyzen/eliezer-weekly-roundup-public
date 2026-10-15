# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-15 Daily Scan

The current governance signal is boundary ownership. Skill admission needs capability evidence before installation, and tool invocation needs an authorized gateway beside the systems of record.

### Profile skill capability before installation

Summary: A study of 6,309 marketplace listings found elevated capability in seven of ten skills, while only 770 of 6,061 parseable listings declared anything. Among declaring listings, 59% understated what the bundle could do.

Analysis: [daily strategy analysis](2026-10-15/sovereignty.md#capability-profiling-measure-what-a-skill-can-reach)
Durable topic: [Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md#october-15-2026-profile-capability-before-installation)
Core sources: [paper v1](https://arxiv.org/abs/2610.19264v1), [SkilLock](https://github.com/skills-lock/skil-lock)
Tools and methodologies worth exploring now: whole-bundle static analysis, dependency provenance, capability manifests, capability lockfiles, CI drift checks, unbiased sandbox detonation
Implementability score: 0.70

### Keep MCP authorization and traffic inside the governed cluster

Summary: Apigee hybrid 1.17.0 can compile approved OpenAPI operations into MCP tools while its data plane, request traffic, authorization, quotas, and trace propagation remain inside the customer's Kubernetes cluster.

Analysis: [daily strategy analysis](2026-10-15/sovereignty.md#apigee-hybrid-keep-mcp-traffic-inside-the-governed-cluster)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md#october-15-2026-keep-the-mcp-data-plane-beside-the-systems-it-governs)
Core sources: [Google Developers announcement](https://developers.googleblog.com/en/announcing-mcp-support-in-apigee-hybrid-agentic-tools-that-run-in-your-own-cluster/), [Apigee MCP documentation](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview)
Tools and methodologies worth exploring now: OpenAPI-derived tool catalogs, in-cluster MCP ingress, existing OAuth and mTLS policy, W3C trace context, maintenance-window canary rollout
Implementability score: 0.68

## Current implication

Require two receipts: a capability manifest that explains what a package may reach, and a gateway trace that proves what an invocation actually did.

Latest roundup: [2026-10-15 daily scan](../roundups/2026-10-15.md).
