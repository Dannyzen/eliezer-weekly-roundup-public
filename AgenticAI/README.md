# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: Friday, 2026-07-31

### AgentRadio gives concurrent workers passive awareness

Summary: AgentRadio adds a background mention channel to coding-agent harnesses. On 124 SWE-Atlas QnA tasks, four agents reached 62.1 percent versus 32.3 percent for one agent and 37.9 percent for compute-matched best-of-six sampling.

Analysis: [daily reasoning analysis](2026-07-31/reasoning.md#agentradio-adds-passive-awareness-to-concurrent-agent-work)
Core sources: [paper](https://arxiv.org/abs/2607.28430v1), [Apache-2.0 repository](https://github.com/Coral-Protocol/AgentRadio)
Implementable now:
- drain scoped worker inboxes between tool steps;
- bind messages to thread, sender, recipient, task revision, and evidence;
- compare passive awareness with blocking negotiation and matched sampling.
Tools, repositories, and methodologies:
- AgentRadio, append-only inboxes, typed thread IDs, background watchers, SWE-Atlas QnA, topology ablations
Implementability score: 0.84

### Change2Task turns repository history into modern executable tasks

Summary: Change2Task reconstructs merged changes on healthy descendant revisions and validates healthy, task, and restored states. It finalized 900 paired tasks from 1,130 eligible changes and beat a pull-request mirror baseline by 29.2 percent on matched candidates.

Analysis: [daily reasoning analysis](2026-07-31/reasoning.md#change2task-reconstructs-executable-tasks-on-healthy-modern-code)
Core source: [paper](https://arxiv.org/abs/2607.28591v1)
Implementable now:
- pilot patch reversal before model-assisted reconstruction;
- freeze source PR, modern base, patches, checks, and adapter versions;
- require pass-fail-pass targets and green protected regressions.
Tools, repositories, and methodologies:
- Git history, pull-request metadata, patch reversal, code mapping, containerized tests, lifecycle verification
Implementability score: 0.68

### OSReward tests whether trajectory judges deserve trust

Summary: OSReward evaluates 27 VLM judges on 1,019 human-gold cross-platform trajectories. The hard-set mean fell to 52 percent and false success dominated errors. The methodology is actionable, but the advertised artifacts were missing or empty at scan time.

Analysis: [daily reasoning analysis](2026-07-31/reasoning.md#osreward-audits-the-judge-before-trusting-trajectory-reward)
Core sources: [paper](https://arxiv.org/abs/2607.28609v1), [project page](https://os-copilot.github.io/OSReward-Home/)
Implementable now:
- build a small human-gold trajectory set;
- report recall on true failures separately;
- ablate screenshots, actions, reasoning, and final claims.
Tools, repositories, and methodologies:
- human-gold trajectories, hard-case subsets, false-success recall, input ablations, deterministic state verifiers
Implementability score: 0.60

## Current implication

Agent scale needs evidence-bearing harness surfaces. Coordination, task construction, and trajectory reward should each have explicit identities, controls, and ablations before they influence production behavior.
