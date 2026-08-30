# AgenticAI Daily Analysis - 2026-08-19

## Scope

The Wednesday arXiv listing was live. The selected papers were submitted between 2026-08-17 12:00 UTC and 2026-08-19 12:00 UTC and first listed on 2026-08-19. Blogwatcher was unavailable, so arXiv, official release metadata, Hugging Face, GitHub, and official web sources were checked directly. GitHub and Hugging Face discovery signals were promoted only after primary-source verification. No external repository was cloned, installed, built, imported, or executed.

Deep Dive Wednesday selected TRUSS as the week's strongest finding. The durable analysis lives in Strategy because skill loading is an admission decision, not only a generation method. This file keeps the implementable AgenticAI findings and points to that control-plane writeup.

## Wednesday deep dive: skill packages need an admission loop

TRUSS treats automated skill generation as a joint functional and safety verification problem. The candidate is a complete package with a frozen digest. A static gate inspects claims and declared capabilities. A shadow agent then exercises the package through brokered tools. Residual failures become a structured revision spec, not a later hope that the task still finished.

This belongs in the implementation layer because the first build is concrete: digest the package, inspect bundled files, run a disposable shadow agent, compare against an empty-skill control, and keep blocked requests in the record. The governance claim, and why this beat HarnessRisk, audience checks, lowering, and plugin packaging, is in the Strategy deep dive.

Analysis: [skill admission control](../../Strategy/skill-admission-control/skill-admission-control.md#august-19-deep-dive-why-truss-is-the-weeks-control-primitive)

Implementability score: 0.72

Core source: https://arxiv.org/abs/2608.17588v1

## Harness safety is a lifecycle, not a model score

HarnessRisk treats the harness as the unit of safety evaluation. Configuration, capability extension, runtime operation, state persistence, action control, and incident recovery are separate phases, not one prompt-injection score.

The protocol is concrete. There are 128 sandboxed cases. Each pairs a benign owner objective with an adversarial instruction inside an untrusted workflow artifact. The agent gets three owner turns, case-specific files and tools, persistent state, and mocked services. Every run starts from a fresh environment with real network access disabled. Trajectories are scored on Utility, Attack Success Rate, Persistence, and Detection.

The measured result is the point. Across OpenClaw, Hermes, and Nanobot, six models, and 14 model-harness configurations, attack success ranged from 12.6% to 80.9% while utility stayed between 75.0% and 97.6%. Configuration was the weakest phase in all three harnesses. Some configurations detected risk in more than 90% of runs and still completed the attack.

Why it matters: a finished task is not a safe run. Detection is not containment. A model ranking that ignores harness phase will rank the wrong thing. For Deep Dive Wednesday, HarnessRisk is the post-install score. It does not decide whether a new skill package should be mounted.

Practical paths:
- score utility, attack success, persistence, and detection separately;
- add fixtures for config mutation, capability install, memory writeback, action admission, and recovery;
- treat owner-authorized workflows as an attack surface, not a trusted envelope;
- compare the same model across more than one harness before claiming a safety ranking;
- fail closed when a detected risk still has an executable path.

Artifact status: the project page, MIT implementation repository, and public dataset were resolved read-only. The repository is populated, with adapters, case runners, and data files. Nothing was executed.

Implementability score: 0.86

Core sources:
- https://arxiv.org/abs/2608.17597v1
- https://baiyajing.github.io/harness-risk/
- https://github.com/Baiyajing/HarnessRisk
- https://huggingface.co/datasets/YajingB/HarnessRisk

## Skill code needs checked lowering before dispatch

SkillEffect starts from a serving fact: even a semantically correct skill program can load an entire input and blow the memory budget of one tool call. The paper's answer is not a larger sandbox. It is checked lowering.

The runtime keeps a recoverable source relation, an audited bounded implementation, and a registered output postcondition. Before execution authority is granted, an independent checker rebuilds the proposed lowering from the submitted program and the immutable input. Eager plans can be rewritten onto a bounded implementation when the source relation matches.

The integration evidence is useful. In the native Qwen harness, all 16 schema-valid actions requested bounded execution, and all 48 capped repeats verified and committed. In the external smolagents 1.26.0 path, every otherwise valid call requested eager access. The registry lowered all 16 before dispatch, and all 48 capped repeats verified. A deployment-owned typed tool surface is simpler, but SkillEffect is the path for code-generating agents and mixed eager/bounded interfaces.

Why it matters: skills are becoming executable programs. If the model chooses the access mode, the sandbox budget is just a hope. The control plane should own physical execution shape. Lowering happens after a skill is trusted enough to run. TRUSS decides whether that skill may be trusted at all.

Practical paths:
- register each tool with an eager form, a bounded form, and a source recognizer;
- rebuild proposed lowerings from the program and immutable input before dispatch;
- default sandboxes to 128-512 MiB class limits and treat OOM as an admission failure;
- keep the tool result schema separate from the model's final answer;
- replay the same bounded action in fresh cgroups before trusting a skill path.

Artifact status: no exact public implementation repository was resolved from the primary arXiv page or PDF during this read-only scan. Cite the paper, not a missing repo.

Implementability score: 0.62

Core source:
- https://arxiv.org/abs/2608.17007v1

## Working conclusion

Harnesses and skills are execution substrates. Measure them by phase, not by completed tasks, and do not let generated code choose its own memory shape. The week's deeper implementation claim is that a skill package needs a digest, a shadow run, and a residual record before it becomes part of either substrate.
