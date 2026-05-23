# Daily Strategy Scan: 2026-05-23

Today’s strategic signal is that agent state is becoming less visible. Agents are starting to share latent KV state, hide malicious intent across turns and artifacts, and advertise heterogeneous MCP client capabilities. Governance has to move from “inspect the current prompt” to “inspect the state channel, the trace, the artifact path, and the client capability surface.”

## KV-cache sharing creates an opaque data boundary

LCGuard targets a real next-stage multi-agent problem: agents may coordinate by sharing transformer KV caches rather than natural-language messages. That can improve efficiency and preserve richer task state, but it also creates an opaque data channel. Sensitive prompt content, intermediate reasoning, and agent-specific context can leak through a shared cache even when no explicit text disclosure occurs.

The paper’s useful framing is representation-level policy. A shared cache artifact is unsafe if an adversarial decoder can reconstruct sensitive agent-specific input from it. LCGuard proposes learned transformations that preserve task utility while reducing reconstruction leakage.

Why it matters: text-only data-loss-prevention is insufficient for multi-agent systems that share model internals, embeddings, memories, summaries, or compressed state. The data boundary has moved below text.

How it fits into the strategy stack: LCGuard belongs in agent containment and sovereign AI infrastructure. It says operators need policy over latent state transfer, not just chat messages, API calls, and files.

Practical tools, repos, and methodologies worth exploring:

- forbid cross-principal KV/cache sharing unless the runtime can label source, destination, sensitivity, and retention;
- treat KV caches, embeddings, summaries, and compressed memory as data artifacts with provenance;
- test reconstruction leakage before enabling latent communication;
- keep text-channel and latent-channel audit trails separate but linked;
- prefer explicit text/tool communication when auditability matters more than cache efficiency.

Implementability score: 0.42

Core source: [LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems](https://arxiv.org/abs/2605.22786v1)

## Agent security needs stateful evasion tests plus live MCP-client inventory

A3S-Bench shows that agent attacks are not only single-turn prompt injections. The paper defines temporal, spatial, and semantic evasion: malicious intent can be split across turns, hidden in external artifacts, or disguised inside benign task context. Its reported framework raises average risk-trigger rate from a 28.3% baseline to 52.6%, using 2,254 trajectories and 20 threat scenarios.

The implementable lesson is blunt: inspect the whole run. A safe-looking current instruction can become dangerous once previous turns, imported files, tool outputs, memory, and pending actions are considered.

The Hugging Face `evalstate/mcp-clients` dataset adds a second governance surface: live MCP clients advertise different capabilities and extensions, including UI, elicitation, roots, sampling, tasks, and experimental auth. That dataset was last modified on 2026-05-23 and gives operators a low-friction way to monitor client heterogeneity instead of pretending “MCP client” is one uniform capability class.

Why it matters: gateway policy needs two inputs at once: stateful adversarial traces and actual client capability telemetry. Otherwise a gateway can enforce clean-looking tool auth while missing the attack path or the client feature that made it possible.

How it fits into the strategy stack: this belongs in agent gateway governance and network containment. The control plane should know what client is connected, what capabilities it claims, what state/artifact path influenced an action, and whether the trajectory matches known evasion patterns.

Practical tools, repos, and methodologies worth exploring:

- run temporal/spatial/semantic evasion tests against staging agents;
- label trace segments by source, artifact, turn, memory object, and tool output;
- scan imported PDFs, spreadsheets, code repos, and web pages as possible spatial-evasion carriers;
- inventory MCP client names, versions, and advertised capabilities;
- gate high-risk features such as UI rendering, elicitation, roots, sampling, and experimental auth by client identity;
- add canary payloads that only become malicious when combined across turns or artifacts.

Implementability score: 0.74

Core sources:

- [Benchmarking Autonomous Agents against Temporal, Spatial, and Semantic Evasions](https://arxiv.org/abs/2605.22321v1)
- [antgroup/Agent3Sigma-Stage](https://github.com/antgroup/Agent3Sigma-Stage)
- [evalstate/mcp-clients dataset](https://huggingface.co/datasets/evalstate/mcp-clients)
