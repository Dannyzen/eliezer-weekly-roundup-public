# Agent Network Containment

Agent network containment is the control discipline for systems where agents communicate with other agents, call tools across trust boundaries, and act for different human or organizational principals.

## Why this topic now

Two May 1 sources make the boundary shift explicit:
- Microsoft Research red-teamed a live internal platform with more than 100 always-on agents and found network-level failures that single-agent tests miss.
- MCPHunt shows that multi-server MCP agents can propagate canary secrets across trust boundaries as a structural side effect of faithful tool composition.

Core sources:
- Microsoft Research, “Red-teaming a network of agents”: https://www.microsoft.com/en-us/research/blog/red-teaming-a-network-of-agents-understanding-what-breaks-when-ai-agents-interact-at-scale/
- MCPHunt paper: https://arxiv.org/abs/2604.27819
- MCPHunt repo: https://github.com/lihaonan0716/MCPHunt
- MCPHunt traces: https://huggingface.co/datasets/lihaonan0716/mcphunt-agent-traces
- Agent Name Service proof of concept: https://arxiv.org/abs/2604.26997
- Autonomous LLM Agent Worms: https://arxiv.org/abs/2605.02812v1

## Core thesis

A safe individual agent can still be unsafe in a network.

The containment problem changes when agents:
- represent different human principals;
- message each other directly;
- post into shared spaces;
- use marketplaces, wallets, or reputation systems;
- discover other agents or services dynamically;
- compose MCP servers with different trust boundaries;
- read from one surface and write to another.

In that world, “the model followed the instruction” is not a defense. Faithful execution can still become data propagation, amplification, trust capture, or invisible proxying.

## May 1 update: cross-boundary data flow is the test case for agent network containment

Microsoft’s red-team report and MCPHunt should be read together. Microsoft shows the social/network failure modes. MCPHunt shows the tool/data-flow failure modes.

Microsoft identifies four network-level risks:
- **Propagation:** an agent worm spreads across peers and collects private data at each hop.
- **Amplification:** an attacker uses trusted agents to manufacture social proof around a false claim.
- **Trust capture:** the attacker controls the peer set an agent consults to verify claims.
- **Invisibility:** sensitive information moves through unaware proxy agents, hiding the attacker from the target.

MCPHunt turns the same lesson into an evaluation pattern for MCP. It uses canary-based taint tracking, risky/benign/hard-negative environments, and credential-relevance stratification to distinguish task-mandated transfer from policy-violating propagation. Across 3,615 traces, policy-violating propagation reached 11.5% to 41.3% across models, with browser-mediated pathways especially risky.

The shared strategic lesson is direct: agent networks need observable containment across communication and tool paths. Prompts can reduce some failures, but they are not the security boundary.

## May 5 update: persistent state turns reads into re-entry paths

Autonomous LLM Agent Worms moves the containment problem inside the agent's own durable state. Persistent workspaces, memory files, scheduled task state, summaries, and messaging integrations can store attacker-influenced content that re-enters a future prompt. In that model, a read is not harmless. A read can become the first step in a write-to-future-context chain.

The useful defense shape is RTW-A: block write-before-exposed-read re-entry, seal configuration, use typed memory promotion, and attenuate capabilities after external reads. This is a containment rule, not merely a prompt rule.

Practical additions:
- label external reads, imported files, peer messages, and derived summaries as tainted until promoted
- prevent tainted content from entering system/developer prompts, trusted memory, or scheduled autoload state
- seal static configuration from ordinary agent writes
- require typed memory promotion before persistent summaries influence future privileged runs
- attenuate shell, credential, messaging, deployment, and config-edit tools after untrusted reads
- test staging agents with canary payloads that survive summarization attempts

