# Strategy Daily Analysis - 2026-09-20

## Run a closed-world resolver before policy gates

"Closed-World Resolution Against Tool Hallucination" separates three controls that agent stacks often collapse: selecting a tool, resolving an emitted call against a real registry and schema, and authorizing the resolved action. A policy gate cannot reject a fabricated tool if the call never resolved to a known contract.

Across ten hosted models and two invocation surfaces, the study records 322 genuine tool hallucinations. Fabricated-tool calls concentrate on unconstrained raw JSON, 34 versus 3 under a schema-enforcing API. On a merged live MCP surface, the authors record another 154 hallucinations, including collisions and shadowing that a single flat registry cannot represent.

The strategic pattern is a fail-closed resolution rung before any causal or permission gate. Resolve exact tool identity, namespace, version, and argument signature first. Only then evaluate authority and policy.

Why it matters: authentication and policy do not help if runtime dispatch interprets an unbound name or undeclared argument. Resolution is the boundary that turns model text into a candidate action.

Practical controls worth exploring now:
- reject tool names absent from the admitted registry;
- validate arguments against the exact admitted signature before policy evaluation;
- qualify MCP identities by server, package or source revision, schema hash, and endpoint origin;
- reject namespace collisions and shadowed definitions during catalog merge;
- log resolution failure separately from policy denial and execution failure;
- preserve one explicit irreducible class for schema-indistinguishable borrowed arguments.

Evidence caveat: the paper assumes a trusted registry and primarily measures the failure class rather than a production deployment. No public implementation repository resolved from the primary paper surfaces, so the released benchmark claim was not independently inspected here.

Implementability score: 0.94

Core source: [Closed-World Resolution Against Tool Hallucination in LLM Agents](https://arxiv.org/abs/2609.19425v1)
