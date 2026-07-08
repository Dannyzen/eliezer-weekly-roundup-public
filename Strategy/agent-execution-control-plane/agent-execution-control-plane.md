# Agent Execution Control Plane

Last updated: 2026-07-08

Core finding: MCP-style connection is not execution control. A serious agent runtime needs a separate layer that binds principal, grant, resource, capability, handle, data flow, policy decision, and audit evidence before tools create side effects.

Core sources:
- From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes: https://arxiv.org/abs/2606.29073v1
- HCP reference repository: https://github.com/SymbolicLight-AGI/handle-capability-protocol
- HCP security invariants: https://github.com/SymbolicLight-AGI/handle-capability-protocol/blob/main/docs/security-invariants.md
- HCP threat model: https://github.com/SymbolicLight-AGI/handle-capability-protocol/blob/main/docs/threat-model.md
- SessionBound: https://arxiv.org/abs/2607.00751v1

## Overview

The strongest finding from the 2026-06-25 to 2026-07-01 window is HCP, the Handle-Capability Protocol reference runtime from the paper "From Tool Connection to Execution Control." The paper's claim is narrow and useful: MCP-style ecosystems give agents a connection layer, but execution security remains scattered across clients, servers, prompts, approval dialogs, OAuth deployments, and logs.

HCP inserts a runtime object model between agent intent and provider execution. The runtime owns grants, policy decisions, data handles, data-pipe checks, task state, and audit entries. MCP-like tools can still exist, but the authority to act is no longer hidden inside a tool description, a prompt, or a UI approval checkbox.

This beat the other strong findings this week because it names the layer underneath them. ECHO needs source-indexed memory. CubeSandbox needs egress policy and audit. agents-cli needs lifecycle commands and skills. Agent community governance needs membership and replay. HCP supplies the missing execution-control grammar: who is acting, on which resource, under which grant, through which capability, with which data handle, and with which deny or allow evidence.

## Core innovation

The core innovation is to make execution-layer security invariants explicit, testable, and represented as runtime objects.

The paper defines eight invariants:

1. Metadata non-authority: tool metadata and descriptions do not grant authority.
2. Grant-backed approval: approval can confirm risk, but cannot replace a valid grant.
3. Canonical resources: providers supply canonical resource identifiers for policy decisions.
4. Principal binding: invocations and data projections are bound to an acting principal.
5. Scoped capability invocation: capabilities require matching scopes, resources, and grants.
6. Source-and-target data-flow authorization: moving data from one handle to another capability requires checks on both sides.
7. Deny-path audit: denials are first-class trace events, not silent failures.
8. Explicit protocol state: tasks, handles, grants, policy decisions, and audit entries are durable protocol objects.

The HCP repository extends that into a reviewable prototype with docs, schemas, SDK prototypes, conformance harnesses, MCP compatibility shims, and paper artifacts. Its README is explicit about the boundary: HCP is a reference prototype, not a production security platform.

## Why it matters

MCP made tool exposure easy. That also made a common mistake easier: treating reachability as authority.

A tool connection says the agent can reach a server. It does not prove that this principal should access this resource, that a user's approval covers this exact write, that the provider resolved the same resource the policy checked, that a handle can be piped into an external-send tool, or that a denied path leaves enough evidence for forensics.

HCP matters because it turns those questions into runtime checks. The paper evaluates three runtimes over 10 benchmark cases: a naive connection-layer baseline permits all modeled attacks, a practice-informed mitigation baseline with metadata linting, session checks, and per-call approvals still permits 6 of 10, while HCP blocks all 10 and preserves audit evidence. The local in-memory microbenchmark reports sub-millisecond mean latencies for measured policy, invocation, peek, and pipe operations.

Do not over-read those numbers. The benchmark is small and controlled. The latency result is local and in-memory. The repo has no production authentication, real signature verification, durable multi-tenant state, complete policy language, provider supervision, or full third-party MCP certification. The useful claim is not "deploy HCP tomorrow." The useful claim is "connection-layer mitigations are structurally insufficient without execution-control objects."

## Fit into the agentic stack

This belongs primarily in the Strategy layer because it is an authority and governance boundary. It also has direct AgenticAI implementation consequences.

Stack placement:

