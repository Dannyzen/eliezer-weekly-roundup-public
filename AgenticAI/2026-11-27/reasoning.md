# Daily AgenticAI Analysis: 2026-11-27

## Thesis

Reliable agents need evidence-producing harnesses around their work. Today's strongest results turn patch minimality, memory failure diagnosis, and security reachability into explicit replay or audit procedures instead of relying on output quality alone.

## Patch size is the wrong over-editing metric

Delta Residue Attribution replays a resolved coding-agent trajectory, maps final patch blocks to the step that created them, removes each block, and reruns task tests. Across 7,660 resolved GitHub Copilot CLI trajectories from 18 frontier models, the study found that extra lines were often tests or documentation rather than unnecessary code. On SWE-bench Verified, 61% of extra lines were tests and 13% were documentation. Eleven of 18 models left less unneeded code than developer patches under the paper's necessity metric.

Why it matters: line count confuses useful evidence with risky scope. A release gate should ask whether each code block is behaviorally necessary and whether added tests actually detect regressions.

Fit into the stack: coding-agent control plane, trajectory replay, mutation testing, and merge evidence.

Practical tools and methods worth exploring now:
- preserve step-to-diff attribution in coding-agent traces;
- replay focused tests after removing suspicious patch blocks;
- use mutation testing to check whether agent-authored tests protect new code;
- report code, test, documentation, and configuration residue separately;
- treat a passing but reducible patch as review work, not an automatic rejection.

Artifact status: the paper studies GitHub Copilot CLI trajectories and cites public Copilot CLI and `mutmut` repositories, but no dedicated DRA implementation repository was identified. The method is reproducible engineering work rather than a drop-in package.

Implementability score: 0.78

Core source: [How Much Do Coding Agents Over-Edit, and Why? v1](https://arxiv.org/abs/2611.34875v1)

Supporting tools: [GitHub Copilot CLI](https://github.com/github/copilot-cli), [mutmut](https://github.com/boxed/mutmut)

## Memory optimization should diagnose where evidence disappeared

HoMe treats a long-running memory system as a harness made of construction, maintenance, retrieval, and answer-generation code, prompts, and configuration. Failed cases are traced to stages such as never written, overwritten, or stored but not retrieved. Candidate changes are gated by smoke tests, adaptive sampling, memory reuse, and session-level version diffs.

The authors evaluated six candidate harnesses per benchmark on ReMe using LongMemEval-S and BEAM. The selected harnesses improved over the original by 2.8 and 5.4 percentage points while using fewer query-time tokens. The BEAM-100K optimized harness also generalized to BEAM-1M, where conversations were about eight times longer on average.

Why it matters: memory quality cannot be improved safely by rewriting a summary prompt. The system needs stage-level failure labels, versioned state, and replayable evidence before changing construction or retrieval behavior.

Fit into the stack: memory systems, harness optimization, evaluation economics, and long-horizon observability.

Practical tools and methods worth exploring now:
- record write, supersession, retrieval, context-delivery, and answer stages separately;
- keep session-level memory diffs so each failure can be traced backward;
- reject broken candidate harnesses with cheap smoke tests before full replay;
- optimize for task score and query-token cost together;
- evaluate on held-out histories longer than the optimization set.

Artifact status: ReMe is public and its repository includes the HoMe benchmark split configuration. The external source was inspected read-only; no code was cloned or executed.

Implementability score: 0.72

Core source: [HoMe v1](https://arxiv.org/abs/2611.34624v1)

Implementation artifact: [agentscope-ai/ReMe](https://github.com/agentscope-ai/ReMe)

## Security findings need executable reachability proof

AgentLens builds an Audit Knowledge Graph from components, control and data flows, weaknesses, and guardrails. It derives candidate attack paths, generates path-specific payloads, and validates them in multi-turn scenarios. Across Aider, MetaGPT, Goose, Cline, and Roo-Code, it reported 44 execution-validated vulnerabilities, 3.67 times the count found by AgentFuzz, with 12 assigned CVE identifiers at publication time.

Why it matters: static warnings are hypotheses. Agent deployment gates need to prove that an attacker-controlled input can traverse real component interactions and reach a security-violating outcome despite existing defenses.

Fit into the stack: agent static analysis, executable security testing, provenance graphs, and release gating.

Practical tools and methods worth exploring now:
- model prompts, tools, files, APIs, permissions, and guardrails as one reachability graph;
- translate each high-risk path into a bounded executable audit scenario;
- require a receipt containing the path, payload class, observed effect, and defense state;
- keep static candidates separate from execution-validated vulnerabilities;
- run audits in isolated test environments because validation intentionally exercises dangerous paths.

Artifact status: the paper claims an anonymized 4open.science artifact with code, scripts, reproduction instructions, and proof-of-concept results. The URL returned HTTP 401 from this cron environment, so artifact contents were not independently inspected or executed.

Implementability score: 0.67

Core source: [AgentLens v1](https://arxiv.org/abs/2611.34380v1)

Research artifact: paper-claimed anonymized repository, access not verified from this environment.
