# Excel / Power BI native acceptance — 23 November 2026

## Excel workbook (direct structural inspection)

- Workbook source: `OpsConsult_360_Excel_Final_Review.xlsx`.
- 19 worksheets.
- Project Portfolio headers on row 6 include **Project ID**, **Department**, **Status**, **Planned Cost YTD**, **Actual Cost YTD**.
- Resource Allocation headers on row 6 include **Department**, **Hours Logged**, **Assigned Capacity**.
- `excel/CREATE_NATIVE_PIVOTS.bas` references those exact headers and uses source ranges anchored at A6. This is a **static compatibility check only**, not Excel execution.
- The workbook has **no native PivotTable OOXML parts** in its current committed state; slicers are not verified.

### Native Excel acceptance still required

1. Open a COPY of the workbook using Microsoft Excel (Mac or Windows) and import `excel/CREATE_NATIVE_PIVOTS.bas` into a VBA module.
2. Run `CreateOpsConsultPivotTables` and confirm all three new PivotTable sheets appear without error.
3. Run `AddOpsConsultDepartmentSlicers` where supported, or insert slicers manually.
4. Change the Department slicer and verify the pivot measures against the COO Review sheets; save and reopen the workbook.
5. Keep `.xlsm` if retaining macros; save a clean `.xlsx` only once pivot objects are verified in Excel.

**Status:** NOT executed in Excel. Do not claim native Excel PivotTables or slicers complete.

## Power BI Service (account-level verification)

The Microsoft Power BI app has been installed, but the current ChatGPT tool connection does not expose actions for opening or editing reports, and no authenticated Power BI browser tab was available. The project ZIPs contain no `.pbix`/`.pbit` report file.

The report previously described as saved in My workspace **has not been independently reopened in this session**. Its four pages, DAX results, slicers, visuals, persistence, and report URL therefore remain **unverified**.

### To complete verification

Open the actual Power BI Service report via a supported interactive browser session or supply a readable report export/model and screenshots. Validate the 4 pages, 60-project count, 15 delayed projects, cost variance of ₹2,679,054.29, project/employee relationships, cross-filtering and persistence.

**Status:** Saved-report existence and functionality NOT confirmed in this session.

## What IS verified

The HTML OpsConsult 360 v2 site was deployed to Vercel and its public assets passed GitHub Actions HTTP checks. Cross-source SQLite/CSV validation and Playwright browser testing of the HTML site passed. These are **not substitutes** for native Excel and Power BI testing.
