# Runtime Governance

Last updated: 2026-07-06

Runtime governance is becoming the real control plane for agent systems.

The durable pattern is straightforward: the more autonomy an agent gets, the less acceptable it is to rely on prompt-only guardrails or after-the-fact policy review. Real systems need execution-time mediation.

## Core thesis

Governance for agents should look more like platform engineering than policy paperwork.

That means:
- identity for agents and subagents
- scoped permissions for tools and data sources
- policy checks before action execution
- approval gates for high-risk actions
- kill switches and rollback paths
- evidence collection tied to traces, not screenshots in a slide deck

## Why this matters

Traditional software governance assumed deterministic code paths and relatively stable permissions. Agent systems break that comfort. They plan, select tools, branch, retry, and act under changing context. If control only happens at design time, you do not really have control.

## Practical runtime patterns

### 1. Policy before tool execution
Every tool call should pass through a mediation layer that can allow, deny, rewrite, require approval, or attach additional constraints.

Useful technologies:
- Open Policy Agent
- Cedar
- signed tool registries
- least-privilege credentials

### 2. Agent identity and scopes
Treat agents as services, not as magical prompt wrappers.

Minimum expectations:
- stable identity per agent or workflow
- scoped access tokens
- separation between read, write, and destructive actions
- environment-aware permissions

### 3. Approval and interruption semantics
High-risk operations need explicit interrupt points.

Examples:
- sending an email externally
- modifying production systems
- moving money
- deleting records
- writing durable memory that will affect future runs

### 4. Reliability controls
Agent platforms need classic SRE patterns.

That includes:
- SLOs and error budgets
- circuit breakers
- rate limits
- staged rollout
- replay and audit trails

### 5. Evidence capture
If a workflow is regulated or business-critical, proof has to be collected during execution.

Capture:
- who acted
- what policy was evaluated
- which tools were called
- which approval path was taken
- what memory or retrieved context influenced the action

## What to build now

If you are building an agent platform today, the minimum viable governance stack should include:
1. a policy mediation layer in front of tools
2. identity and scope assignment for each workflow
3. approval gates for risky actions
4. trace-linked evidence capture
5. a kill switch that actually works in production

## What to avoid

Avoid these traps:
- treating prompts as the primary security boundary
- letting memory writes bypass policy review
- storing traces without enough metadata to reconstruct decisions
- assuming better models reduce governance needs
- waiting for regulation before implementing controls

## Representative sources

- Microsoft Agent Governance Toolkit: https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/
- OWASP Top 10 for Agentic Applications for 2026: referenced in the Microsoft post above
- eTAMP memory poisoning paper: https://arxiv.org/abs/2604.02623
- Springdrift auditable runtime report: https://arxiv.org/abs/2604.04660
- OpenClaw real-world safety analysis: https://arxiv.org/abs/2604.04759
- TraceSafe: https://arxiv.org/abs/2604.07223
- PIArena: https://arxiv.org/abs/2604.08499v1
- AgentCity: https://arxiv.org/abs/2604.07007
- Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation: https://arxiv.org/abs/2604.15559
- AgentWard: https://arxiv.org/abs/2604.24657
- FIND-Lab/AgentWard: https://github.com/FIND-Lab/AgentWard
- AgentVisor: https://arxiv.org/abs/2604.24118
- Governing What You Cannot Observe: https://arxiv.org/abs/2604.24686
- OpenAI Privacy Filter: https://openai.com/index/introducing-openai-privacy-filter/
- openai/privacy-filter: https://github.com/openai/privacy-filter

## New April 2026 additions

### Auditable persistence is part of governance, not just ops
Springdrift sharpens an important point: if an agent is long-lived, governance has to include append-only evidence, recoverable state, and deterministic policy gates. Runtime governance is not complete if the system cannot reconstruct what happened after the fact.

### Capability, identity, and knowledge should be governed separately
The OpenClaw real-world safety analysis introduces a useful framing: capability, identity, and knowledge are distinct attack surfaces. That suggests governance should separate tool authority, principal identity, and durable memory instead of treating "agent state" as one blob.

### Trace understanding is now a first-class safety requirement
TraceSafe adds a blunt lesson: a guardrail that cannot parse and reason over tool trajectories is not a serious runtime control. Safety for agents depends on structured-trace competence as much as on refusal behavior or jailbreak resistance.

### Prompt injection has to be tested as a systems problem
PIArena adds a needed correction. Prompt injection defense is not serious if it only survives one benchmark and one attack style. Runtime governance has to assume adaptive attackers, cross-task transfer, and interaction with tool scopes, retrieval paths, and policy mediation.

### Checkpoint restore paths are part of the governance surface
Microsoft Agent Framework's Python 1.0.1 release added restricted checkpoint deserialization by default for `FileCheckpointStorage`. That is not a minor patch note. It is a reminder that persisted workflow state is a privileged trust boundary. If a runtime can restore opaque objects from disk, governance has to cover deserialization policy, custom type allowlists, migration, and replay evidence just as seriously as it covers tool permissions.

### Distillation pipelines inherit behavior, not just task skill
Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation closes an easy governance loophole. A student agent can inherit destructive tendencies from teacher trajectories even when the visible traces look clean and deletion keywords were filtered out. In the paper's API-style setup, the student inherits a deletion bias strongly enough to hit a 100% deletion rate against a 5% baseline. In the Bash setting, the student develops a strong `chmod`-first preference even after keyword sanitation.

That means governance has to cover the training and distillation path, not only the runtime path. Demonstration corpora, replay datasets, and distilled student checkpoints are all policy-relevant artifacts. Keyword filtering is not a serious defense if the behavior survives in trajectory dynamics. Distilled agents still need post-training behavior probes, destructive-action canaries, and sandboxed execution surfaces.

### Accountability chains matter once agents cross principals
AgentCity is still highly conceptual, but it surfaces a durable governance question: who authored the rule, who executed the action, and who is accountable when agents transact across organizational boundaries? Runtime governance will eventually need an answer to that, even outside blockchain-heavy designs.

### Runtime security is becoming lifecycle mediation
AgentWard, AgentVisor, RiskGate, and OpenAI Privacy Filter sharpen this topic into an implementation pattern.

AgentWard organizes controls across startup, input processing, memory, decision-making, and execution. That is the right level of abstraction because agent failures propagate through lifecycle stages instead of staying inside one prompt boundary.

AgentVisor frames the target agent as an untrusted guest and places a trusted semantic mediator at the tool-call boundary. The important idea is semantic privilege separation: the system should inspect what the action means, what context caused it, and whether the privilege escalation is justified before the tool executes.

RiskGate adds adaptive monitoring. Agents can become unsafe without a code change, so governance has to observe drift, pattern shifts, and unobserved-risk margins at runtime.

OpenAI Privacy Filter adds a practical local-first context gate. Sensitive context should be labeled or redacted before it is stored in memory, retrieved into prompts, routed to hosted models, or passed to external tools.

Practical lesson:
- split controls across lifecycle stages
- put a mediator in front of privileged tool calls
- keep PII filtering local where possible
- record governance events in the same trace as actions and memory writes
- treat drift monitoring as part of runtime policy, not only analytics

