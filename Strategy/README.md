# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-22 Friday Synthesis

### Agent gateway admission now means semantic API readiness plus MCP auth
Summary: Valid API specs are not automatically agent-ready, and remote MCP discovery is not an authorization boundary. The week’s strongest strategy finding is to gate tools before agents can reach them.

Analysis: [weekly sovereignty analysis](2026-05-22/sovereignty.md#agent-gateway-admission-now-means-semantic-api-readiness-plus-mcp-auth)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [OpenAPI agent-readiness gates](https://arxiv.org/abs/2605.14312), [remote MCP auth measurement](https://arxiv.org/abs/2605.22333)
Implementable now:
- run semantic API-readiness checks before MCP exposure;
- block unauthenticated non-public MCP servers;
- gate dynamic client registration;
- enforce scoped OAuth/OIDC, PKCE, redirect pinning, token rotation, and audit logs;
- log discovery, authorization, denial, approval, and final tool effects.
Tools, repos, and methodologies worth exploring:
- MCP Inspector, Microsoft Agent Governance Toolkit, OAuth 2.1/OIDC conformance tests, OPA/Cedar, Cloudflare Access/AI Gateway patterns, shadow-MCP scans
Implementability score: 0.84

### Memory is now an authorization surface
Summary: Persistent memory can change future actions, so it needs provenance, trust tiers, taint labels, deletion handling, review controls, and action-time policy checks. Memory is authority, not just recall.

Analysis: [weekly sovereignty analysis](2026-05-22/sovereignty.md#memory-is-now-an-authorization-surface)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [memory-lineage authorization](https://arxiv.org/abs/2605.14421), [faulty memory consolidation](https://arxiv.org/abs/2605.12978), [sleeper memory poisoning](https://arxiv.org/abs/2605.15338)
Implementable now:
- separate raw events from promoted memory and user preferences;
- attach source, timestamp, trust tier, consent, deletion state, and taint labels;
- require review before low-trust memory influences side effects;
- test stale-premise, deletion, conflict, and poisoning cases.
Tools, repos, and methodologies worth exploring:
- provenance IDs, memory ACLs, taint tracking, writeback firewalls, user-consent gates, OPA/Cedar action-time policy
Implementability score: 0.68

### Managed agents are becoming brain, sandbox, and steering-plane infrastructure
Summary: Enterprise agent deployment is splitting into model brain, sandboxed hands, and operator steering plane. The operator needs inventory, policy, audit, model routing, network controls, and revocation.

Analysis: [weekly sovereignty analysis](2026-05-22/sovereignty.md#managed-agents-are-becoming-brain-sandbox-and-steering-plane-infrastructure)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [Copilot cloud-agent audit API](https://github.blog/changelog/2026-05-18-audit-repository-copilot-cloud-agent-configuration-via-the-rest-api), [Cloudflare Claude managed agents](https://blog.cloudflare.com/claude-managed-agents/), [Dell Codex Enterprise partnership](https://openai.com/index/dell-codex-enterprise-partnership)
Implementable now:
- inventory managed agents by repo/project, writable root, token class, model, network mode, and approval state;
- route privileged work through sandbox profiles;
- log commands, approvals, network decisions, model routing, and PR lifecycle events;
- require per-repo configuration audits before broad delegation.
Tools, repos, and methodologies worth exploring:
- GitHub Copilot cloud-agent audit APIs, Cloudflare Sandbox, Cloudflare Access, private network connectors, OpenTelemetry traces, repo policy manifests, sandbox profiles
Implementability score: 0.73

### Security eval needs coverage maps, not benchmark name-dropping
Summary: Agent security evidence needs Target x Technique coverage maps tied to runtime controls. A benchmark name alone does not prove coverage of MCP, browser, shell, memory, skills, files, credentials, or CI paths.

Analysis: [weekly sovereignty analysis](2026-05-22/sovereignty.md#security-eval-needs-coverage-maps-not-benchmark-name-dropping)
Durable topic: [Agent Network Containment](agent-network-containment/agent-network-containment.md)
Core sources: [LLM security coverage maps](https://arxiv.org/abs/2605.15118), [agent permissioning](https://arxiv.org/abs/2605.14460), [semantic skill scanning](https://arxiv.org/abs/2605.14859), [Snyk Agent Scan](https://github.com/snyk/agent-scan)
Implementable now:
- maintain Target x Technique coverage maps for memory, MCP, browser, shell, files, credentials, CI, and code-review paths;
- list untested cells explicitly;
- require permission manifests for skills/tools;
- bind security-eval output to trace artifacts and gateway logs.
Tools, repos, and methodologies worth exploring:
- coverage matrices, MITRE-style threat mapping, Snyk Agent Scan, permission manifests, semantic fuzzing, MCP auth tests, sandbox escape tests
Implementability score: 0.69

## Previous structured update

The prior strategy scan for 2026-05-22 focused narrowly on remote MCP authentication. This Friday synthesis folds that finding into the broader weekly control-plane model.
