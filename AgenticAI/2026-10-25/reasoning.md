# AgenticAI Daily Analysis: 2026-10-25

## Freshness note

arXiv's newest agent-relevant listing is Friday, October 23. This Sunday update selects one nonduplicate implementation finding from that batch. The paper was submitted October 22, 2026 at 01:00:43 UTC and first listed October 23.

## 1. Give live code precedence when repository instructions are stale

Coding-agent instruction files carry higher prompt authority than code returned through tools. That ordering becomes dangerous when `CLAUDE.md`, `AGENTS.md`, or similar guidance has drifted from the repository.

The study built 40 Python projects with 16 kinds of conflict between instruction files and live code. Claude Code and Codex CLI completed 320 runs. Without a precedence rule, 90.1% of choices followed the stale file. Claude Code explicitly noticed the conflict in 79 of 80 runs and still followed the stale instruction. Codex CLI rewrote working code in 20 of 80 runs, and 17 of those rewrites broke the project's tests.

A single user-level rule changed the behavior: when repository documentation and existing code disagree, follow the existing code and report the inconsistency. Code-conforming choices rose from 4.2% to 91.4%, stale-file rewrites stopped, and test pass rate rose from 89.4% to 100%.

### Why it matters

Instruction files are executable control surfaces. A stale line can override direct repository evidence even when the agent correctly identifies the mismatch. Repository quality therefore needs both instruction freshness checks and an explicit conflict policy.

### Fit in the stack

This belongs in the coding-agent control plane, between repository context assembly and the first edit. It complements instruction linting: lint detects drift, while precedence policy limits damage when drift escapes detection.

### Implementable now

- add a user-level rule that live code wins when descriptive instructions conflict with established repository conventions;
- require the agent to report every detected inconsistency rather than silently choosing one source;
- test the rule with seeded `AGENTS.md` or `CLAUDE.md` drift fixtures;
- keep normative safety, approval, and scope constraints separate from descriptive code conventions, since live code must not override explicit authorization boundaries;
- use the public `WenJing95/stale-docs-data` corpus as a read-only source for designing regression cases.

Implementability score: 0.97

Core source: [Stale Instruction Files Override the Code in Coding Agents v1](https://arxiv.org/abs/2610.30571v1)

Artifact: [WenJing95/stale-docs-data](https://github.com/WenJing95/stale-docs-data), contents inspected read-only. The study is limited to 40 small Python projects, two agents, and single unattended feature tasks.
