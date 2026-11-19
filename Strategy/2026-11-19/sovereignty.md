# Strategy Daily Analysis: 2026-11-19

## Scope

This scan covers sources first listed by arXiv on 19 November 2026 and submitted on 18 November 2026. Public artifacts were inspected read-only. No external source was cloned or executed.

## 1. Treat intent contracts as provenance, not authorization

Intent Contracts removes tools from the planning model. For each step the planner emits a goal, a verbatim quotation of the user's request, and scope fields. Code validates the structure and a smaller trusted model writes the actual tool call.

The design creates useful attribution. Every changed object was named in the producing contract's goal, and contracts completed a benign bundling task in 27 of 30 runs versus 16 of 30 for an intent-visible command reviewer. The central negative result matters more: contracts did not reduce unauthorized actions. After ambiguous environment terms were clarified, every state-changing condition still chose a wrong target in 40% to 49% of runs because the trusted executor could not inspect the environment needed to resolve the reference.

Why it matters: a declaration can bind an action to visible intent and still authorize the wrong effect. Provenance improves audit and repair. Authorization requires environment-grounded object identity, current state, policy, and a final effect check.

Fits into the stack: execution control, trusted dispatch, authority separation, and effect receipts.

Tools and patterns worth exploring now:
- [zwang-devv/intent-contracts](https://github.com/zwang-devv/intent-contracts), inspected read-only;
- planner without direct tools;
- checked quotations and typed scope fields;
- ordered contract and tool-call logs;
- model-free validation before dispatch;
- environment-grounded target resolution and last-boundary authorization as the required extension.

Artifact status: contents inspected read-only. The public repository contains the OpenCode plugin, per-run records, ordered event logs, tests, and a table-recomputation script. It excludes the external benchmark environment.

Evidence limit: the authorization comparison uses one planner and one trusted executor on three AmPermBench task families, and it studies benign overreach rather than adversarial planners.

Implementability score: 0.76

Core sources: [Intent Contracts v1](https://arxiv.org/abs/2611.24025v1), [implementation and run records](https://github.com/zwang-devv/intent-contracts)

## 2. Compile skill prose into enforceable control flow

SkillCFI applies control-flow integrity to procedural agent skills. An offline compiler turns skill prose into instructions and an executable contract. A deterministic host-side enforcer admits tool requests only when trusted boundary evidence proves the next transition and rejects unmediated execution paths.

Across eight self-written skills and 770 agent sessions, SkillCFI blocked all 240 tested violations before dispatch, while an allowlist admitted them. Showing the next legal steps after refusal raised recovery from 21% to 65%. Runtime checking consumed about 2% of task time, and compact commands reduced session slowdown from 1.32 times to 1.08 times. The harsh result is useful: none of 53 public skills was accepted as written, although diagnostics guided seven into enforceable contracts.

Why it matters: permission allowlists govern available operations, not required order, preconditions, evidence, or recovery. A skill is enforceable only where mandatory obligations cross a trusted boundary that the host can observe.

Fits into the stack: skill admission, deterministic runtime governance, tool mediation, and executable procedure contracts.

Practical methods worth exploring now:
- compile source-linked obligations into typed state transitions;
- reject mandatory checks that produce no observable evidence;
- keep enforcement state outside model context;
- block shell expansions and inline scripts that bypass mediation;
- return legal next steps with every refusal;
- test source mutations and regime migration, not only forbidden tools.

Artifact status: claimed future release only. The paper says code and artifacts will be released upon acceptance, so the implementation is not available for read-only qualification today.

Evidence limit: the live evaluation uses one agent and eight self-written skills. The public-skill result proves a large contract gap, not that all 53 skills are unsafe in every deployment.

Implementability score: 0.52

Core source: [SkillCFI v1](https://arxiv.org/abs/2611.24185v1)

## Strategic conclusion

Visible contracts and permission lists are incomplete authority controls. The host needs typed targets, observable obligations, deterministic transition checks, and a final effect decision grounded in live state.
