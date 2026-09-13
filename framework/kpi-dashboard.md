# HCPN Indonesia — KPI Dashboard Framework

> **Purpose:** Provide a consistent executive and operational measurement model for HCPN Indonesia partner enablement across Reseller, Distributor, Service Partner, and CSP tracks.

The dashboard is designed to connect enablement activity with measurable capability and business outcomes:

**Training → Learning → Capability → Activation → Adoption → Business Impact**

---

## 1. Dashboard Objectives

The KPI Dashboard should answer five management questions:

1. **Are partners participating in the enablement program?**
2. **Are participants actually learning and improving?**
3. **Are partners becoming ready to sell, manage, implement, or integrate Huawei Cloud solutions?**
4. **Are those capabilities being activated in customer-facing activities?**
5. **Is enablement contributing to cloud adoption and measurable business outcomes?**

The dashboard should therefore avoid becoming only a training attendance report.

---

# 2. Dashboard Measurement Layers

The recommended dashboard contains five layers.

| Layer | Primary Question | Example KPIs |
|---|---|---|
| **L1 — Training Operations** | Is the program being delivered effectively? | Registration, Attendance, Completion, Drop-off, Learning Hours |
| **L2 — Learning Performance** | Are participants improving? | Pre/Post Test, Assessment Score, Certification Readiness, Skill Gap Closure |
| **L3 — Partner Capability** | Is the partner becoming ready? | Partner Readiness Index, Ready Personnel, Capability Gate Completion |
| **L4 — Market Activation** | Is capability being applied? | Workshops, Qualified Opportunities, PoCs, Implementations, Activated Partners |
| **L5 — Business Impact** | Is enablement creating measurable value? | Production Deployment, Cloud Adoption, Pipeline, Revenue, ROTI |

Executive relationship:

```text
Training Operations
        ↓
Learning Performance
        ↓
Partner Capability
        ↓
Market Activation
        ↓
Customer Adoption
        ↓
Business Impact
```

---

# 3. Layer 1 — Training Operations KPI

These KPIs measure program execution.

## 3.1 Registration Rate

**Purpose:** Measure interest and conversion from invitation to registration.

```text
Registration Rate (%) = Registered Participants / Invited Participants × 100
```

Recommended dimensions:

- partner type;
- partner company;
- training track;
- month;
- geography;
- online/offline delivery.

---

## 3.2 Attendance Rate

```text
Attendance Rate (%) = Attendees / Registered Participants × 100
```

Interpretation:

- high registration + low attendance may indicate scheduling or engagement issues;
- low registration may indicate weak relevance or partner communication.

---

## 3.3 Completion Rate

```text
Completion Rate (%) = Participants Completing Required Activities / Attendees × 100
```

Completion should ideally include required learning and assignment components, not only presence in a classroom.

---

## 3.4 Drop-off Rate

```text
Drop-off Rate (%) = 100 - Completion Rate
```

Track recurring causes such as:

- scheduling conflict;
- content difficulty;
- participant role mismatch;
- insufficient manager support;
- lab/access issues.

---

## 3.5 Learning Hours

Track:

- instructor-led hours;
- self-learning hours;
- hands-on lab hours;
- assessment hours.

This is useful for capacity planning, but should not be treated as a business outcome.

---

## 3.6 Training Capacity Utilization

```text
Capacity Utilization (%) = Actual Participants / Planned Capacity × 100
```

Useful for:

- class planning;
- trainer capacity;
- venue/lab planning;
- cost optimization.

---

# 4. Layer 2 — Learning Performance KPI

These metrics determine whether training creates measurable improvement.

## 4.1 Pre-Test Score

Baseline knowledge before training.

## 4.2 Post-Test Score

Knowledge level after training.

## 4.3 Learning Improvement

```text
Learning Improvement = Average Post-Test Score - Average Pre-Test Score
```

Optional normalized improvement:

```text
Improvement (%) = (Post-Test - Pre-Test) / Pre-Test × 100
```

---

## 4.4 Assessment Pass Rate

```text
Assessment Pass Rate (%) = Participants Passing Assessment / Participants Assessed × 100
```

---

## 4.5 Certification Readiness / Pass Rate

