# Agent Harness Architecture

Last updated: 2026-07-03

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