- Connection layer: MCP-style clients, servers, tools, resources, prompts, transports, and adapter shims.
- Execution-control layer: principals, grants, resources, capabilities, handles, policy decisions, approvals, data-pipe checks, tasks, and audit entries.
- Sandbox layer: OS, VM, browser, network, filesystem, and credential boundaries where code or tool effects actually happen.
- Trace layer: allow, deny, approval, handle projection, pipe, task, provider, and final-effect events.
- Evaluation layer: fixtures that test approval bypass, confused deputy resource resolution, handle exfiltration, data-flow laundering, grant enumeration, and missing-deny-audit cases.

The important separation is connection versus execution. MCP, A2A, ACP, ANP, and similar protocols should be treated as interoperability surfaces. They do not remove the need for a broker that owns authority, data handles, and evidence.

## Practical tools, repos, and methodologies worth trying now

Tools and repos:

- HCP reference repository for object vocabulary, schemas, conformance fixtures, and reproducibility artifacts: https://github.com/SymbolicLight-AGI/handle-capability-protocol
- MCP-style gateway or broker code in Danny's own stack as the place to experiment with grants, handles, and deny audits.
- OPA, Cedar, or OpenFGA for deterministic policy checks over principal, resource, capability, data class, workflow, and approval state.
- OpenTelemetry or JSONL traces for allow, deny, approval, pipe, handle, task, and final-effect events.
- CubeSandbox or another sandbox worker layer for OS and network isolation underneath the execution-control broker: https://github.com/TencentCloud/CubeSandbox

Methodologies:

1. Inventory privileged tools by effect class: read, write, execute, external-send, memory-write, credential-use, browser-act, deploy, and delete.
2. Define canonical resource functions before writing policy. Do not let caller hints decide what resource the provider actually touches.
3. Represent tool outputs as handles, not ambient prompt text, whenever the output may later flow into a write, send, shell, browser, database, or memory action.
4. Require both valid grant and approval for high-risk effects. Approval alone should never create authority.
5. Log deny paths with reason codes. A blocked action without audit is not governance.
6. Add fixtures for the exact failures HCP targets: metadata laundering, approval bypass, confused deputy, wrong-principal handle access, target-side pipe bypass, and grant enumeration.
7. Keep the execution-control broker separate from the sandbox. The broker decides authority. The sandbox limits damage if the broker or tool path fails.

## Implementation complexity

Implementability score: 0.71

A thin version is implementable now with normal engineering effort plus discipline: wrap privileged tools behind a broker, introduce principal and grant objects, canonicalize resources, represent sensitive outputs as handles, check source and target when piping data, and emit allow/deny audit events.

A production version is materially harder. It needs durable storage, policy versioning, credential custody, provider attestation, multi-tenant isolation, key management, incident response workflows, signed approvals, backward compatibility with existing MCP clients, and operator UX that makes denials debuggable rather than mysterious.

The score is above 0.7 because the object model and reference artifacts are available. It is not above 0.8 because production security depends on everything HCP explicitly says it does not yet provide.

## Strategic implications for Danny's worldview and product thinking

The product lesson is simple: the winning agent platform is not the one with the largest tool catalog. It is the one that can prove why a tool effect was allowed.

For Hermes, FriendVM, and any local-first agent product, the execution-control plane should become a first-class product surface:

- Run manifests should bind principal, task, allowed tools, memory scope, sandbox profile, policy version, approval gates, and trace sink.
- Tool outputs that may influence later actions should become handles with ownership, expiry, projection, and data-class metadata.
- Approval should be a signed artifact attached to a specific grant, resource, capability, and risk class, not a generic chat acknowledgement.
- Denied actions should be visible and replayable. A good denial explains the missing grant, resource mismatch, expired handle, insufficient scope, or missing approval.
- MCP servers should be admitted as providers behind the broker, not trusted as the broker.

This reframes agent sovereignty. Sovereignty is not only self-hosting models or running tools locally. It is owning the runtime boundary where intent becomes authority.

## July 4 update: permission UX creates grant evidence

Janus adds the user-facing half of the execution-control plane. HCP-style grants, handles, and audit objects define authority, but real agents still need a permission interface that decides when user context is necessary and when repeated prompting becomes fatigue. Janus makes that design space testable with multiple permission assistants, scenarios, responder profiles, and metrics.

