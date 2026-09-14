# Strategy Daily Sovereignty Analysis: 2026-09-14

## Freshness and selection

Both selected papers were submitted September 10 and first listed in the Monday, September 14 arXiv batch. They extend, rather than repeat, the repository's existing skill-admission and context-to-execution work: one separates publish-time artifact scanning from action-time permission; the other separates predeployment evaluation from deployment evidence.

## Govern each executed action, not only the installed skill

### Finding

Scan the Skill, Govern the Action measures the gap between artifact verdicts and runtime permission. Across 66,192 public ClawHub skill versions, the authors found 705 skills from 135 publishers that every available scanner and registry judge rated clean while the documentation instructed an action many operators would prohibit. A hand audit of 100 reported 92 percent precision, with a 95 percent sampling interval of 84.8 to 96.5 percent.

The execution gap was larger. A live agent issued 144 commands while following 39 skills; only two appeared verbatim in the documentation, and 50, or 34.7 percent, carried a consequence class absent from every code block. In a second run over 53 cleared skills that documented a never-graduating action, the agent attempted one in 23 cases and the gate held or blocked all 23.

The proposed OATS control point resolves each concrete action with a deterministic rule before execution, emits a receipt, and tracks authority per resource and consequence class. The paper reports 67.6 ms median end-to-end latency through its CLI hook. Its 64-case semantics-preserving evasion benchmark exposes the weak point honestly: the reference resolver reaches 52 percent macro resolution across techniques and misses staged fetch-then-execute completely.

### Why it matters

Clean and permitted are different predicates. A registry can correctly decide that a skill is not malicious while an operator correctly refuses the action it induces on a particular machine. The scanned document is also only a partial bound on the command the agent eventually constructs.

### Strategy fit

This belongs in skill admission control, runtime governance, and context-to-execution integrity. Artifact scanning decides whether a package is eligible to load. A separate complete-mediation layer decides whether this principal may perform this exact consequence on this resource now.

### Practical path now

- Keep package verdicts and action decisions as separate records.
- Resolve every side-effecting tool call through a deterministic consequence classifier and operator policy.
- Track authority by principal, resource, action class, and evidence lane.
- Emit receipts for allow, hold, block, promotion, demotion, and revocation.
- Derive promotion thresholds from the operator's tolerated failure rate; never graduate irreversible classes on a clean streak.
- Add semantics-preserving rewrites and multi-step staged effects to the gate's regression corpus.

Implementability score: 0.84

Artifact status: `pheo-ai/open-agent-trust-system` is a populated Apache-2.0 repository with JSON Schemas, a dependency-free reference runtime, policy examples, contract tests, research scripts, and per-command records. It has no release. The study is a Pheo self-audit with one model on one day, one registry snapshot, small live samples, no instruction-detector recall estimate, and an action resolver that its own benchmark only partly covers. The repository README still carries an older 93-command count while the immutable v1 paper and bundled paper source report 144; the paper is the quantitative source of record. The artifact was inspected read-only and not executed.

Core sources:
- [Scan the Skill, Govern the Action](https://arxiv.org/abs/2609.12001v1)
- [OATS repository](https://github.com/pheo-ai/open-agent-trust-system)
- [ClawHub security signals dataset](https://huggingface.co/datasets/OpenClaw/clawhub-security-signals)

## Treat deployment counterexamples as evaluator revisions

### Finding

Reality Is the Final Verifier separates two gaps that predeployment tests cannot generally close. The requirement gap lies between stakeholder intent and the written requirements. The model gap lies between the real deployment world and the environment represented in testing. Reward hacking exploits omissions in either gap; hallucination widens them by inventing requirements or environment assumptions.

The proposed architecture keeps the normal implementation-verification loop, then adds an outer assurance-revision loop. Deployment counterexamples, stakeholder rejection, monitoring, and incidents must revise the requirements, environment model, evaluator, or safeguards. The paper frames the scarce resources directly: accountable human judgment is the bottleneck for requirement truth, while faithful and costly evaluation is the bottleneck for environment truth.

### Why it matters

A stronger verifier proves conformance only to the requirements and environment it was given. It cannot certify that the product is acceptable in an open, changing world. Treating a green benchmark as final authority freezes the exact assumptions that deployment will invalidate.

### Strategy fit

This belongs in context-to-execution integrity, runtime governance, and evidence provenance. Deployment evidence must be able to reopen an accepted artifact and name which requirement, model, evaluator, or safeguard became false.

### Practical path now

- Version stakeholder requirements separately from environment assumptions.
- Bind every evaluation to both versions and to the evaluator identity.
- Stage consequential deployments and capture counterexamples as first-class evidence.
- Classify each failure as requirement, environment-model, evaluator, implementation, or control failure.
- Turn accepted incidents into frozen regression fixtures and revised assurance claims.
- Keep authorized stakeholders in charge of what counts as acceptable behavior.

Implementability score: 0.58

Artifact status: this is a framework and research agenda, not an empirical benchmark or released implementation. Its two-loop architecture is usable now, but deployment-specific requirement elicitation, monitoring, staged exposure, and revision authority remain organization work.

Core source:
- [Reality Is the Final Verifier](https://arxiv.org/abs/2609.12039v1)

## Working conclusion

Sovereignty lives at two runtime boundaries. The first checks the exact action after a skill has been loaded. The second lets real deployment evidence reopen requirements and evaluators after a system has passed predeployment checks. Artifact trust and benchmark success are inputs, not authority.
