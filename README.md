# OpsConsult 360
**Project Performance & Operations MIS** · Advanced Excel · SQL · Management Reporting · Power BI preparation

A professional portfolio case study for business operations and COO reporting. **All records are synthetic** and do not describe Celoxis or any real employer.

## Purpose
Support the full operations workflow: **Observe → Investigate → Understand → Decide → Report.** Review project delivery, cost overruns, recorded revenue, staffing capacity and follow-up ownership.

## Repository structure

| Location | Deliverable |
|---|---|
| [excel/OpsConsult_360_Excel_Final_Review.xlsx](excel/OpsConsult_360_Excel_Final_Review.xlsx) | 19-sheet formula-driven MIS workbook and executive review |
| [excel/CREATE_NATIVE_PIVOTS.bas](excel/CREATE_NATIVE_PIVOTS.bas) | VBA module to create three *native* Excel PivotTables |
| [dashboard/index.html](dashboard/index.html) | Self-contained interactive HTML dashboard (download and open locally) |
| [dashboard/data.json](dashboard/data.json) | Synthetic data behind the offline dashboard |
| [data/](data/) | Six relational CSV datasets |
| [sql/opsconsult.db](sql/opsconsult.db) | SQLite database / reproducible data snapshot |
| [sql/analysis.sql](sql/analysis.sql) | Department, cost, monthly revenue and utilization analyses |
| [docs/COO_Management_Review.pptx](docs/COO_Management_Review.pptx) | Five-slide executive management review |
| [docs/KPI_DICTIONARY.md](docs/KPI_DICTIONARY.md) | Metric definitions, time grain and caveats |
| [docs/AUTOMATED_QA.md](docs/AUTOMATED_QA.md) | Results of automated cross-file validation |
| [powerbi/](powerbi/) | DAX measure references and authoring steps, **not a finished Power BI report** |
| [tools/](tools/) | Rebuild and verification scripts |

## Quick start
1. Download the repository ZIP from GitHub.
2. Open `excel/OpsConsult_360_Excel_Final_Review.xlsx` using Excel. Start with **COO Review**, **Project Investigation**, **Pivot Analysis**, and **Executive QA Plus**.
3. Open `dashboard/index.html` in a browser. The generated version contains embedded synthetic data and works offline. Test department filters, exception investigation, search, Reset and CSV export.
4. If SQLite is installed, run `sqlite3 sql/opsconsult.db < sql/analysis.sql`.
5. Open `docs/COO_Management_Review.pptx` to review management findings and recommended decisions.

## Advanced Excel: native PivotTables
The workbook currently has formula-based pivot-*style* summaries, **not native PivotTable objects or slicers**. To add native PivotTables in Excel on Mac:
1. Make a copy of the workbook. In Excel, enable the **Developer** tab if needed.
2. Open the Visual Basic Editor, insert/import the module from `excel/CREATE_NATIVE_PIVOTS.bas`.
3. Run `CreateOpsConsultPivotTables` and inspect the generated **Native Pivot - Delivery**, **Native Pivot - Finance**, and **Native Pivot - Resources** sheets.
4. Reconcile totals to **COO Review** and **Excel QA**. Save as `.xlsm` to preserve the macro, or copy the completed PivotTable sheets into a macro-free `.xlsx` if desired.

**The macro has been prepared, but has not been executed or tested inside Microsoft Excel.** Excel for Mac features and macro settings may vary.

## Reproducible build and QA
All six CSVs and the **GitHub version** of the offline HTML dashboard are deterministically regenerated from the committed SQLite snapshot:

```bash
python3 tools/build_assets.py
python3 tools/qa_data.py
node tools/dashboard_smoke.cjs
```

The GitHub Actions workflow performs those checks automatically, then commits any regenerated datasets/dashboard and the QA report. The GitHub HTML version **is not byte-identical to the earlier locally tested design**, although it uses the same dataset and its key logic was smoke-tested.

## Data notes
- 60 projects, 360 tasks, 240 finance rows, 48 employees, 240 timesheets and 21 actions.
- 15 completed projects and 15 delayed projects.
- Recorded-period unfavorable cost variance: **₹2,679,054.29**.
- Sampled finance, projects and timesheets have different reporting grains. Do not equate sampled financial cost with a whole-project budget or sampled utilization with total organization capacity.
- These figures demonstrate a simulated scenario, not measured business impact.

## Completion and limitations
**Verified:** repository file presence, six-table reconciliation with SQLite, key project and finance KPIs, workbook package structure, no cached formula errors, dashboard JavaScript smoke tests, 5-slide presentation structure.

**Pending:** live Excel macro/PivotTable execution, full Excel recalculation and slicer testing, manual browser-level acceptance of the GitHub-regenerated dashboard, and Power BI Service report validation. A native `.pbix` is not included.

## Portfolio interview demonstration
Start with a delayed-project KPI, filter to the department, inspect a project and its recorded cost variance, review owner follow-ups, and present one defensible corrective action. Clearly distinguish observations from recommendations.
