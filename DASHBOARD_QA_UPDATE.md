# OpsConsult 360 — Dashboard QA update (23 November 2026)

## What was improved

1. **Department-filter behavior:** preserved one consistent department filter for KPI cards, cost-variance bar chart, priority exception list, financial report, tasks and actions. The project-detail panel is hidden when the department filter changes to prevent stale context.
2. **Project drill-down:** the priority exceptions list now contains accessible **Review project** controls. Selecting one opens Project delivery, filters the register to the chosen project, and opens a project investigation panel with deadline, owner, status, cost variance, completed tasks and overdue follow-up count.
3. **Exception queue:** the dashboard now displays how many distinct projects require review and which have delayed status or a recorded positive cost variance. Its rows are limited to the highest-priority ten; the count shows the full department-level set. The queue is meant to support review, not establish causality.
4. **Keyboard accessibility:** added visible focus styling and a labelled project-investigation region.

## Executed checks

The source JavaScript compiled successfully via Node.js `vm.Script`. The checked JavaScript was run against a minimal simulated document to verify:

- default portfolio displays 60 projects;
- choosing Engineering changes the rendered KPI cards and financial variance chart;
- filtered exception counts and action buttons are rendered;
- project investigation includes financials, due dates, tasks and action counts;
- reset restores unfiltered KPI rendering.

**Limitation:** Full Chromium interaction testing could not run in the provided container because its browser navigation to `file://` and `localhost` was blocked by the environment administrator. These JavaScript behavior checks do **not** replace user-side browser testing. No claim is made that full accessibility, responsive layout, or CSV-download behavior was tested by this update. User previously reported CSV export and search working.

## Re-test in your browser

1. Open `dashboard/index.html` from this updated package (not a previously downloaded version).
2. Note overall project count `60` and the full-scope exception summary.
3. Choose **Engineering** from the Department dropdown: project count should drop, cost-variance bars should narrow to Engineering and the exception summary should recalculate.
4. In **Priority exceptions**, select a project ID. You should navigate to **Project delivery** with the selected project shown in its investigation panel.
5. Close the investigation, change Department, then verify the old investigation doesn't remain on screen.
6. Select Reset and ensure the portfolio total returns to `60`.
7. Export CSV and check selected department records, since filters should affect exported data as well.

The dataset is entirely synthetic. Project statuses are fixed as of 23 November 2026. Monetary values represent sampled-period financials, not audited company figures.
