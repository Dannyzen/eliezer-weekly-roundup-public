# Enterprise MCP Orchestration

Last updated: 2026-07-14

Core sources:
- Queen-Bee Agents: A BeeSpec-Centered Architecture for Governed Enterprise MCP Orchestration: https://arxiv.org/abs/2606.06545v1
- SecureClaw: Clawing Back Control of LLM Agents: https://arxiv.org/abs/2606.09549v1
- Less Context, Better Agents: https://arxiv.org/abs/2606.10209v1
- Extending MCP support for Amazon Bedrock AgentCore Gateway: https://aws.amazon.com/blogs/machine-learning/extending-mcp-support-for-amazon-bedrock-agentcore-gateway-2/
- From Failed Trajectories to Reliable LLM Agents: https://arxiv.org/abs/2606.06324v1

## Overview

The strongest finding from the 2026-06-04 to 2026-06-10 window is Queen-Bee Agents. The paper's naming is cute, but the architectural move is serious: compile a user request into a scoped execution contract before any specialized agent touches tools.

Queen-Bee separates the agent system into a Queen control plane, a BeeSpec intermediate representation, specialized Bee execution units, and tenant-scoped MCP connectors. The Queen retrieves capabilities, chooses skills and tools, sets tenant and memory scope, attaches policy, and emits BeeSpecs. Bees then execute only within that compiled boundary.

This won the week over the other good findings because it connects the layers the repo has been tracking separately: skills-as-control, MCP gateway governance, multi-agent orchestration, context economy, and executable evaluation. The durable insight is not "use a queen agent." It is this:

> Enterprise agents need a compiled work order between planning and side effects.

Without that layer, teams keep rediscovering the same failure: a capable model receives too many tools, too much context, too little tenant scope, and no traceable reason why a particular subagent had authority to act.

## Core innovation

The core innovation is BeeSpec as an execution-boundary object.

The paper's BeeSpec schema includes:

- `bee_id`: unique execution-unit identifier for audit and trace linking;
- `role`: the assigned natural-language role;
- `domain`: operational domain such as HR, IT, finance-sensitive, or chemistry;
- `tenant_scope`: tenant boundary for MCP calls;
- `memory_scope`: accessible memory namespace;
- `attached_skills`: retrieved skills used by the Bee;
- `allowed_tools`: MCP-backed tools authorized for the Bee;
- `policy_profile`: guardrail profile checked before tool invocation;
- `approval_gate`: optional human approval before downstream execution.

That turns orchestration into a typed contract instead of a chat prompt. The Queen can plan and provision, but the Bee runtime is constrained by the compiled work order. The MCP connector layer then resolves tool calls inside the active tenant and policy scope.

The reported prototype is small but useful. It uses Python, tenant-scoped MCP connectors, real stdio MCP adapters backed by a local FastMCP server, a policy engine mediating tool invocation, an MCP registry, and a skill registry. On 59 enterprise-style tasks, the retrieval-driven Queen-Bee variant reports 0.964 task success, 1.000 finance guardrail blocking, 1.000 cross-tenant blocking, 1.000 tenant-scope accuracy, and one wrong-tool call. The no-policy and single-agent baselines both fail the finance and cross-tenant blocking metrics.

Do not over-read those numbers. The paper is explicit that this is prototype-level systems evidence, not a production deployment study. The task set is synthetic, the MCP stack uses local demo business systems, the governance model is mostly rule-based, and the registry-noise test is structured rather than open-world. The important result is the architecture: scoped provisioning makes the residual failures narrower and easier to debug.

## Why it matters

MCP makes it easy to expose tools. It does not decide which principal should see which tool, which subagent should execute which part of the task, which memory namespace is in scope, or which approval is needed before an external effect.

That missing layer is where enterprise agents break.

A general agent with a broad MCP catalog can be impressive in demos and unacceptable in production. It may complete the task while crossing tenant boundaries, touching the wrong SaaS surface, leaking sensitive context into summaries, calling a high-risk tool for a low-risk request, or leaving no artifact explaining why that tool was allowed.

