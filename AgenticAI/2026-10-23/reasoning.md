# AgenticAI Daily Analysis - 2026-10-23

## Route skill granularity at runtime and recover from failed macros

Adaptive Skill Granularity treats skill use as an execution policy rather than a retrieval decision. A coding agent can stay at primitive tool level, invoke a macro skill, or fall back from a failed macro to micro tools through a finite-state recovery path. The paper's deterministic protocol grades success, route match, transition correctness, recovery, steps, and token cost.

Why it matters: fixed macro execution saves cost when its assumptions hold and fails sharply when they do not. Fixed micro execution is robust and expensive. The useful control point is the transition between them, where the runtime can inspect task structure, observed state, and macro failure before selecting the next abstraction level.

Fit in the stack: this belongs between skill retrieval and tool execution. The skill catalog proposes capabilities; a runtime granularity controller decides how much procedure to bind into one action and whether to downgrade after failure.

Practical tools and methods worth exploring now:
- assign each macro skill explicit preconditions, postconditions, and fallback tools;
- log mode choice, transition reason, verifier result, and normalized cost;
- start with deterministic routing rules before learning from outcomes;
- require postcondition checks before treating a late macro error as failure;
- use the public repository as a read-only design reference before any isolated evaluation.

Evidence and caveat: the public repository is populated, but the reported fixed-versus-adaptive comparison uses 12 mixed tasks. The learned router reaches full success on that small evaluated set, which is promising evidence rather than broad generalization.

Implementability score: 0.78

Core sources:
- [paper v1](https://arxiv.org/abs/2610.31461v1)
- [public repository](https://github.com/Jayceon-3/Adaptive-Skill-Agent)

## Train agents against executable terminal state

ThinkingBox Training turns deterministic checks of final database state and side effects into reinforcement-learning rewards for multi-turn agents. On 507 held-out benchmark tasks with 20 attempts each, the reported Qwen3.8-27B checkpoint increased pass@1 from 51.70% to 60.78% and increased tasks passed on all 20 attempts from 38 to 107 after 50 GRPO steps.

Why it matters: a narrative judge can reward plausible completion language. Executable state checks bind reward to the resulting world. The strongest lesson is methodological: build deterministic outcome oracles first, then use the same oracle for evaluation, selection, and training.

Fit in the stack: terminal-state checks sit beneath model training and above the environment. They provide a common contract for pre-training task selection, rollout rewards, repeated evaluation, and release gating.

Practical tools and methods worth exploring now:
- define binary checks over database state, side effects, and required cleanup;
- keep simulated users separate from graders;
- measure pass@1, at-least-once success, and repeated success separately;
- freeze the selected training pool before optimization;
- exclude benchmark tasks from the training source.

Evidence and caveat: the public Microsoft repository contains the training integration, data-preparation guides, evaluation scripts, and a validated reference configuration. The reported run used 24 H100 GPUs and a private 187-task training pool. Pass@20 declined from 89.35% to 87.97%, so repeatability improved while breadth narrowed.

Implementability score: 0.62

Core sources:
- [implementation article](https://huggingface.co/blog/microsoft/thinkingbox-training)
- [public repository](https://github.com/microsoft/thinkingbox-training)
- [ThinkingBox paper v4](https://arxiv.org/abs/2608.19741v4)
