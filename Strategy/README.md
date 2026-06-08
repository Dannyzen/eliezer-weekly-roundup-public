# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-08

### Agent skills are now runtime-verified supply-chain dependencies
Summary: A skill is a hybrid dependency: natural-language instruction, executable code, and authority hint. Scanning only prompt text or only scripts misses mixed instruction-code attacks.

Analysis: [daily sovereignty analysis](2026-06-08/sovereignty.md#agent-skills-are-now-runtime-verified-supply-chain-dependencies)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [MalSkillBench paper](https://arxiv.org/abs/2606.07131v1), [MalSkillBench repository](https://github.com/lxyeternal/MalSkillBench)
Implementable now:
- require skill manifests with source, version, body hash, scripts, tool scope, file/network/memory scope, and approval points;
- statically scan prose, scripts, tool declarations, hidden instructions, and permission claims;
- runtime-verify high-risk community skills in a sandbox before production admission.
Tools, repos, and methodologies worth exploring:
- MalSkillBench taxonomy, generated and in-the-wild malicious skill fixtures, sandbox verification, loaded-skill side-effect traces, quarantine gates
Implementability score: 0.78

### Sabotage monitors need cross-step evidence accumulation
Summary: Long-horizon sabotage can be split across individually benign actions. Safety monitors need triage, targeted inspection, accumulated evidence, and cited-step trajectory verdicts.

Analysis: [daily sovereignty analysis](2026-06-08/sovereignty.md#sabotage-monitors-need-cross-step-evidence-accumulation)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Trajectory-Aware Evaluation](../AgenticAI/trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [TRACE](https://arxiv.org/abs/2606.07054v1)
Implementable now:
- normalize traces into typed events for observations, tools, arguments, results, policy decisions, and external effects;
- run cheap triage before expensive LLM inspection;
- preserve an accumulated evidence ledger that links distant actions into a trajectory-level risk hypothesis.
Tools, repos, and methodologies worth exploring:
- triage-inspect-judge loops, SHADE-Arena-style sabotage fixtures, permission-laundering tests, trajectory evidence ledgers, offline calibration before online blocking
Implementability score: 0.66

## Previous structured update

The prior daily scan for 2026-06-07 focused on managed-client and CI governance for agent toolchains: [2026-06-07 roundup](../roundups/2026-06-07.md).
