# Agent Gateway Governance

Last updated: 2026-06-27

Agent gateway governance is the control-plane discipline for exposing enterprise tools, data, and workflows to autonomous agents.

The gateway should not be a thin MCP proxy. It should be the place where identity, tool discovery, authorization, semantic policy, approval, fuzzing, tracing, and audit evidence meet.

## Why this topic now

The June 3 signal is stronger than the original gateway thesis. Google made object storage directly agent-addressable through the GCS MCP server. AWS framed AgentCore Gateway as the production control point for MCP servers. NSA's MCP guidance made the security case explicit. A same-day authorization paper supplied the formal vocabulary: recursive delegation, contextual scope, and capability attenuation.

Older sources still matter: *From CRUD to Autonomous Agents* proposed a zero-trust Semantic Gateway governed by MCP, and Jarvis Registry showed a practical open-source product shape for MCP/A2A gatewaying with identity, access control, discovery, audit, tracing, and metrics.

Core sources:
- GCS MCP server: https://cloud.google.com/blog/topics/developers-practitioners/build-ai-agents-faster-with-gcs-google-cloud-storage-mcp-server/
- AgentCore Gateway MCP support: https://aws.amazon.com/blogs/machine-learning/extending-mcp-support-for-amazon-bedrock-agentcore-gateway-2/
- AgentCore Gateway auth code flow: https://aws.amazon.com/blogs/machine-learning/building-a-secure-auth-code-flow-setup-using-agentcore-gateway-with-mcp-clients/
- Overlaying Governance: https://arxiv.org/abs/2606.03518
- NSA MCP security release: https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/
- Semantic Gateway paper: https://arxiv.org/abs/2604.25555v1
- Jarvis Registry: https://github.com/ascending-llc/jarvis-registry
- Agentic Resource Discovery: https://commandline.microsoft.com/agentic-resource-discovery-specification-ard/
- ToolPrivBench: https://arxiv.org/abs/2606.20023v1

## Core thesis

Agents should not receive raw enterprise API access. They should receive a governed semantic tool surface.

That means:
- every agent or workflow has identity;
- every tool has explicit authorization requirements;
- tool discovery is scoped by policy;
- high-risk transitions require signed approval;
- trajectories can be fuzzed against unauthorized-state goals;
- traces record what was enabled, selected, denied, approved, and executed.

## Deep Dive Wednesday 2026-06-03 gateway as identity-bound MCP data plane

### Overview

The strongest finding from the 2026-05-28 to 2026-06-03 window is that the agent gateway is becoming the identity-bound MCP data plane. Google made object storage agent-addressable through a GCS MCP server. AWS framed AgentCore Gateway as the centralized control point for production MCP servers: fine-grained access control, credential custody, observability, exfiltration controls, private connectivity, policy interceptors, and user-bound OAuth flows. NSA's MCP guidance and the new compositional-authorization paper explain why this has to be treated as infrastructure, not connector glue.

This beat SkillGuard, DMF, SPOQ, and the other good AgenticAI findings because it sits at the blast-radius boundary. Skills, memory, subagents, and coding workflows eventually ask for tools, storage, SaaS, or admin systems. The gateway is where those requests become real effects.

### Core innovation

The important shift is from "the agent can call this tool" to "this principal, acting through this agent and session, may exercise this attenuated capability over this data boundary for this workflow, with this trace evidence."

That requires four primitives:

1. Principal binding: user, agent, client, server, session, task, and delegated authority are runtime fields, not prose in a system prompt.
2. Capability attenuation: authority narrows as it moves through tools, storage prefixes, generated artifacts, summaries, subagents, and delegated tasks.
3. Gateway-owned mediation: discovery, credentials, policy, interceptors, approvals, data projection, and exfiltration checks happen before the tool or storage system observes the full request.
4. Replayable evidence: traces record selected tools, denied tools, object paths, argument projections, auth claims, policy IDs, approval artifacts, and final effects.

### Why it matters

MCP is crossing from developer convenience into enterprise data-plane infrastructure. Object storage is often the memory lake, document archive, dataset staging area, log store, and report warehouse. Browser-security MCP servers, GitHub MCP tools, cloud-agent configuration APIs, and object-storage MCP servers are not low-risk integrations. They are authority surfaces.

If agents get broad storage, admin, or SaaS tools without gateway policy, the failure mode is not just a bad answer. It is data exposure, permission laundering, unreviewed policy mutation, credential sprawl, invisible external observation, or cross-session authority confusion.

### How it fits into the strategic layer

This belongs primarily in Strategy because the architectural decision is about sovereignty and operating model: who owns the boundary between agent intent and enterprise systems.

For Danny's worldview, the pattern is clear: serious agent products should not compete on "more MCP servers" alone. They should compete on governed MCP surfaces: scoped discovery, identity propagation, delegated authority, storage/data policies, trace evidence, and red-team fixtures that prove forbidden data flows stay forbidden.

### Practical tools, repos, and methodologies worth trying now

