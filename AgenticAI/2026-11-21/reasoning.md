# AgenticAI Daily Analysis: 2026-11-21

## Scope

Saturday has no new arXiv listing batch. These are Friday carry-forward signals and a 20 November Hugging Face release, selected because they add implementable evidence beyond the 20 November weekly synthesis. External repositories and artifact pages were inspected read-only. No external code was cloned or executed.

## 1. Evolve harnesses against requirements, not benchmark deltas

[Agentic Harness Engineering Beta](https://arxiv.org/abs/2611.24924v1) treats harness improvement as a requirements loop. Simulated users surface explicit and implicit needs, a role-separated team turns recurring needs into general changes, and selection requires evidence that the requirement was resolved. Benchmarks evaluate the result after evolution rather than choosing patches directly.

On 38 held-out tasks with GLM-5.3-Flash, the paper reports pass@1 rising from 21.9% to 33.3% with 40.8% fewer tokens than its Base Harness. In a blind human A/B test, users preferred AHE-Beta in 31 of 48 valid pairs. The released repository includes an offline scripted demo, experiment configurations, evidence collection, and a separate Harbor evaluation workflow. The artifact is early, with five stars and one release when inspected, so the method matters more than project adoption.

Why it matters: harness changes should enter through traceable requirements and leave through evidence packages. That is a stronger engineering boundary than optimizing one aggregate score, and it limits task-specific prompt patches.

Stack fit: harness architecture, user-driven evaluation, requirement intake, and change admission.

Practical methods and artifacts:
- convert repeated trajectory failures into evidence-backed issues
- consolidate issues by root cause before implementation
- require a requirement-specific proof package for merge
- keep held-out benchmark evaluation separate from patch selection
- inspect [Curry09/AHE-Beta](https://github.com/Curry09/AHE-Beta) read-only before any trial

Implementability score: 0.65

Core sources: [AHE-Beta paper v1](https://arxiv.org/abs/2611.24924v1), [AHE-Beta repository](https://github.com/Curry09/AHE-Beta)

## 2. Train the model inside the deployed harness

[Hugging Face harness adapters](https://huggingface.co/blog/harness-adapters-at-scale) makes the harness a training condition rather than an evaluation wrapper. The team trained Qwen3.8-27B LoRA adapters inside pi, Hermes Agent v0.22.6, and OpenCode, using the shipped tool loop in an OpenEnv sandbox. The pi adapter reportedly moved Terminal-Bench 2.1 from 39% to 55% pass@1 while reducing average tokens per task from 2.9K to 1.5K.

The strongest methodological detail is task admission. Of 1,127 Hub candidates, 858 passed validation; wrong-answer controls exposed tasks whose verifiers accepted incomplete or known-wrong solutions. The work also publishes adapters, GGUFs, training tasks, and a safeagents plugin. Out-of-distribution AutomationBench results stayed near the base model overall, with the Hermes adapter below it at 17.7% versus 23.0%, so the gains should be treated as harness-and-distribution specific.

Why it matters: model, harness, task distribution, verifier, and tool policy form one deployed system. Training a surrogate loop can optimize behavior that the real harness never produces.

Stack fit: model-harness co-design, executable evaluation environments, task validation, and cost-aware routing.

Practical methods and artifacts:
- replay the exact production harness in sandboxed training and evaluation
- validate reference, unfixed, known-wrong, and valid-alternative solutions
- measure pass rate, tool calls, blocked calls, tokens, and transfer separately
- use a cheap adapter bakeoff before considering full RL infrastructure
- inspect the [published adapter collection](https://huggingface.co/collections/harness-hub/qwen38-27b-harness-adapters) read-only

Implementability score: 0.45

Core sources: [Hugging Face harness-adapter report](https://huggingface.co/blog/harness-adapters-at-scale), [artifact collection](https://huggingface.co/collections/harness-hub/qwen38-27b-harness-adapters)

## Actionable cut

1. Turn repeated trajectory failures into requirement issues with exact evidence.
2. Separate requirement admission from held-out benchmark evaluation.
3. Validate task verifiers with known-wrong and valid-alternative controls.
4. Treat harness version, model version, task distribution, and tool policy as one evaluation identity.
