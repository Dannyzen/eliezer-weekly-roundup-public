# Strategy Daily Analysis: 2026-11-20

## Scope

This scan covers sources first listed by arXiv on 20 November 2026. Signed, Valid, and Unauthorized was submitted on 18 November at 08:36 UTC. Tether was submitted on 19 November at 06:46 UTC. Public upstream protocol and supporting repositories were inspected read-only. No external source was cloned or executed.

## 1. Enforce policy over observed side effects, not command text

Tether runs each proposed agent action in an ephemeral sandbox, observes its system calls, maps them to conservative abstract actions, and applies stateful policy before committing effects. Its Lean 4 policy language can carry labels across multiple steps, so a secret read in one command can block a later network write even when intermediate files or scripts obscure the flow.

The evaluation covers two coding-agent benchmarks with 344 adversarial and 1,590 benign trajectories: 199 adversarial plus 218 benign on MonitoringBenchHonest, and 145 adversarial plus 1,372 benign on LinuxArena. On in-scope trajectories, one policy blocked all tested attacks with reported benign false-positive rates of 2.3% and 5.0%.

Why it matters: command allowlists inspect the declared operation. Agent-written scripts, subprocesses, and multi-step staging can produce effects that the command surface does not reveal. A trusted runtime must observe the effect path, persist security labels outside model context, and deny the state transition before host mutation.

Fits into the stack: sandboxing, information-flow control, runtime policy verification, and execution authority.

Practical methods worth exploring now:
- execute proposed actions in disposable sandboxes;
- translate system calls into a small conservative action algebra;
- persist source and destination labels across steps;
- use deny-overrides composition and state preservation on refusal;
- prove policy invariants separately from the semantic inference engine;
- block untraced external state at the boundary.

Artifact status: paper only in this scan. The paper links supporting benchmark and analysis repositories, but no public Tether implementation URL was verified.

Evidence limit: Tether cannot stop purely semantic attacks that violate no modeled system-level invariant. Untraced daemons, databases, and other external state require coarse boundary blocking. Conservative syscall inference can create false positives.

Implementability score: 0.62

Core source: [Tether v1](https://arxiv.org/abs/2611.25599v1)

## 2. Check the closure of delegated authority before signing

Signed, Valid, and Unauthorized defines authority closure as every transfer sequence a holder can enable with a signed wallet object. The wallet should sign only when that full set is a subset of the buyer's mandate for payee, asset, chain, amount, time, and retry or period behavior.

The paper's executable oracle covers 13 signed-object families and 25 correct or faulty translation classes. Across 2,130 generated objects and 62,979 execution programs, 265 objects with an observed violation still passed both field-and-expiry matching and an address allowlist. Under the test model, the Closure checker rejected all 1,680 objects with an observed violation and accepted the remaining 450. The reported median decision time was at most 12 microseconds per family.

Why it matters: a signature proves who authorized an object. It does not prove that every effect enabled by that object stays inside the human mandate. The same gap appears in agent tools, OAuth grants, database sessions, and delegated workflows: visible fields and one successful simulation are weaker than checking the closure of the capability.

Fits into the stack: authority manifests, agent commerce, wallet signing, capability analysis, and last-boundary authorization.

Tools and methods worth exploring now:
- [Coinbase x402](https://github.com/coinbase/x402), inspected read-only;
- [Google AP2](https://github.com/google-agentic-commerce/AP2), inspected read-only;
- [Uniswap Permit2](https://github.com/Uniswap/permit2);
- [MetaMask delegation framework](https://github.com/MetaMask/delegation-framework);
- mandate schemas that include sequence, retry, period, start-time, and downstream-contract effects;
- model checking or bounded adversary programs before signing.

Artifact status: the paper's primary page links the upstream protocols and contracts. Its Closure harness is described in detail, but no public implementation repository for Closure was verified in this scan.

Evidence limit: the result is bounded by the 13 object families, modeled contracts, generated corpus, and adversary library. It does not establish closure for arbitrary contracts or future protocol upgrades.

Implementability score: 0.68

Core source: [Signed, Valid, and Unauthorized v1](https://arxiv.org/abs/2611.24989v1)

## Strategic conclusion

Authority should be evaluated over reachable effects. Observe system behavior before committing host changes, and compute the full capability envelope before signing delegated objects.
