# Agent Gateway Governance

Agent gateway governance is the control-plane discipline for exposing enterprise tools, data, and workflows to autonomous agents.

The gateway should not be a thin MCP proxy. It should be the place where identity, tool discovery, authorization, semantic policy, approval, fuzzing, tracing, and audit evidence meet.

## Why this topic now

Two current signals converge:
- *From CRUD to Autonomous Agents* proposes a formally validated, zero-trust Semantic Gateway governed by MCP.
- Jarvis Registry shows a practical open-source product shape for MCP/A2A gatewaying with identity, access control, discovery, audit, tracing, and metrics.

Core sources:
- Semantic Gateway paper: https://arxiv.org/abs/2604.25555v1
- Jarvis Registry: https://github.com/ascending-llc/jarvis-registry

## Core thesis

Agents should not receive raw enterprise API access. They should receive a governed semantic tool surface.

That means:
- every agent or workflow has identity;
- every tool has explicit authorization requirements;
- tool discovery is scoped by policy;
- high-risk transitions require signed approval;
- trajectories can be fuzzed against unauthorized-state goals;
- traces record what was enabled, selected, denied, approved, and executed.

## Control layers

### 1. Identity

Use OIDC/OAuth-backed identity for users, agents, and workflows. Do not let a generic “agent service account” become the universal principal.

### 2. Tool discovery

Discovery should be permissioned. An agent should not even see tools outside its scope unless the system has a deliberate reason to expose them.

### 3. Semantic firewall

A semantic firewall inspects intended action meaning before privileged execution. It should sit before tool selection or before execution, depending on the system design.

### 4. Tool-level RBAC

RBAC needs to be deterministic and auditable. Natural language intent should not be the only control.

### 5. Human approval

Approval should be out-of-band and trace-linked for high-risk state transitions. A signed approval artifact is stronger than an ephemeral chat acknowledgement.

### 6. Enabled-tool graph audit

The gateway should expose enough structure to analyze which state transitions are possible under a given tool set and policy configuration.

### 7. Observability

Gateway events should emit traces, metrics, and audit logs that operators can replay.

## What to build now

- Put a gateway in front of internal MCP servers and privileged tool APIs.
- Assign identities and scopes to each agent workflow.
- Maintain an enabled-tool graph per workflow.
- Log policy decisions and approval artifacts with the agent trace.
- Add multi-turn adversarial tests that try to produce unauthorized state transitions.
- Treat gateway policy changes like infrastructure changes: reviewed, tested, and versioned.

## What to avoid

Avoid these traps:
- exposing all MCP tools to all agents;
- treating MCP as a security boundary by itself;
- hiding policy decisions inside prompts;
- approving high-risk actions without durable artifacts;
- collecting traces that omit disabled tools, denied calls, or approval context.

## May 1 update: gateway policy needs identity and data-flow tests

MCPHunt and Agent Name Service sharpen this topic from two sides. MCPHunt shows why gateway governance must test information flow, not only tool authorization: canary secrets can propagate across multi-server MCP workflows even when each component looks benign. Agent Name Service shows one plausible infrastructure direction for internal deployments: DIDs, verifiable credentials, OPA, Kubernetes CRDs, admission controls, and service-mesh integration.

Practical update:
- add taint/canary propagation tests to gateway CI
- log data class, source, destination, and redaction state on tool calls
- bind agent identities to workload identities instead of generic service accounts
- gate discovery and capability claims through policy-as-code
- treat MCP server output and peer-agent messages as untrusted until policy says otherwise

