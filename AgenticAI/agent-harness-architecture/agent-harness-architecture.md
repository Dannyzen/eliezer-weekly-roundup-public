# Agent Harness Architecture

Last updated: 2026-07-14

Agent harness architecture is becoming the part of the agent stack that teams can actually standardize.

The durable pattern across recent work is simple: the interesting engineering differences are no longer only inside the model. They sit in the non-LLM infrastructure around it: context services, tool mediation, delegation, isolation, orchestration, and safety controls. Once those choices become explicit, agent systems stop looking like prompt tricks and start looking like software architecture.

## Why this topic now

The April 2026 signal is unusually clear:
- **Architectural Design Decisions in AI Agent Harnesses** studies 70 public projects and shows that recurrent design dimensions are now visible enough to classify.
- **Microsoft Agent Framework 1.1.0** turns several of those dimensions into concrete runtime knobs: file history providers, checkpoint allowlists, hosted workflow support, and stronger execution/runtime surfaces.
- **Claude Context** shows another important trend: context handling is externalizing into installable services instead of staying buried inside one agent loop.
- **Agentic Harness Engineering (AHE)** makes the next jump: the harness is not only an architecture to inspect, it is an editable control surface that can be evolved, attributed, rolled back, and tested.

Core sources:
- Architectural Design Decisions in AI Agent Harnesses: https://arxiv.org/abs/2604.18071v1
- Microsoft Agent Framework python-1.1.0: https://github.com/microsoft/agent-framework/releases/tag/python-1.1.0
- Microsoft Agent Framework repo: https://github.com/microsoft/agent-framework
- Claude Context: https://github.com/zilliztech/claude-context
- Agentic Harness Engineering paper: https://arxiv.org/abs/2604.25850v1
- Agentic Harness Engineering repo: https://github.com/china-qijizhifeng/agentic-harness-engineering

## Deep Dive Wednesday 2026-04-29: AHE turns harness work into a falsifiable engineering loop

### Overview

Agentic Harness Engineering is the strongest agentic-stack finding this week because it moves coding-agent improvement out of prompt folklore and into an observable engineering loop. AHE keeps the base model fixed and evolves the surrounding harness: system prompt, tool descriptions, tool implementations, middleware, skills, sub-agent configuration, and long-term memory. The important claim is not merely that a benchmark score improved. The important claim is that the harness can become a versioned, inspectable, rollbackable artifact with evidence attached to every change.

AHE belongs in the harness and evaluation layer of the stack. It is about how an agent sees a repository, calls tools, preserves state, verifies work, uses middleware, and turns run history into future control-surface changes.

### Core innovation

AHE combines three observability surfaces into one loop:

1. **Component observability.** The harness is decomposed into file-level components at fixed mount points. The paper's NexAU substrate exposes seven component types: system prompt, tool description, tool implementation, middleware, skill, sub-agent configuration, and long-term memory. This gives the optimizer an explicit action space and gives operators file-level diffs and rollback.
2. **Experience observability.** Multi-million-token trajectories are distilled into layered, drill-down evidence. The optimizer reads overview reports first, then per-task details, and can still inspect raw traces when needed.
3. **Decision observability.** Every harness edit ships with a change manifest naming the failure evidence, root cause, targeted fix, expected fixes, and at-risk regressions. The next evaluation round checks those predictions against task-level deltas.

That last piece is the architectural breakthrough. A harness edit is treated as a falsifiable contract, not a clever explanation after the fact.

### Why it matters

The current coding-agent market talks as if better models, longer context, or a nicer terminal are the whole story. AHE says the operational substrate around the model is itself a learnable artifact. That matters because serious agent platforms need to know which component caused a performance change, which traces justified it, which tasks it helped, which tasks it broke, and how to revert it.

The paper reports a ten-iteration run on Terminal-Bench 2 where pass@1 rises from 69.7% to 77.0%, above the reported human-designed Codex-CLI harness at 71.9% and above prompt/playbook-style self-evolution baselines. It also reports transfer to SWE-bench-verified with the highest aggregate success and 12% fewer tokens than the seed harness. Treat those numbers as early evidence, not settled law. The durable insight is the loop shape.

### How it fits into the agentic stack

- **Harness layer:** prompts, tools, middleware, skills, sub-agents, and memory become versioned components.
- **Trace layer:** raw runs become drill-down evidence rather than transcript sludge.
- **Evaluation layer:** task outcomes are compared against predicted fixes and regressions.
- **Governance layer:** bounded write scopes, manifests, git history, rollback, and read-only verifier/model configuration constrain self-modification.
- **Developer-experience layer:** terminal agents, skills repos, and code-graph tools become useful only when their control surfaces are observable enough to improve.

### Practical tools, repos, and methodologies worth trying now

- Git-backed harness directories with component ownership for prompts, tool schemas, middleware, skills, sub-agents, and memory.
- OpenTelemetry, Langfuse, or LangSmith-style traces that record harness component versions with each run.
- A small internal replay suite modeled on Terminal-Bench or SWE-bench-verified, even if it starts with only 20 recurring tasks.
- Change manifests for harness PRs: failure evidence, root cause, targeted fix, predicted fixes, at-risk regressions, and post-run verdict.
- E2B, local containers, or other sandbox substrates so rollouts do not leak state across tasks.
- Product-shape references: Warp for terminal-native agent UX, jcode for a coding-agent harness, GitNexus for repo knowledge graphs, and skills repos for procedural control packages.

### Implementation complexity

The first 60% is very implementable. A team can version harness files, log versions per run, keep traces, write change manifests, and replay a small task set without inventing new research. The next 40% is architecture-heavy: faithful trace distillation, regression prediction, benchmark-overfit control, sandbox cost, and attribution across interacting components are all hard.

AHE's own limitations matter. The public repo notes that Agent Debugger is only partially open-sourced, the quick-start depends on private NexAU/harbor repositories, and the paper says the system is a controlled research prototype rather than a complete guardrail stack. This is a pattern to copy, not a drop-in production system.

### Implementability score

0.72

The pattern can be implemented now with ordinary engineering discipline and existing tracing, git, sandboxing, and evaluation tools. Full autonomous harness evolution is less mature because it needs robust attribution, faithful trajectory distillation, and regression-aware governance.

### Strategic implications for this stack

The agent platform moat is shifting from model access to harness operations. A product that can observe, version, replay, and improve its agent harness will learn faster than a product that only swaps frontier models. This also changes how to evaluate vendors: ask for harness diffs, trace evidence, rollback mechanics, replay suites, and predicted-effect records. If they cannot show those, they are selling agent vibes, not an operating substrate.

For this stack's product direction, the near-term opportunity is a lightweight "agent harness control plane": versioned skills and tools, run traces tied to harness commits, replay packs, and a manifest-based review loop for every scaffold change.

### Core source links

- Agentic Harness Engineering paper: https://arxiv.org/abs/2604.25850v1
- Agentic Harness Engineering repo: https://github.com/china-qijizhifeng/agentic-harness-engineering

### Useful supporting sources

- Warp: https://github.com/warpdotdev/warp
- jcode: https://github.com/1jehuang/jcode
- GitNexus: https://github.com/abhigyanpatwari/GitNexus
- Matt Pocock Skills: https://github.com/mattpocock/skills
- Awesome Codex Skills: https://github.com/ComposioHQ/awesome-codex-skills

## May 9 update: tool-schema compilation is a harness control surface

TSCG and DADL sharpen the tool-system dimension of harness architecture. Tool schemas are not neutral metadata. They consume context, shape model attention, affect tool-call accuracy, and determine whether smaller or local models can operate a large catalog. A serious harness should therefore treat tool-schema representation as a compiled artifact with benchmarks, versions, and rollback, not as copy-pasted JSON that happens to sit inside a prompt.

The practical update:
- version tool schemas and compiled representations separately from tool implementation code
- benchmark native JSON schemas against compressed or structured representations on the same tasks
- record catalog size, schema version, compression profile, and model in tool-call traces
- put schema compilation before gateway policy so both the model and the policy layer see a stable tool surface
- use declarative API descriptions for internal REST catalogs where one wrapper server per API would create operational sprawl

This makes schema compilation part of harness governance. The agent platform should know which representation caused a tool call to succeed or fail.

