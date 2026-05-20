# Strategy Daily Analysis: 2026-05-16

Today’s strategy signal is that agent memory, skills, and MCP/tool surfaces are becoming authority-bearing infrastructure. The important question is no longer whether agents can remember or call tools. It is whether memory and skills can justify actions safely, whether preferences can cross projects without becoming hidden policy, and whether agent runtimes can enforce least privilege like operating systems do.

## Agent memory needs lineage gates before it can become authority

MemLineage is the strongest strategy source today because it treats memory poisoning as a chain-of-custody problem rather than a better-filtering problem. The proposed design attaches cryptographic provenance and LLM-mediated derivation lineage to memory entries, represents derivations as a DAG, and blocks sensitive actions when the active justification descends from an untrusted external ancestor. The key design move is subtle: the agent may still recall untrusted information, but that information cannot authorize high-risk action.

LiSA adds the adaptation layer. Instead of retraining a guardrail every time local policy changes, it stores sparse feedback as reusable policy abstractions and uses conservative evidence-aware gating before overriding the base guardrail. GitHub’s May 15 Copilot Memory update is the product signal: user-level preferences can now persist across repositories and Copilot agents, including stated and inferred preferences that users can review or delete.

Why it matters: memory is now an authorization input. If a persistent memory can influence file writes, shell commands, code review style, repo policy, cloud actions, or user-specific defaults, then it needs provenance, confidence, scope, and revocation. Cross-repository preferences are useful, but they also create a hidden policy plane unless they are inspectable and gated.

How it fits into the stack or strategy: this belongs in memory writeback, profile memory, guardrails, policy engines, and audit logs. Treat durable memory as a database row with lineage and authority limits, not as a blob of remembered text.

Implementable now:
- attach source, trust tier, timestamp, scope, confidence, and supersession metadata to every durable memory;
- separate benign recall from sensitive-action justification;
- require a policy gate when external or inferred memory influences writes, shell, credentials, payments, cloud resources, or durable preference changes;
- expose a review/delete UI for user-level memories and preferences;
- use conservative lower-bound or multi-evidence thresholds before adapting safety policy from sparse feedback.

Tools, repos, and methodologies worth exploring:
- Merkle-log or append-only audit trails for memory writes;
- derivation DAGs that track which retrieved memories influenced a new memory;
- Open Policy Agent or Cedar for sensitive-action gates;
- profile-memory review and deletion workflows;
- LiSA-style conservative policy induction for organization-specific guardrails.

Implementability score: 0.74

Core source links:
- https://arxiv.org/abs/2605.14421
- https://arxiv.org/abs/2605.14454
- https://github.blog/changelog/2026-05-15-copilot-memory-supports-user-preferences-for-pro-pro-users/

## Agent security is converging on OS permissions and semantic skill scanning

`Toward Securing AI Agents Like Operating Systems` frames agent security through OS concepts: resource isolation, privilege separation, mediated communication, and careful configuration. `Do Coding Agents Understand Least-Privilege Authorization?` makes the implementation problem concrete by introducing permission-boundary inference for coding agents: map a task and terminal environment to file-level read/write/execute policy. Its AuthBench result is a warning that models are not naturally reliable policy engines; some omit needed permissions, others grant unused sensitive access, and more reasoning can make each model more consistent in its own failure mode.

`Exploiting LLM Agent Supply Chains via Payload-less Skills` extends the same point to skill libraries. The dangerous payload may not be code. It can be natural-language “compliance” text that causes the agent to synthesize malicious behavior at runtime, bypassing scanners that only look for explicit AST/code signatures. Snyk’s Agent Scan is the practical demand signal: a real scanner now inventories agent components, MCP servers, and skills for prompt injections, tool poisoning, tool shadowing, toxic flows, malware payloads, credential handling, and hardcoded secrets. Its README also contains the operational caveat that scanning MCP configurations may execute the configured stdio MCP commands, so scans of untrusted configurations should run in a sandbox.

Why it matters: agent security is not prompt safety. It is runtime permissioning, local process control, skill supply-chain governance, and semantic inspection. A skill can be safe-looking text and still be an attack. A model can be asked for least privilege and still give an unsafe policy. A scanner can help, but even the scanner must be governed because MCP discovery can start processes.

How it fits into the stack or strategy: this belongs in the agent operating substrate: sandboxed workers, per-task file policies, skill manifests, MCP config review, semantic scanners, and execution mediation before tools run.

Implementable now:
- generate an initial permissive-enough policy, then audit it for unnecessary sensitive access before execution;
- classify files, tools, skills, MCP servers, and secrets by read/write/execute/network/credential authority;
- scan skills semantically, not only for code payloads;
- require sandboxed scanner runs for untrusted MCP configs because discovery can execute commands;
- preserve permission-policy decisions in the same trace as tool calls and approvals.

Tools, repos, and methodologies worth exploring:
- file-level read/write/execute policy manifests;
- OS sandbox users, containers, VMs, seccomp/AppArmor/Seatbelt, and network egress policy;
- Snyk Agent Scan for inventory and semantic scanning, run in a disposable environment for untrusted configs;
- semantic skill validators and fuzz fixtures;
- AuthBench-style permission-boundary tests before granting coding agents broad workspace access.

Implementability score: 0.66

Core source links:
- https://arxiv.org/abs/2605.14932
- https://arxiv.org/abs/2605.14859
- https://arxiv.org/abs/2605.14460
- https://github.com/snyk/agent-scan
