# Evidence Provenance Control Plane

Last updated: 2026-07-03

Core sources:
- ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents: https://arxiv.org/abs/2606.18037v1
- All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code: https://arxiv.org/abs/2606.18168v1
- Offline Preference-Based Trajectory Evaluation: https://arxiv.org/abs/2606.17541v1
- Zscaler agentic AI security platform announcement: https://www.zscaler.com/press/zscaler-unveils-new-product-innovations-secure-agentic-ai
- Salesforce Agentforce Multi-Agent Orchestration: https://www.salesforce.com/agentforce/multi-agent-orchestration/

## Overview

The strongest finding from the 2026-06-11 to 2026-06-17 window is ProvenanceGuard. The paper's narrow claim is source-aware factuality for MCP agents. The broader architectural lesson is bigger: serious agent systems need evidence ownership, not just evidence presence.

A sourced answer is not trustworthy because the answer includes links. A coding-agent PR is not trustworthy because it includes test files. A multi-agent handoff is not trustworthy because the platform routed it to a specialist. Each one needs a durable evidence path that says which source, tool output, skill, trajectory segment, oracle, policy verdict, or delegated agent actually carried the proof.

This won the week over the other strong candidates because it generalizes across them. SkillWeaver makes skill routing compositional. All Smoke, No Alarm shows that agent-authored tests often lack real oracles. Offline trajectory preferences recover partial-progress signal from traces. Zscaler and Salesforce show the market packaging agent identity, access graphs, MCP/A2A brokerage, observability, and delegation traces as control-plane features. ProvenanceGuard names the shared primitive: bind claims and actions to source-owned evidence.

The durable insight is:

> Agent governance is becoming evidence provenance engineering.

Without that layer, teams will keep confusing verification theater with verification. The answer can be supported by the wrong source. The test can execute code without checking behavior. The subagent can complete a task without a traceable delegation contract. The gateway can log traffic without knowing which source owned the final claim.

## Core innovation

The core innovation is separating support from source ownership.

ProvenanceGuard observes that standard factuality checks usually pool retrieved evidence and ask whether the answer is supported somewhere in the available context. That misses cross-source conflation: a claim may be true in one source but falsely attributed to another. The paper's example is a medical-style attribution swap, where a trial abstract supports a drug mortality endpoint but the patient's chart does not. A source-blind verifier can approve the answer; a source-aware verifier should reject the attribution.

The ProvenanceGuard pipeline is the useful architecture:

1. Capture MCP traces with stable tool IDs, source IDs, and raw tool outputs.
2. Decompose the final answer into atomic claims.
3. Route each claim to source-specific evidence, not pooled context.
4. Check support with NLI plus token-alignment evidence.
5. Compare the claim's stated attribution with the routed source.
6. Return per-claim source verdicts plus an answer-level allow/block decision.
7. Repair blocked answers and re-verify them.

The reported results are strong enough to matter and weak enough to be useful. On a 40-trace, 361-claim held-out split from 281 captured medical-domain MCP-agent traces, ProvenanceGuard reports block F1 0.802 and source accuracy 0.858 over 260 source-eligible claims. Source-blind baselines such as MiniCheck, RAGAS Faithfulness, AlignScore, and SummaC-ZS can score support, but they do not emit claim-to-source IDs. On a harder multi-source benchmark, ProvenanceGuard keeps block F1 at 0.846 while source-plus-relation accuracy drops to 0.229. That is the real lesson: exact evidence ownership is an independent axis, and it is hard when sources are semantically close.

## Why it matters

The agentic stack is filling with artifacts that look like proof but may not be proof.

- A citation can be a decoration unless every claim maps to the cited source.
- A trace can be an audit log unless it preserves source IDs, policy IDs, raw-output handles, and final claim routing.
- A test file can be theater unless it contains an oracle that checks expected behavior.
- A skill can be dangerous authority unless the runtime knows why it was selected, what version loaded, and whether it improved performance over a no-skill baseline.
- A multi-agent delegation can be an accountability gap unless the route, specialist identity, task scope, and returned evidence are bound into one trace.

All Smoke, No Alarm shows the coding-agent version. It studies 86,156 test-file patches from 33,596 agent-authored PRs across 2,807 GitHub repositories from OpenAI Codex, GitHub Copilot, Devin, Cursor, and Claude Code. It finds that 80.2% of agent-authored test patches contain weak or no explicit oracle signals. Strong oracles improve merge likelihood after adjustment (OR 1.28, p < 0.001). The file exists, but the proof may not.

