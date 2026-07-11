#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


class ValidationError(Exception):
    pass


def parse_skill_md(text: str) -> tuple[str, str]:
    name_match = re.search(r"^Name:\s*(.+)$", text, re.M)
    desc_match = re.search(r"^Description:\s*(.+)$", text, re.M)
    if not name_match:
        raise ValidationError("missing Name header")
    if not desc_match:
        raise ValidationError("missing Description header")
    return name_match.group(1).strip(), desc_match.group(1).strip()


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "Skill.md"
    if not skill_md.exists():
        errors.append("missing Skill.md")
        return errors

    name, description = parse_skill_md(skill_md.read_text(encoding="utf-8"))
    expected_name = skill_dir.name
    if name != expected_name:
        errors.append(f"name mismatch: {name!r} != {expected_name!r}")
    if not description:
        errors.append("description is empty")
    return errors


def main() -> int:
    if not SKILLS.exists():
        print("skills/ directory is missing", file=sys.stderr)
        return 1

    failures: list[str] = []
    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        errors = validate_skill(skill_dir)
        if errors:
            failures.append(f"{skill_dir.name}: {', '.join(errors)}")

    if failures:
        print("Skill validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Validated {sum(1 for p in SKILLS.iterdir() if p.is_dir())} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
