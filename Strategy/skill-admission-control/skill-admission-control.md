# Skill Admission Control

Last updated: 2026-09-02

Primary layer: Strategy / runtime governance

Implementability score: 0.72

Core sources:
- TRUSS: Towards Task-Reliable and User-Safe Automated Agent Skill Generation: https://arxiv.org/abs/2608.17588v1
- TRUSS PDF, immutable v1: https://arxiv.org/pdf/2608.17588v1
- Skill-Inject: https://arxiv.org/abs/2602.20156v1
- SkillSafetyBench: https://arxiv.org/abs/2605.12015v1
- SkillGenBench: https://arxiv.org/abs/2605.18693v1

## Overview

A skill package is no longer a prompt snippet. It is a reusable procedure plus executable resources that a host agent will load with local-user authority. Once that package can write files, run commands, or call tools, installing it is a release decision.

TRUSS is the strongest finding of the 2026-08-13 through 2026-08-19 window because it treats skill generation as a joint functional and safety verification problem. The candidate is not certified by looking finished, sounding useful, or completing a task. It is certified only after a static gate, a shadow execution, and a refinement loop that preserves both utility and safety evidence against one frozen package digest.

## Core innovation

TRUSS splits skill admission into three owned roles:

1. Generator: emit a complete package, not a SKILL.md fragment. Natural-language procedure and bundled scripts enter the same candidate identity.
2. Checker: inspect the artifact first, then observe the behavior it induces. Static inspection covers claims and declared capabilities. Runtime inspection covers requested actions, broker decisions, and final environment state.
3. Refiner: revise only the evidence-bearing spans, keep previously satisfied obligations as preservation constraints, assign a new digest, and restart the whole check.

The useful object is the Function and Safety Record. Each conclusion is bound to an artifact span or an execution event. A blocked action still enters the trace. Residual state after cleanup still belongs to the digest that produced it. Certification is therefore a receipt, not a vibe.

The safety contract is explicit. Nine properties cover control integrity, access boundary, execution integrity, lifecycle isolation, resource boundedness, evidence integrity, authority integrity, composition integrity, and transaction safety. Some properties can be discharged from the artifact. Others become runtime obligations before the model executor ever receives the skill.

The execution substrate is equally explicit. The Controllable Execution Environment mounts the admitted skill as read-only, excludes host resources, disables command networking, terminates HTTP at mock services, and evaluates every requested action through an intermediate breaker. The agent can still ask for a dangerous action. The environment can refuse it and keep the attempt as evidence.

## Why this beat the rest of the week

This week's other finalists were strong and narrower.

- HarnessRisk proves that high utility can coexist with 12.6% to 80.9% attack success, and that configuration is the weakest harness phase. That is the measurement case. It does not say how to admit a new capability.
- Authorization Before Context gives a clean audience-membership rule at memory-to-context admission. That is the recall gate, not the skill-release gate.
- SkillEffect rebuilds bounded tool programs before dispatch. That is the physical-shape gate after a skill is already trusted enough to run.
- On the Fragility of Self-Improving Agents shows that memory writeback needs multi-run and shuffled-order evidence. That is the promotion statistic, not the package contract.
- DeepSeek Harness makes models, tools, skills, sessions, sandboxes, and loops into plugins. That is packaging leverage. Preview status and plugin composability make admission more important, not less.
- Bounded Agents / Agentic Principal Chain already covered Monday's authority-narrowing problem for delegated actions.

TRUSS sits below those findings. Skills are becoming the cheapest way to add durable procedure and executable helpers. If a generated or downloaded package can be installed because the task later succeeded, every other control plane inherits a poisoned procedure.

The decisive evidence is the gap between artifact inspection and induced behavior. On 84 matched SkillInject pairs, a direct LLM checker reached 19.05% recall and 44.64% precision. Static inspection rose to 94.05% recall and 81.55% precision. Adding runtime evidence reached 100.00% on precision, recall, and F1. The remaining errors were not wording problems. They were behaviors that appeared only after the skill was loaded.

Repair and generation make the same point. On 155 SkillSafetyBench cases, repair cut attack success from 38.71% to 19.35% with GPT-5.5 and from 46.45% to 29.68% with GPT-5.4, with zero attack regression. On 187 SkillGenBench tasks, TRUSS raised effectiveness from 17.11% with no skills to 52.94%, and raised the benchmark Security rate from 50.80% to 100.00%. An intermediate LLM generator captured only part of that gain and left 46 unsafe outcomes.

