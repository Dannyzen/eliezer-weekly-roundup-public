# AgenticAI

This index tracks the most recent structured update. Each finding includes a summary, a link into the detailed analysis, core sources, practical implementation paths, and an implementability score from 0 to 1.

## Most Recent Structured Update: Thursday, 2026-07-23

### Skill safety needs end-to-end admission tests

Summary: OpenSkillRisk packages 263 real marketplace risky skills into controlled sandboxes. Even the safest tested configurations execute unsafe actions in about 17 percent of cases, and awareness often fails to become timely intervention.

Analysis: [daily reasoning analysis](2026-07-23/reasoning.md#skill-safety-needs-end-to-end-admission-tests)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md#july-23-update-skill-admission-needs-end-to-end-effect-tests)
Core sources: [paper](https://arxiv.org/abs/2607.20121v1), [repository](https://github.com/Miaow-Lab/OpenSkillRisk), [dataset](https://huggingface.co/datasets/Miaow-Lab/OpenSkillRisk)
Implementable now:
- import the seven-class taxonomy into the skill registry;
- detonate untrusted skills with fake secrets, marker files, and network traps;
- score the first unsafe attempted effect, intervention timing, completion, and over-defense;
- enforce side-effect policy below the skill prompt.
Tools, repositories, and methodologies:
- OpenSkillRisk, SkillSpector, sandbox detonation, canary resources, policy-as-code, approval replay
Implementability score: 0.82

### Document agents need deterministic artifact verification

Summary: DocOps ships 210 Word, Excel, PowerPoint, and PDF tasks with deterministic native-state verifiers. The best reported configuration passes 0.671 overall, while complex long-range workflows approach zero and often damage structural metadata.

Analysis: [daily reasoning analysis](2026-07-23/reasoning.md#document-agents-need-deterministic-artifact-verification)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md#july-23-update-document-work-needs-native-artifact-verifiers)
Core sources: [paper](https://arxiv.org/abs/2607.19865v1), [repository](https://github.com/icip-cas/DocOps), [project page](https://docopsbench.github.io)
Implementable now:
- select ten representative tasks and run fixed model-and-harness comparisons;
- verify formulas, styles, bookmarks, metadata, and untouched object trees;
- bind output digests and verifier versions to traces;
- promote passing tasks into the release suite.
Tools, repositories, and methodologies:
- DocOps, Harbor, native-format parsers, structural diffs, deterministic tests, artifact receipts
Implementability score: 0.88

## Current implication

Agent packages and agent outputs need symmetric evidence gates. Detonate capabilities before admission, then deterministically verify the native artifact before release.
