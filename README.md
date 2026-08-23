# HCPN Indonesia Partner Enablement

> Public partner enablement, training roadmap, capability tracking, and progress visibility framework for Huawei Cloud Partner Network (HCPN) partners in Indonesia.

This repository is designed as a shared workspace for partner enablement programs across **Reseller, Distributor, Service Partner, and Cloud Solution Provider (CSP)** tracks.

The objective is not only to document training activities, but to make partner capability development visible and measurable through the following journey:

**Training → Capability → Certification → Partner Activation → Customer Adoption → Revenue**

---

## 🎯 Purpose

The repository helps HCPN partners and program owners to:

- understand the learning track for each partner type;
- follow a structured 6-month enablement journey;
- extend the program into a 12-month advanced roadmap;
- track monthly training and capability progress;
- prepare for assessments and certification readiness;
- connect training outcomes with partner activation and business impact;
- provide transparent progress visibility to partners;
- maintain a reusable framework for future partner enablement programs.

---

## 🧭 Partner Tracks

| Partner Type | Primary Focus | 6-Month Target Outcome |
|---|---|---|
| **Reseller** | Product Knowledge & Sales | Sales Ready |
| **Distributor** | Channel Management & Ecosystem | Channel Ready |
| **Service Partner** | Technical Delivery & Service | Technical Delivery Ready |
| **CSP** | Solution Integration & Resale | Solution Ready |

Detailed tracks:

- [Reseller Track](tracks/reseller.md)
- [Distributor Track](tracks/distributor.md)
- [Service Partner Track](tracks/service-partner.md)
- [CSP Track](tracks/csp.md)

---

## 🗓️ 6-Month Core Enablement Roadmap

The first six months focus on building foundational capability and validating partner readiness.

| Month | Theme | Reseller | Distributor | Service Partner | CSP |
|---|---|---|---|---|---|
| **M1** | Foundation | Product Quick Start | Distributor Foundation | Technical Foundation | Cloud Native Foundation |
| **M2** | Knowledge | HCCDA-Tech Essentials | Partner Center Platform | Solution Architecture | Solution Architecture |
| **M3** | Capability | Solution Selling | HCPN Ecosystem | Migration & Infrastructure | AI & Data |
| **M4** | Practice | Commercial Workshop | Channel Management | Big Data & Cloud Native | Golden Course |
| **M5** | Activation | HCPN Policy + Sales Activation | Partner Business Development | HCIP/HCIE Preparation | HCPP / Pre-sales |
| **M6** | Validation | Sales Readiness | Channel Capability | Technical Delivery Assessment | Solution Design Assessment |

Monthly learning cycle:

**Learn → Practice → Apply → Validate**

See the full roadmap:

- [6-Month Roadmap](roadmap/6-month-roadmap.md)

---

## 🚀 12-Month Program Expansion

After Month 6, the program moves from capability development into specialization, customer engagement, and business activation.

| Quarter | Phase | Main Objective |
|---|---|---|
| **Q1** | Foundation | Understand Huawei Cloud and HCPN role |
| **Q2** | Capability | Build sales, channel, technical, or solution capability |
| **Q3** | Specialization | Develop advanced and industry-specific expertise |
| **Q4** | Activation | Drive customer engagement, PoC, production, and business outcomes |

Months 7–12 focus on:

- Advanced Capability
- AI / Data / Cloud Native / Security specialization
- Industry Enablement
- Customer Workshops
- PoC & Joint GTM
- Annual Business Review

See:

- [12-Month Roadmap](roadmap/12-month-roadmap.md)

---

## 📊 Partner Progress Tracking

Each partner can have a public progress page inside:

```text
partners/<partner-id>.md
```

Example:

```text
partners/partner-example.md
```

Recommended status values:

- `Not Started`
- `In Progress`
- `Completed`
- `Validated`
- `Blocked`

Example progress view:

| Month | Milestone | Status |
|---|---|---|
| M1 | Foundation | ✅ Validated |
| M2 | Knowledge | ✅ Completed |
| M3 | Capability | 🟡 In Progress |
| M4 | Practice | ⚪ Not Started |
| M5 | Activation | ⚪ Not Started |
| M6 | Validation | ⚪ Not Started |

Use the template:

- [Partner Progress Template](templates/partner-progress-template.md)

---

## 📈 Partner Readiness Model

A partner can be evaluated using a proposed readiness model:

| Dimension | Weight |
|---|---:|
| Training Completion | 10% |
| Knowledge Assessment | 15% |
| Certification | 20% |
| Hands-on / Assignment | 20% |
| Partner Activation | 15% |
| Customer Opportunity / PoC | 10% |
| Business Outcome | 10% |
| **Total** | **100%** |

