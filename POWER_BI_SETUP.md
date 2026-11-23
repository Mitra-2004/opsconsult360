# Power BI Desktop report build | OpsConsult 360

A genuine `.pbix` file is **not included**: Power BI Desktop is unavailable in this build environment. The interactive `dashboard/index.html` is the fully working, tested alternative; this folder provides CSV inputs, DAX and a precise plan for creating the native Power BI report.

1. Power BI Desktop → Get Data → Text/CSV; load all six files from `../data/`.
2. Set amount/hour fields to Decimal Number and `completion_pct` to Whole Number (0–100). Set `start_date`, `planned_end_date` and `due_date` as Date. Convert `month` into a MonthStart date by adding `-01` before converting.
3. Model relationships: `projects[project_id]` (1) → (*) `financials`, `tasks`, `timesheets`, `actions` using single direction. `employees[employee_id]` (1) → (*) `timesheets[employee_id]`.
4. Add measures in `measures.dax`; DAX measures are separate expressions, not one executable multi-measure script.
5. Report page 1 **Executive Overview**: cards Projects, Completed, Delayed, Cost Variance; status bar and department slicer.
6. Report page 2 **Delivery & Exceptions**: status by department, project detail table with completion %, related tasks, project slicer, optional drill-through.
7. Report page 3 **Financials**: month axis planned vs actual and revenue, department slicer, project-level variance and conditional formatting.
8. Report page 4 **Resources & Actions**: sample utilization, hours by employee/project, action status and due date table.
9. Validate each KPI against Excel/SQLite on identical department and time filters. Project and resource KPIs have different grains: project counts are snapshot values, finance/time sheets are sampled transactions. Explicitly label their periods.
10. Test slicers, blank values, drillthrough, export and mobile view before claiming native Power BI delivery.

## Caveats
Do not add `budget_inr` (full-project budgets) to a chart of `financials[actual_cost_inr]` (sampled monthly actuals) without an explicit compatible comparison. Do not use `employee weekly_capacity_hours` as a denominator for timesheet monthly hours.