Where applicable:

```text
Certification Pass Rate (%) = Participants Passing Certification / Participants Taking Exam × 100
```

For a public repository, publish only aggregate or partner-approved status. Do not expose personal exam IDs or confidential examination data.

---

## 4.6 Skill Gap Closure

Recommended model:

```text
Skill Gap Closure (%) = Skills Improved / Skills Identified as Gaps × 100
```

Possible skill categories:

- product knowledge;
- architecture;
- cloud-native;
- migration;
- security;
- solution selling;
- channel management;
- pre-sales;
- service delivery.

---

# 5. Layer 3 — Partner Capability KPI

This layer connects learning with operational partner readiness.

Primary framework:

- [Partner Readiness Framework](partner-readiness.md)

## 5.1 Partner Readiness Index

Recommended dimensions:

| Dimension | Weight |
|---|---:|
| Training Completion | 10% |
| Knowledge Assessment | 15% |
| Certification / Credential Readiness | 20% |
| Hands-on / Assignment | 20% |
| Partner Activation | 15% |
| Customer Opportunity / PoC | 10% |
| Business Outcome | 10% |
| **Total** | **100%** |

Suggested levels:

| Score | Level |
|---|---|
| 0–49 | Foundation |
| 50–69 | Developing |
| 70–84 | Ready |
| 85–100 | Advanced |

> This score is a proposed program management framework, not an official Huawei Cloud partner qualification score.

---

## 5.2 Ready Personnel

Count partner personnel who have passed the required capability gate.

Track-specific examples:

- Reseller → Sales Ready personnel;
- Distributor → Channel Ready personnel;
- Service Partner → Technical Delivery Ready personnel;
- CSP → Solution Ready personnel.

---

## 5.3 Capability Gate Completion

```text
Capability Gate Completion (%) = Completed Capability Gates / Required Capability Gates × 100
```

Example gates:

- product foundation;
- architecture assessment;
- solution selling role-play;
- partner activation plan;
- capstone implementation;
- packaged solution review.

---

## 5.4 Partner Readiness Distribution

Recommended visualization:

```text
Foundation   ███████
Developing   ██████████
Ready        ███████████████
Advanced     █████
```

This helps management see ecosystem maturity rather than only average score.

---

# 6. Layer 4 — Market Activation KPI

Market Activation measures whether learned capability is being applied.

Different partner types require different activation metrics.

## 6.1 Reseller Activation

Suggested KPIs:

- account plans created;
- customer discovery meetings;
- solution workshops;
- qualified opportunities;
- PoC candidates;
- partner-led proposals.

Activation path:

```text
Sales Ready
   ↓
Account Plan
   ↓
Discovery
   ↓
Qualified Opportunity
   ↓
Solution Workshop / PoC
```

---

## 6.2 Distributor Activation

Suggested KPIs:

- downstream partners recruited;
- downstream partners trained;
- downstream partners activated;
- certification coverage;
- active partner ratio;
- partner-led opportunities.

```text
Channel Ready
   ↓
Partner Recruitment
   ↓
Partner Enablement
   ↓
Partner Activation
   ↓
Partner-Generated Opportunity
```

---

## 6.3 Service Partner Activation

Suggested KPIs:

- architecture engagements;
- migration assessments;
- PoCs;
- implementation projects;
- production deployments;
- successful service delivery.

```text
Technical Delivery Ready
   ↓
Assessment / Architecture
   ↓
PoC
   ↓
Implementation
   ↓
Production
```

---

## 6.4 CSP Activation

Suggested KPIs:

- packaged solutions;
- demos;
- joint solution workshops;
- PoCs;
- GTM activities;
- solution adoption.

```text
Solution Ready
   ↓
Packaged Solution
   ↓
Demo
   ↓
PoC
   ↓
Joint GTM
   ↓
Customer Adoption
```

---

# 7. Layer 5 — Business Impact KPI

These metrics demonstrate whether partner enablement contributes to measurable cloud outcomes.

## 7.1 Training-to-Activation Conversion

```text
Training-to-Activation (%) = Activated Partners / Partners Completing Enablement × 100
```

---

## 7.2 Training-to-PoC Conversion

