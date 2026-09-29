# Strategy Daily Sovereignty - 2026-09-26

## Scope note

No new arXiv listing exists for Saturday, 26 September 2026. This note covers leftover Friday papers plus official GitHub and GitGuardian releases that were still live on Saturday. External repositories were inspected read-only. No external source was cloned, installed, built, imported, or executed.

## Bind approval to the transitive effect closure

Loopjacking showed that an approved representation can diverge from the operation later released. Approval laundering is the next failure: the durable record names a truthful entry invocation, while the developer tool executes the workflow that invocation activates. Package installation can run lifecycle hooks and write files. An MCP call can exercise network authority. The human approved the named command; the host executed the closure.

The paper formalizes closure-bound approval over six effect classes and derives an information limit: identical policy-visible fields can require different effect-specific decisions, so no record-only policy can guarantee both. Across 111 fixed approval-object and trace pairs, residual records fall from 40 under explicit fields to 17 with command semantics and 13 with decision-time metadata. Across 11 fixed-SHA executions, the retrospective ladder reaches zero metadata residuals, and two exact mappings recur across three product frontends. For prospective recovery, effect-bound records commit frozen, source-backed predictions before authorization. On 17 prespecified holdout workflows, those predictions reach 0.926 macro recall and 0.941 macro precision; binding them cuts residual effects from 10 to 3. A Claude Code PreToolUse integration carries the frozen record through the permission path without automatic approval.

GitHub's proof-of-presence preview is the product-side complement. For Entra ID managed-user enterprises, high-impact actions such as creating a token, editing webhooks, changing organization security settings, or viewing recovery codes can require a fresh IdP challenge. The changelog states the control is meant to block hijacked sessions and "agents going an extra step without your knowledge." After a successful challenge, the sudo-mode window lasts two hours. Pull-request merge coverage is not yet shipping.

Why it matters: approving a command name is not approving npm lifecycle hooks, generated files, or MCP network side channels. Approving a GitHub session is not approving a later token mint or webhook edit by an agent holding that session.

Strategic fit: compile one effect-bound record before authorization. The record must name the entry invocation and a source-backed prediction of the workflow's transitive boundary. Compare that frozen prediction at use time. For high-impact host actions, require a live human presence challenge that an agent session cannot satisfy.

Tools and methodologies worth exploring now:
- PreToolUse or equivalent hooks that attach a frozen effect-bound record;
- source-backed predictions for install, build, MCP, and shell closures;
- residual-effect scoring against post-execution evidence;
- GitHub proof of presence for token, webhook, and recovery-code paths;
- fail closed when the predicted closure cannot be bound.

Implementability score: 0.78

The Claude Code hook path and GitHub IdP challenge are product-ready. Full closure prediction is still research: no paper-owned public repository resolved, the 17-workflow holdout is small, and proof of presence is an Entra ID EMU public preview with a two-hour sudo window.

