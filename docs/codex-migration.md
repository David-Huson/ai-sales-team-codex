# Codex adaptation

The upstream project is an instruction-based sales toolkit, not an Anthropic SDK application. No model API migration was necessary.

## Changes

- Added required skill names and descriptions to all 14 entrypoints.
- Moved detailed upstream workflows into linked reference files to keep discovery and initial loading small.
- Added relative repository discovery links under `.agents/skills`.
- Bundled shared scripts, templates, and role briefs under `skills/sales`, with root compatibility links.
- Replaced Claude-specific commands and tool assumptions with Codex prompts and available host capabilities.
- Made five-role analysis work sequentially when delegation is unavailable or disallowed.
- Added an installer that creates links, preflights conflicts, and removes only links belonging to this checkout.
- Added shared guidance for source provenance, unknown values, draft-only outreach, seller context, and separate output folders.
- Preserved the original MIT attribution and sales methodologies.

## Validation

- All 14 skill entrypoints passed the Skill Creator validator.
- Four automated tests passed for repository discovery, complete resource resolution, repeat installation, conflict handling, and conservative uninstall behavior.
- The analyzer and contact finder CLI entrypoints loaded successfully.
- The lead scorer produced structured JSON for an offline fixture.
- The PDF generator produced a valid 12,660-byte sample PDF from its built-in demo.
- An independent agent executed a source-only quick prospect request using the skill and correctly separated facts, hypotheses, and unknowns without using web access or writing outputs.
- Shell syntax and Git whitespace checks passed.

An authenticated Codex CLI executable is not installed in the preparation environment, so an actual CLI skill-selector session and live prospect research have not been tested. The Python utilities retain upstream scoring heuristics and extraction behavior; this port does not establish their predictive accuracy. No outreach was sent.

## Publication

The Codex adaptation is maintained at https://github.com/David-Huson/ai-sales-team-codex on `feat/codex-port`. The original upstream remains https://github.com/zubair-trabzada/ai-sales-team-claude. Publish adaptation changes to the Codex fork.

Discovery and invocation follow https://learn.chatgpt.com/docs/build-skills.
