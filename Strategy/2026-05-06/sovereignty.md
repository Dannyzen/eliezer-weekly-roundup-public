# Strategy Daily Analysis: 2026-05-06

Today's strategy signal is that agent security is moving away from generic safety prompts and toward runtime evidence. The best new work asks: which untrusted context influenced this decision, which memory preserved safety-critical state, and which deterministic gates checked code before an agent committed it?

## Provenance graphs and shadow memory are becoming the agent defense layer

Core sources:
- [ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection](https://arxiv.org/abs/2605.03378)
- [MAGE: Safeguarding LLM Agents against Long-Horizon Threats via Shadow Memory](https://arxiv.org/abs/2605.03228)
- [MEMSAD: Gradient-Coupled Anomaly Detection for Memory Poisoning in Retrieval-Augmented Agents](https://arxiv.org/abs/2605.03482)

ARGUS, MAGE, and MEMSAD all attack the same weakness from different angles: agents make decisions from dynamic context, tool outputs, memories, and retrieved content, but most defenses still inspect prompts or final actions too shallowly. ARGUS builds an influence provenance graph to check whether a decision is justified by trustworthy evidence before execution. MAGE keeps a safety-focused shadow memory across the full trajectory. MEMSAD formalizes retrieval-memory poisoning and proposes calibrated anomaly detection for persistent external memory.

Why it matters: long-running agents cannot be secured by static instructions alone. A malicious instruction can be hidden in retrieved context, survive into memory, or become relevant only after several benign-looking steps. The defense layer needs to remember safety-relevant facts, track influence from untrusted context, and audit decisions before high-risk execution.

How it fits into strategy: this extends agent network containment from cross-agent propagation into intra-agent causality. A governance layer should know not only what the agent did, but why the agent believed the action was justified and which pieces of untrusted state contributed to that belief.

Implementable tools, repos, or methodologies worth exploring now:
- tag retrieved documents, peer messages, tool outputs, and memories with provenance and trust tier
- build an influence graph from evidence objects to proposed decisions before privileged tool execution
- maintain a small safety shadow memory containing unresolved risks, constraints, prior refusals, credentials exposure, and user-approved boundaries
- add canary and poisoning tests to memory/RAG evaluation suites
- use policy-as-code gates to block high-risk actions when the supporting evidence path includes untrusted context without independent confirmation

Implementability score: 0.58

The first version is implementable with taint labels, trace metadata, retrieval provenance, and policy gates. The full ARGUS/MAGE/MEMSAD research stack is architecture-heavy: influence graphs, adaptive adversaries, memory-poisoning calibration, and utility preservation all need careful integration.

## Coding-agent security needs MCP-time and pre-commit gates

Core sources:
- [MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents](https://arxiv.org/abs/2605.03952)
- [Secret scanning with GitHub MCP Server is now generally available](https://github.blog/changelog/2026-05-05-secret-scanning-with-github-mcp-server-is-now-generally-available)
- [Dependency scanning with GitHub MCP Server is in public preview](https://github.blog/changelog/2026-05-05-dependency-scanning-with-github-mcp-server-is-in-public-preview)
- [github/github-mcp-server](https://github.com/github/github-mcp-server)

MOSAIC-Bench shows why prompt-level coding-agent safety is too weak: staged, innocuous-looking tickets can compose into exploitable software even when direct malicious prompts would be refused or hardened. The GitHub MCP Server updates are the product-side response pattern: move checks into the coding workflow itself. Secret scanning is now generally available through the MCP server, and dependency vulnerability scanning is in public preview through the Dependabot toolset.

Why it matters: coding agents increasingly act inside real repositories before a human has read every diff. If security checks are post-hoc, the agent can spend the whole session building a vulnerable chain and only discover the issue after the workflow has already shaped the code. Security gates need to run when the agent is about to commit, add dependencies, edit config, or handle secrets.

How it fits into strategy: this is gateway governance for developer workflows. MCP should not be only a convenience protocol for giving agents more tools. It should also be the place where agents invoke deterministic security checks, return structured findings, and preserve audit evidence in the trace.

Implementable tools, repos, or methodologies worth exploring now:
- install or enable the GitHub MCP Server in coding-agent environments
- require secret scanning before commit for agent-authored changes
- require dependency scanning when an agent adds or changes package manifests
- run adversarial reviewer or pentester-framed checks on multi-ticket code changes, not only single prompts
- preserve scan results, affected files, severity, and recommended fixed versions in the agent trace
- add deterministic exploit or regression oracles for high-risk staged changes

Implementability score: 0.88

The GitHub MCP pieces are ready enough to try now, and ordinary CI/pre-commit checks can cover much of the same ground. The harder part is MOSAIC-style staged vulnerability evaluation, but the immediate security move is straightforward: put deterministic scanners in the agent loop before commit.
