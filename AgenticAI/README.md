# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-12

### HyperTool moves context control into tool execution
Summary: HyperTool argues that agents waste context by unfolding deterministic tool workflows into many model-visible atomic calls. The better interface is an executable MCP-style block that calls existing tools locally, manages intermediate state, and returns only the task-relevant result.

Analysis: [daily reasoning analysis](2026-06-12/reasoning.md#hypertool-moves-context-control-into-tool-execution)
Durable topics: [Context Economy](context-economy/context-economy.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [HyperTool](https://arxiv.org/abs/2606.13663v1), [GitHub Copilot CLI LSP setup](https://github.blog/ai-and-ml/github-copilot/give-github-copilot-cli-real-code-intelligence-with-language-servers/)
Implementable now:
- build macro-tools for deterministic read-only subroutines;
- preserve original tool schemas inside the executable boundary;
- return compact outputs with source IDs and intermediate-operation logs.
Tools, repos, and methodologies worth exploring:
- MCP-style tool wrappers, language-server tools, macro-actions, trace compaction, tool-call ablation suites
Implementability score: 0.82

### Recursive agent harnesses turn subagent spawning into a harness primitive
Summary: Recursive Agent Harnesses names a practical pattern: the recursive unit is a full agent harness with filesystem, execution, planning, context, and result contracts, not a raw model call or role-play chat.

Analysis: [daily reasoning analysis](2026-06-12/reasoning.md#recursive-agent-harnesses-turn-subagent-spawning-into-a-harness-primitive)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
Core source: [Recursive Agent Harnesses](https://arxiv.org/abs/2606.13643v1)
Implementable now:
- create parent-child run manifests;
- cap recursion depth, tokens, wall-clock, tool calls, and filesystem writes;
- preserve typed child outputs and disagreement instead of flattening results.
Tools, repos, and methodologies worth exploring:
- recursive harness manifests, bounded subagent pools, parent-child traces, parallel evidence extraction, topology ablations
Implementability score: 0.69

### User corrections should compile into runtime checks
Summary: Trace shows that storing user preferences is not enough. User corrections should become atomic rules with applicability checks and runtime verifiers that gate future task completion.

Analysis: [daily reasoning analysis](2026-06-12/reasoning.md#user-corrections-should-compile-into-runtime-checks)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Skills as Control](skills-as-control/skills-as-control.md)
Core source: [Getting Better at Working With You](https://arxiv.org/abs/2606.13174v1)
Implementable now:
- mine corrections from real repeated-friction cases;
- compile applicability checks and final-state verifiers;
- store rule source, hash, last-fired date, false positives, and trace evidence.
Tools, repos, and methodologies worth exploring:
- skill-layer rule libraries, executable checks, correction-derived regression fixtures, preference-compliance dashboards
Implementability score: 0.85

## Previous structured update

The prior daily scan for 2026-06-11 focused on evented project memory, deterministic layer slices, and targeted runtime skill probes: [2026-06-11 roundup](../roundups/2026-06-11.md).
