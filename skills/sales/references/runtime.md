# Codex runtime guidance

## Resources

Resolve this file's real path, including symlinks. `SALES_ROOT` means the absolute path to its parent skill directory, `skills/sales`. Before running shell examples, set the shell variable `SALES_ROOT` to that resolved absolute path and quote it. It is not the current working directory. This variable is a convention for examples, not a variable provided by Codex.

The shared skill contains `scripts/`, `templates/`, and `agents/`. Resolve sibling skills as `$SALES_ROOT/../sales-<command>/SKILL.md`. Paths in workflow documents starting `../sales-` are relative to the skill directory, not the references directory. Install all 14 skills together so these dependencies exist.

Read the corresponding template from `$SALES_ROOT/templates/` for outreach, proposals, meeting prep, or objections. Run helpers with Python 3 from the configured environment. If an optional dependency is missing, explain the exact missing dependency. Do not install packages globally without authorization.

## Invocation and tools

`$sales prospect <url>` and `$sales-prospect <url>` invoke the same workflow. Other `$sales <command>` requests route to the matching `sales-<command>` sibling; `quick` stays in the main workflow. These are prompts to Codex, not shell commands or custom slash commands. Natural-language requests also work.

Use web search, page retrieval, shell, and file tools actually available in the host. No Claude-specific tools or hard-coded agent types are required. If web access is absent, work from user-provided source material and identify what cannot be verified. Never fabricate search results or imply live verification took place.

For full prospect analysis, follow the five role briefs under `agents/`. Use parallel workers only when host tools and session instructions permit delegation. Otherwise perform the roles sequentially. Workers return findings; only the coordinator writes the combined report. Pass the seller's offer and ICP to every role. Reconcile outreach against the completed research before producing the final draft.

## Business context and evidence

Use the seller's supplied offer and ICP. If these are missing, ask for them when needed to judge fit; company research can still proceed. Do not silently substitute a SaaS offer or claim that general company attractiveness establishes fit.

Separate verified facts, estimates, hypotheses, and unknowns. Record URLs and retrieval dates for factual claims. A guessed email pattern is unverified and is not a confirmed contact route. Scores prioritize research and outreach; they are not calibrated probabilities of closing a deal. Missing analyses remain unavailable, with evidence coverage stated separately; do not fill gaps with a score of 50.

Outreach and proposals are drafts. Drafting does not authorize sending messages, connecting with prospects, or writing CRM records. Perform external actions only when the user has explicitly authorized those actions in the session. Do not invent customer results, shared connections, or personal experience for personalization.

## Outputs

Create a separate working folder per prospect and run, for example `outputs/acme/2026-09-12-01/`. The workflow's report filenames live in that folder. Reuse earlier analysis only when the company and date match the requested context; never mix unrelated prospects. Ask for or choose explicit input folders for pipeline reports.

Do not overwrite prior runs. Respect a host's required artifact-saving workflow. Keep customer outputs and contact data out of source control unless explicitly requested. Include source URLs and dates in reports and report any unavailable tool or analysis.
