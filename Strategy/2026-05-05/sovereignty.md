# Strategy Daily Analysis: 2026-05-05

Today's strategic signal: the risk surface is moving into persistent state and domain-specific procedural packages. Agents are no longer just live prompt sessions. They are networks of memories, workspaces, scheduled runs, skills, connectors, and governance labels that survive into future execution.

## Persistent agent state is now a worm propagation surface

Core source:
- [Autonomous LLM Agent Worms: Cross-Platform Propagation, Automated Discovery and Temporal Re-Entry Defense](https://arxiv.org/abs/2605.02812v1)

### What it says

The paper argues that autonomous LLM agents create a new propagation surface because they run as long-lived processes with persistent workspaces, memory files, scheduled task state, and messaging integrations. Attacker-influenced content can be written into persistent state, later re-enter the LLM context through scheduled autoloading or workspace reads, and then trigger high-risk actions or cross-agent transmission.

The authors introduce SSCGV, a source-code graph analyzer that traces data flow from file I/O to LLM context injection points, and SRPO, a payload optimizer intended to remain effective across summarization and paraphrasing. They report zero-click autonomous propagation across three production agent frameworks, including multi-hop cross-platform transmission and inter-agent privilege escalation.

The defensive contribution is RTW-A: block write-before-exposed-read re-entry, seal configuration, use typed memory promotion, and attenuate capabilities after external reads. The important empirical warning is blunt: read operations are a primary integrity threat in LLM-mediated systems because reading untrusted state can change future behavior.

### Why it matters

Most agent safety thinking still treats tool writes as dangerous and reads as mostly safe. Persistent agents break that distinction. A read from a workspace, memory file, inbox, ticket, chat, or previous summary can become an instruction surface when it is injected into a future prompt.

That means memory admission, file autoloading, scheduled task state, and summarization are security boundaries. If a platform cannot distinguish trusted persistent state from untrusted imported state, it cannot reliably contain worms.

### Fit in the strategy stack

This belongs in runtime governance, memory governance, and agent-network containment:
- memory layer: untrusted summaries must not be promoted into trusted memory automatically;
- workspace layer: files created after external reads need taint labels and re-entry controls;
- scheduler layer: cron/autoloaded state must not blindly rehydrate attacker-influenced content;
- gateway layer: high-risk capabilities should attenuate after external reads;
- network layer: repeated payloads and fan-out need quarantine and revocation paths.

### Implementable now

- Treat external reads as tainted events, not neutral context acquisition.
- Add labels for trusted config, trusted memory, untrusted workspace content, and promoted memory.
- Block untrusted write-before-read re-entry into system/developer prompts and privileged memory.
- Seal static configuration and avoid allowing ordinary agent writes to modify it.
- Require typed memory promotion before summaries can influence future high-privilege runs.
- Attenuate shell, credential, messaging, email, payment, deployment, and config-edit capabilities after reading untrusted content.
- Add canary payloads to staging workspaces and verify they do not survive summarization into future prompts.
- Preserve trace evidence for every read-to-write-to-reentry chain.

### Implementability score

0.66

The ingredients are available: taint labels, sealed config paths, memory promotion gates, policy engines, trace scanning, and capability attenuation. The hard part is wiring them through agent frameworks that currently treat reads as ordinary context and state files as benign convenience.

## Domain skills need domain-risk labels, not generic autonomy labels

Core source:
- [An Empirical Study of Agent Skills for Healthcare: Practice, Gaps, and Governance](https://arxiv.org/abs/2605.02709v1)

### What it says

The paper studies 557 healthcare-related skills filtered from 58,159 public skills on ClawHub and annotates them across ten dimensions covering function, deployment context, autonomy, and safety. Its strongest finding is that public healthcare skills emphasize patient-facing workflow automation and monitoring more than the diagnostic and treatment tasks foregrounded in healthcare-agent research. It also finds uneven lifecycle coverage and warns that general technical risk does not reliably capture clinical risk.

The strategic lesson is bigger than healthcare. Skills are becoming procedural packages that encode local workflows. A skill's risk cannot be inferred only from whether it calls a dangerous tool or claims low autonomy. Domain context changes the risk: a benign reminder, intake, triage, or monitoring step can become high impact when it affects regulated clinical workflow.

### Why it matters

Yesterday's skill-verification finding said a skill is untrusted code until verified. Today's healthcare-skills finding adds: verification has to include the domain's risk semantics. A generic skill manifest that says "uses email" or "requires approval" is not enough. The manifest needs to know what kind of patient data, workflow phase, handoff, record update, escalation, or regulated decision the skill touches.

For enterprise and regulated domains, skills become the place where domain governance meets agent procedure. If the skill format cannot express domain risk, the agent platform will either overblock useful workflow automation or underblock dangerous workflow automation.

### Fit in the strategy stack

This belongs in skill governance, domain operating models, and regulated-agent deployment:
- skill layer: manifests need domain-risk fields, not only tool and autonomy fields;
- governance layer: approval policy should depend on domain action class;
- audit layer: traces should preserve which skill section justified each domain action;
- evaluation layer: benchmark tasks should cover workflow and monitoring failures, not only diagnosis-like hero tasks;
- operating model layer: local procedures and organizational constraints are first-class inputs.

### Implementable now

- Extend skill manifests with domain, workflow phase, affected record type, data sensitivity, action class, escalation path, and required reviewer role.
- Separate technical risk from domain risk in review checklists.
- Build sector-specific adversarial fixtures: unsafe triage, wrong handoff, stale patient instruction, unapproved record mutation, missing escalation, and privacy leakage.
- Require regulated-domain skills to cite local policy or clinical/business SOP sections.
- Log skill version, domain-risk label, reviewer decision, and downstream action in the trace.
- Prefer workflow/monitoring automation with explicit handoff over autonomous regulated decisions unless the domain case has stronger validation.

### Implementability score

0.69

Adding domain-risk fields, review workflows, and trace labels is straightforward. The harder work is domain-specific validation, reviewer availability, and keeping local procedures current as skills spread across teams and institutions.
