#!/usr/bin/env python3
"""Validate HCPN partner progress Markdown files.

Usage:
    python scripts/validate_partner_files.py partners/foo.md partners/bar.md

If no file arguments are supplied, all partners/*.md files except README.md
are validated.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

VALID_TRACKS = {"Reseller", "Distributor", "Service Partner", "CSP"}
VALID_STATUSES = {"Not Started", "In Progress", "Completed", "Validated", "Blocked"}
VALID_READINESS = {"Foundation", "Developing", "Ready", "Advanced"}

REQUIRED_FIELDS = (
    "Partner ID",
    "Track",
    "Current Stage",
    "Overall Status",
    "Readiness Level",
)

REQUIRED_SECTIONS = (
    "Next Milestone",
    "Public Disclosure Check",
)

PLACEHOLDER_PATTERNS = (
    r"<partner-id>",
    r"<approved-public-name>",
    r"<next milestone>",
    r"YYYY-MM-DD",
)


def extract_table_value(text: str, field: str) -> str | None:
    pattern = rf"^\|\s*{re.escape(field)}\s*\|\s*(.*?)\s*\|\s*$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    return match.group(1).strip().strip("`") if match else None


def normalize_stage(value: str) -> str | None:
    match = re.match(r"^(M(?:[1-9]|1[0-2]))(?:\s*(?:—|-|:).*)?$", value.strip(), flags=re.IGNORECASE)
    return match.group(1).upper() if match else None


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []

    if not path.exists():
        return [f"File does not exist: {path}"]

    text = path.read_text(encoding="utf-8")

    if path.name.lower() == "readme.md":
        return errors

    values: dict[str, str] = {}
    for field in REQUIRED_FIELDS:
        value = extract_table_value(text, field)
        if not value:
            errors.append(f"Missing required Partner Profile field: {field}")
        else:
            values[field] = value

    partner_id = values.get("Partner ID")
    if partner_id:
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", partner_id):
            errors.append("Partner ID must use lowercase letters, numbers, and hyphens only")
        expected_filename = f"{partner_id}.md"
        if path.name != expected_filename and path.name != "partner-example.md":
            errors.append(
                f"Filename must match Partner ID: expected '{expected_filename}', got '{path.name}'"
            )

    track = values.get("Track")
    if track and track not in VALID_TRACKS:
        errors.append(f"Invalid Track '{track}'. Allowed: {', '.join(sorted(VALID_TRACKS))}")

    status = values.get("Overall Status")
    if status and status not in VALID_STATUSES:
        errors.append(
            f"Invalid Overall Status '{status}'. Allowed: {', '.join(sorted(VALID_STATUSES))}"
        )

    readiness = values.get("Readiness Level")
    if readiness and readiness not in VALID_READINESS:
        errors.append(
            f"Invalid Readiness Level '{readiness}'. Allowed: {', '.join(sorted(VALID_READINESS))}"
        )

    stage = values.get("Current Stage")
    if stage and normalize_stage(stage) is None:
        errors.append("Current Stage must start with M1 through M12")

    for section in REQUIRED_SECTIONS:
        if not re.search(rf"^##\s+{re.escape(section)}\s*$", text, flags=re.MULTILINE):
            errors.append(f"Missing required section: ## {section}")

    next_milestone = re.search(
        r"^##\s+Next Milestone\s*$([\s\S]*?)(?=^##\s+|\Z)",
        text,
        flags=re.MULTILINE,
    )
    if next_milestone:
        body = next_milestone.group(1).strip()
        if not body or body in {"None", "N/A"}:
            errors.append("Next Milestone section must contain a measurable next milestone")

    if path.name != "partner-example.md":
        for pattern in PLACEHOLDER_PATTERNS:
            if re.search(pattern, text, flags=re.IGNORECASE):
                errors.append(f"Unresolved placeholder found: {pattern}")

    return errors


def main() -> int:
    args = [Path(p) for p in sys.argv[1:]]
    files = args or [p for p in Path("partners").glob("*.md") if p.name.lower() != "readme.md"]

    if not files:
        print("No partner files to validate.")
        return 0

    total_errors = 0
    for path in files:
        if path.name.lower() == "readme.md":
            continue
        errors = validate_file(path)
        if errors:
            total_errors += len(errors)
            print(f"\n❌ {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"✅ {path}")

    if total_errors:
        print(f"\nValidation failed with {total_errors} error(s).")
        return 1

    print("\nAll partner files passed validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