```text
Training-to-PoC (%) = Partners Generating PoC / Partners Completing Enablement × 100
```

---

## 7.3 PoC-to-Production Conversion

```text
PoC-to-Production (%) = Production Deployments / Completed PoCs × 100
```

This is one of the strongest indicators of actual solution adoption.

---

## 7.4 Customer Adoption

Possible indicators:

- number of production customers;
- number of workloads deployed;
- activated cloud services;
- production usage status.

Sensitive consumption data should remain internal.

---

## 7.5 Pipeline Impact

Internal metric only unless explicitly approved for publication.

Possible measures:

- opportunity count;
- qualified pipeline value;
- influenced pipeline;
- partner-generated pipeline.

---

## 7.6 Revenue Impact

Internal measurement may include:

- partner-attributed revenue;
- influenced revenue;
- incremental cloud consumption;
- customer acquisition contribution.

Do not expose revenue values in the public GitHub repository.

---

## 7.7 Return on Training Investment — ROTI

Conceptual formula:

```text
ROTI = (Business Benefit Attributed to Training - Training Cost) / Training Cost
```

Possible training cost components:

- trainer cost;
- venue;
- lab/cloud resource;
- platform;
- certification subsidy;
- content development;
- participant time.

ROTI requires an agreed attribution methodology and should not be treated as exact unless business attribution rules are defined.

---

# 8. Core Executive KPI Set

For an executive dashboard, avoid displaying dozens of metrics on the first page.

Recommended top-level scorecard:

| KPI | Layer | Purpose |
|---|---|---|
| Attendance Rate | Operations | Participation |
| Completion Rate | Operations | Program execution |
| Learning Improvement | Learning | Knowledge gain |
| Assessment / Certification Pass Rate | Learning | Validation |
| Partner Readiness Index | Capability | Ecosystem capability |
| Ready Partners / Personnel | Capability | Deployable capability |
| Partner Activation Rate | Activation | Capability usage |
| Training-to-PoC Conversion | Activation | Customer engagement |
| PoC-to-Production Conversion | Adoption | Solution adoption |
| Business Impact / ROTI | Business | Executive value |

---

# 9. Example Dashboard Layout

## Executive View

```text
+-----------------------------------------------------------+
| HCPN INDONESIA PARTNER ENABLEMENT DASHBOARD               |
+------------------+------------------+---------------------+
| Attendance       | Completion       | Learning Improvement|
| 88%              | 81%              | +24 pts             |
+------------------+------------------+---------------------+
| Certification    | Partner Ready    | Activation Rate     |
| 74%              | 72%              | 58%                 |
+------------------+------------------+---------------------+
| Training → PoC   | PoC → Production | ROTI                |
| 22%              | 45%              | Internal            |
+------------------+------------------+---------------------+
```

> Numbers above are illustrative examples only and are not official Huawei Cloud targets.

---

# 10. Recommended Dashboard Pages

## Page 1 — Executive Summary

Display:

- total active partners;
- total participants;
- completion rate;
- certification / assessment rate;
- average Partner Readiness Index;
- activated partners;
- PoCs;
- production deployments;
- business impact status.

Recommended audience:

- Country Manager;
- ecosystem leadership;
- partner development leadership.

---

## Page 2 — Training Operations

Display:

- registrations;
- attendance;
- completion;
- drop-off;
- learning hours;
- utilization;
- month-over-month trend.

---

## Page 3 — Learning Performance

Display:

- pre-test vs post-test;
- assessment score;
- certification result;
- skill gap by domain;
- trainer effectiveness;
- content relevance.

---

## Page 4 — Partner Capability

Display:

- Partner Readiness Index;
- readiness distribution;
- readiness by partner type;
- capability gates;
- ready personnel;
- track completion.

Filter by:

- Reseller;
- Distributor;
- Service Partner;
- CSP.

---

## Page 5 — Activation & Adoption

Display:

- partner activation;
- discovery/workshop activity;
- PoC;
- implementation;
- production deployment;
- adoption funnel.

---

## Page 6 — Business Impact

Internal dashboard only.

Display:

- pipeline impact;
- partner-attributed revenue;
- cloud consumption impact;
- customer acquisition;
- ROTI;
- training-to-revenue funnel.

