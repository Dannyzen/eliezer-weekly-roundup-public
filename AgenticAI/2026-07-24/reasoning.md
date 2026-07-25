# AgenticAI Weekly Analysis - 2026-07-24

## Weekly thesis

The unit of trustworthy autonomy is not the model turn. It is an evidence-bearing boundary object that connects a claim to observable state. This week's strongest work converges on that pattern from three directions: trajectory-backed test oracles, deterministic verification of native artifacts, and harness-owned state adapters.

An agent can sound finished while the harness is stuck, pass a test suite that never exercises its changed lines, or produce a plausible document whose formulas and metadata are wrong. The repair is not another general-purpose judge. Preserve the exact run, identify the changed surface, and verify the resulting state with domain-native checks.

## The test oracle must include the trajectory and changed surface

[Understanding Agent-Reactive Bugs at the Model-Harness Boundary](https://arxiv.org/abs/2607.15684v1) manually studies 255 issue reports from Codex, Gemini CLI, LangChain, and CrewAI. It finds that model output and harness behavior jointly create failures that neither layer explains alone. The daily analysis identified 108 silent errors: the final answer can be fluent while tool logs, workspace state, or workflow progress show that the claimed work did not happen.

[Test Coverage Analysis of Agentic Pull Requests](https://arxiv.org/abs/2607.18057v1) gives the same problem a concrete software release surface. Across 4,882 agent-generated pull requests, only 49.6 percent of code-changing pull requests include test changes. Existing tests execute 61.5 percent of changed Java lines and 27.0 percent of changed Python lines. In 64.8 percent of Python pull requests, no changed line is executed by the existing suite. Error-handling miss rates reach 86.0 percent in Java and 81.0 percent in Python.

Why it matters: a passing final answer and a passing repository test suite are both weak receipts unless they cover the trajectory and the changed behavior. The oracle needs model output, harness reactions, tool receipts, state deltas, changed-line coverage, and post-state under one run identity.

Stack fit:
- harness layer owns run identity and captures every model and tool transition;
- evaluation layer compares narration with tool receipts and final state;
- CI layer gates changed lines, with stricter thresholds for error handling and privileged paths;
- observability layer makes silent model-harness divergence queryable.

Implementable now:
1. Attach one run ID to prompts, model responses, tool calls, retries, state deltas, and final narration.
2. Add diff coverage to coding-agent pull requests and reject uncovered high-risk branches.
3. Create fixtures where the model claims success but the tool or workspace receipt shows failure.
4. Preserve failed stochastic responses so harness bugs can be replayed rather than paraphrased.

Tools, repositories, and methodologies:
- coverage.py, JaCoCo, diff-cover, OpenTelemetry, structured tool receipts, workspace snapshots
- [SageSELab/Agentic-Pull-Request-Test-Coverage](https://github.com/SageSELab/Agentic-Pull-Request-Test-Coverage), inspected read-only; populated analysis code and data, but no repository license was exposed

Implementability score: **0.89**

## Native artifacts need deterministic state verification

[DocOps](https://arxiv.org/abs/2607.19865v1) treats Word, Excel, PowerPoint, and PDF outputs as structured native state rather than screenshots or prose. Its public benchmark packages 210 executable tasks with checks for formulas, styles, metadata, bookmarks, and document structure. The best reported configuration reaches 0.671 overall, while long-range workflows expose state-tracking collapse, shallow verification, and destructive metadata edits.

[Copy-on-Write Scoring](https://arxiv.org/abs/2607.14336v1) applies the same idea to application data. It places each agent session on an isolated PostgreSQL changes layer, compares agent and human reference sessions, and scores structural and content differences without committing agent writes to the base state.

Why it matters: artifact quality is not a visual impression. A document, database mutation, or generated work product must be bound to an exact digest or isolated state branch, then tested through the semantics of that artifact.

Stack fit:
- sandbox layer creates a reversible work surface;
- artifact layer preserves native structure and exact digests;
- verifier layer applies deterministic, domain-specific assertions;
- release layer commits only a verified artifact or state delta.

Implementable now:
1. Select ten representative DocOps tasks for document-agent regression testing.
2. Bind every verifier report to the SHA-256 digest of the artifact it examined.
3. Put one PostgreSQL-backed workflow behind disposable copy-on-write state.
4. Compare final state, extra writes, missing writes, and operation order before promotion.

Tools, repositories, and methodologies:
- [icip-cas/DocOps](https://github.com/icip-cas/DocOps), Apache-2.0, populated tasks, harnesses, Docker support, and package verifier
- [trail-ml/agent-cow-python](https://github.com/trail-ml/agent-cow-python)
- LibreOffice headless checks, OOXML inspection, PDF metadata tests, PostgreSQL views and row-level scoring

Implementability score: **0.85**

## Harness state should be owned by runtime adapters

Three findings move hidden agent behavior into runtime-owned objects. Microsoft's [stable Agent Framework harness](https://devblogs.microsoft.com/agent-framework/the-microsoft-agent-framework-harness-is-now-released/) packages per-service-call history, compaction, todo and plan state, file memory, approvals, and OpenTelemetry behind one harness surface. [OpenForgeRL](https://arxiv.org/abs/2607.21557v1) records production-style harness model calls through a proxy and isolates rollouts in remote containers so standard RL infrastructure can train on the deployed loop. [Delivery, Not Storage](https://arxiv.org/abs/2607.20972v1) makes memory delivery a deterministic harness event rather than a voluntary model action.

The memory evidence is intentionally narrow but sharp: zero voluntary memory operations over 114 turns; conversation-only facts disappear at the first summary and remain absent in 106 of 108 compactions; harness-owned injection delivers seeded facts through all 138 compact-resumes. OpenForgeRL reports strong claw and GUI results, but no exact public implementation artifact resolved from the primary pages and error recovery remains weak.

Why it matters: training, compaction, memory, and replay cannot depend on model cooperation. The harness must own the state transition and expose it as a testable adapter.

Stack fit:
- model proxy records calls without changing the harness contract;
- rollout adapter binds environment identity, tool receipts, rewards, and state deltas;
- memory policy evaluates typed path, symbol, semantic, event, and temporal cues;
- replay layer reproduces compaction, resume, and error-recovery paths.

Implementable now:
1. Wrap one coding harness model endpoint with a recording proxy.
2. Store model calls, environment digest, tool receipts, rewards, and state deltas under one rollout ID.
3. Add deterministic memory triggers and log candidate, injected, rejected, and consumed memory IDs.
4. Test crash, resume, compaction, approval replay, and false memory injection on a stable reference harness.

Tools, repositories, and methodologies:
- [microsoft/agent-framework](https://github.com/microsoft/agent-framework), veRL, Kubernetes jobs, container-per-rollout isolation, OpenTelemetry
- event hooks, compaction callbacks, deterministic cue fixtures, harness ablations

Implementability score: **0.70**

## Implementation order

1. Instrument one real workflow with a complete run identity.
2. Add changed-surface and native-artifact assertions.
3. Move memory and compaction events into deterministic harness policy.
4. Only then use captured rollouts for routing, fine-tuning, or RL.

This order is deliberate. Better training on an unverified harness scales the wrong behavior faster.

## Evidence and caveats

- The papers above were checked at immutable arXiv v1 URLs. OpenSkillRisk had advanced to v2, but it is analyzed in Strategy and the cited v1 claims remain version-bound.
- GitHub artifacts were inspected through metadata, root trees, README content, and licenses only. No external source was cloned, installed, imported, built, or executed.
- The agentic pull-request artifact is populated but lacks a visible repository license, so treat it as study material rather than reusable code.
- OpenForgeRL calls itself open source in the abstract, but no exact public project URL resolved from the primary pages during this run.
- NotebookLM remained disabled. No podcast command, audio artifact, or manifest edit was made.
