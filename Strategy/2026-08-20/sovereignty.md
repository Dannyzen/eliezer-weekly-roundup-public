# Strategy Daily Analysis - 2026-08-20

## Scope

The Thursday arXiv listing was live and headed 2026-08-20. The selected papers were submitted on 2026-08-18 and first listed on 2026-08-20. Paper claims were checked against immutable v1 abstract pages and downloaded PDFs. No external source repository was cloned or executed. NotebookLM remained disabled.

## Remediation must invalidate prior gate decisions

One Gate Is Not Enough identifies a control-plane bug that appears only after multiple useful gates are composed. An authority gate may allow an action. A budget gate may then downroute it. An evidence gate may substitute a source. Those remediations change the action or evidence that earlier gates evaluated, so the earlier allow is stale.

The paper formalizes remediation-induced control coupling and proposes remediate-and-regate: when one control transforms an action, evidence, or derived context, every affected control must evaluate the transformed object again before execution. Its implemented evidence-substitution and resource-downroute operators do not commute. Order is therefore policy, not an implementation detail.

The prototype's 30-seed sweep found a mean 207.5 divergent decisions between single-pass and re-gated composition. It also shows a second-order risk: currently admissible observations can poison future governance state when defects are promoted into an evidence buffer. Quarantine and median-based mitigations reduce but do not eliminate that exposure.

Why it matters: adding more gates can make a system less sound when their remediations interact. A sequence of individually correct decisions is not a correct composed decision.

Practical paths:
- canonicalize the proposed action and evidence bundle before the first gate;
- make each gate declare which fields and state scopes it reads and may transform;
- invalidate dependent verdicts after any remediation;
- use a fixed, versioned remediation order and detect cycles;
- revalidate policy state at commit time, not only after transformation;
- store original action, every transformation, invalidated verdicts, re-gated verdicts, and final effect in one receipt.

Artifact status: the PDF describes an Apache-2.0 deterministic suite artifact, but no exact public implementation repository resolved from the primary source during this scan.

Caveat: this is a single-author draft and mechanism demonstration. The workflows are synthetic, the implemented remediators are narrow, and general termination, confluence, and concurrent multi-agent composition remain open.

Implementability score: 0.64

Core source:
- https://arxiv.org/abs/2608.18360v1

## Learned least privilege is a routing prior, not authority

Task-Conditioned Least-Privilege Learning tests whether a 4B model can learn to choose the minimum authority needed for terminal and MCP tasks. The selected Qwen3.5-4B policy was trained over 1,500 tasks and evaluated over 2,896 held-out episodes.

The result is large: task success rose from 68.92% to 99.27%, safe success rose from 64.36% to 98.48%, and excess-authority success fell from 4.56% to 0.79%. This shows that authority choice is learnable behavior, not only a prompt instruction.

The design implication is narrower than the headline. A learned policy can reduce noisy approval prompts and choose a lower-risk tool variant, but its residual 0.79% excess-authority rate is unacceptable as the final enforcement boundary. The model should propose the authority envelope. A deterministic broker should intersect that proposal with user grant, task contract, target identity, policy state, and budget.

Practical paths:
- include privilege level, side-effect class, target scope, and data scope in tool schemas;
- train or rank on safe task completion, not completion alone;
- let the model choose among pre-declared authority profiles;
- enforce a deterministic ceiling outside the model;
- log proposed privilege, effective privilege, denied excess, task result, and effect receipt;
- keep adversarial and ambiguous tasks in the held-out gate.

Artifact status: the paper names Qwen3.5-4B and standard training tools, but no exact public code repository, tuned checkpoint, or evaluation dataset URL resolved from the primary source during this scan.

Caveat: this is a two-author preprint, the reported gains are tied to a constructed task curriculum, and faithful reproduction requires post-training infrastructure.

Implementability score: 0.46

Core source:
- https://arxiv.org/abs/2608.18351v1

## Working conclusion

Learned least privilege can improve defaults. It cannot own authority. The control plane still needs deterministic ceilings, dependency-aware re-gating after remediation, and commit-time validation.
