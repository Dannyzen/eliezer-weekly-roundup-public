# Defense as Skill

Last updated: 2026-09-02

Primary layer: Strategy / runtime governance / skill admission control

Implementability score: 0.58

Core sources:
- Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents: https://arxiv.org/abs/2609.01487v1
- Immutable v1 PDF: https://arxiv.org/pdf/2609.01487v1

Related durable topics:
- [Skill Admission Control](../skill-admission-control/skill-admission-control.md)
- [Skills as Control](../../AgenticAI/skills-as-control/skills-as-control.md)
- [Untrusted Data Boundaries](../untrusted-data-boundaries/untrusted-data-boundaries.md)
- [Runtime Governance](../runtime-governance/runtime-governance.md)
- [Agent Execution Control Plane](../agent-execution-control-plane/agent-execution-control-plane.md)

## Overview

Install-time skill vetting answers the wrong question. A malicious or compromised skill does not need to look dangerous when it is loaded. It can wait until a later user task, workspace state, and tool set make an unsafe action look useful: leak a secret, corrupt code, bypass an approval, or stage data for exfiltration.

Defense-as-Skill is the missing control after admission. The runtime guard is itself an installable, inspectable, editable skill. It sits beside untrusted task skills, checks proposed actions against the user's current task boundary, and returns allow, replan, or confirmation. The paper instantiates that pattern as SkillSonar and evaluates it on Claude Code and OpenClaw.

This belongs in Strategy, not AgenticAI. The load-bearing decision is whether a loaded skill may authorize an effect after the install gate has already passed. Packaging a guard as Markdown is an implementation convenience. Authority still has to live outside the model.

## Why this finding won the week

The rest of the week was strong and narrower.

- CIPR already showed that user invocation activates poisoned repository paths. That finding is in the repo as of 2026-09-01. It does not cover skills that wait for a later task.
- LoopArena separates controller from worker. That is loop engineering, not skill authority.
- Salesforce TraceLab's live trace model is a real serving and observability advance, but it extends June's TraceLab work and is labeled descriptive because the benchmark was co-developed with the system.
- HarnessDev and Harness-of-Harness ask whether models can grow their own execution infrastructure. Capability growth without a task-conditioned guard makes the skill problem worse.
- CordisBench tests lifecycle reasoning about dynamic harness components. That is evaluation, not a runtime gate.

Defense-as-Skill changes the trust model underneath all of them. Once skills are persistent runtime context, pre-install scanners, static package digests, and prompt-level safety paragraphs are not enough. Harm is task-conditioned. The guard has to see the current user goal, the proposed action, and the loaded skill together.

Three facts make it the week's durable primitive:

1. The failure is delayed. A skill can pass admission and still become an attack only after a later task makes the unsafe action look in-scope.
2. The first useful control is structural: a dedicated guard with explicit safety responsibility, not a better system prompt.
3. The paper measures the trade-off that actually matters in production: attack success versus benign-task utility, not refusal rate alone.

## Core innovation

SkillSonar does four things that a scanner does not:

1. Install the guard as an ordinary skill artifact, so operators can read, edit, version, and transfer it.
2. Assign it a distinct safety responsibility. The host is instructed to consult the guard before sensitive actions. The paper finds that safety skills do not get invoked reliably if they are merely present the way capability skills are.
3. Route each checked action to allow, replan, or confirmation against the user's task boundary, without patching Claude Code or OpenClaw internals.
4. Evolve the on-disk guard with a small Monte-Carlo Tree Search over rollout feedback: attack success, task utility, confirmation burden, and token cost.

SCOPE-R is the evaluation substrate: 6 risk families, 21 sub-categories, 206 attack-confirmed malicious instances, and 43 benign tasks. Four families are used for training and in-distribution test. Capability Control and Privacy and Data Flow are held out as out-of-distribution families. Eleven benign tasks are used during evolution; 32 are held out for final utility measurement.

