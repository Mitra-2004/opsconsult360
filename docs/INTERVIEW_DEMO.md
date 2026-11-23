# OpsConsult 360 — recruiter demonstration (2 minutes)

**Scenario:** An operations leader wants to investigate project delays, recorded cost variance, resource utilization and follow-up ownership. **All records are synthetic.**

| Time | Demonstration | Explanation |
|---|---|---|
| 0:00–0:20 | Live dashboard / Excel COO Review | "I modeled a 60-project synthetic portfolio and its connected finance, task, staffing and action data." |
| 0:20–0:40 | Excel native Delivery, Finance and Resources PivotTables | "I can compare departments, apply slicers and reconcile the numbers against the source." |
| 0:40–1:00 | Native Power BI Executive Overview | "My executive KPIs reconcile against ten Excel checkpoints and support operational filtering." |
| 1:00–1:20 | Power BI Project Performance → Project Detail drill-through | "I can investigate one project's performance and return to the management summary." |
| 1:20–1:40 | Power BI Financial Analytics and Resource & Operations | "The reporting-period slicer controls period-aware financial metrics; resource hours use a comparable sample denominator." |
| 1:40–2:00 | SQL queries and COO management review | "I prevent duplicate aggregates when joining one-to-many operational tables and communicate corrective actions clearly." |

**If the interviewer cannot access your authenticated Power BI report:** demonstrate the [public interactive dashboard](https://opsconsult360.vercel.app/) and use screenshots of the actual Power BI report only when captured and accurately labeled.

## Questions to rehearse

- **Why these KPIs?** Delays, costs, resource availability and open follow-ups give complementary signals; no single number defines portfolio health.
- **Why Excel + SQL + Power BI?** Excel supports operational ad hoc review; SQL validates aggregation and grain; Power BI provides interactive reporting; the website provides a publicly accessible demo.
- **How did you avoid errors?** Reconciled ten common KPIs across Excel and Power BI, checked 13 measures, and separated project snapshots from sampled-period transactions.
- **What is the biggest analytical risk?** Double-counting when joining projects to multiple one-to-many tables, and comparing sample-period costs with lifecycle budgets.
- **What should an operations manager do?** Assign owners to the highest-impact delayed projects and investigate cost variances before recommending a change.

## Evidence and disclosure

The [Power BI acceptance record](POWER_BI_ACCEPTANCE.md) reports final owner-confirmed acceptance after remediation; private report access and screenshots have not been published. The native Excel final workbook was structurally validated, but its `.xlsm` upload to GitHub is outstanding. Do not say the project generated real revenue, was adopted by an employer, or uses actual Celoxis data.