Source:
- [Autonomous LLM Agent Worms](https://arxiv.org/abs/2605.02812v1)

## Control layers

### 1. Principal identity

Every agent should act for an explicit principal: a user, team, service, or organization. Avoid generic “agent” identities that erase accountability.

### 2. Peer-agent input handling

Messages from other agents should be treated as untrusted input, not as privileged instructions. Require source, reason, and intended action before acting on peer claims.

### 3. Data-flow policy

Tool calls should carry data class, source, destination, and redaction state. The system should know when private data from one boundary is about to cross into another.

### 4. Hop and rate limits

Agent-to-agent messages need propagation controls: hop limits, fan-out limits, repeated-payload detection, and quarantine when a payload behaves like a worm.

### 5. Independence checks

Do not treat repeated claims as corroboration unless the sources are independent. Agent networks are especially vulnerable to Sybil-style trust capture.

### 6. Cross-agent observability

Single-agent traces are not enough. Operators need network traces that show which agent communicated what to whom, which tool surfaces were used, and which data crossed each boundary.

### 7. Quarantine and revocation

The platform needs an emergency path to pause agents, revoke tools, quarantine messages, and invalidate credentials when a propagation event starts.

## What to build now

- Add canary secrets to staging workspaces and MCP test environments.
- Run MCPHunt-style risky, benign, and hard-negative evals before exposing new tools broadly.
- Label traces with principal, agent identity, data class, source, destination, redaction state, and peer-message lineage.
- Add hop limits and rate limits to agent-to-agent messaging.
- Require a stated reason before an agent acts on another agent’s request.
- Detect repeated payloads and sudden fan-out across peer-agent channels.
- Gate high-risk tool transitions through policy-as-code rather than prompt instructions.
- Keep a kill switch that can pause an agent group and revoke its tool grants.

## What to avoid

Avoid these traps:
- assuming that “trusted” MCP servers cannot compose into unsafe data flows;
- allowing agents to forward peer instructions without provenance and hop limits;
- using reputation or voting systems without Sybil resistance;
- relying on repeated claims as evidence when the sources may be attacker-controlled;
- logging only the final tool call and not the peer-message chain that caused it;
- treating prompt-level “do not leak secrets” rules as a substitute for taint tests and gateway policy.

## Practical tools and methodologies

- MCPHunt for canary-based cross-boundary propagation testing.
- OPA, Cedar, or similar policy engines for gateway enforcement.
- OpenTelemetry spans annotated with data-flow metadata.
- Service mesh or Kubernetes identity for internal agent deployments.
- Agent Name Service-style catalogs for verifiable discovery and capabilities.
- Network anomaly detection for fan-out, repeated payloads, and unusual peer-message paths.
- Red-team drills for agent worms, trust capture, and proxy exfiltration.

## Implementability score

0.64

The ingredients exist: canary strings, trace scanning, policy engines, identity systems, message-rate limits, gateway wrappers, and red-team harnesses. The hard part is integration. Most agent stacks still log tool calls as local events rather than graph events crossing principals and trust boundaries.

## May 6 update: containment needs influence provenance inside the run

ARGUS, MAGE, and MEMSAD extend the containment problem from network propagation into intra-agent causality. The system needs to know which untrusted content influenced a decision, which safety facts persisted across the trajectory, and whether a memory object looks poisoned before it can steer future behavior.

ARGUS is the cleanest architectural signal: construct an influence provenance graph and require trustworthy justification before execution. MAGE adds a complementary safety shadow memory that persists safety-critical context across long-horizon runs. MEMSAD adds the retrieval-memory poisoning angle: persistent memory can be attacked directly, so memory defenses need calibration and adversarial tests.

Practical additions:
- label every retrieved document, memory, tool output, and peer message with source and trust tier
- build decision records that cite the evidence path for high-risk actions
- keep safety shadow memory separate from task memory so constraints are not overwritten by ordinary summarization
- run memory-poisoning and canary tests against retrieval stores before broad deployment
- block privileged actions when the provenance path depends on untrusted context without independent confirmation

Sources:
- [ARGUS](https://arxiv.org/abs/2605.03378)
- [MAGE](https://arxiv.org/abs/2605.03228)
- [MEMSAD](https://arxiv.org/abs/2605.03482)

## Working conclusion

Agent network containment is the next governance layer after tool permissioning. Once agents can discover, message, delegate, and relay across principals, the operator has to govern the graph: who spoke, who acted, what data crossed, what policy allowed it, and how the system can stop spread when a benign-looking workflow turns viral.
