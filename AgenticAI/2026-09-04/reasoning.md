# AgenticAI Daily Analysis - 2026-09-04

## Passing functional tests is not enough for coding-agent acceptance

SWE-Gate splits repository-level repair into two executable oracles: a functional test for the reported issue, and a constraint test derived from real pull-request review comments. Each of 303 instances, spanning 75 Python repositories, also ships a non-compliant patch that passes F and fails C, plus a gold patch that passes both. That matrix is the product. Functional success is no longer allowed to stand in for maintainer acceptance.

Under Mini-SWE-Agent, four backends produced 644 functionally successful repairs. 221 of those, 34.3%, failed the constraint suite. GPT-5.5 reached 74.9% functional success and only 52.8% joint success. Providing the constraint text raised joint success (GPT-5.5 +11.5 points) and constraint-following among functional repairs (CFR +10.2 to +25.6 points), while functional success itself did not improve. Scope generalization, lifecycle cleanup, encoding, and schema/typing remain the hard categories.

Why it matters: SWE-bench-style gates still answer "did the issue test go green." Production merge answers "would a reviewer accept this." Hidden failures are the gap between those questions.

Stack fit: this belongs in trajectory-aware evaluation and the coding-agent control plane. Pair it with yesterday's EarlyEval. Early stop can save eval budget; SWE-Gate decides whether a green functional trajectory was even the right acceptance object.

Implementable now:

- keep separate F and C oracles, plus a non-compliant reference that proves they are not the same test
- report FSR, CFR, JSR, and hidden-failure rate instead of a single resolve rate
- feed review constraints as first-class task input, then still hide the constraint tests
- start with the released 303-instance package rather than synthesizing a private dual-oracle set

Implementability score: 0.74

The public repository is populated: 303 instances, 99 Docker contexts, encoded model predictions, and a documented 48-instance gap in optional `validation_matrix.json` files. Running it needs Docker, Git, Node, and model credentials. Do not clone or execute it from this cron.

Core source: https://arxiv.org/abs/2609.04167v1

Artifact: https://github.com/DeepSoftwareAnalytics/SWE-Gate

## The serving interface can censor the trajectory before evaluation sees it

Interface-Induced Trajectory Censoring shows that a tool-call rate read off the serving stack can be zero while the model is emitting well-formed calls. On BFCL v4, holding weights, cases, executor, scorer, decoding, and seeds fixed, changing only the serving adapter moves the same model from 0.00 to 0.96 / 0.19 on simple_python / multi_turn_base. A 2x2 over chat template and parser puts both main effects at zero. The whole effect sits in their interaction. On tau-bench's 115 retail tasks, the same swap moves server-parsed calls from 0 to 636 and tasks that reach any tool execution from 0 to 103.

The author's own Qwen2.5-Coder probe, 1.5B to 32B, is worse than a noisy parser. The hermes parser reports 0/100 parsed calls at every scale, while well-formed emitted calls rise to 80/100 at 32B. HTTP 200, `tool_calls: []`, a single-turn trajectory. Four families fail at different layers after official vLLM function-calling setup: DeepSeek-Coder never injects tools in the template, Qwen emits markdown JSON instead of `<tool_call>` (adapter 0 to 84), Llama-3.1-8B calls the task function as a tool until `strict: true` (23 to 0), Mistral repeats `[TOOL_CALLS]` into HTTP 400.

The RL contamination is the strategic half. In the author's GRPO/RLOO runs, pass@1 rose 2.6 to 2.8 points, but 91 to 94% of newly passing items passed on turn 1, and items rescued on turn 2 or later stayed flat at 6 to 9 of 540. A later 10-step GRPO run under function calling executed zero tool calls while `critic/rewards/mean` climbed from 0.233 to 0.281. Opening the channel is also not sufficient: a 75-step ReAct run with 23,676 tool calls still left multi-turn rescues at 6 to 8 of 540.

Why it matters: eval dashboards and RL critics will both look healthy while the branch being measured does not exist. Yesterday's EarlyEval assumes the trajectory is the agent's. This paper says the interface may have deleted the tool-using part first.

Stack fit: agent serving runtime first, RL training governance second. Treat template, parser, tool schema, and token constraints as part of the measurement instrument, not as invisible plumbing.

Implementable now:

- log raw model bytes, parser output, and executor admissions as three separate counters
- run a 2x2 over template and parser before publishing a tool-call score
- fail closed when HTTP 200 returns empty `tool_calls` but the completion contains a well-formed call
- keep ERRATA.md in the loop; the repo documents seven arms with wrong provenance and five inadmissible for pass-rate comparison

Implementability score: 0.80

The public repository is populated with probes, analysis scripts, RESULTS.md, and pre-registrations. Read `runs/final/ERRATA.md` before citing any training number. No clone, install, or execute from this cron.

Core source: https://arxiv.org/abs/2609.03966v1

Artifact: https://github.com/nebula-1999/Interface-Induced-Trajectory-Censoring

## Watchlist

- ConflictGUI / ConflictGuard: vanilla GUI agents stay above 70% on feasible tasks and below 10% on conflict tasks. The intervention is inference-time steering plus a feasibility prompt, not a runtime object. Repo and dataset exist: https://github.com/serein356/ConflictGuard, https://huggingface.co/datasets/serein356/ConflictGUI, paper https://arxiv.org/abs/2609.03438v1
- Terminal-Universe and Environment Evolution: trajectory-to-environment synthesis for terminal-agent post-training. Useful later, not this week's control-plane delta.
- Hugging Face Funes, dated 2026-09-03: "Give Your Coding Agents a Memory You Own." Operator color until the memory object is specified as typed state with provenance.

## Scope and evidence

Friday 2026-09-04 arXiv listings were live for cs.AI (165), cs.CL (115), cs.LG (168), cs.SE (21), cs.CR (39), and cs.MA (15). Selected papers were submitted 2026-09-03 UTC and first listed Friday. Immutable v1 PDFs were converted with `pdftotext -layout`. SWE-Gate, IITC, and ConflictGuard repositories were inspected read-only via GitHub metadata, tree, and README. ConflictGUI was verified through the Hugging Face dataset API. No HookPry or PlanFence official repository resolved. Hugging Face blog RSS, GitHub Blog RSS, Hermes releases, Simon Willison, DeepMind, and Google News were scanned as demand or vendor signal only. Duplicate-checked against 2026-09-01 through 2026-09-03 repo notes.

No external source code was cloned, installed, built, imported, or executed.