Sources:
- [TSCG](https://arxiv.org/abs/2605.04107)
- [SKZL-AI/tscg](https://github.com/SKZL-AI/tscg)
- [DADL](https://arxiv.org/abs/2605.05247)

## May 10 update: capability routing is escaping prompt-bloated MCP catalogs

QVeris is useful product signal for the tool-system correction that TSCG and DADL made explicit: the harness should not blindly inject every tool schema into every model turn. A discover/inspect/call/audit flow gives agents a way to search a large capability surface, inspect only candidates, execute through a deterministic interface, and preserve usage evidence without prompt-bloating the entire catalog.

The architecture lesson is broader than QVeris. A mature harness should choose the smallest sufficient tool-exposure mode for each task: native prompt schema, MCP server, CLI/subprocess call, gateway API, or human-approved manual action. The trace should record not only the final tool call but also the discovery query, candidate set, inspected schema/version, call result, cost, latency, and audit verdict.

Practical lesson:
- split large tool catalogs into discover, inspect, call, and audit phases
- compare MCP schema injection against CLI/subprocess execution on token cost, correctness, latency, and debuggability
- keep capability registries behind policy before allowing side-effecting actions
- log tool-surface version, candidate IDs, selected capability, parameters, result, and charge/effect evidence
- use schema compilation and capability routing together: compile the small active surface, not the universe of possible tools

Source:
- [QVeris Agent Toolkit](https://github.com/QVerisAI/qveris-agent-toolkit)

## May 13 update: computer-use agents need hybrid path supervision

Dedicated deep dive: [GUI-Tool Path Orchestration](../gui-tool-path-orchestration/gui-tool-path-orchestration.md)

ToolCUA and ComplexMCP update harness architecture at the action-path layer. Computer-use agents are no longer only choosing text responses or simple tool calls; they are navigating mixed GUI and API surfaces where the wrong path can be faster and still wrong. The harness therefore needs to supervise the choice between GUI actions, structured tools, verification steps, and recovery attempts.

ToolCUA's durable contribution is not just the reported 46.85% OSWorld-MCP accuracy. It is the training/eval shape: interleaved GUI-tool trajectories, switching-point supervision, and a tool-efficient path reward. ComplexMCP adds the benchmark pressure with stateful MCP sandboxes, dynamic seeds, noisy failures, and failure modes such as tool retrieval saturation, over-confidence, and strategic defeatism.

Practical lesson:
- record GUI steps, tool calls, screenshots/state observations, verification actions, path length, and recovery attempts in one trace
- compare GUI-only, tool-only, and hybrid paths on the same tasks before assuming more tools help
- evaluate large tool surfaces under stateful sandbox seeds, not only static API-call correctness
- expose path-choice metrics in the harness: when did the agent switch, what evidence justified the switch, and did tool use improve success or only shorten the trajectory
- treat CUA and OSWorld-MCP-style sandboxes as evaluation substrates first, not as permission to deploy side-effecting desktop agents immediately

Sources:
- [ToolCUA](https://arxiv.org/abs/2605.12481v1)
- [ToolCUA project](https://x-plug.github.io/ToolCUA/)
- [X-PLUG/ToolCUA](https://github.com/X-PLUG/ToolCUA)
- [X-PLUG/OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)
- [ComplexMCP](https://arxiv.org/abs/2605.10787v1)
- [trycua/cua](https://github.com/trycua/cua)

## May 14 update: agent workflows need compile-time profiling and credit assignment

FlowCompile and CANTANTE update harness architecture at the workflow-optimization layer. A structured agent workflow should not be a hand-waved graph of subagents. It should be a profiled artifact with model choices, reasoning budgets, tool exposure, latency, cost, and expected quality trade-offs attached to each node and to the whole graph.

FlowCompile's useful move is compile-time exploration: profile subagent configurations and compose those measurements into reusable workflow-level trade-off sets before deployment. CANTANTE's useful move is local credit assignment: contrast joint rollouts on the same query so a system-level score can become per-agent update signals. GitHub's token-efficiency work shows the production counterpart: log token usage, prune unused MCP tools, move deterministic metadata fetches into CLI setup steps, and normalize costs with Effective Tokens.

Practical lesson:
- collect per-node token, latency, model, cache, tool, and output-quality telemetry
- profile small/medium/large model options and reasoning budgets before runtime
- maintain a reusable workflow Pareto frontier instead of ad hoc routing rules
- prefetch deterministic context through CLI/API steps rather than LLM tool loops
- attribute wins and regressions to local subagent/workflow components where possible
- version workflow profiles as deployable harness artifacts with rollback

Sources:
- [FlowCompile](https://arxiv.org/abs/2605.13647)
- [CANTANTE](https://arxiv.org/abs/2605.13295)
- [GitHub token efficiency in agentic workflows](https://github.blog/ai-and-ml/github-copilot/improving-token-efficiency-in-github-agentic-workflows/)
- [GitHub Agentic Workflows weekly update](https://github.github.com/gh-aw/blog/2026-05-11-weekly-update/)

## May 20 update: SDB makes the action boundary explicit

The production-runtime-patterns paper and companion repository add a useful missing primitive to harness architecture: the stochastic-deterministic boundary. Every material action should be modeled as proposer -> verifier -> commit -> reject signal. That is more useful than arguing about agent frameworks because it identifies where model output stops being suggestion and starts becoming system state.

This updates the harness thesis in three ways:
- side-effecting tools should not be raw model-to-action pipes;
- orchestration patterns should be selected by task horizon and state durability, not by framework popularity;
- rejection signals are runtime evidence and should be preserved for retries, audits, and harness patches.

Practical lesson:
- make every side-effecting tool expose a verifier and explicit commit step
- keep reject reasons structured enough for retry and postmortem analysis
- map long-horizon agents onto shared state machines or event logs before adding subagents
- use saga compensation for parallel branches that may partially succeed
- bind human approval to the same SDB contract instead of treating it as an out-of-band chat instruction

Sources:
- [A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents](https://arxiv.org/abs/2605.20173v1)
- [Runtime Architecture Patterns for Agents in Production](https://github.com/vasundras/agent-runtime-patterns)

## May 21 update: web agents should compile action programs

Agent JIT Compilation updates harness architecture at the browser-action layer. The old loop is fetch screenshot -> ask model -> execute one action -> fetch screenshot again. That is simple, slow, and easy to break. The better shape is compiler-like: generate candidate plans, validate them against tool/state constraints, estimate cost, schedule independent work, execute under invariants, and record rejection reasons.

This directly complements the May 20 stochastic-deterministic-boundary update. The compiled plan is still stochastic output until it passes deterministic validation. Preconditions and postconditions are the boundary between model proposal and real browser action.

Practical lesson:
- define browser/API tools with preconditions, postconditions, and observable state checks;
- generate multi-step candidate plans before executing side effects;
- estimate latency and parallelize independent reads or tab work;
- preserve invalid-plan rejection reasons as replay and training data;
- treat browser-agent serving engines like BLAST as harness infrastructure, not just demos.

Sources:
- [Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling](https://arxiv.org/abs/2605.21470v1)
- [stanford-mast/blast](https://github.com/stanford-mast/blast)

## May 22 update: event logs and interface harnesses make control explicit
ActiveGraph and Life-Harness update harness architecture from two sides. ActiveGraph says the durable runtime should be event-sourced: model calls, tool responses, object mutations, relations, policies, failures, and final artifacts should become replayable events. Life-Harness says many deterministic-agent gains come from fixing the model-environment interface: contracts, procedural skills, action realization, and trajectory regulation.

The shared lesson is that the harness is the control surface. The model is not the only thing that learns or improves. The runtime can preserve causality, replay a run, fork a hypothesis, and patch interface failures without changing model weights.

Practical lesson:
- record agent runs as append-only events, not only transcripts;
- project claims, tasks, evidence, artifacts, tool calls, and policy decisions into a graph or structured state view;
- make replay and fork/diff a harness primitive for at least one critical workflow;
- mine failed traces for environment-contract, action-realization, termination, and recovery failures;
- convert recurring failures into versioned harness interventions with predicted effects and regression risks;
- test harness interventions across models before attributing improvements to model-specific prompting.

Sources:
- [The Log is the Agent](https://arxiv.org/abs/2605.21997)
- [yoheinakajima/activegraph](https://github.com/yoheinakajima/activegraph)
- [ActiveGraph site](https://activegraph.ai/)
- [Adapting the Interface, Not the Model](https://arxiv.org/abs/2605.22166)
- [Event-Sourced Agent Runtime](../event-sourced-agent-runtime/event-sourced-agent-runtime.md)

## June 22 update: production agent frameworks are becoming service-language infrastructure

Google ADK and tRPC-Agent-Go update the harness architecture thesis from the implementation side. Agent frameworks are starting to look less like demo scaffolds and more like ordinary service runtimes: graph workflows, typed tasks, sessions, memory services, tool calls, human pauses, cancellation, evaluation hooks, and OpenTelemetry-style observability.

The durable lesson is to evaluate frameworks by their control surfaces, not their agent branding. A service team should be able to inspect where state lives, how graph topology is reviewed, how tool calls are traced, how retries and HITL pauses are represented, and how the runtime deploys inside existing platform standards.

Practical lesson:
- choose a framework by service ownership, trace coverage, workflow typing, cancellation behavior, and deployment fit;
- keep graph workflow definitions in code review;
- require session, memory, tool, model, retry, and cancellation metadata in traces;
- test task delegation and human approval as workflow nodes instead of side-channel chat messages;
- compare Python, Go, and Java surfaces on the same small replay suite before standardizing.

Sources:
- [ADK docs](https://adk.dev/)
- [google/adk-python](https://github.com/google/adk-python)
- [google/adk-go](https://github.com/google/adk-go)
- [google/adk-java](https://github.com/google/adk-java)
- [tRPC-Agent-Go](https://github.com/trpc-group/trpc-agent-go)

## Core thesis

The wrong question is "which agent framework is best?"

The right questions are:
- how does it manage context over long-running work?
- how are tool boundaries declared and governed?
- what isolation or sandbox model exists for risky execution?
- how does it represent subagents and orchestration?
- what evidence does it preserve for replay, audit, and debugging?

If those questions are ignored, teams end up comparing demos instead of systems.

## The five design dimensions that matter

### 1. Subagent architecture
How does the system delegate?

Useful distinctions:
- flat tool-call loops
- hierarchical subagents
- mixed graph-and-agent patterns
- explicit handoff semantics versus ad hoc nested prompts

### 2. Context management
How does state persist and return?

Useful distinctions:
- ephemeral transcript-only context
- file-persistent context
- hybrid context that mixes transcript, files, and structured state
- hierarchical context services with explicit scopes

### 3. Tool systems
How are actions exposed?

Useful distinctions:
- registry-oriented tool catalogs
- MCP-based external tool surfaces
- plugin architectures
- typed versus loosely structured tool interfaces

### 4. Safety mechanisms
Where does control enter the execution path?

Useful distinctions:
- sandbox level
- policy mediation points
- approval gates
- checkpoint restore controls
- auditability of memory, tools, and handoffs

### 5. Orchestration
How is work sequenced?

Useful distinctions:
- prompt-loop orchestration
- workflow graphs
- event-driven orchestration
- resumable execution with checkpoints and replay

## What the recent evidence says

The 70-project harness survey surfaces several regularities that are likely to persist:
- file-persistent, hybrid, and hierarchical context strategies are common in serious systems
- registry-oriented tool systems still dominate, but MCP and plugin extensions are clearly rising
- deeper coordination tends to pair with more explicit context services
- stronger execution environments tend to pair with more structured governance
- intermediate isolation is common, but high-assurance audit is still rare

That last point matters. Many projects have some containment. Very few have governance strong enough to satisfy real operational scrutiny.

## What to build now

### Compare harnesses with a scorecard
Do not choose a framework by vibe.

Score at least these dimensions:
- context persistence model
- tool registration model
- isolation model
- checkpoint and restore policy
- replay and trace quality
- orchestration flexibility

### Treat context as infrastructure
For long-running work, default to:
- file-persistent or hybrid context
- explicit scope boundaries
- structured retrieval or history providers
- clear rules for what becomes durable

### Make tool boundaries governable
A tool system should be legible enough that policy can sit in front of it.

Minimum expectations:
- explicit registration
- typed arguments
- per-tool permissions or policy hooks
- observable tool-call traces

### Bring restore paths under policy
Checkpoint restore is a privileged operation.

Build with:
- type allowlists
- migration rules
- replay visibility
- failure modes that are obvious when state cannot be restored safely

### Separate retrieval services from the core agent loop
External context services and code search surfaces can be a feature, not a smell, when they are inspectable and permissioned.

## What to avoid

Avoid these traps:
- hiding long-term context in one growing transcript buffer
- mixing every tool into one undifferentiated omnipotent catalog
- treating MCP adoption as a substitute for architecture
- assuming sandboxing is binary instead of graded
- restoring opaque checkpoint state without explicit type controls
- shipping multi-agent delegation without replayable evidence

## New April 2026 additions

### Architectural regularities are finally visible
The harness survey is strategically important because it makes agent-system engineering comparable across projects. Five dimensions recur often enough that the field can stop pretending every framework is sui generis.

### Releases are turning those regularities into knobs
Microsoft Agent Framework 1.1.0 is useful because it turns survey dimensions into concrete product surfaces: file history providers, checkpoint allowlists, hosted workflow support, and stronger runtime integrations. The architecture is leaving the whitepaper and entering the runtime.

### Context services are externalizing
Claude Context is good category signal because it treats code retrieval as an installable service rather than a hidden prompt trick. That is the right shape. Context should increasingly look like governed infrastructure.

### Delegation needs contextual calibration, not static role cards
CADMAS-CTX sharpens the subagent point. The same agent can be strong on short edits and weak on long-horizon debugging, so a single global skill label is too blunt. The paper's practical move is to keep per-context capability posteriors and route with an uncertainty penalty. That is a better harness pattern than hard-coded specialist identities or static skill scores.

Practical lesson:
- delegation should depend on context buckets and observed outcomes
- sparse evidence should reduce routing confidence instead of being averaged away
- harnesses need delegation telemetry good enough to learn from comparable situations, not just final task pass rates

Source:
- [CADMAS-CTX](https://arxiv.org/abs/2604.17950)

### Observability-driven harness evolution turns edits into falsifiable contracts
AHE adds the missing improvement loop for this topic. Harnesses should be represented as editable, file-level components; long trajectories should be distilled into layered evidence; and every harness edit should carry a predicted effect that is checked after the next run.

The practical lesson is blunt:
- store harness components as versioned files
- log the component version set with every agent run
- summarize trajectories into evidence that preserves tool calls, failures, patches, and tests
- require harness-edit PRs to declare predicted effects
- replay task suites before adopting scaffold changes

This makes harness engineering falsifiable instead of anecdotal. The exact AHE benchmark numbers will need independent replication, but the control pattern is immediately useful.

Source:
- [Agentic Harness Engineering](https://arxiv.org/abs/2604.25850v1)


### May 2 update: orchestration has to beat a prompt-only baseline

The in-context prompting paper is a useful corrective to framework enthusiasm. For bounded procedural conversations, the paper reports that a complete system-prompt procedure beat a LangGraph orchestrator using the same model across travel booking, Zoom support, and insurance claims. The orchestrated condition needed more calls and introduced routing/state-management failures the prompt-only baseline avoided.

This does not invalidate orchestration. It clarifies the selection rule. External orchestration earns its keep when the workflow needs durable state, external tools, approvals, parallelism, recovery, policy gates, or audit evidence. If the workflow is mainly conversational and the procedure is stable enough to fit in context, the baseline should be a full-procedure prompt plus evaluation harness.

Practical lesson:
- require a prompt-only baseline before adopting graph orchestration for procedural workflows
- measure call count, latency, cost, failure mode, and user/task quality
- reserve graphs for workflows where state boundaries, tool authority, recovery, or auditability matter
- treat orchestration as architecture, not ceremony

Source:
- [In-Context Prompting Obsoletes Agent Orchestration for Procedural Tasks](https://arxiv.org/abs/2604.27891)

### May 3 update: coding agents need deterministic software-process authority

TDD Governance and CI-Repair-Bench sharpen the harness layer from two sides. TDD Governance argues that Red-Green-Refactor should be encoded as prompt-level and workflow-level governance, with phase ordering, bounded repair loops, validation gates, and atomic mutation control enforced by a deterministic engine. CI-Repair-Bench supplies the evaluation pressure: real CI failures are repository-level, workflow-level, and often non-code; the best LLM reaches only 18.9% repair success when correctness is judged by full original GitHub Actions re-execution.

The practical lesson is blunt:
- let the model propose, but let the harness authorize phase transitions and file mutations
- make tests and CI gates authoritative instead of optional context
- cap repair loops and preserve failed attempts as evidence
- classify CI failures by type before asking a model to repair them
- replay the project’s real validation path wherever feasible

This is the reliable coding-agent product shape: a state machine around the model, not a motivational system prompt asking it to be disciplined.

Sources:
- [TDD Governance for Multi-Agent Code Generation](https://arxiv.org/abs/2604.26615)
- [CI-Repair-Bench](https://arxiv.org/abs/2604.27148)

### May 4 update: orchestration granularity should be quality-gated

Agent Capsules adds a useful control rule for multi-agent pipelines: execution granularity should be selected at runtime under empirical quality constraints. The paper and code artifact show a controller that measures coordination overhead, dependency shape, tool-call rate, and rolling quality, then chooses whether a group should run as separate agents or as a compound call. If quality drops, the runtime escalates or falls back to fine-grained execution.

The practical lesson is not to replace every graph with a merged prompt. It is to make the graph elastic:
- instrument each pipeline group with cost, latency, call count, tool use, dependency depth, and quality
- compare prompt-only, fine-grained, and compound baselines
- allow compound execution only where the rolling quality floor holds
- preserve fallback when tools, permissions, or output quality degrade
- treat orchestration overhead as a measured systems property, not a vibe

This extends the May 2 prompt-baseline lesson. Orchestration earns its keep only when it improves measured outcomes or governance; otherwise it should collapse to a simpler execution shape.

Sources:
- [Agent Capsules](https://arxiv.org/abs/2605.00410v1)
- [agent-capsules repo](https://github.com/aray-17/agent-capsules)

### May 5 update: orchestration traces are the substrate for training and governance

Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces gives the harness layer a practical next artifact: a typed event graph for spawn, delegate, message, tool, return, aggregate, and stop decisions. The paper's most useful contribution is not a drop-in RL recipe. It is the claim that multi-agent learning, debugging, and governance need replayable orchestration traces before they need more swarm abstractions.

The practical lesson:
- record orchestration events as structured data, not only transcript text
- preserve parent/child IDs, timestamps, permissions, model, tool, cost, latency, and outcome
- make stop decisions explicit and include stop reasons
- compute simple rewards for duplicate work, failed delegation, poor aggregation, cost, and latency before attempting RL
- replay historical traces to test orchestration-policy changes

This pairs with Agent Capsules. Granularity control needs measured traces; RL over orchestration needs the same traces. The harness should own the event graph.

Sources:
- [Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces](https://arxiv.org/abs/2605.02801v1)
- [awesome-llm-mas-rl](https://github.com/xxzcc/awesome-llm-mas-rl)

### May 7 update: selective delegation beats static agent routing

Uno-Orchestra adds a clean orchestration rule: delegation should be selective and evidence-driven. A multi-agent harness should decide whether to decompose a task and which model/primitive pair should handle each subtask under one cost-quality objective. Static specialist role cards and automatic fan-out are too expensive and too hard to debug.

This extends the recent Agent Capsules and orchestration-trace updates. Granularity control, RL over orchestration, and selective delegation all need the same substrate: structured traces of task features, decomposition choices, worker/model choices, cost, latency, quality, handoffs, and outcomes.

Practical lesson:
- build prompt-only and single-agent baselines before adding subagents
- log every delegation decision with cost, latency, selected worker, rejected workers, and outcome
- start with rules or bandits before training an RL delegation policy
- penalize duplicate work, failed handoffs, low-value aggregation, and unnecessary fan-out in offline replay
- let orchestration collapse to the simpler path when decomposition does not clear a quality threshold

Source:
- [Uno-Orchestra](https://arxiv.org/abs/2605.05007)

### May 8 update: recursive and adaptive teams need delegation ledgers

Recursive Agent Optimization and LATTE extend the week's orchestration theme. RAO explores recursive agents that spawn and delegate to new instantiations of themselves. LATTE coordinates teams through an evolving task graph that tracks subtask dependencies, assignments, and progress state. Both are useful research signals, but the implementable lesson is simpler: before learning recursive delegation, the harness needs a delegation ledger.

Practical lesson:
- record spawn, delegate, message, tool, file-touch, return, aggregate, and stop events as structured data
- preserve parent/child IDs, selected worker/model, transferred context, permissions, task owner, dependency, status, evidence path, and conflict state
- track token cost, wall time, duplicate work, failed handoffs, file conflicts, and final quality for every delegation strategy
- compare single-agent, prompt-only, static-team, adaptive-team, and recursive-team baselines before adding recursion
- start with deterministic task-graph rules and conflict locks before attempting RL over recursive delegation

This makes multi-agent improvement falsifiable. A learned recursive policy without a task graph and replayable delegation evidence is just a more expensive swarm.

Sources:
- [Recursive Agent Optimization](https://arxiv.org/abs/2605.06639)
- [Improving the Efficiency of Language Agent Teams with Adaptive Task Graphs](https://arxiv.org/abs/2605.06320)

## May 15 update: agent runtimes need environment substrates and async tool scheduling

Orchard and AsyncFC update harness architecture below the visible agent loop. Orchard says agent training needs a reusable environment substrate: sandbox lifecycle primitives, trajectory capture, verification outcomes, and recipes that can feed SFT/RL/evaluation across coding, GUI, and assistant tasks. AsyncFC says tool use should not be forced through synchronous blocking semantics when dependencies permit overlap.

Together they push the harness from "prompt plus tools" toward an execution substrate:
- an environment layer that can reset, observe, act, snapshot, verify, and teardown;
- a trajectory layer that preserves successful rollouts and productive failed segments;
- a scheduler layer that can return symbolic futures, continue decoding, and await concrete results only when needed;
- a dependency layer that records read/write resource sets for safe tool parallelism;
- an observability layer that ties environment state, tool futures, latency, cost, and verification results to the same trace.

Practical lesson:
- define a small environment API before accumulating one-off sandbox wrappers
- store trajectories with enough state to replay, score, and train from them
- start async tool calls conservatively by overlapping model decoding with serialized execution
- add read/write annotations only for tools where resource boundaries are clear
- track which speedups preserve accuracy rather than celebrating wall-clock gains alone
- treat paused or unstable public datasets as watch items until their release status is clear

Sources:
- [Orchard](https://arxiv.org/abs/2605.15040v1)
- [microsoft/Orchard dataset](https://huggingface.co/datasets/microsoft/Orchard)
- [AsyncFC](https://arxiv.org/abs/2605.15077v1)

## May 23 update: source-level and workflow-placement changes need stronger harness gates

MOSS, GraphFlow, and workflow compilation extend the harness topic below prompt engineering. MOSS says recurring structural failures sometimes require source-level changes, not new prompts or skills. GraphFlow says reusable workflow graphs can serve task-specific flows and manage KV-cache state more efficiently. The workflow-compilation paper says stable procedural workflows may belong in small fine-tuned models rather than repeated external orchestration.

The durable lesson is a placement rule. The harness should decide where control logic lives: prompt, graph, gateway, source code, or weights. That decision needs evidence, not framework taste.

Practical lesson:
- source-level self-evolution needs failure-batch replay, isolated candidate images, predicted-effect manifests, consent gates, health probes, and rollback;
- workflow graphs need typed atomic operations, state ownership, cache policy, and per-node traces;
- stable workflow compilation needs prompt-only and graph-orchestrated baselines before fine-tuning;
- do not compile workflows into weights when approval logic, auditability, or policy change frequency matters;
- record workflow placement, model, graph/source version, cost, latency, and failure mode in every trace.

Sources:
- [MOSS](https://arxiv.org/abs/2605.22794v1)
- [GraphFlow](https://arxiv.org/abs/2605.22566v1)
- [Compiling Agentic Workflows into LLM Weights](https://arxiv.org/abs/2605.22502v1)

## May 25 update: operations agents need falsifiable measurement substrates

The agentic Kubernetes measurement paper adds the operations version of harness discipline. Autonomous ops-agent claims should not be accepted from anecdotes or curated demos. They need controlled fault injection, agent-disabled baselines, ground-truth scoring, and outcome-labeled `(state, action, outcome)` tuples.

This matters because code agents already have a fast falsification substrate: tests. Operations agents usually do not. A serious ops harness should therefore create one:
- disposable or staging environments;
- injected faults with known ground truth;
- separate scores for diagnosis, action correctness, recovery, and side effects;
- agent-disabled and simple-script baselines;
- trace-linked state/action/outcome records;
- replay packs for regression.

The durable architecture lesson is that agent harnesses need environment-specific falsification surfaces. Browser agents need screenshots and DOM state. Coding agents need tests and diffs. Ops agents need controlled incidents and recovery evidence.

Sources:
- [A measurement substrate for agentic Kubernetes operations](https://arxiv.org/abs/2605.23058)
- [odmarkj/agent-breakage](https://github.com/odmarkj/agent-breakage)

## May 28 update: harnesses are moving into incident response and pytest-native red teams

ITBench-AA and RAMPART show the harness layer getting more operational. ITBench-AA tests agentic enterprise IT work through SRE-style Kubernetes incident response: read logs, trace dependencies, and identify root-cause entities in live-style infrastructure. The reported frontier-model ceiling remains below 50%, which makes it a useful unsaturated benchmark rather than another polished leaderboard.

RAMPART is the complementary builder primitive: a pytest-native framework for agentic safety and security tests covering adversarial attacks, benign failures, harm categories, and assertion-driven evaluation. This matters because agent testing should live next to normal software tests, not only in a separate eval dashboard.

Practical lesson:
- turn real incidents into read-only fixtures with logs, dependency graphs, fault injections, and known root causes;
- encode agent safety and security expectations as pytest assertions;
- log false positives, turn count, tool count, latency, cost, and root-cause accuracy;
- gate write-capable ops agents behind incident-diagnosis performance first;
- keep benign-failure tests alongside adversarial tests because production breaks are often not attacks.

Sources:
- [ITBench-AA](https://huggingface.co/blog/ibm-research/itbench-aa)
- [microsoft/RAMPART](https://github.com/microsoft/RAMPART)
- [RAMPART on PyPI](https://pypi.org/project/RAMPART/)

## May 29 update: spec reasoning belongs before code generation

SpecBench updates harness architecture at the requirements layer. Most coding-agent benchmarks hand the agent a fixed implementation task and then grade the patch. That misses a high-value engineering skill: recognizing that the task specification is incomplete, ambiguous, contradictory, or unsafe to implement without review.

The practical harness correction is to add a pre-code stage. Before editing files, the agent should identify missing requirements, contradictory constraints, undefined acceptance criteria, non-functional risks, and project-history conflicts. That output should be scored and either accepted, revised, or explicitly waived before implementation starts.

Practical lesson:
- build spec-review fixtures from RFCs, ADRs, issue threads, and postmortems;
- require the agent to produce omissions, ambiguities, contradictions, risks, and acceptance-test gaps before code edits;
- score spec critique separately from final patch success;
- preserve the spec-review artifact in the same trace as implementation and tests;
- block high-risk implementation when the spec gate fails instead of relying on better code generation.

Source:
- [SpecBench](https://arxiv.org/abs/2605.30314)

## May 30 update: real-session misalignment labels belong in coding-agent traces

The large-scale coding-agent misalignment study adds a missing harness primitive: labels for how an agent failed in the user’s real workflow. The useful unit is not only pass/fail on a patch. It is failure form, cause, cost, resolution, and whether the user had to correct the agent.

The physicist-supervised scientific-software case study adds the oracle-test warning. An agent can pass a fiducial test while optimizing the wrong architecture or adding an unphysical numerical patch. Harnesses therefore need non-fiducial tests, shared changelogs, and explicit rules against symptom-fitting when the task has domain constraints.

Practical lesson:
- label project-reading failure, intent drift, rule violation, action overreach, execution error, inaccurate self-reporting, and user-correction burden;
- preserve user corrections as replay fixtures and regression data;
- require agents to cite project-reading evidence before edits;
- test across parameter/diversity slices instead of only a fiducial oracle case;
- keep session changelogs so repeated loops and stalled architectural exploration are visible.

Sources:
- [How Coding Agents Fail Their Users](https://arxiv.org/abs/2605.29442v1)
- [Physics Is All You Need?](https://arxiv.org/abs/2605.30353v1)
- [MinhMPA/clax-pt](https://github.com/MinhMPA/clax-pt)


## May 31 update: agent evals need soundness gates and versioned failure fixtures

SoundnessBench and AWS’s AgentCore/LangSmith evaluation posts converge on the same harness lesson: agent evaluation has to happen before and after action. Before action, proposal-stage gates should catch weak research ideas, bad experimental designs, missing baselines, and plausible-looking confounds. After action, production failures should become versioned fixtures with trajectory, assertion, and outcome checks.

The SoundnessBench result is especially useful for AI-scientist and research-agent harnesses because it names optimism bias as a measurable failure. The AWS posts are the implementable counterpart: predefined scenarios for locked regression gates, user-simulation scenarios for exploration, multiple trials for nondeterminism, complete transcripts for debugging, and final environment outcomes for truth.

Practical lesson:
- add a pre-expense soundness gate for research, benchmark, and experiment proposals;
- track false-positive optimism and false-negative rejection separately;
- promote production failures into immutable fixture versions with expected tool paths, assertions, and final-state checks;
- keep simulated-user scenarios in the discovery loop, then lock useful failures into the release gate;
- grade trajectory, final answer, and environment outcome separately;
- record model version, harness commit, grader version, dataset version, and trace ID with every eval run.

Sources:
- [SoundnessBench](https://arxiv.org/abs/2605.30329v1)
- [SoundnessBench project](https://hosytuyen.github.io/projects/SoundnessBench)
- [Build a test suite that grows with your agent with dataset management in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/build-a-test-suite-that-grows-with-your-agent-with-dataset-management-in-amazon-bedrock-agentcore/)
- [Evaluating Deep Agents using LangSmith on AWS](https://aws.amazon.com/blogs/machine-learning/evaluating-deep-agents-using-langsmith-on-aws/)

## June 4 update: long-horizon R&E agents need artifact-loop benchmarks

AutoLab moves agent harness design toward the loop that real research and engineering agents must run: propose a change, edit an artifact, run experiments, measure outcomes, and keep improving. That is more useful than another one-shot answer benchmark because it exposes budget drift, bad stopping criteria, weak experiment design, fragile measurement, and artifact-state mistakes.

The implementation lesson is to make the artifact loop explicit. A serious harness should preserve patch IDs, commands, metric deltas, failed attempts, wall-clock time, token spend, and stopping decisions. If a model improves the artifact but burns an unlimited loop to do it, that is not the same capability as an agent that improves it under bounded time, budget, and authority.

Practical lesson:
- build internal artifact-loop fixtures around repo tasks, benchmark tuning, and infra optimization;
- require experiment plans, patch IDs, commands, result summaries, failed attempts, and stopping reasons;
- score improvement per dollar, tool call, and wall-clock minute;
- record loop budgets, allowed mutation scope, and evaluation versions in the trace;
- treat public benchmark execution as a manual next step until running external code is explicitly approved.

Sources:
- [AutoLab](https://arxiv.org/abs/2606.05080)
- [autolabhq/autolab](https://github.com/autolabhq/autolab)
- [AutoLab project site](https://autolab.moe/)

## June 6 update: tool exposure should be a causal frontier

ToolChoiceConfusion sharpens the tool-system layer of harness architecture. The core correction is simple: semantic relevance is too weak for tool exposure. A tool may be related to the user goal while still being unnecessary, premature, or dangerous at the current state. Causal Minimal Tool Filtering uses lightweight precondition-effect contracts to expose only the minimal next-step frontier.

That is an implementable harness primitive. The system should know current state, goal, tool preconditions, expected effects, and risk class before showing full schemas to the model. Tool gating then becomes auditable state transition logic instead of prompt-space search.

Practical lesson:
- attach precondition and effect contracts to non-trivial tools;
- compute visible tools from current state and next admissible transitions;
- log hidden tools, exposed tools, selected tools, wrong-tool calls, premature actions, and token cost;
- add regression fixtures where semantically related tools should remain hidden until a precondition is satisfied;
- treat the active tool surface as a versioned harness artifact.

Source:
- [ToolChoiceConfusion](https://arxiv.org/abs/2606.06284v1)

## June 7 update: failed trajectories should repair the harness layer that broke

From Failed Trajectories to Reliable LLM Agents adds the missing repair loop to harness architecture. A failed final answer is not enough evidence. The harness owns the execution environment, tool interfaces, context package, lifecycle rules, observability, verification, and governance surface, so a failure should be attributed to the layer that actually broke.

The practical correction is to make failed runs replayable before prompt mutation. If a tool schema hid a side effect, patch the tool contract. If the verifier missed a final-state check, patch the verifier. If context routing omitted the decisive evidence, patch context assembly. If lifecycle orchestration retried or stopped at the wrong point, patch the lifecycle rule. The prompt may still be wrong, but it should not be the only thing allowed to change.

Practical lesson:
- store trace IR with task state, tool calls, observations, verifier outputs, lifecycle events, environment transitions, and policy decisions;
- replay failed trajectories before prompt edits;
- label failures by harness layer: tool-contract, context, lifecycle, verifier, environment, policy, or model;
- promote repaired failures into regression fixtures with expected trace and outcome;
- track which repair class actually improved future reliability.

Source:
- [From Failed Trajectories to Reliable LLM Agents](https://arxiv.org/abs/2606.06324v1)

## June 9 update: OpenEnv makes agentic RL environments a harness interface

OpenEnv turns environment design into a harness contract. The useful move is not another agent framework. It is a common interface between harness, environment, and trainer, with Gymnasium-style `reset`, `step`, and `state`, client/server deployment, HTTP/WebSocket transport, Docker packaging, and MCP compatibility.

That matters because open-source agent training needs comparable task surfaces. If every harness has a private environment adapter, models learn the harness instead of the task. A shared socket lets teams vary the model, trainer, reward library, and infrastructure while holding the environment contract stable.

Practical lesson:
- wrap internal tasks as environment contracts before trying to train on them;
- keep reward definition and trainer logic outside the environment interface;
- make MCP servers and environment actions consistent between train/eval and production modes;
- attach tasksets to datasets so environments and benchmark cases compose;
- auto-validate environment quality before treating it as a learning signal.

Sources:
- [The Open Source Community is backing OpenEnv for Agentic RL](https://huggingface.co/blog/openenv-agentic-rl)
- [huggingface/OpenEnv](https://github.com/huggingface/OpenEnv)


## June 11 update: deterministic scaffold slices should gate agent changes

Layer-Isolated Evaluation adds a practical CI pattern to harness architecture. Instead of relying only on end-to-end agent success, decompose the deterministic scaffold into layers: ontology or state normalization, intent, routing, decomposition, escalation, safety, memory, and envelope/defense. Each layer gets a no-LLM assertion slice against a locked baseline.

The important result is masking. A local scaffold regression may barely move the aggregate pass rate while the relevant slice collapses. That means aggregate dashboards are too slow and too vague for scaffold changes.

Practical lesson:
- write pure deterministic tests for routing, memory, safety, verifier, lifecycle, and tool-boundary code;
- run those slices before expensive model-in-the-loop evals;
- report which layer failed, not only whether the whole agent failed;
- use controlled regression injection to validate that each slice localizes the failure it claims to catch;
- bind layer-test version and harness commit into every agent release record.

Source:
- [Layer-Isolated Evaluation](https://arxiv.org/abs/2606.11686v1)

## June 12 update: recursive harness spawning needs manifests and budgets

Recursive Agent Harnesses makes subagent spawning a harness primitive. The recursive unit is a full agent harness with tools, workspace, planning, context, and result contract, not a raw model call. That is powerful because it lets a parent split large context or file-batch tasks into bounded child runs. It is risky because recursive harnesses can multiply spend, writes, and authority if the runtime treats them as ordinary tool calls.

Practical lesson:
- require a parent-child run manifest before spawning: depth, budget, workspace, tool scope, model, and output schema;
- fan out only when the task has independent work units and a typed aggregation rule;
- cap recursion depth, wall-clock, tool calls, token spend, and filesystem writes;
- preserve parent-child trace links, child evidence, and disagreement at aggregation time;
- compare recursive harnesses against matched single-agent and naive multi-agent baselines before deploying them.

Source:
- [Recursive Agent Harnesses](https://arxiv.org/abs/2606.13643v1)

## June 15 update: harnesses need typed foundries and component interfaces

HarnessX and AgentSpec extend the harness thesis from replayable scaffolds into typed component systems. HarnessX treats the harness as prompts, tools, memory, and control flow assembled from typed primitives, then adapted through trace-driven evolution. AgentSpec applies the same discipline to embodied agents by standardizing component interfaces for perception, memory, reasoning, reflection, action, and optional learning.

The practical correction is to stop treating the harness as one prompt-shaped blob. A real harness should expose component boundaries, version each component, trace which version ran, and allow controlled one-component swaps before bigger architecture changes.

Practical lesson:
- define internal harness interfaces for perception, context, memory, tool selection, action, verification, and final answer;
- log component version, config, and input/output schema with every run;
- replay the same tasks with one component changed at a time;
- require harness patches to cite failed trace evidence, expected fix, and regression risk;
- keep autonomous harness evolution behind review until attribution, rollback, and eval coverage are strong.

Sources:
- [HarnessX](https://arxiv.org/abs/2606.14249v1)
- [AgentSpec](https://arxiv.org/abs/2606.14674v1)

## June 17 update: skill routing and test oracles are harness gates

Compositional Skill Routing and All Smoke, No Alarm both push harness architecture toward explicit pre-action gates. A skill-capable harness should not just retrieve a plausible skill and proceed. It should decompose the task, select skills, compose a dependency-aware plan, and record validators for the resulting artifact. A coding-agent harness should not accept "tests were added" as verification. It should inspect whether the tests contain real oracle signals.

This makes two harness components first-class:
1. **Skill planner:** task decomposition, skill retrieval, DAG composition, dependency checking, and loaded-skill hash logging.
2. **Verification oracle gate:** test-oracle classification, mutation/property checks where practical, and CI failure for smoke-only agent tests.

Practical lesson:
- make skill decomposition output a versioned harness artifact;
- store selected skill IDs, body hashes, dependency edges, and expected validators in the trace;
- run no-skill and wrong-skill baselines for high-value harness skills;
- classify agent-authored tests by assertion, expected output, property, mutation-kill potential, and self-mocking risk;
- block merge or task completion when tests only execute code without checking behavior.

Sources:
- [Compositional Skill Routing](https://arxiv.org/abs/2606.18051v1)
- [A Framework for Evaluating Agentic Skills at Scale](https://arxiv.org/abs/2606.17819v1)
- [All Smoke, No Alarm](https://arxiv.org/abs/2606.18168v1)

## June 23 update: coding harnesses need process rubrics, not only tests

RigorBench adds a harness-level quality gate this topic needed. A coding-agent harness should not be judged only by the final diff or final test result. It should expose whether the agent planned before mutation, verified its own work, recovered from errors without thrashing, abstained when context was insufficient, and preserved atomic step integrity.

GroundEval adds the evidence-path version of the same correction. The harness has to keep enough trace structure to prove which artifact supported the final claim or patch rationale.

Practical lesson:
- make plan-before-mutation a harness event;
- log verifier runs and skipped-verifier reasons;
- detect repeated failed fixes and tool thrashing as process failures;
- add an abstention route for insufficient context or risky mutations;
- tie final answers and patch rationales back to retrieved artifacts in the trace.

Sources:
- [RigorBench](https://arxiv.org/abs/2606.22678v1)
- [GroundEval](https://arxiv.org/abs/2606.22737v1)

## August 13 update: tool architecture needs equivalent-capability experiments

The Devil Is in the Interface isolates how capability exposure changes coding-agent behavior. Across six architectures, three actors, and 11,700 trajectories, interface shape changed consistency, exploration, steps, and tokens even when underlying access stayed similar.

The harness contract should therefore bind every run to a tool-interface schema version and compare equivalent-capability variants on repeated trajectories. Outcome, variance, relevant-file coverage, steps, tokens, and side effects belong in the same release record.

Source: https://arxiv.org/abs/2608.11386v1

## August 16 update: provider-neutral tests make control state executable

OpenAI Agents SDK v0.21.0 adds public scripted testing utilities for Agent, Sandbox, Realtime, and Voice workflows without provider requests. The release also isolates interruption snapshots, recursive approvals, MCP lifecycle state, and per-operation sandbox policy.

Practical lesson:
- test interruption, resume, recursive approval, terminal failure, and cleanup with fixed scripted models;
- snapshot state objects rather than sharing mutable results across attempts;
- separate deterministic control-contract tests from smaller live-provider integration tests;
- preserve MCP and sandbox lifecycle identity in every fixture.

Source:
- [OpenAI Agents SDK v0.21.0](https://github.com/openai/openai-agents-python/releases/tag/v0.21.0)

## Working conclusion

Agent harness architecture is becoming one of the clearest ways to tell whether a team is building a toy, a developer tool, or a real operating substrate. The winning systems will make context explicit, tool boundaries governable, restore paths safe, typed component interfaces inspectable, orchestration empirically justified and quality-gated, skill routing compositional, test-oracle strength machine-checkable, evidence easy to inspect, environment-specific falsification surfaces routine, real-session misalignment labels routine, proposal-soundness gates explicit, failed trajectories layer-attributed, process discipline measurable, and production failures routinely promoted into versioned regression fixtures with trajectory and outcome graders.

## June 26 update: coding-agent configuration needs deterministic control-plane treatment

Dedicated topic: [Coding Agent Control Plane](../coding-agent-control-plane/coding-agent-control-plane.md)

A deterministic control plane for coding agents updates this topic at the configuration layer. Agent harnesses are not only prompts, tools, and traces. They also include the repo-local rules files and IDE-specific markdown that tell the agent how to behave. Those files now need provenance, hashes, lockfiles, permission declarations, compiled targets, CI drift checks, and trace binding.

Source:
- [A Deterministic Control Plane for LLM Coding Agents](https://arxiv.org/abs/2606.26924v1)

## June 27 update: process harnesses preserve workflow authority

CUGA FLO adds a useful enterprise harness pattern: place a policy-governed agentic layer around a deterministic workflow engine, and intercept only designated control points. The harness contributes reasoning, adaptation, and oversight, but the workflow engine keeps structural authority over ordering, state transitions, and compliance.

Practical lesson:
- map workflow hook points before assigning agents;
- keep TaskAgent, DecisionAgent, and FlowAgent responsibilities separate;
- bind allowed tools, data scope, escalation rule, audit event, and rollback path to each hook;
- make the deterministic engine own ordering and required approvals;
- compare harness overlays against workflow replacement, because replacement often destroys the compliance surface the enterprise still needs.

Sources:
- [A Process Harness for Uplifting Legacy Workflows to Agentic BPM](https://arxiv.org/abs/2606.27188v1)
- [IBM CUGA examples](https://huggingface.co/blog/ibm-research/cuga-apps)
- [cuga-project/cuga-agent](https://github.com/cuga-project/cuga-agent)

## June 29 update: verifier cascades make architecture changes harness-owned

NOVA and repository-level risk measurement add a sharper rule for harness architecture: architecture-changing agents need promotion gates, and coding-agent performance needs repository outcome metrics. A harness that only returns a patch and a test result is too shallow for production architecture work.

Practical lesson:
- define mutation classes and invariants before letting agents alter architecture;
- run proposed changes through static checks, local execution, offline metrics, compatibility checks, and human approval where needed;
- preserve failed proposals and verifier diagnostics as trajectory memory;
- track repository-level integration friction as a harness outcome;
- judge autonomy by sustained repo health, not isolated benchmark wins.

Sources:
- [NOVA](https://arxiv.org/abs/2606.27243v2)
- [Govern the Repository, Not the Agent](https://arxiv.org/abs/2606.28235v1)

## July 2 update: benchmark scores need admissibility gates

RepoRescue and the performance-benchmark audit add a hard rule to harness architecture: benchmark scores should not be accepted unless the harness can prove what was editable, how the patch was replayed, and how stable the scoring rule is.

Practical lesson:
- enforce source-only or no-test-edit regimes in the runtime, not only in prompts;
- rerun patches after removing test edits when source repair is the target;
- replay performance tasks across machine profiles before trusting small deltas;
- report reference-patch validity, per-task score weight, and variance with every benchmark score;
- treat benchmark submissions as evidence packets with admissibility fields.

Sources:
- [RepoRescue](https://arxiv.org/abs/2607.01213v1)
- [Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?](https://arxiv.org/abs/2607.01211v1)

## July 3 update: action-boundary oracles are harness gates

UnderSpecBench adds a practical harness rule: task completion is not enough when the instruction is underspecified and the action has side effects. A harness should score Safe Success, Wrong Target, and OverScope separately, and it should classify non-action as clarification, refusal, or deferment rather than flattening all non-completion into failure.

Practical lesson:
- vary intent clarity, target certainty, and blast radius independently in regression fixtures;
- require target identity and scope fields before effectful tool calls;
- preserve deterministic side-effect oracles for wrong-target and overscope outcomes;
- reward clarification and deferment when safe action is not identifiable;
- route high-blast-radius actions through approval or policy before commit.

Source:
- [Coding Agents Are Guessing](https://arxiv.org/abs/2607.02294v1)

## July 5 update: tests and prompts need coupled coverage gates

TestEvo-Bench and Prompt Coverage Adequacy add two useful harness gates for coding agents. TestEvo-Bench evaluates whether code changes and tests evolve together, using executable test-generation and test-update tasks mined from real repositories. Prompt Coverage Adequacy treats the task description itself as a coverage target, so generated tests are judged against expressed requirements rather than code lines alone.

The reasoning-effort study adds a routing companion: if first-run failures come from weak reasoning, extra browser testing can add cost without improving reliability. The harness should know which knob it is turning.

Practical lesson:
- mine internal code-plus-test evolution fixtures from real commit histories;
- score test generation and test update separately;
- record task timestamp, environment, pass rate, coverage, mutation score, cost, and training-cutoff eligibility;
- add prompt or requirement coverage checks for agent-authored tests;
- route reasoning effort, verifier depth, and tool exposure based on observed failure class.

Sources:
- [TestEvo-Bench](https://arxiv.org/abs/2607.02469v1)
- [TestEvo-Bench site](https://www.testevo-bench.com/)
- [Prompt Coverage Adequacy](https://arxiv.org/abs/2607.02057v1)
- [Reasoning effort, not tool access](https://arxiv.org/abs/2607.02436v1)

## July 6 update: conversation regressions are harness failures

Regression Accumulation makes multi-turn coding a harness problem. The issue is not only whether the latest patch passes the latest request. The harness has to preserve prior accepted behavior as the conversation evolves. Without that, a coding agent can produce a locally plausible final answer that violates the session contract.

Practical lesson:
- maintain a turn-indexed requirement ledger;
- convert accepted requirements into tests, invariants, or oracle checks before later edits;
- replay prior checks on every turn;
- rollback and retry when new code violates old commitments;
- record regression origin turn, broken requirement, mitigation path, and final verifier outcome in the trace.

Source:
- [Regression Accumulation in Multi-Turn LLM Programming Conversations](https://arxiv.org/abs/2607.01855v1)


## July 8 update: language-specific SWE-bench packs make harness eval operational

Kotlin SWE-bench is useful because it turns a language ecosystem into an executable harness artifact. The benchmark packages repository-level Kotlin tasks with issue instructions, base commits, gold patches, hidden regression tests, and containerized validators. That is the shape serious coding-agent evaluation should copy.

Practical lesson:
- build small domain-specific replay packs before arguing from generic leaderboard results;
- record agent, model, effort setting, cost, wall time, validation command, and failure phase for every run;
- treat task packaging as harness infrastructure, not one-off benchmark glue;
- use language-specific suites to catch framework, build-system, style, and test-layout failures that generic SWE tasks miss.

Sources:
- [JetBrains Kotlin Benchmark release](https://blog.jetbrains.com/kotlin/2026/07/introducing-the-kotlin-benchmark-evaluate-ai-coding-agents-on-real-world-kotlin-tasks/)
- [Kotlin SWE-bench](https://github.com/Kotlin/kotlin-swe-bench)
- [Kotlin Benchmark leaderboard](https://kotlinlang.org/benchmark/)

## July 10 update: runtime guarantees should be executable contracts

From Prompts to Contracts makes the harness boundary concrete. Source scope, entity routing, trace hygiene, output shape, and recommendation rules should live in manifests, schemas, validators, and deterministic fallbacks around the model, not only in prompt prose. The paper reports that its code-owned checks held across all 270 model-substitution runs. Its ablation is the useful engineering result: prompt-only enforcement leaked violations, while a bolt-on guardrail over-refused and reduced utility. The integrated harness preserved both contract enforcement and 120/120 utility.

Practical lesson:
- define a typed run manifest for sources, model, prompt version, entity scope, and validators;
- keep deterministic validators outside the model for every load-bearing behavior;
- add deliberate contract violations as fault-injection fixtures;
- preserve failed model output, validator verdicts, and fallback output in the trace;
- rerun a fixed contract suite whenever the model, prompt, retrieval layer, or scaffold changes.

Sources:
- [From Prompts to Contracts](https://arxiv.org/abs/2607.08028v1)
- [hammerbaki/enterprise-llm-agent-harness](https://github.com/hammerbaki/enterprise-llm-agent-harness)

## July 13 update: proof and property tests should share one intent contract

Agentic Proof and Property-Based Testing makes validation architecture explicit. A typed property template exposes only the holes specific to one invariant and generates two evidence tracks: a Lean 4 proof over the formal model and a property-based test over the real implementation.

This is a harness pattern, not only a formal-methods result. The model should not freely author the requirement, proof architecture, generators, and test oracle at once. The harness owns the template and the agent fills bounded, typed slots. Agreement is strong evidence. Disagreement is a first-class model-to-runtime defect.

Practical lesson:
- identify one recurring invariant family and write its typed property template;
- generate proof and runtime test artifacts from the same claim;
- preserve model assumptions, proof result, executable test, counterexamples, and disagreement status together;
- review compiling but vacuous proofs as an explicit hallucination class;
- promote validated templates into reusable harness contracts rather than regenerating them per task.

Artifact caveat: the browsable package is substantial, but the evaluation is limited to Apache Spark and four property families. Generalization requires domain-specific formal models, generators, and invariant libraries.

Sources:
- [Agentic Proof and Property-Based Testing via Property-Templates](https://arxiv.org/abs/2607.09072v1)
- [browsable artifact](https://anonymous.4open.science/r/AgentLeanDiscprop-1597/)

## July 14 update: compile procedures before paging them

Compile, Then Page separates a safe representation change from a model-dependent runtime optimization. A deterministic compiler turns machine-readable SOP constraints into process functions, verifier subroutines, branches, and evidence-bearing returns. A symbolic stack machine then owns the cursor, variables, recovery, and audit transitions while the model handles semantic execution.

The useful deployment rule is asymmetric. Compiled text never significantly hurts in the reported study, but active-frame paging helps strong models and harms weaker ones. Paging is therefore a capability-gated harness feature, not a generic context optimization.

Practical lesson:
- compile one runbook into typed states, verifier recipes, branch logic, and refusal exits;
- preserve source rule IDs and evidence in every runtime transition;
- compare prose, compiled full text, and compiled plus paging on the same tasks;
- measure state discipline, refusal correctness, and recovery before enabling paging for a model;
- keep permissions and commit checks outside the paged prompt because the paper's runtime enforcement is intentionally soft.

Artifact caveat: no public implementation repository was found during the July 14 scan. The compiler pattern is concrete, but the reported model gate and SOPBench results still need independent reproduction.

Source:
- [Compile, Then Page](https://arxiv.org/abs/2607.11346v1)

## July 16 update: evaluation needs explicit component boundaries

AgentCompass and Harness Handbook strengthen different sides of harness architecture. AgentCompass separates benchmark, harness, and environment so model, scaffold, and runtime effects can be compared. Harness Handbook maps behavior requests back to scattered implementation sites before changes are planned.

Practical lesson:
- version benchmark, harness, environment, model, budget, and protocol independently;
- store retry, progress, task, and trajectory evidence under one run identity;
- compare harnesses while holding model, tasks, budget, and environment fixed;
- generate behavior maps from static program facts and verify every behavior claim against current source;
- use the behavior map for localization, but re-run structural callers, tests, and policy checks before editing.

Sources:
- [AgentCompass](https://arxiv.org/abs/2607.13705v1)
- [open-compass/AgentCompass](https://github.com/open-compass/AgentCompass)
- [Harness Handbook](https://arxiv.org/abs/2607.13285v1)
- [project page](https://ruhan-wang.github.io/Harness-Handbook/)

## July 18 update: score real writes in isolated application state

Copy-on-Write Scoring makes application-specific evaluation a data-plane control. Instead of grading only the agent's answer or maintaining a drifting replica, isolate each session's PostgreSQL writes behind base tables, changes tables, and views. Compare the resulting state to a human ground-truth session, then score extra, missing, and malformed writes at session and operation level.

Practical lesson:
- start with a disposable mirror or staging database because table-to-view conversion is invasive;
- record one high-value workflow as a human ground-truth session;
- bind every write to session and operation IDs;
- compare final state and operation utility before selective commit or discard;
- preserve tool-surface changes and score deltas as regression evidence.

Artifact caveat: the MIT repository is populated and tagged through `v0.1.7`, but the paper studies one PostgreSQL application and 20 workflows. It is a credible pilot substrate, not a universal benchmark.

Sources:
- [Copy-on-Write Scoring](https://arxiv.org/abs/2607.14336v1)
- [trail-ml/agent-cow-python](https://github.com/trail-ml/agent-cow-python)

## July 20 update: silent errors need trace-backed oracles

The agent-reactive bug study makes the model-harness boundary measurable. Of 255 manually confirmed bugs across Codex, Gemini CLI, LangChain, and CrewAI, 108 were silent errors. The model's narration looked valid while the tool trace, context state, workspace, or workflow progress showed that the claimed work had not occurred.

Practical lesson:
- store raw model output, parsed action, validator decision, tool receipt, state delta, and final narration under one run identity;
- make impossible claimed actions and missing required tool arguments deterministic failures;
- replay the same trigger across model, prompt, harness, and environment versions;
- classify fixes by model, harness, environment, or oracle layer instead of calling every defect a model failure;
- treat retry loops, context compaction regressions, and silent premature completion as harness test classes.

Evidence caveat: the corpus comes from four projects and public issue reports. It measures reported, manually classified failures rather than deployment prevalence.

Source:
- [Understanding Agent-Reactive Bugs at the Model-Harness Boundary](https://arxiv.org/abs/2607.15684v1)
## July 22 update: stable harnesses make the default runtime a versioned product surface

Microsoft Agent Framework's stable harness release turns a common architecture checklist into a concrete open-source composition. Tool loops, per-service-call history persistence, compaction, todos and modes, file memory, skills, approvals, provider web search, and OpenTelemetry now share one versioned surface in Python and .NET.

The release boundary is the useful control. File access is opt-in, and background agents, looping, and shell tooling are not all stable core features. A production harness should graduate high-risk capabilities separately rather than inherit them from a batteries-included label.

Practical lesson:
- pin the harness, model, provider, tool schemas, compaction policy, and persistence schema together;
- emit tool, approval, todo, compaction, history, and resume events under one run identity;
- keep file, shell, loop, and background authority out of the default profile;
- run crash, resume, compaction, approval replay, tool-name collision, and trace-propagation fixtures;
- compare harnesses while holding tasks, models, tools, budgets, and environments fixed.

Artifact caveat: the MIT monorepo is mature and the core API is stable, but the production-ready claim is vendor-authored and the release does not include an independent cross-framework benchmark.

Sources:
- [Microsoft Agent Framework Harness announcement](https://devblogs.microsoft.com/agent-framework/the-microsoft-agent-framework-harness-is-now-released/)
- [Python 1.12.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.12.0)
- [.NET 1.14.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.14.0)
- [microsoft/agent-framework](https://github.com/microsoft/agent-framework)

## July 24 update: real harness rollouts need an explicit training adapter

OpenForgeRL makes harness behavior a training surface. A model-serving proxy records calls from production-style coding and GUI harnesses, while remote containers isolate environment execution and a standard trainer consumes the resulting trajectories.

Practical lesson:
- bind model requests, responses, tool events, subagents, compaction, state deltas, rewards, and environment digests to one rollout ID;
- keep the deployed harness outside the trainer process and connect it through a typed adapter;
- compare harnesses while holding model, task, budget, reward, and environment fixed;
- isolate each rollout and preserve crash, retry, timeout, and cleanup receipts;
- score error recovery explicitly because broad RL gains did not eliminate that weakness.

Artifact caveat: the paper claims open-source code, data, and models, but its primary pages expose no exact OpenForge project artifact. The architecture is concrete; full reproduction still needs distributed rollout infrastructure.

Source:
- [OpenForgeRL](https://arxiv.org/abs/2607.21557v1)

## July 29 update: optimize explicit artifacts, not unconstrained adaptation

Specula and the frozen-harness study define two complementary harness rules. Agent-authored formal specifications need deterministic trace and replay checks. Adaptive harness policies need to beat an optimized static configuration before they receive online authority.

Practical lesson:
- make specifications, prompts, tool policies, memory policies, planning depth, verification, and budgets versioned artifacts;
- require model checking, trace validation, and code-level replay for agent-authored formal models;
- begin harness optimization from a small reviewed action space and a strong static baseline;
- isolate malformed episodes and preserve reward, cost, latency, compliance, and cache-accounting evidence;
- enable online adaptation only when held-out gains justify its sample and governance cost.

Artifact caveats: Specula is Apache-2.0 and populated. The context-optimization repository is populated but has no declared license, and its online controllers did not beat the static baseline in the reported budget.

Sources:
- [Specula](https://arxiv.org/abs/2607.25333v1)
- [specula-org/Specula](https://github.com/specula-org/Specula)
- [Frozen harness control study](https://arxiv.org/abs/2607.25415v1)
- [context-optimization-rl](https://github.com/dpaul0501/context-optimization-rl)
## July 31 update: benchmark tasks need executable reconstruction lifecycles

Change2Task turns repository history into a reusable task-construction surface. A task is accepted only when a frozen modern base, task patch, restoration patch, target checks, protected regressions, edit scope, and provenance survive a healthy, task, and restored lifecycle.

Practical lesson:
- begin with deterministic patch reversal and escalate only when repository evolution requires mapping or reconstruction;
- freeze source PR, modern base, task and restoration patches, checks, adapter, and environment identity;
- require pass-fail-pass target behavior and green regressions across all states;
- compare historical and reconstructed variants under the same agent and verifier;
- treat artifact absence as a reproduction gap even when the paper method is detailed.

Artifact caveat: no paper-owned public implementation repository resolved from primary pages or exact-title GitHub search.

Source:
- [Change2Task](https://arxiv.org/abs/2607.28591v1)

## August 1 update: replayable session state is a released harness contract

Microsoft Agent Framework Python 1.13.0 combines reusable session stores, complete Responses-session persistence, replayable checkpoints from initial input and human responses, approval continuity fixes, bounded archive-backed MCP skill discovery, and cache-write token observability.

Practical lesson:
- version session schema, checkpoint schema, provider adapters, approvals, and compaction policy together;
- preserve initial input, human responses, tool calls, results, and approval decisions under one run identity;
- run crash, resume, compaction, duplicate-call, and checkpoint migration fixtures;
- bound archive skill sources by identity, size, authorization, and retention;
- review process-wide telemetry before production adoption.

Release caveat: replay behavior is breaking, archive-backed skills widen the executable context surface, and first-party feature telemetry needs explicit review.

Sources:
- [Microsoft Agent Framework Python 1.13.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.13.0)
- [microsoft/agent-framework](https://github.com/microsoft/agent-framework)

## August 8 update: harness optimization needs a trusted held-out boundary

HarnessOpt-Bench makes harness self-improvement measurable across five optimizer models, four tasks, and 111 scored runs. The reusable control pattern is an immutable candidate, an inaccessible test partition, isolated evaluation, fixed budgets, and complete receipts.

Source: https://arxiv.org/abs/2608.06301v1


## August 12 update: self-evolution is a typed compensation layer, not a universal recipe

One Recipe, Many Harnesses holds a self-evolution recipe fixed across eight languages and three models. Typed failure signals and falsifiable edit contracts made the resulting changes inspectable. Most cells improved, but Python and GPT-5-mini were null regions, and 20 to 40 percent of each harness remained ecosystem-specific.

Practical lesson:
- evolve against measured execution defects;
- keep null results as evidence against unnecessary edits;
- distill only the transfer-tested common core;
- retain ecosystem-specific adapters and held-out gates.

Source:
- [One Recipe, Many Harnesses](https://arxiv.org/abs/2608.10178v1)
