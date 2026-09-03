# AgenticAI Daily Analysis - 2026-09-03

Thursday's listing batch is large. The useful implementation signal is not another skill installer. It is three control questions: when to stop an eval run, how a harness should change from evidence, and whether a skill's declared task is the same object as its induced policy.

## Halt evaluation once the trajectory already predicts the outcome

EarlyEval treats agent evaluation as a within-task cost problem rather than a shorter-benchmark problem. Distilling the suite still leaves every retained task fully executed. The paper's claim is that final success or failure is often visible from intermediate behavior, so a cheap predictor can halt the run.

The implementation is deliberately small: two LightGBM classifiers over behavioral, textual, and reference-solution features, with a calibrated confidence threshold. Across SWE-bench Verified, TerminalBench, and Toolathlon, EarlyEval reports 13% to 26% fewer agent steps and up to 44.1% fewer input tokens and 29.4% fewer output tokens at 89% to 97% prediction accuracy. Per-agent resolve rates move by about 1 to 2 percentage points. On SWE-bench Verified at 95% prediction accuracy, it can halt roughly 35% of runs, cut about 26% of steps, and shift resolve rate by 1.1 points.

Why it matters: Hermes and client coding loops already pay for repeated full-task eval. The first product slice is not a new leaderboard. It is an early-stop policy that preserves ranking while refusing to spend the tail of doomed or already-won trajectories.

How it fits: this belongs in trajectory-aware evaluation. Terminal verifiers stay the hard gate. Early stopping is a budget overlay with an explicit false-stop cost.

Implementable now:

- log prefix features that do not require the final patch: step count, repeated tool errors, test-fail signatures, file-touch entropy
- train separate success and failure predictors; halt only when either crosses a calibrated threshold
- keep leave-one-agent-out splits so the predictor never judges the harness it trained on
- report delta Pass@1, delta rank, and tokens saved beside the headline score
- do not ship early stop into production task execution; it is an eval-cost control

Implementability score: 0.70

The public repository is code-only and populated. It excludes trained models, parquet trajectories, and generated tables, so reproduction still needs the paper artifacts.

Core source: [EarlyEval](https://arxiv.org/abs/2609.02783v1)

Supporting artifact: [inphotoo/earlyeval](https://github.com/inphotoo/earlyeval)

## Evolve the harness from trajectories, then train the policy to use it

SafeEvolve argues that agent safety is jointly owned by the base policy and the runtime harness. Updating only the prompt or only the weights leaves a gap: the harness is ignored, or the policy never learns to consult it. The loop is: on-policy trajectories, bounded component-level harness edits (global safety prompt plus hierarchical SkillBank), harness-use SFT, then harness-augmented GRPO.

On Qwen3.5-4B, the paper reports AgentDojo ASR falling from 2.37% to 0.79% (a 3x reduction) while clean utility rises from 59.79% to 61.86%. On AgentHarm, harm score falls from 56.45 to 12.27 and refusal rises from 28.98% to 83.83%. Ablations matter more than the headline: model-only RL can worsen utility under attack, and evolved skills beat evolved prompts for multi-step injection.

Why it matters: yesterday's Defense-as-Skill result said the guard should be a first-class skill. SafeEvolve says that skill, and the rest of the harness, should change only from trajectory evidence with reversible artifacts, then the policy should be trained to use the new artifacts.

How it fits: harness architecture plus skills-as-control. Do not take the full SFT-RL loop as the Hermes default. Take the admission rule: harness edits are bounded, auditable, and rejected unless safety and utility gates both pass.

Implementable now:

- store harness components as named, diffable objects (prompt, skill bank, runtime constraints)
- accept an edit only after paired safety and utility scores on held-out fixtures
- keep evolution logs as JSONL, the same shape as the public repo's `assets/evolution_logs`
- do not promote live-attack rollouts into unsupervised harness rewrites
- if policy training is in scope later, bootstrap harness-use before reward optimization

Implementability score: 0.50

The official repository is public, MIT-licensed, and populated with configs, core code, and compact evolution logs. It is still a research training loop, not a drop-in Hermes feature.

Core source: [SafeEvolve](https://arxiv.org/abs/2609.02786v1)

Supporting artifact: [MaoPopovich/SafeEvolve](https://github.com/MaoPopovich/SafeEvolve)

## Audit skills as frozen behavioral policies, not just packages

SkillShift shows a third-party skill can keep the declared task and a valid output interface while changing the induced selection policy. In shopping recommendation, attacker-favored selection (PSR) rises from 37.33% to 81.33% at 100% valid-output rate. In Python dependency selection, PSR rises from near-zero to 63.33% at 100% VR. Each domain uses 50 in-distribution queries (30 development, 20 held-out) and three runs per query. Frozen skills transfer across backends (Claude Haiku 4.5, DeepSeek v4-Flash, GLM-4.7, Gemini 3-Flash, Qwen3.5-Flash) without further optimization.

The scanner result is the operational punch. Direct-Skill Injection, which overrides the original policy, is caught by 4 of 6 tools. SkillShift's paired Attack skills are not distinguished from Clean skills by skill-scanner-full, Aguara, Snyk Agent Scan, STARS, SkillSpector, or ProtectAI DeBERTa. Static skill review is necessary and insufficient.

Why it matters: Hermes already loads skills as delayed-authority objects. SkillShift says the attack is not only delayed harm after a later user task. It is a policy that looks helpful on the original task while steering brand, library, or vendor choice.

How it fits: skills-as-control and defense-as-skill. Add outcome-level skill fixtures: same candidates, same user request, measure selection shift. Do not treat a green SkillSpector scan as policy integrity.

Implementable now:

- define Skill Policy Integrity as declared functionality plus user-authorized objective
- freeze candidate sets and score PSR / valid-output rate on clean versus attack skills
- keep a direct-injection positive control so scanners can still prove they work
- fail closed on unexplained selection lift even when the output schema is valid
- do not clone or run SkillShift generators; the paper artifact did not resolve to an official repo

Implementability score: 0.72 for the audit fixtures; the generator itself is not a product path.

Core source: [A Finger on the Scale](https://arxiv.org/abs/2609.02564v1)

## Watchlist

- [Coverage, Not Targeting](https://arxiv.org/abs/2609.02417v1): terminal verifiers expose too little of the causal chain for per-turn credit targeting. Strong eval/RL design note, not today's product cut.
- [Repo-To-Skill / DisCo](https://arxiv.org/abs/2609.02749v1): 5,000+ distilled ML skills. Useful later, too large and too skill-supply-chain-risky to index above SkillShift.
- [ACLE-MCP](https://arxiv.org/abs/2609.02690v1) is filed under Strategy. It is the remote-tool complement to today's skill-policy finding.

## Scope and evidence

arXiv recent pages for cs.AI, cs.CL, cs.LG, cs.SE, cs.CR, and cs.MA show a Thursday 2026-09-03 listing batch. Selected papers were submitted 2026-09-02 UTC and first listed Thursday. Immutable v1 PDFs were converted with `pdftotext -layout`. GitHub metadata and READMEs for EarlyEval and SafeEvolve were inspected read-only. No SkillShift or ACLE-MCP implementation repository resolved. No external source code was cloned, installed, built, imported, or executed.

NotebookLM was disabled.
