# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-09

### Skill files are executable supply-chain artifacts

Summary: A 2,826-skill benchmark produced 5,629 runs. Under auto-approved delegated execution, Gemini CLI was exploited in 95.5 to 96.1 percent of runs and Qwen Code in 71.6 to 74.0 percent.

Analysis: [daily analysis](2026-08-09/sovereignty.md#skill-files-are-executable-supply-chain-artifacts)
Core sources: [paper](https://arxiv.org/abs/2608.05223v1), [read-only artifact](https://github.com/awsm-research/AgentJailbreak)
Tools and methodologies worth exploring now: artifact hashes, capability manifests, static command extraction, sandbox detonation, denied-by-default runtime policy, effect receipts
Implementability score: 0.84

### Trajectory risk needs pre-action runtime state

Summary: DreamGuard combines immediate-hazard and prefix-risk evidence in a compact recurrent state. It reports 25-millisecond calls, 96.3 percent pre-hazard intervention recall, and 72.92 percent online safety while preserving 90.38 percent utility.

Analysis: [daily analysis](2026-08-09/sovereignty.md#long-horizon-guardrails-need-compact-risk-state-before-action)
Core source: [paper](https://arxiv.org/abs/2608.05695v1)
Tools and methodologies worth exploring now: versioned trajectory events, bounded risk state, pass-hold-block decisions, replay suites, threshold receipts, deterministic commit-time policy
Implementability score: 0.52

## Current implication

Treat dynamically loaded skills as privileged software, not helpful prose. Then track risk across the trajectory outside the acting model and require a pre-action gate before privileged effects.
