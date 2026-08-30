# Strategy Daily Analysis - 2026-08-30

## Scope note

There was no new weekend arXiv listing, so the research lane used the newest complete Friday, August 28 listing and excluded papers already covered by the repository. The two selected strategy papers were submitted on August 27. They are included as the newest complete primary-source batch, not represented as Sunday submissions.

No external code was cloned, installed, built, imported, or executed. Neither selected paper exposed a public implementation repository in its arXiv page. NotebookLM remained disabled.

## Separate persona drift from audited execution

### Finding

[Persona-Execution Separation](https://arxiv.org/abs/2608.27427v1) argues that an agent's mutable persona and its stateful work should occupy different trust domains. The persona may evolve in tone, instructions, and presentation. Execution remains faceless, audited, and tied to one stable operational identity. A governed contract bridge allows status summaries to return while keeping data bodies in the restrictive domain unless a graded DLP exception is approved.

The paper derives the pattern from three goals: free persona drift, strict execution traceability, and decoupling between them. It reports one development or pilot case with mechanism, trace-isolation, structural, and five-model perturbation checks.

### Why it matters

Many agent systems bind identity, memory, tools, credentials, tone, and work state into one object. That makes harmless persona edits operationally dangerous and makes execution policy expensive to reason about. Separation turns persona into a presentation and planning surface while keeping work authority in a smaller, stable domain.

The bridge is the cost. It needs typed change objects, explicit data classes, an approval matrix, DLP, and audit. Without those controls, two domains merely create a larger attack surface.

### Strategy fit

This belongs in context-to-execution integrity and organizational agent governance:

- persona instructions are mutable context, not authority;
- execution identity, credentials, work state, and audit remain stable;
- cross-domain requests become typed contract objects;
- summaries and data bodies have different egress rules;
- persona changes cannot silently revalidate or rewrite execution policy.

### Practical path now

- Separate persona configuration from execution configuration and credentials.
- Give execution a stable service identity independent of display name or tone.
- Define bridge request types for work submission, status return, and data egress.
- Default status to summary-only and require DLP plus approval for data bodies.
- Record persona version, bridge request, execution identity, decision, and receipt in one trace.

The evidence is a single case and architecture argument. The paper itself says applicability outside the reference case is not validated, and no public implementation artifact was surfaced for independent inspection.

Implementability score: 0.61

Core source: [paper](https://arxiv.org/abs/2608.27427v1)

## Secure persistent state with plan-first information-flow control

### Finding

[SPA](https://arxiv.org/abs/2608.27234v1) combines one-shot declarative planning with confidentiality and integrity labels that survive tool execution and cross-query storage. The planner commits to a complete executable plan before seeing untrusted tool output. Execution results become labeled artifacts. Later planners receive semantic metadata, while concrete values are retrieved only during execution with their original labels.

On AgentDojo and the paper's multi-query AgentDojo-MQ extension, information-flow control reduced `tool_knowledge` attack success to 0 percent and 0.2 percent. Persistent reuse remained high but not free: producer artifacts were reused in 95.4 percent of opportunities without IFC and 89.9 percent with IFC.

### Why it matters

Persistent agents face a delayed-control problem. Poisoned data can be stored during one query, then drive a sensitive action days later. Per-call tool policy does not preserve enough history. SPA makes control dependencies explicit and carries source labels across the state boundary.

The strongest design move is semantic planning over labels, not raw payload replay. The planner can know that an invoice exists and what capability is needed without reading attacker-controlled instructions embedded in the invoice body.

### Strategy fit

This belongs in persistent-state control and the execution-control plane:

1. compile the trusted request into a complete plan;
2. bind planned capabilities to installed tools;
3. execute untrusted outputs outside the planner;
4. label confidentiality, integrity, and control dependencies;
5. persist artifacts with those labels;
6. expose metadata to future planning and values only to constrained execution;
7. reject low-integrity data driving high-integrity effects.

### Practical path now

- Store provenance and integrity labels beside every persistent artifact.
- Split semantic metadata from concrete values in the memory interface.
- Bind future tool arguments to the originating artifact labels.
- Add multi-query delayed-attack fixtures, not only single-turn prompt-injection tests.
- Measure both attack success and legitimate reuse because strict integrity enforcement can block useful workflows.

The reported security rates are benchmark-specific and paper-authored. Strict integrity creates a real utility cost, and no public SPA implementation repository was surfaced for independent inspection.

Implementability score: 0.68

Core source: [paper](https://arxiv.org/abs/2608.27234v1)
