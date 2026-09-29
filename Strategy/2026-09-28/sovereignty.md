# Strategy Daily Analysis - 2026-09-28

Today's strategy signal is one control rule applied at two boundaries: credentials and repeated claims are inputs to admission decisions, not authority by themselves.

## Make shared-memory admission a provenance decision

The Correlated Promotion Benchmark shows why majority-like memory writes are unsafe. An agent can retrieve one belief, paraphrase it, and create apparent agreement without adding an independent source. In CPB-Live, uncontested false beliefs were repeated in 0.97 to 0.99 of probes. A declared-source-type gate reduced false adoption to 0.06 to 0.09.

### Why it matters

A shared memory write can shape every later agent. Counting repetitions as corroboration turns one bad source into fleet-wide standing context.

### How it fits

This is the admission layer of the memory authority control plane. Source identity, lineage, contest state, and supersession need to be runtime-owned fields.

### Practical tools and methodologies

- Require source class and provenance root before a claim enters shared memory.
- Collapse copied and paraphrased claims before counting support.
- Separate writer permission from claim-admission policy.
- Preserve contest, demote, supersede, and tombstone operations.
- Re-evaluate admitted claims when their cited sources change.

Evidence caveat: CPB-Live is authored fiction and does not test correction operations. The public MIT artifact withholds transcripts and run summaries until acceptance.

Implementability score: 0.88

Core source: [A Benchmark and Diagnostic Study of Epistemic Admission in Shared Agent Memory](https://arxiv.org/abs/2609.30813v1)

Supporting source: [lxy1134/iclr_2027](https://github.com/lxy1134/iclr_2027)

## Admit MCP credentials independently from tool authority

Two releases on 28 September expose both sides of the same boundary. Codex CLI 0.158.0 adds pre-registered MCP OAuth client secrets, bearer authentication for direct exec-server WebSockets, and default approval prompts for elevated terminal input. LiteLLM 1.103.0 requires admission for delegated MCP OAuth and preserves request-selected guardrails during tool execution, although two end-to-end OAuth tests were reverted in the same release.

### Why it matters

A valid OAuth client secret proves a client identity. It does not decide which principal may delegate, which server revision is admitted, or which tools and arguments may execute. Connection authentication and runtime authorization must remain separate.

### How it fits

This belongs in agent gateway governance and context-to-execution integrity. The gateway should bind credential, principal, admitted server, tool schema, guardrails, and invocation receipt before execution.

### Practical tools and methodologies

- Store MCP OAuth client secrets in a secret manager and rotate them independently from server policy.
- Require admission for delegated OAuth before persisting or forwarding credentials.
- Bind bearer tokens to the exact exec-server audience and short expiry.
- Re-test guardrail preservation through tool execution and fallback routes.
- Treat the reverted scoped-execution and cold-restart tests as a release caveat, not as proof of failure.
- Canary both releases before live promotion because each changes authentication or policy behavior.

Release caveat: both projects ship broad releases. Codex adds credential support at the client, while LiteLLM changes gateway policy and contains reverted OAuth isolation tests. Upgrade only with provider-specific regression coverage.

Implementability score: 0.91

Core sources:

- [OpenAI Codex CLI 0.158.0](https://github.com/openai/codex/releases/tag/rust-v0.158.0)
- [LiteLLM 1.103.0](https://github.com/BerriAI/litellm/releases/tag/v1.103.0)
