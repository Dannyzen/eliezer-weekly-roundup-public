# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-10

### Prismata applies contextual least privilege to web agents

Summary: Prismata derives task-specific privilege labels over page structure, restricts which untrusted content reaches planning, and gates which actions that content can influence. The paper reports average attack success falling from 85.5% to 0.7% in its main attack settings while preserving benign task utility.

Analysis: [daily sovereignty analysis](2026-07-10/sovereignty.md#prismata-confines-both-what-a-web-agent-sees-and-what-it-can-do)
Durable topic: [Untrusted Data Boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md)
Core source: [Prismata](https://arxiv.org/abs/2607.08147v1)
Implementable now:
- classify DOM regions by origin and trust class before planner exposure
- derive a task-scoped action allowlist and fail closed when uncertainty could widen capability
- bind each effectful action to the content label and policy verdict that authorized it
Tools, repos, and methodologies worth exploring:
- BrowserGym-style structured DOM traces, Biba-style integrity labels, Cedar or OPA policies, WebArena or WASP fixtures, OpenTelemetry evidence-to-effect spans
Artifact caveat: no public implementation repository was identified during this scan.
Implementability score: 0.55

## Supporting recent Strategy context

The 2026-07-09 scan put deterministic gates before state-changing tools and identity checks before resource acquisition. Prismata extends the same thesis to browser observation: untrusted content should not gain more visibility or capability than the current task requires.
