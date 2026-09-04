# Memory Authority Control Plane

Last updated: 2026-08-19

Primary layer: Strategy / runtime governance

Implementability score: 0.74

Core sources:
- Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees: https://arxiv.org/abs/2606.24322v1
- MEM-INV-Bench / TMA-NM repository: https://github.com/yedidel/mem-inv-bench
- MEM-INV-Bench dataset: https://huggingface.co/datasets/anonymos-2321135/MEM-INV-Bench
- Governed Shared Memory for Multi-Agent LLM Systems: https://arxiv.org/abs/2606.24535v1
- AgentRiskBOM: A Risk-Scoping Security Bill of Materials for Agentic AI Systems: https://arxiv.org/abs/2606.21877v1
- Lingering Authority: Revocable Resource-and-Effect Capabilities for Coding Agents: https://arxiv.org/abs/2606.22504v1
- MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows: https://arxiv.org/abs/2608.10509v1

## Overview

The strongest finding of the week is that long-term memory is now an authority surface.

A durable memory is not just context. If a future agent can retrieve it and act from it, the memory record is effectively a stored capability request. That means memory systems need a control plane: write-time origin authority, scoped retrieval, elevation rules, provenance preservation, and action-time enforcement.

The core paper, `Securing LLM-Agent Long-Term Memory Against Poisoning`, matters because it moves memory security from detection to authority engineering. The paper verifies the hard failure mode: existing content and lineage defenses fail under laundering, with up to 68% laundering attack success, while TMA-NM reaches 0% attack success on direct and laundering attacks across the tested models and channels.

## Core innovation

The paper's useful move is to stop asking whether a recalled memory looks malicious.

The control question is: what authority did this memory have when it was written, and has any later transformation legitimately elevated that authority?

TMA-NM, Tamper-evident Memory Authority, Non-Malleable, does three things that should become standard in serious agent runtimes:

1. Bind authority at write time to the memory origin.
2. Propagate that authority non-malleably through summaries, retrieval, and derived notes.
3. Elevate authority only through Sybil-resistant corroboration from independent trusted principals.

This is a strategic improvement over prompt-injection filters. A filter tries to classify text. An authority control plane decides whether a stored fact is allowed to influence a future action.

## Why this beat the rest of the week

Other findings this week were strong. ESAA-Conversational gives coding-agent handoff a clean event-sourced shape. GUI vs CLI shows skill coverage can beat visual interaction when final-state verifiers are matched. Governed Shared Memory turns fleet memory into a policy service. AgentRiskBOM and Lingering Authority define deployable authority artifacts and revocable capability handles.

Memory authority matters more because it is the cross-time version of the same problem. A prompt injection can die with the session. A poisoned memory can survive, be summarized, be echoed by a trusted tool, and later steer a consequential action after the visible attack context is gone.

That makes memory authority a product-layer primitive, not a research curiosity.

## How it fits into the agentic stack

- Memory systems: every stored memory needs origin, scope, derivation, authority tier, and elevation state.
- Runtime governance: the planner should see only memories whose authority is valid for the current task and effect.
- Agent gateway governance: memory search and direct memory reads need the same policy checks.
- Evidence provenance: summaries and embeddings must preserve source-event lineage and authority metadata.
- Agent authority manifests: workflow manifests should declare which memory scopes can inform which actions.
- Shared-state agents: fleet memory needs tenant, principal, task, and propagation controls before cross-agent recall.

The stack lesson is simple: retrieval is not enough. Recall must be mediated like tool use.

## Practical tools, repos, and methodologies worth trying now

1. Run the offline parts of `yedidel/mem-inv-bench` as a local regression suite before trusting long-term memory in an agent runtime.
   - Repository: https://github.com/yedidel/mem-inv-bench
   - Dataset: https://huggingface.co/datasets/anonymos-2321135/MEM-INV-Bench
2. Add authority fields to memory records:
   - `origin_principal`
   - `source_event_id`
   - `authority_tier`
   - `scope`
   - `derived_from`
   - `elevation_rule`
   - `valid_until`
   - `allowed_effects`
