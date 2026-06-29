# Strategy Daily Sovereignty, 2026-06-29

## Bottom line

Today's governance signal is that privacy and prompt-injection safety have to be enforced at the information-flow boundary. Final-output review is too late, and better prompts cannot create a hard control-data separation inside a shared model context.

The practical correction is to govern tool arguments, memory writes, policy routing, and provenance before effects occur.

## Purpose-bound privacy makes tool arguments part of the security boundary

Core source: https://arxiv.org/abs/2606.28061v1

Category: Strategy

Implementability score: 0.78

### What changed

ToolPrivacyBench audits whether task-private atoms are routed only to authorized tools and downstream sinks during multi-tool workflows. The benchmark contains 2,150 cases: 1,150 synthetic privacy-sensitive business workflows and 1,000 cases adapted from existing multi-tool and function-calling benchmarks.

The important correction is simple: task completion does not prove appropriate disclosure. An agent can finish the job while leaking unnecessary private fields through intermediate tool calls.

### Why it matters

This moves privacy from final answer review into trajectory-level auditing. The security boundary includes tool arguments, backend audit logs, and downstream sinks. A gateway that only checks whether the final message exposed private data is blind to the most important leakage path.

This fits the strategy layer as purpose-bound information flow. Each private atom needs a purpose, an authorized recipient set, and an audit rule.

### Practical tools and methods worth exploring

- policy knowledge bases that map private fields to allowed tools and sinks
- mock business backends that record tool arguments and audit logs
- OpenTelemetry spans for field-level disclosure events
- OPA, Cedar, or custom ABAC policy checks before tool invocation
- privacy regression suites that score task success and over-disclosure separately

### Implementation path

1. Label sensitive fields as task-private atoms.
2. Define which tool and sink may receive each field for each workflow purpose.
3. Record every tool argument and backend write with field IDs.
4. Fail tests when the agent sends a private atom to an unauthorized tool or sink.
5. Report task success and privacy over-disclosure as separate metrics.

This is implementable now for narrow internal workflows. It gets harder across arbitrary external tools, but the first useful version is a policy table plus argument audit logs.

## Prompt injection is a control-data separation problem, not a better-prompt problem

Core source: https://arxiv.org/abs/2606.27567v1

Category: Strategy

Implementability score: 0.44

### What changed

On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models argues that perfect prompt-injection prevention is mathematically impossible in shared-embedding architectures that lack enforced control-data separation. The paper formalizes control-authoritative actions such as tool authorization, policy routing, refusal decisions, and memory writes, then argues those actions cannot be perfectly protected if trusted instructions and untrusted data flow through the same representational pipeline without immutable provenance enforcement.

The practical takeaway is not despair. It is architectural humility: the model can help classify risk, but it cannot be the only enforcement boundary for authority-bearing actions.

### Why it matters

This strengthens the current repo thesis. Prompt-injection defense should be built like systems security: provenance labels, capability handles, reference monitors, taint tracking, data-plane isolation, and deterministic policy checks. Natural-language instructions remain useful, but they are not a hard boundary.

### Practical tools and methods worth exploring

- immutable provenance labels on retrieved content, user input, tool output, and memory
- separate policy routers that receive typed facts, not raw mixed prompts
- reference monitors for tool calls and memory writes
- capability handles that encode scope, purpose, and expiry
- taint tests that prove untrusted content cannot authorize privileged actions

### Implementation path

1. Mark retrieved content and tool outputs as untrusted data by default.
2. Prevent untrusted data from directly producing tool grants, memory writes, or policy changes.
3. Route authority-bearing actions through a deterministic policy layer outside the model.
4. Preserve provenance and taint labels in traces.
5. Test prompt-injection attempts as control-plane bypass attempts, not only as text attacks.

The theorem is conceptual, so the score is low. The engineering response is still clear and already partly available.

## Watchlist

Agent-Native Immune System is a useful taxonomy signal, but it is not a drop-in architecture yet. Its strongest contribution is the warning that memory poisoning, tool-chain manipulation, and multi-agent protocol attacks happen inside the agent loop, so purely perimeter defenses are incomplete. Source: https://arxiv.org/abs/2606.28270v1

## Stack placement

- Gateway layer: purpose-bound disclosure policy before tool calls.
- Runtime layer: provenance, taint, and policy verdicts attached to action traces.
- Memory layer: memory writes treated as control-authoritative actions.
- Strategy layer: prompts guide behavior, external systems enforce authority.

## References

- ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents: https://arxiv.org/abs/2606.28061v1
- On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models: https://arxiv.org/abs/2606.27567v1
- Agent-Native Immune System: Architecture, Taxonomy, and Engineering: https://arxiv.org/abs/2606.28270v1
