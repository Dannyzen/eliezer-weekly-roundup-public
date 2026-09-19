# AgenticAI Weekly Analysis - 2026-09-18

## Thesis

The agentic stack should preserve the process evidence that final answers erase. Evaluation, diagnosis, harness routing, and skill improvement become more reliable when trajectories, incidents, budgets, and mutations are explicit runtime objects.

## Evaluate the process, then replay the failure

### Finding

ParaRecover provides 10,626 faulted parallel tool-use cases across 14 error types. Models kept Pass@1 above 89% while average process scores stayed below 70, exposing weak localization and replanning behind successful completion. The SWE-bench resolution audit reaches the same conclusion from a different direction: among 254 submissions, the leading two Verified entries tied at 396 of 500 and all 29 examined frontier pairs were statistically unresolved.

AgentLSD adds adversarial task evidence. Across 3,061 trap trials on 11 web security challenges, clean agents captured 41% of flags, while deceptive artifacts added about 20 turns and 2,000 reasoning tokens even when the flag was recovered. Chronicle turns those failures into durable regression tests by recording nondeterministic boundaries and replaying only selected cut points against changed code. Its six incidents were stable across repeated replays, and selective tests caught every unsafe-action mutant while a fully stubbed baseline caught none.

### Why it matters

A correct final answer can hide a brittle process, wasted search, unsafe intermediate state, or an evaluation unable to distinguish systems. Terminal success is necessary, not sufficient.

### Stack fit

This belongs in trajectory-aware evaluation, incident replay testing, coding-agent control planes, and multi-agent orchestration. The canonical object is an evidence-bearing trajectory with process scores and replayable boundaries.

### Practical path now

- Inject intermediate faults and adversarial evidence into existing task fixtures.
- Score localization, dependency impact, repair minimality, invalid plans, rounds, cost, and terminal outcome separately.
- Replace small leaderboard rank differences with statistically separable tiers.
- Commit production incidents as immutable boundary envelopes.
- Keep only the code boundary under test live, then compare resulting effects deterministically.

Implementability score: 0.88