Offline Preference-Based Trajectory Evaluation shows the harness version. Success-rate metrics create ties on roughly 75% of instance-level comparisons, while trajectory-aware preferences reduce ties to roughly 35%. The run ended, but the final score discards useful evidence about progress and recovery.

The strategic implication is direct: if agent platforms do not make evidence ownership a first-class control-plane primitive, operators cannot distinguish real verification from artifacts that merely resemble verification.

## How it fits into the strategic layer

This belongs primarily in Strategy because the load-bearing decision is who owns the evidence boundary between agent behavior and institutional trust.

Stack placement:

- **Source identity layer:** stable IDs for tools, sources, datasets, documents, APIs, users, agents, and delegated specialists.
- **Trace layer:** raw-output handles, tool-call spans, source IDs, claim IDs, skill IDs, policy IDs, oracle IDs, and delegation IDs.
- **Claim layer:** atomic answer claims with routed source evidence and attribution verdicts.
- **Verification layer:** NLI, entailment, citation checks, token alignment, oracle-strength checks, mutation tests, and trajectory preferences.
- **Gateway layer:** source-aware MCP/A2A brokerage, access graphs, credential custody, policy checks, and data-lineage preservation.
- **Release layer:** final answer, PR, workflow completion, or external effect is accepted only when the required evidence fields exist and pass.
- **Audit layer:** operators can replay the run, inspect why each source was trusted, and identify which proof artifact failed.

This also clarifies how the week's runners-up fit. Skill routing, context pruning, trajectory preferences, and test-oracle checks are not separate themes. They are all evidence-provenance subproblems. Each asks the same control-plane question: which artifact had authority, and what verified it?

## Practical tools, repos, and methodologies worth trying now

Build the thin version now. Do not wait for a perfect provenance framework.

### Tools and repos

- **MCP trace schema extensions** for `tool_id`, `source_id`, `raw_output_ref`, `claim_id`, `policy_id`, `delegation_id`, and `verifier_result`.
- **Pydantic or JSON Schema** for evidence packets attached to answers, PRs, memory writes, and delegated tasks.
- **MiniCheck, RAGAS Faithfulness, AlignScore, SummaC-ZS, or NLI/entailment models** as support estimators, with the caveat that support scoring is not source ownership.
- **Langfuse, LangSmith, OpenTelemetry, or JSONL trace exports** for trace-linked evidence, tool spans, verifier spans, and source verdicts.
- **OPA, Cedar, or OpenFGA** for deterministic policy checks over principal, source, tool, data class, workflow state, and approval artifact.
- **Mutation testing, property-based tests, assertion-density checks, and AST rules** for oracle-aware review of agent-authored tests.
- **Pairwise trajectory comparison and progress ledgers** for grading runs that do not cleanly pass or fail.
- **Agent registries and access graphs** for mapping which agents, users, identities, models, applications, and data sources are allowed to communicate.

### Methodologies

1. **Name the evidence-bearing artifact.** For each workflow, define whether the proof should be a source-owned claim, a test oracle, a policy verdict, a trajectory checkpoint, a signed approval, or a delegated-agent return packet.
2. **Require stable IDs.** Tool names and citations are not enough. Store source IDs, raw-output references, trace IDs, skill hashes, policy IDs, and verifier versions.
3. **Split support from attribution.** Score whether a claim is supported and whether the claim is supported by the source it names.
4. **Block proof theater.** Reject answer citations without claim routing, tests without oracles, skills without utility evidence, and handoffs without delegation traces.
5. **Preserve raw evidence out-of-band.** Do not stuff all raw evidence into the prompt. Keep handles in trusted storage and put compact evidence packets into the runtime trace.
6. **Create adversarial fixtures.** Test source swaps, stale citations, self-mocking tests, wrong-skill retrieval, cross-tenant source leakage, and specialist-agent laundering.
7. **Review evidence schemas like APIs.** Evidence fields are product contracts. Version them, diff them, and fail CI when they disappear.

## Implementation complexity

Implementability score: 0.76

A thin version is implementable with existing tracing, claim extraction, policy, and test-analysis tools. A production version is platform work because evidence has to survive across tools, agents, documents, skills, tests, memory writes, and external effects.

### Implementable now

