# Sessionful Agent Loops

Sessionful agent loops are becoming the architecture that separates serious systems from clever demos.

The durable pattern is straightforward: the useful unit is no longer a single request with some tool calls attached. It is a bounded run with a workspace, reusable state, approval checkpoints, analytics, and a transport that does not rebuild full context after every action.

## Why this topic now

The April 2026 signal is unusually clear:
- **OpenAI workspace agents** package shared cloud agents with files, code, tools, memory, schedules, Slack deployment, approvals, and enterprise monitoring.
- **Responses API WebSockets** keep connection-scoped state in memory and reuse prior response state instead of reconstructing everything on each follow-up call, cutting agent-loop latency materially.
- **Hugging Face ml-intern**, today's strongest GitHub-trending open-source agent repo, shows the same shape in public code: context compaction, approval checks, tool routing, doom-loop detection, and MCP servers.

Core sources:
- Introducing workspace agents in ChatGPT: https://openai.com/index/introducing-workspace-agents-in-chatgpt
- Workspace agents academy guide: https://openai.com/academy/workspace-agents
- Speeding up agentic workflows with WebSockets in the Responses API: https://openai.com/index/speeding-up-agentic-workflows-with-websockets
- Hugging Face ml-intern: https://github.com/huggingface/ml-intern

## Core thesis

The wrong question is "how many tools can my model call?"

The better questions are:
- where does a run begin and end?
- what state survives between tool calls?
- what part of that state is cached, compacted, or replayable?
- what approvals and controls sit in front of side effects?
- what analytics tell you whether the shared agent is actually helping?

If those questions are missing, the agent is usually still a stateless chat wrapper pretending to be a workflow engine.

## What changed

### Product surfaces are becoming long-lived
Workspace agents make the runtime visible to end users. The agent can run in the cloud, keep working when the user is away, operate on a schedule, live in Slack, access a workspace for files and code, and expose analytics plus admin controls. That is a much richer product surface than a one-off assistant response.

### Transport now matters as much as the model
The Responses API WebSockets work is strategically important because it shows where latency was hiding. Once model inference got faster, request-validation and context-rebuild overhead started dominating. The fix was not a prompt trick. It was transport and state design: keep a persistent connection, cache previous response state in memory, and process only the new increment.

### Open source is converging on the same stack shape
`ml-intern` matters less as a product and more as evidence. Its architecture includes a context manager, auto-compaction, a tool router spanning docs/repos/jobs/MCP servers, approval checks for risky actions, and a doom-loop detector. Different ecosystems are converging on the same answer: session state, control points, and tool mediation are the real product.

## What to build now

### 1. Give every serious run a durable identity
A multi-step job should not dissolve into unrelated API calls. Keep a run or session object that can carry state, metrics, approvals, and eventual replay.

### 2. Separate reusable state from new input
Cache what does not need to be rebuilt: validated conversation state, tool definitions, rendered tokens, or other reusable context. Only process the delta when a tool returns.

### 3. Treat the workspace as part of the runtime
Files, code, memory, and tool outputs should live inside an explicit workspace boundary. That makes the run inspectable and easier to govern.

### 4. Put approvals in the execution path
If the agent can mutate files, send messages, or schedule work, approval gates should be a first-class runtime concept, not a product patch later.

### 5. Make analytics and compliance visible
Shared agents need operator surfaces: run counts, failure modes, connected systems, policy configuration, and a way to suspend or revoke unsafe agents.

### 6. Compact context instead of letting it bloat
Long-lived sessions need compaction, summaries, or scoped memory. Otherwise the session model collapses under its own history.

## What to avoid

Avoid these traps:
- rebuilding the full conversation and validation path after every tool call
- treating memory as an opaque side effect rather than an explicit runtime surface
- hiding approvals outside the agent loop
- shipping shared agents without analytics, trace retention, or admin controls
- letting one session accumulate unbounded context with no compaction or replay policy

## Practical tools and methods worth exploring now

- OpenAI workspace agents for shared, scheduled, approval-aware workflow automation
- Responses API WebSocket mode for lower-overhead tool loops and state reuse
- `previous_response_id`-style continuation semantics
- open-source comparators like `huggingface/ml-intern`
- run analytics, trace retention, and suspension controls for shared agents

## June 27 update: loops need semantic stop policies, not fixed caps

Semantic Early-Stopping for Iterative LLM Agent Loops adds a practical runtime governor for sessionful loops. A loop should not run until an arbitrary `max_iterations` cap. It should stop when consecutive drafts stop changing meaning, and the harness should prove the quality-cost tradeoff by replaying policies over the same cached trajectories.

Practical lesson:
- attach a stop policy to every recurring writer-critic, RAG, review, or multi-agent revision loop;
- log semantic distance, patience window, selected round, operational tokens, and wall time;
- evaluate stopping policies by replaying identical full trajectories, not by comparing noisy separate runs;
- separate operational-token cost from evaluation-token cost;
- treat round selection as the next open problem after cheap stopping is working.

Sources:
- [Semantic Early-Stopping for Iterative LLM Agent Loops](https://arxiv.org/abs/2606.27009v1)
- [semantic-halting-problem](https://github.com/SahilShrivastava-Dev/semantic-halting-problem)

## July 4 update: loops need static bound coverage before runtime

IAL-Scan adds the static-analysis complement to semantic stop policies. A loop can look bounded at the product surface while the actual feedback path still reaches model calls, tools, handoffs, retries, state growth, or external effects without a real bound. That makes loop safety a preflight property, not only a runtime metric.

Practical lesson:
- recover agentic feedback paths from framework-specific code before deployment;
- classify repeated operations by model cost, tool side effect, memory growth, and external action;
- prove that max turns, recursion limits, retry limits, and approval gates cover the actual repeated path;
- store loop-bound coverage with the Agent BOM and run trace;
- keep semantic early stopping as a cost-quality policy, but do not confuse it with safety coverage.

Source:
- [When Agents Do Not Stop](https://arxiv.org/abs/2607.01641v1)

## July 21 update: verify-repair loops need calibrated stop and guarded fallback

VRR-Stop extends semantic stop policies from surface similarity into correctness dynamics. It separates verifier false acceptance and false rejection from repair benefit and repair damage, then stops when another repair has negative expected gain.

Practical lesson:
- replay full trajectories before changing the live loop;
- measure repair success and damage separately;
- track verifier discrimination and decision margin, not acceptance alone;
- calibrate on held-out transitions and do not transfer parameters across model, verifier, task, or prompt changes;
- retain the incumbent when calibration is weak, shifted, or sign-indeterminate.

Evidence caveat: the headline stress setting deliberately corrupts the repairer's task copy, each round uses eight verifier calls, the state is binary, and a low-discrimination Llama verifier makes calibrated stopping collapse. The public artifact supports zero-GPU replay from frozen traces but was not executed in this scan.

Sources:
- [Verify, Repair, Repeat, or Stop?](https://arxiv.org/abs/2607.17641v1)
- [VRR-Stop artifact](https://anonymous.4open.science/r/vrr-artifact-2583)

## Working conclusion

The agent loop is becoming a sessionful service. Teams that keep thinking in one-turn prompts will keep paying reconstruction costs, losing state, and bolting governance on after the fact. Teams that design for long-lived runs, explicit workspaces, compaction, approvals, replay, semantic stop policies, and static loop-bound coverage will have a much more stable foundation for everything else in the agent stack.