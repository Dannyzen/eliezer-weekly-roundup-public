# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-09

### Deterministic pre-execution gates expose silent policy violations

Summary: Reason Less, Verify More shows that tool-using agents can leave silent wrong states when policy-permissive tools execute valid-looking but forbidden writes. Read-only pre-execution gates check proposed writes against current state before execution, raising tau-squared-bench airline success from 29.6% to 42.0% on gpt-4o-mini in the reported setup.

Analysis: [daily sovereignty analysis](2026-07-09/sovereignty.md#deterministic-pre-execution-gates-expose-silent-policy-violations)
Durable topics: [Agent Execution Control Plane](agent-execution-control-plane/agent-execution-control-plane.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [Reason Less, Verify More](https://arxiv.org/abs/2607.07405v1)
Implementable now:
- put read-only policy gates before state-changing tools
- inspect current state, requested transition, principal, task, and approval artifact before writes
- emit allow and deny traces with gate ID, inspected fields, reason code, and state snapshot reference
Tools, repos, and methodologies worth exploring:
- deterministic state-transition validators, OPA or Cedar policy checks, pre-write gate fixtures, tau-squared-bench-style policy-permissive domains, allow and deny trace schemas
Implementability score: 0.86

### HalluSquatting turns resource identifiers into a supply-chain boundary

Summary: Agentic Botnets shows that model-hallucinated repositories, skills, or resources can be squatted by attackers and later fetched by agents. The defense is catalog and source control, not prompt steering: exact owner and artifact verification before clone, install, skill load, or MCP-server admission.

Analysis: [daily sovereignty analysis](2026-07-09/sovereignty.md#hallusquatting-turns-resource-identifiers-into-a-supply-chain-boundary)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Untrusted Data Boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md), [Agent Execution Control Plane](agent-execution-control-plane/agent-execution-control-plane.md)
Core source: [Agentic Botnets and HalluSquatting](https://arxiv.org/abs/2607.07433v1)
Implementable now:
- deny clone, install, or skill-load actions from model-guessed names unless a trusted source supplied the exact URL
- verify owner, repository, registry, publisher, and canonical URL before artifact fetch
- maintain allowed-source lists for skills, MCP servers, packages, plugins, and GitHub repositories
Tools, repos, and methodologies worth exploring:
- strict-known marketplace policies, signed manifests, GitHub owner and default-branch verification, package registry metadata checks, artifact checksums, catalog admission logs
Implementability score: 0.82

## Supporting recent Strategy context

The 2026-07-08 Deep Dive said writable context is not execution authority until it passes a typed release gate. The 2026-07-09 scan makes the same point operational: state-changing tools need pre-write gates, and resource acquisition needs exact identity checks before a model-generated name can become a real artifact fetch.
