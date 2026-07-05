# AgenticAI Daily Analysis, 2026-07-05

Today's signal is selective state under test. Memory state, reasoning budget, test evolution, and skill composition all need explicit evidence gates before the agent gets more autonomy.

## Memory systems need failure-mode tests, not only recall tests

Source links:
- MemSyco-Bench paper: https://arxiv.org/abs/2607.01071v2
- MemSyco-Bench repository: https://github.com/XMUDeepLIT/MemSyco-Bench
- A-TMA paper: https://arxiv.org/abs/2607.01935v1

MemSyco-Bench is useful because it evaluates how retrieved memories change downstream decisions, not only whether a memory can be stored or retrieved. Its five tracks cover objective fact judgment, contextual scope control, memory-evidence conflict, valid memory selection, and personalized memory use. The public repository exposes 1,550 samples, task data, baseline adapters, and evaluation code.

A-TMA names the complementary failure: ghost memory. Old, current, and transition facts can coexist in the memory bank, mix during retrieval, and mislead the answer model. Its ATMA overlay keeps superseded and transition records visible, labels evidence as current, historical, or transition state, and evaluates bank maintenance, retrieval, and answer-time resolution separately. The paper reports Graphiti+ATMA improving LTP conflict accuracy by 0.240 absolute and raising LoCoMo temporal F1 from 0.0295 to 0.1705.

Why it matters: memory quality cannot be measured by recall alone. A memory system can retrieve the right-looking item and still over-apply it, obey stale user preference over objective evidence, ignore supersession, or hide where the failure happened.

Fit in the stack: memory systems, context economy, trajectory-aware evaluation, memory authority, and shared-state agents.

Practical implementation path:
- Add memory-use tests where the correct answer is to ignore or scope a recalled memory.
- Track memory state roles: current, superseded, historical, transition, conflicting, and personalized-only.
- Split memory evaluation into write-path bank maintenance, retrieval selection, and answer-time resolution.
- Preserve source event, supersession lineage, state role, and requested state view with every memory packet.
- Treat personalization memories as scoped hints, not factual authority.

Tools, repos, and methodologies worth exploring now:
- `XMUDeepLIT/MemSyco-Bench` for benchmark data, baseline adapters, and memory-induced sycophancy tests.
- ATMA's state-role overlay as a lightweight schema for existing memory stores.
- LTP-style conflict-heavy fixtures for profile updates, project facts, dependency versions, and user preferences.
- Graphiti-style temporal graph memory only when state labels and evaluation hooks are explicit.

Implementability score: 0.76

This is implementable now because MemSyco-Bench is public and the first ATMA-style controls are schema and evaluation changes. Full guarantees still need every summary, retrieval, and answer path to preserve state roles.

## Reasoning budgets should be routed before extra tools

Source links:
- Reasoning effort study: https://arxiv.org/abs/2607.02436v1
- Zenodo dataset and artifacts: https://doi.org/10.5281/zenodo.21134406

The coding-agent result today is blunt: more tools did not buy reliability in this controlled setting, but more reasoning did. The study ran 90 independent agents on the same real-time retrospective board specification, scored each run on a fixed 14-criterion, 42-point functional rubric, and reviewed visual quality.

The key operational findings are specific enough to use. Browser-based testing raised cost by 42 to 68 percent without improving functional score or first-try reliability. Raising reasoning effort from High to xHigh lifted first-try perfect runs from 28 percent to 89 percent, cut corrective prompts about fivefold, and cost 9 to 29 percent more. A design prompt improved visual quality from 3.0 to 4.5 on a 5-point scale, but did not improve function, and a one-paragraph paraphrase reproduced the lift.

Why it matters: a serious coding-agent router should not reflexively add tool access. It should identify the failure class first. If first-run failures are reasoning failures, buy reasoning effort or a stronger model. If failures are visual polish, add a style directive. If failures are deployment boundaries, add deterministic environment checks.

Fit in the stack: coding-agent control plane, model-router governance, agent serving runtime, and agent harness architecture.

Practical implementation path:
- Track failures by criterion, not only total score.
- Log requested reasoning effort, effective reasoning effort, tool exposure, run cost, corrective prompts, and first-run pass status.
- Add a router rule: increase reasoning effort before adding broad tool access when the failure cluster is planning or integration.
- Keep browser testing as a targeted verifier for UI-visible or browser-state defects, not a default cost multiplier.
- Use short design directives for visual quality, then separately verify function.

Tools, repos, and methodologies worth exploring now:
- The Zenodo artifact set for a repeatable retrospective-board coding benchmark.
- Per-criterion scoring rubrics for internal coding-agent evals.
- Router policies that compare reasoning effort, model class, tool access, and cost on matched tasks.
- First-try perfect-run rate as a practical metric for agent workflow quality.

Implementability score: 0.81

This is highly implementable. The evidence artifact is public, and the first policy change is logging and routing discipline, not new infrastructure.

## Live test co-evolution benchmarks expose coding-agent regressions

