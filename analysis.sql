-- OpsConsult 360: SQLite/PostgreSQL compatible analytics; monetary values are INR.
-- Project-level cost totals avoid double-counting when joining tasks or timesheets.
WITH project_cost AS (
  SELECT project_id, SUM(planned_cost_inr) AS planned_cost,
         SUM(actual_cost_inr) AS actual_cost,
         SUM(revenue_inr) AS revenue
  FROM financials GROUP BY project_id
)
SELECT p.department, COUNT(*) AS project_count,
       SUM(CASE WHEN p.status = 'Delayed' THEN 1 ELSE 0 END) AS delayed_projects,
       ROUND(AVG(p.completion_pct), 1) AS avg_completion_pct,
       ROUND(SUM(c.actual_cost), 2) AS actual_cost_inr,
       ROUND(SUM(c.revenue), 2) AS revenue_inr,
       ROUND(SUM(c.revenue-c.actual_cost), 2) AS contribution_inr
FROM projects p JOIN project_cost c ON p.project_id=c.project_id
GROUP BY p.department ORDER BY delayed_projects DESC, actual_cost_inr DESC;

-- Budget overrun exceptions (actual to date against planned cost to date)
SELECT p.project_id,p.project_name,p.department,
       ROUND(SUM(f.actual_cost_inr)-SUM(f.planned_cost_inr),2) AS unfavorable_variance_inr
FROM projects p JOIN financials f ON f.project_id=p.project_id
GROUP BY p.project_id,p.project_name,p.department
HAVING SUM(f.actual_cost_inr)>SUM(f.planned_cost_inr)
ORDER BY unfavorable_variance_inr DESC;

-- Monthly revenue trend
SELECT month, ROUND(SUM(revenue_inr),2) AS revenue_inr,
       ROUND(SUM(actual_cost_inr),2) AS cost_inr
FROM financials GROUP BY month ORDER BY month;

-- Resource utilization, across the sample recorded month-level allocations
SELECT employee_id, ROUND(100.0*SUM(hours_logged)/NULLIF(SUM(available_hours),0),1)
       AS logged_vs_allocated_capacity_pct
FROM timesheets GROUP BY employee_id ORDER BY logged_vs_allocated_capacity_pct DESC;