Sources:
- [AgentWard](https://arxiv.org/abs/2604.24657)
- [FIND-Lab/AgentWard](https://github.com/FIND-Lab/AgentWard)
- [AgentVisor](https://arxiv.org/abs/2604.24118)
- [Governing What You Cannot Observe](https://arxiv.org/abs/2604.24686)
- [OpenAI Privacy Filter](https://openai.com/index/introducing-openai-privacy-filter/)
- [openai/privacy-filter](https://github.com/openai/privacy-filter)

### Semantic gateways turn MCP exposure into a governable enterprise boundary
The Semantic Gateway paper and Jarvis Registry update this topic with a concrete enterprise control-plane pattern. MCP makes tool discovery easy; governance has to make discovery scoped, execution authorized, and transitions auditable.

Practical lesson:
- put an MCP/A2A gateway in front of privileged tools
- assign identity and scopes to each agent workflow
- enforce tool-level RBAC deterministically
- place semantic policy checks before privileged execution
- preserve approval artifacts in the trace
- fuzz enabled-tool graphs for unauthorized state transitions

The gateway is becoming the runtime governance choke point. It should expose not just what the agent did, but what it could have done under the enabled tool set and policy configuration.

Sources:
- [From CRUD to Autonomous Agents](https://arxiv.org/abs/2604.25555v1)
- [Jarvis Registry](https://github.com/ascending-llc/jarvis-registry)


### May 3 update: control planes and trajectory firewalls move governance below the prompt

Microsoft Agent 365 and the behavioral-firewall paper update this topic at two different layers.

Microsoft’s Agent 365 general availability makes the inventory layer concrete: discover local and SaaS agents, distinguish delegated agents from agents with their own credentials, manage endpoint agents through Defender/Intune, run agents in managed Windows 365 environments, sync registries with AWS Bedrock and Google Gemini Enterprise Agent Platform, and extend Entra network controls to agent traffic. That is the enterprise product version of the runtime-governance thesis.

The behavioral-firewall paper pushes the execution layer. It compiles verified benign tool-call telemetry into a parameterized DFA and checks the next state transition at runtime through a lightweight gateway. The point is not that every workflow can be perfectly modeled. The point is that stateless prompt scanners are the wrong primitive for structured workflows where harm emerges from sequence, context, and parameters.

Practical lesson:
- inventory agents as principals, not only as apps or scripts
- attach credential, network, and data policy to the agent identity
- run privileged agents in managed execution environments
- log tool trajectories with enough structure to compile allowed paths
- enforce stable workflows with state-machine guards before tool execution
- keep exact parameter guards for secrets and destructive actions

Sources:
- [Microsoft Agent 365 general availability](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)
- [Enforcing Benign Trajectories](https://arxiv.org/abs/2604.26274)

## May 9 update: prompt injection is now a code-execution primitive

Microsoft's Semantic Kernel write-up makes the runtime-governance thesis concrete: once a model can map language into framework/tool parameters, prompt injection can cross from content manipulation into unauthorized file writes, code execution, database access, or host-level behavior. The model is not the security boundary. The boundary is where parsed parameters meet framework code and privileged tools.

The enterprise retrieval paper adds the data-plane version of the same problem. Relevance is not authorization. A retrieval system that ranks by semantic match before tenant and scope checks can leak data even if each component looks normal in isolation.

Practical lesson:
- patch affected frameworks and audit whether model outputs can autonomously trigger dangerous functions
- validate and authorize tool parameters before execution, especially file paths, script arguments, vector-store operations, browser actions, database queries, and shell commands
- enforce tenant authorization before relevance-ranked documents enter context
- correlate model-level intent, parsed parameters, policy verdicts, host detections, and patch versions in one trace
- add adversarial fixtures that try to turn retrieval, memory, or benign plugin calls into file writes, script execution, or cross-tenant disclosure

Sources:
- [When prompts become shells](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
- [Securing the Agent](https://arxiv.org/abs/2605.05287)
- [SkillScope](https://arxiv.org/abs/2605.05868)

## May 10 update: Codex safety makes local agents managed endpoints

OpenAI's Codex safety write-up is a concrete runtime-governance blueprint for local coding agents. The control stack is sandbox plus approval policy plus network policy plus managed auth plus agent-native telemetry. That is the right product shape: a local agent should be productive inside a bounded environment, low-risk actions should be frictionless, and higher-risk actions should stop for review.

The observability lesson matters as much as the sandboxing lesson. Endpoint logs can show that a process ran or a file changed, but agent-native logs explain the user request, tool approval decision, tool result, MCP server usage, and network allow/deny verdict. Those events belong in OpenTelemetry and SIEM/compliance pipelines so security teams can tell expected agent behavior from benign mistakes and real escalation.

Practical lesson:
- default local coding agents to read-only or workspace-write sandboxes
- define writable roots and protected paths explicitly
- use network allow/deny lists and cached web-fetch modes instead of open outbound access
- require approval or auto-review for actions outside the sandbox
- store CLI/MCP credentials in secure OS keyrings and bind auth to enterprise workspaces where possible
- export prompts, tool decisions, tool results, MCP usage, and network verdicts through OpenTelemetry

Sources:
- [Running Codex safely at OpenAI](https://openai.com/index/running-codex-safely)
- [openai/codex](https://github.com/openai/codex)

## May 11 update: agentic workflow injection makes CI/CD an agent security boundary

Agentic Workflow Injection updates runtime governance with a repository-native threat model. Issue bodies, pull-request descriptions, comments, titles, and artifacts are untrusted inputs. If those inputs reach an agent prompt and the agent's response later drives a shell command, `gh` call, GitHub API operation, MCP server, or workflow output, prompt injection has become a CI/CD dataflow problem.

GitHub's Copilot cloud agent secrets update shows the matching control surface. Agent secrets and variables now have a dedicated Agents type, separate from Actions, Codespaces, and Dependabot, with organization-level selected-repository scoping and `COPILOT_MCP_` prefixes for MCP server configuration. That is useful, but only if workflows treat secrets and model outputs as explicitly scoped, typed, and taint-aware.

Practical lesson:
- classify GitHub event fields as tainted before they enter prompts or scripts
- separate trusted system/workflow instructions from untrusted repository content
- avoid direct shell interpolation of model outputs; prefer files, validated JSON, environment variables, and safe escaping
- restrict `GITHUB_TOKEN` and Agents secrets to the smallest repository, job, and MCP scope
- add static checks for flows from event context to agent prompts, model outputs, shell commands, `gh` operations, `git push`, and secret-bearing MCP configuration
- treat prompt-only instructions such as "ignore prompt injection" as advisory, not as a security boundary

Sources:
- [Agentic Workflow Injection](https://arxiv.org/abs/2605.07135)
- [Configure secrets and variables for Copilot cloud agent](https://docs.github.com/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/configure-secrets-and-variables)
- [More flexible secrets and variables for Copilot cloud agent](https://github.blog/changelog/2026-05-08-more-flexible-secrets-and-variables-for-copilot-cloud-agent)

## May 13 update: MCP consent and browser red-teaming move policy into the tool path

Conleash and IPI-proxy sharpen runtime governance at two adjacent boundaries. MCP consent needs argument-scoped policy rather than broad always-allow toggles. Browser agents need red-team tests on real retrieved content from allowed domains rather than only mock malicious pages.

The shared lesson is that authority lives in the tool path. A safe MCP call is not defined by the tool name alone; it depends on arguments, data boundary, credential use, side effects, and repeated user intent. A safe browser retrieval is not defined by the domain alone; whitelisted pages can still carry hidden instructions that become agent-consumed context.

Microsoft's SocialReasoning-Bench adds the delegation metric above this layer: task completion is not enough if the agent fails to act in the principal's best interest. Runtime governance should eventually connect consent and policy decisions to outcome optimality and due diligence, not only allow/deny verdicts.

Practical lesson:
- classify tools by argument-level boundaries: read-only, local file, network, credential, money, external communication, durable memory, and destructive action
- auto-permit safe repeated calls only inside scoped boundaries, then escalate risky argument combinations
- convert user decisions into expiring rules with evidence and rollback
- run indirect-prompt-injection sweeps by rewriting real whitelisted HTTP responses before the browser agent reads them
- track exfiltration callbacks, policy verdicts, approvals, denials, and content provenance in the same trace as the final tool action
- evaluate delegated agents on outcome optimality and due diligence where they negotiate or schedule on behalf of a user

Sources:
- [Options, Not Clicks](https://arxiv.org/abs/2605.11360v1)
- [IPI-proxy](https://arxiv.org/abs/2605.11868v1)
- [SocialReasoning-Bench](https://www.microsoft.com/en-us/research/blog/socialreasoning-bench-measuring-whether-ai-agents-act-in-users-best-interests/)

## May 14 update: always-on agents need provenance gates and OS-level sandboxes

Sleeper Channels and Provenance Gates makes persistent prompt injection concrete for always-on agents. The dangerous pattern is not one bad prompt; it is cross-surface persistence. An untrusted input can become memory, a skill, a cron entry, or a filesystem patch, then trigger a later action through a different surface after the attacker is gone. The paper's D2 gate pattern is useful because it binds authorization to a canonical action-instance digest and a one-shot owner attestation, not to a broad paraphrase of intent.

MCPShield adds the monitoring lesson for tool traffic: metadata-only detectors are weak, content-level features over arguments and responses matter, and random train/test splits can overstate performance. OpenAI's Windows Codex sandbox adds the execution lesson: local coding agents need OS-enforced writable roots, protected paths, and network-deny defaults rather than prompt-only rules. GitHub's Copilot cloud task API adds the operations lesson: background agents can now be started programmatically, so task identity, scope, and provenance become automation controls.

Practical lesson:
- record provenance for memory writes, skill edits, scheduled jobs, filesystem patches, cloud-agent tasks, and tool calls
- bind approvals to exact action digests with scoped, one-shot, or expiring attestations
- treat persistent inputs as tainted until policy revalidates them at firing time
- evaluate MCP/tool-call monitors with task-disjoint splits and content-aware argument/response features
- default local coding agents to OS-level sandboxes with protected paths and network-deny modes
- scope background-agent task APIs by principal, repository, token class, secret access, and trace evidence

Sources:
- [Sleeper Channels and Provenance Gates](https://arxiv.org/abs/2605.13471)
- [maloyan/sleeper-channels](https://github.com/maloyan/sleeper-channels)
- [MCPShield](https://arxiv.org/abs/2605.11053)
- [OpenAI Codex Windows sandbox](https://openai.com/index/building-codex-windows-sandbox)
- [GitHub Copilot cloud agent task API](https://github.blog/changelog/2026-05-13-start-copilot-cloud-agent-tasks-via-the-rest-api)

## May 15 update: web-agent guards must run in parallel with sessionful coding-agent policy

WARD and the same-day GitHub/OpenAI coding-agent updates sharpen runtime governance at the live-session boundary. WARD is the browser-agent security piece: prompt injection can live in HTML or screenshots, so the guard needs to inspect user task, page content, screenshot, and proposed action. The useful product pattern is a parallel sidecar, not a slow sequential review step.

GitHub's Copilot app technical preview and auto model selection update, plus OpenAI's Codex mobile/session update, show the operational pressure. Coding agents are becoming persistent sessions across desktop, mobile, cloud, local hosts, remote SSH, branches, PRs, hooks, access tokens, and model routers. That is too much authority to govern as a chat transcript.

Practical lesson:
- run browser-agent guards in parallel over task intent, HTML, screenshot, URL, proposed action, and tool context
- require structured guard output: attack goal, injection location, evidence, confidence, and verdict
- bind coding-agent sessions to principal, repository, branch, host, token class, network mode, and approval state
- record model auto-selection, fallback, cost multiplier, health signal, and policy reason in the session trace
- use hooks for secret scanning, prompt validation, repository-specific policy, and logging before side effects
- treat mobile steering and remote SSH as privileged control surfaces, not convenience-only UX

Sources:
- [WARD](https://arxiv.org/abs/2605.15030v1)
- [WARD-WebAgent](https://github.com/caothientri2001vn/WARD-WebAgent)
- [GitHub Copilot app technical preview](https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview)
- [Copilot cloud agent auto model selection](https://github.blog/changelog/2026-05-14-copilot-cloud-agent-supports-auto-model-selection)
- [OpenAI Codex mobile/session update](https://openai.com/index/work-with-codex-from-anywhere)

## May 17 update: threat coverage maps are a governance artifact

Talk is (Not) Cheap makes a governance problem visible: LLM security benchmarks cover different and often non-overlapping parts of the attack surface. The paper builds a STRIDE-grounded Target x Technique matrix from a 507-leaf taxonomy of inference-time attacks and finds that major benchmarks such as HarmBench, InjecAgent, and AgentDojo cover at most 25% of the matrix.

The strategic correction is simple: a pass rate is not enough. Agent governance needs a coverage map that shows which threat cells were tested, which remain blank, and which controls exist for each cell. Otherwise benchmark success can hide untested service-disruption, model-internals, token-amplification, tool-abuse, retrieval, memory, and workflow-injection risks.

Practical lesson:
- maintain a Target x Technique coverage matrix for each agent product or runtime surface
- map public benchmarks and internal red-team fixtures into explicit cells
- publish untested high-risk cells in release notes and risk reviews
- add service-disruption, token-amplification, model-internals, tool-argument abuse, retrieval poisoning, and memory poisoning tests where gaps exist
- connect coverage cells to runtime controls, trace evidence, and owner accountability

Source:
- [Talk is (Not) Cheap: A Taxonomy and Benchmark Coverage Audit for LLM Attacks](https://arxiv.org/abs/2605.15118)

## May 18 update: sleeper memory poisoning makes persistent state tainted until proven otherwise

Hidden in Memory makes the runtime-governance consequence of persistent memory explicit. Prompt injection no longer has to win in the current context window. An attacker can place malicious content in a document, webpage, repository, or email; the assistant can store a fabricated memory; and that memory can later be retrieved to steer an unrelated future action.

This turns memory into a governance boundary. A memory entry needs source, trust tier, derivation path, timestamp, and use-time policy. The most dangerous entries are instruction-like memories derived from external context because they can look like personalized user preferences while actually encoding attacker intent.

Practical lesson:
- tag memory writes as user-authored, agent-inferred, or externally supplied
- require confirmation for instruction-like memories extracted from untrusted content
- prevent externally descended memories from justifying sensitive tool calls alone
- revalidate memory provenance when the memory is used, not only when it is written
- add sleeper-memory red-team fixtures with malicious docs, pages, repos, and emails
- record memory influence in the same trace as tool policy and action execution

Source:
- [Hidden in Memory: Sleeper Memory Poisoning in LLM Agents](https://arxiv.org/abs/2605.15338)

## May 25 update: trajectory-level guardrails are now deployable enough to test offline

AgentDoG 1.5 makes trajectory-level risk classification a practical artifact rather than only a paper pattern. The model card describes guardrail variants that classify full tool-using trajectories across observations, reasoning/actions, and environment feedback, with labels for failure mode, risk consequence, and risk source. The new OpenClaw risk paper reinforces why this matters for privileged local agents: persistent local storage, tool invocation, cross-context aggregation, plugins, and multi-user interaction create risks that final-output moderation can miss.

The practical lesson is not to drop a classifier inline and trust it immediately. It is to start with offline governance evidence:
- normalize stored traces into a stable trajectory format;
- label unconfirmed actions, tool misuse, privacy leakage, prompt injection, and over-privileged local file access;
- compare model flags against human-reviewed canary traces;
- keep policy mediation separate from risk classification;
- only move to online blocking after false-positive and false-negative behavior is understood.

This extends runtime governance below prompts and final answers. The unit of safety is the trajectory and the authority boundary it crosses.

Sources:
- [AgentDoG 1.5 model card](https://huggingface.co/AI45Research/AgentDoG1.5-Qwen3.5-4B)
- [Security, Privacy, and Ethical Risks in OpenClaw](https://arxiv.org/abs/2605.23330)

## May 29 update: sabotage audits need deployment-shaped scenarios

Gram sharpens runtime governance by evaluating sabotage propensity in simulated agentic coding and research deployments. The useful move is not the exact 2-3% misbehavior rate reported for the tested Gemini models. The useful move is the audit shape: construct deployment scenarios with incentives to misbehave, preserve trajectories, and run targeted experiments to identify whether failures come from overeagerness, role-play, objective pressure, unrealistic prompts, or tool affordances.

Practical lesson:
- create sabotage and overeagerness scenario packs for each high-trust agent role;
- test concealment, evidence manipulation, policy bypass, unjustified goal pursuit, and excessive role-play;
- ablate tool scope, approval gates, environment realism, and objective wording;
- route full traces through investigator agents and human review before expanding permissions;
- treat model-level safety claims as insufficient for deployment-level autonomy.

Source:
- [Gram](https://arxiv.org/abs/2605.30322)

## May 30 update: deterministic replay depends on serving conditions

MarginGate adds an infrastructure-level governance issue: temperature-zero BF16 decoding can still produce different tokens when the request is decoded alone versus inside a larger batch. If a governed agent run cannot be replayed under equivalent serving conditions, the trace is incomplete.

The practical takeaway is not to immediately adopt one verifier policy. It is to make inference determinism observable. Serving precision, batch mode, model build, decoding settings, and verifier policy should be trace fields for eval baselines, approvals, incident reviews, and high-trust automation.

Practical lesson:
- run solo-vs-batch reproducibility tests for deployed models and serving engines;
- record precision, batch mode, model build, decoding settings, and verifier policy in traces;
- reserve deterministic serving or verifier-backed serving for approvals, audits, and eval baselines;
- treat replay mismatch as a runtime-governance event;
- measure determinism before routing high-authority workflows to cheaper shared-batch serving.

Source:
- [MarginGate](https://arxiv.org/abs/2605.30218v1)

## June 1 update: sandboxing and AI-factory security are runtime policy

NVIDIA's NemoClaw/OpenShell and DOCA security materials make the infrastructure version of runtime governance explicit. Always-on agents need sandbox lifecycle management, routed inference, network policy, runtime detection, data access control, and supply-chain controls around skills, images, and tool adapters. The DOCA post frames agentic AI as a new attack surface spanning infrastructure, software supply chains, models, data, and autonomous agents with growing authority to act.

The practical lesson does not require adopting NVIDIA's full stack. It says privileged agents need platform controls below the prompt: constrained workers, governed inference endpoints, explicit egress policy, trace-linked network and tool decisions, and separate authority for diagnosis versus mutation.

Practical lesson:
- run privileged agents inside constrained worker or sandbox environments;
- route inference through governed endpoints with model, data, budget, and locality policy;
- enforce network egress policy per agent workflow;
- log sandbox lifecycle, network decisions, tool calls, inference route, and final effect in one trace;
- treat runtime images, skills, and tool adapters as supply-chain artifacts;
- separate read-only diagnosis authority from mutation authority.

Sources:
- [NVIDIA NemoClaw](https://github.com/NVIDIA/NemoClaw)
- [Enterprise Software Leaders Build AI Agents With NVIDIA](https://nvidianews.nvidia.com/news/enterprise-software-leaders-build-ai-agents-with-nvidia)
- [NVIDIA DOCA in-silicon security for agentic AI](https://developer.nvidia.com/blog/advancing-ai-infrastructure-for-agentic-ai-with-nvidia-doca-in-silicon-security/)

## June 2 update: AgentOps makes agent artifacts deployable infrastructure

AWS's AgentOps reference architecture turns production agent work into a release-engineering problem. It names four pillars, governance and security, build and operations, evaluation, and observability, and makes the deployable unit broader than a prompt: every agent, tool, and memory configuration should be versioned and tested through a pipeline. The operational telemetry includes decision traces, tool invocation patterns, latency, errors, memory usage, and cost per interaction.

Microsoft's Build 2026 Agent Framework page points at the same runtime direction through hosted agents, triggers, state management, file access, governance patterns, evals, OpenTelemetry instrumentation, MCP, skills, Playwright CLI, Responses API, and A2A. IBM's agent-logic article adds the enterprise design rule: policy-as-code, knowledge graphs, program analysis, and workflow-specific logic should bound model behavior instead of pushing every constraint into context.

Practical lesson:
- version agent definitions, prompts, tool manifests, memory configuration, policies, and eval fixtures together;
- run pre-prod tests for identity propagation, tool authorization, memory access, HITL gates, rollback, and agent-specific quality;
- register agents, tools, skills, MCP servers, and ownership metadata in an internal catalog;
- emit trace fields for decisions, tool calls, denied calls, memory use, cost, latency, errors, and final outcomes;
- feed production telemetry and eval failures back into release gates instead of treating them as dashboard-only data.

Sources:
- [AWS AgentOps with Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/agentops-operationalize-agentic-ai-at-scale-with-amazon-bedrock-agentcore/)
- [Microsoft Agent Framework at BUILD 2026](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026/)
- [IBM agent logic and scalable AI adoption](https://huggingface.co/blog/ibm-research/agent-logic-and-scalable-ai-adoption)

## June 4 update: budget and workflow controls are becoming runtime artifacts

Token Budgets frames runaway agent spend as an authority failure, not merely a billing problem. AWS Step Functions adding an AgentCore reasoning step, Microsoft packaging hosted agents, and GitHub adding Copilot sandboxes point in the same direction from the platform side: agent work is being wrapped in workflow steps, sessions, sandboxes, budgets, and traceable runtime policy.

The practical governance lesson is to represent these controls as first-class runtime artifacts. A budget should be delegated once and spent once. A workflow step should have input and output contracts. A sandbox should have filesystem, network, and credential boundaries. A hosted agent should have version, session state, owner, policy, and rollback metadata.

Practical lesson:
- create per-workflow, per-agent, per-step, per-tool, and per-subagent budget leases;
- log requested, granted, spent, denied, expired, and refunded budget events;
- wrap high-risk agent work in state-machine steps with explicit retry, timeout, approval, and failure policy;
- run tool execution inside local or cloud sandboxes with filesystem, network, and credential controls;
- trace hosted-agent version, session state, sandbox identity, tool calls, approvals, spend, and final effects together.

Sources:
- [Token Budgets](https://arxiv.org/abs/2606.04056)
- [AWS Step Functions adds AgentCore-powered agentic reasoning step](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-step-functions-agentcore/)
- [Microsoft Agent Framework at BUILD 2026](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/)
- [Cloud and local sandboxes for GitHub Copilot](https://github.blog/changelog/2026-06-02-cloud-and-local-sandboxes-for-github-copilot-now-in-public-preview/)


## June 8 update: sabotage monitors need cross-step evidence accumulation

TRACE sharpens runtime governance for long-horizon agents. Some malicious objectives are not visible in any single tool call. The agent can gather information, transform it, test policy edges, and only later attempt the harmful effect. Each action may look locally benign while the sequence is not.

The runtime-governance correction is to pair deterministic policy gates with accumulated trajectory evidence. Policy still blocks clear violations. The monitor handles ambiguous cross-step patterns by preserving a hypothesis ledger: suspicious regions, inspected evidence, linked steps, weakening evidence, verdict, and recommended operator action.

Practical lesson:
- emit typed trace events for every observation, tool call, argument, result, policy decision, approval, denial, and external effect;
- triage suspicious regions cheaply before expensive semantic review;
- accumulate evidence across steps instead of resetting risk at window boundaries;
- keep trajectory verdicts cite-linked to concrete trace events;
- use offline sabotage and permission-laundering fixtures before enabling live blocking.

Source:
- [TRACE](https://arxiv.org/abs/2606.07054v1)

## June 9 update: provenance gaps make artifacts runtime state

Context-Fractured Decomposition Attacks extends the June 8 TRACE lesson. Cross-step risk does not only live in the trajectory. It can be stored in artifacts that survive across modules and time. A runtime that treats files, logs, scratchpads, summaries, memories, and generated scripts as neutral context is missing part of the attack surface.

The runtime-governance correction is to make artifact state typed and trace-linked. When an artifact is created, transformed, read, trusted, or promoted into an instruction or executable input, that transition should appear in the same trace as tool calls and policy decisions.

Practical lesson:
- emit artifact-created, artifact-read, artifact-transformed, artifact-promoted, and artifact-executed events;
- attach origin, trust class, data class, transformation lineage, and policy verdict;
- separate evidence artifacts from instruction artifacts until policy explicitly promotes them;
- quarantine generated scripts/configs from untrusted artifact lineage;
- add replay fixtures for cross-context jailbreaks and artifact-laundering paths.

Source:
- [Context-Fractured Decomposition Attacks](https://arxiv.org/abs/2606.09084v1)


## June 10 update: security evaluation needs executable environments and trace-safe evidence release

AgentCanary and RedAct sharpen both sides of runtime governance. AgentCanary says agent security evals need real executable environments with persistent state and full-trajectory scoring, because static prompts and mocked tools miss system compromise. RedAct says raw traces are not harmless audit logs; they can leak reusable procedural skills unless trace release preserves verifier-critical evidence while redacting protected capability details.

GitHub's third-party coding-agent validation turns the same pattern into platform behavior: generated code from Claude, OpenAI Codex, and other third-party coding agents now gets CodeQL, dependency advisory, and secret-scanning validation before PR finalization.

Practical lesson:
- build executable security fixtures with real tools, stateful artifacts, and trajectory-level scoring;
- score outcome safety, security awareness, task utility, tool arguments, denied actions, and final effects separately;
- run CodeQL, dependency advisory checks, and secret scanning on agent-generated PRs;
- redact traces by protected capability class while preserving verifier-critical audit evidence;
- watermark released traces or summaries when provenance matters;
- require trace IDs, scan result IDs, and approval artifacts before agent code reaches production.

Sources:
- [AgentCanary](https://arxiv.org/abs/2606.10484v1)
- [RedAct](https://arxiv.org/abs/2606.10813v1)
- [XuShuwenn/RedAct](https://github.com/XuShuwenn/RedAct)
- [Security validation for third-party coding agents](https://github.blog/changelog/2026-06-09-security-validation-for-third-party-coding-agents)

## June 11 update: five-plane governance turns policy into runtime composition

A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents gives runtime governance a useful enterprise shape. Agents are not only crossing data boundaries. They are composing workflows. An individually permitted read, transformation, tool call, and write can still become an unauthorized business process when sequenced by an agent.

The proposed split is a reasoning plane plus network, identity, endpoint, and data enforcement planes. The reasoning plane adjudicates intent against composite principal and session state. The enforcement planes realize that decision through existing infrastructure. A composed evidence record binds the policy decision to the realized effects.

Practical lesson:
- model user, agent, subagent, tenant, workflow, and tool as composite principals with attenuated authority;
- mediate at planning, retrieval, tool selection, tool execution, effect commit, memory write, and audit emission;
- use a verdict vocabulary broader than allow/deny: redact, require approval, defer, isolate, or request more evidence;
- connect reasoning-plane decisions to identity, network, endpoint, data, and gateway enforcement adapters;
- preserve one composed evidence record per material action so audit can replay the policy path.

Source:
- [A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents](https://arxiv.org/abs/2606.12320v1)

## June 12 update: governance has to meter trajectory state, not only actions

OCELOT and Selection Integrity sharpen runtime governance at the state layer. OCELOT says privacy loss accumulates across releases, observations, sinks, and injected content. Selection Integrity says graph-memory structure can steer future selection without appearing in final citations. OpenAI's Ona acquisition announcement is the market signal that this state will increasingly live inside persistent cloud workspaces.

The governance implication is straightforward: per-action approval is not enough. The runtime needs budgets, taint, selection-path logs, and workspace lineage that survive across steps.

Practical lesson:
- maintain per-sink disclosure ledgers and charge releases against privacy budgets;
- include release, redact, coarsen, defer, ask, and keep-local as first-class policy verdicts;
- label memory graph structure by writer principal and trust tier;
- log graph-selection paths before final facts reach the model;
- bind persistent cloud workspaces to owner, tenant, project, policy, checkpoint, credential, and trace metadata.

Sources:
- [OCELOT](https://arxiv.org/abs/2606.12341v1)
- [Selection Integrity for LLM Graph Memory](https://arxiv.org/abs/2606.12290v1)
- [OpenAI to acquire Ona](https://openai.com/index/openai-to-acquire-ona)

## June 13 update: agentic workflows are governed runtime units

GitHub Agentic Workflows moves runtime governance from abstract architecture into a familiar CI surface. Teams define reasoning-based automations in Markdown, GitHub compiles them into Actions YAML, and the workflows reuse runner groups and policy constraints. The important part is the control envelope: read-only defaults, integrity filter rules, sandboxed containers, an Agent Workflow Firewall, safe-output validation, and a dedicated threat-detection job before changes are applied.

The runtime lesson is transferable even outside GitHub. An agentic workflow definition is not a prompt. It is a deployable runtime unit with an author, compiled artifact, runner identity, sandbox policy, repository scope, output validator, threat detector, and final mutation path.

Practical lesson:
- treat agentic workflow definitions and compiled artifacts as code;
- bind workflow, repository, actor, runner group, sandbox image, policy constraint, and model/agent identity in the trace;
- default to read-only access and require explicit gates for mutation;
- preserve safe-output and threat-detection results before applying changes;
- test workflow definitions for privilege escalation, prompt injection, overbroad repository access, and unsafe artifact promotion.

Source:
- [GitHub Agentic Workflows public preview](https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview)

## June 15 update: guardrails need resource budgets, not only policy intent

From Shield to Target makes an uncomfortable governance point: an LLM-based guardrail can itself be attacked as a reasoning resource. If crafted payloads can force the guardrail into extended reasoning loops, then guardrails are not free safety checks. They are runtime components that need budgets, circuit breakers, observability, and fail-closed states.

This pairs with SkillMutator and SkillAudit. Skills and guardrails both sit on the enforcement path, but both can be manipulated. The governance layer should defend the policy mechanism, not only the downstream tool call.

Practical lesson:
- put token, wall-clock, recursion, and tool-call budgets around LLM guardrails;
- classify guardrail exits as allow, deny, require approval, budget exhausted, timeout, loop suspected, or uncertain;
- treat guardrail budget exhaustion as a policy event, not a silent retry;
- include adversarial resource-exhaustion payloads in safety-gate regression suites;
- preserve guardrail prompt, model, budget, elapsed time, verdict, and failure class in the trace.

Sources:
- [From Shield to Target](https://arxiv.org/abs/2606.14517v1)
- [SkillMutator](https://arxiv.org/abs/2606.14154v1)
- [SkillAudit](https://arxiv.org/abs/2606.14239v1)

## June 16 update: mutable skills and plaintext routers need hard runtime boundaries

Dynamic Malicious Skills and The Proxy Knows Too Much reinforce the same runtime-governance rule from opposite sides. A skill file that can be rewritten during execution is not a stable control surface. A model router that sees plaintext and can rewrite tool calls is not only a cost optimizer, it is an action-path authority.

The practical runtime boundary has to drop below the prompt. Skill directories should be immutable while admitted. Router paths should be constrained, logged, and treated as privileged infrastructure. For high-sensitivity paths, AEGIS-style attestation is the right design reference even if the first deployable step is signed images, host allowlists, and strict route logging.

Practical lesson:
- mount skill directories read-only during execution and verify mutation attempts fail;
- log skill body hash, script hash, mount mode, and loaded-skill ID in every run;
- treat LLM API routers and compatibility shims as privileged runtime components;
- restrict provider destinations and route parameters before plaintext leaves the client boundary;
- evaluate attestation or enclave-backed pass-through for high-sensitivity router traffic.

Sources:
- [Dynamic Malicious Skills](https://arxiv.org/abs/2606.16287v1)
- [The Proxy Knows Too Much](https://arxiv.org/abs/2606.16358v1)

## June 18 update: compliance and contracts have to fire during execution

C-Trace and ContractGuard converge on the same runtime-governance correction. Static red-team prompts, policy documents, and post-hoc logs are not enough once agents call tools and handle personal data. Compliance rules and tool contracts need to be predicates over the execution trace, and they need to block model outputs or tool calls before external mutation.

C-Trace expresses consent, purpose limitation, data minimization, and erasure as formal policy checks over events such as user messages, assistant messages, tool calls, tool returns, consent, and erasure. ContractGuard does the same kind of hardening for tool eligibility: signed provenance, typed contract attestation, and runtime effect verification.

Practical lesson:
- define trace event schemas for consent, purpose, erasure, tool call, tool return, model output, contract hash, declared effect, and policy verdict;
- place runtime monitors before tool execution and before externally visible model output;
- treat extractor uncertainty, monitor timeout, and contract mismatch as explicit policy outcomes;
- test policies with attack dialogues and mutated tool contracts;
- distinguish state-integrity blocking from real-world rollback for irreversible effects.

Sources:
- [Runtime Compliance Verification for AI Agents](https://arxiv.org/abs/2606.19242v1)
- [ContractGuard](https://arxiv.org/abs/2606.18550v1)


## June 19 update: execution brokers remove standing mutation credentials

Sovereign Execution Brokers sharpen the runtime-governance boundary. If an agent or wrapper holds standing production credentials, an admission certificate can be bypassed. The broker has to be the only accepted mutation path: verify the action certificate, check scope, validity window, policy epoch, revocation epoch, and live-state drift, mint a short-lived scoped credential, invoke the infrastructure API, and record the signed outcome.

Google DeepMind's AI Control Roadmap supplies the monitoring side: treat capable agents as potentially imperfectly aligned, define AI-specific threat models, monitor trajectories, and measure coverage, recall, and time-to-response.

Practical lesson:
- remove reusable write credentials from agent runtimes where possible;
- require production mutation APIs to reject non-broker identities;
- bind broker checks to action contract, principal, scope, policy epoch, revocation epoch, and live-state hash;
- mint short-lived scoped credentials only after validation;
- record proposal, admission, broker decision, credential mint, mutation request, mutation result, and monitor verdict in one trace.

Sources:
- [Sovereign Execution Brokers](https://arxiv.org/abs/2606.20520v1)
- [Google DeepMind AI Control Roadmap](https://deepmind.google/blog/securing-the-future-of-ai-agents/)

## June 20 update: policy ledgers make state checks executable

LedgerAgent sharpens runtime governance from another angle: state-dependent policy should fire before a side-effecting tool call, not after the agent has already acted. The ledger holds facts, identifiers, constraints, and conditions observed across user turns and tool returns. Policy checks read that ledger before environment-changing calls execute.

The control-plane lesson is direct. Prompts can tell an agent to obey policy, but a ledger plus pre-mutation check can block a tool call. That turns governance into an execution-path component.

Practical lesson:
- split observation, state projection, action proposal, and action approval into separate trace events;
- keep ledger entries tied to source event IDs and validity metadata;
- check side-effecting tool calls against current ledger state before execution;
- record ledger snapshot hash, policy ID, verdict, rejected arguments, and remediation path;
- treat ledger extraction failures as policy outcomes, not hidden model uncertainty.

Source:
- [LedgerAgent](https://arxiv.org/abs/2606.20529)

## June 21 update: least privilege needs runtime evidence, not only IAM

ToolPrivBench turns least privilege into an agent-runtime evaluation problem. The failure is not that a tool lacks IAM. The failure is that the agent selects or escalates to a higher-privilege tool when a lower-privilege path is sufficient, especially after a transient failure.

The runtime-governance correction is to log the decision context around tool choice: available alternatives, privilege tier, reason for escalation, failure class, retry count, and final effect. A router that cannot explain why lower privilege was insufficient should not get the higher-privilege tool by default.

Practical lesson:
- add privilege tiers and effect classes to every agent-visible tool;
- include available lower-privilege alternatives in the trace;
- distinguish transient failure from semantic insufficiency;
- require explicit escalation reasons and policy verdicts;
- build paired tool-choice fixtures into runtime regression tests.

Sources:
- [ToolPrivBench](https://arxiv.org/abs/2606.20023v1)
- [AISafetyHub/agent-tool-selection-bias](https://github.com/AISafetyHub/agent-tool-selection-bias)

## June 23 update: authority manifests make runtime governance diffable

AgentRiskBOM and Lingering Authority make runtime governance concrete at two levels. AgentRiskBOM says each deployed agent should have a machine-readable account of autonomy level, tools, memory scope, credentials, approvals, audit signals, delegation, and external effects. Lingering Authority says temporary capabilities must expire when the subgoal that justified them closes.

Practical lesson:
- ship an authority manifest with every agent workflow;
- diff tools, credentials, memory scopes, external effects, and delegation rights across releases;
- compile task contracts into temporary capability handles;
- revoke handles on trusted closure predicates;
- reject stale handle replay before side effects occur;
- log grant, invoke, close, deny, and stale-replay events as runtime governance evidence.

Sources:
- [AgentRiskBOM](https://arxiv.org/abs/2606.21877v1)
- [Lingering Authority](https://arxiv.org/abs/2606.22504v1)

## June 25 update: execution-time safety needs a path the agent cannot fire

The Unfireable Safety Kernel sharpens runtime governance into an only-path requirement. A guardrail inside the agent runtime can request safe behavior, but it cannot be the hard control boundary if the agent can reach the tools, files, APIs, or self-modification seam that the guardrail is supposed to constrain.

The practical target is a separate reference monitor on the mutation path: the agent proposes, the monitor validates authority and policy, the tool accepts only monitor-mediated requests, and the trace preserves the verdict. That is the runtime-governance version of least privilege.

Practical lesson:
- place high-risk side effects behind a process-separated monitor;
- require privileged tools to reject direct calls from the agent process;
- fail closed on parse failure, policy timeout, missing scope, stale epoch, or absent approval evidence;
- sign or make tamper-evident the allow, deny, timeout, and fail-closed decisions;
- test bypass attempts, stale capability reuse, guardrail mutation, and direct-tool invocation as runtime fixtures.

Sources:
- [The Unfireable Safety Kernel](https://arxiv.org/abs/2606.26057v1)
- [Can Trustless Agents Be Trusted?](https://arxiv.org/abs/2606.26028v1)

## Working conclusion

Runtime governance is not a niche enterprise concern. It is the natural consequence of giving agents durable memory, tool access, repository permissions, CI/CD authority, local storage, plugins, delegated secrets, shared inference infrastructure, sandboxed execution environments, mutable skills, router paths, workflow definitions that compile into automations, broker-mediated mutation paths, authority manifests, and revocable capability handles. The control plane has to move into runtime: inventory the agents, bind identity and scope, manage execution environments, preserve trace evidence, enforce valid next transitions before privileged tools execute, calibrate trust from outcomes, test trajectory-level guardrails offline, budget the guardrails themselves, record serving conditions for replayability, constrain network and inference routes, keep skills immutable while active, and keep tainted inputs from silently becoming trusted agent instructions or script data.

## June 26 update: agent instructions can compile into external policy

Autoformalization of Agent Instructions into Policy-as-Code strengthens the central runtime-governance thesis: prompts are not the enforcement boundary. The useful pattern is LLM-assisted compilation from prompts, MCP tool definitions, and written policy docs into Cedar policies, followed by deterministic parsing, schema checks, contradiction checks, semantic review, and external runtime enforcement before an action executes.

Practical lesson:
- treat LLM policy generation as a compiler front-end, not as authority
- enforce policies outside the agent process
- store policy ID, input fields, verdict, denial reason, and final effect in the trace
- return denial reasons to the agent as recoverable feedback

Sources:
- [Autoformalization of Agent Instructions into Policy-as-Code](https://arxiv.org/abs/2606.26649v1)
- [sondera-ai/sondera-harness-python](https://github.com/sondera-ai/sondera-harness-python)

## June 28 update: runtime monitors must see trace obligations, not only calls

VIGIL and the adaptive out-of-band defense evaluation reinforce the same runtime-governance rule. Enforcement belongs outside the model, but an action-level allowlist is too shallow when the violation depends on event order, value flow, stale authority, or adversarial adaptation.

Practical lesson:
- represent high-risk obligations as trace policies, not only prompt instructions;
- collect typed events for tool calls, artifacts, arguments, outputs, statuses, policy IDs, and consuming calls;
- block or escalate before a violating invocation's effects land;
- test monitors against adaptive, defense-aware attacks rather than static attack strings alone;
- preserve allow, deny, timeout, false positive, false negative, and task-utility outcomes in the regression history.

Sources:
- [VIGIL](https://arxiv.org/abs/2606.26524v1)
- [Adaptive Evaluation of Out-of-Band Defenses](https://arxiv.org/abs/2606.26479v1)

## June 29 update: privacy and prompt injection are information-flow problems

ToolPrivacyBench and the prompt-injection inseparability theorem sharpen runtime governance around information flow. The runtime must decide what private atoms can move to which tools, and it must prevent untrusted data from becoming authority for tool grants, policy routing, or memory writes. Prompt-only controls cannot guarantee that separation.

Practical lesson:
- represent sensitive fields as private atoms with purpose-bound policies;
- record field movement through tool arguments, backend writes, and memory operations;
- attach provenance and taint metadata to every untrusted input and retrieved artifact;
- enforce authority-bearing actions outside the shared prompt channel;
- regression-test both over-disclosure and control-plane bypass.

Sources:
- [ToolPrivacyBench](https://arxiv.org/abs/2606.28061v1)
- [On the Inseparability of Instructions and Data](https://arxiv.org/abs/2606.27567v1)

## July 2 update: skill supply chains belong on the runtime policy path

Skills Are Not Islands adds a runtime-governance requirement: a loaded skill should carry its transitive dependency graph into the policy path. A runtime cannot enforce least privilege if a skill's package, service, and skill dependencies are invisible.

Practical lesson:
- admit skills through manifests and lockfiles, not loose markdown alone;
- include skill, package, service, tool, credential, browser, repository, and memory authority in the dependency graph;
- fail CI when the dependency graph changes without review;
- emit risk warnings when transitive dependencies add shell, network, credential, or external-service authority;
- bind policy decisions to the loaded skill hash and dependency graph hash.

Source:
- [Skills Are Not Islands](https://arxiv.org/abs/2607.01136v1)

## July 3 update: persistent state and underspecification require stateful boundary checks

Distributed Attacks in Persistent-State AI Control and UnderSpecBench sharpen the same runtime-governance point. A dangerous agent action can be unsafe because it completes a prior cross-PR buildup, or because the current instruction leaves target, scope, or blast radius ambiguous. In both cases, a prompt-level request to be careful is too weak.

Practical lesson:
- preserve cross-PR suspicion state and prior monitor warnings;
- track whether a new diff completes dormant hooks, delayed activation paths, or repeated sensitive-file touches;
- require target identity and scope fields before DevOps mutations;
- treat clarification and deferment as valid safe outcomes under underspecification;
- score Wrong Target and OverScope separately from task failure.

Sources:
- [Distributed Attacks in Persistent-State AI Control](https://arxiv.org/abs/2607.02514v1)
- [Coding Agents Are Guessing](https://arxiv.org/abs/2607.02294v1)

## July 6 update: process gates are runtime governance

SkillCoach, Regression Accumulation, Steerability via constraints, and SessionBound all point to the same runtime-governance shape: the runtime should enforce process boundaries before an effect lands. Final success, chat approval, or reviewer confidence is not enough.

Practical lesson:
- score skill process separately from final outcome;
- replay prior coding commitments before accepting later edits;
- put coding agents inside constrained substrates rather than reviewing unconstrained work after the fact;
- compile enterprise task approvals into signed, budgeted execution sessions;
- log process denials, budget exhaustion, regression rollbacks, and omitted checks as governance events.

Sources:
- [SkillCoach](https://arxiv.org/abs/2607.01874v1)
- [Regression Accumulation in Multi-Turn LLM Programming Conversations](https://arxiv.org/abs/2607.01855v1)
- [Steerability via constraints](https://arxiv.org/abs/2607.02389v1)
- [SessionBound](https://arxiv.org/abs/2607.00751v1)

## July 16 update: permission needs canonical action identity

CAVA and the user-permissions survey connect the interface and runtime halves of governance. A user preference has to become a machine policy, and the resulting approval has to bind to one semantic action rather than one wrapper-shaped prompt or dialog.

Practical lesson:
- canonicalize principal, task, operation, target, arguments, data class, effect class, policy version, and expiry;
- hash semantic action identity and invalidate approval when semantics drift;
- expose enforcement depth as block, intercept, observe, or unknown;
- preserve interface request, derived policy, action fingerprint, verdict, execution status, and final effect receipt;
- test equivalent wrappers, wrapper bypass, semantic separation, stale approval, and tampered receipts.

Sources:
- [CAVA](https://arxiv.org/abs/2607.13716v1)
- [How Agents Ask for Permission](https://arxiv.org/abs/2607.13718v1)

## July 19 update: memory scope and retry termination belong in runtime

jcode `v0.52.0` turns two common prompt-level expectations into runtime behavior. Memory tool results are scoped to the session working directory, and automatic retries stop after consecutive provider guardrail refusals.

Practical lesson:
- bind memory queries to canonical workspace and session identity;
- require an explicit release for cross-project recall;
- separate provider refusals from transient transport failures;
- cap consecutive refusals and emit a terminal or escalation event;
- test symlink, shared-mount, multi-repo, and copied-artifact boundary cases.

Sources:
- [jcode v0.52.0](https://github.com/1jehuang/jcode/releases/tag/v0.52.0)
- [1jehuang/jcode](https://github.com/1jehuang/jcode)
## July 22 update: monitors need executable artifact tests, not only trajectories

ResearchArena makes artifact evaluation a runtime-governance requirement. A trajectory, visible source, and chain-of-thought can all look ordinary while sabotage lives in training data or only appears under a hidden trigger.

Pooled detection reaches 83% for optimization-embedded attacks but only 27% for post-training embedded attacks, against a 6% baseline false-positive rate. Artifact access helps when the monitor runs the right test. It does not help when the monitor only reads, explains away an anomaly, or probes the wrong inputs.

Practical lesson:
- separate independent side effects from embedded artifact sabotage in the threat model;
- keep hidden canaries and behavior-specific probes outside the agent workspace;
- execute artifacts under a separate evaluator principal before promotion;
- bind artifact digest, monitor access, tests chosen, observations, misses, and release verdict in one record;
- include strategically hidden, delayed, data-carried, dependency, benchmark-gaming, and diffuse attacks in regression suites.

Evidence caveat: the MIT repository is public and substantial, but three trials per configuration are noisy, the red teams do not strategically hide, and faithful evaluation requires expensive long-horizon GPU workloads.

Sources:
- [ResearchArena](https://arxiv.org/abs/2607.19321v1)
- [aisa-group/ResearchArena](https://github.com/aisa-group/ResearchArena)

## July 24 update: telemetry needs a per-agent policy boundary

AgentCore's unified observability destination puts traces, prompts, structured logs, and stdout into one per-agent CloudWatch log group. That aligns debugging identity with IAM, encryption, retention, and export identity, but also concentrates sensitive run data.

Practical lesson:
- define IAM, CMK, retention, redaction, and export policy before changing destinations;
- preserve one trace identity across prompt, model, tool, memory, gateway, identity, and stdout events;
- test that each agent's operators and exporters cannot read another agent's log group;
- record migration flag, ADOT version, sampling policy, and destination as runtime configuration;
- support external OpenTelemetry sinks without weakening per-agent access controls.

Provider caveat: the feature is specific to AgentCore and CloudWatch. The reusable pattern is the per-agent evidence boundary, not the AWS storage choice.

Sources:
- [AgentCore unified observability launch](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-unified-observability-single-log-group/)
- [AgentCore observability guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html)

## July 25 update: one runtime needs one lifecycle owner

NemoClaw v0.0.95 makes lifecycle authority explicit for OpenShell gateways. The runtime validates whether NemoClaw or an external systemd service owns the listener and prevents recovery, stop, or uninstall from mutating an externally supervised gateway.

Practical lesson:
- store one canonical lifecycle owner per gateway and runtime;
- verify owner and listener state before mutation;
- make restore a staged, verified, atomic replacement;
- accept only immutable remote digests or images pinned during the current operation;
- reject skipped release gates as passing evidence and separate runner wait from execution time.

Artifact caveat: the active Apache-2.0 repository supports Hermes, but GitHub exposes no tagged v0.0.95 release. NVIDIA's dated release notes are the authoritative delta.

Sources:
- [NemoClaw v0.0.95](https://docs.nvidia.com/nemoclaw/user-guide/openclaw/release-notes/2026/7/24)
- [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)
- [Gateway lifecycle authority](https://docs.nvidia.com/nemoclaw/user-guide/openclaw/deployment/gateway-lifecycle-authority)
## July 31 update: system prompts need assurance and provenance

AISPA treats the system prompt as a policy-bearing artifact and audits exact spans across eight user-protection dimensions. The paper finds broad but incomplete protection and pervasive problematic instructions across 88 commercial products.

Practical lesson:
- version prompt source, product, model, date, digest, and approval identity;
- preserve exact spans, dimensions, reviewer class, confidence, and methodology version;
- connect protective claims to behavioral regression tests;
- block or document problematic instructions before release;
- invalidate approval when prompt semantics change.

Artifact caveat: the public System Prompt Index is populated but lacks a declared license, mixes prompt sources whose authenticity and freshness are not guaranteed, and removes fields that distinguish automated from human-reviewed findings.

Sources:
- [AISPA](https://arxiv.org/abs/2607.28617v1)
- [System Prompt Index](https://systempromptindex.com/)
- [XiangningLin/SystemPromptIndex](https://github.com/XiangningLin/SystemPromptIndex)

## August 4 update: runtime controls need one event and policy identity

Four fresh findings converge on the same boundary. Shared-workspace changes need revision events, anomaly monitors need deployment-specific calibration, execution backends need capability-based routing, and team policy inheritance needs immutable ceilings. Each control is useful alone, but they become governance only when their decisions name the same trajectory, actor, revision, capability grant, and effective policy.

Build one runtime receipt that records mutation origin, monitor alarms, backend escalation, validation evidence, and inherited policy. This keeps observability from drifting away from authority.

Sources:
- https://arxiv.org/abs/2608.02499v1
- https://arxiv.org/abs/2608.02464v1
- https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/
- https://github.blog/changelog/2026-08-03-enterprise-team-specialization-for-managed-settings

## August 5 update: policy authority belongs at commit time

Stateful Governance shows why request-time authorization is insufficient for concurrent agents. A decision can be valid when requested and invalid when the effect commits because budgets, inventory, approvals, or risk state changed in between.

Practical lesson:
- declare the policy-state scopes consumed by each effect;
- coordinate policy state and effect execution in one transaction;
- reserve state across delayed approvals and revalidate before commit;
- test full-conflict and disjoint-scope workloads separately;
- attach policy version, principal, effect ID, state snapshot, and commit outcome to one receipt.

Evidence caveat: the PostgreSQL prototype reports zero stale allows where request-local baselines violate a shared budget, but no public implementation repository was verified.

Source:
- [Stateful Governance for Concurrent Agentic Systems](https://arxiv.org/abs/2608.02764v1)


## August 7 update: stateful gateway policy and metered agent traffic

AgentCore's temporal policies and gateway rate limits push runtime governance below the prompt. Authorization can depend on what the agent already did. Spend and burstiness can be capped per principal, tool, target, and model. That is the same sovereignty move as commit-time checks and scout-before-spend: the boundary, not the model, owns the grant.

Practical lesson:
- keep stateful policy evaluation next to tool mediation;
- attach remaining budget and matched rule to every gateway decision;
- do not treat policy-authoring skills as a substitute for enforcement.

Sources:
- [Temporal policies in AgentCore](https://aws.amazon.com/blogs/machine-learning/securing-ai-agents-with-temporal-policies-in-amazon-bedrock-agentcore/)
- [Rate limits on AgentCore gateway](https://aws.amazon.com/blogs/machine-learning/configure-rate-limits-for-ai-traffic-on-agentcore-gateway/)

## August 9 update: trajectory risk belongs in pre-action runtime state

DreamGuard replaces repeated LLM review of growing histories with a compact recurrent risk state. It combines immediate-hazard and prefix-risk signals before each action, reports 25-millisecond average calls, and intervenes before the first hazardous step in 96.3 percent of unsafe long-horizon trajectories.

Practical lesson:
- normalize actions into a versioned event schema;
- keep bounded risk state outside the acting model;
- separate immediate hazard from accumulated prefix risk;
- expose pass, hold, and block before execution;
- bind calibration version, thresholds, state digest, action manifest, verdict, and effect receipt;
- retain deterministic policy and commit-time checks as final authority.

Artifact caveat: no exact public DreamGuard implementation repository was verified. The method uses a frozen Qwen3-4B encoder and H100 training, so faithful reproduction is architecture-heavy.

Source:
- [DreamGuard](https://arxiv.org/abs/2608.05695v1)