Queen-Bee gives the stack a better shape:

1. Retrieve capabilities from structured registries.
2. Compile a task-scoped execution boundary.
3. Provision a specialized worker with only the relevant tools, skills, memory, tenant, and policy.
4. Mediate every tool call through a gateway or connector layer.
5. Preserve the compiled contract and tool decisions in the trace.
6. Evaluate not only success, but routing accuracy, scoped execution quality, blocked unsafe requests, wrong-tool calls, and failure-mode concentration.

The paper's strongest line is in the implication, not the naming: enterprise agent systems should be evaluated by governed provisioning, bounded execution, workflow coordination, and failure-mode quality, not only final task completion.

## How it fits into the agentic stack

Enterprise MCP orchestration belongs primarily in AgenticAI because it is a runtime architecture pattern. It has strategic consequences, but the load-bearing object is the harness contract between planner and executor.

Stack placement:

- **Intent layer:** user request, task class, tenant, risk class, and allowed operating mode.
- **Capability registry:** MCP tools, skills, domains, risk levels, dependencies, owners, tenant metadata, and validation status.
- **Control plane:** retrieves capabilities, decomposes the task, chooses subagents, and emits BeeSpec-style work orders.
- **Execution contract layer:** stores the structured work order: role, memory scope, tool scope, policy profile, approval gates, output contract, and trace identifiers.
- **Worker layer:** executes under the contract, not under broad ambient authority.
- **Gateway layer:** enforces identity, policy, tenant scope, data projection, and external-effect approval before tools observe the full request.
- **Trace layer:** records contract hash, selected tools, denied tools, policy checks, approvals, summaries, raw-evidence pointers, outputs, and final effects.
- **Evaluation layer:** compares single-agent, static specialized, retrieval-provisioned, no-policy, and noisy-registry variants under the same task suite.

This also connects directly to the week's other findings. Less Context, Better Agents says active context should be pruned and summarized rather than blindly retained. SecureClaw says sensitive reads and external effects need separate trusted boundaries. The skills and context-rot papers say procedural guidance is authority-bearing and must be maintained. BeeSpec is where those policies can become one auditable run contract.

## Practical tools, repos, and methodologies worth trying now

Implement the idea before copying the branding.

### Tools and repos

- **Pydantic or JSON Schema** for the execution contract: `role`, `tenant_scope`, `memory_scope`, `allowed_tools`, `attached_skills`, `policy_profile`, `approval_gate`, `output_contract`, and `trace_id`.
- **FastMCP** for local MCP servers and test connectors before using real enterprise systems.
- **LangGraph, Temporal, Prefect, or a simple state machine** for Queen-style planning, task decomposition, worker dispatch, approvals, and retries.
- **OPA, Cedar, or OpenFGA** for policy checks over tool, tenant, data class, workflow state, and approval artifacts.
- **OpenTelemetry, Langfuse, LangSmith, or JSONL traces** to record work-order hashes, capability retrieval, selected tools, denied tools, approvals, and final effects.
- **SecureClaw-style PREVIEW→COMMIT** for effectful writes and opaque-handle summaries for sensitive reads.
- **Context-retention ablations** from Less Context, Better Agents to keep raw transcripts out-of-band and only active summaries in the worker prompt.

### Methodologies

1. **Start with one internal workflow.** Pick a workflow with two domains, one sensitive data class, and at least one side-effecting tool.
2. **Build the registry.** Give every tool domain, risk level, tenant scope, owner, dependencies, expected inputs, and side-effect class.
3. **Define the work-order schema.** The schema should be reviewable without reading a prompt transcript.
4. **Run baselines.** Compare broad single-agent, static worker, retrieval-provisioned worker, and no-policy variants.
5. **Score governance directly.** Measure blocked unsafe requests, wrong-tool calls, tenant-scope accuracy, approval compliance, and final task success.
6. **Preserve raw evidence separately.** Workers should receive scoped summaries and handles, while raw transcripts and sensitive values remain in a trusted store.
7. **Treat work orders as artifacts.** Store them, hash them, diff them, replay them, and review changes like code.