3. Add a memory gateway that mediates both semantic search and direct reads by the same policy.
4. Preserve provenance through summaries and embeddings. A summary may compress text, but it must not erase origin authority.
5. Create laundering fixtures:
   - self-summarization laundering;
   - trusted-tool echo laundering;
   - manufactured corroboration from non-independent sources;
   - stale memory that tries to authorize a new effect;
   - direct object read bypass of scoped retrieval.
6. Use TLA+ or another small-state model checker for the memory authority invariant before wiring it into production code.
7. Emit trace spans for memory write, derive, retrieve, elevate, deny, and action-authorize decisions.

## Implementation complexity

The thin version is straightforward:

1. Store memory records with origin and scope metadata.
2. Route recall through a policy function.
3. Block memories from authorizing actions outside their declared scope.
4. Test laundering fixtures with the MEM-INV-Bench scenarios.
5. Log every memory authority decision.

The hard version is end-to-end propagation. Real agent systems summarize, embed, rerank, cite, copy into handoff files, echo through tools, and share state across tenants or agents. If any one path drops the authority metadata, untrusted memory can reappear as trusted context.

That is why the implementability score is 0.66. The first guardrails are deployable now. The full guarantee requires memory storage, retrieval, summarization, propagation, and action execution to share one authority model.

## What remains conceptual or unproven

- The TMA-NM formal model is useful, but production runtimes have more side channels than a paper model can cover.
- The benchmark repo is public, but it still needs integration against the specific memory stack being protected.
- Sybil-resistant corroboration is easy to say and hard to operationalize when many sources are summaries of the same upstream event.
- Multi-tenant direct reads, exports, backups, and admin tools can bypass semantic retrieval policy unless they are explicitly governed.
- Human operator UX for memory authority remains underdeveloped. A system can have correct policy and still be unreadable to the person responsible for approving it.

## Strategic implications for Danny's product thinking

The product boundary should shift from “agent memory” to “memory authority control plane.”

A credible agent platform should not promise that it remembers everything. It should prove which memories are allowed to matter, for which tasks, under which authority, and with what revocation or elevation path.

This also changes the sales and governance story:

- For builders: memory becomes inspectable infrastructure, not hidden prompt stuffing.
- For enterprise buyers: memory risk can be reviewed as a manifest and trace, not as vague assurances.
- For local-first agents: origin and authority can stay inside the workspace, which makes the trust boundary clearer.
- For FriendVM-style agent nodes: each node can own its memory authority policy, while shared memory needs explicit propagation contracts.

The durable worldview update is this: memory is not a store. Memory is a policy-bearing runtime object.

## June 30 update: poisoning detectors should watch memory-to-effect transitions

Forensic Trajectory Signatures for Agent Memory Poisoning Detection moves this topic from authority modeling into runtime detection. The important object is the transition from recalled memory to effectful action. In the evaluated architecture, successful exfiltration attacks required a memory recall before an email send, and that transition was enough for a strong detector.

Practical lesson:
- add memory recall, direct memory read, memory-derived summary, and effectful sink events to one trace schema;
- define deny or review rules for recall-to-email, recall-to-export, recall-to-deploy, recall-to-payment, and recall-to-external-post paths;
- train classifiers only after simple invariants and labels exist;
- preserve enough provenance to distinguish memory-channel poisoning from ordinary prompt injection.

