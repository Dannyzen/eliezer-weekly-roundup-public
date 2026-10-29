# AgenticAI Daily Analysis, 2026-10-29

The strongest new evidence says long-running agents need explicit work structure and longitudinal tests. A good single-turn result does not prove that an agent can preserve unfinished work, extend its own earlier code, or obey a multi-step protocol under pressure.

## 1. Compile the work tree into context

Spine represents nested work as a persistent execution tree. Before each model call, it keeps unfinished scopes in detail and replaces completed scopes with their submitted results. The same agent can open and close nested scopes locally, while independent scopes can still be delegated.

On SWE-Milestone with GPT-5.6 Sol, SpineCodex resolved 19 of 98 milestones, compared with 14 for native Codex and 17 for recursive subagents. It reduced total cost by 32.4% versus native Codex and 73.7% versus recursive subagents. Across the Pi integration, it improved SWE-Milestone Score by 9.5% to 17.5% and ProgramBench test-pass rate by 4.3% to 8.7% across evaluated models.

Why it matters: context management should preserve task topology and completion state. Flat history compression can discard unfinished evidence, while mandatory delegation makes every subtask boundary pay coordination overhead.

Fit in the stack: context economy, long-horizon harnesses, and multi-agent orchestration.

Implementable now:
- represent work as typed scopes with parent, status, evidence, and submitted result;
- retain detailed interactions only for unfinished scopes;
- replace completed scopes with immutable result objects;
- choose local execution or delegation independently from task decomposition;
- measure task score and total cost together.

Artifact status: paper methodology inspected. No external code was cloned, installed, imported, or executed during this scan.

Implementability score: 0.78

Core source: [Spine v1](https://arxiv.org/abs/2610.37224v1)

## 2. Test coding agents across feature evolution

FeatureArc evaluates 10 coding agents on 73 manually reviewed feature-evolution tasks with 2 to 10 stages. Agents work in one persistent session and carry their own earlier code forward. Pooled success fell from 62.7% on the first stage to 28.5% when the complete feature was tested on final code. Inherited defects appeared in 72.9% of failed later stages, and agents left an earlier error unnoticed about 95% of the time after a failed stage.

Why it matters: issue-level benchmarks miss regression accumulation. A coding agent can solve isolated requests while degrading a feature across successive changes.

Fit in the stack: coding-agent quality gates, stateful integration verification, and release evidence.

Implementable now:
- build staged feature fixtures from real repository history;
- carry the agent's own workspace forward across stages;
- test new behavior and all prior behavior after every stage;
- withhold hidden-test feedback when evaluating autonomous maintenance;
- report first-stage success, final-feature success, and inherited-defect rate separately.

Artifact status: paper methodology inspected. No public implementation artifact was verified in this scan.

Implementability score: 0.83

Core source: [FeatureArc v1](https://arxiv.org/abs/2610.37434v1)

## 3. Enforce consequential conversations as typed sessions

Concordat defines an agent interface as a finite-state protocol. Each turn exposes only legal tools, rejects illegal calls before side effects, reserves designated decisions for humans, and splits token and tool budgets linearly across handoffs.

On 50 airline tasks with customers pressuring agents to skip confirmation, the standard agent made unconfirmed changes in 13 of 50 tasks with GPT-4.1 and 29 of 128 task-runs with Claude Haiku 5.5. Concordat made none, with no significant task-success loss. The benchmark's normal reward missed most violations.

Why it matters: prompt rules are advisory. Runtime state machines can make ordering, approval, least privilege, and budget constraints executable.

Fit in the stack: sessionful loops, execution control, and policy enforcement.

Implementable now:
- declare legal actions and transitions for consequential workflows;
- expose tools from the current state instead of the full catalog;
- represent human approval as a distinct transition;
- reject illegal effects before tool dispatch;
- split budgets so parent and child cannot spend the same allocation twice.

Weakest point: the paper is a single-author preprint and the repository labels itself pre-alpha. The public Apache-2.0 repository had one GitHub star when inspected.

Artifact status: repository contents inspected read-only. No external source was cloned, installed, imported, or executed.

Implementability score: 0.79

Core sources: [Concordat paper v1](https://arxiv.org/abs/2610.37461v1), [public repository](https://github.com/miladsikaroudi/concordat)

## Working conclusion

Structure work before compressing it, test features across their full evolution, and enforce consequential dialogue as an executable protocol. These controls move reliability from prompt prose into runtime state and longitudinal evidence.
