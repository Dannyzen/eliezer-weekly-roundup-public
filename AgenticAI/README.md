# AgenticAI

Implementation analysis for agent evaluation, memory, context policy, tools, model routing, and orchestration.

## Latest Structured Update: 2026-10-20 Daily Scan

### Test evidence exposure, not only tool execution

Summary: Correct tool execution can still produce a wrong answer when retrieval makes the agent use a non-authoritative output.

Analysis: [test evidence exposure, not only tool execution](2026-10-20/reasoning.md#test-evidence-exposure-not-only-tool-execution)

Core source: [Same Simulation, Different Evidence v1](https://arxiv.org/abs/2610.26836v1)

Implementable now:
- label authoritative tool outputs;
- record build, exposure, and closure stages;
- replay deterministic calls to isolate computation from evidence use;
- compare inline, indexed, and authority-labeled retrieval.

Implementability score: 0.88

### Grade compression on evidence preservation

Summary: Downstream QA can hide unfaithful compression; evaluate whether qualifiers, alternatives, and minority evidence survive.

Analysis: [grade compression on evidence preservation](2026-10-20/reasoning.md#grade-compression-on-evidence-preservation)

Core sources: [KEEP-Bench v1](https://arxiv.org/abs/2610.26827v1), [repository](https://github.com/PlusLabNLP/KEEP-Bench), [dataset](https://huggingface.co/datasets/uclanlp/KEEP-Bench)

Implementable now:
- run proposition-level evidence recall;
- test parallel, conditional, and imbalanced evidence;
- retain raw spans outside the compressed view;
- measure recall, tokens, FLOPs, latency, and outcome together.

Implementability score: 0.76

### Evaluate coding agents against complete delivery contracts

Summary: Component production and passing isolated tests do not prove that a full PRD, including integration obligations, was delivered.

Analysis: [evaluate coding agents against complete delivery contracts](2026-10-20/reasoning.md#evaluate-coding-agents-against-complete-delivery-contracts)

Core source: [When Coding Agents Outpace Review v1](https://arxiv.org/abs/2610.26394v1)

Implementable now:
- decompose PRDs into atomic Code Points;
- bind criteria to source, test, integration, or inspection evidence;
- report component, integration, and complete-delivery scores separately;
- sample independent expert review.

Artifact caveat: the paper's named repository did not resolve during this scan.

Implementability score: 0.62

## Current implication

Agent evaluation should trace authoritative evidence through computation, retrieval, compression, integration, and acceptance. Final answers and passing components are weak proof when the harness cannot show which evidence survived and which obligations were delivered.
