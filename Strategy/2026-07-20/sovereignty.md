# Strategy Daily Sovereignty - 2026-07-20

## Verdict

The gateway and execution broker are becoming the two sovereign boundaries of the agentic stack. The gateway controls which capabilities and sessions reach the model. The broker controls which proposed actions become authorized effects.

## Scan boundary

- Both promoted papers were submitted Friday, 2026-07-17 and first listed Monday, 2026-07-20.
- Primary PDFs were read directly.
- No public implementation repository was linked from either primary paper, so both are treated as architecture and evaluation references rather than drop-in systems.

## Cloud-scale MCP needs a gateway-owned data plane

Core source: [Scalable LLM Agent Tool Access in the Cloud](https://arxiv.org/abs/2607.15593v1)

Submission: 2026-07-17 03:40:49 UTC. First listed: 2026-07-20.

### What it found

The Alibaba Cloud system breaks MCP's direct-connect assumption. It moves legacy API adaptation, protocol compatibility, access control, tool recommendation, and session-aware routing into a shared gateway.

The reported evaluation uses up to 3,616 tools from a production catalog, four production traces, and ToolBench with up to 640 tools. Hybrid retrieval reaches more than 98% Top-15 recall for thousand-scale catalogs, stays below 250 ms, reduces tool-selection time by 8.9x, and reduces token use by 23.8x relative to exposing the full catalog.

The strongest part of the paper is the failure accounting. Stateful routing is not free. At about 100 QPS, session lookup and routing account for 75% of mean request time in the reported single-instance setup. Cross-instance misses push state into a centralized coordination path, and the paper uses shared storage plus Pub/Sub to preserve long-lived sessions and response ownership.

### Why it matters

Tool retrieval and tool authorization cannot be separate afterthoughts. A catalog search that ignores principal, tenant, workflow, policy, session, and server identity can retrieve the right semantic tool and still create the wrong authority path.

### Fit in the stack

- **Gateway:** protocol normalization, authentication, access control, tool retrieval, and audit.
- **Orchestration:** session ownership, affinity, Pub/Sub response routing, and long-lived connection state.
- **Context economy:** expose Top-K tools instead of thousands of schemas.

### Implementable now

1. Put tool discovery behind the same policy filter as invocation.
2. Return a small authorized tool set with stable server and tool identities.
3. Bind session ownership, return path, tenant, and trace sink before the first call.
4. Measure retrieval recall, selection accuracy, prompt tokens, latency, and authorization false positives together.
5. Add cache invalidation and manifest-drift tests for a changing tool catalog.

Tools and methodologies worth exploring:

- hybrid BM25 plus dense retrieval
- Redis or equivalent shared session state, Pub/Sub, consistent hashing, session-affinity traces
- Agent Gateway, Amazon Bedrock AgentCore Gateway, Microsoft MCP Gateway, and Alibaba Cloud's paper as architecture references

Implementability score: **0.65**

A thin authorized retrieval gateway is buildable now. Production session routing across thousands of tools and replicas is serious distributed-systems work, and the evaluated Alibaba system is not released as public code.

## Cryptographic release separates neural intent from execution authority

Core source: [From Neural Intent to Cryptographic Authorization](https://arxiv.org/abs/2607.15596v1)

Submission: 2026-07-17 03:44:05 UTC. First listed: 2026-07-20.

### What it found

Neural Cryptographic Services (NCS) treats the planner as untrusted. The model produces a plan draft but cannot release execution authority. A deterministic controller verifies an offline signature and hash chain, releases one instruction payload at a time, and rejects tool names, arguments, or order that do not match the authorized step.

On AgentDojo, NCS-Full reports 0.0% unauthorized tool execution for DeepSeek-Chat, GPT-5 Reasoning, and GPT-5 Chat, and 8.3% for GPT-4o-mini. The caveat is material: GPT-4o-mini's benign utility falls from 50.0% to 44.4%, and attack utility falls from 41.7% to 33.3%. Security is not uniformly free.

The custom 85-case argument-hijacking suite is the sharper result. NCS-Full drives argument-hijack success to 0.0% across the evaluated models and control tools. Ed25519 plus SHA-256 verification remains below 1.2 ms at p50 in the reported microbenchmark. No public implementation artifact is linked, and the custom benchmark comes from the same authors.

### Why it matters

Identity authentication answers who is calling. NCS answers whether this exact step, order, tool, and argument set was authorized. Agent systems need both. A valid token plus an injected transfer amount is still an unauthorized effect.

### Fit in the stack

- **Context-to-execution integrity:** writable model output becomes authority only through a typed release.
- **Execution control:** exact argument binding, order checks, fail-closed denial, and audit state.
- **Sovereignty:** the owner controls the signed instruction stream and release policy outside the model.

### Implementable now

1. Start with one high-risk tool, such as payment, email send, repository write, or deployment.
2. Canonicalize operation, target, arguments, principal, policy epoch, expiry, and prior-step hash.
3. Sign the approved instruction sequence outside the model.
4. Release one step at a time and reject any mismatch before the side effect.
5. Preserve proposal, release, denial, execution result, and resulting state under one receipt chain.

Tools and methodologies worth exploring:

- Ed25519, SHA-256 hash chains, JSON canonicalization, capability tokens, deterministic policy engines, AgentDojo, argument-hijack fixtures

Implementability score: **0.58**

The thin pattern is buildable. Full deployment requires complete mediation, key custody, canonicalization for every privileged tool, recovery semantics, and operator UX. There is no public NCS implementation to adopt.

## Working conclusion

The model should select from a narrow authorized capability surface and propose actions. The gateway and execution broker should own state, identity, policy, exact arguments, release order, and receipts. That is the line between useful autonomy and ambient authority.
