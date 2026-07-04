# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-04

### Agent program static analysis becomes the new preflight gate

Summary: AgentFlow and IAL-Scan make agent applications inspectable before execution. The practical pattern is an Agent Dependency Graph plus loop-bound coverage: recover agents, prompts, models, tools, memory, policies, handoffs, and repeated feedback paths before the runtime grants authority.

Analysis: [daily reasoning analysis](2026-07-04/reasoning.md#agent-program-static-analysis-becomes-the-new-preflight-gate)
Durable topics: [Agent Static Analysis](agent-static-analysis/agent-static-analysis.md), [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Sessionful Agent Loops](sessionful-agent-loops/sessionful-agent-loops.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [AgentFlow](https://arxiv.org/abs/2607.01640v1), [When Agents Do Not Stop](https://arxiv.org/abs/2607.01641v1)
Implementable now:
- parse framework-specific agent constructs into typed graph nodes and edges
- emit Agent BOM JSON in CI
- check prompt-to-tool and memory-to-tool taint paths
- prove loop-bound coverage for costly and side-effecting feedback paths
Tools, repos, and methodologies worth exploring:
- tree-sitter, CodeQL or Semgrep-style rules, framework-specific AST adapters, Agent BOM artifacts, loop-bound fixtures
Implementability score: 0.72

### Proxy benchmarks can make agent routing cheap enough to run continuously

Summary: PACE predicts expensive agentic benchmark performance from compact non-agentic proxy instances. This is useful for daily model-selection and router-shadowing loops where full SWE-Bench or GAIA-style rollouts are too slow and expensive.

Analysis: [daily reasoning analysis](2026-07-04/reasoning.md#proxy-benchmarks-can-make-agent-routing-cheap-enough-to-run-continuously)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Agent Serving Runtime](agent-serving-runtime/agent-serving-runtime.md), [Strategy Model Router Governance](../Strategy/model-router-governance/model-router-governance.md)
Core sources: [PACE paper](https://arxiv.org/abs/2607.02032v1), [neulab/pace](https://github.com/neulab/pace), [PACE-Bench dataset](https://huggingface.co/datasets/neulab/pace-bench)
Implementable now:
- run released PACE-Bench instances for candidate models
- compare predicted scores before router changes
- use proxy evals for daily regression and full agent evals for release gates
- log predicted score, cost, latency, and known proxy blind spots
Tools, repos, and methodologies worth exploring:
- neulab/pace, neulab/pace-bench, shadow routing, workflow-specific proxy suites, occasional full-eval calibration
Implementability score: 0.86

### Skill malware defeats static scanners, so skill admission needs detonation

Summary: Cloak and Detonate shows that payload-preserving transformations can bypass static skill scanners. The implementation correction is a behavior admission lane: sandbox untrusted skills, use fake secrets and marker files, and inspect file, process, context, and network flows before the skill gets real authority.

Analysis: [daily reasoning analysis](2026-07-04/reasoning.md#skill-malware-defeats-static-scanners-so-skill-admission-needs-detonation)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Sandbox-Native Agent Workers](sandbox-native-agent-workers/sandbox-native-agent-workers.md), [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Strategy Runtime Governance](../Strategy/runtime-governance/runtime-governance.md)
Core source: [Cloak and Detonate](https://arxiv.org/abs/2607.02357v1)
Implementable now:
- keep static skill scanning as first-pass triage
- run third-party skills in a network-denied or egress-logged sandbox
- seed fake secrets, marker files, and fake repositories into detonation runs
- store scanner output, sandbox trace ID, skill hash, script hash, and admission verdict
Tools, repos, and methodologies worth exploring:
- SkillSpector, sandbox workers, marker-based taint fixtures, egress traps, skill manifests and lockfiles
Implementability score: 0.64

## Supporting recent AgenticAI context

The 2026-07-03 weekly synthesis remains the broader structured map. The 2026-07-04 daily scan adds a more specific build order: recover the agent graph, bound the loops, run cheap proxy evals, and detonate untrusted skills before granting tool authority.