## Implementation complexity

Implementability score: 0.72

A thin version is immediately buildable. A production version is real platform work.

### Implementable now

- Create a BeeSpec-like Pydantic schema.
- Put two or three MCP tools behind a local FastMCP server.
- Add a structured capability registry with tenant, domain, and risk metadata.
- Write deterministic policy checks for allowed tool, tenant, and approval class.
- Dispatch a scoped worker with only the tools and memory namespace in its contract.
- Log the contract hash and every tool decision.
- Run synthetic tasks that intentionally ask for cross-tenant access or finance-sensitive leakage.

### Architecture-heavy

- Real credential custody and on-behalf-of auth.
- Recursive delegation where a worker may spawn subworkers without laundering authority.
- Data classification across raw documents, summaries, memory writes, tool outputs, and artifacts.
- Production-quality registry maintenance, dependency tracking, and skill lifecycle governance.
- Adversarial evals that combine indirect injection, stale context, memory poisoning, wrong-tool routing, and approval bypass.
- Operational UX for humans to inspect, approve, replay, and revoke work orders.

The score is above 0.7 because the primitives exist. It is below 0.8 because getting identity, policy, memory, summaries, approvals, and MCP tools into one coherent runtime is not a weekend script.

## Strategic implications for Danny's worldview and product thinking

This reinforces the repo's central thesis: the agentic stack is becoming less about bigger prompts and more about governed runtime surfaces.

For Danny's product thinking, the useful abstraction is a **run contract**. Every serious agent run should be able to answer:

- What task was compiled?
- Which capabilities were retrieved?
- Which skills were attached?
- Which tools were allowed, and which were hidden or denied?
- Which memory namespace was in scope?
- Which tenant or account boundary applied?
- Which policy profile and approval gates controlled side effects?
- Which raw evidence was kept out of prompt but available for audit?
- Which final effects occurred?

That is a product surface. A local-first Friend Node or Hermes runtime can use the same idea without copying the enterprise packaging: compile user intent into a scoped, reviewable work order before a subagent gets tools. The moat is not having more MCP servers. The moat is safely turning MCP servers into bounded, replayable, owner-controlled work.

## Why this beat the other candidates this week

The other candidates were strong but narrower:

- Skills as governed artifacts had the broadest source volume, but skills are one dependency inside the run contract.
- Less Context, Better Agents had the cleanest immediate optimization, but context retention is one field of the runtime policy.
- SecureClaw had the sharpest security boundary, but it mainly covers sensitive reads and effectful writes.
- AGENTSERVESIM had strong serving implications, but it optimizes infrastructure after the work shape exists.
- OpenEnv helps standardize environments for agentic RL, but the training socket still needs governed capability boundaries.

Queen-Bee won because it gives the stack a unifying object: a compiled, auditable, scoped execution contract that ties planner, worker, skills, MCP tools, memory scope, policy, approval, and trace evidence together.

## What remains conceptual or unresolved

- The public paper does not point to a verified implementation repository, so treat the source as a design and evaluation reference, not a drop-in framework.
- The benchmark is synthetic and small. The reported 0.964 success rate should not be marketed as production evidence.
- The registry is highly structured. Open-world capability growth will create harder retrieval, compatibility, and policy conflicts.
- The security model is mostly rule-based. It still needs adversarial policy tests, data-flow tests, and cross-session authority tests.
- Tenant-scoped local MCP demos are not the same as real enterprise SaaS integrations with credential custody, audit retention, legal holds, and administrator override paths.

## Core source links

