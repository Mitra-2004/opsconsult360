# OpsConsult 360 — Project Performance & Operations MIS

Portfolio case study for an internal business-operations review system. **All data is synthetic. This is not actual Celoxis data.**

## Deliverables
- `OpsConsult_360_Excel_Final_Review.xlsx` — latest formula-driven Excel management reporting workbook with department summaries, financials, COO review and project investigation.
- `dashboard/index.html` and `dashboard/data.json` — locally hosted/standalone interactive management reporting interface. Open HTML with local files if supported; for reliable JSON loading serve this folder with `python3 -m http.server 8000` then open `http://localhost:8000/dashboard/`.
- `data/` — 6 connected CSV tables: projects, tasks, financials, employees, timesheets, and actions.
- `sql/analysis.sql`, `sql/opsconsult.db` — reproducible analysis queries and SQLite example database.
- `docs/COO_Management_Review.pptx` — five-slide management review.
- `powerbi/` — DAX measures and setup instructions, **not a finished PBIX report**.

## Main management questions
What is the status of the project portfolio? Which departments have delays or unfavorable financial variance? Where is resource capacity constrained? What corrective actions are overdue?

## Quick start
1. Open the Excel workbook in Microsoft Excel; inspect `COO Review`, `Project Investigation`, `Pivot Analysis`, and `Executive QA Plus`.
2. Open `dashboard/index.html` with a local browser; check department filters, priority exceptions, drill-downs, CSV export and Reset.
3. Run `sqlite3 sql/opsconsult.db < sql/analysis.sql` to reproduce the SQL analyses.
4. Open the COO review presentation to discuss prioritization and suggested actions.

## QA and limitations
- Prior user-side browser checks confirmed department filtering, exception drilldown, search, export, and reset in the corrected dashboard.
- Formula and SQL validations are recorded in `docs/VALIDATION_REPORT.md` and `docs/DASHBOARD_QA_UPDATE.md`.
- The spreadsheet has pivot-*style* formula summaries, **not native PivotTable objects or slicers**.
- A native Power BI report is still pending; do not claim it is built until verified.
- No claim of real company impact, deployment or accuracy on real business operations is made.

## Interview demo
Observe a delivery KPI, filter to the department, investigate a delayed or over-budget project, inspect financial and action-owner details, and recommend a tracked follow-up action.
