# AgenticAI Daily Analysis - 2026-07-24

## Verdict

The strongest implementation signal is that the harness should own both the training boundary and the memory delivery boundary. If either depends on the agent voluntarily exposing its state, the system cannot reliably train or remind it.

OpenForgeRL makes real harness rollouts visible to standard RL infrastructure. Delivery, Not Storage shows why memory retrieval should be triggered by runtime state rather than model discretion.

## Scan boundary

- arXiv exposed a real Friday, 2026-07-24 listing section across AI, language, machine learning, software engineering, security, and multi-agent systems.
- OpenForgeRL and Delivery, Not Storage were both submitted on 2026-07-23 and first listed on 2026-07-24.
- Their primary PDFs were downloaded as documents on Bigs and checked with `pdftotext -layout`.
- Hugging Face, GitHub, official release feeds, and GitHub metadata were checked. `blogwatcher-cli` was unavailable, so official feeds were read directly.
- Public repositories were inspected through metadata and documentation only. No external repository was cloned, installed, built, imported, or executed.

## Harness-native training needs an explicit rollout adapter

Core source: [OpenForgeRL](https://arxiv.org/abs/2607.21557v1)

Submission: 2026-07-23 17:38:30 UTC. First listed: 2026-07-24.

### What it found

OpenForgeRL separates real agent execution from the RL trainer. A lightweight proxy serves model calls from Claude Code, Codex, OpenClaw-style, and GUI harnesses while recording training trajectories. A Kubernetes orchestrator gives each rollout its own remote container. The resulting records feed a standard trainer such as veRL without forcing the production harness into the trainer process.

The paper trains two model families with hundreds to a few thousand tasks. OpenForgeClaw reports 31.7 pass^3 and 55.9 pass@3 on ClawEval plus 33.7 on QwenClawBench. OpenForgeGUI reports 37.7 on OSWorld-Verified, 63.0 on Online-Mind2Web, and 72.3 on WebVoyager. The behavioral analysis says RL improves self-verification, tool coverage, and multi-step completion, while error recovery remains weak.

The architecture is the important part: model calls, harness events, environment identity, rewards, and resulting state become one rollout object. The primary pages claim open-source code, data, and models, but expose no exact OpenForge repository or model URL. The paper links public benchmark and baseline artifacts, not a verified project artifact for this framework.

### Why it matters

Training on simplified tool loops can optimize behavior that disappears inside the actual production harness. A rollout adapter makes the deployed harness the evaluation and training surface while keeping trainer integration standard.

### Fit in the stack

- **Harness architecture:** capture model calls, tool events, subagents, compaction, and environment state under one rollout identity.
- **RL training:** decouple distributed harness execution from policy optimization.
- **Sandboxing:** isolate each trajectory in a disposable environment.
- **Evaluation:** compare harnesses while holding model, task, budget, and reward fixed.

### Implementable now

1. Wrap one coding harness model endpoint with a recording proxy.
2. Emit request, response, tool receipt, state delta, reward, and environment digest under one rollout ID.
3. Run a small task set in disposable containers before attempting distributed training.
4. Replay the same policy through two harnesses to measure harness-induced behavior.
5. Add explicit error-recovery rewards instead of assuming broad RL gains cover recovery.

Tools and methodologies worth exploring:

- OpenForgeRL architecture, veRL, Kubernetes jobs, container-per-rollout isolation, OpenTelemetry, immutable trajectory stores, harness ablations

Implementability score: **0.63**

The adapter pattern is concrete, but full reproduction needs distributed infrastructure and a public project artifact was not resolved from the primary source.

## Working memory should be delivered by cues, not requested by the agent

Core source: [Delivery, Not Storage](https://arxiv.org/abs/2607.20972v1)

Submission: 2026-07-23 06:50:04 UTC. First listed: 2026-07-24.

### What it found

The paper separates deliberate document memory from incidental working memory. Its proposed runtime gives each memory explicit trigger conditions over path, symbol, semantic, event, and temporal cues. The harness evaluates those conditions and injects matching facts without waiting for the agent to search or call a memory tool.

In one controlled coding task, a pre-seeded store receives zero memory operations across 114 turns. Deterministic injection fires in every seeded run with zero reported false alarms. Thirty-nine percent of intra-session re-reads recover content already consumed before compaction. In the repeated-compaction probe, ten conversation-only facts disappear at the first summary and remain absent from 106 of 108 compactions, while harness-injected facts survive all 138 compact-resumes.

The result isolates a real failure mode, but the evidence is narrow: one author, one controlled coding task, no public implementation artifact, and no broad false-positive evaluation over diverse repositories.

### Why it matters

A memory store can be perfectly durable and still fail if the model never asks for the right fact. Retrieval policy belongs in the harness, where runtime events can be matched deterministically and measured independently from model behavior.

### Fit in the stack

- **Memory systems:** separate durable evidence from trigger and delivery policy.
- **Context economy:** inject only facts bound to the current path, symbol, event, or phase.
- **Compaction:** re-evaluate cues after every resume instead of trusting summaries.
- **Evaluation:** measure missed delivery, false delivery, re-read cost, and downstream behavior.

### Implementable now

1. Add typed triggers to a small set of repository-specific memory records.
2. Evaluate triggers on file open, symbol lookup, command failure, phase change, and compact-resume.
3. Log candidate matches, injected IDs, rejected IDs, token cost, and downstream use.
4. Compare voluntary retrieval, always-on injection, and cue-triggered injection on the same tasks.
5. Require evidence provenance and scope checks before any injected memory reaches the active context.

Tools and methodologies worth exploring:

- event hooks, path and symbol matchers, compaction-resume callbacks, deterministic trigger tests, memory provenance, false-injection fixtures

Implementability score: **0.61**

A rule-based pilot is straightforward, but the published evidence is too narrow to justify broad automatic injection without local false-positive testing.

## Watchlist not promoted

- [DynamicMCPBench](https://arxiv.org/abs/2607.20531v1) provides effect-scored evaluation across 24 models, 121 live MCP servers, and 750 tasks. It was submitted on 2026-07-10, and no public implementation repository resolved from the primary paper, so it is useful prior art rather than a top fresh finding.
- [Tencent WorkBuddy Bench](https://arxiv.org/abs/2607.20911v1) adds contamination-resistant coding-agent evaluation, but today’s harness and memory findings expose more reusable control boundaries.

## Working conclusion

The harness should capture what the agent does without requiring cooperation, and deliver what the agent needs without relying on voluntary recall. Make both boundaries explicit, typed, and replayable before adding more model autonomy.