- Amazon Bedrock AgentCore Gateway for centralized MCP routing, dynamic listing, OAuth flows, Lambda interceptors, AgentCore Policy, private connectivity, and observability.
- Google Cloud Storage MCP server for testing object-store agents with IAM-backed access and Cloud Logging audit trails.
- OAuth/OIDC with PKCE, subject/claim propagation, and user-bound transport sessions.
- OpenFGA/Zanzibar-style relationship authorization for delegation chains and scoped resource graphs.
- OPA or Cedar for deterministic policy checks over tool, data, workflow, and approval fields.
- OpenTelemetry spans for gateway events: discovered tools, selected tools, denied tools, object paths, argument projection, auth claims, policy ID, approval artifact, and final effect.
- Canary and taint tests for permission laundering: read sensitive object, summarize/transform, then attempt an external send or cross-bucket write.
- MCP client capability inventory and remote-MCP auth scans before admitting third-party servers.

### Implementation complexity

The basic version is implementable now: put MCP servers behind a gateway, bind requests to identity, scope tools by workflow/data class, and log decisions.

The harder version needs real architecture: attenuating authority across transformations, propagating data-class labels through summaries, preventing speculative external observation, supporting recursive delegation, and testing policy with adversarial multi-tool trajectories.

### Implementability score

0.76

This is not a one-weekend script, but it is not speculative. The components exist. The hard work is integration discipline: policy schemas, identity propagation, gateway event models, test fixtures, and operator workflows.

### Strategic implications

- The winning agent platform is likely a governed data plane, not a chat UI with a large tool list.
- MCP registries and skill catalogs need admission control, not just discovery UX.
- Storage access is the new memory boundary. If object stores become agent-addressable, retention, provenance, data classification, and exfiltration policy have to move into the same runtime trace.
- Vendor gateways are becoming strategically important because they own credentials, telemetry, policy, and private connectivity. Local-first systems need a comparable control plane if they want sovereignty instead of cloud lock-in.
- Agentic products should sell replayable evidence: what the agent could see, what it could call, what it was denied, what data it touched, and why the final effect was allowed.

### Core source links

- Build AI agents faster with GCS MCP server: https://cloud.google.com/blog/topics/developers-practitioners/build-ai-agents-faster-with-gcs-google-cloud-storage-mcp-server/
- Extending MCP support for Amazon Bedrock AgentCore Gateway: https://aws.amazon.com/blogs/machine-learning/extending-mcp-support-for-amazon-bedrock-agentcore-gateway-2/
- Building a secure auth code flow setup using AgentCore Gateway with MCP clients: https://aws.amazon.com/blogs/machine-learning/building-a-secure-auth-code-flow-setup-using-agentcore-gateway-with-mcp-clients/
- NSA MCP security design considerations release: https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/
- Overlaying Governance: A Compositional Authorization Framework for Delegation and Scope in Agentic AI: https://arxiv.org/abs/2606.03518
- MCP Python SDK v1.27.2 release: https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.27.2

### What remains conceptual

The compositional-authorization paper gives the right language for recursive delegation and scope attenuation, but the referenced implementation repository did not resolve during verification. Treat it as a formal design direction, not a drop-in library. The deployable path today is still gateway engineering with existing IAM, OAuth/OIDC, policy-as-code, relationship authorization, logs, and adversarial fixtures.

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

GitHub’s Copilot cloud-agent configuration API makes a core governance requirement explicit: operators need repo-level inventory before they can safely delegate work to cloud agents at scale. The API exposes MCP server configuration, enabled tools, GitHub Actions workflow policy, and firewall configuration. The adjacent releases, one-click Actions fixes and cheaper model choices for simple delegated tasks, make the inventory even more important because the agent is now part of CI repair and model-routing policy.

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

## May 26 update: tool descriptions are part of the trusted computing base

When the Manual Lies makes the MCP governance problem sharper. Tool Description Poisoning hides malicious instructions in a tool’s descriptive metadata instead of executable code. That is enough to compromise planning because the agent reads the description as operational truth. Attested Tool-Server Admission points toward the control-plane response: server admission, bounded tool subsets, sensitivity labels, and contracts outside raw MCP self-declaration.

The gateway should treat tool descriptions, parameter docs, examples, and schemas as security-critical metadata. They need identity, versioning, diff review, semantic tests, and trace linkage.

Practical lesson:
- pin MCP server identity, tool list, schema digest, and description digest;
- review tool-description diffs like code changes before production exposure;
- maintain gateway-owned allowlists of admitted servers and tool subsets per workflow;
- fuzz descriptions, examples, parameter docs, and error messages for hidden instructions or misleading semantics;
- require declared data classes, side effects, and approval points in tool metadata;
- log metadata version and digest with every tool-call trace.

