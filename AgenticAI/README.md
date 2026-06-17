# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-17

### MCP factuality needs source ownership, not pooled support

Summary: ProvenanceGuard catches a failure mode that normal source-grounded scoring misses: a claim can be supported somewhere in pooled evidence while being attributed to the wrong source. MCP agents need stable tool IDs, source IDs, raw outputs, claim routing, and per-claim source verdicts.

Analysis: [daily reasoning analysis](2026-06-17/reasoning.md#mcp-factuality-needs-source-ownership-not-pooled-support)
Durable topics: [Agent Gateway Governance](../Strategy/agent-gateway-governance/agent-gateway-governance.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [ProvenanceGuard](https://arxiv.org/abs/2606.18037v1), [Zscaler agentic AI security platform](https://www.zscaler.com/press/zscaler-unveils-new-product-innovations-secure-agentic-ai)
Implementable now:
- require MCP tools to emit stable tool IDs, source IDs, and raw output references
- decompose final answers into atomic claims for high-risk workflows
- route each claim back to source-specific evidence rather than pooled context
- block or downgrade answers when support exists but source attribution is wrong
Tools, repos, and methodologies worth exploring:
- MCP trace schemas, claim extraction, NLI or entailment checks, token-alignment evidence, source IDs, LangSmith or Langfuse trace exports, provenance-aware citation checks
Implementability score: 0.74

### Skill systems need compositional routing plus per-skill utility evals

Summary: SkillWeaver treats skill use as decompose, retrieve, and compose, not one-shot semantic lookup. The agentic skills evaluation framework supplies the missing promotion gate: test individual skills against realistic skill-derived tasks, rubrics, and no-skill baselines before they become default runtime authority.

Analysis: [daily reasoning analysis](2026-06-17/reasoning.md#skill-systems-need-compositional-routing-plus-per-skill-utility-evals)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Context Economy](context-economy/context-economy.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [Compositional Skill Routing](https://arxiv.org/abs/2606.18051v1), [A Framework for Evaluating Agentic Skills at Scale](https://arxiv.org/abs/2606.17819v1)
Implementable now:
- split skill metadata from full skill bodies and index metadata first
- decompose tasks into atomic skill needs before retrieval
- compose selected skills into a dependency-aware DAG with validators
- keep no-skill, wrong-skill, thin-skill, and full-skill baselines for high-value skills
Tools, repos, and methodologies worth exploring:
- FAISS or pgvector, DAG planners, MCP skill catalogs, skill manifests, rubric generation, paired trajectory comparison, progressive disclosure
Implementability score: 0.76

### Evaluation needs trajectory preferences and oracle-aware test gates

Summary: Offline trajectory preferences reduce tied agent comparisons by using partial progress and time-to-return profiles, while All Smoke, No Alarm shows that most agent-authored test patches have weak or no explicit oracle signals. Agent eval needs progress evidence and test-oracle evidence, not only terminal pass/fail or test-file counts.

Analysis: [daily reasoning analysis](2026-06-17/reasoning.md#evaluation-needs-trajectory-preferences-and-oracle-aware-test-gates)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [Offline Preference-Based Trajectory Evaluation](https://arxiv.org/abs/2606.17541v1), [All Smoke, No Alarm](https://arxiv.org/abs/2606.18168v1)
Implementable now:
- store progress checkpoints and time-to-return profiles for agent runs
- compare near-miss trajectories instead of treating all failures as equal
- classify agent-authored tests by explicit oracle strength
- block smoke-only tests before merge or completion
Tools, repos, and methodologies worth exploring:
- pairwise preference evals, progress ledgers, trace checkpoints, assertion-density checks, mutation testing, property-based tests, CodeQL or AST rules for test oracles, CI gates for agent-authored diffs
Implementability score: 0.86

## Previous structured update: Daily scan, 2026-06-16

### Procedure fingerprints turn traces into routing and monitoring signals

Summary: Agent trajectories as programs and ProcGrep make the agent trace a procedural artifact. Instead of only scoring pass/fail, teams can fingerprint how an agent searches, reads, edits, tests, retries, and fails, then use those fingerprints for routing, monitoring, and regression detection.

Analysis: [daily reasoning analysis](2026-06-16/reasoning.md#procedure-fingerprints-turn-traces-into-routing-and-monitoring-signals)
Core sources: [Agent trajectories as programs](https://arxiv.org/abs/2606.16988v1), [ProcGrep](https://github.com/hamidahoderinwale/procgrep), [PACT](https://arxiv.org/abs/2606.16215v1)
Implementability score: 0.80

### Tool and context selection must preserve intention fit and cache continuity

Summary: SING retrieves tools through an intention-tool graph instead of schema stuffing, while TokenPilot and LightMem2 show that context pruning must preserve prompt-prefix cache continuity.

Analysis: [daily reasoning analysis](2026-06-16/reasoning.md#tool-and-context-selection-must-preserve-intention-fit-and-cache-continuity)
Core sources: [SING](https://arxiv.org/abs/2606.16591v1), [TokenPilot](https://arxiv.org/abs/2606.17016v1), [LightMem2](https://github.com/zjunlp/LightMem2)
Implementability score: 0.83

### Skills are moving from runtime text toward searched and learned behavior modules

Summary: OpenClaw-Skill uses collective skill tree search, while Skill-to-LoRA uses skill documents offline to train dynamically loadable behavior adapters. The audited source and hashes still matter.

Analysis: [daily reasoning analysis](2026-06-16/reasoning.md#skills-are-moving-from-runtime-text-toward-searched-and-learned-behavior-modules)
Core sources: [OpenClaw-Skill](https://arxiv.org/abs/2606.16774v1), [Skill-to-LoRA](https://arxiv.org/abs/2606.16769v1), [Dynamic Malicious Skills](https://arxiv.org/abs/2606.16287v1)
Implementability score: 0.58