Source:
- [Forensic Trajectory Signatures for Agent Memory Poisoning Detection](https://arxiv.org/abs/2606.30566v1)

## July 3 update: governed context vaults are memory authority infrastructure

ContextNest adds the retrieval-facing version of memory authority. A knowledge object should not influence an agent only because it is semantically relevant. It should be eligible: approved for AI use, current, attributable, integrity-verified, and reconstructable at the point it was consumed.

Practical lesson:
- add approval state, source identity, version ID, and integrity hash to AI-consumable knowledge records;
- route semantic retrieval through a deterministic eligibility selector first;
- preserve point-in-time context sets so later audits can reconstruct what the agent saw;
- treat MCP source nodes as authority-bearing inputs, not neutral connectors;
- fail closed when a context artifact is stale, unapproved, or unverifiable.

Sources:
- [ContextNest](https://arxiv.org/abs/2607.02116v1)
- [PromptOwl/ContextNest](https://github.com/PromptOwl/ContextNest)

## July 5 update: valid memory still needs state and scope authority

MemSyco-Bench and A-TMA extend this topic beyond poisoning. A memory can come from a legitimate user and still be unsafe for the current action if it is stale, out of scope, contradicted by stronger evidence, or only valid as personalization. That means memory authority must include state and scope, not only origin.

Practical lesson:
- treat preference memory as scoped influence, not general factual authority;
- require current, historical, transition, superseded, and conflict labels for high-value memory records;
- block or downgrade memory influence when the task requires objective evidence;
- preserve supersession lineage through summaries, embeddings, handoffs, and direct reads;
- add authority checks before memory-derived context can affect external actions.

Sources:
- [MemSyco-Bench](https://arxiv.org/abs/2607.01071v2)
- [A-TMA](https://arxiv.org/abs/2607.01935v1)

## Implementation checklist

- [ ] Define a memory authority schema.
- [ ] Add authority metadata to every memory write.
- [ ] Require summaries and embeddings to carry `derived_from` and authority tier.
- [ ] Route search and direct reads through the same policy gate.
- [ ] Block action authorization from untrusted or out-of-scope memories.
- [ ] Add laundering regression fixtures.
- [ ] Add trace spans for authority propagation and denial.
- [ ] Diff memory-authority policy in CI when workflows change.

## Source notes

Primary source:
- Securing LLM-Agent Long-Term Memory Against Poisoning: https://arxiv.org/abs/2606.24322v1

Implementation artifacts:
- MEM-INV-Bench / TMA-NM repository: https://github.com/yedidel/mem-inv-bench
- MEM-INV-Bench dataset: https://huggingface.co/datasets/anonymos-2321135/MEM-INV-Bench

Supporting sources:
- Governed Shared Memory for Multi-Agent LLM Systems: https://arxiv.org/abs/2606.24535v1
- AgentRiskBOM: https://arxiv.org/abs/2606.21877v1
- Lingering Authority: https://arxiv.org/abs/2606.22504v1
- From Untrusted Input to Trusted Memory: https://arxiv.org/abs/2606.04329v1
- Poison Once, Exploit Forever: https://arxiv.org/abs/2604.02623v2

## July 18 update: memory admission must run again at use time

Bad Memory and MemPoison show why write-time trust is incomplete. A payload already present in a persistent workspace can affect future sessions, while individually plausible records can become harmful only when retrieved together or activated by a later trigger.

Practical lesson:
- preserve origin, injection channel, scope, derivation, and write-time verdict on every record;
- evaluate the retrieved set as one influence object;
- add multi-record and trigger-conditioned poisoning fixtures;
- block memory-only authorization for external writes, sends, installs, payments, and deployments;
- trace memory write, retrieved set, use-time policy, downstream action, and final receipt together.

Evidence caveat: Bad Memory uses a synthetic workspace and assumes the payload is already present. MemPoison evaluates 1,227 hand-validated cases across ten model families, but its claimed structured dataset had no resolvable public artifact URL in this scan.

Sources:
- [Bad Memory](https://arxiv.org/abs/2607.14611v1)
- [Bad Memory anonymized artifact](https://anonymous.4open.science/r/self-modifying-agent-security-3248/README.md)
- [MemPoison](https://arxiv.org/abs/2607.14651v1)

## August 3 update: consolidation must preserve non-amplifying authority

Memory Provenance Laundering isolates the failure that occurs when summarization preserves an action trigger but erases the low-trust source. PPMF makes platform-owned provenance and risk labels a precondition for exact tool effects rather than readable hints inside memory prose.

Practical lesson:
- keep provenance metadata outside model-authored summaries;
- propagate trust, derivation, confirmation, scope, risk, and expiry through every memory transformation;
- bind action-relevant memories to exact tool arguments;
- deny high-risk effects when the supporting authority is insufficient;
- require fresh trusted confirmation rather than allowing consolidation to manufacture it.

Artifact caveat: the paper reports sanitized scenarios and scripts as planned release material, but no public implementation URL was exposed on the primary pages. Its guarantee assumes the platform-maintained confirmation and risk labels remain intact.

Source:
- [Memory Provenance Laundering](https://arxiv.org/abs/2607.29167v1)


## August 6 update: commitment needs certificates over retained worlds

SafeCommit formalizes premature commitment under memory uncertainty. Before a side effect, the controller retains a calibrated set of plausible worlds from memory, observations, tool outputs, provenance, and policy. The action commits only when a conformal certificate says it is safe in every retained world; otherwise the system probes or falls back. In the authors' synthetic study, unsafe commitment falls from about 41.2 percent single-world action to about 2.6 percent with certification plus targeted probes.

Practical lesson:
- do not treat one retrieved memory context as the world;
- retain conflicting candidate worlds until probes resolve them;
- require action certificates before external side effects;
- prefer targeted low-side-effect probes over generic confirmation prompts;
- record retained worlds, probe results, and commit or fallback receipts.

Artifact caveat: the public repository is explicit that the included benchmark is a controlled synthetic mechanism study, not deployed LLM-agent performance.

Sources:
- [SafeCommit](https://arxiv.org/abs/2608.04289v1)
- [akewarmayur/SafeCommit](https://github.com/akewarmayur/SafeCommit)


## August 12 deep dive: memory needs two gates, not one smarter retriever

MAP-Graph is the strongest finding of the 2026-08-06 through 2026-08-12 window because it turns provenance from audit metadata into an online control signal. The system models principals, sources, memories, claims, and actions in one typed execution graph, then runs a sequence that ordinary vector memory omits:

1. Trace the ancestry of each candidate memory.
2. Exclude records whose inherited permission scope does not admit the requesting principal.
3. Rerank only eligible records using semantic similarity and multiplicative path trust.
4. Re-evaluate the selected evidence against the proposed action's risk.
5. Preserve affected descendants and the final decision as an audit receipt.

The key architecture is not the graph by itself. It is the separation of two policy questions:

- Retrieval gate: may this principal read or use this memory?
- Action gate: is this evidence sufficient to authorize this exact effect?

On 2,700 synthetic tasks per method across three domains, MAP-Graph reports 94.96 percent task success, 72.70 percent exact decision accuracy, and 90.22 percent clean-setting success. It rejected every observed unauthorized read and blocked all 450 revoked cases. The full study records 21,600 main-experiment decisions, 18,900 ablation decisions, and a three-backbone transfer subset.

The ablations are the important proof. Removing the permission filter increased task success from 94.96 to 96.00 percent and exact accuracy from 72.70 to 78.63 percent, but unauthorized access rose from zero to every observed attempt. Better aggregate utility hid a destroyed security boundary. Provenance therefore has to constrain the candidate set before ranking, not merely add another score after retrieval.

### Why this won the week

One Recipe, Many Harnesses gives self-evolving coding agents a strong transfer methodology. REDAgentBench improves realized-state safety measurement. Quadrat-IPI provides a ready-to-run detector evaluation map. All three are useful, but they optimize or evaluate one subsystem.

MAP-Graph defines the policy seam that every persistent multi-agent product eventually needs: one agent's retained state can become another agent's evidence, and evidence can become action. If that seam is wrong, better memory increases the reach of stale, private, poisoned, or revoked authority.

### Practical implementation now

Start with a thin control plane, not a full graph database migration:

- add stable identifiers for principal, source event, memory record, derived claim, proposed action, and policy decision;
- store `owner`, `visibility`, `permission_scope`, `derived_from`, `trust_label`, `revoked_at`, `valid_until`, and `allowed_effects` outside model-authored prose;
- propagate the most restrictive inherited scope through summaries and derived claims;
- filter ineligible memories before vector or lexical ranking;
- make `Allow`, `Block`, `Redact`, `Reverify`, and `AskUser` typed action-gate outcomes;
- retain receipts for candidate IDs, filtered IDs, selected evidence, proposed effect, effective policy, and final decision;
- test private ancestry, revoked ancestry, poisoned ancestry, stale evidence, clean allow, and high-risk action cases separately.

A relational prototype is enough. Use immutable IDs plus parent tables or recursive common-table expressions first. Add a specialized graph store only if measured lineage-query cost justifies it.

### Implementation complexity

The thin version is moderate: schema changes, one retrieval gateway, one policy evaluator, recursive ancestry resolution, and deterministic fixtures. The hard part is complete mediation. Direct reads, exports, summaries, embeddings, handoffs, background jobs, and admin tools all need to preserve and enforce the same authority fields.

Implementability score: 0.74. The architecture can be prototyped now, but the paper exposes no exact public implementation repository, and production correctness depends on closing every bypass path.

### What remains conceptual or unproven

- The benchmark is synthetic and templated; actions are simulated.
- Most reported cells are one run, not deployment-scale reliability evidence.
- The model still made 41 impermissible Allow decisions in the 450 high-risk action cases.
- Trust labels, permissions, and action-risk fields are supplied by the benchmark. Real systems still need an authority for issuing and revising those labels.
- No exact public implementation artifact was resolved from the immutable v1 paper.

These are not reasons to dismiss the design. They identify the guardrail: provenance eligibility is deterministic policy, while high-risk action authorization needs its own stricter engine and cannot be delegated to retrieval confidence.

### Strategic implication for Danny's product thinking

The product promise should not be “shared memory that remembers more.” It should be “shared state whose authority can be explained, revoked, and bounded before it changes the world.”

For FriendVM-style personal agents, a memory written by one node should not silently become another node's capability. For client workflows, a summary should not shed the permissions or expiry of its sources. For human approval, the useful screen is not a paragraph of recalled context; it is the receipt showing which principal, source lineage, policy, and effect are being joined.

The durable worldview update is: persistent context may propose evidence, but only a separate policy boundary can admit that evidence and authorize the effect.

### Core and supporting sources

- [MAP-Graph abstract, immutable v1](https://arxiv.org/abs/2608.10509v1)
- [MAP-Graph full paper, immutable v1](https://arxiv.org/pdf/2608.10509v1)
- [Governed Shared Memory for Multi-Agent LLM Systems](https://arxiv.org/abs/2606.24535v1)
- [Memory Provenance Laundering](https://arxiv.org/abs/2607.29167v1)
- [SafeCommit](https://arxiv.org/abs/2608.04289v1)

## August 19 update: authorize memory before context assembly

Authorization Before Context isolates the memory-to-context transition. Each item carries the audience present at recording. The current viewer set comes from channel metadata and falls back to public when ambiguous. Admission requires every current viewer to already belong to that audience.

The paper proves one-way confidentiality and per-participant recall from that single anti-monotone rule. In the evaluated configuration, no known forbidden fact entered unauthorized context, and audited read paths failed closed. Action safety and audience widening remain out of scope.

Practical lesson:
- stamp recorded audience at write time;
- resolve viewers from channel metadata, not from the query;
- exclude unauthorized items before prompt assembly;
- keep an exact-context receipt of admitted and excluded IDs.

Source:
- [Authorization Before Context](https://arxiv.org/abs/2608.17148v1)

## September 4, 2026 update: plans need parent IDs, not replica freshness

PlanFence names stale-plan execution. An executor can hold r4 and still run a plan derived from r3. In 30 live workflows with a post-plan revision, freshness-only execution issued the obsolete action every time (0/30). PlanFence completed all 30 without an invalid action.

Practical lesson:

- stamp plans with exact parent record IDs
- validate only action-relevant parents at the effect gate
- replan once or block; do not splice a new fact into an old plan
- keep a freshness-only negative fixture

No public PlanFence repository resolved.

Implementability score: 0.58

Source:

- [Fresh Memory, Stale Plans](https://arxiv.org/abs/2609.03340v1)
