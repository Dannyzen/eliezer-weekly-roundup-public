# AgenticAI Daily Analysis, 2026-08-10

The Monday arXiv batch is live. Both selected papers were submitted on Friday, 2026-08-07 and first listed on Monday, 2026-08-10. Exact-title and arXiv-ID checks found no prior coverage in this repository.

## Agent reliability needs runtime fault injection at the shared API boundary

AgentChaos brings chaos engineering into agent systems by injecting faults where every agent already depends on a common contract: the LLM HTTP response. It defines crash, omission, and value faults over content and tool-call fields, then verifies whether each configured fault actually triggered before scoring the run.

Across agent systems, benchmarks, backbone models, and 65 fault configurations, pass@1 fell by as much as 50 percentage points. System rankings remained consistent across models, which suggests that recovery behavior is largely a harness property rather than a model-capability property. Existing diagnosis methods identified the fault type with less than 53 percent accuracy and the fault step with less than 56 percent accuracy.

Why it matters: ordinary benchmark success does not prove recovery from truncated content, malformed tool calls, 5xx errors, or corrupted fields. The runtime needs a repeatable way to inject these failures, observe retries and propagation, and certify whether the system recovered without duplicated effects.

Fit in the stack: harness testing, fault taxonomy, deterministic evaluation, transport observability, retry policy, and release gates.

Practical tools and methods:
- place a test-only interception layer at the LLM HTTP boundary;
- inject crash, omission, and value faults into both text and tool-call fields;
- verify the fault actually fired before including a task in the denominator;
- bind fault configuration, triggering call, retry behavior, downstream propagation, outcome, and side-effect receipts;
- distinguish graceful recovery, silent corruption, duplicate effect, early termination, and unresolved diagnosis;
- run the matrix after harness, model, parser, tool-schema, or retry-policy changes.

Artifact status: the paper-owned `IntelligentDDS/AgentChaos` repository and Zenodo v0.1 software artifact resolved read-only. The repository is populated with fault-injection, trace parsing, benchmark, and evaluation files. No external code was downloaded or executed.

Implementability score: 0.90

Core sources:
- https://arxiv.org/abs/2608.06790v1
- https://github.com/IntelligentDDS/AgentChaos
- https://zenodo.org/records/21823973

## Coding-agent steering should separate deterministic judgment from LLM advice

LivePlan monitors coding-agent trajectories with deterministic rules and invokes an advisor LLM only after a rule detects drift. The monitor looks for general signals such as skipped validation, repeated failed actions, phase stagnation, and plan deviation. Blocking signals can stop an unsafe transition, while non-blocking signals can request one high-level next-step correction.

Built on SWE-agent and evaluated with three executor models and two advisor models across SWE-bench Verified and SWE-bench Pro, LivePlan improved issue-resolution rates by up to 15.2 percent, with a 9.9 percent average gain. The abstract reports only $0.08 additional cost per instance, while the paper's detailed evaluation reports average advisor cost of $0.01 to $0.06 and near-zero rule-monitor overhead. Gains concentrated on medium and hard instances, with minimal regression on already successful runs.

Why it matters: an LLM judge asked to find a problem is incentivized to invent one, while periodic review wastes cost and can arrive too late. A deterministic detector can decide whether intervention is warranted. The LLM can then remain an advisor rather than an authority.

Fit in the stack: coding-agent control planes, sessionful loops, trajectory monitors, plan-state tracking, and selective model escalation.

Practical tools and methods:
- encode lifecycle phases such as localize, reproduce, patch, and validate as explicit runtime state;
- detect repeated tool failures, repeated thoughts or actions, skipped phases, and stagnation deterministically;
- classify signals as blocking or advisory before deployment;
- invoke an advisor only when a monitor fires;
- request one bounded next step instead of replacing the whole plan;
- record signal, state snapshot, advice, accepted action, patch outcome, and regression status;
- add every false positive, missed drift, and harmful intervention to a replay suite.

Artifact status: the primary paper describes a pluggable SWE-agent implementation, but no exact public LivePlan repository was verified. The control pattern is implementable from standard trajectory events, but the reported gains remain paper-only until reproduced locally.

Implementability score: 0.83

Core source: https://arxiv.org/abs/2608.06701v1

## Working conclusion

Agent reliability should be exercised before production and corrected during execution. Inject controlled failures at the shared API boundary, then use deterministic trajectory signals to decide when an expensive advisor is allowed to intervene.
