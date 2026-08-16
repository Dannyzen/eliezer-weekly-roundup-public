# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-16

### A control plane needs provider-independent fixtures

Summary: OpenAI Agents SDK v0.21.0 makes interruptions, approvals, MCP lifecycle, sandbox policy, and cleanup testable without live provider requests.

Analysis: [daily strategy](2026-08-16/sovereignty.md#a-control-plane-needs-provider-independent-fixtures)
Core source: [OpenAI Agents SDK v0.21.0](https://github.com/openai/openai-agents-python/releases/tag/v0.21.0)
Tools and methodologies worth exploring now: scripted control-contract fixtures, recursive approval replay, MCP lifecycle isolation, per-operation sandbox policy snapshots
Implementability score: 1.00

### Security labels need source-owned behavioral evidence

Summary: Labels Are Not Endpoints shows that a deterministic grader can still leak treatment identity. Behavioral conclusions need request identity, authorization state, raw execution evidence, and treatment-invariant endpoints.

Analysis: [daily strategy](2026-08-16/sovereignty.md#security-labels-need-source-owned-behavioral-evidence)
Core sources: [Labels Are Not Endpoints](https://arxiv.org/abs/2608.12880v1), [evidence repository](https://github.com/rana-m-ahmed/ResearchWork-on-Mcp-Privilege-Aggregation)
Tools and methodologies worth exploring now: treatment-invariance release gates, evidence hashes, explicit denominators, separate attempt and realized-effect classes
Implementability score: 0.92

### Proof systems need benchmark-defect authority

Summary: Vero gives agents a machine-checked appeal path when specifications are unsatisfiable or reference code is wrong. The benchmark is not allowed to define truth without challenge.

Analysis: [daily strategy](2026-08-16/sovereignty.md#proof-systems-need-benchmark-defect-authority)
Core sources: [Vero paper](https://arxiv.org/abs/2608.13522v1), [Vero repository](https://github.com/sunblaze-ucb/vero)
Tools and methodologies worth exploring now: clean-state proof checking, immutable spec boundaries, formal defect appeals, versioned benchmark corrections
Implementability score: 0.88

### Untrusted observations must stay evidence until verified

Summary: ATOBench shows that deceptive target responses can break verification even while agents take more actions. Observations need provenance and corroboration before they authorize a claim.

Analysis: [daily strategy](2026-08-16/sovereignty.md#untrusted-observations-must-stay-evidence-until-verified)
Core sources: [ATOBench paper](https://arxiv.org/abs/2608.12996v1), [artifact lead](https://github.com/daxtar2/ATOBench)
Tools and methodologies worth exploring now: observation provenance, safe matched perturbations, first-contact trajectory alignment, evidence-to-report support checks
Implementability score: 0.62

## Current implication

Evaluation becomes governance only when a separately owned evidence chain supports the label, proof, report, or release decision.
