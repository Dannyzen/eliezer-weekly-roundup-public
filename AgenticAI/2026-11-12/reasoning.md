# AgenticAI Daily Analysis: 2026-11-12

The strongest implementation signal is to compile repeated agent behavior into deterministic workflows and evaluate agents inside the messy workspaces where real delivery happens.

## 1. Compile repeated agent traces into planner-free workflows

ReTrace converts a natural-language SOP and a few agent traces into an intermediate rule document, then synthesizes an executable workflow. Each rule links back to the reasoning and tool evidence that produced it. At runtime, code selects the next step. Individual tools may still call models, but the orchestration path no longer needs an LLM planner.

On 79 production procedures, the compiled workflows reached 93.8 percent completion versus 96.8 percent for the agent, with 24 percent lower cost per task. On tau2-bench, they reached 75.8 percent task success versus 80.6 percent for the agent and ran in 1.3 seconds instead of 170 seconds. Three repair rounds lifted two-trace workflows from 66.7 percent to 81.2 percent. The paper estimates that its public-benchmark construction cost would break even after about 75 enterprise executions, while explicitly warning that the real production construction cost was not measured.

Why it matters:
- recurring procedures can graduate from model-selected orchestration to code-selected execution;
- the intermediate rule document preserves evidence and stays portable across workflow engines;
- traces need reasoning, tool calls, inputs, and outcomes to recover decision conditions;
- labeled failures become compiler-repair fixtures instead of permanent runtime planner cost.

Implementable now:
- pick one high-volume SOP with stable tools and clear completion checks;
- retain reasoning, tool calls, input provenance, outputs, and outcomes from successful and failed runs;
- compile a typed rule document with guards, input sources, completion checks, and evidence links;
- generate code or a workflow graph, then test it on held-out cases and counterfactual branches;
- keep an escape path for genuinely novel cases instead of forcing every input through the compiled path.

The weakest point is artifact availability. The paper exposes a detailed method and public benchmark results, but no paper-owned implementation repository resolved. The method also gives up several points of unrepaired task success in exchange for speed and cost. This is a bounded workflow-compilation pattern, not evidence that open-ended agents should be removed from every loop.

Implementability score: 0.72

Artifact status: paper and HTML method inspected. No public implementation artifact resolved, and no external code was executed.

First listed: 2026-11-11. Submitted: 2026-11-10 18:49:47 UTC.

Durable topic: [Decision-state compilation](../decision-state-compilation/decision-state-compilation.md)

Core source: [ReTrace paper v1](https://arxiv.org/abs/2611.14492v1)

## 2. Test research agents in inherited workspaces

ARE-bench evaluates 75 tasks reconstructed from real researcher sessions and full in-progress workspaces. The tasks span seven research stages, 33 requirements, 150 sub-requirements, and 1,173 binary checklist items. Each workspace is replayed to the exact request boundary without cleanup, preserving unfinished files, outdated versions, failed attempts, and earlier agent-written material.

The strongest evaluated model passed every checklist item on 66.2 percent of tasks. Three models passed about 69 percent when grading only the immediate delivery contract and general norms, then fell to 28.4 to 40.0 percent when historical decisions and material workspace requirements were included. That gap is the useful result: clean-room task success can hide failures to respect inherited state.

Why it matters:
- long-horizon delivery depends on prior decisions that are not restated in the latest prompt;
- stale and failed artifacts are part of the operating environment;
- evaluation must distinguish immediate request compliance from historical and workspace constraints;
- task completion is only credible when the final artifact preserves the project's state contract.

Implementable now:
- construct evaluation snapshots from real sessions at a known request boundary;
- preserve the complete workspace, including misleading and obsolete artifacts;
- compile separate checklist groups for the current request, standing decisions, material state, and general norms;
- require all critical checklist items to pass rather than averaging away a broken dependency;
- compare clean-room and inherited-workspace scores to expose context-handling gaps.

The full benchmark is a research data collection, not a drop-in test suite for another organization. The practical pattern is reusable, but local fixtures must be built from consented projects and scrubbed for private data.

Implementability score: 0.79

Artifact status: paper and HTML methodology verified. No public benchmark repository resolved from the paper, and no external code was executed.

First listed: 2026-11-11. Submitted: 2026-11-10 17:21:31 UTC.

Core source: [ARE-bench paper v1](https://arxiv.org/abs/2611.14364v1)

## Working conclusion

Use agents to discover and handle variance, then compile stable paths into evidence-linked workflows. Evaluate both layers against inherited project state. The goal is cheaper execution without erasing the historical constraints that make the work correct.