Practical lesson:
- represent permission requests as typed actor, resource, capability, action, risk, source-evidence, and proposed-effect objects;
- test multiple permission modes instead of relying on one generic approval dialog;
- model user fatigue and alignment behavior in harness fixtures;
- convert approvals into scoped grant records and denials into durable reason-coded audit events;
- measure false approvals, false denials, prompts per task, completion, and attack resistance.

Sources:
- [Janus paper](https://arxiv.org/abs/2607.01510v1)
- [GraceBrigham/Janus](https://github.com/GraceBrigham/Janus)

## July 6 update: approved tasks should become budgeted sessions

SessionBound maps directly onto the execution-control thesis. A business approval should not become ambient database authority. It should compile into a short-lived task session with a signed token, safe views, row scope, denied fields, operation limits, query budgets, disclosure budgets, and receipts.

The general lesson extends beyond SQL. Email, object storage, CRM, ticketing, analytics, and admin consoles should all move from broad credentials to task-scoped execution sessions where the runtime enforces the bounds deterministically.

Practical lesson:
- bind approval to principal, task, resource scope, operation class, budget, expiry, and receipt sink;
- enforce scope at the provider or gateway, not in model instructions;
- log denied attempts as first-class audit evidence;
- make budget exhaustion and disclosure limits recoverable planning feedback;
- treat approval as a signed grant input, not as the grant itself.

Sources:
- [SessionBound](https://arxiv.org/abs/2607.00751v1)
- [SessionBound/sessionbound](https://github.com/SessionBound/sessionbound)


## July 8 update: writable context needs typed releases before execution

Context-to-Execution Integrity adds a practical rule to the execution-control plane: writable context can inform an agent, but it should not directly populate protected sink fields. Protected arguments need typed releases from opaque evidence slots to specific destinations under deterministic gates.

Practical lesson:
- mark protected sink fields on privileged tools before exposing them to agents;
- keep attacker-writable values in opaque slots until a validator releases a narrow value;
- bind each release to principal, task, destination, expiry, and reason;
- log allowed and denied releases as audit events;
- add fixtures where issue bodies, README files, CI logs, memories, and tool outputs contain plausible but unauthorized values.

Source:
- [Context-to-Execution Integrity for LLM Agents](https://arxiv.org/abs/2607.06000v1)

## What remains conceptual or unproven

- The benchmark is small: 10 modeled cases are useful fixtures, not a complete security evaluation.
- The GitHub ecosystem screen is a README-signal sample, not vulnerability research.
- The reference runtime is in-memory and explicitly not production security infrastructure.
- The repository does not claim real signature verification, durable multi-tenant storage, full OAuth integration, production policy language, provider supervision, or complete MCP certification.
- HCP's object model still has to be tested against messy real providers, streaming tool outputs, browser automation, generated code, long-lived memory, and recursive subagent delegation.

## Implementation checklist

1. Define principal, grant, resource, capability, handle, task, policy decision, approval, and audit event schemas.
2. Put all privileged tools behind the broker path.
3. Canonicalize resources in provider code before policy evaluation.
4. Store sensitive tool outputs behind handles and expose preview, summary, and full projections by principal.
5. Require source and target authorization for data-pipe flows.
6. Emit structured allow and deny events with stable reason codes.
7. Add benchmark fixtures for approval bypass, metadata authority, confused deputy, wrong-principal handle reads, target-side pipe bypass, and grant enumeration.
8. Run the broker above sandbox workers, not instead of sandbox workers.
9. Treat the policy and grant store as production infrastructure before using it for real users.

## Core source links

- From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes: https://arxiv.org/abs/2606.29073v1
- PDF: https://arxiv.org/pdf/2606.29073v1
- HCP reference repository: https://github.com/SymbolicLight-AGI/handle-capability-protocol
- HCP README: https://github.com/SymbolicLight-AGI/handle-capability-protocol/blob/main/README.md
- HCP security invariants: https://github.com/SymbolicLight-AGI/handle-capability-protocol/blob/main/docs/security-invariants.md
- HCP threat model: https://github.com/SymbolicLight-AGI/handle-capability-protocol/blob/main/docs/threat-model.md
- CubeSandbox, complementary sandbox substrate: https://github.com/TencentCloud/CubeSandbox
- Governance Gaps in Agent Interoperability Protocols, complementary layer-above-protocol argument: https://arxiv.org/abs/2606.31498v1
