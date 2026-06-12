# Strategy Daily Analysis: 2026-06-12

Today's strategy signal is stateful mediation. Persistent agents do not create risk one output at a time. They accumulate releases, memories, graph structure, tool calls, cloud sessions, and delegated authority over trajectories.

## Privacy is a trajectory budget, not an output filter

OCELOT is the strongest Strategy finding today because it treats agent privacy as cumulative posterior-risk control. The paper argues that LLM-agent privacy is not a property of one answer. It is a property of an entire trajectory in which the agent reads personal files, calls tools, receives untrusted observations, and releases information to multiple sinks.

The paper names three hard properties. Leakage is cumulative: individually harmless releases can combine into a protected inference. Leakage is bidirectional: a malicious observation can inject instructions that cause later releases. Leakage is task-dependent: the same field can be necessary for one recipient and gratuitous for another.

Why it matters: per-output redaction is structurally too small. A travel agent, finance agent, coding agent, or personal operator can leak private state without ever printing a single obvious secret. The strategic boundary is the cumulative state of what each external sink can infer after the sequence.

How it fits into the stack: this is runtime governance and local-first agent strategy. OCELOT proposes a runtime mediator with Witness-Verified Declassification and leakage budgets. A deterministic verifier audits declassification operators and charges certified min-entropy cost. The practical lesson is to make disclosure a budgeted transition in the run trace, not a model-only judgment.

Practical tools, repos, and methodologies worth exploring now:
- per-sink release ledgers that track what each external service has learned;
- semantic variants for release, redact, coarsen, defer, ask, or keep local;
- deterministic privacy-budget checks before external sends, tool calls, memory writes, and report publication;
- Merkle-chained or append-only evidence records for disclosure decisions;
- adversarial fixtures for cumulative inference, sink collusion, and injected observations.

Implementability score: 0.57

Core source:
- [OCELOT: Inference-Leakage Budgets for Privacy-Preserving LLM Agents](https://arxiv.org/abs/2606.12341v1)

## Graph memory selection is a write-path security boundary

Selection Integrity for LLM Graph Memory is the sharper memory-governance warning today. The paper argues that provenance checks over retrieved records miss a different attack surface: graph structure can influence which authenticated facts are selected before any cited record enters the prompt.

The bad case is subtle. An untrusted principal writes structure into graph memory: edges, entity merges, rankings, or tool-imported relations. Later, the selector uses that structure to choose authenticated facts. The final citations can all be legitimate while the selection path was steered by untrusted structure. Provenance of final records is necessary, but it is not selection integrity.

Why it matters: agent memory is moving toward graphs because flat vector recall cannot handle relationships and evolving state. But graph selection makes memory writes consequential even when the written item is never cited. That turns the memory write path into a policy surface.

Practical tools, repos, and methodologies worth exploring now:
- label graph edges, merges, and selection features by writer principal and trust tier;
- log graph-selection paths, not only final retrieved facts;
- prevent untrusted structure from steering high-authority decisions such as tool authorization, policy creation, credential use, or memory promotion;
- add tests where poisoned edges change retrieval without appearing in final citations;
- separate advisory retrieval from trusted-fact override, policy creation, and external-send decisions.

Implementability score: 0.61

Core source:
- [Selection Integrity for LLM Graph Memory](https://arxiv.org/abs/2606.12290v1)

## Persistent cloud agents make stateful governance unavoidable

OpenAI's announcement that it will acquire Ona is not a research result, but it is a strong market signal. The post frames the target as secure, customer-controlled cloud infrastructure for long-running Codex agents across software and knowledge work. It says the valuable work is increasingly unfolding over hours or days rather than minutes, with users checking progress, providing direction, making decisions, and reviewing results from anywhere.

Why it matters: once agents leave the local terminal and continue in persistent cloud environments, runtime state becomes the product boundary. Identity, filesystem scope, network policy, memory, progress checkpoints, approvals, audit evidence, and customer-controlled execution all become strategic differentiators.

How it fits into the stack: this reinforces the local-first and runtime-governance thesis. A persistent cloud workspace can be useful, but only if it exposes the same evidence and control surfaces a serious operator needs locally: scoped credentials, tenant boundary, workspace lineage, checkpoint policy, tool-call audit, and exportable traces.

Practical tools, repos, and methodologies worth exploring now:
- persistent workspaces with explicit owner, tenant, project, model, policy, and checkpoint metadata;
- cloud/local parity tests for filesystem, network, credential, and approval behavior;
- customer-controlled logs and artifact export instead of vendor-only observability;
- long-running task budgets with pause, resume, revoke, and handoff semantics;
- threat models where a stale cloud agent continues after user intent or authorization changed.

Implementability score: 0.66

Core source:
- [OpenAI to acquire Ona](https://openai.com/index/openai-to-acquire-ona)

## Strategic readout

The strategic pattern is now consistent: the winning agent platform is the one that mediates state transitions, not only messages. Disclosure, graph-memory writes, persistent cloud sessions, recursive delegation, and compiled user corrections all need the same product shape: bounded authority, traceable state, deterministic checks where possible, and evidence that survives the run.
