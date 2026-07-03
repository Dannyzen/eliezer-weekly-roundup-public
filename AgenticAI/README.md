# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Friday synthesis, week ending 2026-07-03

### Coding-agent loops now have measurable economics

Summary: Semantic early stopping and TraceLab turn agent loops into measurable workload objects. Stop rules, trace capture, token accounting, tool latency, and cache behavior are now part of runtime design, not after-the-fact observability.

Analysis: [weekly reasoning analysis](2026-07-03/reasoning.md#coding-agent-loops-now-have-measurable-economics)
Durable topics: [Sessionful Agent Loops](sessionful-agent-loops/sessionful-agent-loops.md), [Agent Serving Runtime](agent-serving-runtime/agent-serving-runtime.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Context Economy](context-economy/context-economy.md)
Core sources: [Semantic Early-Stopping](https://arxiv.org/abs/2606.27009v1), [semantic-halting repo](https://github.com/SahilShrivastava-Dev/semantic-halting-problem), [TraceLab paper](https://arxiv.org/abs/2606.30560v1), [TraceLab repo](https://github.com/uw-syfi/TraceLab)
Implementable now:
- add semantic-distance early stopping to writer-critic, RAG synthesis, review, and planning loops
- record prompt length, output length, tool calls, cache-hit behavior, latency, and human gaps per step
- replay alternate stop policies over saved trajectories
- separate operational tokens from evaluation tokens
Tools, repos, and methodologies worth exploring:
- TraceLab, semantic-halting-problem, paired trajectory replay, cached judge calls, prefix-cache accounting
Implementability score: 0.88

### Repository work needs repo-level and source-only evaluation

Summary: Generated PRs and compatibility repairs need evidence at the repository level. This week tied together knowledge-based PRs, repository-level friction metrics, source-only repair checks, and practical validation after tests pass.

Analysis: [weekly reasoning analysis](2026-07-03/reasoning.md#repository-work-needs-repo-level-and-source-only-evaluation)
Durable topics: [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Ticket-Native Agent Orchestration](ticket-native-agent-orchestration/ticket-native-agent-orchestration.md)
Core sources: [Knowledge-Based Pull Requests](https://arxiv.org/abs/2606.26721v1), [Govern the Repository, Not the Agent](https://arxiv.org/abs/2606.28235v1), [RepoRescue](https://arxiv.org/abs/2607.01213v1), [Antaeus](https://arxiv.org/abs/2607.01138v1)
Implementable now:
- attach source evidence packets to generated PRs
- track review churn, merge friction, failed CI retries, and reverts by repository
- rerun repairs after removing test-file edits
- block test edits in selected benchmarks and require practical-use validation
Tools, repos, and methodologies worth exploring:
- source-only repair rules, PR evidence packets, repository-level friction dashboards, benchmark replay packets
Implementability score: 0.80

### Memory becomes bounded, ledgered, and ablatable

Summary: The memory cluster moved away from raw transcript stuffing. Temporal validity, ECHO, AutoMem, AgenticSTS, and memory-poisoning trajectory work all point toward typed memory events, visibility scopes, and ablation-ready traces.

Analysis: [weekly reasoning analysis](2026-07-03/reasoning.md#memory-becomes-bounded-ledgered-and-ablatable)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Context Economy](context-economy/context-economy.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [Temporal Validity](https://arxiv.org/abs/2606.26511v1), [ECHO](https://arxiv.org/abs/2606.31650v1), [AutoMem](https://arxiv.org/abs/2607.01224v1), [AutoMem repo](https://github.com/autoLearnMem/AutoMem), [AgenticSTS](https://arxiv.org/abs/2607.02255v1)
Implementable now:
- store memory writes as append-only events with source, validity, owner, and reason
- assemble decision prompts from typed retrieval instead of raw accumulated transcripts
- persist retrieved item IDs, memory layer IDs, skill snapshot IDs, and prompt records
- run no-store, full-history, typed-retrieval, and skill-triggered ablations
Tools, repos, and methodologies worth exploring:
- AutoMem, typed retrieval, frozen memory snapshots, condition-tagged trajectories, memory-layer ablations
Implementability score: 0.73

### Skills and tool surfaces become governed implementation artifacts

Summary: Skills, plugins, MCP servers, and lifecycle CLIs are becoming the operational substrate of agents. They need manifests, lockfiles, provenance, schema checks, and runtime reference monitors.

Analysis: [weekly reasoning analysis](2026-07-03/reasoning.md#skills-and-tool-surfaces-become-governed-implementation-artifacts)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Enterprise MCP Orchestration](enterprise-mcp-orchestration/enterprise-mcp-orchestration.md), [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Agent Discovery](agent-discovery/agent-discovery.md)
Core sources: [VIGIL](https://arxiv.org/abs/2606.26524v1), [Google agents-cli](https://github.com/google/agents-cli), [skill supply-chain manifests](https://arxiv.org/abs/2607.01136v1), [MCP Server Architecture Patterns](https://arxiv.org/abs/2606.30317v1)
Implementable now:
- add skill manifests with owner, source repo, version, dependencies, services, tools, and side effects
- lock skill versions per run
- lint tool descriptions against callable schemas
- attach runtime reference monitors to high-risk skills
Tools, repos, and methodologies worth exploring:
- agents-cli, VIGIL-style reference monitors, MCP pattern taxonomy, skill manifests, lockfiles, schema linting
Implementability score: 0.79

### Sandboxes and DevOps action boundaries move into the harness

Summary: CubeSandbox, UnderSpecBench, and HCP-style execution control make the action surface explicit. Risky agent work needs sandbox workers, target/scope schemas, deterministic side-effect oracles, and policy-wrapped tool invocation.

Analysis: [weekly reasoning analysis](2026-07-03/reasoning.md#sandboxes-and-devops-action-boundaries-move-into-the-harness)
Durable topics: [Sandbox-Native Agent Workers](sandbox-native-agent-workers/sandbox-native-agent-workers.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Strategy Agent Execution Control Plane](../Strategy/agent-execution-control-plane/agent-execution-control-plane.md)
Core sources: [CubeSandbox](https://github.com/TencentCloud/CubeSandbox), [UnderSpecBench](https://arxiv.org/abs/2607.02294v1), [HCP paper](https://arxiv.org/abs/2606.29073v1), [HCP repo](https://github.com/SymbolicLight-AGI/handle-capability-protocol)
Implementable now:
- run high-variance tasks in sandbox workers
- require target identity, scope, and blast-radius fields before DevOps actions
- split Safe Success, Wrong Target, OverScope, clarification, refusal, and deferment outcomes
- attach policy and egress checks to tool invocation
Tools, repos, and methodologies worth exploring:
- CubeSandbox, HCP, ControlArena, deterministic side-effect oracles, sandbox workers, target/scope schemas
Implementability score: 0.84

## Supporting recent AgenticAI context

The 2026-07-03 weekly synthesis replaces the daily scan as the current structured map. The durable implementation thesis is now trace-first: build replayable run records, then layer stop rules, source-only validation, bounded memory, skill manifests, and sandboxed execution around those traces.
