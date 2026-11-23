# KPI methodology and validation

**Data:** synthetic IT delivery projects. Snapshot as of **2026-11-23**. All financials and timesheets represent sampled records; none are Celoxis or employer data.

| KPI | Business definition | Calculation | Grain / limitation |
|---|---|---|---|
| Projects | Unique active portfolio records in synthetic snapshot | Count distinct project_id | Snapshot, not time series |
| Completed | Projects whose recorded status is Completed | Count status = Completed | Does not imply on-time |
| Delayed | Projects whose recorded status is Delayed | Count status = Delayed | Status-based, not recalculated against today |
| Completion rate | Completed divided by all projects | Completed / projects | Snapshot |
| Planned cost | Total planned cost entries | Sum financials.planned_cost_inr | Sampled months |
| Actual cost | Total actual cost entries | Sum financials.actual_cost_inr | Sampled months |
| Unfavorable variance | Recorded actual less recorded plan | Actual − planned | Positive is unfavorable |
| Recorded revenue | Recorded invoicing proxy | Sum revenue_inr | Sampled months; not cash receipts |
| Contribution proxy | Recorded revenue less actual cost | Revenue − actual | Excludes other overhead; not accounting net profit |
| Utilization | Sample hours / sample availability | Sum hours_logged / sum available_hours | Only sampled timesheets, not organization capacity |
| Open follow-ups | Actions with status Open | Count status Open | Status-based |
| Overdue actions | Open and due date earlier than report date | Open AND due date < snapshot | Snapshot-dependent |

**Data QA:** foreign keys must resolve, numerical costs are nonnegative, known status values are used and project count is not double-counted after joining one-to-many tables. Excel cross-tab is formula-based, not a native PivotTable.
