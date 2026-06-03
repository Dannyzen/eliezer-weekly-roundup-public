# Skills as Control

Last updated: 2026-06-03

Core sources:
- From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation: https://arxiv.org/abs/2604.21910v1
- Agentic AI-assisted coding offers a unique opportunity to instill epistemic grounding during software development: https://arxiv.org/abs/2604.21744v1
- Thinking with Reasoning Skills: Fewer Tokens, More Accuracy: https://arxiv.org/abs/2604.21764v1
- AEL: Agent Evolving Learning for Open-Ended Environments: https://arxiv.org/abs/2604.21725v1
- OpenAI Codex plugins and skills: https://openai.com/academy/codex-plugins-and-skills
- ComposioHQ/awesome-codex-skills: https://github.com/ComposioHQ/awesome-codex-skills
- Skill Retrieval Augmentation for Agentic AI: https://arxiv.org/abs/2604.24594
- From Skill Text to Skill Structure: https://arxiv.org/abs/2604.24026
- Skills as Verifiable Artifacts: https://arxiv.org/abs/2605.00424v1
- Semia: Auditing Agent Skills via Constraint-Guided Representation Synthesis: https://arxiv.org/abs/2605.00314v1
- An Empirical Study of Agent Skills for Healthcare: https://arxiv.org/abs/2605.02709v1
- SkillSafetyBench: https://arxiv.org/abs/2605.12015v1
- Under the Hood of SKILL.md: https://arxiv.org/abs/2605.11418v1
- Proteus: https://arxiv.org/abs/2605.11891v1
- SkillOps: https://arxiv.org/abs/2605.13716
- Hik289/SkillOps: https://github.com/Hik289/SkillOps
- Sefz semantic fuzzing: https://arxiv.org/abs/2605.13044
- HarnessAPI: https://arxiv.org/abs/2605.22733
- HarnessAPI repository: https://github.com/edwinjosechittilappilly/harnessapi
- Unbrowse: https://github.com/unbrowse-ai/unbrowse
- CodeGraph: https://github.com/colbymchenry/codegraph
- More Skills, Worse Agents?: https://arxiv.org/abs/2605.24050
- CODESKILL: https://arxiv.org/abs/2605.25430
- MUSE-Autoskill: https://arxiv.org/abs/2605.27366
- NVIDIA skills: https://github.com/NVIDIA/skills
- NVIDIA-Verified Agent Skills: https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/
- NVIDIA physical-AI skills release: https://nvidianews.nvidia.com/news/nvidia-releases-major-collection-of-open-source-agent-tools-and-skills-for-physical-ai
- SkillHarm: https://arxiv.org/abs/2606.02540v1
- SkillGuard: https://arxiv.org/abs/2606.03024v1

## Thesis

Skills are not just reusable prompt snippets. In serious agent systems, skills are becoming a control layer: reviewed, scoped, versioned procedural knowledge that constrains model behavior, translates domain language into structured intents, and lets deterministic code perform the final execution.

The pattern is strongest when the LLM is allowed to interpret ambiguous human intent but is not allowed to improvise domain rules, validity constraints, workflow topology, or execution semantics.

## April 26 distribution update: skills are becoming packages

The newest practical signal is that skills are becoming installable packages. OpenAI’s Codex docs define a skill as a playbook Codex can follow for a team-specific process, distinct from a plugin that connects Codex to an external tool or source of information. That boundary is important: plugins grant access; skills constrain procedure.

`ComposioHQ/awesome-codex-skills` turns the pattern into a distribution format. It uses `$CODEX_HOME/skills`, per-skill folders, required `SKILL.md` metadata, optional `scripts/`, `references/`, and `assets/`, and an installer that fetches skills from GitHub. The README also describes progressive disclosure: load metadata to decide whether a skill applies, then load the body only after the skill fires.

That turns the skill from a prompt trick into a software artifact. It can be pinned, reviewed, installed, tested, shared, deprecated, and audited.

## April 28 retrieval update: skills need admission control