Suggested readiness levels:

| Score | Level |
|---|---|
| `< 50` | Foundation |
| `50–69` | Developing |
| `70–84` | Ready |
| `85–100` | Advanced |

> This scoring model is a proposed program framework and is not an official Huawei Cloud partner qualification model.

See:

- [Partner Readiness Framework](framework/partner-readiness.md)

---

## 🔄 Capability Funnel

Partner enablement should be measured beyond training attendance.

```text
Reach
  ↓
Registration
  ↓
Attendance
  ↓
Learning
  ↓
Certification
  ↓
Capability
  ↓
Partner Activation
  ↓
PoC
  ↓
Production Deployment
  ↓
Customer Adoption
  ↓
Revenue
```

See:

- [Capability Funnel](framework/capability-funnel.md)
- [KPI Dashboard Framework](framework/kpi-dashboard.md)

---

## 🏗️ Repository Structure

```text
.
├── README.md
├── CONTRIBUTING.md
├── NOTICE.md
├── tracks/
│   ├── reseller.md
│   ├── distributor.md
│   ├── service-partner.md
│   └── csp.md
├── roadmap/
│   ├── 6-month-roadmap.md
│   └── 12-month-roadmap.md
├── framework/
│   ├── capability-funnel.md
│   ├── partner-readiness.md
│   └── kpi-dashboard.md
├── partners/
│   └── partner-example.md
├── templates/
│   ├── partner-progress-template.md
│   └── monthly-update-template.md
├── docs/
│   ├── index.md
│   └── _config.yml
└── .github/
    ├── ISSUE_TEMPLATE/
    │   └── partner-progress-update.yml
    └── PULL_REQUEST_TEMPLATE.md
```

---

## 🤝 How Partners Update Progress

Recommended contribution workflow:

1. Fork or clone this repository.
2. Open the relevant partner progress file.
3. Update current month, checklist, status, and public-safe evidence.
4. Commit the changes.
5. Open a Pull Request.
6. Program owner or reviewer validates the update.
7. Once merged, the GitHub repository becomes the shared source of truth.

Suggested branch naming:

```text
partner/<partner-id>/m1-update
partner/<partner-id>/m2-assessment
track/reseller/content-update
```

---

## 🧑‍💼 Suggested Governance

| Role | Responsibility |
|---|---|
| Repository Owner | Overall program governance |
| Track Owner | Manages Reseller / Distributor / Service Partner / CSP track |
| Partner PIC | Updates partner progress |
| Reviewer | Validates evidence and milestone completion |
| Program Analyst | Tracks KPI, readiness, and business impact |

Recommended update frequency:

**After every training, assessment, or at least once per month.**

---

## 🔐 Public Repository Rules

Because this repository is intended to be public, do **not** publish:

- Huawei confidential information;
- customer confidential information;
- confidential pricing;
- opportunity values;
- credentials or access keys;
- exam voucher codes;
- personal certification IDs;
- private partner contracts;
- internal system screenshots;
- proprietary course materials without redistribution rights.

Public pages should show only information that is approved for external disclosure.

---

## 🌏 Future Development

This repository can evolve into a broader HCPN Indonesia enablement platform, including:

- GitHub Pages partner portal;
- visual partner progress dashboard;
- automated progress badge;
- partner readiness score;
- training calendar;
- certification roadmap;
- industry specialization tracks;
- AI / Data / Cloud Native / Security learning paths;
- automated issue-based progress updates;
- dashboard integration with Power BI or Looker Studio;
- training-to-PoC tracking;
- training-to-revenue attribution.

---

## 💡 Program Philosophy

Training should not end with attendance or certification.

The intended progression is:

**Training → Skill → Certification → Capability → Activation → Adoption → Revenue**

The goal is to build a measurable **Partner Business Enablement Engine**, not only a training calendar.

---

## ⚠️ Disclaimer

This repository is a community/program-management framework intended to support partner enablement activities in Indonesia.

It is **not an official Huawei Cloud repository, policy document, certification standard, or partner qualification document** unless formally designated or approved by Huawei Cloud.

Huawei, Huawei Cloud, HCPN, and related names and trademarks are the property of their respective owners.

Official partner requirements, certification rules, policies, incentives, and program terms should always refer to official Huawei Cloud / HCPN communication.

---

## 📬 Contribution

Partner representatives and program contributors are welcome to submit updates through Issues or Pull Requests.

Please read:

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [NOTICE.md](NOTICE.md)

---

**HCPN Indonesia Partner Enablement**

*Build Capability. Activate Partners. Accelerate Cloud Adoption.*
