# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-11

### Project memory should be an event log plus a pre-action judge
Summary: PROJECTMEM makes coding-agent memory local, append-only, typed, and action-aware. It records issues, attempts, fixes, decisions, and notes as a plain-text event log, projects compact MCP summaries, and warns before repeated failed fixes or edits to fragile files.

Analysis: [daily reasoning analysis](2026-06-11/reasoning.md#project-memory-should-be-an-event-log-plus-a-pre-action-judge)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md)
Core sources: [PROJECTMEM](https://arxiv.org/abs/2606.12329v1), [riponcm/projectmem](https://github.com/riponcm/projectmem)
Implementable now:
- log project events as typed append-only records;
- project summaries for active agent context through MCP or local files;
- gate proposed edits against known failed attempts and fragile-file records.
Tools, repos, and methodologies worth exploring:
- projectmem, MCP summary tools, SQLite or plain-text event logs, pre-action validators, trace-linked memory events
Implementability score: 0.86

### Deterministic layer slices catch regressions that aggregate agent scores hide
Summary: Layer-Isolated Evaluation decomposes an agent into deterministic scaffold layers and tests each with no-LLM assertion slices. The key lesson is that aggregate task success can hide local routing, memory, safety, or lifecycle failures.

Analysis: [daily reasoning analysis](2026-06-11/reasoning.md#deterministic-layer-slices-catch-regressions-that-aggregate-agent-scores-hide)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [Layer-Isolated Evaluation](https://arxiv.org/abs/2606.11686v1)
Implementable now:
- define harness layers for routing, memory, decomposition, safety, escalation, verifier, and envelope logic;
- run per-layer deterministic tests in CI;
- inject controlled regressions to verify localization.
Tools, repos, and methodologies worth exploring:
- no-LLM pure test mode, locked per-layer baselines, CI slice dashboards, regression-injection fixtures
Implementability score: 0.91

### Skill security needs targeted runtime probes, not static inspection
Summary: Runtime Skill Audit shows that skill risk can be environment-dependent. A skill may look harmless until it sees a specific local file, persistent state, user request, or multi-step tool path, so admission needs targeted runtime probing.

Analysis: [daily reasoning analysis](2026-06-11/reasoning.md#skill-security-needs-targeted-runtime-probes-not-static-inspection)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core sources: [Runtime Skill Audit](https://arxiv.org/abs/2606.11671v1), [snyk/agent-scan](https://github.com/snyk/agent-scan)
Implementable now:
- profile skill risk interfaces before admission;
- run sandbox probes against file, network, shell, memory, and credential surfaces;
- store verdict, probe set, skill hash, trace ID, and allowed scopes.
Tools, repos, and methodologies worth exploring:
- RSA-style targeted probes, Snyk Agent Scan, skill risk manifests, sandboxed test contexts, trace-based labels
Implementability score: 0.80

## Previous structured update

The prior daily scan for 2026-06-10 focused on pruned tool history, topic-document memory, context-rot checks, and executable security validation: [2026-06-10 roundup](../roundups/2026-06-10.md).