The authors follow a defensive release strategy. They say they will release evaluation metadata, benign sources, labels, success indicators, and scripts, while redacting or controlling high-risk malicious payloads. As of this writing, no public SkillSonar or SCOPE-R repository resolved. Treat the paper as the verified source. Do not treat the cited [pinchbench/skill](https://github.com/pinchbench/skill) repo as their guard: that repository is a PinchBench OpenClaw coding-agent benchmark, not SkillSonar.

## Evidence

On the primary Claude Code setting with GLM-5, repeated over N = 10 runs:

| Defense | ID ASR | OOD ASR | ID TaskUtil | OOD TaskUtil |
|---|---|---|---|---|
| No-guard | 0.482 ± 0.039 | 0.606 ± 0.043 | 0.811 ± 0.033 | 0.839 ± 0.027 |
| System prompt | 0.414 ± 0.042 | 0.489 ± 0.048 | 0.783 ± 0.045 | 0.807 ± 0.058 |
| AcceptEdits | 0.122 ± 0.039 | 0.073 ± 0.025 | 0.650 ± 0.062 | 0.715 ± 0.040 |
| AcceptEdits + allowlist | 0.460 ± 0.043 | 0.610 ± 0.034 | 0.811 ± 0.025 | 0.832 ± 0.023 |
| SkillSonar | 0.104 ± 0.036 | 0.115 ± 0.037 | 0.779 ± 0.077 | 0.715 ± 0.099 |

The transferable result is not "lowest ASR at any cost." AcceptEdits, Claude Code's interactive permission preset, can match or beat SkillSonar on some OOD ASR cells, but it costs utility. SkillSonar keeps more of the original task: 0.779 versus 0.650 on GLM-5 ID. Adding an allowlist to AcceptEdits collapses protection back toward no-guard. That is the production failure mode: operators suppress confirmations for "common" commands and re-open the hole.

Cross-model point estimates on Claude Code:

- Claude Haiku 4.5: ID ASR 0.481 to 0.096, OOD ASR 0.707 to 0.254.
- GPT-5.4: ID ASR 0.588 to 0.019, OOD ASR 0.559 to 0.034.

OpenClaw, the additional runtime, still moves in the same direction with weaker absolute numbers. On GLM-5, SkillSonar cuts ID ASR from 0.596 to 0.245 and OOD ASR from 0.621 to 0.232, while holding or improving ID utility.

Benign-task utility on Claude Code stays close to no-guard for GLM-5 (0.817 versus 0.815) and Haiku (0.836 versus 0.827). GPT-5.4 drops from 0.793 to 0.724, so the utility cost is model-dependent.

Adaptive attackers after three refinement iterations still lose overall ASR from 45.1 percent to 22.9 percent. Specification Integrity is the weakest family (53.3 percent to 43.3 percent). Privacy and Data Flow is the strongest (43.3 percent to 8.3 percent). A Markdown guard is not a sealed boundary.

Ablations in the paper's conclusion are load-bearing: explicit safety responsibility assignment and the skill-native representation both matter. Flattening the same policy into a system prompt is a weaker control.

## Why it matters

### Admission is not runtime

TRUSS, MaliciousSkillBench, and SkillSafetyBench improved the install gate. That work stays necessary. It does not answer what happens after a package is already in the runtime context and a later task makes a delayed payload look helpful.

### Presence is not invocation

Capability skills fire because they match the user's request. A safety skill does not. If the host is not explicitly required to consult the guard before sensitive actions, the guard is documentation.

### Permission prompts are not a policy

AcceptEdits shows the trap. Interactive confirmation lowers ASR and also lowers utility. Operators then allowlist "safe" commands and the ASR returns. Task-conditioned policy has to survive the moment someone is tired of clicking Allow.

### Soft guards complement hard gates

The authors are explicit: SkillSonar is instruction-following. A more advanced malicious skill can ignore, override, or bypass it. The guard should sit beside permission systems, sandboxes, logging, and human oversight, not replace them.

## Fit in the agentic stack

- Package layer: skills remain versioned procedure plus optional scripts. Admission still owns the digest, static scan, and shadow run.
- Runtime-context layer: loaded skills are persistent untrusted context, not trusted procedure, until a later gate says otherwise.
- Guard layer: a dedicated policy skill with explicit consult-before-action responsibility.
- Decision layer: allow, replan, or confirmation bound to the current user task, not to a static command denylist.
- Effect layer: permissions, sandboxes, and brokers still own the actual write, network, and secret surfaces.
- Evidence layer: record the proposed action, task boundary, guard decision, confirmation outcome, and effect receipt.

The product boundary should shift from `skill scanner` to `task-conditioned skill guard`. Scanning asks "is this package malicious." The guard asks "may this loaded skill do this action for this user task."

## Practical tools, repos, and methodologies worth trying now

Do not wait for SCOPE-R payloads or an official SkillSonar repo.

1. Add a first-class guard skill in Hermes, separate from capability skills. Give it an explicit consult-before-action instruction. Do not rely on discovery.
2. Represent each sensitive action as `proposed_effect`, `target_identity`, `skill_id`, `user_task`, and `decision` in `{allow, replan, confirm}`.
3. Keep the user task boundary as a typed object, not a paragraph in the prompt. The guard compares proposed effects against that object.
4. Preserve permission systems and sandboxes as hard gates. If the Markdown guard says allow and the broker says deny, deny wins.
5. Measure four numbers on every guard change: attack success, benign utility, confirmation count, and token cost. A guard that refuses everything is not a win.
6. Add fixtures for delayed harm: the skill is clean at install, then a later task makes exfiltration, approval bypass, or secret read look in-scope.
7. Add an allowlist-regression fixture. Confirm that suppressing confirmations for "common" commands restores attack success.
8. Use CIPR as the invocation-side complement: https://github.com/StarConnor/CIPR and https://arxiv.org/abs/2608.30686v1. User phrasing and skill loading jointly set risk.
9. Keep TRUSS-style admission in front of the guard: https://arxiv.org/abs/2608.17588v1. The guard is not a substitute for digest, shadow execution, and preservation constraints.
10. If reproducing the paper later, treat withheld malicious payloads as inert evaluation input only. Do not clone, install, or execute third-party skill malware.

## Implementation complexity

The first slice is ordinary engineering: one extra skill, an explicit invocation rule, a small action schema, and a handful of delayed-harm fixtures. That is why the score is above 0.5.

The rest is architecture-heavy:

- evolving the guard from live attack rollouts;
- a trustworthy judge for ASR, utility, confirmation, and tokens;
- transferring a Markdown policy across Hermes, Claude Code, Codex, and OpenClaw without pretending instruction-following is enforcement;
- holding out entire risk families so the policy learns least privilege rather than family cues.

MCTS with a cap of 8 full evaluations is a research procedure, not a product loop. Product evolution should be reviewable diffs against named fixtures, not an unsupervised search over attack transcripts.

## What remains conceptual or blocked

- No public SkillSonar or SCOPE-R repository resolved in this scan. Artifact status: claimed with a defensive-release note, not URL-verified as a populated implementation.
- The guard is still a Markdown policy. Bypass by ignoring the guard is in-scope.
- Optimization depends on a runtime judge. Judge error can move the reported operating point.
- Adaptive attackers cut the advantage roughly in half. Specification Integrity remains weak.
- OpenClaw numbers are weaker than Claude Code. The pattern transfers; the operating point does not.
- The paper's footnote to `pinchbench/skill` is not their defense artifact.

## Strategic implications for Danny's product thinking

Hermes already treats skills as packages. FriendVM, client bots, and collaborator repos will keep accumulating skills because they are the cheapest way to add durable procedure. That is the same mechanism this paper attacks.

The useful product move is not a better scanner banner. It is a runtime that can answer, for every sensitive tool call:

- which skill proposed it;
- which user task it claims to serve;
- whether the guard was consulted;
- whether the decision was allow, replan, or confirm;
- whether a hard broker still denied the effect.

For client work, especially SJJCC, FTS, and any bot that can load third-party skills, delayed harm is the realistic case. A skill that looks helpful in `#teese` or a coding workspace can wait for a later request that makes data movement look in-scope. Install-time review will not see that.

This also bounds self-improvement. If a runtime may rewrite its own skills, the guard skill needs a tighter change path than capability skills: review, digest, fixture replay, and no unsupervised MCTS against live user tasks.

The weakest honest objection: a Markdown guard can be ignored, so why bother? Because the measurements show a dedicated, explicitly invoked policy skill beats a system-prompt paragraph and beats naive allowlists, while remaining inspectable. The answer is to ship the cheap guard and keep the hard broker. Not to wait for a formally sealed skill kernel.

## Implementation checklist

1. Create a Hermes guard skill with explicit consult-before-action text.
2. Bound it to a small set of sensitive effects: secret read, network send, approval bypass, destructive write, install/execute.
3. Log proposed effect, skill id, task id, and decision.
4. Add delayed-harm fixtures that pass install review and fail only after a later user task.
5. Add an allowlist-regression fixture.
6. Keep sandbox and permission denial as the last word.
7. Do not promote guard-skill edits from live attack rollouts without named fixtures and a human review.

## Source notes

Verified from the immutable v1 abstract, PDF text via `pdftotext -layout`, and read-only GitHub metadata. No external source code was cloned, installed, built, imported, or executed.

- Paper submitted 2026-09-01T16:19:31Z, first listed in the Wednesday 2026-09-02 cs.CR / cs.AI batch.
- Authors: Xiaofang Yang, Ziqi Miao, Dianbo Sui, Jing Shao, Lijun Li (Shanghai AI Laboratory, Fudan, HIT Weihai).
- Claimed but unresolved: SkillSonar source and SCOPE-R payload release.
- Not an implementation of this paper: https://github.com/pinchbench/skill
- Complementary week sources that lost: https://arxiv.org/abs/2609.01466v1 (live trace), https://arxiv.org/abs/2608.30686v1 (CIPR), https://arxiv.org/abs/2608.28281v1 (LoopArena), https://arxiv.org/abs/2609.01437v1 (HarnessDev), https://arxiv.org/abs/2609.01481v1 (Harness-of-Harness), https://arxiv.org/abs/2609.01600v1 (CordisBench).

## September 3, 2026 update: delayed authority now includes covert policy

Defense-as-Skill covered the later-task case: a loaded skill waits until a new request makes leakage look useful. SkillShift covers the same-task case: the skill keeps the original request, keeps a valid answer, and still steers brand, library, or vendor choice. Install review, static scanning, and consult-before-action remain necessary. They are not Skill Policy Integrity.

Add paired clean/attack fixtures over frozen candidate sets. Measure PSR and valid-output rate. Keep Direct-Skill Injection as a scanner positive control. Treat unexplained selection lift as a release blocker.

Implementability score: 0.72

Source: [A Finger on the Scale](https://arxiv.org/abs/2609.02564v1)
