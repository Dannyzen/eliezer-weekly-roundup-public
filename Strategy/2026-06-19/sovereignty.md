# Strategy Daily Sovereignty: 2026-06-19

Today's strategic signal is that agent authority is moving out of the model and into runtime-controlled objects: sessions, tool catalogs, tool programs, staged eval evidence, and brokered mutation certificates. The model can propose; the platform should own state, discovery, evidence, and authority.

## Executive summary

1. **Mutation authority belongs in brokers, not agents.** Sovereign Execution Brokers remove standing production credentials from agents and enforce certificate-bound authority at the moment of mutation.
2. **Capability discovery is becoming a governed supply chain.** Agentic Resource Discovery and ToolPro show why capability search, manifest provenance, effect typing, and compiled execution should be gateway-owned infrastructure.
3. **Safety claims need deployment-shaped evidence.** SafeClawBench, OpenAI Deployment Simulation, and Google DeepMind's AI Control Roadmap all reject benchmark theater in favor of staged endpoints, realistic distributions, monitoring coverage, recall, and time-to-response.

## Mutation authority belongs in brokers, not agents

Sovereign Execution Brokers is the clearest sovereignty paper today. Its core claim is simple: production mutation authority should not sit inside a non-deterministic reasoning process. Identity-based access control authorizes principals, and admission systems can certify proposed actions, but neither is enough unless the infrastructure mutation path itself requires a broker to verify the certificate at execution time.

The proposed SEB consumes certificates from a Sovereign Assurance Boundary, verifies that the requested mutation matches the certified contract, checks validity windows, policy epochs, revocation epochs, and live-state drift, mints scoped execution identity, invokes infrastructure APIs, and records signed decision and outcome records. The paper describes a Go prototype with AWS STS and Kubernetes TokenRequest adapters and emphasizes the hard deployment rule: production mutation APIs must reject non-broker identities.

Google DeepMind's AI Control Roadmap is the operating-model cousin of the same idea. It treats capable agents as potentially imperfectly aligned, then layers threat modeling, active monitoring, prevention, response, and capability-aligned security scaling around internal agent deployments. The useful metrics are operational: coverage, recall, and time-to-response.

Implementable now:
- remove standing write credentials from agent runtimes where possible
- route production mutations through a broker that validates a signed action certificate
- bind certificate checks to action contract, principal, resource scope, policy epoch, revocation epoch, and live-state hash
- mint short-lived scoped credentials only after validation
- track monitoring coverage, recall, and time-to-response for risky agent actions

Tools, repos, and methodologies worth exploring:
- AWS STS, Kubernetes TokenRequest, workload identity, short-lived credentials
- OPA or Cedar for certificate and policy predicates
- signed admission artifacts with revocation epochs
- OpenTelemetry spans for proposal, admission, broker decision, scoped credential mint, mutation, and outcome
- DeepMind-style AI control threat taxonomies and monitor metrics

Core sources:
- Sovereign Execution Brokers: https://arxiv.org/abs/2606.20520v1
- Google DeepMind AI Control Roadmap post: https://deepmind.google/blog/securing-the-future-of-ai-agents/

Implementability score: 0.68

## Capability discovery is becoming a governed supply chain

The agent ecosystem is outgrowing static tool lists. Hugging Face's Agentic Resource Discovery draft makes the discovery layer explicit: publishers expose structured catalogs, registries offer natural-language search, and agents can discover Skills, MCP servers, A2A agents, and applications without pre-installing everything. The reference `hf-discover` repo implements that pattern for Hugging Face Spaces, generated Skills, and MCP server cards.

ToolPro extends the same governance problem into execution. Once a capability is selected, the agent should not always issue a fragile sequence of static endpoint calls. For long workflows, the better unit is an executable tool program with control flow, intermediate bindings, READ/WRITE effect types, and effect-aware replay for state-changing operations.

The strategic point is that discovery and execution are authority surfaces. A registry decides what the agent can find. A compiler decides what workflow the service will execute. A gateway should therefore preserve publisher identity, manifest hash, policy scope, effect type, compiled program hash, and final state change.

