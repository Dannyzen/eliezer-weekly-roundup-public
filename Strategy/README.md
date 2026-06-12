# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Friday synthesis, week ending 2026-06-12

### Stateful runtime governance is the strategic control plane

Summary: Five-plane governance, OCELOT, sabotage monitoring, executable validation, and trace-safe release controls all say the same thing: serious agents need state-transition mediation, not per-output filters or isolated tool approvals.

Analysis: [weekly sovereignty analysis](2026-06-12/sovereignty.md#stateful-runtime-governance-is-the-strategic-control-plane)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [Five-Plane Runtime Governance](https://arxiv.org/abs/2606.12320v1), [OCELOT](https://arxiv.org/abs/2606.12341v1), [Agent sabotage monitoring](https://arxiv.org/abs/2606.07054v1), [GitHub third-party coding-agent validation](https://github.blog/changelog/2026-06-09-security-validation-for-third-party-coding-agents)
Implementable now:
- represent material actions as principal, intent, data, destination, tool, policy, budget, and evidence;
- keep per-sink disclosure ledgers and richer verdicts than allow/deny;
- run sabotage and privacy fixtures over typed traces.
Tools, repos, and methodologies worth exploring:
- composite principals, release ledgers, trace-mediated approval gates, executable security fixtures, evidence packages
Implementability score: 0.63

### Memory, artifacts, and skills are now policy write paths

Summary: Selection Integrity, artifact-provenance gaps, MalSkillBench, Runtime Skill Audit, and context-rot work show that security risk often enters before final retrieval or citation. Memory writes, graph edges, artifact transforms, skill loads, and guidance files are policy events.

Analysis: [weekly sovereignty analysis](2026-06-12/sovereignty.md#memory-artifacts-and-skills-are-now-policy-write-paths)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md)
Core sources: [Selection Integrity](https://arxiv.org/abs/2606.12290v1), [Artifact provenance gaps](https://arxiv.org/abs/2606.09084v1), [MalSkillBench](https://arxiv.org/abs/2606.07131v1), [Snyk Agent Scan](https://github.com/snyk/agent-scan)
Implementable now:
- label memory edges, artifact transforms, skill loads, and guidance files by writer principal, trust tier, hash, and source;
- log graph-selection paths and artifact lineage;
- prevent untrusted structure from steering authorization, policy creation, memory promotion, credential use, or external sends.
Tools, repos, and methodologies worth exploring:
- graph provenance, taint-aware selection, policy-gated memory writes, skill manifests, context-rot scanners, artifact lineage logs
Implementability score: 0.72

### Cloud and persistent agents make workspace authority the product boundary

Summary: GitHub Agent Tasks, Fix with Copilot, OpenAI’s Ona acquisition announcement, and GitHub security validation for third-party coding agents show cloud agents becoming persistent programmable resources. Workspace state, not only model quality, becomes the strategic boundary.

Analysis: [weekly sovereignty analysis](2026-06-12/sovereignty.md#cloud-and-persistent-agents-make-workspace-authority-the-product-boundary)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Local-First Agents](local-first-agents/local-first-agents.md)
Core sources: [GitHub Agent Tasks REST API](https://github.blog/changelog/2026-06-04-agent-tasks-rest-api-now-available-for-copilot-pro-pro-and-max/), [GitHub Agent Tasks API docs](https://docs.github.com/rest/agent-tasks/agent-tasks?apiVersion=2026-03-10#start-a-task), [OpenAI to acquire Ona](https://openai.com/index/openai-to-acquire-ona), [GitHub third-party coding-agent validation](https://github.blog/changelog/2026-06-09-security-validation-for-third-party-coding-agents)
Implementable now:
- wrap cloud-agent task creation in an internal policy queue;
- bind workspaces to owner, tenant, project, model, policy, checkpoint, and credential scope;
- export customer-controlled traces, artifacts, logs, and verifier results.
Tools, repos, and methodologies worth exploring:
- cloud/local parity tests, scoped credentials, workspace lineage, checkpoint audit, long-running task budgets, revocation workflows
Implementability score: 0.76

### MCP and toolchain governance are becoming enterprise release surfaces

Summary: GitHub Enterprise managed plugins, FastMCP releases, mcp-guard, Recuse, and AgentBeats show agent tool governance moving from local developer configuration into enterprise release management and protocol-level evaluation.

Analysis: [weekly sovereignty analysis](2026-06-12/sovereignty.md#mcp-and-toolchain-governance-are-becoming-enterprise-release-surfaces)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [GitHub Enterprise managed plugins](https://github.blog/changelog/2026-06-05-enterprise-managed-plugins-in-vs-code-in-public-preview/), [FastMCP v3.4.2](https://github.com/PrefectHQ/fastmcp/releases/tag/v3.4.2), [mcp-guard v1.0.0](https://github.com/diomonogatari/mcp-guard/releases/tag/v1.0.0), [Recuse](https://arxiv.org/abs/2606.06460v1)
Implementable now:
- centralize approved plugins and MCP configs;
- pin MCP dependencies and scan server descriptions before release;
- regression-test OAuth, JWT, session, and principal behavior.
Tools, repos, and methodologies worth exploring:
- approved MCP registries, server-description scanners, enterprise plugin policy, mcp-guard, FastMCP release hygiene, A2A/MCP benchmark interfaces
Implementability score: 0.82

## Previous structured update

The prior Friday synthesis for 2026-06-05 focused on identity-bound MCP data planes and runtime-contract integrity: [week ending 2026-06-05 roundup](../roundups/2026-06-05.md).
