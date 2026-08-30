# Strategy Daily Sovereignty - 2026-08-22

## Scope note

There is no Saturday arXiv announcement batch. The paper below was first listed on Friday, August 21 and submitted on Thursday, August 20. External repositories were inspected read-only, and no external source was executed.

## Model routing should price the inspection step

Pandora's AI Model Routing Box reframes routing as a two-cost decision: the cost of the selected specialist and the cost of estimating whether that specialist is right. Cheap embedding-based estimates are noisy. Better estimates may require a scoring model, retrieval, partial reasoning, or tool execution. The paper derives a value-of-information rule for deciding when the expected benefit of a better estimate exceeds its inspection cost.

Across multi-LLM routing, retrieval-augmented specialists, and variable reasoning-time models, Pandora's Router matched exhaustive-estimation routing quality while querying the expensive estimator less often. The decentralized bidder variant also exposes a governance problem: when competing estimates are noisy, strategic self-assessment can improve one specialist's utility at the expense of the system.

Why it matters: model routing is not only model selection. It is a budgeted evidence-acquisition policy. A router should decide when to gather more evidence, when to stop, and when specialist self-reports are too conflicted to trust.

Practical paths worth exploring now:
- measure cheap and expensive estimator calibration separately;
- log expected value of information, inspection cost, selected specialist, and realized reward;
- start with deterministic thresholds over calibrated historical outcomes;
- treat retrieval, partial reasoning, and test execution as metered inspection actions;
- keep privacy, data residency, tool authority, and budget invariant across routes;
- shadow any learned or self-bidding router before online authority.

Evidence caveat: the paper provides a clear formal method and three experimental domains, but no public implementation artifact was exposed in the primary paper. The mechanism requires local calibration and should not be adopted from paper results alone.

Implementability score: 0.62

Core sources:
- [Pandora's AI Model Routing Box](https://arxiv.org/abs/2608.20316v1)
- [Pandora's AI Model Routing Box PDF](https://arxiv.org/pdf/2608.20316v1)

## Runtime governance is becoming release-note level behavior

Microsoft Agent Framework Python 1.15.0 persists approval state, distinguishes absent and falsey approval data, preserves fan-in trace contexts, restricts workflow-type deserialization, blocks remote MCP tool-name shadowing, deduplicates messages and streamed tool calls, and adds recovery support for long-running hosted workflows.

Why it matters: governance primitives are moving into mainstream runtime releases. Approval state, tool identity, trace continuity, deserialization boundaries, and recovery semantics should be versioned and regression-tested as platform contracts, not rebuilt ad hoc in each agent product.

Practical paths worth exploring now:
- maintain a runtime conformance suite around approval, tool identity, recovery, and telemetry;
- bind every upgrade to exact package tag, source SHA, configuration, migration result, and rollback proof;
- inspect release notes for changed authority or state semantics before dependency updates;
- require integration fixtures for remote MCP collisions, workflow resume payloads, and duplicate tool calls.

Artifact status: official release and public repository inspected read-only. No package was installed.

Implementability score: 0.92

Core sources:
- [Microsoft Agent Framework Python 1.15.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.15.0)
- [Microsoft Agent Framework repository](https://github.com/microsoft/agent-framework)
