# Strategy Weekly Sovereignty Analysis - 2026-09-11

## Thesis

Sovereignty means the proposer cannot also define the evidence, authority, and final state of its own action. Authority must be attenuated per principal, carried across delegation, checked against independent world evidence, and monitored at the fleet layer.

## Attenuate authority per principal and exact effect

### Finding

CapScope fixes a task-wide authority ceiling from trusted input, then gives each sub-agent only the typed capabilities its role needs. Injected effects fell from 33 of 75 under the strongest global baseline to 3 of 75, while 68 of 75 repairs still completed. CONTINUITY makes each security-relevant transformation carry an authenticated witness to the exact effect. Its deterministic suite covered 128 modeled fault-domain classes and 2,560 attack instances without a harmful effect under the complete construction.

### Why it matters

A task may need broad authority in aggregate without any one planner, reader, runner, or patcher needing all of it. Ambient task authority turns any compromised context into an execution path.

### Strategy fit

This is context-to-execution integrity and the agent execution control plane. The control object is a typed, per-principal capability bound to one effect and one transition.

### Practical path now

- Derive a task ceiling from trusted input before untrusted context is read.
- Issue role-specific capabilities for read, execute, patch, publish, and approve.
- Require an authenticated witness at each security-relevant transform.
- Bind the final witness to the exact arguments and destination of the effect.
- Inject missing-context and stale-capability faults between components.

Implementability score: 0.79

Core sources:
- [Authority Is Not a String](https://arxiv.org/abs/2609.08371v1)
- [CONTINUITY](https://arxiv.org/abs/2609.05269v1)
- [CONTINUITY repository](https://github.com/zast-ai/continuity)

## Delegation needs end-principal identity and context ownership

### Finding

A2ABreak reports 11 vulnerabilities in the A2A protocol that remain exploitable by a specification-compliant adversary. The failures include cross-client context injection, loss of identity across multi-hop delegation, and unattested capability claims. Its formal framework reached 73.3% precision and 84.6% F1 against expert review, and the public repository exposes a populated benchmark and analysis surface.

### Why it matters

Protocol compliance proves message shape, not delegation safety. A valid hop can still erase who initiated the task, who owns the context, and which capabilities were actually attested.

### Strategy fit

This belongs in agent gateway governance and shared-state agents. The gateway must carry tenant, end principal, delegation lineage, audience, and capability evidence as first-class fields.

### Practical path now

- Bind context IDs to tenant and owner, not only conversation ID.
- Preserve the end principal across every hop.
- Attach a signed delegation chain and audience-bound credential to each request.
- Require capability attestation rather than trusting an Agent Card claim.
- Test lifecycle edges such as cancellation, reconnect, replay, and cross-client reuse.

Implementability score: 0.73

Core sources:
- [A2ABreak](https://arxiv.org/abs/2609.10871v1)
- [A2ABreak repository](https://github.com/arlotfi79/A2ABreak)
- [A2A specification](https://a2a-protocol.org/latest/specification/)

## Evidence lineage beats model diversity

### Finding

VP-CONTROL evaluates verification portfolios under common-mode data faults. Cross-model voting over shared evidence approved 62.9% of unsafe proposals. Adding an independent evidence source reduced unsafe approval to 22.9%. Evidence-source diversity moved outcomes by 40.9 points, compared with 11.3 points for model diversity.

### Why it matters

A committee of different models can agree confidently on the same poisoned or stale source. Independence is a property of lineage, not vendor count.

### Strategy fit

This is the evidence provenance control plane and stateful effect governance. Verifier selection must account for what evidence each verifier can see and who can mutate it.

### Practical path now

- Assign lineage IDs to source observations and derived claims.
- Reject an independence claim when actor and verifier share the same upstream evidence.
- Add transactional preconditions at commit time.
- Calibrate portfolios by unsafe approval, false hold, cost, and latency.
- Preserve defer as a valid result when independent evidence is unavailable.

Implementability score: 0.74

Core sources:
- [VP-CONTROL](https://arxiv.org/abs/2609.10969v1)
- [VP-CONTROL artifact](https://doi.org/10.6084/m9.figshare.33511441.v1)

## Monitor persistent principals above tool dispatch

### Finding

MOLE tracks 150 persistent AI-operated accounts across nine stateful services and 30 workdays. It verifies completed harm in service state, then measures detection under a realistic review budget of the top one through ten accounts per day. Its selected cascade combines cheap behavioral features with expensive semantic review and reached 0.629 budget-AUC at 2.43 times the modeled cost of uniform GPT-4.1, versus 0.571 for uniform GPT-5.5 at 2.5 times cost.

### Why it matters

Per-call policy cannot see slow misuse, cross-service coordination, or persistent identity. An organization needs a monitor that correlates actions over accounts, services, and days without sending every event to an expensive model.

### Strategy fit

This belongs above gateway and execution control as an agent-fleet monitoring plane. It is detection and triage, not autonomous punishment.

### Practical path now

- Give every agent a stable principal ID across services.
- Compute action rarity, peer deviation, and sequence features cheaply for every principal-day.
- Route only suspicious windows to semantic review.
- Ground alerts in verified resulting state, not intent classification alone.
- Evaluate against the actual analyst review budget and keep human disposition authority.

Implementability score: 0.74

The benchmark is public and populated, but its organization, harmful objectives, and collusions are synthetic. Use it for offline replay and monitor design, not production prevalence claims.

Core sources:
- [MOLE](https://arxiv.org/abs/2609.06966v1)
- [MOLE repository](https://github.com/aashiqmuhamed/mole)
- [MOLE dataset](https://huggingface.co/datasets/forgelab/mole)

## Working conclusion

The control plane should own four things the model cannot self-certify: capability scope, delegation lineage, evidence independence, and persistent principal history. Without those objects, approvals and multi-agent roles are presentation layers over ambient authority.
