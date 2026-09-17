# AI Strategy and Sovereignty Analysis: 2026-09-17

## Freshness and evidence boundary

The selected papers were first listed by arXiv on 17 September 2026 and submitted as v1 on 16 September 2026 UTC. Primary abstract pages and PDFs were verified. External repositories and datasets were inspected read-only. No external source was cloned, installed, built, imported, or executed.

## Govern the composed execution, not only each step

### Finding

Compositional Policy Violations identify a structural gap in per-turn guardrails. Every step can pass its local check while the complete workflow violates the governing policy. The paper defines four classes: Authority Creep, Threshold Laundering, Cumulative Sum Violation, and Context Collapse.

The proposed repair is a provenance-aware runtime that evaluates policy over the complete execution trace and recomputes guarded quantities from raw events rather than trusting a pipeline's summaries or derived representations.

### Why it matters

A more accurate step classifier cannot detect a property that no individual step determines. Authority limits, referral thresholds, aggregate spend, separation of duties, and review requirements are stateful properties. If the runtime does not own their cumulative state, policy can be laundered through individually acceptable actions.

### Fit in the strategy

This extends context-to-execution integrity. The effect gate needs both an exact proposed action and the authoritative history needed to decide whether that action is still allowed.

### Practical tools and methods worth exploring

- Store raw effect proposals, approvals, applications, reversals, and identities in an append-only run ledger.
- Express cumulative and temporal policy in Rego, Cedar, SQL, or a deterministic state machine outside model prose.
- Recompute threshold and authority state from raw events at admission time.
- Version policy, trace schema, and derived-state code independently.
- Add fixtures where every step is locally legal but the composed workflow is not.
- Return inconclusive when required provenance is missing rather than accepting derived summaries.

### Evidence caveat

This is a taxonomy and architecture paper, not a reproduced implementation. It provides illustrative regulated-workflow cases but no linked code artifact or large empirical benchmark. The control pattern is implementable; the paper's taxonomy is not yet a complete policy language.

Implementability score: 0.64

Core source: https://arxiv.org/abs/2609.18820v1

## Supporting signal: task evidence itself is an authority boundary

AgentLSD shows that fake results, decoy endpoints, and misleading validation cues can alter a security agent without an explicit malicious instruction. This is the same strategic error at a different boundary: treating observed evidence as trustworthy because it arrived through an allowed tool.

The governance implication is concrete. Tool admission, task authorization, and output validity are separate checks. A trusted tool can still return attacker-controlled or misleading evidence, so consequential effects need source lineage, independent validation, and a policy check over the resulting trajectory.

Implementability score: 0.88

Core source: https://arxiv.org/abs/2609.19140v1
Artifact: https://github.com/Golim/agent-lsd

## Practical next steps

1. Encode one cumulative policy as a deterministic trace predicate and test it against locally compliant but globally violating fixtures.
2. Require evidence lineage and validation state at the effect gate, not only tool identity.
3. Keep raw events authoritative and treat summaries as rebuildable views.
