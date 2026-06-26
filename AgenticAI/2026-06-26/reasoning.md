# AgenticAI Daily Scan: 2026-06-26

Today's implementation signal is about the layer above the model. Coding agents, RAG agents, and tool-heavy systems are failing at control surfaces that builders can actually own: config files, red-team search, tool admission, and replayable evidence.

## Coding-agent configs need a deterministic control plane

Core source: [A Deterministic Control Plane for LLM Coding Agents](https://arxiv.org/abs/2606.26924v1)

### What changed

The paper studies 10,008 public GitHub repositories and 6,145 agent configuration files, then makes the uncomfortable point explicit: the rules files, IDE markdown, and agent definitions that steer coding agents are propagating like undeclared dependencies. It reports 10.1% exact SHA-256 duplicates across independent repositories, 75.5% of clone pairs crossing organizational boundaries, rare revision, and permission boundaries in less than 1% of agent configs compared with 33% of Actions workflows.

That is the right target. The operational risk is not only that a coding agent makes a bad edit. The risk is that the file that tells the agent how to act is unmanaged, copied from elsewhere, rarely reviewed, and not bound to permissions, tests, or provenance.

### Why it matters

Coding agents now get filesystem and shell authority through repo-local instructions. If those instructions are treated as prose instead of supply-chain objects, the harness cannot answer basic questions:

- where did this instruction come from?
- who approved the permission it implies?
- which tools, files, and tests does it authorize?
- which IDE or agent target was compiled from the canonical definition?
- did the instruction drift from the version that passed eval?

The paper's proposed Rel(AI)Build control plane is useful even if the exact architecture is not production-ready. It gives the right primitives: content-addressed definitions, lockfiles, audit logs, tiered permissions, attack-derived blocklists, phase gates, requirement-to-file-to-test traceability, IDE target compilation, and drift detection.

### How it fits into the stack

This belongs in AgenticAI because it turns coding-agent harness configuration into an implementation layer. It also touches Strategy because permissions and provenance are authority surfaces, but the immediate builder move is concrete: stop letting every repo invent its own untyped agent rules file.

### Practical tools, repos, and methodologies worth exploring

- canonical agent definition files compiled into Cursor, Claude Code, Copilot, OpenHands, Codex, and IDE-specific targets
- SHA-256 or SLSA-style provenance for agent rules and skills
- lockfiles for agent configuration dependencies
- policy checks for allowed shell commands, write paths, network access, and approval requirements
- OpenTelemetry spans that include agent config hash, rules version, target IDE, and permission profile
- CI checks that fail on unreviewed agent-config drift
- replay packs linking requirement, touched files, tests, and final policy verdicts

### Implementability score

0.64

A lightweight version is implementable now with git, hashing, CI, config linting, OpenTelemetry, and policy-as-code. The hard part is standardizing a canonical definition across heterogeneous agent clients and proving that permission declarations map to actual runtime enforcement.

## MIRROR makes agentic RAG red-teaming cross-surface and novelty-aware

Core source: [MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG](https://arxiv.org/abs/2606.26793v1)
Implementation artifact: [FujitsuResearch/mirror](https://github.com/FujitsuResearch/mirror)

### What changed

MIRROR targets multimodal agentic RAG systems, not just prompt-only chatbots. The paper names the expanded attack surface directly: text poisoning, image injection, direct-query attacks, and orchestrator-level tool manipulation. Its core move is a memory-guided Monte Carlo tree search that uses retrieved examples as priors while a deterministic Novelty Gate rejects candidate attacks that duplicate the retrieved set.

The novelty gate matters because the authors measured 73-84% exact duplication in existing text-poisoning benchmarks. A red-team harness that mostly recycles known attacks can look strong while failing to explore new exploit paths.

### Why it matters

Agentic RAG deployments are moving into incident response, compliance, and security operations. In that setting the retriever, tool selector, intermediate context, and orchestrator are all part of the attack surface. MIRROR is useful because it evaluates across surfaces and reports whether the search is producing novel attack candidates, not only whether an attack succeeds.

The public repository is also usefully honest. Its README says it includes deterministic novelty gate code, memory-guided PUCT utilities, metrics, table verification scripts, and config files, while excluding private credentials, internal documents, payload records, and per-case logs. That is the right public-artifact boundary for security research.

### How it fits into the stack

This is trajectory-aware evaluation for RAG agents. The target is not a single answer. It is a sequence of retrieval, context assembly, modality handling, tool choice, and final response. The red-team system has to preserve enough evidence to know which surface failed.

### Practical tools, repos, and methodologies worth exploring

- deterministic novelty gates for internal prompt-injection and RAG-poisoning test suites
- attack search over retrieval context, direct user input, image payloads, and tool-orchestrator state
- DupBench-style duplicate-rate reporting before trusting red-team results
- attack success rate, Novel-ASR, query cost, cross-surface variance, and replayability as separate metrics
- payload-free public artifacts paired with private internal run records
- fixtures that test whether mitigations generalize across text, image, direct-query, and tool-selection surfaces

### Implementability score

0.72

The pattern is implementable now because the public repo exposes the novelty gate, search utilities, metrics, and verification scripts. Full replication needs private or synthetic RAG targets, per-surface payload design, and careful handling of security-sensitive run records.
