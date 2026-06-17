# AgenticAI Daily Analysis: 2026-06-17

Today's signal is that agent quality is moving from broad capability claims to evidence ownership. Tools, skills, traces, and tests are only useful when the runtime knows which source, skill, trajectory segment, or oracle carried the proof.

## MCP factuality needs source ownership, not pooled support

Core sources:
- ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents: https://arxiv.org/abs/2606.18037v1
- Zscaler agentic AI security platform announcement: https://www.zscaler.com/press/zscaler-unveils-new-product-innovations-secure-agentic-ai

ProvenanceGuard names a failure mode that source-grounded agents can hide: cross-source conflation. A claim can be supported somewhere in a pooled evidence packet while being attributed to the wrong source. That is especially relevant for MCP agents because they can query search, APIs, databases, clinical records, formulary tools, and enterprise systems in one run. The paper's verifier consumes captured MCP traces with stable tool IDs, source IDs, and raw outputs, decomposes answers into atomic claims, routes each claim to source-specific evidence, checks support, and compares the stated attribution against the routed source.

The verified result is useful but also humbling. On a 40-trace held-out split, ProvenanceGuard reaches block F1 0.802 and source accuracy 0.858 over 260 source-eligible claims. On a harder multi-source benchmark, block F1 remains 0.846, but source-plus-relation accuracy drops to 0.229. Exact source ownership is hard when sources are semantically close.

Why it matters: source-grounded agents are not verified because they cite links or because an answer is supported by some retrieved text. They are verified when each claim has a source-specific evidence path, stable source identity, and a verdict that can be replayed.

How it fits into the stack:
- MCP trace layer: tool ID, source ID, raw output, and claim routing become first-class fields.
- Factuality layer: support and source attribution are scored separately.
- Gateway layer: tool outputs need source identity before they can become answer evidence.
- Repair layer: blocked answers can be revised and re-verified instead of silently published.

Implementable now:
- require MCP tools to emit stable tool IDs, source IDs, and raw output references;
- decompose final answers into atomic claims before publication for high-risk workflows;
- route each claim back to source-specific evidence instead of pooled context;
- log source-attribution verdicts next to the final answer and trace ID;
- block or downgrade answers when the claim is supported but attributed to the wrong source.

Tools, repos, and methodologies worth exploring:
- MCP trace schemas, claim extraction, NLI or entailment checks, token-alignment evidence, source IDs, LangSmith or Langfuse trace exports, gateway-side evidence packets, provenance-aware citation checks.

Implementability score: 0.74

## Skill systems need compositional routing plus per-skill utility evals

Core sources:
- Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose: https://arxiv.org/abs/2606.18051v1
- A Framework for Evaluating Agentic Skills at Scale: https://arxiv.org/abs/2606.17819v1

Compositional Skill Routing formalizes a problem that shows up immediately in large skill libraries: real tasks need multiple skills in the right dependency order, not a single best-matching skill. SkillWeaver decomposes a complex query into atomic subtasks, retrieves skills with a bi-encoder and FAISS index, then composes an executable dependency-aware DAG. The CompSkillBench benchmark uses 300 compositional queries over 2,209 real MCP server skills across 24 categories from the public MCP ecosystem. The paper reports that standard decomposition reaches only 34.2% category recall at the step level, while iterative skill-aware decomposition improves decomposition accuracy from 51.0% to 67.7% in one iteration and reduces context window consumption by over 99%.

The agentic skills evaluation framework supplies the missing utility gate. It lets skill authors generate realistic tasks and rubrics from the skill content, then estimates skill utility by solving those tasks. The paper applies this to 500 real-world skills, generates 1,000 skill-derived tasks, and evaluates 19 agent-model configurations. The most important result is not a single winner. It is that models vary widely in how well they adhere to skill instructions, and skill access changes behavior compared with no-skill baselines.

Why it matters: skill libraries are becoming runtime infrastructure. The dangerous default is simple semantic retrieval: find one plausible skill, paste it into context, and hope the task decomposes itself. The better pattern is decompose, retrieve, compose, execute, and evaluate skill utility against no-skill and wrong-skill baselines.

How it fits into the stack:
- Skill retrieval layer: atomic subtasks and candidate skills are separate artifacts.
- Planner layer: retrieved skills become a dependency-aware plan, not loose context.
- Evaluation layer: individual skill value is measured with realistic task/rubric pairs.
- Context economy layer: full skill bodies load only when decomposition and policy justify them.

