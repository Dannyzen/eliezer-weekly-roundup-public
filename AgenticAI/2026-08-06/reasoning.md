# AgenticAI Daily Analysis - 2026-08-06

## Verdict

Today's implementation signal is pre-action evidence quality. Skills, tool catalogs, and coding-agent routers all fail in different ways when the harness trusts names, issue text, or unrevalidated memory. The useful units are progressive skill disclosure, planted canary tools, and scout-then-verify routing receipts.

## Skill-Use separates trigger, compliance, and boundary under progressive disclosure

Skill-Use evaluates whether an agent can use skills the way production catalogs actually expose them. The agent sees only a skill name and short description, must retrieve the full procedure, then execute inside an isolated Docker sandbox with full tool access. The benchmark grades three facets separately:

- Trigger: did the agent invoke the relevant skill?
- Compliance: did it follow the prescribed procedure?
- Boundary: did it avoid forbidden operations?

A gated Skill-Use score credits execution only after the skill is triggered. The package pairs 79 real community skills with 177 executable tasks across nine domains, 177 trajectory rubrics, and 1,314 scoring items, of which 882 are skill-derived. The paper evaluates eight models under two agent harnesses.

Why it matters: skill quality and end-task success hide the failure mode that matters in Hermes-style catalogs. An agent can ignore the right skill, half-follow it, or succeed while violating the skill's forbidden operations. Progressive disclosure is the real product surface, not the fully pasted skill body used in many lab demos.

Implementable now:

- grade skill runs on trigger, compliance, and boundary separately;
- expose skills first as name plus short description, then require explicit retrieval before full procedure injection;
- keep trajectory rubrics and sandbox fixtures with the skill identity and hash;
- refuse to score procedure following when the agent never triggered the skill;
- use Skill-Use-style negative items for forbidden tool or file operations.

Tools and repositories worth exploring:

- Skill-Use-Bench, Docker sandbox fixtures, trajectory rubrics, Hermes skill catalogs, progressive disclosure loaders

Evidence and caveat: the public repository is populated and documents the benchmark layout. This scan inspected the paper, abstract page, and README read-only and did not execute the harness. Treat the facet split as the durable method even if individual model leaderboard numbers move.

Implementability score: 0.76

Core sources:

- https://arxiv.org/abs/2608.04828v1
- https://github.com/JinyiHan99/Skill-Use-Bench

## Canary tools turn wrong-tool outcomes into a failure taxonomy

Canary Tools plants diagnostic probe tools into an MCP-style tool set. Each canary is engineered to catch one tool-selection weakness:

- semantic decoys
- parameter traps
- capability mirages
- prerequisite blindness
- temporal decoys
- granularity traps

Instead of a single wrong-tool bit, the harness returns a multi-dimensional susceptibility profile. The paper evaluates eight models across three capability tiers on 120 tasks, three canary-density conditions, and three seeds for 8,640 runs, plus a 2,880-run subtlety ablation. Declared-condition canary susceptibility rates span roughly 0.010 for the strongest hosted model to 0.378 for Llama 3.1 8B, about a 36x spread. Capability mirages remain useful against strong models, while several other trap types fire mainly on weaker open models.

Why it matters: MCP and tool-gateway dashboards usually stop at selected tool name and task success. That hides whether the model is over-trusting descriptions, skipping prerequisites, choosing the wrong granularity, or chasing a more powerful sounding tool. Canaries make those failure modes measurable without waiting for production incidents.

Implementable now:

- generate one canary family per admitted real tool schema;
- inject canaries at controlled density during eval and shadow traffic;
- log selected tool, rejected alternatives, canary type, and task success together;
- block catalog promotion when susceptibility exceeds a fixed budget on high-risk tool classes;
- treat description-only privilege claims as untrusted until prerequisite checks pass.

Tools and methodologies worth exploring:

- MCP tool registries, schema-derived decoy generators, tool-selection fixtures, gateway allowlists, trajectory labels

Evidence and caveat: this scan verified the arXiv abstract and PDF text. No paper-owned public implementation repository resolved from the primary pages, so the method is implementable from the taxonomy while the exact generator remains unreproduced here.

Implementability score: 0.60

Core source: https://arxiv.org/abs/2608.04719v1

## SuperScout routes coding agents only after scouting and stripping false claims

SuperScout changes the routing unit for repository-level repair. A 7B searcher first explores the repository and emits a structured handoff. Reproduction claims are sandbox-verified, false claims are stripped, and only then does a resume-based router dispatch the task to one of four frontier fixers. Adding a fixer does not require retraining. On the full Python slice of SWE-bench Pro under the official capped budget tier, SuperScout solves 159 of 266 tasks versus 158 for the best solo fixer, at about one fifth the total cost per solve at a matched solve rate. The public artifact set includes the verify-then-strip gate, frozen router head, contamination blocklist, label-run data, and per-task receipts.

Why it matters: issue-text routers allocate expensive coding capacity before the agent has any grounded repository state. SuperScout makes the scout trajectory and verified handoff part of the routing evidence. The durable control pieces are claim verification, false-claim stripping, and a frozen router that can accept new backends without a new training loop.

Implementable now:

- scout the repository before model selection;
- require structured handoffs with sandbox-checked reproduction claims;
- strip failed claims before the fixer prompt is built;
- route from scout hidden state plus task text, not issue text alone;
- keep paired solo and routed receipts so cost and solve rate stay recomputable;
- add a new fixer by extending the backend set, not by retraining the router.

Tools and repositories worth exploring:

- TransformerOptimus/superscout, SuperScout-7B model card, SWE-bench Pro receipts, verify-then-strip gates, numpy router heads, Hermes coding lanes

Evidence and caveat: the repository is public, Apache-2.0 for code, CC-BY-4.0 for data, and documents claims-to-artifact mapping. This scan inspected metadata, README, tree, and paper text read-only and did not run the searcher or fixers. Cost and solve claims are paper and README reported against SWE-bench Pro Python-266.

Implementability score: 0.80

Core sources:

- https://arxiv.org/abs/2608.04804v1
- https://github.com/TransformerOptimus/superscout
- https://huggingface.co/SuperAGI/SuperScout-7B

## Current implication

Do not let names decide authority. A skill name, tool description, or GitHub issue is only a lead. The harness should force retrieval, plant traps for false confidence, and spend frontier capacity only after a verified local scout.
