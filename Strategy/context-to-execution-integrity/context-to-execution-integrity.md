# Context-to-Execution Integrity

Last updated: 2026-07-22

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
- Binding Drift paper: https://arxiv.org/abs/2607.18316v1
- Binding Drift code and data: https://github.com/shashank-indukuri/binding-drift

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

## July 14 update: typed releases need commit-time freshness

Temporary Authority, Permanent Effects adds a time dimension to CXI. A typed release can be valid when planning begins and stale when the effect becomes durable. The runtime must therefore carry the authorizing witness through derived state and recheck freshness, causal priority, effect binding, and eligibility at the commit boundary.

Practical lesson:
- add witness ID, source version, policy epoch, principal, target, effect digest, branch ID, expiry, and eligibility to high-risk action manifests;
- recheck those fields inside the final commit activity after every wait, retry, callback, approval, or delegated result;
- distinguish visible completion from authorized completion in evaluation and production telemetry;
- fail closed when the dependency path is incomplete, even if the final payload still looks correct;
- build invalidation fixtures for expired approvals, changed targets, cancelled branches, superseded memory, and ineligible worker output.

Evidence caveat: the controlled suite demonstrates the mechanism, not deployment prevalence, and no public CommitGuard implementation repository was found during the July 14 scan.

Source:
- [Temporary Authority, Permanent Effects](https://arxiv.org/abs/2607.10487v1)

## July 19 update: imagined future is evidence, not an action receipt

BadWAM adds a model-output consistency failure to the context-to-execution boundary. A world-action model can keep its predicted future comparatively close to the clean future while the emitted action shifts enough to fail the task. The preview and command are coupled representations, not one proof object.

Practical lesson:
- canonicalize the exact action payload and predicted effect;
- bind preview, action, principal, target, policy version, and expiry in one manifest;
- validate the payload again at the executor boundary;
- observe post-action state through an independent channel;
- test preview-action divergence, late action substitution, and plausible-preview attacks as runtime fixtures.

Sources:
- [BadWAM](https://arxiv.org/abs/2607.15207v1)
- [LiQiiiii/BadWAM](https://github.com/LiQiiiii/BadWAM)
- [BadWAM models](https://huggingface.co/collections/LIQIIIII/badwam)

## July 20 update: authorized identity is not authorized dispatch

Neural Cryptographic Services sharpens the CXI release object. A valid principal and allowed tool do not authorize arbitrary step order or arguments. The planner should hold no execution authority. A deterministic controller should verify the signed instruction stream, release one step at a time, and bind the proposed dispatch to the exact authorized payload.

Practical lesson:
- canonicalize operation, target, arguments, principal, policy epoch, expiry, and prior-step hash;
- sign the approved sequence outside the model;
- release one instruction at a time and reject reordered or mismatched calls before execution;
- preserve proposal, release, denial, execution result, and post-state in one receipt chain;
- measure both attack success and benign utility because strict gates can suppress legitimate work.

Evidence caveat: NCS reports strong AgentDojo and 85-case argument-hijack results, but GPT-4o-mini loses utility under the full defense, the custom benchmark is author-built, and no public implementation is linked.

Source:
- [From Neural Intent to Cryptographic Authorization](https://arxiv.org/abs/2607.15596v1)

## July 21 update: effect types make requested actions visible before commit

ETAS strengthens CXI by making effects, trace obligations, prompt trust, approvals, and commit events part of the program rather than middleware convention. Static checks can discharge known obligations, while residual monitors guard dynamic targets and resources at runtime.

Practical lesson:
- assign every tool a typed effect and protected resource set;
- compile workflow policy into preflight monitors and residual runtime checks;
- keep request, approval, handling, denial, commit, and post-state as distinct events;
- reject undeclared effects and replay of irreversible commits;
- use effect manifests inside existing runtimes before considering a new language.

Evidence caveat: the paper claims a Rust prototype and formal safety properties, but links no public implementation and presents an evaluation plan rather than measured production comparison. Treat ETAS as a design reference.

Source:
- [ETAS: An Effect-Typed Language for Agent Systems](https://arxiv.org/abs/2607.17780v1)

## July 22 deep dive: target bindings need re-derivation before effects

### Overview

For this week's architecture review, Binding Drift is the strongest finding because it identifies a missing execution-control object: the target binding. An agent may resolve the correct target and drift later, or preserve the same target ID while acting on the wrong entity when the initial binding was wrong. The paper does not test ID reuse, concurrent registry mutation, or a correct stable ID becoming stale.

The durable rule is simple: persistence transports a binding, but only re-derivation checks it. Before a material effect, the runtime should independently resolve the target from the original authorized request and current candidate state, compare that result with the carried binding, and block or escalate disagreement.

This beats the week's alternatives as a deep-dive topic. Microsoft shipped the most immediately usable harness, but a harness release does not define a target-integrity contract. ResearchArena shows that generated artifacts need hidden behavioral tests, but it is expensive and already captured in Runtime Governance. Stop Means Stop remains the strongest effect-gate evidence, but it was central to the July 17 synthesis. Preemptive DLP hardening is broader security work, but it exposes no public implementation artifact. Binding Drift adds a new, reproducible primitive to the existing Context-to-Execution Integrity model.

### Core innovation

The paper separates two failure modes that ordinary workflow state collapses:

- Binding drift: the agent resolves the correct entity first, then silently switches later.
- Error propagation: the agent starts with the wrong entity and faithfully carries that mistake through later actions.

An entity lock eliminates the first failure while amplifying the second. The right object is therefore not a bare ID. It is a target-binding record with at least:

- canonical entity type and ID;
- source mention from the original authorized instruction;
- candidate-set or registry snapshot identifier;
- resolver identity and method;
- evidence and confidence or ambiguity state;
- task, principal, policy epoch, expiry, and state version;
- binding digest attached to the action manifest.

The paper's tested cross-verifier overwrites a disagreeing binding. This deep dive makes a separate production inference: at every material effect, independently re-derive the target from the original request and trusted current entity state. Agreement can renew the binding. Disagreement or ambiguity should block the effect and route to clarification, a trusted deterministic resolver, or human review. A second model can supply evidence, but it does not become execution authority by itself. This deny-or-escalate pattern still needs direct validation.

### Evidence

The v1 paper uses 200 synthetic workflow templates with 890 total steps, 580 entity-binding-scored steps, four enterprise domains, five drift patterns, and eight model backends accessed through Amazon Bedrock. In the natural condition, author-reported drift appeared in 18 percent of eligible workflows, those correctly bound at the first scored action, when results were pooled across models. This is a benchmark result, not an estimate of deployment prevalence. On the fixed cohort with at least three action steps, wrong-target rate rose from 3 percent at steps one and two to 28 percent at step three.

Under controlled injection, 1,280 eligible workflow runs were evaluated per defense configuration, eight models times 160 non-ambiguity workflows. Locking the seeded wrong entity increased pooled downstream wrong actions from 907 to 2,746, a 3.0x amplification with a bootstrap 95 percent confidence interval of 2.8x to 3.3x. A cross-verifier using Nova Micro reduced pooled wrong actions to 189, or 0.21x baseline with a 95 percent confidence interval of 0.18x to 0.25x, compared with 180, or 0.20x, for the paper's approximate oracle comparator. These close aggregate values do not establish statistical equivalence, and the oracle is not strict because it handles derived slots imperfectly.

The public repository was inspected read-only. It has a populated 30-entry tree with the 200-workflow dataset, saved natural and injection results, aggregation code, an offline 25-assertion test, and an MIT license for code. Its README declares CC BY 4.0 for data and results. The latest commit records the full eight-model sweep.

### Why it matters

I interpret Binding Drift as an extension of Context-to-Execution Integrity. Typed releases, exact-effect commitments, and invocation capabilities are incomplete if the target named in a valid release was wrong initially or silently changed inside workflow state. The paper directly studies initial error propagation and later drift; stale registries and concurrent mutation remain production hypotheses to test.

This matters most for irreversible or externally visible effects:

- sending email or money;
- mutating CRM, ticketing, identity, or billing records;
- deploying to an environment or cluster;
- modifying a repository, branch, package, or release;
- reading or writing persistent memory;
- delegating authority to another agent.

A stable but wrong target is more dangerous than an obvious tool error because the action can be syntactically valid, policy-permitted, and consistently logged.

### Fit into the agentic stack

Primary layer: Strategy, context-to-execution integrity and execution control.

Supporting layers:

- Agent gateway: canonical entity registry, candidate retrieval, and target-binding schema.
- Harness: immutable original instruction, current workflow state, and explicit ambiguity path.
- Execution broker: commit-time re-derivation, binding comparison, deny or escalate decision, and manifest-bound lease.
- Evidence plane: target provenance, resolver output, candidate snapshot, mismatch, clarification, and final-effect receipt.
- Evaluation harness: controlled wrong-binding injection, natural drift measurement, long-horizon target switches, stale registry state, and concurrent updates.

### Practical tools, repositories, and methodologies worth trying now

1. Start with one high-risk tool family such as CRM updates, repository writes, or outbound messages.
2. Replace raw target IDs in workflow state with typed binding records.
3. Preserve the original user referent separately from summaries and compaction output.
4. Re-resolve the target before each write or send using current registry data and an independent context.
5. Require exact agreement on canonical ID, entity type, and policy scope before automatic execution.
6. Block and clarify on ambiguity. Do not silently let the verifier overwrite a target and continue.
7. Inject known-wrong early bindings in tests, then measure drift, propagation, wrong effects, clarifications, task completion, latency, and cost separately.
8. Bind the final target digest into the exact-effect commitment and receipt.

Useful starting points:

- Binding Drift code, workflows, saved results, and offline checks: https://github.com/shashank-indukuri/binding-drift
- CXI action-manifest and release model: https://anonymous.4open.science/r/cxi
- HCP execution-control objects: https://github.com/SymbolicLight-AGI/handle-capability-protocol
- OPA or Cedar for deterministic target, principal, and effect policy checks.
- OpenTelemetry or JSONL for binding provenance and mismatch events.

### Implementation complexity

Implementability score: 0.82

Under this repository's rubric, the score is high because a prototype needs only preserved original intent, typed binding state, an independent resolution step, and a fail-closed gate. It remains below 0.9 because real identity registries, complete mediation, concurrency, derived targets, and operator escalation are material engineering work. The paper reports roughly 0.3 seconds of added latency per action for its small cross-verifier.

Production work is materially harder. Real systems have aliases, merges, stale caches, concurrent changes, derived targets such as an account owner, multiple registries, and legitimate target changes. Complete mediation is also required: every side-effecting path must consume the checked binding, not a nearby unverified ID.

### Weakest point and what remains unproven

The benchmark uses synthetic entity stores and workflows of three to eight steps. All live models ran through one provider, Amazon Bedrock. The reported 18 percent natural drift rate is a controlled-benchmark result, not measured enterprise prevalence.

The cross-verifier also trades action risk for friction. In the injected experiment it produced 2,056 actions labeled "over-clarifications" by the paper, versus 743 at baseline, while strict workflow success was 25.2 percent versus 29.2 percent. The paper cautions that clarification under an injected state conflict may be rational. Its strict workflow-success metric also treats clarification, wrong-tool selection, malformed output, and API errors as failures. The verifier sharply reduced wrong actions, but it did not create a free reliability gain. A production gate needs a deterministic resolver or human escalation path for disputed bindings.

Evidence status: this is a first-version arXiv preprint using synthetic three-to-eight-step workflows and one serving provider. The paper and public repository were inspected read-only, but the artifact was not executed and the numerical results were not independently reproduced.

The repository README contains one stale summary sentence with earlier 2.6x and 5.4x figures, while the paper, saved-result headline, and latest commit report 3.0x aggregate and 8.5x maximum amplification. Use the paper and released result files as the quantitative source of record.

### Strategic implications for Danny's worldview and product thinking

The strategic lesson is that durable state is not trustworthy state. Event logs, checkpoints, memory, and workflow engines preserve what happened, including wrong resolutions. Sovereignty requires the runtime to own not only state persistence but also target truth at the moment of effect.

For Hermes and FriendVM, this suggests a concrete product invariant: every privileged tool call should carry a target-binding receipt, and a material effect should fail closed when the target cannot be independently reconstructed from authorized intent and current state.

That moves agent safety from generic confirmation toward a specific operator question: "Which exact entity will this action affect, how was that identity derived, and was it rechecked after the last wait, compaction, retry, or delegation?"

### Core source links

- Binding Drift in Multi-Step Tool-Augmented Agents: https://arxiv.org/abs/2607.18316v1
- Binding Drift immutable PDF: https://arxiv.org/pdf/2607.18316v1
- Binding Drift code and data: https://github.com/shashank-indukuri/binding-drift
- Context-to-Execution Integrity for LLM Agents: https://arxiv.org/abs/2607.06000v1
- CXI artifact: https://anonymous.4open.science/r/cxi


## August 6 update: unresolved worlds cannot release side effects

SafeCommit strengthens context-to-execution integrity by refusing to convert memory-grounded context into external action until every retained world certifies the effect. The release gate is not a better summary. It is a certificate, a probe, or a fallback.

Practical lesson:
- treat memory, tool output, and provenance as world-set inputs;
- bind side-effect release to certificates over retained worlds;
- keep probe selection inside the control plane;
- preserve commit and fallback receipts with the supporting world set.

Sources:
- [SafeCommit](https://arxiv.org/abs/2608.04289v1)
- [akewarmayur/SafeCommit](https://github.com/akewarmayur/SafeCommit)