Skill Retrieval Augmentation makes the scaling problem explicit. A large skill library cannot be pasted into context. The system has to retrieve a small candidate set, decide whether external procedural knowledge is actually needed, and then load only the useful parts. The paper's SRA-Bench construction is useful because it separates retrieval, incorporation, and end-task execution, and it shows that current agents often load skills indiscriminately even when a gold skill is absent or the task does not require one.

The SSL skill-representation paper adds the missing structure. Skills should expose scheduling signals, execution structure, logic-level action/resource evidence, prerequisites, and side effects. That structure improves both discovery and risk assessment compared with text-only lookup.

Immediate design implication:
- keep short metadata separate from full skill bodies
- retrieve by metadata first, then rerank by task fit
- add a load/no-load gate before consuming context
- normalize skills into invocation interfaces, execution phases, resource touches, side effects, and tests
- log retrieved skills, loaded skills, and task outcomes so stale or harmful skills can be pruned

Sources:
- [Skill Retrieval Augmentation for Agentic AI](https://arxiv.org/abs/2604.24594)
- [From Skill Text to Skill Structure](https://arxiv.org/abs/2604.24026)

## Architecture pattern

1. User goal arrives in natural language.
2. The agent retrieves a small set of relevant skills or grounding documents.
3. The model maps the goal into a typed intent or plan while citing the skill sections it used.
4. Deterministic generators, validators, or tools convert the typed intent into artifacts: DAGs, code, config, test cases, or operational steps.
5. Runtime traces preserve which skills were applied, which constraints were checked, and where execution diverged.
6. Repeated successful trajectories are proposed as new or updated skills only after review.

## What belongs in a skill

Good skills should separate:
- hard constraints: invariants the agent must not violate;
- convention parameters: defaults that are usually right but can be overridden deliberately;
- vocabulary mappings: domain words to schemas, APIs, or workflow objects;
- decision rules: when to choose one path over another;
- examples: short, high-signal cases that clarify boundary conditions;
- tests: checks that prove the skill constrained behavior correctly;
- deterministic helpers: scripts, templates, schemas, or small tools that prevent the model from improvising brittle steps;
- long references: loaded only when needed, not pasted into every turn.

Bad skills are long transcripts, motivational prose, stale checklists, unpinned third-party installers, or untested instructions that silently override newer project facts.

## Why this matters for the agentic stack

The science-workflow paper shows the implementation payoff: Skills improved full-match intent accuracy from 44% to 83%, reduced data transfer by 92% through deferred workflow generation, and kept LLM overhead below 15 seconds with sub-mill cent query cost in the reported Kubernetes setup.

The GROUNDING.md paper shows the governance payoff: field-scoped documents can encode non-negotiable scientific or engineering constraints so non-experts can still generate code that respects domain validity.

The reasoning-skills paper shows the cost payoff: reusable distilled reasoning routines can cut redundant reasoning tokens and improve accuracy.

AEL adds the discipline: memory and reflection help, but piling on more self-improvement mechanisms can degrade outcomes. Skills need to be compact, useful, and tested.

The Codex/Composio packaging pattern adds the operational payoff: skills can be distributed and updated like internal libraries, with metadata-triggered loading instead of always-on context bloat.

## Implementation checklist

- Add `GROUNDING.md` or `SKILLS.md` at the repo, domain, and method levels where agents repeatedly work.
- Package recurring workflows as folders with `SKILL.md`, optional `scripts/`, `references/`, `templates/`, and tests.
- Label sections as hard constraints, conventions, examples, and tests.
- Require agents to cite applied skill sections in plans or generated artifacts.
- Convert plans into typed intents before deterministic execution.
- Pin third-party skill installers or skill repos to reviewed commits.
- Add regression tests that intentionally tempt the agent to violate hard constraints.
- Version skills like source code and review changes before they become default behavior.
- Deprecate or remove skills that are stale, overbroad, or no longer tested.

## Pitfalls

- Treating every remembered fact as a skill.
- Letting skills become huge context dumps.
- Allowing stale skills to outrank current repository state.
- Encoding preferences as hard constraints without owner review.
- Skipping tests, which turns a skill into another unverified prompt.
- Hiding domain assumptions inside examples instead of stating them as constraints.
- Installing community skills without supply-chain review.
- Confusing plugins that grant access with skills that guide process.

## Implementability score

0.94

The pattern is implementable immediately with markdown files, metadata, deterministic helper scripts, retrieval, typed schemas, and regression tests. The remaining hard work is lifecycle management: review, versioning, applicability scoring, deprecation, and supply-chain safety for shared skills.

## April 30 ops update: skills are event-specific retrieval contracts

Bian Que sharpens the skill architecture for operations agents. The key move is Flexible Skill Arrangement: a Skill specifies which operational data and knowledge to retrieve for a given business-module context. That is more precise than a generic prompt playbook. For release interception, proactive inspection, and alert root-cause analysis, the skill should encode the event type, relevant metrics/logs/change events, handbook rules, practitioner knowledge, allowed tools, and verification steps.

The public BianQue Assistant repo describes a practical execution skeleton: Parse → Search → Fetch Data → Build Prompt → LLM Inference → Post-process → Feedback Update. It explicitly leaves context management, tool orchestration, RAG, sandboxing, and data-source connectors to the adopter. That makes it a useful pattern rather than a drop-in agent.

GitHub Trending reinforced the same direction with `obra/superpowers`, `mattpocock/skills`, `browserbase/skills`, and `jcode`: procedural knowledge is becoming packaged, composable, and tied to concrete tool surfaces.

Practical lesson:
- make skills declare required evidence and allowed tools, not just advice
- route by event type and business module before retrieving context
- connect correction feedback to both case memory and reviewed skill patches
- keep generated skill updates reviewable and versioned
- measure skill quality by alert reduction, root-cause accuracy, MTTR, false positives, and operator corrections

Sources:
- [Bian Que](https://arxiv.org/abs/2604.26805v1)
- [BianQue Assistant](https://github.com/benchen4395/BianQue_Assistant)
- [Superpowers](https://github.com/obra/superpowers)
- [Browserbase Skills](https://github.com/browserbase/skills)

## May 4 security update: skills are untrusted code until verified

Skills as Verifiable Artifacts and Semia turn the skill layer into a security and supply-chain problem. The central rule is simple: a skill is untrusted code until it has been verified. Signatures, registries, and known authors help with provenance, but they do not prove that the prose, scripts, tool paths, and human-approval conditions are safe.

Semia makes the analysis shape more concrete. It treats a skill as a hybrid artifact: structured declarations plus natural-language behavior. It then lifts the artifact into a Datalog-style fact base so security properties can be queried as reachability problems: indirect injection, secret leakage, confused deputies, unguarded sinks, and missing HITL checkpoints.

Practical update:
- add explicit verification-level metadata to skill manifests
- keep provenance/signature separate from behavioral verification
- list high-impact sinks and required approvals per skill
- statically review bundled scripts and tool declarations
- route unverified skills through stricter HITL gates
- preserve approval and denial artifacts in the agent trace
- build adversarial skill fixtures that try prompt injection, secret exfiltration, and confused-deputy paths

This tightens the original skills thesis. Skills are still a control layer, but an unverified control layer can become an attack surface.

Sources:
- [Skills as Verifiable Artifacts](https://arxiv.org/abs/2605.00424v1)
- [Semia](https://arxiv.org/abs/2605.00314v1)

## May 5 healthcare update: domain-risk labels are part of skill governance

An Empirical Study of Agent Skills for Healthcare adds an empirical domain-governance layer. The authors filtered 557 healthcare-related skills from 58,159 public skills on ClawHub and annotated them across function, deployment context, autonomy, and safety dimensions. The key finding is that public healthcare skills cluster around patient-facing workflow automation and monitoring, while healthcare-agent research often emphasizes diagnosis and treatment. The paper also warns that general technical risk does not reliably capture clinical risk.

The practical lesson is that skill manifests need domain-risk fields, not just tool names and autonomy labels:
- domain and workflow phase
- affected record type and data sensitivity
- action class and escalation path
- required reviewer role
- local SOP or policy citation
- skill-version and domain-risk label in every trace

This extends the May 4 verification rule. A skill is untrusted until verified, and in regulated domains verification has to include domain validity, not only script safety and provenance.

Source:
- [An Empirical Study of Agent Skills for Healthcare](https://arxiv.org/abs/2605.02709v1)

## May 13 update: skills are semantic supply-chain surfaces

SkillSafetyBench, Under the Hood of SKILL.md, and Proteus make the skill-security boundary explicit. Skills package procedural text, scripts, tools, files, memory assumptions, and execution privileges. That means skill metadata and instructions can shape discovery, selection, governance, and runtime behavior before the user ever asks for anything malicious.

The practical correction is to stop treating SKILL.md as passive documentation. It is operational text. It can improve adversarial visibility in embedding retrieval, bias an agent toward an unsafe variant, evade semantic governance checks, or steer a benign task through unsafe local artifacts. Adaptive attackers make this worse because they can mutate a skill after seeing audit and runtime feedback.

Practical update:
- pin third-party skills to reviewed commits and record the loaded body hash in traces
- require skills to declare allowed tools, file/network scopes, memory-write behavior, side effects, and approval points
- keep registry discovery text, selection descriptions, full instructions, scripts, and runtime outputs under separate review surfaces
- build adversarial fixtures for prompt injection, secret exfiltration, unsafe scripts, stale policy, and confused-deputy behavior
- evaluate skills with rule-based verifiers and adaptive red-team loops, not only provenance checks or LLM-as-judge reviews
- treat public skill marketplaces as supply chains: provenance is necessary, but behavioral verification is the control that matters

Sources:
- [SkillSafetyBench](https://arxiv.org/abs/2605.12015v1)
- [Under the Hood of SKILL.md](https://arxiv.org/abs/2605.11418v1)
- [Proteus](https://arxiv.org/abs/2605.11891v1)
- [Anthropic skills repository](https://github.com/anthropics/skills)

## May 14 update: skill libraries need library-time maintenance and semantic fuzzing

SkillOps turns the skill layer from packaging into operations. A useful skill registry is not only a folder of `SKILL.md` files; it is a maintained library with contracts, validators, dependency edges, compatibility checks, and retirement paths. The paper's P/O/A/V/F contract shape is useful because it makes a skill inspectable before retrieval: what preconditions must hold, what operation is allowed, what artifact is produced, what validator proves success, and which failure modes are known.

Sefz adds the missing negative test. A skill can violate its own stated guardrails under benign requests, without any explicit attacker string. Translating natural-language guardrails into trace predicates and fuzzing for ordinary inputs that reach violations is the right way to test whether the skill is actually a control surface.

Practical lesson:
- represent high-value skills as explicit contracts, not only prose
- maintain library-level edges for dependency, redundancy, alternatives, compatibility, and lineage
- add validators and adapters as first-class maintenance actions
- run semantic fuzzing against trace-level guardrail predicates
- log loaded skill hash, contract version, validator result, and side effects on every run
- retire or quarantine stale and under-validated skills before retrieval can select them

Sources:
- [SkillOps](https://arxiv.org/abs/2605.13716)
- [Hik289/SkillOps](https://github.com/Hik289/SkillOps)
- [Sefz semantic fuzzing](https://arxiv.org/abs/2605.13044)


## May 20 update: skills need feedback-bandwidth admission control

When Skills Don't Help is valuable because it is a negative result. It argues that procedural skill packs can become redundant overhead when the environment already gives strict, low-latency, schema-validated feedback. In that setting the tool layer itself supplies the correction signal that a skill would otherwise provide.

This does not weaken the skills thesis. It sharpens it. Skills are a control layer when they add missing procedure, constraints, or domain structure. They are context debt when they restate what the environment already proves through validators, error messages, and immediate state feedback.

Practical lesson:
- add a skill load/no-load gate before full skill retrieval
- measure marginal skill value against no-skill and thin-skill baselines
- log loaded skill hash, tool-feedback quality, retries, token cost, and task outcome
- improve tool errors and validators before adding more procedural markdown
- quarantine or retire skills that correlate with retries, policy misses, or worse completion

Sources:
- [When Skills Don't Help](https://arxiv.org/abs/2605.20023v1)

## May 24 update: skills are becoming executable API surfaces

HarnessAPI, Unbrowse, and CodeGraph push the skills thesis from prose packages into executable infrastructure. HarnessAPI treats a typed skill folder as the source of truth and derives a streaming HTTP endpoint, OpenAPI/Swagger surface, and MCP tool from the same handler and Pydantic schemas. Unbrowse turns repeated browser work into reusable API-native MCP paths. CodeGraph moves codebase context into a local graph surface so agents do not rediscover the same structure through repeated scanning.

The durable lesson: a skill that matters should not stay as untyped advice forever. It should eventually become a reviewed contract with schema, validator, timeout, permission scope, trace hash, and callable interface.

Practical lesson:
- start high-value skills with explicit input/output schemas;
- expose stable skills through both HTTP and MCP only when the permission model is clear;
- keep skill docs, OpenAPI schemas, MCP tool declarations, and validators generated from one source of truth;
- turn browser/API discoveries into reviewed route assets, not automatic authority;
- log compiled-surface version, schema hash, tool arguments, output shape, and side effects on every invocation.

Sources:
- [HarnessAPI](https://arxiv.org/abs/2605.22733)
- [edwinjosechittilappilly/harnessapi](https://github.com/edwinjosechittilappilly/harnessapi)
- [Unbrowse](https://github.com/unbrowse-ai/unbrowse)
- [CodeGraph](https://github.com/colbymchenry/codegraph)

## May 25 update: skills need optimizer discipline and ecosystem audits

SkillOpt and OpenSkillEval push the skill layer from packaging into validation. SkillOpt treats a skill document as external trainable state for a frozen agent: proposed text edits are bounded, evaluated against rollout scores, and accepted only when a held-out validation score improves. OpenSkillEval adds the ecosystem audit shape: realistic artifact-generation tasks across reports, presentations, posters, data visualization, and web design.

The practical correction is that skill updates should look more like software changes than memory consolidation:
- candidate patch;
- task fixture;
- held-out validation result;
- expected improvement;
- at-risk regressions;
- rejected-edit memory;
- loaded skill hash in runtime traces;
- rollback path.

This keeps the skills thesis intact while removing the sloppy version. Skills are a control layer only when they are tested, scoped, and maintained. Untested self-editing skills are just mutable prompt debt.

Sources:
- [SkillOpt](https://arxiv.org/abs/2605.23904)
- [OpenSkillEval](https://arxiv.org/abs/2605.23657)
- [OpenSkillEval project](https://yingjiahao14.github.io/OpenSkillEval-Web/)

## May 26 update: skill shadowing makes selection the bottleneck

CODESKILL is the positive case for self-evolving skills: coding trajectories can be distilled into procedural skills, evolved from experience, and maintained as a compact skill bank with reinforcement learning from rubric and execution feedback. Skill Shadowing is the necessary warning label: expanding a library can degrade performance by up to 21% because agents select the wrong skill more often as the library grows.

The immediate correction is that skill-bank quality is not the number of skills. It is selection precision under realistic tasks. If selection fails, better skill prose does not matter.

Practical lesson:
- evaluate skill selection separately from skill execution;
- keep active skill candidates small through metadata retrieval, reranking, and a load/no-load gate;
- run no-skill, thin-skill, and full-library baselines before claiming a skill library helps;
- log selected skills, rejected candidates, loaded hashes, token cost, retries, and task outcomes;
- require generated or self-edited skills to improve held-out tasks before entering default retrieval;
- add “shadowing” fixtures with plausible but wrong skills to test router precision.

Sources:
- [CODESKILL](https://arxiv.org/abs/2605.25430)
- [More Skills, Worse Agents?](https://arxiv.org/abs/2605.24050)

## May 27 update: skills need lifecycle memory and promotion gates

MUSE-Autoskill adds the lifecycle vocabulary for the skill stack: creation, memory, management, evaluation, and refinement. The useful part is not autonomous markdown generation. It is making each skill a long-lived asset with its own use history, failure cases, tests, runtime feedback, and transfer record.

This sharpens the May 26 skill-shadowing warning. A skill library gets worse when it grows faster than its selection and validation system. The next implementation primitive is per-skill lifecycle memory plus promotion gates.

Practical lesson:
- store per-skill use history, rejected contexts, failures, patches, validators, and held-out fixtures;
- evaluate selection quality separately from execution quality;
- promote generated or patched skills only after held-out improvement;
- keep active candidates small through metadata retrieval, reranking, and load/no-load gates;
- quarantine stale or harmful skills before retrieval can select them.

Source:
- [MUSE-Autoskill](https://arxiv.org/abs/2605.27366)

## June 1 update: verified skills make capability governance concrete

NVIDIA's public skills catalog and verified-skills governance blog turn the skills thesis into a vendor-backed operating pattern. Skills are portable instruction sets, but the important part is the metadata and verification envelope: provenance, risk scanning, cryptographic signing, skill cards, ownership, dependencies, limitations, and verification status.

The physical-AI release makes the capability surface concrete. NVIDIA describes skills for turning complex robotics, autonomous-vehicle, vision-AI, and industrial digital-twin workflows into repeatable agent-executable instructions. That is the right abstraction: a skill is not merely advice. It is a reviewed capability package that can route the agent into a high-leverage domain workflow.

Practical lesson:
- treat high-value skills as supply-chain artifacts with owner, scope, dependency, risk, signature, and validation metadata;
- log loaded skill hash, source repository, verification level, and selected version in every trace;
- keep installable skill catalogs separate from production-admitted skill catalogs;
- require domain-specific regression fixtures before a skill can operate near privileged tools or expensive workflows;
- pair skill lifecycle memory with static verification so stale or harmful skills are quarantined before retrieval can select them.

Sources:
- [NVIDIA/skills](https://github.com/NVIDIA/skills)
- [NVIDIA-Verified Agent Skills Provide Capability Governance for AI Agents](https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/)
- [NVIDIA physical-AI skills release](https://nvidianews.nvidia.com/news/nvidia-releases-major-collection-of-open-source-agent-tools-and-skills-for-physical-ai)

## June 2 update: skill attacks now span the whole lifecycle

SkillHarm makes the next skill-security problem explicit. A malicious skill does not have to fire in the same task where it enters the system. Fixed-payload poisoning can compromise every session that invokes the skill, while self-mutating poisoning can start from a benign-looking execution, change persistent skill content, and defer harm until later reuse.

The practical correction is to treat skill execution state and skill library state as separate authority surfaces. A skill should not be able to mutate itself, another skill, memory policy, tool configuration, or retrieval metadata just because the current task has file access. Production-admitted skills need immutable execution snapshots, reviewed patch paths, loaded-hash traces, and lifecycle tests that cover installation, retrieval, execution, update, reuse, quarantine, and rollback.

Practical lesson:
- freeze the loaded skill body during execution and record its hash;
- block or route skill-file writes through a reviewed patch queue;
- test fixed-payload and self-mutating skill poisoning separately;
- treat memory writes and tool-config writes from a skill as high-risk side effects;
- preserve source, version, manifest hash, body hash, verification level, and update path in every trace.

Source:
- [SkillHarm](https://arxiv.org/abs/2606.02540v1)

## June 3 update: skill permissions need context and side-effect planes

SkillGuard supplies the runtime-policy primitive that SkillHarm implies. A skill should declare not only what it is for, but what context it may inject and what side effects it may induce. Those are separate planes. Context influence can steer the model toward a tool path even when the skill never calls a tool directly; action side effects are the concrete file, network, memory, tool, or external-observation consequences of that influence.

The implementation correction is to bind runtime authority to the skill artifact itself. The trace should know which skill body and manifest were loaded, which sections influenced the plan, which tool calls or writes followed, and whether those effects stayed inside declared scope. A generic tool allow-list is too blunt; it says a tool is callable, not that this skill had authority to cause this call for this task.

Practical lesson:
- require skill manifests for context influence, tool scope, file scope, network scope, memory-write scope, and approval points;
- bind side effects to the skill that influenced them, not only to the final agent message;
- enforce deny-by-default behavior when runtime actions exceed the skill manifest;
- test context-to-action escalation with adversarial skills that never explicitly ask for a forbidden call;
- record skill manifest hash, body hash, authorization decision, and side-effect evidence in the run trace.

Source:
- [SkillGuard](https://arxiv.org/abs/2606.03024v1)

