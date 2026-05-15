# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-15 Friday Synthesis

### Coding agents are now managed endpoints and live sessions
Summary: Codex and Copilot updates show coding agents becoming privileged live systems: local sandboxes, remote SSH hosts, mobile controllers, hooks, REST-startable cloud tasks, agent secrets, isolated sessions, auto model routing, and PR automation. Treat each agent session as a managed principal.

Analysis: [sovereignty analysis](2026-05-15/sovereignty.md#coding-agents-are-now-managed-endpoints-and-live-sessions)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources:
- [Running Codex safely](https://openai.com/index/running-codex-safely)
- [openai/codex](https://github.com/openai/codex)
- [Codex Windows sandbox](https://openai.com/index/building-codex-windows-sandbox)
- [Work with Codex from anywhere](https://openai.com/index/work-with-codex-from-anywhere)
- [GitHub Copilot app technical preview](https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview)
- [Start Copilot cloud agent tasks via REST API](https://github.blog/changelog/2026-05-13-start-copilot-cloud-agent-tasks-via-the-rest-api)
- [Copilot cloud agent auto model selection](https://github.blog/changelog/2026-05-14-copilot-cloud-agent-supports-auto-model-selection)
Implementable now:
- require per-session identity with repo, branch, host, writable roots, network mode, model, token class, and approval state
- enforce sandbox and network policy before granting write or shell authority
- log prompts, approvals, commands, network decisions, model routing, token usage, and PR lifecycle events
- use hooks for secret scanning, validators, logging, and repository-specific memory
Tools, repos, and methodologies worth exploring:
- Codex, Copilot cloud agent, Starlark command rules, OS sandboxes, OpenTelemetry, endpoint logs, scoped access tokens, agent-secret stores
Implementability score: 0.78

### Prompt injection is now a parameter and dataflow security problem
Summary: Microsoft’s Semantic Kernel RCE post showed prompt injection becoming code execution through model-influenced tool parameters. Enterprise retrieval and GitHub Actions agentic workflow papers generalize the problem: untrusted content can flow into tools, tenant data, CI variables, secrets, scripts, and workflow outputs.

Analysis: [sovereignty analysis](2026-05-15/sovereignty.md#prompt-injection-is-now-a-parameter-and-dataflow-security-problem)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources:
- [Microsoft: When prompts become shells](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
- [Enterprise retrieval and tool-use security](https://arxiv.org/abs/2605.05287)
- [Agentic workflow injection in GitHub Actions](https://arxiv.org/abs/2605.07135)
- [Copilot cloud agent secrets docs](https://docs.github.com/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/configure-secrets-and-variables)
- [GitHub agent secrets update](https://github.blog/changelog/2026-05-08-more-flexible-secrets-and-variables-for-copilot-cloud-agent)
Implementable now:
- validate and canonicalize tool parameters before execution
- remove internal helper functions from model-callable tool surfaces
- taint retrieved text, issue bodies, PR comments, web pages, and generated workflow data
- block dangerous sinks unless policy grants the exact action
Tools, repos, and methodologies worth exploring:
- schema validators, AST allowlists, taint tracking, OPA/Cedar, CodeQL, secret scanning, dependency scanning, sandboxed tool workers
Implementability score: 0.74

### MCP and browser authorization need scoped consent and live indirect-injection tests
Summary: Options, Not Clicks makes MCP authorization an option-level consent problem. IPI-proxy shows why approved web domains still need live indirect-injection testing. WARD adds the guardrail shape: run a parallel sidecar over task intent, HTML, screenshots, proposed actions, and context.

Analysis: [sovereignty analysis](2026-05-15/sovereignty.md#mcp-and-browser-authorization-need-scoped-consent-and-live-indirect-injection-tests)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources:
- [Consent-driven MCP authorization](https://arxiv.org/abs/2605.11360v1)
- [IPI-proxy](https://arxiv.org/abs/2605.11868v1)
- [WARD](https://arxiv.org/abs/2605.15030v1)
- [WARD-WebAgent](https://github.com/caothientri2001vn/WARD-WebAgent)
- [WARD-0.8b](https://huggingface.co/tricao1105/WARD-0.8b)
- [WARD-2b](https://huggingface.co/tricao1105/WARD-2b)
Implementable now:
- replace broad tool consent with argument-level or option-level grants
- run indirect prompt injection tests through an intercepting proxy against approved web domains
- run parallel guard checks over task, HTML, screenshot, URL, action, and prior tool context
- emit structured guard verdicts with evidence and policy actions
Tools, repos, and methodologies worth exploring:
- WARD, IPI-proxy, browser-agent red-team fixtures, policy lattices, scoped tokens, guard sidecars, OpenTelemetry spans
Implementability score: 0.74

### Always-on agents need provenance gates action digests and OS containment
Summary: Sleeper Channels frames persistent agents as authority-boundary systems: messaging, memory, self-authored skills, scheduling, shell, and filesystem can turn low-trust reads into delayed writes. MCPShield and Codex sandbox work add tool-call monitoring and OS-level containment.

Analysis: [sovereignty analysis](2026-05-15/sovereignty.md#always-on-agents-need-provenance-gates-action-digests-and-os-containment)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md)
Core sources:
- [Sleeper Channels](https://arxiv.org/abs/2605.13471)
- [maloyan/sleeper-channels](https://github.com/maloyan/sleeper-channels)
- [MCPShield](https://arxiv.org/abs/2605.11053)
- [Codex Windows sandbox](https://openai.com/index/building-codex-windows-sandbox)
Implementable now:
- attach provenance IDs to memories, skills, files, commands, and scheduled tasks
- compute action digests before high-risk side effects
- require policy gates when low-trust provenance reaches shell, filesystem writes, credential access, outbound network, or skill creation
- separate online and offline sandbox principals where possible
Tools, repos, and methodologies worth exploring:
- provenance graphs, action manifests, sandbox users, firewall rules, immutable audit logs, signed skill packages, endpoint detection
Implementability score: 0.58

### Tool-call routing is budget governance not model shopping
Summary: Switchcraft and GitHub’s token-efficiency practices make model choice a governance layer. Route by schema-aware correctness, real cost, token budget, tool behavior, and traceability; do not treat routing as generic model shopping.

Analysis: [sovereignty analysis](2026-05-15/sovereignty.md#tool-call-routing-is-budget-governance-not-model-shopping)
Durable topic: [Model Router Governance](model-router-governance/model-router-governance.md)
Core sources:
- [Switchcraft](https://arxiv.org/abs/2605.07112)
- [GitHub token-efficiency practices](https://github.blog/ai-and-ml/github-copilot/improving-token-efficiency-in-github-agentic-workflows/)
- [Copilot cloud agent auto model selection](https://github.blog/changelog/2026-05-14-copilot-cloud-agent-supports-auto-model-selection)
Implementable now:
- log model, provider, input/output/cache tokens, tool calls, retries, and outcome per workflow phase
- compute effective-token or normalized-cost metrics
- route differently for schema-heavy calls, retrieval, planning, code edits, and verification
- keep routing traces auditable so cost savings do not hide lower tool correctness
Tools, repos, and methodologies worth exploring:
- Switchcraft, LiteLLM, semantic routers, RouteLLM-style evals, BFCL-style tool-call tests, budget ledgers, model-router audit logs
Implementability score: 0.78

### Least-privilege skills and host isolation are a sovereignty layer
Summary: SkillScope, TEE-backed isolation work, and CyberSecQwen point toward a long-term sovereignty layer where skills and specialized security models enforce least privilege before actions reach the host. Near-term work is permission metadata, action classification, and isolated workers; high-assurance TEE deployments remain architecture-heavy.

Analysis: [sovereignty analysis](2026-05-15/sovereignty.md#least-privilege-skills-and-host-isolation-are-a-sovereignty-layer)
Durable topic: [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md)
Core sources:
- [SkillScope-style least-privilege analysis](https://arxiv.org/abs/2605.05868)
- [TEE-backed isolation for agents](https://arxiv.org/abs/2605.06393)
- [CyberSecQwen](https://huggingface.co/blog/lablab-ai-amd-developer-hackathon/cybersecqwen-4b)
Implementable now:
- add permission metadata to every skill and tool
- classify operations as read-only, write, network, credential, shell, memory-write, skill-write, or destructive
- run high-risk skills in isolated workers with narrow filesystem and network access
- use specialized local security models for triage, not as the only guard
Tools, repos, and methodologies worth exploring:
- permission manifests, signed skills, worker sandboxes, seccomp/AppArmor/Seatbelt, VM isolation, local security classifiers, TEE-backed workers for high-trust deployments
Implementability score: 0.55