Core sources:
- [Agent Approval Laundering](https://arxiv.org/abs/2609.28586v1)
- [Require proof of presence for high-impact actions](https://github.blog/changelog/2026-09-24-require-proof-of-presence-for-high-impact-actions)

## Keep specification sign-off outside the acting model

Agents now generate, decide, execute, and declare completion inside one loop. Specifications remain context for the same model. On SkillsBench, the authors extract 509 source-grounded task directions from agent-visible prompts, workspace information, and injected skills. Across seven models, only 79.6 to 86.4 percent of those directions are satisfied, while completion-claim rates exceed official evaluator pass rates by 28.7 to 37.9 percentage points.

SpecHarness compiles visible specifications into source-linked obligations and governs execution through versioned obligation state. Agents may plan, act, and request completion. Only admissible evidence from qualified providers may establish specification-governed state. Verifiable requirements are mediated or validated at runtime; ambiguous requirements stay advisory. On the reported guideline and artifact tasks, full SpecHarness reaches 85.1 percent pass, versus 78.2 without effect validation and 81.6 without commitment. Removing blocking qualification collapses the state-authority gap control.

Why it matters: Friday's OverclaimBench result was about unread files. This paper shows the same custody failure at the specification boundary. Understanding a requirement is not satisfying it. Claiming completion is not establishing the required state.

Strategic fit: treat SKILL.md, schemas, and acceptance checks as an authority plane. The model proposes. A deterministic obligation store records which requirements are open, satisfied, blocked, or advisory. Finalization is a state transition in that store, not a sentence in the agent transcript.

Tools and methodologies worth exploring now:
- compile visible specs into source-linked obligations before the first tool call;
- keep versioned obligation state outside the model context;
- allow completion only after qualified evidence lands;
- keep subjective requirements advisory rather than fake-verified;
- score understanding-execution gaps and state-authority gaps separately.

Implementability score: 0.72

The authority split is implementable with ordinary checkers and an obligation ledger. No public SpecHarness repository resolved from the paper surfaces, and SkillsBench extraction is author-built.

Core source: [Who Holds the Pen? Let Specifications, Not Agents, Sign Off](https://arxiv.org/abs/2609.29921v1)

## Inventory endpoint credentials that repository scanners never see

GitGuardian's 25 September 2026 post maps the credential trail that Cursor, Claude Code, and GitHub Copilot leave on developer machines. Project MCP files travel with the repository. User-level MCP files, session logs, shell history, plaintext token fallbacks, and temp files often never enter git. The State of Secrets Sprawl 2026 analysis found 24,008 unique secrets in public MCP configuration files, 2,117 of them valid, and a 3.2 percent leak rate in Claude Code-assisted public commits against a 1.5 percent baseline.

The documented September 2026 paths are specific enough to operationalize: Cursor `.cursor/mcp.json` and `~/.cursor/mcp.json`; Claude Code `.mcp.json`, `~/.claude.json`, and relocatable `CLAUDE_CONFIG_DIR`; Copilot CLI `~/.copilot/mcp-config.json`, plaintext `config.json` fallback, and relocatable `COPILOT_HOME`. Safer OAuth and variable-reference patterns exist, but they are not enforced. `ggshield` v1.55.0 is current as of 24 September 2026, and GitGuardian documents prompt, pre-tool, and post-tool hooks for Cursor, Claude Code, Codex, Copilot CLI, VS Code, and Mistral Vibe.

Why it matters: repository, pre-commit, and CI secret scanning can work exactly as designed and still miss the agent's home directory. Vaults cannot govern a copy written to a log. An agent with the user's credentials will use whatever it can read.

Strategic fit: treat developer endpoints as part of the agent gateway. Inventory which agents and MCP servers exist on each machine. Scan local config, history, and caches. Block secrets at prompt and pre-tool boundaries. Keep production credentials physically unreachable from coding-agent workspaces.

Tools and methodologies worth exploring now:
- `ggshield machine setup --agent cursor --agent claude-code`;
- fleet inventory of MCP servers and relocatable config directories;
- prompt and pre-tool secret blocking, with post-tool notify-only;
- ban inline tokens in committed `.mcp.json` and `.cursor/mcp.json`;
- honeytokens on developer machines as a last-line detector.

Implementability score: 0.88

The paths, hooks, and CLI are documented and the ggshield repository is public MIT. The sprawl counts are vendor research, the 3.2 percent figure is not proof of causation, and Developer Endpoint Protection is a paid fleet product rather than a drop-in local default.

Core sources:
- [AI Coding Agents Are Leaking Credentials on Endpoints](https://blog.gitguardian.com/ai-coding-agents-credential-security/)
- [Secret scanning for AI coding tools](https://docs.gitguardian.com/ggshield-docs/integrations/ai-coding-tools/secret-scanning-for-ai-coding-tools)

## Working conclusion

Saturday's leftover research tightens Friday's custody thesis at three boundaries the weekly synthesis left open: the transitive workflow behind an approved invocation, the specification store that must sign off completion, and the endpoint credential trail that never enters git.