Core sources:
- [ParaRecover](https://arxiv.org/abs/2609.12345v1)
- [ParaRecover repository](https://github.com/gbw206/ParaRecover)
- [Coding Agents Have Converged](https://arxiv.org/abs/2609.17394v1)
- [Resolution audit repository](https://github.com/Adkid-Zephyr/resolution-audit)
- [AgentLSD](https://arxiv.org/abs/2609.19140v1)
- [AgentLSD repository](https://github.com/Golim/agent-lsd)
- [Chronicle](https://arxiv.org/abs/2609.20625v1)
- [Chronicle repository](https://github.com/theagentplane/chronicle)

## Treat the harness as a conditional policy

### Finding

A 176-setting study across four models and two coding benchmarks found no universal best harness. Context management mattered most under tight windows, deterministic elision should precede summarization, planning changed role with model capability, and tool richness needed to match shell proficiency.

COBRA-Skills applies the same conditional logic to skill optimization. It uses a reward predictor plus LinearUCB to spend evaluations on promising or uncertain candidates and reports 55% to 58% lower optimization cost than SkillOpt across six benchmarks and three target models. Difficulty-aware collaboration adds a topology gate: hierarchical collaboration cost about 9.95 times more tokens than a single call, while its gain rose from 2.4 pass@1 points on easy problems to 21.1 on hard ones.

### Why it matters

A fixed harness bakes model-specific and task-specific assumptions into the product. It can waste tokens on easy work, hide which component mattered, and turn one benchmark's scaffolding into a false universal.

### Stack fit

This belongs in agent harness architecture, model routing, and context economy. The runtime chooses prompt, planning, tool, memory, and collaboration policies from measured conditions under a fixed budget.

### Practical path now

- Run component ablations per model, task family, context window, and budget.
- Elide deterministic low-value context before model summarization.
- Allocate skill evaluations by expected value and uncertainty while preserving frozen holdouts.
- Default to one agent and route to multi-agent collaboration only when calibrated difficulty predicts value.
- Record the route, realized token spend, and outcome for later calibration.

Implementability score: 0.79

Core sources:
- [Harness design study](https://arxiv.org/abs/2609.20804v1)
- [COBRA-Skills](https://arxiv.org/abs/2609.11682v1)
- [COBRA-Skills repository](https://github.com/Jerry-LuP/COBRA-Skills)
- [Difficulty-aware multi-agent collaboration](https://arxiv.org/abs/2609.13890v1)

## Make diagnosis and serving consume runtime evidence

### Finding

Continual Search improved Opus-4.8 F1 from 0.478 to 0.620 on 50 MegaRCA-Mix failures with 286K-token median records by expanding evidence coverage from 70.8% to 97.4%. It did not reliably help short traces, so the useful control is not endless reasoning. It is a coverage gate that asks whether meaningful evidence remains unread.

Tool-progress research shows the same principle in serving. Explicit progress was several times to an order of magnitude more accurate than pre-call duration predictors at cache-decision points. Small progress hints reduced post-tool p90 time to first token by about 20.7% in the tested setup. AgentPProf then projects many runs onto stable semantic task stacks, making cross-run token and failure hotspots visible instead of leaving them buried in spans.

### Why it matters

The model turn is not the only place where useful evidence exists. Unread-log coverage, tool progress, and cross-run semantic profiles should shape search, cache, and diagnosis decisions without bloating model context.

### Stack fit

This belongs in agent serving runtimes, observability, and long-trace diagnosis. Runtime telemetry remains outside model context unless a policy selects it for the next decision.

### Practical path now

- Track unread evidence and stop diagnostic expansion when coverage gain disappears.
- Emit monotonic tool progress as runtime telemetry, not natural-language prompt content.
- Replay cache decisions offline against actual completion times.
- Aggregate tokens, latency, retries, and failures by stable semantic operation path.
- Keep raw traces for drill-down and derived profiles for comparison.

Implementability score: 0.81

Core sources:
- [Continual Search](https://arxiv.org/abs/2609.13463v1)
- [Tool-progress serving study](https://arxiv.org/abs/2609.18849v1)
- [MCP progress specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/progress)
- [AgentPProf](https://arxiv.org/abs/2609.20301v1)
- [AgentPProf guide](https://github.com/eunomia-bpf/agentsight/blob/master/docs/agentpprof.md)

## Mutate persistent skills through localized, reversible change sets

### Finding

Skill Issue evaluates repository guidance by reverse-applying merged pull requests at a frozen base commit and comparing generated skills against a seed. Its reported 4.9-point gain could not be separated from agent variance on 20 to 26-task holdouts, which makes the paired frozen-snapshot method more durable than the result.

SkillAA gives the mutable state a stronger internal structure. It separates applicability, procedure, exclusion, and dependency objects, routes a failure to one editable location or `NO_PATCH`, retests affected cases, rolls back harmful atomic groups, and commits only a net-positive merged graph.

### Why it matters

Blindly rewriting a skill after a failure destroys attribution and makes rollback ambiguous. A persistent skill is executable policy, so its update path should look like a small, evidence-bound software release.

### Stack fit

This belongs in skills-as-control, agent self-improvement, and coding-agent control planes. Skills are content-addressed graphs with stable object identities, affected-case tests, epoch commits, and prior-version rollback.

### Practical path now

- Bind each evaluation to one frozen repository and skill snapshot.
- Keep no-skill and prior-version controls.
- Give applicability, procedure, exclusion, and dependency records stable IDs.
- Route failures to the smallest editable object and allow `NO_PATCH`.
- Run localized regressions before an atomic epoch commit.

Implementability score: 0.70

The public SkillAA repository is populated and active, but GitHub did not expose a recognized license in the inspected metadata. Treat it as a methodology and research artifact until reuse rights and independent replication are clearer.

Core sources:
- [Skill Issue](https://arxiv.org/abs/2609.12742v1)
- [SkillAA](https://arxiv.org/abs/2609.20455v1)
- [SkillAA repository](https://github.com/Ziqiao-Shang/SkillAA)

## Working conclusion

The practical advantage does not come from making every agent reason longer. It comes from preserving the evidence final answers erase, then using that evidence to replay incidents, route harness policy, focus diagnosis, and constrain persistent change.
