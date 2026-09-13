#!/usr/bin/env python3
"""Validate HCPN Pull Request body structure and required confirmations."""

from __future__ import annotations

import os
import re
import sys

body = os.environ.get("PR_BODY", "")
changed_partner_files = os.environ.get("CHANGED_PARTNER_FILES", "").strip()

errors: list[str] = []

if not body.strip():
    errors.append("Pull Request body is empty. Use the repository PR template.")

required_sections = (
    "Change Type",
    "Partner / Program Context",
    "Summary of Changes",
    "Files Changed",
    "Governance Checklist",
)

for section in required_sections:
    if not re.search(rf"^##\s+{re.escape(section)}\s*$", body, flags=re.MULTILINE):
        errors.append(f"Missing PR section: ## {section}")

# Reject obvious untouched placeholders from the template.
placeholder_checks = {
    "<partner-id or N/A>": "Partner ID",
    "<review notes>": "Reviewer notes",
    "<issue-number>": "Related Issue",
}

# Partner-specific PRs require completed partner context and next milestone.
if changed_partner_files:
    partner_required = {
        "Partner ID": r"^\|\s*Partner ID\s*\|\s*(.*?)\s*\|\s*$",
        "Partner Track": r"^\|\s*Partner Track\s*\|\s*(.*?)\s*\|\s*$",
        "Program Stage": r"^\|\s*Program Stage\s*\|\s*(.*?)\s*\|\s*$",
        "Current Status": r"^\|\s*Current Status\s*\|\s*(.*?)\s*\|\s*$",
        "Readiness Level": r"^\|\s*Readiness Level\s*\|\s*(.*?)\s*\|\s*$",
    }

    for label, pattern in partner_required.items():
        match = re.search(pattern, body, flags=re.MULTILINE)
        if not match:
            errors.append(f"Missing PR partner context field: {label}")
            continue
        value = match.group(1).strip().strip("`")
        if not value or "<" in value or value == "N/A":
            errors.append(f"Partner PR must provide a concrete value for {label}")

    nm = re.search(
        r"^###\s+Next Milestone\s*$([\s\S]*?)(?=^---$|^##\s+|\Z)",
        body,
        flags=re.MULTILINE,
    )
    if not nm or not nm.group(1).strip() or "<next measurable milestone>" in nm.group(1):
        errors.append("Partner PR must define a concrete Next Milestone")

    required_confirmations = (
        "I changed only files relevant to this update.",
        "Partner status matches the defined repository status values.",
        "Readiness terminology follows `framework/partner-readiness.md`.",
        "Evidence is appropriate for public disclosure.",
        "No customer-confidential information is included.",
        "No Huawei-confidential or proprietary restricted information is included.",
        "No credentials, access keys, passwords, exam vouchers, or secrets are included.",
        "The partner page includes a clear next milestone.",
    )

    for confirmation in required_confirmations:
        pattern = rf"^- \[x\]\s+{re.escape(confirmation)}\s*$"
        if not re.search(pattern, body, flags=re.MULTILINE | re.IGNORECASE):
            errors.append(f"Governance confirmation not checked: {confirmation}")

if errors:
    print("❌ Pull Request policy validation failed:")
    for error in errors:
        print(f"  - {error}")
    sys.exit(1)

print("✅ Pull Request body passed policy validation.")
