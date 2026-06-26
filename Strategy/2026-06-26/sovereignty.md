# Strategy Daily Scan: 2026-06-26

Today's strategic signal is that the agent authority boundary is becoming formal. Natural-language instructions are being compiled into policies, and MCP poisoning is moving from one obvious malicious tool to coordinated tool sets that defeat naive review.

## Agent instructions are becoming policy-as-code

Core source: [Autoformalization of Agent Instructions into Policy-as-Code](https://arxiv.org/abs/2606.26649v1)
Implementation artifact: [sondera-ai/sondera-harness-python](https://github.com/sondera-ai/sondera-harness-python)

### What changed

The paper proposes an autoformalization pipeline that translates system prompts, MCP tool definitions, and natural-language policy corpora into Cedar policies through a generator-critic loop. The hard critic checks syntax, schemas, contradictions, and vacuous policies. The soft critic checks semantic alignment against the source policy. The resulting policy set is enforced by an external deterministic policy engine before agent actions execute.

That is the right shape. Prompt guardrails and classifiers remain useful as signal, but they are not a safety boundary. A high-stakes agent needs an external policy decision before it touches a tool, a file, a record, or a message channel.

### Why it matters

The strategic move is not "let an LLM write security policy and trust it." The strategic move is to use the LLM as a compiler front-end, then force output through a deterministic language, a parser, a schema checker, contradiction checks, and runtime enforcement outside the agent process.

The verified GitHub artifact is not just a paper stub. The `sondera-harness-python` README describes a Python harness that evaluates Cedar policies before agent actions execute, works with LangGraph, ADK, Strands, or custom agents, and gives the agent a denial reason when policy blocks an action.

### How it fits into the strategic layer

This belongs in Strategy because it changes where sovereignty lives. If policy lives inside the prompt, the model owns the boundary. If policy lives in Cedar, OPA, OpenFGA, IAM, or a brokered gateway, the platform owns the boundary.

### Practical tools, repos, and methodologies worth exploring

- Cedar policies for tool calls, file writes, memory writes, external sends, and privileged reads
- generator-critic policy compilation from prompts, MCP tool schemas, and written policy docs
- deterministic hard critics for syntax, schema mismatch, contradictions, and vacuous policies
- soft critics for policy coverage and semantic alignment, treated as review signal, not authority
- policy denial reasons returned to agents as recoverable feedback
- runtime traces that store policy ID, input fields, verdict, denial reason, and final effect

### Implementability score

0.76

The ingredients exist now: Cedar, policy engines, Python harnesses, MCP tool schemas, and agent middleware. The hard work is building the policy corpus, mapping natural language to enforceable resource/action fields, and testing whether generated policies actually cover edge cases.

## ShareLock shows MCP poisoning is a multi-tool problem

Core source: [ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP](https://arxiv.org/abs/2606.27027v1)

### What changed

ShareLock distributes a hidden malicious instruction across multiple benign-looking MCP tool descriptions using Shamir threshold sharing. A later trigger reconstructs the instruction when enough poisoned tool descriptions are observed together. The paper reports more than 90% average attack success across four multi-tool domains and two MCP clients, while outperforming single-tool poisoning in description-based detection.

The important correction is simple: reviewing each tool description in isolation is not enough. An MCP catalog can be safe-looking one tool at a time and malicious as a set.

### Why it matters

MCP is becoming the default shape for connecting agents to tools, storage, and workflows. Most governance proposals still inspect tools independently: name, description, schema, server identity, permissions, and maybe a prompt-injection classifier. ShareLock says the gateway has to reason over enabled-tool combinations, update events, and reconstruction triggers.

This is a Strategy finding because it is about the authority plane. The bad outcome is not a weird prompt response. It is a tool catalog that can coordinate hidden instructions across allowed tools, then steer privileged execution after admission.

### Practical tools, repos, and methodologies worth exploring

- enabled-tool graph analysis before admitting MCP bundles
- semantic diffing on tool-description updates, not only first install
- cross-tool prompt-injection classifiers that inspect combinations and shared phrases
- canary MCP clients that assemble candidate tool subsets and search for reconstructed intent
- policy that blocks untrusted server updates from silently changing tool descriptions
- gateway traces that record tool catalog version, enabled set, update epoch, selected tools, and denied combinations

### Implementability score

0.46

The defense pattern is implementable, but the paper is mainly a threat model and benchmark. Builders can add catalog-level diffing, update gates, and cross-tool fuzzing now. Proving robust detection against threshold-split instructions still needs deeper research and adversarial fixtures.
