# HCPN Indonesia — Partner Progress Directory

This directory is the public progress layer for participating HCPN Indonesia partners.

Each partner should maintain one progress page using the naming convention:

```text
partners/<partner-id>.md
```

Examples:

```text
partners/partner-example.md
partners/acme-cloud.md
partners/partner-001.md
```

> Use only a partner-approved public name or alias. Do not publish confidential customer, commercial, personal, certification-ID, credential, or Huawei-internal information.

---

## Purpose

The partner page provides a simple public view of:

- partner track;
- current month / stage;
- overall status;
- readiness level;
- completed milestones;
- public-safe evidence;
- blockers;
- next milestone;
- last update date.

The intent is to make the enablement journey transparent and measurable without exposing sensitive business information.

---

## Supported Partner Tracks

| Track | 6-Month Outcome |
|---|---|
| [Reseller](../tracks/reseller.md) | Sales Ready |
| [Distributor](../tracks/distributor.md) | Channel Ready |
| [Service Partner](../tracks/service-partner.md) | Technical Delivery Ready |
| [CSP](../tracks/csp.md) | Solution Ready |

---

## Standard Status Values

Use only the following status values for consistency:

- `Not Started`
- `In Progress`
- `Completed`
- `Validated`
- `Blocked`

Suggested visual markers:

| Status | Marker |
|---|---|
| Not Started | ⚪ |
| In Progress | 🟡 |
| Completed | 🔵 |
| Validated | ✅ |
| Blocked | 🔴 |

---

## Readiness Levels

Use the readiness definitions from [Partner Readiness Framework](../framework/partner-readiness.md):

| Score | Level |
|---|---|
| 0–49 | Foundation |
| 50–69 | Developing |
| 70–84 | Ready |
| 85–100 | Advanced |

Readiness scores are a program-management framework, not an official Huawei Cloud / HCPN qualification score.

---

## Update Cadence

Minimum recommended cadence:

- after each formal training;
- after each assessment;
- after each capability validation;
- when a blocker materially changes;
- at least once per month.

Recommended operating rhythm:

```text
Training / Workshop
       ↓
Partner Update
       ↓
Evidence Submitted
       ↓
Reviewer Validation
       ↓
Progress Page Updated
       ↓
Next Milestone
```

---

## Partner Update Workflow

1. Copy [Partner Progress Template](../templates/partner-progress-template.md).
2. Save as `partners/<partner-id>.md`.
3. Fill in track, current stage, status, readiness, and milestone table.
4. Add public-safe evidence only.
5. Update blockers and next milestone.
6. Submit through Pull Request or repository owner update.
7. Reviewer validates the change.
8. Merge to `main`.

For recurring updates, use:

- [Monthly Update Template](../templates/monthly-update-template.md)
- [Evidence Template](../templates/evidence-template.md)
- [Quarterly Review Template](../templates/quarterly-review-template.md)

---

## Public vs Internal Data

### Safe for Public Repository

Examples:

- partner track;
- stage / month;
- completion status;
- readiness level;
- sanitized assessment status;
- public-safe certification status;
- public workshop or event links;
- sanitized PoC status such as `PoC In Progress`;
- blockers stated without confidential details.

### Keep Internal

Do not publish:

- customer names without approval;
- opportunity values;
- revenue;
- pricing;
- cloud consumption values;
- contract information;
- internal partner scoring details not approved for disclosure;
- personal certification IDs;
- credentials / tokens / keys;
- exam vouchers;
- internal screenshots;
- Huawei confidential information;
- customer confidential information.

---

## Example Partner

See:

- [Partner Example](partner-example.md)

This file demonstrates how a partner page should look and can be copied when onboarding a new participant.

---

## Related Frameworks

- [6-Month Roadmap](../roadmap/6-month-roadmap.md)
- [12-Month Roadmap](../roadmap/12-month-roadmap.md)
- [Capability Funnel](../framework/capability-funnel.md)
- [Partner Readiness](../framework/partner-readiness.md)
- [KPI Dashboard](../framework/kpi-dashboard.md)

---

## Governance

Recommended roles:

| Role | Responsibility |
|---|---|
| Partner PIC | Submits progress update |
| Track Owner | Reviews track alignment |
| Reviewer | Validates evidence and milestone |
| Program Owner | Approves readiness/status changes |
| Program Analyst | Consolidates KPI and dashboard data |

---

## Principle

A partner progress page should answer five questions clearly:

1. **Where is the partner now?**
2. **What has been completed?**
3. **What evidence supports the status?**
4. **What is blocking progress?**
5. **What is the next milestone?**

The goal is not to create administrative overhead, but to make partner enablement visible, consistent, and actionable.
