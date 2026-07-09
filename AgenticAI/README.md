# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-09

### Action-graded severity makes tool-agent red-team results operational

Summary: Binary attack-success rate hides the difference between a harmless bad action and an externally visible, cross-scope, privilege-expanding one. Action-graded severity scores the actual tool-call trajectory on an L0 to L6 ordinal scale, with a public artifact for code, prompts, configs, figures, and per-episode results.

Analysis: [daily reasoning analysis](2026-07-09/reasoning.md#action-graded-severity-makes-tool-agent-red-team-results-operational)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [Action-graded severity paper](https://arxiv.org/abs/2607.07474v1), [action-graded-severity repo](https://github.com/Harry-Ashley/action-graded-severity)
Implementable now:
- score internal red-team traces by reversibility, scope crossing, and privilege expansion
- keep per-episode logs that record action target, scope, privilege level, and final effect
- report severity distribution next to attack-success rate and task utility
Tools, repos, and methodologies worth exploring:
- `Harry-Ashley/action-graded-severity`, AgentDojo-style traces, deterministic severity oracles, LLM judge agreement checks, escalation-chain labels
Implementability score: 0.88

### STRACE makes trajectory optimization root-cause aware

Summary: STRACE turns noisy long-horizon traces into high-signal optimization inputs. It filters redundant failure traces at batch level, then builds textual dependency graphs inside selected traces to remove non-causal steps and identify the root-cause module.

Analysis: [daily reasoning analysis](2026-07-09/reasoning.md#strace-makes-trajectory-optimization-root-cause-aware)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Sessionful Agent Loops](sessionful-agent-loops/sessionful-agent-loops.md)
Core sources: [STRACE paper](https://arxiv.org/abs/2607.07702v1), [STRACE repo](https://github.com/moomight/STRACE)
Implementable now:
- cluster failure traces before asking a model to propose repairs
- represent plan steps, tool calls, observations, verifier results, and policy decisions as dependency graphs
- send only the causal failure slice into reflection, fine-tuning, or remediation workflows
Tools, repos, and methodologies worth exploring:
- `moomight/STRACE`, textual dependency graphs, causal slice extraction, failure-pattern mining, module-level remediation labels
Implementability score: 0.68

## Supporting recent AgenticAI context

The 2026-07-08 scan showed that replayable benchmark packs and conflict-preserving memory are becoming concrete implementation artifacts. The 2026-07-09 scan adds the next layer: tool trajectories should be severity-scored and causally sliced before they drive optimization.