Sources:
- [MCPHunt](https://arxiv.org/abs/2604.27819)
- [MCPHunt repo](https://github.com/lihaonan0716/MCPHunt)
- [Agent Name Service](https://arxiv.org/abs/2604.26997)

## May 4 update: the AI gateway is becoming a security control plane

Palo Alto Networks’ intent to acquire Portkey is strong market validation for this topic. Portkey is framed as an AI Gateway for autonomous agents, and Palo Alto says it will become the AI Gateway for Prisma AIRS. The important product shape is not only model routing. It is centralized visibility, routing, security policy, governance policy, guardrails, agent identity, observability, and runtime inspection for agent-to-agent and agent-to-tool traffic.

Portkey’s own Agent Gateway language matches the same control-plane pattern: register agents, give each a governed endpoint, track MCP calls, enforce budgets and RBAC, preserve traces, and manage skills/capabilities through an agent registry.

Practical update:
- put agent and model traffic through a gateway before privileged tools or providers
- assign identity and owner metadata to every agent endpoint
- log model calls, MCP calls, denied calls, fallback decisions, budget events, and policy decisions
- enforce routing, cost, data-class, guardrail, and tool-scope rules at the gateway
- treat the gateway as part of security operations, not only developer middleware

Sources:
- [Palo Alto Networks to acquire Portkey](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-to-acquire-portkey-to-secure-the-rise-of-ai-agents)
- [Portkey Agent Gateway](https://portkey.ai/blog/agent-gateway/)
- [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway)

## May 6 update: MCP should carry security checks, not only tools

MOSAIC-Bench and GitHub's MCP Server updates sharpen the developer-workflow version of gateway governance. Staged coding tasks can compose into vulnerable software even when each ticket looks benign. The response cannot be only a better refusal prompt. The agent loop needs deterministic security checks before commit.

GitHub's secret scanning through MCP is now generally available, and dependency vulnerability scanning is in public preview through the Dependabot toolset. That is the right product shape: the agent asks the gateway to inspect current changes, receives structured findings, and fixes issues before the diff becomes a committed artifact.

Practical update:
- expose secret scanning, dependency scanning, and code scanning as first-class MCP tools
- require those tools before commit, package-manifest changes, deployment config changes, or credential-adjacent edits
- preserve scanner findings, affected files, severity, recommended fixes, and bypass decisions in the trace
- use adversarial reviewer or pentester framing for multi-ticket changes that may compose into a vulnerable end state
- treat scanner configuration as gateway policy that is versioned and reviewed like infrastructure

Sources:
- [MOSAIC-Bench](https://arxiv.org/abs/2605.03952)
- [GitHub MCP secret scanning GA](https://github.blog/changelog/2026-05-05-secret-scanning-with-github-mcp-server-is-now-generally-available)
- [GitHub MCP dependency scanning preview](https://github.blog/changelog/2026-05-05-dependency-scanning-with-github-mcp-server-is-in-public-preview)
- [github/github-mcp-server](https://github.com/github/github-mcp-server)

## May 7 update: runtime safety should intercept tool calls before execution

AgentTrust and DTap sharpen gateway governance from policy configuration into execution-path safety. AgentTrust intercepts proposed side-effecting actions before they run and returns structured verdicts: allow, warn, block, or review. DTap provides controllable red-team environments and task-runner infrastructure for evaluating agents under benign and malicious scenarios. The deployment-alignment paper supplies the governance frame: model-level benchmarks alone cannot justify deployment-level safety claims.

The gateway lesson is direct. A sandbox controls where execution happens, but the gateway must understand what action is being attempted. Shell commands, file operations, HTTP calls, database mutations, email, payments, and deployments should pass through a normalizer and policy/interception layer before side effects occur.

Practical update:
- normalize shell commands, URLs, file paths, and database actions before safety judgment
- return verdict, risk category, safer alternative, policy reason, and evidence path as structured data
- reserve LLM-as-judge for ambiguous semantic meaning; keep deterministic allow/deny rules for clear policy boundaries
- build DTap-style benign/malicious workflow fixtures for internal agent evaluations
- label safety evidence by model, response, interaction, and deployment level
- store every verdict and bypass decision in the agent trace

Sources:
- [AgentTrust](https://arxiv.org/abs/2605.04785)
- [DTap](https://arxiv.org/abs/2605.04808)
- [BillChan226/dtap-neurips](https://github.com/BillChan226/dtap-neurips)
- [Deployment-Relevant Alignment Cannot Be Inferred from Model-Level Evaluation Alone](https://arxiv.org/abs/2605.04454)

## May 8 update: manuals should become machine-checkable trace policies

MANTRA adds the procedural-compliance version of gateway governance. Many high-risk agent failures are not obviously malicious tool calls. They are valid-looking actions in the wrong order, without the required prerequisite, without the right approval, or after the workflow has entered a state where the action is no longer allowed.

The practical update:
- choose one critical SOP and one tool schema, then model required states, prerequisites, approvals, ordering constraints, and forbidden terminal states
- validate traces with state-machine or SMT-style checks before relying on LLM judges
- attach compliance verdicts to the agent trace with policy ID, manual section, violated step, and remediation hint
- run adversarial procedural tasks that tempt agents to skip approval, reorder steps, or satisfy the final goal through an invalid path
- expose deterministic trace validators through the gateway and CI so violations block deployment or execution

The strategic point is that manuals should not remain PDFs next to an autonomous tool surface. Serious agent gateways will compile procedures into executable policy artifacts and then collect trace evidence that those policies were followed.

Source:
- [MANTRA](https://arxiv.org/abs/2605.06334)

## May 18 update: API documentation needs semantic readiness gates

The OpenAPI agent-readiness study sharpens gateway governance at the tool-surface layer. An internal API can be structurally valid, stable, and useful to humans while still being a bad agent tool. In the reported industrial setting, MCP-based agents failed at task planning, tool selection, and payload construction across an ecosystem of 16 production APIs and roughly 600 endpoints. The researchers’ Hermes system found 2,450 documentation and REST smells, with deficiencies present in all analyzed operations.

The gateway lesson is direct: do not bulk-wrap enterprise APIs as MCP tools and call that modernization. Tool exposure needs a readiness gate that checks whether an autonomous planner can understand parameter semantics, constraints, examples, error behavior, and endpoint boundaries.

Practical lesson:
- run semantic OpenAPI linting before MCP/tool exposure
- require descriptions, examples, constraints, and failure modes for agent-visible parameters
- generate tool-use tests from endpoint specs and replay payload-construction failures
- expose selected endpoints first, not the whole microservice estate
- treat documentation fixes as gateway policy work, not only docs cleanup

Source:
- [Making OpenAPI Documentation Agent-Ready](https://arxiv.org/abs/2605.14312)

## May 19 update: managed coding agents need repo-level configuration inventory

GitHub’s Copilot cloud-agent configuration API makes a core governance requirement explicit: operators need repo-level inventory before they can safely delegate work to cloud agents at scale. The API exposes MCP server configuration, enabled tools, GitHub Actions workflow policy, and firewall configuration. The adjacent releases — one-click Actions fixes and cheaper model choices for simple delegated tasks — make the inventory even more important because the agent is now part of CI repair and model-routing policy.

The enterprise direction is broader than GitHub. OpenAI and Dell’s Codex partnership frames coding agents as hybrid/on-prem enterprise infrastructure near codebases, documents, systems of record, and operational knowledge. That reinforces the same gateway thesis: agent placement, data boundary, tool authority, model choice, and audit trail have to be governed together.

Practical lesson:
- inventory enabled tools, MCP servers, workflow policy, firewall configuration, and model policy per repository
- diff agent configuration like infrastructure, not personal settings
- route low-risk CI/lint fixes to cheaper models only when branch protection and review gates remain intact
- require trace-linked review for cloud-agent commits before merge
- treat hybrid/on-prem coding-agent deployment as a data-governance and control-plane decision

Sources:
- [Audit repository Copilot cloud agent configuration via the REST API](https://github.blog/changelog/2026-05-18-audit-repository-copilot-cloud-agent-configuration-via-the-rest-api)
- [One-click fixes for failing Actions with Copilot cloud agent](https://github.blog/changelog/2026-05-18-one-click-fixes-for-failing-actions-with-copilot-cloud-agent)
- [Copilot cloud agent: Fast, cost-efficient models for simple tasks](https://github.blog/changelog/2026-05-18-copilot-cloud-agent-fast-cost-efficient-models-for-simple-tasks)
- [OpenAI and Dell Technologies partner to bring Codex to hybrid and on-premises enterprise environments](https://openai.com/index/dell-codex-enterprise-partnership)

## May 22 update: remote MCP auth needs gateway-owned client registration
The first measurement study of real-world remote MCP authentication turns the gateway thesis into an urgent control-plane requirement. The paper reports 7,973 live remote MCP servers, with 40.55% exposing tools without authentication. In a tested sample of 119 OAuth-enabled servers, every server had at least one flaw, and dynamic client registration flaws affected 96.6%.

The strategic lesson is direct: OAuth support is not the same as secure agent authorization. Remote MCP deployments combine open client environments, dynamic client registration, delegated authorization, and side-effecting tools. That boundary needs gateway ownership, not blind client trust.

Practical lesson:
- require auth on every non-public remote MCP server;
- disable or tightly constrain dynamic client registration;
- pin redirect URIs and client metadata for trusted agent clients;
- enforce scoped OAuth/OIDC, PKCE, token rotation, and per-tool authorization;
- scan for unauthenticated tools, weak registration, redirect manipulation, token leakage, and overbroad scopes;
- log discovery, enabled tools, denied calls, approvals, auth context, and final tool effects;
- treat third-party remote MCP servers as untrusted until their auth behavior is tested.

Sources:
- [A First Measurement Study on Authentication Security in Real-World Remote MCP Servers](https://arxiv.org/abs/2605.22333)
- [Measuring Security Without Fooling Ourselves](https://arxiv.org/abs/2605.22568)
- [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit)
- [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)

## May 23 update: gateway policy needs MCP client capability inventory

The `evalstate/mcp-clients` dataset is useful because it turns MCP client heterogeneity into observable data. Clients advertise different combinations of UI, elicitation, roots, sampling, tasks, and experimental auth capabilities. Gateway policy should not treat all MCP clients as equivalent just because they speak the protocol.

Practical lesson:
- inventory client name, version, and advertised capabilities during MCP connection setup;
- gate high-risk features such as UI rendering, elicitation, roots, sampling, task execution, and experimental auth by client identity and policy;
- diff client-capability changes like infrastructure changes;
- log client capability, selected tools, denied tools, auth context, and final effects in the same trace;
- use live capability telemetry to prioritize gateway test cases.

Source:
- [evalstate/mcp-clients](https://huggingface.co/datasets/evalstate/mcp-clients)

## Implementability score

0.76

The ingredients exist: MCP gateways, OAuth/OIDC, RBAC engines, OPA/Cedar, OpenTelemetry, Prometheus, and adversarial test harnesses. The hard part is integrating them into a coherent control plane without making the gateway unusable.