- Add `source_id` and `raw_output_ref` fields to MCP tool outputs.
- Attach `claim_id`, `source_id`, and support verdicts to high-risk generated answers.
- Store raw tool outputs in a trusted evidence store and pass handles through traces.
- Run source-aware checks on critical reports, medical-style summaries, legal-style summaries, financial recommendations, and user-visible research answers.
- Add a CI check that classifies agent-authored tests by oracle strength before merge.
- Store progress checkpoints and time-to-return profiles for agent evaluation runs.
- Log agent identity, delegated specialist, selected tool, denied tool, policy verdict, approval artifact, and final evidence packet in the same trace.

### Architecture-heavy

- Reliable source attribution when many sources are semantically close.
- Data-lineage propagation through summaries, memory writes, embeddings, screenshots, generated files, and delegated subagents.
- Evidence compaction that preserves auditability without exploding prompt cost.
- Cross-system identity binding across MCP, A2A, SaaS APIs, local tools, model providers, and subagents.
- Operator UX for inspecting proof packets without reading full transcripts.
- Verifier independence. A repair loop that re-verifies with the same verifier is useful for consistency, but it is not independent proof of domain completeness.

The score is above 0.7 because the first implementation can be built from current primitives. It stays below 0.8 because the hard part is not the first schema field. The hard part is making evidence ownership durable across the whole run.

## Strategic implications for Danny's worldview and product thinking

This strengthens the repo's current thesis: the agentic stack is moving from broad context and permissive tool catalogs to trace-governed operational units.

For Danny's product thinking, evidence provenance should be a visible product surface, not hidden observability plumbing. A serious local-first or enterprise agent runtime should let an operator ask:

- Which source owns this claim?
- Which raw tool output is the evidence?
- Which skill or policy admitted this action?
- Which oracle proved the agent-authored test checked behavior?
- Which trace segment shows progress rather than lucky final success?
- Which specialist agent received the delegated task, under what scope, and what evidence did it return?
- Which data path, identity, and access graph allowed or denied the action?

That points to a product moat for Hermes/Friend Node style systems: not more tools by default, but better proof boundaries. Local-first agents can own raw evidence, source IDs, skill hashes, and traces close to the user. Cloud gateways can sell access graphs and brokered observability. The winning system will likely combine both: local evidence custody plus portable proof packets for collaboration, review, and enterprise policy.

## Why this beat the other candidates this week

The other candidates were strong, but each is a subsystem of the provenance problem:

- **SkillWeaver and agentic skill evaluation** gave the best skill-library architecture: decompose, retrieve, compose, and evaluate skills. It lost because skill evidence is one type of evidence, not the control plane itself.
- **All Smoke, No Alarm** gave the most immediately actionable coding-agent gate: reject smoke-only tests. It lost because test oracles are one proof surface; source-owned evidence covers answers, tests, tools, skills, memory, and delegation.
- **Offline Preference-Based Trajectory Evaluation** gave the cleanest evaluation upgrade: compare progress and time-to-return, not only pass/fail. It lost because trajectory preference is a trace-scoring method, while provenance defines what the trace must carry.
- **Hugging Face's Strands Robots and olmo-eval releases** were useful implementation signals. They lost because they are product/tooling moves, not the week's load-bearing architecture shift.
- **Zscaler and Salesforce** were strong market validation, but they are packaging the control-plane trend rather than defining the technical primitive.

ProvenanceGuard won because it names the primitive that all of those findings need: source-owned, replayable evidence attached to every claim, action, test, and handoff.

## What remains conceptual or unresolved

- ProvenanceGuard does not publish a verified implementation repository in the paper artifact I checked, so treat it as a design and evaluation reference, not a drop-in package.
- The source-aware benchmark is strongest in a medical-domain MCP setting. General enterprise, legal, coding, and multi-agent systems need their own source-ownership fixtures.
- Source-plus-relation accuracy dropping to 0.229 on the harder benchmark is a warning. The method detects the right problem, but exact attribution remains difficult.
- Vendor control-plane announcements validate the market direction, but they do not prove interoperable evidence schemas.
- Evidence ownership can become expensive. The product has to decide which workflows require claim-level proof and which can use lighter trace evidence.

## Core source links

- ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents: https://arxiv.org/abs/2606.18037v1
- All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code: https://arxiv.org/abs/2606.18168v1
- Offline Preference-Based Trajectory Evaluation: https://arxiv.org/abs/2606.17541v1
- Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose: https://arxiv.org/abs/2606.18051v1
- Zscaler Unveils New Product Innovations to Secure Agentic AI: https://www.zscaler.com/press/zscaler-unveils-new-product-innovations-secure-agentic-ai
- Salesforce Agentforce Multi-Agent Orchestration: https://www.salesforce.com/agentforce/multi-agent-orchestration/
- Hugging Face, From the Hub to robot hardware with Strands Agents and LeRobot: https://huggingface.co/blog/amazon/strands-lerobot-hub-to-hardware
- Hugging Face, olmo-eval: An evaluation workbench for the model development loop: https://huggingface.co/blog/allenai/olmo-eval

## July 2 update: reasoning transitions need evidence licenses

Theoria sharpens this topic by moving from claim-level provenance to transition-level provenance. A final answer can look supported while hiding an unsupported mutation between reasoning states. Theoria's completeness-of-change invariant says every difference between consecutive states needs an explicit license, such as a citation, computation, or problem-given fact.

Practical lesson:
- represent high-risk reasoning, memory updates, and final recommendations as state transitions;
- diff consecutive states and require each change to cite a license type and evidence ID;
- treat hidden premises, fabricated citations, stale source swaps, and unsupported memory updates as verifier fixtures;
- preserve transition-ledger verdicts in the same trace as tool calls and policy decisions;
- use holistic LLM judges as coverage aids, not as the only proof surface.

Sources:
- [Theoria](https://arxiv.org/abs/2607.01223v1)
- [zaladbar/theoria](https://github.com/zaladbar/theoria)

## July 3 update: context eligibility comes before retrieval relevance

ContextNest strengthens the evidence-provenance topic by putting governance below retrieval. The question is not only whether an answer cites a source. It is whether that source version was approved, current, integrity-verified, attributable, and reconstructable when the agent consumed it.

Practical lesson:
- pre-filter retrieval through deterministic context selectors;
- preserve document version IDs, integrity hashes, approval state, and source identity;
- store context consumption audit traces alongside answer or action evidence;
- use graph checkpoints or equivalent snapshots for point-in-time reconstruction;
- treat dense retrieval over an ungoverned corpus as relevance, not proof.

Sources:
- [ContextNest](https://arxiv.org/abs/2607.02116v1)
- [PromptOwl/ContextNest](https://github.com/PromptOwl/ContextNest)
- [PromptOwl/context-nest-spec](https://github.com/PromptOwl/context-nest-spec)


## July 30 update: evidence quality needs a pre-action gate

SARC-DQ demonstrates the placement rule for provenance controls. Payload-only agents cannot detect stale, superseded, or lineage-defective evidence when the discriminating metadata never enters context. A metadata-aware gate immediately before action can block or substitute covered defects without granting the agent write authority over the source system.

Practical lesson:
- carry freshness, source, version, lineage, schema, and completeness metadata to the action boundary;
- evaluate deterministic predicates before side effects;
- perform downstream-only repair in a governed buffer;
- log admitted evidence IDs, predicate versions, substitutions, uncovered classes, action intent, and final effect;
- pair corrupted and clean runs to price the action delta;
- publish predicate coverage and declared gaps as part of the control contract.

Evidence caveat: the populated MIT repository is an alpha research artifact. The paper is single-author and the measured environment is one priced replenishment task.

Sources:
- [SARC-DQ](https://arxiv.org/abs/2607.26313v1)
- [besanson/dqSarc](https://github.com/besanson/dqSarc)

## August 16 update: graders and benchmarks also need provenance authority

Labels Are Not Endpoints and Vero extend evidence provenance into evaluation governance. A stored label is not behavioral proof when treatment identity enters the endpoint. A failed proof attempt is not agent failure when the specification or reference is defective.

Practical lesson:
- bind labels to exact request and execution evidence;
- run treatment-invariance tests before publishing security results;
- preserve endpoint code, evidence hashes, denominators, and authorization state;
- accept machine-checkable benchmark-defect evidence;
- version corrected benchmarks without rewriting historical attempts.

Sources:
- [Labels Are Not Endpoints](https://arxiv.org/abs/2608.12880v1)
- [Vero](https://arxiv.org/abs/2608.13522v1)

## Working conclusion

The architectural lesson is simple: do not confuse artifacts with proof.

A serious agent runtime needs source-owned evidence packets that bind claims, tests, skills, tools, memory writes, delegated agents, policy verdicts, and final effects into one replayable control plane. That is the next layer above tracing and below governance dashboards.
