# Strategy Daily Analysis: 2026-11-23

## Scope

Today's strategy findings come from the 23 November arXiv listing and were submitted on 20 November. Papers and linked public artifacts were inspected read-only. No external source was executed.

## 1. Keep supplier choice and uncertain effects outside the agent

[Keep the Process, Change the Supplier](https://arxiv.org/abs/2611.26966v1) places an Open Process Control Plane between an agent proposal and a capability supplier. The boundary owns input projection, authority checks, supplier eligibility, selection, and outcome records. It distinguishes definite refusal from the dangerous case where a supplier may have committed an effect before the reply was lost.

The prototype was exercised with 2,400 fault episodes across four policies, 60 process-termination and restart episodes, 19,000 timed calls across 19 configurations, five targeted mutations over 43 fixtures, and 160 substitution records. Retry-all duplicated effects in every tested lost-reply-after-commit case. Persistent runtime state prevented cross-supplier replay after restart, while same-supplier duplicate prevention still required supplier idempotency.

Why it matters: model routing and tool failover cannot treat an effectful call like a stateless inference request. An uncertain outcome must block supplier substitution until the runtime reconciles the original effect.

Practical implementation:
- compile model proposals into typed capability calls;
- project only supplier-required fields;
- keep supplier eligibility and routing policy outside model context;
- persist attempt identity before dispatch;
- model refused, committed, uncertain, and reconciled outcomes explicitly;
- fail closed on uncertain writes;
- require supplier idempotency for same-supplier retries;
- retain supplier, policy, request, outcome, and reconciliation receipts.

Artifact status: no paper-owned public implementation repository was verified. The paper evaluates scripted requests and synthetic suppliers, not an autonomous agent or live vendor portability.

Caveat: the study does not establish better task success, prompt-injection resistance, semantic correctness, compensation success, or real supplier interchangeability.

Implementability score: 0.62

Core source: [Keep the Process, Change the Supplier v1](https://arxiv.org/abs/2611.26966v1)

## 2. Treat tool metadata as executable supply-chain input

[Subverting Tool Arguments](https://arxiv.org/abs/2611.27041v1) attacks the descriptions supplied by third-party MCP servers. GRAFT mutates a tool description so an agent still selects the expected tool while replacing a targeted argument with an attacker-chosen value. This evades defenses that look mainly for conspicuous injection language or wrong-tool selection.

The evaluation uses 327 held-out queries across three MCP security datasets and seven proprietary or open models. GRAFT reported average stealthy attack success of 81.5% on MCP-SafetyBench and 63.8% on MCPTox. On MCPTox, held-out attack success was 88.0% under greedy decoding and 83.6% plus or minus 3.3% across three temperature-0.7 runs.

Why it matters: a valid tool name and JSON-valid arguments do not prove that argument values came from the user, approved evidence, or policy. Tool descriptions are executable supply-chain inputs because they shape both selection and argument construction.

Practical implementation:
- admit tool descriptors only from approved origins;
- pin and diff descriptor, schema, and server identities;
- present the exact descriptor and schema under approval;
- derive authority-bearing argument values from trusted request fields;
- compare generated arguments with request-bound values before dispatch;
- quarantine descriptor changes until regression and red-team fixtures pass;
- log descriptor hash, schema hash, argument provenance, and policy result.

Artifact status: no paper-owned public implementation repository was verified. The paper reports controlled benchmark attacks with synthesized proxy queries rather than field incidents.

Caveat: attack success depends on benchmark tool surfaces, generated query proxies, optimization budget, and victim model. The result establishes a credible attack class, not its prevalence in deployed MCP catalogs.

Implementability score: 0.76

Core source: [Subverting Tool Arguments v1](https://arxiv.org/abs/2611.27041v1)

## Working conclusion

The control plane must own both supplier state and tool-definition provenance. Agents may propose calls, but trusted runtime code must decide which supplier can act, whether a prior effect is unresolved, and where consequential argument values came from.