Implementable now:
- split skill metadata from full bodies and index metadata first;
- decompose tasks into atomic skill needs before retrieval;
- compose selected skills into a DAG with explicit dependencies and validators;
- keep no-skill, wrong-skill, thin-skill, and full-skill baselines for high-value skills;
- generate small skill-specific task suites and rubrics before promoting a skill to default use.

Tools, repos, and methodologies worth exploring:
- FAISS or pgvector indexes for skill metadata, DAG planners, MCP skill catalogs, skill manifests, rubric generation, paired trajectory comparison, no-skill baselines, progressive disclosure.

Implementability score: 0.76

## Evaluation needs trajectory preferences and oracle-aware test gates

Core sources:
- Offline Preference-Based Trajectory Evaluation: https://arxiv.org/abs/2606.17541v1
- All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code: https://arxiv.org/abs/2606.18168v1

Offline Preference-Based Trajectory Evaluation makes a direct attack on terminal-success scoring. The paper argues that offline agent evals collapse trajectories to final success and discard partial progress. Across diverse agentic and interactive benchmarks, standard success metrics produce tied comparisons on roughly 75% of instances, while trajectory-aware preferences reduce ties to roughly 35%. That turns the same offline data into a more discriminative ranking signal.

All Smoke, No Alarm exposes the coding-agent version of the same problem. Test-file presence is a weak proxy for verification strength. The study analyzes 86,156 test-file patches from 33,596 agent-authored pull requests across 2,807 repositories produced by OpenAI Codex, GitHub Copilot, Devin, Cursor, and Claude Code. It finds that 80.2% of agent-authored test patches contain weak or no explicit oracle signals. Strong oracle signals significantly improve merge likelihood after adjustment (OR 1.28, p < 0.001).

Why it matters: agent evaluation is failing at two levels. At the trajectory level, pass/fail loses information about partial progress and efficient recovery. At the coding level, "the agent added tests" can be theater if the tests execute code without checking behavior. A serious harness needs trajectory preferences and oracle-aware test gates.

How it fits into the stack:
- Evaluation layer: compare trajectories by progress and time-to-return, not only final outcome.
- Harness layer: test-generation steps need oracle-signal analysis before merge or completion.
- CI layer: test-file counts should be replaced by assertion/oracle-quality checks.
- Trace layer: partial progress, retries, failed attempts, and verification strength become release evidence.

Implementable now:
- store progress checkpoints and time-to-return profiles for agent runs;
- compare near-miss trajectories instead of treating all failures as equal;
- add a linter or review bot that classifies agent-authored tests by oracle strength;
- block agent-written tests that have no assertions, no expected-output checks, or only self-mocking behavior;
- score patch quality with test-oracle strength, not only test count or green CI.

Tools, repos, and methodologies worth exploring:
- pairwise preference evals, progress ledgers, trace checkpoints, assertion-density checks, mutation testing, property-based tests, CodeQL or AST rules for test oracles, CI gates for agent-authored diffs.

Implementability score: 0.86

## Watchlist

- Salesforce Agentforce Multi-Agent Orchestration is a market signal for primary-agent to specialist-agent routing with A2A support and observability: https://www.salesforce.com/agentforce/multi-agent-orchestration/
- Zscaler's AI Broker, Agent Registry, and AI Access Graph are a market signal that agent access, lineage, MCP/A2A traffic, and endpoint tool/plugin risk are being packaged as security-control-plane features: https://www.zscaler.com/press/zscaler-unveils-new-product-innovations-secure-agentic-ai
- Trustworthy self-composable BDaaS is relevant to multi-agent lifecycle orchestration, but it is too domain-broad for today's top set: https://arxiv.org/abs/2606.17915v1
- RubricsTree is relevant to rubric hierarchies for personal health agents, but it is domain-specific and less immediately reusable for the general stack than the skill and trajectory papers: https://arxiv.org/abs/2606.18203v1

## Scan quality note

This scan used arXiv API metadata plus PDF text verification for selected papers, Hugging Face RSS/blog extraction, GitHub Trending HTML and GitHub search as demand signals only, Google News RSS as lead discovery only, and managed web extraction for vendor/source pages. `blogwatcher-cli` was absent, so direct RSS/API retrieval was used. External repositories were not cloned, installed, built, imported, or executed.
