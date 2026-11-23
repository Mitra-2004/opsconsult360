# OpsConsult 360
**Project Performance & Operations MIS | Excel · SQL · Management Reporting**

A portfolio case study for an internal business-operations review system. All records and results are **synthetic** and are not actual Celoxis company data.

## Repository contents

| Path | Purpose | Status |
|---|---|---|
| `excel/OpsConsult_360_Excel_Final_Review.xlsx` | Excel MIS with executive metrics, department analysis, investigation, financial and resource reporting | Uploaded |
| `sql/opsconsult.db` | Sample SQLite relational database | Uploaded |
| `sql/analysis.sql` | Department delivery, financial variance, monthly revenue and resource utilization analyses | Uploaded |
| `docs/COO_Management_Review.pptx` | Five-slide management review and recommendations | Uploaded |
| `docs/KPI_DICTIONARY.md` | Precise KPI definitions and assumptions | Uploaded |
| `docs/VALIDATION_REPORT.md` | Recorded dataset and analytical QA | Uploaded |
| `docs/DASHBOARD_QA_UPDATE.md` | Dashboard fixes and user-side interaction checks | Uploaded |
| `powerbi/measures.dax` | Reference DAX measures for authoring | Uploaded |
| `powerbi/POWER_BI_SETUP.md` | Power BI implementation instructions | Uploaded |

### Important: files not present in this repository yet
- `dashboard/index.html` and `dashboard/data.json` — the previously tested HTML dashboard and its data payload.
- `data/` — six source CSV datasets (`projects`, `tasks`, `financials`, `employees`, `timesheets`, `actions`).

These components existed in the previously prepared local ZIP, but were **not found in the GitHub tree** during the 23 November 2026 audit. Until uploaded, the dashboard cannot be reproduced from this repository alone; the SQL example database and Excel workbook are available.

## Business use case
A COO or operations analyst needs to monitor project completion, exceptions, sampled actual vs planned expenditure, employee utilization and action follow-ups. An analyst should be able to observe an exception, investigate it, recommend a decision and track an owner.

## Open the files
1. Open `excel/OpsConsult_360_Excel_Final_Review.xlsx` in Excel. Explore COO Review, Project Investigation, Pivot Analysis and QA sheets.
2. Open `docs/COO_Management_Review.pptx` for the executive narrative.
3. Run the SQL reports with `sqlite3 sql/opsconsult.db < sql/analysis.sql`. (SQLite command-line tool required.)
4. Once the `dashboard/` and `data/` folders are uploaded, follow the dashboard instructions and test its interactions.

## Verification and limitations
- The dataset is fictional and sampled; finance, project status and resource measures have different reporting grains.
- Prior user-side HTML dashboard checks confirmed filter, project drill-down, search, export and reset interactions **in the local ZIP version**, not in this repository.
- Excel contains **formula-based pivot-style summaries, not native PivotTables or slicers**.
- `powerbi/` contains a model guide and DAX reference, **not an authored, tested or published Power BI report**.
- Do not claim real business impact or company deployment.

## Next milestone
Upload the missing six CSVs and the corrected HTML dashboard, reconcile their KPIs with Excel and the SQLite database, then finish native Excel PivotTables and Power BI authoring when available.
