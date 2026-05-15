# Strategy Daily Analysis: 2026-05-07

Today's strategy signal is that agent safety is moving into the execution path. The important question is not only whether the model is aligned in a benchmark. It is whether the deployed system can intercept dangerous tool calls, reproduce adversarial scenarios, and collect evidence at the interaction and deployment levels.

## Runtime safety has to intercept tool calls before execution

Core sources:
- [AgentTrust: Runtime Safety Evaluation and Interception for AI Agent Tool Use](https://arxiv.org/abs/2605.04785)
- [DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents](https://arxiv.org/abs/2605.04808)
- [BillChan226/dtap-neurips](https://github.com/BillChan226/dtap-neurips)
- [Deployment-Relevant Alignment Cannot Be Inferred from Model-Level Evaluation Alone](https://arxiv.org/abs/2605.04454)

AgentTrust is the most practical governance signal today. It puts a safety layer directly in front of side-effecting tool calls: shell commands, file operations, HTTP requests, and database queries. Instead of scoring the agent after harm occurs, it intercepts the proposed action and returns a structured verdict: allow, warn, block, or review. The paper combines shell deobfuscation, safer-action suggestions, multi-step RiskChain detection, and an LLM judge only for ambiguous cases.

DTap supplies the other missing piece: controllable, interactive red-team environments for agents. Its paper covers 14 domains and more than 50 simulated environments, while the public repo exposes a task-runner shape for benign and malicious tasks across domains such as workflow and CRM. That turns agent red-teaming from one-off prompt games into repeatable environment tests.

The deployment-alignment paper is the strategy frame: model-level benchmarks do not prove deployment-level alignment. Alignment claims should identify which level produced the evidence: model, response, interaction, or deployment. AgentTrust and DTap are concrete examples of the higher levels becoming buildable.

Why it matters: agents are starting to operate with irreversible side effects. A sandbox controls where code runs, but it often does not understand what an action means. A generic refusal prompt can miss obfuscated shell commands, staged exfiltration, or context-dependent tool misuse. Runtime interception plus deployment-like red-team fixtures is the control layer operators actually need.

How it fits into strategy: this is agent gateway governance becoming an execution firewall. The gateway should not only route tools; it should normalize proposed actions, classify risk, attach policy evidence, require review for ambiguous/high-risk transitions, and preserve verdicts in the trace.

Implementable tools, repos, or methodologies worth exploring now:
- put a policy/interception layer before shell, filesystem, HTTP, database, email, payment, and deployment tools
- normalize shell and URL actions before judging them; do not judge only the raw string
- return structured verdicts: allow, warn, block, review, safer alternative, policy reason, and evidence path
- build DTap-style benign/malicious task suites for the team's own workflows
- use OPA/Cedar or custom policy rules for deterministic high-risk actions, with an LLM judge reserved for ambiguous meaning
- report safety evidence by level: model, response, interaction, and deployment

Implementability score: 0.66

A useful first version is very doable with wrappers, policy rules, shell normalization, and recorded review gates. Full benchmark-grade red-team environments and multi-step attack-chain detection are architecture-heavy, but the execution-path pattern should be adopted now.
