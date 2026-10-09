# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-09

The implementation signal is to move control earlier in execution: monitor trajectory structure, check terminal obligations, govern the first skill read, and compile policy into deterministic gates.

### Guard the first skill read

Summary: A similar co-installed skill displaced the intended skill in one in five runs without lowering task completion. A pre-tool first-read hook restored fidelity on exclusive core functions.

Analysis: [dated analysis](2026-10-09/reasoning.md#guard-the-first-skill-read)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.11647v1), [replication package](https://github.com/ltroin/conflict)
Tools and methodologies worth exploring now: similarity scans, exclusive core functions, first-read hooks, selected-skill receipts, paired configuration tests
Implementability score: 0.90

### Detect required actions that never happened

Summary: ObligationBench evaluates safety-critical actions that remained undone. The public package includes 240 expert-validated trajectories, 40,000 training examples, prompts, checksums, and evaluation code.

Analysis: [dated analysis](2026-10-09/reasoning.md#detect-required-actions-that-never-happened)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.11773v1), [public repository](https://github.com/THU-Agent/ObligationGuard)
Tools and methodologies worth exploring now: positive obligations, terminal-state graders, unresolved-obligation reports, cleanup and handoff checks
Implementability score: 0.78

### Intervene on trajectory structure before failure completes

Summary: OnTrack performs streaming structural comparison of partial agent trajectories. Its SWE-bench evaluation reports about one millisecond per step and 18% compute savings on failing runs under an abort policy.

Analysis: [dated analysis](2026-10-09/reasoning.md#intervene-on-trajectory-structure-before-failure-completes)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [paper v1](https://arxiv.org/abs/2610.12375v1)
Tools and methodologies worth exploring now: normalized event streams, reference trajectories, warn and pause thresholds, intervention receipts, false-positive review
Implementability score: 0.62

### Compile policy into schema-checked tool gates

Summary: NOMOS compiles written policy into deterministic rules, rejects rules that do not fit tool schemas, and enforces state-changing calls without an online LLM.

Analysis: [dated analysis](2026-10-09/reasoning.md#compile-policy-into-schema-checked-tool-gates)
Durable topic: [Enterprise MCP Orchestration](enterprise-mcp-orchestration/enterprise-mcp-orchestration.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.11030v1), [artifact repository](https://github.com/iamupd/NOMOS), [Zenodo record](https://zenodo.org/records/22123420)
Tools and methodologies worth exploring now: typed rule IR, tool-schema validation, good-transcript replay, deterministic block receipts, safety plus utility measurement
Implementability score: 0.58

## Current implication

The next harness layer should own capability selection, terminal obligations, live intervention, and state-change gates. Model output remains a proposal until those controls issue evidence.

Latest roundup: [2026-10-09](../roundups/2026-10-09.md).
