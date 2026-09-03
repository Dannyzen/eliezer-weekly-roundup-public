# Strategy Daily Sovereignty - 2026-09-02

## Scope note

This is Deep Dive Wednesday. The winning paper was submitted 2026-09-01T16:19:31Z and first listed in the Wednesday 2026-09-02 cs.CR / cs.AI batch. The immutable v1 abstract and PDF were inspected with `pdftotext -layout`. No public SkillSonar or SCOPE-R repository resolved. No external source code was cloned, installed, built, imported, or executed. NotebookLM remained disabled.

## Treat loaded skills as delayed-authority objects

A skill can pass install review and still become an attack later. The payload waits until a user task, workspace state, and tool set make leaking a secret, bypassing approval, or staging data look useful. Pre-install scanners, package digests, and safety paragraphs in the system prompt do not see that moment.

Defense-as-Skill makes the runtime guard itself an installable skill. SkillSonar sits beside untrusted task skills, compares proposed actions with the current user task boundary, and returns allow, replan, or confirmation. Explicit safety responsibility assignment matters: a safety skill does not get invoked the way a capability skill does.

On Claude Code with GLM-5, N = 10, SkillSonar cuts in-distribution attack success from 0.482 ± 0.039 to 0.104 ± 0.036 and out-of-distribution attack success from 0.606 ± 0.043 to 0.115 ± 0.037, while keeping more task utility than Claude Code AcceptEdits (0.779 versus 0.650 on the ID split). Adding an allowlist to AcceptEdits collapses protection back toward no-guard. That is the operator failure mode this control has to survive.

Why it matters: Hermes, FriendVM, and client bots already load skills as persistent runtime context. Admission remains necessary. It is no longer sufficient. The runtime has to decide whether a loaded skill may perform this action for this user task, then let a hard broker still deny the effect.

Practical tools and methodologies worth exploring:

- add a dedicated guard skill with an explicit consult-before-action instruction;
- bind each sensitive action to proposed effect, target identity, skill id, user task, and `{allow, replan, confirm}`;
- keep sandboxes and permission brokers as the last word;
- add delayed-harm fixtures that pass install review;
- add an allowlist-regression fixture that restores attack success when confirmations are suppressed;
- measure attack success, benign utility, confirmation count, and token cost on every guard change.

Weakest point: SkillSonar is still Markdown. A more advanced skill can ignore it, and no public implementation artifact resolved. The first Hermes slice does not need that artifact. It needs an explicit guard skill, a small action schema, delayed-harm fixtures, and an unchanged hard broker.

Implementability score: 0.58

Durable deep dive:
- [Defense as Skill](../defense-as-skill/defense-as-skill.md)

Core source:
- [Defense-as-Skill](https://arxiv.org/abs/2609.01487v1)

Related week sources that lost:
- [Parsing the Stream](https://arxiv.org/abs/2609.01466v1)
- [CIPR](https://arxiv.org/abs/2608.30686v1)
- [LoopArena](https://arxiv.org/abs/2608.28281v1)
