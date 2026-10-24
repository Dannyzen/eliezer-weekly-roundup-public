# Strategy Weekly Sovereignty - 2026-10-23

## Weekly thesis: evidence can inform authority, never silently become it

The week's strategic signal is a single control-plane rule: information that persists, compresses, retrieves, or crosses a tool boundary remains evidence. Authority must be granted by a current policy decision tied to an exact principal, capability, destination, and effect.

This rule connects context compaction, long-term memory, dynamic tool catalogs, sandboxing, egress, and incident diagnosis. Each fails when one layer assumes another layer already enforced authority.

## 1. Reauthorize persistent state when it resurfaces

CarryoverBench separates attack planting from later triggering across memory and scheduled execution. Payloads showed no monotonic decay over five rounds. Hermes reduced attack success relative to another runtime but remained vulnerable, with reported Latent attack success from 2.8% to 27.8% across tested models.

Why it matters: a stored instruction is delayed execution authority if the runtime later acts on it without a fresh gate. Time and session boundaries do not revoke it by themselves.

Fit in strategy: persistent writes need policy-bearing metadata, and every resurfacing into planning or execution needs current authorization.

Implementable now:
- attach origin, principal, purpose, trust, expiry, and revocation to persistent writes;
- quarantine instructions derived from webpages, email, documents, tool results, and peer agents;
- separate facts and preferences from procedures, schedules, and grants;
- reauthorize wake-ups and memory-derived effects against current policy;
- grade planting and triggering in separate sessions with real effect receipts.

Implementability score: 0.78

Core sources:
- [CarryoverBench v1](https://arxiv.org/abs/2610.28425v1)
- [CarryoverBench repository](https://github.com/igloomatics/CarryoverBench)
- [Persistent-State Agent Control](../persistent-state-agent-control/persistent-state-agent-control.md)

## 2. Enforce capability below declared tool intent

My Credentials, Please scanned 21,097 MCP servers and found 787 filesystem-capability signals among 4,806 triaged non-filesystem servers. Dynamic validation confirmed 150 vulnerable instances under tested policies. The declared tool schema described intent, while the process retained ambient host authority.

Why it matters: tool names, descriptions, approvals, and schemas cannot constrain filesystem or credential access that the operating system already grants.

Fit in strategy: catalog discovery belongs behind a gateway, while filesystem, credential, network, and process capabilities belong in sandbox and host enforcement planes.

Implementable now:
- run local tool servers under exact filesystem roots and dedicated identities;
- deny ambient credential and home-directory access;
- canonicalize paths and test symlink and traversal bypasses;
- fail startup when required containment cannot be installed;
- bind dynamic tool search to an eligible catalog before ranking.

Implementability score: 0.86

Core sources:
- [My Credentials, Please v1](https://arxiv.org/abs/2610.22301v1)
- [Arcade dynamic tool discovery v1](https://arxiv.org/abs/2610.23707v1)

## 3. Make effects and diagnoses replayable

AgentTriage normalizes five heterogeneous runtimes into one canonical event contract. It captured all 159 applicable executions and achieved 0.858 grounded joint diagnosis on 120 adjudicated cases, with 0.966 required-evidence coverage. ThinkingBox Training reaches the same control point from evaluation: executable checks over database state and side effects provide stronger reward signals than persuasive completion text.

Why it matters: security and quality claims need the same thing, a trace that identifies the invoked capability, observed result, terminal effect, and policy decision.

Fit in strategy: a canonical event model should sit between runtime telemetry and audit, incident response, evaluation, or training. Native and synthesized identities must remain distinguishable.

Implementable now:
- define canonical source-ingress, tool-intent, tool-result, and terminal-effect events;
- join invocation and result lifecycles deterministically;
- bind claims to event IDs and abstain when mandatory evidence is absent;
- version runtime overlays and policy oracles with the trace;
- reuse deterministic world-state checks for evaluation and release gates.

Implementability score: 0.84

Core sources:
- [AgentTriage v1](https://arxiv.org/abs/2610.30738v1)
- [AgentTriage repository](https://github.com/AsnGs/agenttriage-open-source)
- [ThinkingBox Training article](https://huggingface.co/blog/microsoft/thinkingbox-training)

## 4. Bind approval to the exact effect path

SPACE exposes templates, lifecycle operations, process sessions, and egress policies outside Firecracker guests. Connection Escrow goes narrower by parking an outbound TCP connection before packets leave and releasing it only under a signed, unexpired, single-use verdict bound to that socket and destination.

Why it matters: an approval that authorizes a narrative intent can be replayed, redirected, or applied to a different resource. Effect-bound authorization removes this ambiguity.

Fit in strategy: approval belongs at the narrowest enforceable layer that still sees the exact effect. Guest policy remains useful, while host-held enforcement is the durable boundary.

Implementable now:
- bind sandbox creates to exact template digests, principals, and egress profiles;
- keep lifecycle and recovery receipts outside the guest;
- bind network approval to destination, socket, expiry, and one use;
- test fail-closed recovery after controller restart;
- isolate kernel and Firecracker experiments from production workloads.

Evidence caveat: both patterns require meaningful Linux, privilege, recovery, and operational engineering.

Implementability score: 0.58

Core sources:
- [SPACE announcement](https://www.perplexity.ai/hub/blog/open-sourcing-space)
- [SPACE repository](https://github.com/perplexityai/SPACE)
- [Connection Escrow v1](https://arxiv.org/abs/2610.26501v1)
- [Connection Escrow repository](https://github.com/45h0kg/benign-attach-gateway)

## Strategic decision

> Treat every persisted or transformed input as evidence with lineage. Grant authority only through a current, effect-bound runtime decision. You gain replayability and containment, while giving up some convenience and low-latency autonomy.

The weakest point is operational weight. Typed provenance, policy metadata, canonical events, sandbox identities, and effect receipts increase storage and integration cost. The guardrail is incremental adoption: begin at the highest-risk transitions, compaction, persistent writes, privileged tools, and external effects, then widen only when failure evidence justifies it.
