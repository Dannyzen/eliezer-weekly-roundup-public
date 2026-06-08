# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-08

### Declarative skills help only when retrieval is already good
Summary: Skill files can reduce procedural and orchestration errors, but they do not fix missing or skewed evidence. Retrieval quality is the first bottleneck; declarative skill control is useful only after the evidence substrate is good enough.

Analysis: [daily reasoning analysis](2026-06-08/reasoning.md#declarative-skills-help-only-when-retrieval-is-already-good)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core source: [Declarative Skills for AI Agents in Knowledge-Grounded Tool-Use Workflows](https://arxiv.org/abs/2606.06923v1)
Implementable now:
- write compact workflow skills with preconditions, procedural rules, examples, and validators;
- run no-skill, thin-skill, full-skill, and imperative-state-machine baselines under identical retrieval;
- trace retrieved evidence, loaded skill hash, cited skill section, and verifier outcome.
Tools, repos, and methodologies worth exploring:
- skill load/no-load gates, retrieval-quality tiers, orchestration-error labels, skill/no-skill baselines, evidence coverage tests
Implementability score: 0.84

### Repository exploration should be scored before patch success
Summary: Coding-agent eval should isolate repository exploration before full patch generation. A fixed line budget, coverage, ranking, and context-efficiency score reveal whether the agent found the right code regions before editing.

Analysis: [daily reasoning analysis](2026-06-08/reasoning.md#repository-exploration-should-be-scored-before-patch-success)
Durable topic: [Agentic Search and Retrieval](agentic-search/agentic-search.md)
Core sources: [SWE-Explore](https://arxiv.org/abs/2606.07297v1), [SWE-Explore-Bench](https://github.com/Qiushao-E/SWE-Explore-Bench)
Implementable now:
- create internal issue-to-line-range exploration fixtures;
- compare ripgrep/BM25, vector retrieval, and agentic explorers under a fixed line budget;
- log search, read, localization, diagnosis, edit, and verification as separate trace phases.
Tools, repos, and methodologies worth exploring:
- fixed-line-budget repo exploration, line-level coverage, ranking metrics, context-efficiency scorecards, SWE-Explore-Bench as read-only reference
Implementability score: 0.80

## Previous structured update

The prior daily scan for 2026-06-07 focused on failed-trajectory harness repair, normalized multi-agent baselines, and memory retrieval policy plus bitemporal conflict handling: [2026-06-07 roundup](../roundups/2026-06-07.md).
