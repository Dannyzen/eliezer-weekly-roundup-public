# Strategy Daily Analysis - 2026-08-16

## Scope

No Sunday arXiv batch was listed. This strategy note combines one August 15 stable SDK release with three non-duplicate Friday carry-forwards. Primary release notes, immutable arXiv papers, PDFs, and read-only artifact metadata were verified. No external repository code was executed.

## Thesis

Evaluation becomes governance only when the runtime owns the evidence path.

## A control plane needs provider-independent fixtures

OpenAI Agents SDK v0.21.0 makes deterministic Agent, Sandbox, Realtime, and Voice tests public without provider requests. It also hardens interruption snapshots, recursive approvals, MCP lifecycle isolation, and sandbox policy snapshots.

Strategic implication: approval and recovery claims should be release-gated by deterministic fixtures before live provider tests. Provider calls test integration. Provider-independent fixtures test the control contract itself.

What to implement now:
- one interrupted-run fixture with detached state snapshots;
- one recursive approval and resume fixture;
- one MCP lifecycle isolation fixture;
- one sandbox policy and path-grant fixture;
- one terminal-failure cleanup fixture.

Cost: scripted models cannot prove provider fidelity. Keep a smaller live integration lane after the deterministic gate.

Implementability score: 1.00

Core source:
- https://github.com/openai/openai-agents-python/releases/tag/v0.21.0

## Security labels need source-owned behavioral evidence

Labels Are Not Endpoints shows how treatment metadata can contaminate a grader while the underlying behavior stays fixed. Its correction reduced 10,200 stored rows to the actual request units and changed 58 historical positive labels without erasing verified protected-data transfers.

Strategic implication: benchmark labels are claims, not authority. A security result should be releasable only when raw requests, outputs, parser events, dispatcher receipts, authorization state, and grader predicates support the same behavioral conclusion.

What to implement now:
- a treatment-invariance gate for every condition-aware grader;
- explicit row, request, scenario, and model denominators;
- frozen endpoint code and evidence hashes;
- separate authorized completion, attempted hijack, and realized protected transfer classes.

Cost: evidence reconstruction is slower than reading a results table. It is still cheaper than governing deployments with a leaked endpoint.

Implementability score: 0.92

Core sources:
- https://arxiv.org/abs/2608.12880v1
- https://github.com/rana-m-ahmed/ResearchWork-on-Mcp-Privilege-Aggregation

## Proof systems need benchmark-defect authority

Vero evaluates implementation and machine-checked proof across 43 multi-module repositories. Its audit path lets agents prove that a specification is unsatisfiable or reference code is wrong rather than forcing every failure into the agent-error bucket.

Strategic implication: a verifier should not have unilateral authority over a flawed benchmark. The release contract needs two paths: prove the submitted work satisfies the specification, or produce machine-checkable evidence that the specification or reference is defective.

What to implement now:
- independent proof checking from a clean state;
- immutable API, specification, and axiom boundaries;
- machine-checked defect appeals;
- benchmark versioning when an appeal succeeds;
- separate agent failure and benchmark defect receipts.

Cost: Lean expertise and curation effort are material. Start with one repository where correctness matters enough to justify the proof surface.

Implementability score: 0.88

Core sources:
- https://arxiv.org/abs/2608.13522v1
- https://github.com/sunblaze-ucb/vero

## Untrusted observations must stay evidence until verified

ATOBench pairs native and transformed target runs, aligns them at the first changed response, and follows later actions, evidence recovery, stopping, and reporting. Under one contract, 44 of 45 transformed episodes preserved primary evidence into a supported report. Under SQL injection, extra activity never restored a supported finding.

Strategic implication: target responses and tool outputs are observations, not truth. A runtime should preserve their source and transformation identity, then require independent corroboration before they authorize a final claim or effect.

What to implement now:
- observation identity and provenance at tool ingress;
- safe matched perturbation tests in mock environments;
- first-contact alignment across trajectories;
- evidence-to-report support checks;
- denial or uncertainty when recovery evidence is absent.

Cost: the linked ATOBench repository is not populated beyond a README. The control pattern is implementable, but the paper's harness is not currently reusable.

Implementability score: 0.62

Core sources:
- https://arxiv.org/abs/2608.12996v1
- https://github.com/daxtar2/ATOBench

## Working conclusion

Do not promote a result because the agent was active, the grader was deterministic, or the proof checker returned green. Promote it only when the evidence path is identifiable, invariant under irrelevant labels, independently checked, and preserved through the final claim.
