# Strategy Daily Sovereignty: 2026-11-28

## Scope

The strongest fresh control-plane signal is a 27 November Pydantic AI release. The monitor-evaluation paper was submitted on 25 November and first listed on 26 November. The repository and pull request were inspected read-only. The paper is a fresh preprint and the release probe is maintainer-reported evidence, not independent replication.

## 1. Bind workspace context to source authority

[Pydantic AI v2.77.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.77.0) ships an authority-aware boundary for `RepoContext`, `Skills`, and `Memory`. Workspace files below `operator` authority no longer enter model instructions as if the application authored them. Their text arrives as tool output or framed data with a named source. Low-authority skills are listed and loaded through tools, and low-authority memory snapshots are attributed to their `MEMORY.md` source rather than to the agent.

The merged [implementation pull request](https://github.com/pydantic/pydantic-ai/pull/11837) reports a useful directional probe: a planted instruction in a low-authority working-directory file was followed 1 of 6 times by Claude Opus 5.5 and 0 of 6 by Gemini 4 Argon when exposed through file-tool output, versus 6 of 6 when injected as an instruction block. The sample is tiny and maintainer-run, but the architecture is sound: provenance changes the channel before model interpretation.

Why it matters: a repository may contain valuable context and hostile instructions at the same time. Loading every `AGENTS.md`, skill, or memory file into the instruction channel silently promotes writable data into authority.

Strategic fit: untrusted-data boundaries, context-to-execution integrity, skill admission, and memory provenance.

Implementable now:
- attach authority and source identity to every context file
- reserve instruction channels for application and operator authority
- expose lower-authority context through tools or framed data
- attribute memory snapshots to the file or system that produced them
- test planted instructions at each channel boundary

Implementability score: 0.93

Core sources: [Pydantic AI v2.77.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.77.0), [authority-aware workspace PR](https://github.com/pydantic/pydantic-ai/pull/11837)

## 2. Evaluate monitors across attack-policy envelopes

[Attack Policy Selection can Mislead Monitor Evaluators](https://arxiv.org/abs/2611.34934v1) holds the deployment scenario and 30 control tasks fixed while varying how attack transcripts are generated. Against a held-out ex-production GPT-5.4 monitor, false-negative rate ranged from 0.5% to 20.8% across optimization levels of reinforcement learning. Across attack methods at their best observed optimization levels, it ranged from 6.4% for optimized prompting to 23.0% for transcript editing.

Every attack policy was developed against proxy monitors, so the reported failures transferred to the held-out target. The operational lesson is larger than the specific monitor: one weak attack generator can make the same detector look far safer than a stronger generator does.

Why it matters: monitor quality is inseparable from attacker coverage. A single miss rate is incomplete without attack-policy identity, optimization budget, transfer setup, and the envelope across methods.

Strategic fit: evaluation containment, monitor governance, adversarial validation, and release evidence.

Implementable now:
- version attack policies and their optimization budgets
- sweep prompting, learned attacks, and transcript-level editing
- develop attacks against proxy monitors and reserve a held-out target
- report the full false-negative envelope, not one preferred point
- preserve clean-traffic false positives and utility beside attack success

Implementability score: 0.78

Core source: [Attack Policy Selection can Mislead Monitor Evaluators v1](https://arxiv.org/abs/2611.34934v1)

## Strategic conclusion

Context provenance and monitor evaluation share one rule: the channel and generator are part of the evidence. Treat neither a file nor an evaluation transcript as authoritative until its source, optimization path, and release boundary are explicit.
