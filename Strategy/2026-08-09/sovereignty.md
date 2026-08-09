# Strategy Daily Sovereignty, 2026-08-09

No new arXiv listing appears on Sunday. These findings are non-duplicate extensions from the Friday, 2026-08-07 listing batch. The malicious-skill paper was submitted on 2026-08-05 and first listed on Friday; DreamGuard v1 was submitted on 2026-08-06.

## Skill files are executable supply-chain artifacts

Towards a Risk Assessment of Malicious Skill Files in Coding Agents turns skill-file trust into a measured execution risk. Six LLMs across four families transformed 471 real shell commands into 2,826 benign-looking skill files mapped to 11 MITRE ATT&CK tactics. Across 5,629 completed runs, Gemini CLI was exploited in 95.5 to 96.1 percent of runs and Qwen Code in 71.6 to 74.0 percent. Explicit safety recognition appeared in only 1.99 percent of runs.

The important boundary is not prompt injection in the abstract. It is delegated shell authority inherited from a dynamically loaded file. A skill can describe a harmful command as mandatory setup, and a coding agent can treat that prose as permission.

Why it matters: skill text combines instructions, scripts, dependencies, and trigger metadata. It therefore belongs in the same admission path as packages, plugins, and CI actions, with stronger controls when the agent can use shells, credentials, networks, or production APIs.

Strategic fit: skill supply-chain governance, untrusted-data boundaries, execution control, and enterprise coding-agent adoption.

Implement now:
- resolve exact publisher, repository, revision, version, hash, license, and dependency identity before load;
- statically extract shell, network, credential, persistence, and destructive-operation requests;
- require a capability manifest independent of the skill prose;
- detonate untrusted skills in a disposable sandbox with inert credentials and denied production access;
- prohibit auto-approval for untrusted or changed skills;
- bind skill identity, requested capabilities, policy verdict, human approval, loaded content hash, tool calls, and effects in one receipt;
- revoke and quarantine by hash, not only by display name.

Evidence caveat: the experiment uses two coding agents, one benign task, auto-approved execution, and a 120-second window. Its primary exploitability measure includes declared intent to execute, not only completed external effects, although the paper also adds shell-invocation and audit-shim corroboration. Treat the rates as strong evidence of a boundary failure under the tested configuration, not universal rates for every agent deployment.

Artifact status: `awsm-research/AgentJailbreak` is public and populated with the dataset basis, run pipelines, evaluation tools, sandbox template, and paper. It was inspected read-only and not executed. The repository does not declare a license.

Implementability score: 0.84

Core sources:
- https://arxiv.org/abs/2608.05223v1
- https://github.com/awsm-research/AgentJailbreak

## Long-horizon guardrails need compact risk state before action

DreamGuard treats trajectory risk as runtime state rather than re-reading an ever-growing history with an LLM at every step. A frozen Qwen3-4B encoder feeds a GRU-based recurrent state. The gate combines immediate-hazard evidence with prefix-risk evidence before the proposed action executes.

Across SafetyDrift, AgentDojo, Agent Security Bench, and ASSE-Security, the paper reports an average end-to-end latency of 25 milliseconds per call. It intervenes before the first hazardous action in 96.3 percent of unsafe long-horizon trajectories. In the online evaluation, it reports 72.92 percent safety while preserving 90.38 percent task utility.

Why it matters: individually benign actions can form a hazardous sequence. Copying a sensitive file, moving it into a workspace, and creating a public link may each look acceptable in isolation. The runtime needs a compact, versioned risk state that can block the transition before the final effect.

Strategic fit: runtime governance, stateful effect control, trajectory observability, and pre-action authorization.

Implement now:
- normalize model and tool activity into a versioned event schema;
- maintain a bounded risk state outside the acting model process;
- score immediate hazard and accumulated prefix risk separately;
- expose explicit pass, hold, and block outcomes before tool execution;
- bind calibration version, thresholds, state digest, action manifest, verdict, and effect receipt;
- replay known safe and unsafe trajectories after model, tool, policy, or environment changes;
- keep deterministic policy and commit-time checks as the final authority for narrow high-risk effects.

Evidence caveat: DreamGuard was trained and calibrated on SafetyDrift using one H100, then transferred to the other benchmarks with the same thresholds. The approach is implementable but operationally heavier than deterministic policy, and a learned latent state is not independently interpretable enough to become sole authorization authority.

Artifact status: no exact public DreamGuard implementation repository was verified from the primary paper pages. The paper and evaluation methodology are available; reproduction status remains unverified.

Implementability score: 0.52

Core source: https://arxiv.org/abs/2608.05695v1

## Working conclusion

Authority can enter through a skill file and accumulate through a sequence of otherwise ordinary actions. Treat skills as admitted executable artifacts, then maintain risk state outside the acting model and require a pre-action gate before privileged effects.
