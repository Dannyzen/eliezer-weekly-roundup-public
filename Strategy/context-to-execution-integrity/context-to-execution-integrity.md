# Context-to-Execution Integrity

Last updated: 2026-07-08

Core finding: writable context is not execution authority. An agent may read an issue, README, CI log, email, tool result, memory, or retrieved page, but protected sink fields need a typed release, exact-effect authorization, and invocation capability before the host lets a side effect happen.

Core sources:
- Context-to-Execution Integrity for LLM Agents: https://arxiv.org/abs/2607.06000v1
- CXI anonymous artifact repository: https://anonymous.4open.science/r/cxi
- Context-to-Execution Integrity PDF: https://arxiv.org/pdf/2607.06000v1
- Unicode TAG-Block Concealment of Tool-Metadata Payloads in MCP: https://arxiv.org/abs/2607.05744v1
- Agent Data Injection Attacks are Realistic Threats to AI Agents: https://arxiv.org/abs/2607.05120v1
- Untrusted Content Masking for Web Agents with Security Guarantees: https://arxiv.org/abs/2607.05277v1
- Untrusted Content Masking repository: https://github.com/ethz-spylab/untrusted-content-masking
- SessionBound: https://arxiv.org/abs/2607.00751v1
- SessionBound repository: https://github.com/SessionBound/sessionbound
- HCP execution-control paper: https://arxiv.org/abs/2606.29073v1
- HCP reference repository: https://github.com/SymbolicLight-AGI/handle-capability-protocol

## Overview

Context-to-Execution Integrity, CXI, is the strongest finding from the 2026-07-02 to 2026-07-08 window because it turns the week's security findings into one buildable runtime boundary.

The same week produced important pieces: Untrusted Content Masking masks hostile DOM content before planning; Agent Data Injection shows malicious data can masquerade as trusted metadata; Unicode TAG-block concealment shows an MCP approval dialog can hide model-visible tool metadata; SessionBound turns approved database work into scoped sessions. CXI is the layer that connects them. It says the final transition from context to tool execution must be mediated by field authority, effect authority, and invocation authority bound to the same canonical action manifest.

That is the durable point: evidence can influence reasoning, but authority must be released.

## Why this won the week

CXI beats the other candidates because it is not another local defense. It supplies the missing grammar for the execution-control plane.

- Unicode TAG-block concealment is urgent, but it is one approval-view fidelity failure.
- Untrusted Content Masking is highly implementable, but it is primarily a web-observation boundary.
- Agent Data Injection is a strong threat model, but it mostly names the attack class.
- StateFuse is useful for memory, but it is a state-contract improvement, not the authority boundary itself.
- Regression gates and Kotlin SWE-bench are immediately useful for coding-agent evaluation, but they do not define who may create side effects.

CXI wins because it gives the same answer across web agents, coding agents, database agents, memory writes, shell commands, package manifests, API sends, and delegated subagents: protected effects require typed releases and manifest-bound admission.

## Core innovation

The core innovation is a destination-scoped release gate between attacker-writable context and protected execution.

CXI separates five roles:

1. Trusted state: user objective, policy, registry, approvals, grant state, trusted snapshots.
2. Writable context: attacker-writable or attacker-influenced material such as issues, docs, logs, retrieved pages, package metadata, tool outputs, persistent memories, or other agents' messages.
3. Typed release: trusted validator output that moves a narrow value from writable context to one destination field.
4. Opaque data: preserved evidence that can be quoted or reviewed but carries no authority.
5. Protected sink field: any field that selects, authorizes, parameterizes, schedules, retries, or interprets a side effect.

The admission pipeline is explicit:

1. Canonicalize the candidate action into an action manifest.
2. Check each protected field against field-local authority and provenance.
3. Check sink-interpreted payloads against exact-effect commitments.
4. Authorize the invocation with a manifest-bound capability.
5. Consume the capability to obtain an execution lease.
6. Execute only through the mediated sink.

The compact rule is:

- Raw writable context cannot fill a protected field.
- A typed release can authorize only one destination field.
- A patch, SQL query, shell command, package manifest, CI workflow, or file body needs exact-effect authorization over what the sink will actually do, not just valid syntax.
- A retry, batch, schedule, delegation, or spend event needs invocation authority.
- Opaque data re-enters later side-effecting boundaries as writable context again.

## Why it matters

Most agent platforms still collapse evidence and authority into the same prompt. That is the vulnerability.

A user asks an agent to fix a bug. The agent reads an issue, a README, a failing CI log, dependency metadata, a tool result, and maybe prior memory. Some of that material is useful. Some may be attacker-controlled. Current systems often let the model turn that blended context directly into a tool name, file path, shell command, package target, PR body, memory write, API recipient, or approval state.

