# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-16

### Provider-neutral test doubles make runtime state testable

Summary: OpenAI Agents SDK v0.21.0 adds deterministic Agent, Sandbox, Realtime, and Voice tests without provider requests, plus hardened interruption, approval, MCP, and sandbox state isolation.

Analysis: [daily analysis](2026-08-16/reasoning.md#provider-neutral-test-doubles-make-runtime-state-testable)
Core source: [OpenAI Agents SDK v0.21.0](https://github.com/openai/openai-agents-python/releases/tag/v0.21.0)
Tools and methodologies worth exploring now: scripted model fixtures, interruption and resume replay, recursive approval tests, MCP lifecycle snapshots, sandbox audit-policy tests
Implementability score: 1.00

### Endpoint labels need treatment-invariance tests

Summary: A preserved MCP campaign exposed treatment leakage in its grader. Reconstructing 10,200 rows into 180 requests corrected 58 historical positive labels while preserving verified harmful behavior.

Analysis: [daily analysis](2026-08-16/reasoning.md#endpoint-labels-need-treatment-invariance-tests)
Core sources: [Labels Are Not Endpoints](https://arxiv.org/abs/2608.12880v1), [evidence repository](https://github.com/rana-m-ahmed/ResearchWork-on-Mcp-Privilege-Aggregation)
Tools and methodologies worth exploring now: treatment-invariance tests, request-unit reconstruction, treatment-blind grading, hash-linked execution evidence, endpoint-integrity linting
Implementability score: 0.92

### Formal proof needs repository-scale evaluation

Summary: Vero evaluates code and machine-checked proofs across 43 multi-module repositories. The strongest agent solved 27 instances, and formal defect appeals keep benchmark errors from becoming agent failures.

Analysis: [daily analysis](2026-08-16/reasoning.md#formal-proof-needs-repository-scale-evaluation)
Core sources: [Vero paper](https://arxiv.org/abs/2608.13522v1), [Vero repository](https://github.com/sunblaze-ucb/vero)
Tools and methodologies worth exploring now: Lean 4 repository fixtures, code-plus-proof evaluation, independent graders, axiom allowlists, machine-checked benchmark-defect appeals
Implementability score: 0.88

### Untrusted observations need aligned trajectory reconstruction

Summary: ATOBench aligns 225 native and transformed run pairs at the first changed response, then traces evidence recovery, stopping, and report support. Extra activity did not imply restored verification.

Analysis: [daily analysis](2026-08-16/reasoning.md#untrusted-observations-need-aligned-trajectory-reconstruction)
Core sources: [ATOBench paper](https://arxiv.org/abs/2608.12996v1), [artifact lead](https://github.com/daxtar2/ATOBench)
Tools and methodologies worth exploring now: matched observation perturbations, first-contact alignment, evidence-recovery labels, report-support checks, safe mock targets
Implementability score: 0.62

## Current implication

Make the evidence path the test object. Final labels are trustworthy only when exact inputs, runtime state, interventions, behavior, and verifier decisions remain linked.
