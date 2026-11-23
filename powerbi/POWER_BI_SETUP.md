# Power BI reporting — build instructions

**Status:** This repository does not yet contain a native report (.pbix). These are authoring instructions, not evidence of a published Power BI dashboard.

1. Import the six files from data/ into Power BI Service or Desktop, depending on account permissions.
2. Ensure financial values/hours are numeric; dates are Date; completion_pct is 0–100.
3. Relate projects[project_id] one-to-many to tasks, financials, timesheets and actions using single-direction filtering. Relate employees[employee_id] one-to-many to timesheets.
4. Enter the measures in measures.dax individually (the file is a reference, not an executable multi-measure script).
5. Build four pages: Executive Overview, Delivery & Exceptions, Financials, Resources & Actions.
6. Reconcile all KPI values with the Excel workbook and SQLite queries under equivalent filters; test slicers, exports and drilldowns.

Do not compare sampled monthly actual costs with full-lifecycle project budgets as though they had identical time grains. Resource percentages use recorded available hours rather than nominal weekly capacity.