## How it fits into the agentic stack

- Skills as control: a skill is a versioned procedure package. Admission, not authoring, is the privileged operation.
- Runtime governance: loading a skill expands the action surface. The runtime should treat that load as a state transition with a receipt.
- Context-to-execution integrity: writable skill text can inform planning, but execution authority still needs a typed release.
- Untrusted data boundaries: bundled scripts, helper URLs, and later tool outputs are untrusted until the broker says otherwise.
- Agent self-improvement governance: self-authored skills are the highest-risk generator. They need the same digest, shadow run, and preservation constraints as third-party skills.
- Agent harness architecture: DeepSeek-style plugin harnesses and HarnessRisk-style lifecycle scoring both assume a capability can be mounted. The missing piece is the pre-mount certification loop.
- Evidence provenance: every blocked request, observed state, and refinement should cite the exact digest and the exact span or event that justified it.

The stack lesson is simple: skill generation can stay model-driven. Skill admission cannot.

## Practical tools, repos, or methodologies worth trying now

1. Freeze every candidate skill as a content digest before any check. Revisions get a new digest. Never mutate a digest in place.
2. Inspect the complete package, not just SKILL.md. Scripts, references, and assets are part of the candidate.
3. Keep a fixed property catalog. Start with the nine TRUSS boundaries, even if the first observers are coarse.
4. Put an intermediate breaker in front of shell, file, network, and credential tools. Record allow, block, and rewrite decisions.
5. Run a shadow agent in a disposable workspace with host resources excluded and command networking off.
6. Pair every candidate against an empty-skill control on the same task before claiming functional gain.
7. Use official attack and task verifiers separately. Safe task completion is `attack = 0` and `task = 1`. Task completion alone is not a release metric.
8. Feed residual obligations back as a structured revision spec: failed span or event, preservation constraints, and required observation.
9. Quarantine generated or downloaded skills until the record is complete. Exhausting the revision budget should emit an uncertified candidate plus the residual record, not a silent install.

Useful existing surfaces:
- Skill-Inject pairs for detection fixtures: https://arxiv.org/abs/2602.20156v1
- SkillSafetyBench official attack and task verifiers: https://arxiv.org/abs/2605.12015v1
- SkillGenBench generation and reuse protocol: https://arxiv.org/abs/2605.18693v1
- Anthropic Agent Skills package shape: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- DeepSeek Harness as a plugin-shaped host, not a certification oracle: https://github.com/deepseek-ai/deepseek-harness
- HarnessRisk as the post-install lifecycle score: https://arxiv.org/abs/2608.17597v1
- SkillEffect as the later lowering gate for generated tool programs: https://arxiv.org/abs/2608.17007v1

## Implementation complexity

The thin version is buildable now:

1. Store skill candidates as immutable packages with digest, source, and regime labels.
2. Run a static checklist over instructions and bundled files.
3. Load admitted candidates in a disposable sandbox through brokered tools.
4. Score functional gain against an empty-skill control.
5. Block property violations before they reach the host.
6. Keep the Function and Safety Record beside the digest.

The hard version is the one TRUSS actually claims. Property observers must cover composition, residual state, and evidence integrity. Refinement must restore function without reopening a blocked capability. The executor model changes retained utility after repair: GPT-5.5 kept 52.90% safe task completion, while GPT-5.4 kept 23.87%. Scenario coverage is part of the certificate, not a footnote.

That is why the score is 0.72 rather than 0.9. The control objects are clear. A public TRUSS implementation repository was not resolved from the immutable v1 pages, so the first build is a local admission loop, not a drop-in framework.

## What remains conceptual or blocked

- No exact public TRUSS repository was resolved from the v1 abstract, HTML, or PDF.
- 100.00% SkillInject detection is on matched clean/injected pairs, not wild marketplace skills.
- Residual attack success after repair remains 19.35% to 29.68%. Certification is relative to the evaluated scenarios.
- The 100.00% SkillGenBench Security rate is the paper's own property-probe score, not a claim of universal safety.
- CEE mock services and disabled networking hide live-network and credential side channels unless those observers are added.
- Static functional inspection that retrieves "open-world knowledge" can itself become an untrusted evidence path.

## Strategic implications for Danny's product thinking

