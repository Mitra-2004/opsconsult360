# OpsConsult 360 — Power BI model and reproducibility notes

A native Power BI Service report was reportedly created and tested in the account owner's **My workspace**. **This repository does not contain a downloadable `.pbix` or `.pbit`**, and the separate [HTML dashboard](https://opsconsult360.vercel.app/) is not the Power BI report.

For the actual acceptance findings and their evidence limitations, read [docs/POWER_BI_ACCEPTANCE.md](../docs/POWER_BI_ACCEPTANCE.md).

## Model reference (for reproducibility)

1. Load the six datasets from [../data](../data/) into Power BI.
2. Assign decimals and dates to amount/hour/date columns. Transform the monthly finance key to a true month-start date before building calendar filtering.
3. Use `projects[project_id]` (1) → (*) `tasks`, `financials`, `timesheets`, `actions`, and `employees[employee_id]` (1) → (*) `timesheets[employee_id]`. Confirm the actual deployed model rather than assuming imported relationships are correct.
4. Add the measures documented in [measures.dax](measures.dax) as a reference. The 13 reported saved measures are in the **service model** and may differ from the smaller repository reference.
5. Provide Executive Overview, Project Performance, Financial Analytics, and Resource & Operations. The project owner also reported a Project Detail drill-through page.
6. Use a proper reporting-period dimension for relevant finance/time measures, and a functioning navigation/return flow for project drill-through.
7. Reconcile ten common KPIs under the same filter context. With all filters cleared the portfolio has 60 projects, 15 completed, 15 delayed, and recorded-period unfavorable cost variance ₹2,679,054.29.
8. Test formatting, cross-filtering, DAX, drill-through, and save/close/reopen before signing off.

## Analytical caveats

- Project status is a snapshot. Do not imply historically accurate changes to project counts merely by filtering monthly finance.
- Recorded finance rows are sampled; a whole-project budget is a separate measure.
- Monthly timesheet logged and assigned hours must use matching periods.
- Every input is synthetic and no real company outcomes are asserted.

## Account access

A workspace **semantic model** was observed through an authenticated browser view. That link is not a report URL and is not an externally accessible portfolio demo. If a native report can be shared publicly without exposing private account information, add its explicit report URL separately after testing anonymous/guest access.