Source links:
- TestEvo-Bench paper: https://arxiv.org/abs/2607.02469v1
- TestEvo-Bench site: https://www.testevo-bench.com/
- Prompt Coverage Adequacy: https://arxiv.org/abs/2607.02057v1

TestEvo-Bench is the stronger coding-agent evaluation signal because it evaluates whether tests evolve with code, not only whether the final patch passes a static benchmark. It builds two tracks: test generation for new behavior and test update for changed behavior. The current snapshot has 746 test-generation tasks and 509 test-update tasks mined from 59,950 candidate co-evolution records across 152 open-source Java projects.

The live-benchmark property matters. Each task records the timestamp of code and test changes so evaluators can restrict tasks to changes after a model's training cutoff. It also packages environment configuration for execution-grounded metrics such as pass rate, coverage, and mutation score. The paper reports state-of-the-art agents reaching up to 77.5 percent success on test generation and 74.6 percent on test update, while performance drops on the most recent tasks and under tight cost limits.

Prompt Coverage Adequacy adds the metric layer. It treats the prompt or task description as a primary artifact and asks whether the test suite covers the requirements expressed in that prompt. The reported attention-boosting instantiation finds over 30 percent more faults than traditional code coverage when used to guide test generation.

Why it matters: coding-agent evals that ignore test evolution can reward brittle patches. The next useful harness gate is not only "did tests pass?" It is "did the agent update the tests that define the new behavior, and did those tests cover the intent?"

Fit in the stack: agent harness architecture, trajectory-aware evaluation, coding-agent control plane, and deterministic coverage gates.

Practical implementation path:
- Mine internal code changes into paired code-plus-test evolution tasks.
- Score test generation and test update separately.
- Record task timestamp, training-cutoff eligibility, environment setup, pass rate, coverage, mutation score, and cost.
- Add prompt-coverage or requirement-coverage checks for agent-authored tests.
- Penalize smoke-only tests and tests that pass by self-mocking the changed behavior.

Tools, repos, and methodologies worth exploring now:
- TestEvo-Bench's live task and data-explorer methodology.
- Mutation testing for high-value agent-authored test diffs.
- Prompt Coverage Adequacy as a research direction for requirement-to-test coverage.
- Internal post-cutoff task slices for repo-specific coding-agent regression packs.

Implementability score: 0.68

The methodology is implementable now, but a useful internal version needs mining, environment packaging, mutation tooling, and leakage-aware task timestamps.

## Skill composition needs fuzzing before marketplace admission

Source link:
- SkillFuzz: https://arxiv.org/abs/2607.02345v1

SkillFuzz closes a gap left by isolated skill review. A skill can be benign alone and still become dangerous when co-activated with another skill. The paper names the failure implicit intent: a composed skill set redirects the agent toward an unintended objective even when individual skills pass isolated review.

The approach is practical enough to copy in shape. It treats skill compositions as the unit under test, extracts structured skill contracts, uses contract-guided Monte Carlo Tree Search to prioritize risky co-activations, and compares planning artifacts against a skill-free baseline as a differential oracle. Across representative skill-marketplace workloads, SkillFuzz discovers more than 1,000 distinct implicit intents under a fixed query budget and confirms more than 80 percent of highest-risk flagged compositions during execution-time validation.

Why it matters: skill admission cannot stop at per-skill provenance, static scanning, or sandbox detonation. The loaded set is the authority surface. Marketplace operators need to know which combinations create new intent, tool pressure, or data-flow risk.

Fit in the stack: skills-as-control, agent gateway governance, runtime governance, and skill marketplace operations.

Practical implementation path:
- Extract skill contracts with declared purpose, preconditions, side effects, tool scopes, file scopes, memory scopes, and expected validators.
- Generate composition candidates from task class, shared tools, overlapping files, memory access, and conflicting goals.
- Compare plans with and without the composed skill set before execution.
- Promote high-risk combinations into sandbox execution with fake secrets and marker files.
- Store composition verdicts in the skill registry, not only individual skill verdicts.

Tools, repos, and methodologies worth exploring now:
- Contract-guided fuzzing for skill catalogs.
- Differential planning oracles against a no-skill baseline.
- Monte Carlo Tree Search over high-risk co-activation graphs.
- Composition deny lists and review queues in the skill registry.

Implementability score: 0.62

A first version is feasible with contract extraction, planner diffs, and a small skill catalog. Production coverage is harder because composition space grows quickly and high-risk behavior can be trigger-dependent.

## GitHub watchlist, not promoted to top finding

`alibaba/page-agent` was the strongest open-source tooling signal in GitHub trending: an in-page JavaScript GUI agent with optional Chrome extension and beta MCP server. It is worth evaluating as a browser-copilot implementation surface, but it was not promoted above the research findings because today's durable signal is control-plane evidence, not another browser-agent wrapper.

Source: https://github.com/alibaba/page-agent

## Working conclusion

The daily implementation thesis is selective evidence before autonomy. Test memory influence, route reasoning budget deliberately, evaluate code and tests as a coupled system, and fuzz skill sets before marketplace skills inherit real authority.