Sources:
- [When the Manual Lies](https://arxiv.org/abs/2605.24069)
- [Attested Tool-Server Admission](https://arxiv.org/abs/2605.24248)

## May 27 update: gateway policy must follow values across tools

ChainCaps names the gateway failure mode that per-tool RBAC misses: permission laundering. An agent can read sensitive data with one allowed tool, transform it with another allowed tool, and send the transformed result through a third allowed tool. Each call can pass local authorization while the whole trajectory violates the intended data-flow policy.

The practical correction is monotonic capability attenuation. Data should carry sink-specific authority through the tool chain. A transformation can preserve or reduce authority, but it should not create a new right to email, publish, exfiltrate, write to a database, or call an external API.

AgentSecBench and Cordon-MAS point in the same direction from different surfaces. Prompt annotations are not enforcement, and RAG systems can detect poisoned or contradictory evidence while still letting it influence the final answer. The gateway has to enforce projection, capability restriction, value lineage, and compartmentalized evidence flow before generation or side effects.

Practical lesson:
- classify tool outputs by data class, source, and allowed sinks;
- propagate capability metadata through tool results, summaries, transformations, and final actions;
- intersect authority across composition instead of resetting permissions at each tool boundary;
- require expert-reviewed manifests for high-risk tools because naive manifests collapse the guarantee;
- build adversarial multi-tool fixtures that test read-transform-send laundering, RAG poisoning, and forbidden-action distinguishers.

Sources:
- [ChainCaps](https://arxiv.org/abs/2605.26542)
- [AgentSecBench](https://arxiv.org/abs/2605.26269)
- [Cordon-MAS](https://arxiv.org/abs/2605.26754)

## May 28 update: tool catalogs need validation-carrying admission control

Tool Forge adds a concrete admission-control pattern for MCP-era tools. It treats a tool as a capsule with intent, capability contract, implementation, dependency policy, tests, documentation, runtime validation evidence, lifecycle state, credential bindings, and routing metadata. The router exposes intent-scoped tool sessions instead of dumping a full schema catalog into every prompt.

The gateway lesson is simple: generated code is not a capability until it has evidence. A serious agent gateway should distinguish generated, validated, reviewed, approved, deprecated, and revoked tools. Credential binding should happen at the gateway. Routing should include tool version, manifest digest, test status, and lifecycle state in the trace.

Practical lesson:
- require a `tool_card`-style manifest for every callable tool;
- sandbox-validate implementation behavior before catalog admission;
- pin dependency policy and credential scope separately from model-written code;
- route by intent-scoped sessions to reduce context bloat and exposed authority;
- log tool admission evidence and selected route with every invocation.

Sources:
- [Tool Forge paper](https://arxiv.org/abs/2605.28000)
- [nextmoca/tool-forge](https://github.com/nextmoca/tool-forge)

## Implementability score

0.77

The ingredients exist: MCP gateways, OAuth/OIDC, RBAC engines, OPA/Cedar, OpenTelemetry, Prometheus, and adversarial test harnesses. The hard part is integrating them into a coherent control plane without making the gateway unusable.

## May 29 update: privileged vendor MCP servers need gateway mediation

Google’s Chrome Enterprise Premium MCP server turns browser-security administration into an agent-callable surface: DLP rules, content detectors, connector policies, browser telemetry, license management, health checks, policy optimization, and investigation workflows.

That is useful and dangerous for the same reason. Enterprise browser security is a high-blast-radius admin plane. Exposing it through MCP should trigger gateway controls, not shortcut them. Diagnosis tools should not imply mutation authority. DLP and org-unit changes should have approval semantics, trace-linked before/after state, and rollback paths.

Practical lesson:
- put privileged MCP servers behind identity, scope, approval, and audit policy;
- separate read-only diagnosis from policy mutation tools;
- require scoped OAuth and per-workflow tool exposure;
- label agent-created policies and preserve rollback metadata;
- capture JSON-RPC/tool traces for operator review and compliance.

Sources:
- [Bringing AI agents to Chrome Enterprise security management](https://blog.google/security/bringing-ai-agents-to-chrome-enterprise-security-management/)
- [google/chrome-enterprise-premium-mcp](https://github.com/google/chrome-enterprise-premium-mcp)
- [Pocket CEP MCP example](https://github.com/google/ChromeBrowserEnterprise/tree/main/mcp-examples/pocket-cep)

## May 30 update: NSA guidance turns MCP security into production infrastructure work

NSA’s MCP Cybersecurity Information Sheet makes the gateway thesis explicit. MCP adoption has moved into production and sensitive workflows faster than its security model matured. The guidance names risks that are gateway-shaped: access control gaps, insecure serialization, poor approval workflows, token/session weaknesses, inconsistent behavior, missing audit logs, tool parameter injection, path confusion, repository access overreach, output poisoning, and remote-code-execution-style failures.

The same day’s implementation signal from `mcp-proto-okn` shows why the protocol will keep spreading. Schema-first, read-oriented MCP access to structured knowledge graphs is genuinely useful. The answer is not “avoid MCP.” The answer is to put MCP behind admission, policy, logging, and provenance.

Practical lesson:
- choose supported MCP projects and inventory stale/unsupported servers;
- design explicit boundaries for data, tools, users, workflows, and connected servers;
- validate parameters and restrict parameter forwarding;
- constrain and sandbox tool execution;
- monitor chained output pipelines before downstream automation trusts them;
- log tool identity, arguments, client, server, schema version, auth context, output lineage, approval artifact, and final effect;
- scan local and remote environments for exposed or vulnerable MCP servers.

Sources:
- [NSA MCP security release](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/)
- [mcp-proto-okn paper](https://arxiv.org/abs/2605.30283v1)
- [sbl-sdsc/mcp-proto-okn](https://github.com/sbl-sdsc/mcp-proto-okn)

## May 31 update: authenticated principal binding belongs inside MCP transport sessions

The official MCP Python SDK v1.27.2 release turns yesterday’s security guidance into a concrete implementation primitive: access tokens carry subject and claims, transport sessions bind to the authenticated principal, and experimental tasks are scoped to the session that created them.

That is the right gateway direction. MCP governance cannot depend on an agent remembering who it is or a wrapper prompt describing trust boundaries. The runtime needs principal, client, server, session, task origin, and delegated authority as first-class fields that policy can enforce and traces can audit.

Practical lesson:
- require principal-bound transport sessions for privileged MCP servers;
- log subject, claims, client identity, server identity, session ID, task origin, selected tool, and final effect;
- scope background tasks, cancellation, resume, and message delivery to the creating session unless explicit delegation exists;
- write cross-session access tests for task reads, task writes, cancellation, and resumed tool calls;
- treat MCP SDK upgrades as security-relevant infrastructure changes, not routine dependency noise.

Sources:
- [modelcontextprotocol/python-sdk v1.27.2](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.27.2)
- [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)

## June 1 update: regulated agents need organization-scoped runtime context

The organization-scoped cybersecurity-runtime paper turns gateway governance into a full runtime-context problem. A regulated SOC agent should not start from a generic prompt plus tool list. It should start from a typed Security Context created at every entry point, including SIEM/XDR notifications, and that context should be enforced across retrieval, tool calls, memory, structured findings, reports, human gates, and append-only audit.

The practical correction is to stop treating enterprise tool access as a set of disconnected MCP permissions. The gateway needs to carry organization, analyst, trigger, data scope, evidence state, approval tier, and final-report obligations through the whole run.

Practical lesson:
- create typed organization/security context at every workflow entry point;
- expose SIEM/XDR operations through governed adapters, not raw tool calls;
- require evidence-linked structured findings before reports or response actions;
- tier HITL gates by blast radius and evidence confidence;
- store context creation, tool calls, approvals, findings, and report emissions in append-only audit.

Source:
- [An Organization-Scoped LLM Agent Runtime Architecture for Regulated Cybersecurity Operations](https://arxiv.org/abs/2605.30604)

## June 2 update: speculative tool calls need issue-time privacy contracts

Ghost Tool Calls names the privacy failure in latency-optimized agents. A tool-using agent can speculatively issue future tool calls before it commits to a branch. If the branch is abandoned, the external service still observed the request and can infer user intent. Read-only restrictions and allow-lists do not solve this because the leak is observation before commitment, not mutation after commitment.

The gateway correction is to treat external observation as an effect. Speculative planning can happen locally, but speculative dispatch to an external service needs issue-time policy: suppress the call, change the destination, or project/redact the arguments before the observer sees them.

Practical lesson:
- separate local speculation from external speculative dispatch;
- classify observation, mutation, and disclosure as distinct effects;
- require issue-time policy before any precommit external tool call;
- project or redact speculative arguments by data class and destination;
- log branch state, speculative calls, suppressed calls, argument projection, observer, and final commit path.

Source:
- [Ghost Tool Calls](https://arxiv.org/abs/2606.02483v1)

## June 3 update: object storage MCP makes the gateway a data-plane boundary

Google’s GCS MCP server shows that object storage is becoming directly agent-addressable. AWS’s AgentCore Gateway MCP posts show the necessary control envelope: user-bound authorization, fine-grained access control, centralized credentials, observability, and exfiltration controls. Together they move MCP from tool convenience into enterprise data-plane infrastructure.

The gateway lesson is direct. A bucket, prefix, or enterprise storage namespace is not a harmless tool. It is often the memory lake, document archive, logs store, dataset staging area, and report warehouse. An agent should not receive broad storage tools because a prompt says it is helpful. It should receive scoped capabilities bound to user identity, workflow purpose, data class, and audit policy.

Practical lesson:
- put object-storage MCP servers behind gateway-owned identity and policy;
- bind requests to user, agent, client, server, session, workflow, and delegated authority;
- scope storage tools by bucket, prefix, data class, action type, and retention tier;
- log object path, selected tool, denied tool, argument projection, auth claims, approval artifact, and final effect;
- test overbroad prefix access, export exfiltration, permission laundering, weak OAuth registration, and missing audit fields.

Sources:
- [GCS MCP server](https://cloud.google.com/blog/topics/developers-practitioners/build-ai-agents-faster-with-gcs-google-cloud-storage-mcp-server/)
- [AgentCore Gateway auth code flow](https://aws.amazon.com/blogs/machine-learning/building-a-secure-auth-code-flow-setup-using-agentcore-gateway-with-mcp-clients/)
- [AgentCore Gateway MCP support](https://aws.amazon.com/blogs/machine-learning/extending-mcp-support-for-amazon-bedrock-agentcore-gateway-2/)

## June 4 update: MCP descriptions need behavior consistency checks

The description-code inconsistency paper names a core MCP governance problem: the LLM selects tools from natural-language descriptions, but the server implementation may do something different. That turns documentation mismatch into a security issue. A tool description is not a contract unless the gateway has evidence that behavior matches it.

The practical gateway correction is to make server admission evidence-based. Tool descriptions, schemas, implementation source/version, side-effect class, data class, and dynamic probe results should be stored together. A gateway should deny or downgrade tools whose descriptions hide mutation, external observation, credential use, broad data access, or network effects.

Practical lesson:
- require MCP server manifests with owner, source, version, schemas, side effects, and data classes;
- run description-code consistency tests before production admission;
- compare natural-language descriptions against argument schemas, static behavior, dynamic canary probes, and observed effects;
- record description, implementation version, policy decision, arguments, observed effect, and trace ID for each tool call;
- quarantine third-party MCP servers until they pass consistency and provenance checks.

Source:
- [Description-Code Inconsistency in Real-world MCP Servers](https://arxiv.org/abs/2606.04769)

## June 5 update: WebMCP tool surfaces need origin-bound lifecycle controls

WebMCP Tool Surface Poisoning extends the gateway-governance problem from static tool descriptions to live web sessions. If websites can expose tools directly to agents, third-party scripts can potentially hijack the visible tool set or frame tool metadata while the session is active. The paper calls this Mid-Session Tool Injection and separates Tool Hijacking from Tool Framing.

The practical correction is to treat the tool surface as mutable runtime state. A gateway should not trust a tool because it appeared in the page. It should know where the tool came from, when it registered, whether metadata changed, whether the origin is allowed, and whether the current workflow may call it.

Practical lesson:
- bind tool identity to origin, version, and registration event;
- hash tool metadata fields such as name, description, readOnlyHint, and inputSchema;
- freeze or revalidate the visible tool set at policy checkpoints;
- separate first-party, third-party, read-only, and mutating tools in policy;
- log registration, mutation, selected call, arguments, observed effect, and policy decision.

Source:
- [WebMCP Tool Surface Poisoning](https://arxiv.org/abs/2606.06387)

## June 6 update: recuse signals are policy evidence, not access control

Will the Agent Recuse Itself? proposes a useful cooperative-control primitive: a live service can emit an in-band deny signal over an existing protocol channel and ask automated agents to withdraw even when their credentials work. This belongs in gateway governance because it creates explicit evidence that the infrastructure told the agent the task was out of scope.

The important caveat is non-negotiable. A recuse signal is not a security boundary. It is compliance evidence and a measurement surface. Hard authorization still belongs in IAM, network policy, database grants, and gateway enforcement.

Practical lesson:
- test recuse banners, notices, headers, or MCP error details in non-production environments;
- log whether the agent saw the signal, stopped, asked, escalated, or proceeded;
- separate recuse, require-approval, deny, and hard-fail outcomes in gateway policy;
- use recuse canaries to evaluate agent compliance under different operator-authority framings;
- never rely on recuse as the only protection for sensitive systems.

Sources:
- [Will the Agent Recuse Itself?](https://arxiv.org/abs/2606.06460v1)
- [mthamil107/Recuse](https://github.com/mthamil107/Recuse)

## June 6 update: cloud coding agents need task-state governance

GitHub's Agent tasks REST API and Fix with Copilot for failing Actions move cloud coding agents from chat surfaces into programmable workflow resources. That is strategically important because API-addressable agents can be launched from queues, CI failures, or internal automations. The governance unit becomes the task, not the conversation.

A serious deployment should treat cloud-agent dispatch as a privileged transition. The local control plane should preserve repository, branch, issue, CI run, failure signal, requested scope, model/agent identity, output branch, diff, tests, status, and approval evidence before any merge.

Practical lesson:
- wrap cloud-agent task creation in an internal policy queue;
- attach repo, branch, issue, CI failure, budget, and requested authority to each task;
- require task status, trace, diff review, test output, and approval before merge;
- restrict which workflows can create external cloud-agent tasks;
- reconcile cloud-agent task IDs with local audit logs and PR history.

Sources:
- [Agent tasks REST API changelog](https://github.blog/changelog/2026-06-04-agent-tasks-rest-api-now-available-for-copilot-pro-pro-and-max/)
- [GitHub Agent tasks REST docs](https://docs.github.com/rest/agent-tasks/agent-tasks?apiVersion=2026-03-10#start-a-task)
- [Fix with Copilot for failing Actions](https://github.blog/changelog/2026-06-04-fix-with-copilot-for-failing-actions-now-in-pro-pro-and-max/)

## June 7 update: tool governance now starts in managed clients and CI

GitHub's enterprise-managed plugins preview for VS Code and Copilot CLI turns agent-tool governance into client policy. Administrators can define plugin marketplaces in `.github-private/.github/copilot/settings.json`, auto-install plugins for licensed users, and keep hooks and MCP configurations always enabled across the enterprise. That means the tool surface can be governed before the agent reaches the runtime gateway.

FastMCP and mcp-guard show the infrastructure and CI versions of the same pattern. FastMCP v3.4.1 floors Starlette to avoid CVE-affected dependency resolution and makes OAuthProxy refresh-token cache misses visible. v3.4.2 restores JWT compatibility for providers with private non-critical JWS headers while preserving critical-header rejection. mcp-guard moves prompt-injection and tool-poisoning checks over C# MCP tool descriptions into Roslyn diagnostics and CI gates.

Practical lesson:
- manage approved plugins, hooks, MCP configs, and marketplaces through enterprise client settings;
- version client policy and log which policy was active during an agent run;
- pin MCP server dependencies and treat auth-library releases as security-relevant;
- regression-test OAuth/JWT behavior against the identity providers actually used;
- statically scan tool descriptions, schemas, hidden Unicode, exfiltration phrasing, and description fingerprints before server release;
- connect client policy, server version, tool-description hash, and gateway execution trace.

Sources:
- [GitHub enterprise-managed plugins in VS Code](https://github.blog/changelog/2026-06-05-enterprise-managed-plugins-in-vs-code-in-public-preview/)
- [FastMCP v3.4.1](https://github.com/PrefectHQ/fastmcp/releases/tag/v3.4.1)
- [FastMCP v3.4.2](https://github.com/PrefectHQ/fastmcp/releases/tag/v3.4.2)
- [mcp-guard v1.0.0](https://github.com/diomonogatari/mcp-guard/releases/tag/v1.0.0)


## June 8 update: skills are gateway-admitted supply-chain artifacts

MalSkillBench turns skill governance into a gateway problem. A skill is not passive documentation. It can inject instructions, ship scripts, request tool permissions, influence memory writes, and steer future actions. The paper's benchmark is useful because it treats malicious skills as hybrid artifacts: code injection, prompt injection, and mixed instruction-code attacks.

The gateway implication is that skill admission should look like tool admission. Provenance, signatures, and static scans are useful, but production authority should require behavioral evidence and trace binding.

Practical lesson:
- maintain a production-admitted skill catalog separate from an installable skill catalog;
- require owner, source, version, body hash, script hash, declared scopes, and approval points;
- scan prose, scripts, metadata, and tool declarations jointly;
- sandbox-verify high-risk or community skills before they can influence privileged runs;
- log loaded skill hash, granted scope, selected tools, memory writes, file writes, external observations, and policy verdicts;
- quarantine skills whose runtime side effects exceed their manifests.

Sources:
- [MalSkillBench](https://arxiv.org/abs/2606.07131v1)
- [lxyeternal/MalSkillBench](https://github.com/lxyeternal/MalSkillBench)

## June 9 update: artifact provenance needs gateway lineage

Context-Fractured Decomposition Attacks names a gateway failure mode that current tool policies often miss: artifact provenance gaps. A tool-using agent can write files, logs, scratchpads, plans, summaries, memories, or generated configs that later become context for a different module. If the gateway only sees the later artifact and not its origin, adversarial fragments can be recomposed across contexts.

The gateway implication is that artifact lineage is part of authorization. A durable artifact should carry origin, author, tool, session, task, trust level, and transformation history. When the agent later reads that artifact, summarizes it, turns it into code, or passes it as a privileged tool argument, policy should evaluate the lineage, not just the current text.

Practical lesson:
- track artifact reads and writes as gateway events, not only filesystem events;
- label user input, tool output, model-generated plans, logs, memories, scripts, and summaries as separate trust classes;
- propagate taint through summarization, rewriting, format conversion, and code/config generation;
- gate artifact-to-instruction and artifact-to-execution promotion;
- test cross-context attacks where each fragment is benign until later recomposition.

Source:
- [Context-Fractured Decomposition Attacks](https://arxiv.org/abs/2606.09084v1)

## June 10 update: third-party coding agents need platform-side validation

GitHub's third-party coding-agent validation is a gateway-governance signal. Once external coding agents can work directly in repositories, security validation cannot depend only on the agent's own prompt or vendor claims. The platform that receives the pull request should run the same validation regardless of which agent wrote the code.

GitHub says third-party coding-agent output now receives CodeQL analysis, dependency checks against the GitHub Advisory Database, and secret scanning for sensitive information such as API keys and tokens. If issues are found, the agent attempts to resolve them before finalizing the pull request. That is the right shape: agent-generated code is not done until the host platform has produced independent security evidence.

Practical lesson:
- require host-side security validation for every coding-agent PR, regardless of agent vendor;
- record agent identity, repository, branch, validation tools, alert IDs, remediation attempts, and final reviewer decision;
- keep security validation on by default and tied to repository policy, not optional agent behavior;
- merge only after CodeQL, dependency advisory, secret scanning, tests, and human review pass for the relevant risk tier;
- reconcile external-agent task IDs with local audit logs and PR metadata.

Source:
- [Security validation for third-party coding agents](https://github.blog/changelog/2026-06-09-security-validation-for-third-party-coding-agents)

## June 13 update: gateway tests need stakeholder harm and workflow-source evidence

Who Pays the Price? and PI-Hunter sharpen gateway governance at the web-agent boundary. Prompt injection is not only a malicious string that the model obeys. It is a source-localized contamination event that can create asymmetric harms for users, sellers, platforms, and third parties while the delegated task may still appear to succeed.

The practical gateway correction is to enrich security traces. A prompt-injection test should record affected stakeholder, attack objective, source location, contaminated process step, final outcome, and whether user task integrity survived. PI-Hunter’s source-aware auditing frame adds the needed localization: identify the external source or artifact that carried the latent malicious instruction and preserve that in the trace.

GitHub Agentic Workflows adds the production version of the same gateway lesson. A natural-language workflow definition that compiles into Actions YAML is a deployable automation surface. It should carry owner, repository, runner group, policy constraints, sandbox/firewall state, safe-output result, threat-detection result, and final change lineage.

Practical lesson:
- label prompt-injection fixtures by harmed stakeholder and source locality;
- log URL, DOM node, artifact, memory, tool output, or retrieved chunk that carried untrusted instructions;
- score process contamination separately from final attack success;
- treat agent workflow definitions as gateway-admitted automation artifacts;
- preserve compiled workflow, runner policy, sandbox evidence, safe-output verdict, and threat-detection result before mutation.

Sources:
- [Who Pays the Price?](https://arxiv.org/abs/2606.13385v1)
- [StakeBench/SBC](https://github.com/StakeBench/SBC)
- [PI-Hunter](https://arxiv.org/abs/2606.12737v1)
- [GitHub Agentic Workflows public preview](https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview)

## June 17 update: MCP gateways need source-owned claim evidence

ProvenanceGuard makes a gateway requirement explicit: source attribution is not a formatting detail. MCP agents can pool evidence from search, APIs, databases, clinical records, documents, and internal tools. If the gateway cannot preserve which source produced which evidence, the answer layer can conflate sources while still sounding grounded.

The gateway correction is to make claim evidence an owned object. Tool outputs should carry stable tool IDs, source IDs, raw-output references, trust class, and data-class labels. Answer claims should point back to source-specific evidence, not only to a retrieved context blob. Policy should be able to block or downgrade an answer whose claim is supported somewhere but attributed to the wrong source.

Practical lesson:
- require MCP servers and wrappers to emit stable tool IDs, source IDs, and raw-output references;
- keep source identity through summarization, claim decomposition, answer repair, and citation rendering;
- score support and attribution separately;
- log claim ID, source ID, evidence span, support verdict, attribution verdict, repair action, and final answer ID;
- use vendor agent registries, AI brokers, and access graphs as design references, but keep the evidence schema portable across gateways.

Sources:
- [ProvenanceGuard](https://arxiv.org/abs/2606.18037v1)
- [Zscaler agentic AI security platform](https://www.zscaler.com/press/zscaler-unveils-new-product-innovations-secure-agentic-ai)
- [Salesforce Agentforce Multi-Agent Orchestration](https://www.salesforce.com/agentforce/multi-agent-orchestration/)

## June 18 update: tool contracts are gateway authority

ContractGuard makes the contract layer itself part of gateway governance. A gateway that hides dangerous tools still trusts declared preconditions, effects, risk, and authorization. If an attacker can forge effects in the registry, the dangerous tool can be routed onto the causal path before the admissibility gate ever checks risk.

WitnessAI's Agentic Control is the product-shaped version of the same idea: discover agents, MCP servers, tools, and downstream systems, then enforce allow and block policy at the moment an agent acts. C-Trace adds the compliance variant: formal policy predicates over trace events, with a runtime monitor that intercepts tool invocations and model outputs.

Practical lesson:
- treat MCP tool manifests, skill manifests, and workflow definitions as signed authority artifacts;
- log manifest hash, declared effects, policy scope, principal, purpose, and final effect in the gateway trace;
- fuzz effect forgery and authorization-field tampering, not only prompt injection;
- keep runtime effect verification separate from rollback: once an external action has happened, the gateway can prevent downstream state contamination but may not undo the real-world side effect;
- expose one policy surface for human users, IDE agents, chat agents, custom agents, tools, and MCP servers.

Sources:
- [ContractGuard](https://arxiv.org/abs/2606.18550v1)
- [Runtime Compliance Verification for AI Agents](https://arxiv.org/abs/2606.19242v1)
- [WitnessAI Agentic Control](https://witness.ai/blog/introducing-witnessai-agentic-control-one-control-plane-for-every-agent-tool-and-mcp-server/)


## June 19 update: discovery and execution are gateway authority surfaces

Agentic Resource Discovery, ToolPro, and Sovereign Execution Brokers make the gateway larger than a thin MCP proxy. The gateway should govern what capabilities the agent can find, what generated skill or MCP card it loads, what effect-typed program it submits, and what brokered authority is allowed to mutate production.

Practical lesson:
- make capability search permissioned by principal, tenant, workflow, data class, and risk tier;
- log registry query, selected capability, source URL, publisher identity, manifest hash, media type, and loaded artifact ID;
- require READ/WRITE effect typing before compiled tool programs run;
- route state-changing programs and infrastructure mutations through policy and broker checks;
- preserve discovery, compiled intent, certificate, scoped credential, and final effect in one trace.

Sources:
- [Agentic Resource Discovery](https://huggingface.co/blog/agentic-resource-discovery-launch)
- [huggingface/hf-discover](https://github.com/huggingface/hf-discover)
- [ToolPro](https://arxiv.org/abs/2606.19992v1)
- [Sovereign Execution Brokers](https://arxiv.org/abs/2606.20520v1)


## June 20 update: repo-native instructions and issue fields are gateway state

GitHub's June 18 changes make ordinary repository surfaces part of the agent gateway. Copilot code review now reads root `AGENTS.md`, and the official GitHub MCP server can read and write issue fields such as priority, area, dates, and custom metadata.

The gateway lesson is that repository instructions and ticket fields are not harmless text. They influence review behavior, work routing, prioritization, and downstream automation. If agents can read and mutate them through MCP, they need the same identity, scope, trace, and review discipline as other tool calls.

Practical lesson:
- treat `AGENTS.md` as a reviewed policy artifact, not a casual prompt note;
- scope GitHub MCP issue-field writes by principal, repository, workflow, and field class;
- log agent-originated changes to priority, area, due date, and status fields;
- keep project-field schemas stable enough that agents do not infer semantics from labels alone;
- pair agent writable issue metadata with host-side checks such as branch protection, CODEOWNERS, CodeQL, secret scanning, and audit logs.

Sources:
- [Copilot code review: AGENTS.md support and UI improvements](https://github.blog/changelog/2026-06-18-copilot-code-review-agents-md-support-and-ui-improvements)
- [Detecting Duplicate Issues and issue fields MCP support for GitHub Issues](https://github.blog/changelog/2026-06-18-duplicate-detection-and-issue-fields-mcp-support-for-github-issues)
- [github/github-mcp-server](https://github.com/github/github-mcp-server)

## June 21 update: discovery and privilege choice are gateway decisions

GitHub Agent Finder, ARD, and ToolPrivBench sharpen two gateway responsibilities that are easy to miss.

First, discovery is authority. If an agent can search an approved registry for tools, skills, MCP servers, and workflows, the gateway must scope what can appear in that result set. Relevance ranking cannot stand in for trust or authorization.

Second, least privilege is not guaranteed by a safety prompt. ToolPrivBench shows that agents frequently select or escalate to higher-privilege tools even when lower-privilege alternatives are sufficient, especially after transient failures.

Practical lesson:
- treat capability discovery as a policy-mediated gateway call;
- keep relevance scores separate from trust and authorization scores;
- add privilege tier, declared effects, owner, publisher, registry, and approved workflow to tool metadata;
- require escalation reasons when lower-privilege tools are available;
- log transient failures separately from true tool insufficiency;
- test paired lower/higher privilege alternatives before exposing broad-write or admin tools.

Sources:
- [GitHub Agent Finder](https://github.blog/changelog/2026-06-17-agent-finder-for-github-copilot-now-available/)
- [Agentic Resource Discovery specification](https://commandline.microsoft.com/agentic-resource-discovery-specification-ard/)
- [ToolPrivBench](https://arxiv.org/abs/2606.20023v1)
- [AISafetyHub/agent-tool-selection-bias](https://github.com/AISafetyHub/agent-tool-selection-bias)

## June 23 update: gateway policy needs authority manifests and revocation epochs

AgentRiskBOM and Lingering Authority extend gateway governance from tool admission to authority lifecycle management. The gateway should not only decide whether a tool is visible or callable. It should know which manifest authorized the capability, which task episode granted it, which closure predicate revoked it, and whether the current handle is stale.

Practical lesson:
- attach authority-manifest IDs to gateway sessions;
- scope discovery and execution by manifest, principal, workflow, data class, and task stage;
- issue opaque, epoch-bound handles for temporary grants;
- record grant, invoke, close, denial, and stale-replay events in gateway traces;
- diff authority manifests before changing a workflow's MCP servers, credentials, memory scope, or external effects.

Sources:
- [AgentRiskBOM](https://arxiv.org/abs/2606.21877v1)
- [Lingering Authority](https://arxiv.org/abs/2606.22504v1)

## June 26 update: MCP poisoning has to be analyzed across tool sets

ShareLock updates gateway governance from single-tool review to enabled-set analysis. The attack splits hidden malicious instructions across multiple benign-looking MCP tool descriptions and reconstructs intent only when enough tools are observed together. That means a gateway that reviews each description independently can admit a malicious catalog without ever seeing an obviously malicious tool.

Practical lesson:
- diff MCP tool descriptions on every server update
- inspect enabled-tool combinations, not only individual tools
- fuzz candidate tool subsets for reconstructed intent
- record catalog version, update epoch, enabled set, selected tools, and denied combinations in gateway traces
- require review for untrusted tool-description updates, especially from newly admitted MCP servers

Source:
- [ShareLock](https://arxiv.org/abs/2606.27027v1)

## June 27 update: catalog source control is part of gateway policy

GitHub's `strictKnownMarketplaces` support for Copilot CLI and VS Code reinforces the same gateway lesson as ShareLock: tool and plugin catalogs are pre-execution authority surfaces. Enterprises should control where plugins can come from before an agent or developer can install them, and gateways should treat MCP servers, skills, and plugins as catalog entries with source, publisher, update epoch, and enabled-set risk.

Practical lesson:
- maintain allowed-source lists for plugins, MCP servers, and skills;
- bind installed marketplace, publisher, catalog version, and enabled set into run traces;
- deny untrusted marketplace sources before plugin or tool descriptions enter agent context;
- pair source allowlists with set-level poisoning tests for tool combinations;
- separate relevance ranking from trust and authorization ranking during discovery.

Source:
- [GitHub strictKnownMarketplaces changelog](https://github.blog/changelog/2026-06-25-enterprise-managed-settings-now-support-strictknownmarketplaces-in-vs-code-and-the-cli)