Hermes, FriendVM, and client agent nodes are already skill hosts. The product question is no longer whether skills are convenient. It is whether a node can prove why a package was allowed to expand the action surface.

A credible agent platform should not say "we support skills." It should show:

- the digest that was admitted;
- the properties that were applicable;
- the shadow actions that were allowed or blocked;
- the empty-skill comparison that justified the functional claim;
- the residual obligations that remain out of scope.

This also changes packaging strategy. DeepSeek Harness and Agent Plugins 1.0 make skills cheaper to compose across clients. That is useful only if each client keeps its own admission record. Portability is not inherited trust.

The durable worldview update is this: a skill is a proposed capability. The runtime owns certification. Task success is evidence in the record, not a substitute for the record.

## August 19 deep dive: why TRUSS is the week's control primitive

The last seven days kept repeating the same seam. Configuration can be mutated inside an authorized workflow. Memory can leak across audiences. Generated tool code can choose an eager access mode. Self-written memories can look like learning under a hidden curriculum. Plugin harnesses can mount almost anything.

Those are all post-admission problems if the skill package itself was never certified.

TRUSS is the missing pre-mount loop. It does not replace HarnessRisk scoring, audience checks, lowering, or shuffled-order promotion. It decides whether a new procedure is allowed to become part of the runtime at all.

## Core and supporting sources

Core:
- https://arxiv.org/abs/2608.17588v1
- https://arxiv.org/pdf/2608.17588v1

Supporting:
- https://arxiv.org/abs/2602.20156v1
- https://arxiv.org/abs/2605.12015v1
- https://arxiv.org/abs/2605.18693v1
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- https://github.com/deepseek-ai/deepseek-harness
- https://arxiv.org/abs/2608.17597v1
- https://arxiv.org/abs/2608.17007v1
- https://arxiv.org/abs/2608.17148v1
- https://arxiv.org/abs/2608.18066v1
- https://arxiv.org/abs/2608.12851v1
- https://arxiv.org/abs/2608.15888v1

## August 21 update: static admission needs source-disjoint proof

MaliciousSkillBench consolidates 9,740 normalized-unique skills from 13 public sources and publishes frozen random, structural-disjoint, and source-disjoint splits. The strongest learned baseline fell from 0.932 random Macro-F1 to 0.665 source-disjoint Macro-F1. It retained 95.6% malicious recall while falsely flagging 62.4% of benign skills from held-out sources.

Practical lesson:
- make source-disjoint evaluation the default static-scanner gate;
- report malicious recall and benign false-positive rate beside Macro-F1;
- keep structural families disjoint during tuning;
- bind scanner version, operating point, package digest, and source provenance to the verdict;
- route uncertain or consequential packages to brokered behavior tests.

The repository and Hugging Face dataset are populated and publish schemas, split manifests, baseline scripts, validation code, and responsible-use guidance. The benchmark contains malicious instructions and must remain inert input.

Sources:
- [MaliciousSkillBench](https://arxiv.org/abs/2608.19901v1)
- [protectskills/MaliciousSkillBench](https://github.com/protectskills/MaliciousSkillBench)
- [MaliciousSkillBench dataset](https://huggingface.co/datasets/ProtectSkills/MaliciousSkillBench)

## September 2 update: admission is not the last gate

Defense-as-Skill shows that a skill can pass install review and still become an attack after a later user task makes an unsafe action look useful. Pre-install scanners, package digests, and safety paragraphs do not see that moment.

The complementary control is a dedicated runtime guard skill with explicit consult-before-action responsibility. It routes proposed effects to allow, replan, or confirmation against the current user task, then leaves sandboxes and permission brokers as the last word. On Claude Code / GLM-5, N = 10, that pattern cut in-distribution attack success from 0.482 to 0.104 while keeping more utility than AcceptEdits.

Practical lesson:
- keep TRUSS-style digest, shadow execution, and preservation constraints at install;
- add a task-conditioned guard after load;
- do not treat capability-skill discovery as sufficient for safety skills;
- add delayed-harm and allowlist-regression fixtures.

No public SkillSonar repository resolved. Implement from the paper's control pattern, not from an unverified artifact.

Sources:
- [Defense-as-Skill](https://arxiv.org/abs/2609.01487v1)
- [Defense as Skill deep dive](../defense-as-skill/defense-as-skill.md)
