# AI sales team for Codex

A Codex adaptation of [Zubair Trabzada's AI Sales Team for Claude Code](https://github.com/zubair-trabzada/ai-sales-team-claude), preserving the MIT license, 14 sales workflows, five analysis roles, six templates, and four sales utilities.

Research companies, qualify leads with BANT and MEDDIC, identify decision makers, draft outreach, prepare meetings and proposals, and generate pipeline reports.

## Use in this repository

Open this checkout in Codex, or select it as a Codex cloud environment repository. The committed `.agents/skills/` links expose all 14 skills without an installer. Start with:

```text
$sales icp We help multi-location specialty practices improve operational reporting.
$sales prospect https://example.com
$sales-outreach Draft messages using the research in outputs/example/.
```

Replace the example company and offer with your own. Natural-language requests also work. These prompts belong in Codex, not a terminal. The old `/sales` slash command is not registered in Codex.

## Use in other repositories

Keep this checkout in a stable location, then run:

```bash
bash install.sh
```

This links the full skill set into `~/.agents/skills`. It leaves existing unrelated skills alone and refuses conflicting names. Re-running it is safe. Remove only this checkout's links with:

```bash
bash uninstall.sh
```

To install into a particular project's discovery folder:

```bash
bash install.sh --skills-dir /absolute/path/to/project/.agents/skills
```

Keep the source checkout: the installed skills link to it. Uninstall before moving or deleting it. For native Windows, run the Python installer with symlink privileges, or use WSL. The repo checkout must preserve Git symlinks.

## Requirements

The instructions run inside an authenticated Codex session and do not use an Anthropic API key or an additional model API. Live prospect research needs web search or page retrieval enabled in that session. Without it, provide source documents and expect unverified fields to remain unknown.

Python 3.10+ is needed for installation and the helper scripts. Install optional utility dependencies in a virtual environment:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
```

The lead scorer uses the Python standard library. The PDF generator needs ReportLab; web extraction uses the packages listed in `requirements.txt`. The installer does not install packages or change Codex configuration.

## Skills

| Prompt | Result |
| --- | --- |
| `$sales prospect <url>` or `$sales-prospect <url>` | Full scored prospect analysis |
| `$sales quick <url>` | Short prospect snapshot |
| `$sales-research <url>` | Company research |
| `$sales-qualify <url>` | BANT and MEDDIC qualification |
| `$sales-contacts <url>` | Decision makers and contact routes |
| `$sales-outreach <prospect>` | Personalized first-contact drafts |
| `$sales-followup <prospect>` | Follow-up drafts |
| `$sales-prep <url>` | Meeting preparation |
| `$sales-proposal <client>` | Proposal draft |
| `$sales-objections <topic>` | Objection playbook |
| `$sales-icp <description>` | Ideal customer profile |
| `$sales-competitors <url>` | Competitive intelligence |
| `$sales-report` | Markdown pipeline report |
| `$sales-report-pdf` | PDF pipeline report |

All named skills also route through `$sales <command>`.

## Execution and outputs

Full prospect analysis covers company fit, contact access, opportunity, competition, and outreach readiness. Codex uses parallel workers when available and permitted, or executes the same roles sequentially. The role briefs are reference documents, not registered Codex agent types. The coordinator combines research and revises the outreach after the findings are available.

Provide your offer and ICP before requesting fit scores. Scores are prioritization heuristics, not measured win probabilities. Research must distinguish verified facts from hypotheses; guessed emails remain unverified. Outreach generation prepares drafts. Sending messages or updating a CRM requires explicit user authorization.

Keep each prospect and run in its own folder under `outputs/`. Pipeline reports should use explicitly selected source folders. Output folders and temporary report data are ignored by Git.

## Development

```bash
python3 -m unittest discover -s tests -v
python3 scripts/lead_scorer.py --help
```

See [the migration notes](docs/codex-migration.md) for compatibility decisions and validation limits. The discovery paths and invocation syntax follow [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Attribution

Original work copyright 2026 Zubair Trabzada. Distributed under the [MIT license](LICENSE). This adaptation is not an official OpenAI or Anthropic product.
