# Strategy Daily Analysis: 2026-11-18

Today's strategy signal is that every capability change needs a versioned acceptance test. Provenance and runtime policy control what may run; evals prove whether an admitted configuration still behaves as intended.

## 1. Make capability changes pass owned evals

GitHub Copilot Evals now lets users create repeatable tests for project skills, custom agents, and MCP tools, approve each run, inspect failures, and compare results before and after configuration changes.

Why it matters: an approved source is not proof of safe or useful behavior. Skills, tools, models, prompts, and harnesses interact. A configuration that passed last week can regress after any one of those components changes.

Implementable now:
- assign an owner and user journey to every high-impact capability;
- bind each eval to exact skill, agent, MCP, model, harness, policy, and fixture versions;
- separate outcome checks from trajectory and authority checks;
- require explicit approval for side-effecting test runs;
- compare candidate and incumbent configurations on the same tasks;
- retain inputs, checks, traces, decisions, and effects as one acceptance receipt;
- fail closed when a required eval is absent, stale, or cannot reproduce its fixture.

Evidence and caveat: the product is in public preview for Copilot Individual, Business, and Enterprise. GitHub has not published independent reliability measurements, cross-model stability, or guarantees that every customization path is covered. It should be treated as an immediately usable regression surface, not a complete governance system.

Artifact status: official GitHub changelog inspected. No plugin, extension, or external source was installed or executed.

Implementability score: 0.92

Core source: [GitHub Copilot Evals public preview](https://github.blog/changelog/2026-11-17-github-copilot-evals-is-now-in-public-preview/)

## Working conclusion

Treat evals as the behavioral half of capability admission. Source policy and runtime controls decide what may run; owned, versioned evals decide whether a specific configuration earns promotion.
