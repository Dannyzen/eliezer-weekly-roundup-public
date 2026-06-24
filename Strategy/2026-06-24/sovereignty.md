# Daily Strategy Research Notes - 2026-06-24

## Thesis

Memory has become an authority surface. If stored memories can steer future actions, then memory systems need origin-bound authority, scoped retrieval, temporal supersession, provenance, and policy-governed propagation before the agent sees the memory as context.

## Deep Dive Wednesday: Memory authority control plane

Today's durable finding is that long-term memory has crossed from convenience feature into an authority plane. If a recalled memory can influence a future tool call, file write, credential use, customer action, or delegation decision, then it needs the same kind of scoped authority as any other capability.

The winning source is `Securing LLM-Agent Long-Term Memory Against Poisoning`. It beats the other strong findings this week because it explains how authority survives across time. Handoff logs and GUI/CLI skill coverage improve execution. Origin-bound memory authority changes the trust model underneath future recall.

The practical control plane is clear:

- bind authority at memory write time to origin principal, source event, scope, and allowed effects;
- preserve authority through summaries, embeddings, handoff files, and tool echoes;
- require independent trusted corroboration before untrusted memory can be elevated;
- enforce the same policy on semantic search, direct reads, propagation jobs, and action authorization;
- test laundering fixtures before trusted memory reaches tools.

Deep dive: [Memory Authority Control Plane](../memory-authority-control-plane/memory-authority-control-plane.md)
Implementation artifact: [MEM-INV-Bench / TMA-NM](https://github.com/yedidel/mem-inv-bench)
Implementability score: 0.66

## Top findings

### Origin-bound memory authority closes laundering attacks

Securing LLM-Agent Long-Term Memory Against Poisoning argues that content-based and lineage-based memory defenses are malleable in agent systems. The attack class is memory laundering: adversarial content enters memory through one session, then later appears trustworthy after summarization, trusted-tool echo, or manufactured corroboration.

The paper's useful contribution is not only another memory-poisoning warning. It frames memory authority as a write-time property. A stored memory should not gain authority because its text looks benign or because an LLM summary dropped the untrusted edge. It should carry non-malleable origin-bound authority, and elevation should require corroboration that resists Sybil-style self-confirmation.

The PDF text verifies the sharp result: existing defenses fail where the theory predicts, with up to 68% laundering attack success, while TMA-NM reaches 0% attack success on direct and laundering attacks across the tested models.

Why it matters:

- future behavior can be compromised by old memory, not only by the current prompt;
- provenance has to survive summarization, embedding, retrieval, and tool echoes;
- memory writes need authority metadata before they become retrievable action context;
- trusted memory should be elevated by policy, not by a model's impression of trustworthiness.

Stack fit:

- Agent authority manifests
- Runtime governance
- Memory systems
- Evidence provenance control plane

Practical tools and methods worth exploring now:

- add `origin_principal`, `source_event_id`, `authority_tier`, `scope`, and `elevation_rule` to durable memory records;
- keep raw event provenance even when a memory is summarized or embedded;
- block memory items from authorizing actions outside their declared scope;
- require independent corroboration before promoting untrusted memories into trusted operational guidance;
- add memory-laundering fixtures where summaries, tool echoes, and repeated mentions try to upgrade authority.

Implementability score: 0.66

The policy fields and fixtures are implementable now. The full formal guarantee needs more than metadata: it requires a memory write path, retrieval path, and action path that all preserve and enforce origin authority.

Core source: https://arxiv.org/abs/2606.24322

### Governed shared memory makes fleet memory a policy service

Governed Shared Memory for Multi-Agent LLM Systems formalizes the fleet-memory problem for systems where multiple agents share durable state. The paper identifies four failure modes that matter in production: unauthorized leakage, stale propagation, contradiction persistence, and provenance collapse.

The proposed primitive set is the right systems layer:

- scoped retrieval;
- temporal supersession;
- provenance tracking;
- policy-governed memory propagation.

The authors instantiate these ideas in MemClaw, a production multi-tenant memory service, and evaluate it with ArgusFleet, a reproducible harness against a live REST API. The most valuable part is the negative evidence. Live evaluation surfaced a sub-tenant scope bypass on direct `GET-by-id` requests and a pipeline-ordering conflict where near-duplicate rejection can block contradiction supersession.

Why it matters:

- shared memory is a policy service, not a bigger vector index;
- direct object reads need the same scope checks as search retrieval;
- contradiction handling depends on pipeline order, not only on having a contradiction detector;
- production memory systems should be evaluated against live API paths, not only design diagrams.

Stack fit:

- Shared-state agents
- Agent gateway governance
- Runtime governance
- Memory systems

Practical tools and methods worth exploring now:

- enforce scoped retrieval and direct-read policy through the same gateway;
- attach writer identity and source event IDs to every derived memory;
- implement supersession semantics before near-duplicate suppression blocks useful contradictions;
- build an ArgusFleet-style harness that probes search, direct reads, propagation, contradiction, and provenance reconstruction;
- report governance failures as first-class memory test failures, not as application bugs.

Implementability score: 0.72

The core primitives are implementable with normal platform engineering. The difficulty is enforcing them consistently across search, direct reads, propagation jobs, summaries, and downstream prompts.

Core source: https://arxiv.org/abs/2606.24535

## Watchlist

Are We Ready For An Agent-Native Memory System? is worth a follow-up because it evaluates 12 memory systems across representation, extraction, retrieval/routing, and maintenance, and it points to a public MemoryData artifact. It supports today's thesis but is broader than the two sharper governance findings.

Watchlist source: https://arxiv.org/abs/2606.24775