CXI makes that illegal by construction. Context can be read. Context can be quoted. Context can be validated into one narrow value. But context cannot silently choose a protected effect.

This matters for Danny's stack because Hermes, FriendVM, desktop/browser agents, MCP tools, and managed subagents all cross this boundary constantly. The hard question is not whether the model can propose a plausible action. The hard question is whether the host can prove that the proposed action had authority to execute.

## Fit into the agentic stack

Primary layer: Strategy, execution-control and gateway governance.

Secondary implementation layers:

- Agent gateway: labels tool schemas, protected fields, tool metadata, allowed operations, and approval state.
- Execution broker: canonicalizes candidate actions, checks releases, validates exact effects, consumes capabilities, emits leases.
- Sandbox worker: limits process, filesystem, browser, network, and credential damage if a mediated action is still wrong.
- Evidence plane: stores provenance, release records, manifest digests, allow and deny traces, and source object IDs.
- Evaluation harness: tests prompt-injection, data-injection, field laundering, wrong-field release reuse, opaque reentry, schema repair, duplicate invocation, and alternate sink bypass.

CXI also clarifies the difference between four often-confused layers:

- Prompt defense reduces unsafe proposals.
- Typed release admits only narrow values.
- Exact-effect authorization checks what the sink will do.
- Sandbox containment limits damage after execution.

A serious platform needs all four. CXI is the execution admission layer.

## What the paper actually evaluated

The paper reports several separate evaluation surfaces. They should not be averaged into one score.

- AgentDojo live task bank: 720 episodes, 1,739 LLM calls, 199 safe task completions across six live conditions. The exact-effect subset records 306 field records and 204 leases/effects with zero observed field, effect, or invocation escapes in protected admissions.
- Code-agent exact-effect benchmark: 400 repository episodes, 231 safe task completions, 73 parse failures, 61 parse-ok rows without effect authorization, and 35 authorized executions that failed the task oracle. The paper reports zero observed field, effect, or invocation escapes in this mediated setting.
- Manifest-bound ledger faults: 10 cases and 29 consume attempts, with 19 rejects and two deduplicated retries. The ledger row is about admission faults, not task success.
- Hosted/API field-local compatibility: 800 archived rows, 85 unsafe selections blocked, zero gate escapes, and zero parse failures. This is compatibility evidence, not provider-internal proof about attention masks or KV lineage.
- Mechanism baseline: schema-only structured output still admits unauthorized execution in the reported CXI-Core cases, while the CXI boundary checks source authority and reports zero unauthorized execution or gate escapes in that row.

The artifact repository is useful because it exposes policy and tool-schema manifests, field classifications, declassifier specs, exact-effect adapter records, invocation-ledger traces, archived result roots, generated tables, and replay scripts.

## Practical tools, repos, and methodologies worth trying now

Tools and sources:

- CXI artifact for decision-core extraction, policies, manifests, gate decisions, evidence records, and replay scripts: https://anonymous.4open.science/r/cxi
- HCP reference runtime for principals, grants, handles, capabilities, policy decisions, and audit entries: https://github.com/SymbolicLight-AGI/handle-capability-protocol
- SessionBound for task-scoped database sessions and budgeted execution: https://github.com/SessionBound/sessionbound
- Untrusted Content Masking for DOM quarantine before web-agent planning: https://github.com/ethz-spylab/untrusted-content-masking
- OPA, Cedar, or OpenFGA as candidate policy engines for principal, resource, field, release, and effect checks.
- OpenTelemetry or JSONL traces for release, manifest, allow, deny, lease, and final-effect records.

Methodologies to try first:

1. Classify protected sink fields for every privileged tool: tool, operation, recipient, URL, account, file path, shell command, SQL statement, branch, PR target, package registry, deployment target, approval state, retry schedule, memory-write key, external-send body.
2. Add opaque evidence slots so untrusted material can be preserved without gaining authority.
3. Write three typed releases before attempting a full system: FilePath, ApprovalRef, and BoundedRecipient.
4. Bind releases to principal, task, destination field, validator, policy version, source scope, expiry, and manifest digest.
5. Add exact-effect adapters for repository patch, file body, SQL, and shell command before broad tool rollout.
6. Consume invocation capabilities through a ledger before execution so retries, batches, schedules, and duplicate submits cannot be controlled by writable context.
7. Add fixtures where issue bodies, READMEs, CI logs, tool outputs, and memory entries contain plausible but unauthorized values.
8. Emit deny events with reason codes. A blocked release without evidence is not governance.