- Queen-Bee Agents: A BeeSpec-Centered Architecture for Governed Enterprise MCP Orchestration: https://arxiv.org/abs/2606.06545v1
- SecureClaw: Clawing Back Control of LLM Agents: https://arxiv.org/abs/2606.09549v1
- Less Context, Better Agents: Efficient Context Engineering for Long-Horizon Tool-Using LLM Agents: https://arxiv.org/abs/2606.10209v1
- Extending MCP support for Amazon Bedrock AgentCore Gateway: https://aws.amazon.com/blogs/machine-learning/extending-mcp-support-for-amazon-bedrock-agentcore-gateway-2/
- From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws: https://arxiv.org/abs/2606.06324v1

## June 30 update: MCP server patterns make the run contract easier to audit

MCP Server Architecture Patterns strengthens the run-contract thesis with a production taxonomy. A work order should not only list allowed tools. It should also know whether a tool came from a Resource Gateway, Tool Orchestrator, Stateful Session Server, Proxy Aggregator, or Domain-Specific Adapter.

Practical lesson:
- tag every MCP server in the capability registry by architecture pattern, owner, auth mode, transport, version, and observed latency;
- cap visible tools by workflow and target model instead of exposing a whole registry;
- treat Proxy Aggregators and Stateful Session Servers as higher-review surfaces because they can multiply authority and context confusion;
- run tool-count ablations per target model before expanding an execution contract.

Sources:
- [MCP Server Architecture Patterns](https://arxiv.org/abs/2606.30317v1)
- [rodriguescarson/mcp-patterns-icsme2026](https://github.com/rodriguescarson/mcp-patterns-icsme2026)

## July 14 update: verified tool memory belongs with the provider

ToolAtlas extends the compiled-run-contract thesis upstream. A capability registry should not contain only static names and descriptions. The provider can maintain execution-verified traces, affordances, failure boundaries, uncovered regions, and cross-tool compositions as a versioned graph that every authorized caller can reuse.

Practical lesson:
- make provider memory agent-neutral and bind every record to tool version, environment version, verifier, and evidence time;
- discover boundaries through sandboxed offline probing, not unrestricted production exploration;
- preserve failed probes as evidence and require deterministic verification before promotion;
- filter provider memory by principal, tenant, policy, and allowed tool surface at the gateway;
- compare provider-side memory, agent-side memory, static descriptions, and no memory on one fixed task pack.

Artifact caveat: the MIT-licensed public repository exposes the graph-memory pipeline and a filesystem demonstration, but not the full eight-service experimental surface described in the paper.

Sources:
- [ToolAtlas](https://arxiv.org/abs/2607.11126v1)
- [PuppyKnightUniversity/ToolAtlas](https://github.com/PuppyKnightUniversity/ToolAtlas)

## July 20 update: large tool catalogs need retrieval and session planes

Scalable LLM Agent Tool Access in the Cloud turns the capability registry into a production data plane. Protocol adaptation, authorized retrieval, access control, session ownership, and response routing have to meet at the gateway. Returning a semantically relevant Top-K list without principal and session policy is not governed orchestration.

Practical lesson:
- filter tool discovery and invocation through the same identity, tenant, workflow, and policy contract;
- return stable server and tool identities with manifest versions, not descriptions alone;
- bind session owner, return path, shared-state locator, and trace sink before the first tool call;
- measure retrieval recall, selection accuracy, prompt tokens, latency, and authorization errors together;
- load-test cross-instance misses and Pub/Sub response routing, not only stateless request throughput.

Evidence caveat: the paper reports an Alibaba Cloud production system and public ToolBench comparisons, but does not release the evaluated gateway implementation.

Source:
- [Scalable LLM Agent Tool Access in the Cloud](https://arxiv.org/abs/2607.15593v1)

## Working conclusion

The architectural lesson is simple: do not hand a capable model a broad tool catalog and call it an agent platform. Compile the run first.

A BeeSpec-style contract, whether or not it uses that name, is the missing middle layer between natural-language planning and side-effecting execution. It is where skills, tools, memory, tenant scope, approvals, context policy, and trace evidence become one inspectable artifact.
