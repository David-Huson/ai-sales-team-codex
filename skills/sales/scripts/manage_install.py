#!/usr/bin/env python3
"""Link the complete sales skill set into a Codex discovery directory."""
import argparse
from pathlib import Path
import sys

SOURCE = Path(__file__).resolve().parents[2]
NAMES = (
    'sales', 'sales-prospect', 'sales-research', 'sales-qualify',
    'sales-contacts', 'sales-outreach', 'sales-followup', 'sales-prep',
    'sales-proposal', 'sales-objections', 'sales-icp', 'sales-competitors',
    'sales-report', 'sales-report-pdf',
)


def manage(action, destination):
    destination = Path(destination).expanduser().absolute()
    pairs = [(SOURCE / name, destination / name) for name in NAMES]
    if action == 'install':
        # Preflight the whole set before modifying the destination.
        for source, target in pairs:
            if not (source / 'SKILL.md').is_file():
                raise ValueError(f'Incomplete source checkout: {source}')
            if target.is_symlink() and target.resolve() == source.resolve():
                continue
            if target.exists() or target.is_symlink():
                raise ValueError(f'Refusing to replace existing skill: {target}')
        destination.mkdir(parents=True, exist_ok=True)
        created = []
        try:
            for source, target in pairs:
                if not target.is_symlink():
                    target.symlink_to(source, target_is_directory=True)
                    created.append(target)
        except OSError:
            for target in reversed(created):
                target.unlink()
            raise
        return len(pairs)
    removed = 0
    for source, target in pairs:
        # Never delete a real directory or another checkout's installation.
        if target.is_symlink() and target.resolve() == source.resolve():
            target.unlink()
            removed += 1
    return removed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['install', 'uninstall'])
    parser.add_argument('--skills-dir', type=Path, default=Path.home()/'.agents/skills')
    args = parser.parse_args()
    try:
        count = manage(args.action, args.skills_dir)
    except (OSError, ValueError) as error:
        parser.exit(1, f'{error}\n')
    print(f'{args.action}: {count} sales skill links at {args.skills_dir}')


if __name__ == '__main__':
    main()
