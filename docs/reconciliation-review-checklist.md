# Cross-tool reconciliation review

Use the same synthetic dataset revision and identical department, status and reporting-period filters across Excel, SQL and Power BI. The public HTML dashboard is a separate artifact.

| Check | Review method |
|---|---|
| Project count | Count distinct project IDs, not joined transaction rows |
| Actual and planned costs | Aggregate finance records at their original grain before joining |
| Variance | Actual minus planned; positive cost variance is unfavorable |
| Utilization | Divide aggregate sampled hours by aggregate sampled availability; do not average row percentages |
| Empty selection | Distinguish zero totals from undefined ratios |

Capture filter values, source revision, expected result and actual result. Investigate rounding only after confirming matching row populations. This checklist defines review steps; it is not a new execution or acceptance record.