---

# 11. Recommended Filters

A mature dashboard should support filters such as:

- Year
- Quarter
- Month
- Partner Type
- Partner Name
- Training Track
- Readiness Level
- Industry
- Geography
- Delivery Mode
- Trainer
- Certification / Assessment Status

---

# 12. Suggested Example Targets

For mockup or planning purposes only:

| KPI | Example Target |
|---|---:|
| Attendance Rate | > 85% |
| Completion Rate | > 75% |
| Assessment / Certification Pass | > 70% |
| CSAT | ≥ 4.2 / 5 |
| Partner Readiness | ≥ 80 / 100 |
| Training-to-Activation | program-defined |
| PoC-to-Production | program-defined |
| ROTI | ≥ 3:1 |

> These values are **illustrative program targets**, not official Huawei Cloud or HCPN requirements.

Program owners should establish targets based on approved local business objectives and historical baseline data.

---

# 13. Engagement & Experience KPI

Learning quality should also be monitored.

Recommended indicators:

- CSAT;
- NPS where appropriate;
- trainer effectiveness;
- content relevance;
- hands-on lab satisfaction;
- participant engagement;
- question / forum interaction;
- recommendation score.

Example CSAT formula:

```text
CSAT = Sum of Satisfaction Scores / Number of Responses
```

---

# 14. Public vs Internal Dashboard

Because this repository is public, separate external visibility from internal business intelligence.

## Public-safe metrics

Examples:

- training status;
- track status;
- month completed;
- readiness level;
- aggregate completion;
- aggregate certification-readiness status;
- approved workshop / PoC status;
- non-confidential capability achievements.

## Internal-only metrics

Do not publish:

- customer identity unless approved;
- opportunity value;
- pipeline value;
- revenue;
- pricing;
- cloud consumption;
- contract details;
- personal exam IDs;
- internal HCPN data;
- customer architecture containing confidential information.

Recommended model:

```text
PUBLIC GITHUB
Capability Status / Progress
         |
         | aggregated / sanitized
         v
INTERNAL BI PLATFORM
Full Operational + Commercial Analytics
```

---

# 15. Data Sources

Potential sources include:

- training registration platform;
- attendance records;
- LMS;
- assessment platform;
- certification data;
- partner progress files;
- GitHub Issues / Pull Requests;
- CRM;
- PoC tracking;
- project delivery system;
- cloud usage / business systems;
- survey tools.

Not every source should feed the public repository.

---

# 16. Suggested Data Model

A simple analytical structure may contain:

## Partner Dimension

```text
partner_id
partner_name
partner_type
region
industry_focus
program_status
```

## Participant Dimension

```text
participant_id
partner_id
role
track
```

Personally identifiable information should be minimized and protected.

## Training Fact

```text
training_id
partner_id
participant_id
module
training_date
attendance
completion
pre_test
post_test
assessment_score
```

## Capability Fact

```text
partner_id
month
track
readiness_score
readiness_level
capability_gate
validation_status
```

## Activation Fact

```text
partner_id
activity_type
activity_date
status
```

## Business Fact — Internal Only

```text
partner_id
opportunity_id
poc_status
production_status
pipeline
revenue
cloud_consumption
```

---

# 17. Dashboard Refresh Cadence

Recommended cadence:

| Data | Refresh |
|---|---|
| Registration | Per training / weekly |
| Attendance | After session |
| Completion | Weekly / monthly |
| Assessment | After assessment |
| Partner Readiness | Monthly |
| Activation | Monthly |
| PoC / Production | Monthly |
| Business Impact | Monthly / Quarterly |
| Executive Review | Quarterly |

---

# 18. Monthly Operating Review

Suggested monthly review agenda:

1. training delivered;
2. participation and completion;
3. learning improvement;
4. capability gate status;
5. Partner Readiness movement;
6. partner activation;
7. blockers;
8. next-month actions.

---

# 19. Quarterly Executive Review

Recommended executive narrative:

```text
How many partners did we reach?
        ↓
How many completed enablement?
        ↓
How many became Ready?
        ↓
How many became Activated?
        ↓
How many generated customer engagement / PoC?
        ↓
How many reached Production?
        ↓
What business outcome was created?
```

