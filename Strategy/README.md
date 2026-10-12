# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-12 Daily Scan

The current governance signal is representation-to-authority control. Tool schemas and persistent artifacts both need evidence-bearing gates before they can cause effects.

### Compile tool metadata into semantic admission tests

Summary: ToFu maps tool metadata to 74 CWE-guided sanitizers and runtime oracles. It reports 253 verified bugs affecting 343 tools across 118 of 273 evaluated MCP servers.

Analysis: [daily strategy analysis](2026-10-12/sovereignty.md#tofu-compile-tool-metadata-into-security-tests)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [paper v1](https://arxiv.org/abs/2610.13651v1)
Tools and methodologies worth exploring now: metadata-to-policy compilation, schema-valid fuzzing, effect introspection, version-bound sanitizer suites, catalog admission receipts
Implementability score: 0.72

### Restore artifact provenance before reuse

Summary: SkillRelayGuard restores artifact origin and evidence at read time, then reviews the proposed operation before execution. It reduces aggregate attack success from 69.5% to 10.9% on a 270-case benchmark.

Analysis: [daily strategy analysis](2026-10-12/sovereignty.md#skillrelayguard-restore-artifact-provenance-before-reuse)
Durable topic: [Persistent-State Agent Control](persistent-state-agent-control/persistent-state-agent-control.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.13227v1), [SkillRelay repository](https://github.com/Dianshu-Liao/SkillRelay)
Tools and methodologies worth exploring now: artifact lineage, read-time context restoration, current-request authorization, pre-execution advisory review, exact-effect receipts
Implementability score: 0.79

## Current implication

Persistent availability does not grant current authority. Restore origin, scope, and evidence before reused state can influence an external effect.

Latest roundup: [2026-10-12 daily scan](../roundups/2026-10-12.md).