## Implementation complexity

Implementability score: 0.70

A thin version is implementable now. The first useful prototype does not need a full formal IFC system or custom model serving stack. It needs a broker that wraps privileged tools, labels protected fields, stores opaque evidence separately, runs validator functions, emits typed releases, canonicalizes the proposed action, and rejects calls that lack matching release, effect, and invocation records.

Production implementation is harder for five reasons:

1. Complete mediation is unforgiving. Every side-effecting route must pass through the gate, including helper APIs, generated files, bots, install hooks, browser actions, memory writes, and delegated subagents.
2. Validator quality becomes trusted infrastructure. A bad FilePath, SQL, patch, package, or shell validator can bless the wrong effect.
3. Hosted models cannot expose provider-internal attention, mask, or KV-cache lineage, so they can provide host-observed compatibility evidence but not the strongest open-weight evidence.
4. Exact-effect authorization is adapter-specific. Repository patches, shell commands, SQL, file writes, CI workflows, and API sends each need different canonicalization.
5. Operator UX is still unsolved. Humans need understandable release requests and denial reasons, not raw provenance graphs.

The score is above 0.5 because the artifact and object model are concrete. It is not above 0.8 because a real deployment needs policy state, validator tests, trace storage, complete mediation, sandbox integration, and readable operator workflows.

## What remains conceptual or unproven

- The paper does not prove validator completeness.
- The hosted/API path does not prove provider-internal mask, attention, or KV-cache enforcement.
- The results are observed under fixed task banks, policies, adapters, and archived traces, not arbitrary production workloads.
- Exact-once external delivery still needs service-specific mechanisms.
- Complete mediation remains a deployment obligation.
- Task quality is separate from admission integrity. CXI can admit only authorized effects, but the authorized effect may still be a bad patch or bad answer.

## Strategic implications for Danny's worldview and product thinking

The strategic lesson is that autonomy becomes governable when the runtime owns the transition from evidence to authority.

For Hermes and FriendVM, CXI suggests a concrete product direction:

- Treat tool calls as proposed manifests, not direct model output.
- Treat user approvals as scoped grant inputs, not generic chat consent.
- Treat retrieved text, browser DOM, tool results, repo files, and memory as evidence with trust class, not as authority.
- Treat high-risk arguments as protected sink fields that require release records.
- Treat release denial as a first-class UX event with a reason and recovery path.
- Treat MCP servers as providers behind a broker, not as the broker.

This reframes agent sovereignty. Sovereignty is not only self-hosting or local execution. It is owning the gate where context becomes action.

## First prototype shape

Start with one narrow tool class: repository file writes.

1. Wrap `write_file`, `patch`, and shell file mutation behind an execution broker.
2. Mark protected fields: operation, path, file body, patch delta, commit target, and invocation event.
3. Keep issue text, CI logs, README text, and tool outputs as opaque evidence slots.
4. Add FilePathRelease from trusted validator code that canonicalizes repo-relative paths and checks allowed directories.
5. Add exact-effect authorization for patch/file-body state delta against base commit.
6. Add invocation capability for one task, one branch, one path set, one policy epoch, and one expiry.
7. Emit JSONL records for proposed action, releases, exact-effect commitment, gate decision, lease, execution result, and denial reason.
8. Add adversarial fixtures: copied `approved`, hidden target paths in logs, retry requests in tool output, package install hooks, and README instructions that try to change protected fields.

If that works, extend to shell commands and browser actions. Do not start with every tool.

## Core source links

- Context-to-Execution Integrity for LLM Agents: https://arxiv.org/abs/2607.06000v1
- CXI anonymous artifact repository: https://anonymous.4open.science/r/cxi
- Context-to-Execution Integrity PDF: https://arxiv.org/pdf/2607.06000v1
- Unicode TAG-Block Concealment of Tool-Metadata Payloads in MCP: https://arxiv.org/abs/2607.05744v1
- Agent Data Injection Attacks are Realistic Threats to AI Agents: https://arxiv.org/abs/2607.05120v1
- Untrusted Content Masking for Web Agents with Security Guarantees: https://arxiv.org/abs/2607.05277v1
- Untrusted Content Masking repository: https://github.com/ethz-spylab/untrusted-content-masking
- SessionBound: https://arxiv.org/abs/2607.00751v1
- SessionBound repository: https://github.com/SessionBound/sessionbound
- HCP execution-control paper: https://arxiv.org/abs/2606.29073v1
- HCP reference repository: https://github.com/SymbolicLight-AGI/handle-capability-protocol
