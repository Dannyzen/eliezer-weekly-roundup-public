# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: Wednesday, 2026-07-29

### Formal specifications need trace validation and code replay

Summary: Specula turns agent-authored TLA+ models into candidate artifacts checked by model checking, trace validation, and code-level reproduction. The authors report 249 bugs across 48 systems, with 89 reported, 68 confirmed, and 24 fixed.

Analysis: [daily reasoning analysis](2026-07-29/reasoning.md#specula-makes-formal-specifications-executable-bug-finding-artifacts)
Core sources: [paper](https://arxiv.org/abs/2607.25333v1), [Apache-2.0 repository](https://github.com/specula-org/Specula)
Implementable now:
- pilot one narrow invariant class against an immutable target revision;
- require trace validation and code-level replay;
- bind the specification and reproduction evidence to one run identity.
Tools, repositories, and methodologies:
- Specula, TLA+, TLC, trace validation, isolated target copies, code-level replay
Implementability score: 0.78

### Optimize a static harness before learning online

Summary: In a released 729-configuration study, a DSPy-optimized static baseline matched or beat online bandit and REINFORCE controllers across the reported domains and models, usually with fewer tokens.

Analysis: [daily reasoning analysis](2026-07-29/reasoning.md#static-harness-optimization-beats-cold-start-online-adaptation)
Core sources: [paper](https://arxiv.org/abs/2607.25415v1), [research repository](https://github.com/dpaul0501/context-optimization-rl)
Implementable now:
- define deterministic verifiers and a small reviewed action space;
- establish a static optimized baseline;
- promote online adaptation only after held-out success and total-cost gains.
Tools, repositories, and methodologies:
- DSPy BootstrapFewShot, contextual bandits, REINFORCE, reward decomposition, trajectory replay
Implementability score: 0.65

## Current implication

Agent reliability improves when model output becomes a candidate artifact rather than accepted truth. Validate specifications against code behavior, and validate adaptive harnesses against a cheaper static baseline.
