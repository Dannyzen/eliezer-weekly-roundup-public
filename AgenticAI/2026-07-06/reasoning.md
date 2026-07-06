# AgenticAI Daily Analysis, 2026-07-06

Today's signal is process-preserving control. Skill use, coding conversations, and coding-agent oversight all fail when the runtime only checks the final answer. The useful layer is the one that preserves process evidence and gates each step before authority expands.

## Skill use needs process rubrics, not final verifier wins

Source link:
- SkillCoach: https://arxiv.org/abs/2607.01874v1

SkillCoach is useful because it targets the gap between task success and skill-use quality. A skill-using agent can eventually pass a final verifier while still selecting distractor skills, skipping required steps, composing workflows incorrectly, or omitting final checks. Final accuracy hides those defects.

The paper's control surface is the rubric. SkillCoach derives skill-grounded process rubrics from real rollouts, then evaluates trajectories along four dimensions: skill selection, skill following, skill composition, and skill-grounded reflection. It keeps the external verifier as a separate outcome signal, so process quality is not collapsed into accidental success.

Why it matters: skill libraries are becoming operational infrastructure. If the only score is final success, the registry cannot tell whether a skill was useful, redundant, harmful, or merely present while the model recovered through trial and error.

Fit in the stack: skills-as-control, agent harness architecture, trajectory-aware evaluation, and skill registry operations.

Practical implementation path:
- Log retrieved skill IDs, loaded body hashes, selected skill, rejected candidate skills, step-level compliance, validation checks, and final verifier result.
- Score skill selection, following, composition, and reflection separately.
- Keep final task success as an outcome metric, not as a proxy for process quality.
- Use failed and successful rollouts to evolve rubrics, but require human review before rubric changes become production gates.
- Feed high-quality trajectories into training or prompt improvement only when both process rubric and final verifier agree.

Tools, repos, and methodologies worth exploring now:
- Skill-grounded process rubrics for Hermes skills, MCP tool playbooks, and coding-agent skill packs.
- Per-skill validators that prove required files, schemas, checks, or side effects occurred.
- Registry dashboards that show skill utility, distractor frequency, omitted checks, and composition failures.

Implementability score: 0.70

This is implementable now as trace logging plus rubric scoring. The hard part is rubric quality: bad rubrics will teach agents to perform visible ceremony rather than do the right work.

## Multi-turn coding agents need regression gates

Source links:
- Regression Accumulation paper: https://arxiv.org/abs/2607.01855v1
- Artifact repository: https://anonymous.4open.science/r/multi-turn-llm-regression-E73E
- Bug taxonomy repository: https://anonymous.4open.science/r/multiturn-code-bugs

Regression Accumulation in Multi-Turn LLM Programming Conversations gives the cleanest implementation signal today. The paper turns coding chat into an 8-turn requirement-evolution problem and asks whether later turns preserve behavior established earlier. It builds 542 tasks from HumanEval+ and MBPP+, evaluates six LLMs across 26,016 turn instances, and checks whether current code still passes earlier tests at each turn.

The result is not subtle. Across models, 40 to 73 percent of tasks lose previously correct behavior over the full conversation. The dominant manual failure class is Cross-Turn Conflict, where later code conflicts with earlier requirements. The only tested mitigation that consistently improves all models is a Verification Gate: check new code against prior tests, then rollback and retry when earlier behavior breaks. The paper reports final-turn quality rising from 75.8 percent to 87.9 percent on DeepSeek-V3 and from 31.6 percent to 47.3 percent on Llama-3.1-8B.

Why it matters: coding-agent reliability is stateful. A model can look good on the latest request while silently breaking the contract it built two turns ago. Current-turn success is too weak for agentic programming.

Fit in the stack: coding-agent control plane, agent harness architecture, deterministic coverage gates, trajectory-aware evaluation, and sessionful-agent loops.

Practical implementation path:
- Store every accepted requirement as a session contract, not as chat history.
- Convert earlier requirements into replayable tests or invariants before applying later edits.
- Run prior tests plus new tests on every turn.
- Roll back and retry when prior behavior fails.
- Record which turn introduced the regression, which requirement broke, which gate caught it, and whether the retry preserved both old and new requirements.

Tools, repos, and methodologies worth exploring now:
- Multi-turn requirement-evolution fixtures modeled on HumanEval+/MBPP+ chains.
- Verification Gate policy in coding-agent harnesses.
- Git worktrees or patch stacks for cheap rollback per conversational turn.
- Regression taxonomy labels such as cross-turn conflict, over-specialization, validation drift, and refactor breakage.

Implementability score: 0.84

This is the highest score today because the control is ordinary engineering: keep prior tests, replay them, and roll back on regression. The harder part is converting natural-language requirements into stable tests or invariants.

## Coding-agent steerability belongs in the substrate

Source link:
- Steerability via constraints: https://arxiv.org/abs/2607.02389v1

Steerability via constraints argues that coding-agent oversight should not depend on unconstrained model behavior plus heroic human review. The paper's useful claim is that the old controls for human engineering teams also transfer to coding agents: access control, network policy, strict conventions, typed boundaries, layered docs, linters, and tool-enforced review surfaces.

The paper reports a controlled oversight experiment where a small reviewer model inspects a Python codebase with 11 inserted backdoors. Recall rises from 54.5 percent in the unconstrained no-tools condition to 90.9 percent with a constrained substrate plus a roughly 200-line docs CLI, with substrate and tools contributing independently.

Why it matters: a coding agent is easier to supervise when the environment is shaped for supervision. More reviewer tokens are weaker than fewer possible bad paths, better local docs, clearer invariants, and deterministic checks that expose suspicious changes.

Fit in the stack: coding-agent control plane, agent harness architecture, runtime governance, and agent static analysis.

Practical implementation path:
- Put coding agents inside constrained workspaces with explicit file, network, package, and command boundaries.
- Enforce style, type, dependency, and architecture constraints with tools, not reminder prose.
- Maintain local docs that expose module ownership, invariants, forbidden patterns, and threat surfaces.
- Give reviewer agents compact deterministic inspection tools instead of only raw file search.
- Treat substrate constraints as part of the evaluation condition when comparing agent performance.

Tools, repos, and methodologies worth exploring now:
- Type checkers, linters, architecture tests, dependency policies, protected paths, and network-deny defaults.
- Repo-local docs CLI or code-map CLI for reviewer agents.
- Static-analysis gates from the 2026-07-04 scan combined with regression gates from today.

Implementability score: 0.78

The principle is highly implementable with existing engineering tools. The specific experiment still needs independent reproduction and a public artifact before it should be treated as a benchmark.

## Watchlist, not promoted to top finding

EvoPolicyGym is worth tracking because it evaluates agents that repeatedly edit executable policies under a fixed interaction budget, then exposes trajectory-level diagnostics around budget allocation and feedback conversion. It has a public GitHub repo and Hugging Face dataset. I did not promote it above the top three AgenticAI findings because today's strongest implementation pattern is process preservation in real coding and skill workflows, not a new RL-style benchmark.

Sources:
- EvoPolicyGym paper: https://arxiv.org/abs/2607.02440v1
- EvoPolicyGym repository: https://github.com/Linzwcs/EvoPolicyGym
- EvoPolicyGym dataset: https://huggingface.co/datasets/linzw/EvoPolicyGym-Exp-data

## Working conclusion

The implementation thesis is that serious agents need process evidence before process authority. Skill selection, code evolution, and reviewer oversight should be measured at the step where they can fail, not only after the agent produces a plausible final artifact.
