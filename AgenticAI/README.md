# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Friday synthesis, week ending 2026-07-10

### Executable preflight and harness contracts move runtime guarantees into code

Summary: AgentFlow, IAL-Scan, and From Prompts to Contracts point to the same implementation layer: extract the agent graph before execution, then enforce source scope, routing, trace hygiene, output shape, and loop bounds through code-owned contracts around the model.

Analysis: [weekly reasoning analysis](2026-07-10/reasoning.md#executable-preflight-and-harness-contracts-move-runtime-guarantees-into-code)
Durable topics: [Agent Static Analysis](agent-static-analysis/agent-static-analysis.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [AgentFlow](https://arxiv.org/abs/2607.01640v1), [IAL-Scan](https://arxiv.org/abs/2607.01641v1), [From Prompts to Contracts](https://arxiv.org/abs/2607.08028v1), [enterprise-llm-agent-harness](https://github.com/hammerbaki/enterprise-llm-agent-harness)
Implementable now:
- extract an Agent BOM for models, tools, memory, policies, handoffs, and effects
- add loop-bound coverage and contract-violation fixtures to CI
- validate source scope, output shape, recommendation language, and trace leakage outside the model
Tools, repos, and methodologies worth exploring:
- Agent Dependency Graph extraction, `hammerbaki/enterprise-llm-agent-harness`, JSON Schema or Pydantic, fault-injection tests, CI contract artifacts
Implementability score: 0.82

### Framework and trajectory evals make agent systems measurable

Summary: PACE, Kotlin SWE-bench, UniClawBench, ToolFailBench, Action-Graded Severity, and STRACE move evaluation from final answer scoring to system measurement. The model, framework, task world, tool-call phase, action effect, recovery loop, and causal failure slice become separate evidence objects.

Analysis: [weekly reasoning analysis](2026-07-10/reasoning.md#framework-and-trajectory-evals-make-agent-systems-measurable)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [PACE](https://arxiv.org/abs/2607.02032v1), [PACE repo](https://github.com/neulab/pace), [Kotlin SWE-bench](https://github.com/Kotlin/kotlin-swe-bench), [UniClawBench](https://arxiv.org/abs/2607.08768v1), [ToolFailBench](https://arxiv.org/abs/2607.04686v1), [Action-Graded Severity](https://arxiv.org/abs/2607.07474v1), [STRACE](https://arxiv.org/abs/2607.07702v1)
Implementable now:
- build a small internal capability pack with hidden checkpoints and artifact-state validation
- label tool failures by phase and risky actions by reversibility, scope, and privilege
- run identical tasks across scaffolds while holding the model fixed
Tools, repos, and methodologies worth exploring:
- `neulab/pace`, `Kotlin/kotlin-swe-bench`, `HKU-MMLab/UniClawBench`, `Harry-Ashley/action-graded-severity`, `moomight/STRACE`, hidden verifier services
Implementability score: 0.84

### Memory influence must be scoped, conflict-preserving, and allowed to abstain

Summary: MemSyco-Bench tests memory-induced sycophancy, A-TMA separates ghost state from current state, StateFuse preserves multi-agent memory conflicts, and Remember When It Matters turns recall into a selective intervention policy with an explicit remain-silent path.

Analysis: [weekly reasoning analysis](2026-07-10/reasoning.md#memory-influence-must-be-scoped-conflict-preserving-and-allowed-to-abstain)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
Core sources: [MemSyco-Bench](https://arxiv.org/abs/2607.01071v2), [MemSyco-Bench repo](https://github.com/XMUDeepLIT/MemSyco-Bench), [A-TMA](https://arxiv.org/abs/2607.01935v1), [StateFuse](https://arxiv.org/abs/2607.05844v1), [StateFuse repo](https://github.com/nZiben/statefuse), [Remember When It Matters](https://arxiv.org/abs/2607.08716v1)
Implementable now:
- tag memories as current, superseded, historical, transition, conflicting, or personalization-only
- store append-only memory operations with source event IDs and validity state
- run no-memory, passive, always-on, and selective-intervention ablations
Tools, repos, and methodologies worth exploring:
- `XMUDeepLIT/MemSyco-Bench`, `nZiben/statefuse`, typed memory packets, intervention-effect logs, Terminal-Bench-style fixtures
Artifact caveat: `yifannnwu/proactive-memory-agent` resolved but had no populated default branch during this synthesis.
Implementability score: 0.74

### Coding-agent reliability is process preservation

Summary: The week’s coding-agent work shows that reliability comes from preserving process evidence: route reasoning effort before adding broad tools, replay prior commitments on later turns, co-evolve tests with code, and constrain the substrate before asking reviewers to inspect unconstrained agent output.

Analysis: [weekly reasoning analysis](2026-07-10/reasoning.md#coding-agents-need-process-preservation-not-only-final-green-tests)
Durable topics: [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Sessionful Agent Loops](sessionful-agent-loops/sessionful-agent-loops.md)
Core sources: [Reasoning effort study](https://arxiv.org/abs/2607.02436v1), [Regression Accumulation](https://arxiv.org/abs/2607.01855v1), [TestEvo-Bench](https://arxiv.org/abs/2607.02469v1), [TestEvo-Bench site](https://www.testevo-bench.com/), [Prompt Coverage Adequacy](https://arxiv.org/abs/2607.02057v1), [Steerability via constraints](https://arxiv.org/abs/2607.02389v1)
Implementable now:
- route reasoning effort deliberately before adding browser, shell, or network access
- convert prior turns into tests, invariants, or acceptance checks
- score test generation and test update separately
Tools, repos, and methodologies worth exploring:
- TestEvo-Bench fixtures, prompt coverage metrics, multi-turn regression repositories, constrained workspaces, local docs CLIs, replayable repo-level tasks
Implementability score: 0.80

### Skills and tool surfaces need behavioral admission and composition testing

Summary: SkillCoach, Cloak and Detonate, SkillFuzz, and HalluSquatting frame skills and tools as authority-bearing supply chain. Final task success is not enough. Skill process, sandbox behavior, skill composition, and exact artifact identity need to be checked before production authority.

Analysis: [weekly reasoning analysis](2026-07-10/reasoning.md#skills-and-tool-surfaces-need-behavioral-admission-and-composition-testing)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Agent Static Analysis](agent-static-analysis/agent-static-analysis.md)
Core sources: [SkillCoach](https://arxiv.org/abs/2607.01874v1), [Cloak and Detonate](https://arxiv.org/abs/2607.02357v1), [SkillFuzz](https://arxiv.org/abs/2607.02345v1), [HalluSquatting](https://arxiv.org/abs/2607.07433v1)
Implementable now:
- attach process rubrics to skill traces
- detonate risky skills with fake secrets, marker files, egress traps, and OS-boundary traces
- block clone, install, skill-load, or MCP-server admission unless a trusted source supplied the exact artifact identity
Tools, repos, and methodologies worth exploring:
- SkillCoach-style rubrics, SkillDetonate-style sandboxes, SkillFuzz-style composition search, exact-source allowlists, package registry metadata checks
Implementability score: 0.68

## Supporting recent AgenticAI context

The week ending 2026-07-10 tightened the repo’s operating model: agents should be represented before execution, evaluated by process and effect, given memory only when it earns influence, and denied tool or skill authority unless provenance and behavior are inspectable.
