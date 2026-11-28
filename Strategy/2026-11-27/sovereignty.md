# Strategy Weekly Sovereignty: 2026-11-27

## Thesis

Sovereign agent operation requires authority and effects to survive context changes without becoming model-authored fiction. The control plane must distinguish what the agent reads from what the system authorizes.

## Preserve authenticated intent across compaction

[LLM Agent Authorization Across Context Compaction](https://arxiv.org/abs/2611.32194v1) shows that model-written summaries can erase authorship boundaries and cause injected data to be credited as user intent. The proposed fix carries authenticated user text across compaction separately while the agent continues to read the summary.

Why it matters: a summary is a lossy interpretation. Treating it as an authority source lets the model or attacker rewrite the policy basis.

Fit in the stack: the authority plane stores origin-bound user statements and policy facts independently from conversational context.

Implementable now:
- authenticate and retain user intent at ingress
- bind policy derivation to origin-bearing records
- keep summaries read-only to the authorizer
- fail closed when the required original statement is unavailable

Implementability score: **0.72**

Core source: [LLM Agent Authorization Across Context Compaction](https://arxiv.org/abs/2611.32194v1)

Related durable topic: [Context compaction provenance](../context-compaction-provenance/context-compaction-provenance.md)

## Mediate concrete effects below tool calls

[AgentBouncer](https://arxiv.org/abs/2611.30621v1) argues that trajectory defenses miss what tools actually execute. It mediates system calls and judges necessity and safety at the effect boundary. [AgentLens](https://arxiv.org/abs/2611.34380v1) complements that design by requiring executable reachability before a static weakness becomes a confirmed security finding.

Why it matters: tool names and model explanations are narratives. Filesystem, network, credential, and process effects are the consequences that need enforcement.

Fit in the stack: an execution-control broker sits between tool runtimes and the host, with explicit grants, deterministic rules, learned arbitration for ambiguous cases, and receipts.

Implementable now:
- isolated workers with scoped filesystem and network access
- syscall, eBPF, seccomp, container, or VM-level effect observation
- deterministic deny rules before learned arbitration
- bounded exploit validation for high-severity findings

Implementability score: **0.48**

Core sources: [AgentBouncer](https://arxiv.org/abs/2611.30621v1), [AgentLens](https://arxiv.org/abs/2611.34380v1)

Related durable topic: [Runtime governance](../runtime-governance/runtime-governance.md)

## Require evidence certificates for release decisions

[Agent-as-a-Verifier](https://arxiv.org/abs/2611.34132v1) compiles claims and acceptance obligations independently, then produces checkable evidence certificates rather than a scalar score.

Why it matters: confidence scores rank candidates but do not explain what was checked. A release authority needs evidence tied to source identity, exact obligations, commands, and artifacts.

Fit in the stack: the verification plane produces a certificate that the release gate can inspect without trusting the candidate agent's narrative.

Implementable now:
- claim and dependency graphs
- independently compiled acceptance contracts
- obligation-level command and artifact receipts
- fail-closed handling for missing evidence

Implementability score: **0.74**

Core sources: [Agent-as-a-Verifier](https://arxiv.org/abs/2611.34132v1), [General-Verifier](https://github.com/sunyxedu/General-Verifier)

Related durable topic: [Evaluation containment control plane](../evaluation-containment-control-plane/evaluation-containment-control-plane.md)

## Audit routeability before deploying a router

[RouteabilityBench](https://arxiv.org/abs/2611.34825v1) asks whether a benchmark and portfolio contain enough prompt-specific variation for routing to beat a single strong model. Across four benchmarks and 66 models, common routing enhancements did not consistently outperform the best single model.

Why it matters: a router adds another predictor, policy surface, and failure mode. If oracle headroom is small or models tie frequently, routing complexity has no justified target.

Fit in the stack: routeability is a preflight gate before online model selection. Routing remains shadow-only until the audit shows separability and bounded fallback behavior.

Implementable now:
- oracle headroom and tied-best analysis
- family-corrected comparisons
- shadow routing against a fail-closed single-model baseline
- cost and latency accounting on the same scored matrix

Implementability score: **0.76**

Core source: [Routeability Before Routing](https://arxiv.org/abs/2611.34825v1)

Related durable topic: [Model router governance](../model-router-governance/model-router-governance.md)

## Working conclusion

The strongest strategic move is to keep interpretation flexible while making authority, effects, and acceptance evidence rigid. Summaries can change. Permissions, side effects, and release receipts need origin, scope, and replay.
