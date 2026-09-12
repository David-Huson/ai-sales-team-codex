# AI sales team for Codex

This repository provides 14 sales skills, five analysis role briefs, six templates, and Python helpers. Codex discovers the checked-in links in `.agents/skills/`; canonical content is in `skills/`.

For a sales task, read the matching `SKILL.md`, then its linked runtime guidance and workflow. For a repository maintenance task, inspect only the relevant implementation. Do not start prospecting merely because this repository is open.

Shared scripts, templates, and role briefs are in `skills/sales/`. The root `scripts`, `templates`, and `agents` paths are compatibility symlinks. Keep all links relative inside the repository. Never add Claude-specific runtime requirements.

Validate packaging and installer behavior with `python3 -m unittest discover -s tests -v`. Use Python 3.10 or newer. Optional sales utility dependencies are in `requirements.txt`. Do not commit real prospect outputs or credentials. Preserve the upstream MIT license and attribution.
