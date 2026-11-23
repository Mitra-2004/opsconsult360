# Power BI Service — final acceptance checklist

**Status:** Remote Power BI workspace cannot be opened from this GitHub repository. This checklist is for final interactive review; it is not a claim that the checks passed.

1. Verify that the saved report belongs to the correct **My workspace** and is associated with the OpsConsult 360 project.
2. Confirm the report contains **Executive Overview**, **Project Performance**, **Financial Analytics**, and **Resource & Operations** pages.
3. Validate data sources: six CSVs; no accidental duplicates and no missing project or employee relationship.
4. Validate model relationships: projects[project_id] to tasks, financials, timesheets, actions as one-to-many; employees[employee_id] to timesheets as one-to-many. Prefer single-direction filtering.
5. Reset slicers to all departments and compare 60 projects, 15 completed, 15 delayed, 25% completion and recorded cost variance **₹2,679,054.29** against SQLite/Excel. Be explicit that status is a snapshot and finance is sampled periods.
6. Choose Engineering and a second department; verify cards, tables and charts all update coherently and that no visual shows an outdated selected-project context.
7. Drill to a delayed project; verify project ID, status, costs and dates against its source CSV records.
8. Check financial time trend: recorded planned costs, actual costs and revenue are time-aligned and consistent with monthly source totals.
9. Review resource utilization: sample hours / sample availability; don't compare directly with employees' nominal weekly capacity.
10. Test export, sorting, empty states, tooltips, visual labels, responsiveness and contrast. Check that all sensitive data is synthetic.
11. Save changes, reopen the report, and verify persistence.

**Evidence to capture:** workspace report URL, screenshot of all four pages, data model screenshot, one filtered department screenshot, and numeric reconciliation notes.

Never mark a step PASS without observing it in Power BI Service.
