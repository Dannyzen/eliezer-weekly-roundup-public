# AgenticAI Daily Analysis - 2026-08-16

## Scope

There is no Sunday arXiv listing. This analysis uses one August 15 stable SDK release and three non-duplicate Friday carry-forwards submitted August 13 and listed August 14. Hugging Face and GitHub Trending were discovery signals only. Primary papers, PDFs, release notes, and repository metadata were verified read-only. No external source code was cloned or executed.

## Thesis

A credible agent test must own the evidence path, not only the final label.

## Provider-neutral test doubles make runtime state testable

OpenAI Agents SDK v0.21.0 adds public scripted testing utilities for Agent, Sandbox, Realtime, and Voice workflows without provider requests. The same release isolates interruption snapshots, checkpoint tool decisions, MCP lifecycle results, recursive agent-tool approvals, and per-operation sandbox policy snapshots.

Why it matters: deterministic test doubles now cover the runtime surfaces that usually become flaky or expensive in integration tests. This is not only mocking model output. It makes interruption, resume, approvals, sandbox policy, streaming cleanup, and MCP lifecycle behavior testable under fixed inputs.

Stack fit: harness architecture, stateful integration verification, approval continuity, and deterministic CI.

Practical tools and methodologies worth exploring:
- `agents.testing`, `agents.realtime.testing`, and `agents.voice.testing`;
- scripted interruption and resume fixtures;
- recursive approval replay;
- MCP lifecycle snapshot isolation;
- sandbox audit-policy and path-grant tests;
- provider-free failure and cleanup fixtures in CI.

Implementability score: 1.00

Core source:
- https://github.com/openai/openai-agents-python/releases/tag/v0.21.0

## Endpoint labels need treatment-invariance tests

Labels Are Not Endpoints audits an MCP security campaign by reconstructing 10,200 execution rows into 180 model-bound requests, 45 semantic requests, and 15 observable stimuli. The original grader used treatment metadata to gate the positive class. Relabeling treatment could therefore change the outcome while executed behavior stayed fixed.

The treatment-blind reconstruction corrected 58 historical `ATTACK_SUCCESS` or `HIJACK_ATTEMPT` labels to authorized benign completions. It preserved three verified protected-data transfers and one separate unauthorized-forwarding case. The locked v2 census contained zero `ATTACK_SUCCESS` records. The authors explicitly limit this to a finite campaign audit, not an attack-rate or model-ranking claim.

Why it matters: a deterministic grader can be perfectly reproducible and still measure its own experimental condition. The reusable test is simple: hold behavior fixed, vary treatment metadata, and require the endpoint class to remain unchanged.

Stack fit: evaluation integrity, MCP security testing, evidence lineage, and benchmark governance.

Practical tools and methodologies worth exploring:
- treatment-invariance tests for every security endpoint;
- exact request identity across schema, tokenizer, model revision, and delivered content;
- row-to-request denominator reconstruction;
- treatment-blind deterministic grading;
- hash-linked raw output, parser, dispatcher, and grader evidence;
- endpoint-integrity linting before benchmark publication.

Artifact status: the Apache-2.0 public repository has a populated main branch with campaign lineage, analysis, tests, CI, and manuscript artifacts. It has no tagged release.

Implementability score: 0.92

Core sources:
- https://arxiv.org/abs/2608.12880v1
- https://github.com/rana-m-ahmed/ResearchWork-on-Mcp-Privilege-Aggregation

## Formal proof needs repository-scale evaluation

Vero moves verified code generation from single functions to 43 multi-module Lean 4 repositories derived from Python, Dafny, Verus, and Coq projects. The benchmark contains 743 scored APIs and 2,705 scored specifications, supports proof-only and code-plus-proof modes, and uses an independent grader with anti-cheating constraints.

The strongest evaluated agent fully solved 27 of 43 instances and closed no specifications on the hardest repositories. Vero also accepts machine-checked evidence that a specification is unsatisfiable or a reference implementation is wrong, so benchmark defects can be surfaced instead of misclassified as agent failures.

Why it matters: formal verification is only useful when the implementation, specification, proof, repository dependencies, and grader remain coherent together. Vero turns that whole repository state into the evaluation unit.

Stack fit: coding-agent evaluation, formal methods, repository-scale harnesses, and benchmark defect handling.

Practical tools and methodologies worth exploring:
- one Vero instance as a manual coding-agent evaluation pilot;
- proof-only versus code-plus-proof comparison;
- clean-state rebuilds and axiom allowlists;
- machine-checked negative evidence for benchmark defects;
- independent grading across multi-file dependency changes.

Artifact status: the Apache-2.0 repository has a populated main branch, 43 benchmark instances, evaluation harnesses, curation tools, and agent skill files. No tagged release exists.

Implementability score: 0.88

Core sources:
- https://arxiv.org/abs/2608.13522v1
- https://github.com/sunblaze-ucb/vero

## Untrusted observations need aligned trajectory reconstruction

ATOBench injects registered response transformations into penetration-test targets, pairs each transformed run with a native run, and aligns the pair at the first affected response. Its 450 episodes form 225 matched pairs across three observation contracts and five model routes.

The process evidence matters more than extra activity. Under the JWT contract, 44 of 45 transformed episodes with primary evidence carried that evidence into a supported report. Under SQL injection, the transformation added a median of 14 actions and nine repetitions, yet no model route restored a supported finding.

Why it matters: more actions can hide a broken verification chain. Evaluation should locate the first corrupted observation, follow recovery evidence, inspect the stop decision, and bind the final claim back to the evidence path.

Stack fit: trajectory-aware evaluation, untrusted tool output, adversarial environment testing, and report support.

Practical tools and methodologies worth exploring:
- matched native versus transformed runs;
- registered observation selectors and doses;
- alignment at first intervention contact;
- evidence recovery and report-support labels;
- separate activity, recovery, stopping, and final-claim metrics.

Artifact status: the paper links a public repository, but the repository currently contains only a two-line README, no code, no license, and no release. Treat the paper as a methodology reference until the promised artifact is populated.

Implementability score: 0.62

Core sources:
- https://arxiv.org/abs/2608.12996v1
- https://github.com/daxtar2/ATOBench

## Working conclusion

The practical sequence is fixture, identity, intervention, evidence, label. If a test cannot preserve that chain, its final score is not strong enough to govern an agent runtime.