This turns training reporting into ecosystem business reporting.

---

# 20. Track-Specific KPI Summary

| KPI Area | Reseller | Distributor | Service Partner | CSP |
|---|---|---|---|---|
| Primary Readiness | Sales Ready | Channel Ready | Technical Delivery Ready | Solution Ready |
| Main Activation | Opportunity | Downstream Partner Activation | PoC / Implementation | Packaged Solution / PoC |
| Key Capability | Solution Selling | Channel Management | Architecture & Delivery | Solution Integration |
| Customer Outcome | Acquisition | Ecosystem Reach | Production Delivery | Solution Adoption |

---

# 21. KPI Ownership

Suggested ownership:

| KPI Category | Suggested Owner |
|---|---|
| Training Operations | Enablement / Training Team |
| Learning Performance | Training / Certification Team |
| Partner Capability | Track Owner / Partner Development |
| Activation | Partner Business / Sales / Ecosystem Team |
| Adoption | Solution / Service / Customer Team |
| Business Impact | Sales Operations / Finance / Management |

Ownership should be explicitly defined to avoid missing or disputed data.

---

# 22. Data Quality Rules

Every KPI should have:

- clear definition;
- calculation formula;
- source system;
- owner;
- refresh frequency;
- confidentiality classification;
- last update timestamp.

Avoid combining inconsistent definitions across partner tracks.

Example:

> "Activated Partner" must have one agreed definition across the program.

Possible definition:

> A partner that has completed the required readiness gate and has performed at least one validated customer-facing or ecosystem activation activity.

---

# 23. Dashboard Health Indicators

Recommended status model:

```text
🟢 On Track
🟡 Attention Required
🔴 Off Track
⚪ No Data
```

Do not assign status based on subjective judgment alone. Each color should map to defined thresholds.

---

# 24. Suggested Tooling

The measurement framework is technology-neutral.

Possible implementation tools:

- Microsoft Power BI;
- Looker Studio;
- Tableau;
- Excel / Google Sheets for initial phase;
- SQL data warehouse;
- GitHub data for public progress;
- CRM data for internal activation/business metrics.

A practical maturity path:

```text
Phase 1
Spreadsheet + GitHub
      ↓
Phase 2
Central SQL / Data Model
      ↓
Phase 3
Power BI / BI Dashboard
      ↓
Phase 4
Automated Training-to-Revenue Analytics
```

---

# 25. Relationship to Other Frameworks

This dashboard should be used together with:

- [Capability Funnel](capability-funnel.md)
- [Partner Readiness Framework](partner-readiness.md)
- [6-Month Roadmap](../roadmap/6-month-roadmap.md)
- [12-Month Roadmap](../roadmap/12-month-roadmap.md)

Partner tracks:

- [Reseller](../tracks/reseller.md)
- [Distributor](../tracks/distributor.md)
- [Service Partner](../tracks/service-partner.md)
- [CSP](../tracks/csp.md)

---

# 26. Definition of Dashboard Success

The KPI Dashboard is successful when management can move from a training statement like:

```text
We trained 500 participants.
```

to an outcome-oriented statement such as:

```text
500 participants trained
        ↓
420 completed
        ↓
310 passed capability validation
        ↓
180 partner personnel became Ready
        ↓
90 partners activated
        ↓
40 PoCs / customer engagements
        ↓
18 production deployments
        ↓
measurable cloud adoption / business impact
```

The actual numbers will vary by program and must come from validated data.

---

# 27. Executive Principle

> **Do not measure training only by how many people attended. Measure whether capability was created, activated, adopted, and converted into business value.**

The intended management chain is:

**Training → Capability → Activation → Adoption → Revenue**

---

# 28. Disclaimer

This KPI Dashboard Framework is a proposed program-management and analytics model for the HCPN Indonesia Partner Enablement repository.

It is **not an official Huawei Cloud KPI standard, HCPN qualification framework, incentive policy, or certification requirement** unless explicitly approved by Huawei Cloud.

All target values shown in this document are examples for planning and dashboard design. Official metrics, targets, policies, and commercial data must follow authorized Huawei Cloud / HCPN sources and local management approval.
