# Strategy Daily Analysis - 2026-10-23

## Make security diagnosis replayable across agent runtimes

AgentTriage defines one canonical event contract across five heterogeneous agent runtimes. Runtime overlays normalize native observations, invocation and result lifecycles are joined deterministically, and a typed provenance graph yields a policy-decisive evidence slice. Claims must cite recorded events, and the system abstains when mandatory evidence is absent.

Why it matters: a final assistant message does not prove which effects occurred or why. Runtime-specific logs also prevent one security method from traveling across harnesses. A canonical event contract creates a portable diagnosis layer without pretending synthesized identifiers are native evidence.

Fit in strategy: this is an evidence-provenance and incident-response control plane. It belongs after execution telemetry and before policy attribution, audit, or remediation.

Practical tools and methods worth exploring now:
- normalize source ingress, planning, tool invocation, tool result, and terminal effect events;
- mark native and synthesized identifiers separately;
- bind every diagnosis claim to a canonical event;
- version overlays and policy oracles with the trace;
- make the same trace deterministically replayable without an LLM judge.

Evidence and caveat: one contract captured all 159 applicable executions. On 120 adjudicated cases, AgentTriage reports 0.858 grounded joint diagnosis, 0.966 required-evidence coverage, and a 0.036 unsupported-claim rate. The Apache-2.0 repository is populated with five overlays, tests, contracts, schemas, one 53-case behavior repetition, and sanitized evidence. The evidence remains author-run and partly depends on overlay-synthesized identity.

Implementability score: 0.84

Core sources:
- [paper v1](https://arxiv.org/abs/2610.30738v1)
- [public repository](https://github.com/AsnGs/agenttriage-open-source)

## Missing evidence must trigger recovery or abstention

EpiSEM-Bench tests a precise safety failure: a tool response can contain only true statements and still omit the fact that makes an action prohibited. The benchmark uses 300 matched safe and unsafe task pairs across six domains, 1,363 annotated facts, and 10 models. Each model receives 6,052 fixed evaluation conditions before additional combination testing.

Why it matters: ordinary correctness checks ask whether the agent used available evidence. Consequential agents also need a policy for evidence that should exist but was not observed. Safe behavior requires active recovery when facts are obtainable, abstention when required facts remain missing, and useful execution when the permissible twin is established.

Fit in strategy: evidence completeness is an execution authorization condition. Missing facts should change the allowed action set before the model selects a tool call.

Practical tools and methods worth exploring now:
- enumerate safety-critical facts for each effect class;
- distinguish critical, irrelevant, observed, and recoverable evidence;
- test matched prohibited and permissible worlds;
- grade unsafe execution and excessive refusal separately;
- add one recovery tool path before final abstention.

Evidence and caveat: recovery access reduced unsafe execution for all 10 evaluated models, but resistance to omission did not guarantee useful recovery. No public implementation repository was verified during this scan, so the benchmark pattern is currently more implementable than the exact evaluation suite.

Implementability score: 0.68

Core source: [paper v1](https://arxiv.org/abs/2610.31650v1)
