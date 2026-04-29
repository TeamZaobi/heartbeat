#!/usr/bin/env python3
"""Link a native skill directory into common Agent host discovery paths."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Iterable


USER_TARGETS = {
    "claude": Path.home() / ".claude" / "skills",
    "codex": Path.home() / ".agents" / "skills",
    "antigravity": Path.home() / ".gemini" / "antigravity" / "skills",
}


def project_targets(project_root: Path) -> dict[str, Path]:
    return {
        "claude": project_root / ".claude" / "skills",
        "codex": project_root / ".agents" / "skills",
        "antigravity": project_root / ".agents" / "skills",
    }


def parse_targets(raw: str | None, project_root: Path | None) -> list[str]:
    defaults = ["claude", "codex"] if project_root else ["claude", "codex", "antigravity"]
    if raw is None:
        return defaults
    targets = [item.strip().lower() for item in raw.split(",") if item.strip()]
    valid_names = set(defaults if project_root else USER_TARGETS)
    invalid = [item for item in targets if item not in valid_names]
    if invalid:
        raise SystemExit(f"Unknown target(s): {', '.join(invalid)}")
    return targets


def resolve_skill(path: str) -> Path:
    skill = Path(path).expanduser().resolve()
    if not skill.is_dir():
        raise SystemExit(f"Not a directory: {skill}")
    if not (skill / "SKILL.md").is_file():
        raise SystemExit(f"No SKILL.md found in: {skill}")
    return skill


def target_map(project_root: str | None) -> tuple[dict[str, Path], Path | None]:
    if project_root is None:
        return USER_TARGETS, None
    root = Path(project_root).expanduser().resolve()
    return project_targets(root), root


def rel_link_value(link_path: Path, source: Path) -> str:
    return os.path.relpath(source, link_path.parent)


def is_native(skill: Path, target_dir: Path) -> bool:
    return skill.parent.resolve() == target_dir.resolve()


def print_status(skill: Path, targets: Iterable[str], targets_by_name: dict[str, Path]) -> int:
    warnings = 0
    print(f"Skill: {skill.name}")
    print(f"Source: {skill}")
    for name in targets:
        target_dir = targets_by_name[name]
        link_path = target_dir / skill.name
        if is_native(skill, target_dir):
            print(f"OK    {name}: native source at {target_dir}")
            continue
        if link_path.is_symlink():
            link_value = os.readlink(link_path)
            resolved = (link_path.parent / link_value).resolve()
            if resolved == skill:
                print(f"OK    {name}: {link_path} -> {link_value}")
            else:
                print(f"WARN  {name}: {link_path} -> {link_value}; expected {skill}")
                warnings += 1
        elif link_path.exists():
            print(f"WARN  {name}: {link_path} exists but is not a symlink")
            warnings += 1
        else:
            print(f"MISS  {name}: {link_path}")
            warnings += 1
    return warnings


def link(skill: Path, targets: Iterable[str], targets_by_name: dict[str, Path], force: bool) -> int:
    warnings = 0
    for name in targets:
        target_dir = targets_by_name[name]
        link_path = target_dir / skill.name
        if is_native(skill, target_dir):
            print(f"OK    {name}: native source at {target_dir}")
            continue
        target_dir.mkdir(parents=True, exist_ok=True)
        if link_path.is_symlink():
            current = (link_path.parent / os.readlink(link_path)).resolve()
            if current == skill:
                print(f"OK    {name}: already linked")
                continue
            if not force:
                print(f"WARN  {name}: existing symlink points to {current}; use --force to replace")
                warnings += 1
                continue
            link_path.unlink()
        elif link_path.exists():
            print(f"WARN  {name}: {link_path} exists and is not a symlink")
            warnings += 1
            continue
        link_path.symlink_to(rel_link_value(link_path, skill))
        print(f"LINK  {name}: {link_path} -> {os.readlink(link_path)}")
    return warnings


def unlink(skill: Path, targets: Iterable[str], targets_by_name: dict[str, Path]) -> int:
    warnings = 0
    for name in targets:
        target_dir = targets_by_name[name]
        link_path = target_dir / skill.name
        if is_native(skill, target_dir):
            print(f"OK    {name}: native source; nothing to unlink")
            continue
        if link_path.is_symlink():
            current = (link_path.parent / os.readlink(link_path)).resolve()
            if current != skill:
                print(f"WARN  {name}: symlink points to {current}; not removing")
                warnings += 1
                continue
            link_path.unlink()
            print(f"UNLINK {name}: {link_path}")
        else:
            print(f"MISS  {name}: no managed symlink")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_path", help="Path to the native skill directory")
    parser.add_argument("--targets", help="Comma-separated target list: claude,codex,antigravity")
    parser.add_argument("--project-root", help="Project root for project-local discovery paths")
    parser.add_argument("--status", action="store_true", help="Show status without changing links")
    parser.add_argument("--unlink", action="store_true", help="Remove managed symlinks")
    parser.add_argument("--force", action="store_true", help="Replace mismatched symlinks")
    args = parser.parse_args()

    skill = resolve_skill(args.skill_path)
    targets_by_name, project_root = target_map(args.project_root)
    targets = parse_targets(args.targets, project_root)

    if args.status:
        return 1 if print_status(skill, targets, targets_by_name) else 0
    if args.unlink:
        return 1 if unlink(skill, targets, targets_by_name) else 0
    return 1 if link(skill, targets, targets_by_name, args.force) else 0


if __name__ == "__main__":
    raise SystemExit(main())