Implementable now:
- make capability discovery permissioned by principal, tenant, workflow, and data class
- require agent-visible tools and skills to carry source metadata and manifest hashes
- record registry query, selected result, generated skill or MCP card, and installed or loaded artifact
- require effect typing before compiled tool programs can write state
- block or require review when manifest provenance, effect typing, or publisher identity is weak

Tools, repos, and methodologies worth exploring:
- hf-discover and ARD-style registries
- MCP gateways with scoped catalog search
- signed ai-catalog-like manifests for internal tools
- effect-typed workflow DSLs or service-side tool programs
- policy-as-code over capability discovery and compiled execution

Core sources:
- Agentic Resource Discovery launch: https://huggingface.co/blog/agentic-resource-discovery-launch
- hf-discover repository: https://github.com/huggingface/hf-discover
- ToolPro paper: https://arxiv.org/abs/2606.19992v1

Implementability score: 0.73

## Safety claims need deployment-shaped evidence

SafeClawBench, OpenAI Deployment Simulation, and DeepMind's AI Control Roadmap all push against a weak evaluation habit: one benchmark score, one refusal rate, or one red-team pass cannot justify deployment authority.

SafeClawBench separates semantic attack acceptance, audit-visible harm, and sandbox-observed harm. That matters because executable tool protocols can still produce state harm even when the semantic check passes. OpenAI's Deployment Simulation uses realistic previous conversations to forecast candidate-model behavior before release and explicitly says the method extends to challenging agentic rollouts involving tool use. DeepMind's roadmap moves from evaluation to operating controls: threat-model agents as insider-like actors, monitor trajectories, and measure coverage, recall, and time-to-response.

The governance lesson is that safety evidence must match the deployment claim. If the claim is about tool harm, measure tool harm. If the claim is about real traffic, sample realistic traffic. If the claim is about internal agents, measure monitors on internal task trajectories and report what traffic they cover.

Implementable now:
- separate refusal, harmful evidence, sandbox state mutation, and deployment-like incidence estimates
- sample representative historical workflows for pre-release simulation
- tag each eval result with traffic slice, tool set, scaffold, model, policy, and environment state
- measure monitor coverage, recall, false positives, time-to-response, and human escalation outcomes
- treat missing coverage as an explicit limitation, not an invisible caveat

Tools, repos, and methodologies worth exploring:
- SafeClawBench and staged endpoint reports
- OpenAI-style deployment simulation on privacy-preserved historical workflows
- DeepMind-style AI control metrics
- sandbox state oracles and audit evidence extractors
- release gates that require both tail-risk red teams and representative-distribution checks

Core sources:
- SafeClawBench: https://arxiv.org/abs/2606.18356v1
- OpenAI Deployment Simulation: https://openai.com/index/deployment-simulation
- Google DeepMind AI Control Roadmap post: https://deepmind.google/blog/securing-the-future-of-ai-agents/

Implementability score: 0.75

## Strategic read

The sovereignty move is not owning every model. It is owning the runtime boundaries where state, capability, evidence, and authority become real. Let the model propose. Make the platform decide what state is valid, which tools are discoverable, which programs may write, which evidence supports a safety claim, and which broker is allowed to mutate production.

## References

- Sovereign Execution Brokers: Enforcing Certificate-Bound Authority in Agentic Control Planes: https://arxiv.org/abs/2606.20520v1
- Securing internal systems against increasingly capable and imperfectly aligned AI: https://deepmind.google/blog/securing-the-future-of-ai-agents/
- Agentic Resource Discovery: Let agents search: https://huggingface.co/blog/agentic-resource-discovery-launch
- hf-discover repository: https://github.com/huggingface/hf-discover
- Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services: https://arxiv.org/abs/2606.19992v1
- SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents: https://arxiv.org/abs/2606.18356v1
- Predicting model behavior before release by simulating deployment: https://openai.com/index/deployment-simulation
