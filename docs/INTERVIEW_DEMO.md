# OpsConsult 360 — Interview demonstration (2 minutes)

**Scenario:** COO needs to review an IT services project portfolio and understand which deliveries require intervention. Data is fictional and clearly synthetic.

| Time | What to show | What to say |
|---|---|---|
| 0:00–0:20 | Excel COO Review, portfolio totals | "I created a 60-project synthetic operational portfolio with consistent project, cost, resource and action records." |
| 0:20–0:40 | Excel Pivot Analysis, department trends | "I compare status, progress and recorded costs by department, distinguishing sampled-period spending from whole-project budgets." |
| 0:40–1:05 | HTML dashboard: department filter, priority exceptions | "I identify delivery risks and variance exceptions, rather than making decisions using the overall average alone." |
| 1:05–1:25 | Project investigation and action ownership | "I drill into the affected project, review cost variance and outstanding follow-up responsibility." |
| 1:25–1:45 | SQLite SQL scripts / QA report | "I aggregate finance to project grain to avoid duplicate costs when joining the one-to-many operational tables." |
| 1:45–2:00 | Five-slide COO review | "I summarize findings, suggest corrective actions and acknowledge synthetic-data limitations." |

## Interview questions to rehearse

**What is your biggest KPI?** Not one number: delivery delays, recorded cost variance and overdue follow-ups together explain operational priorities.

**Why SQLite and Excel?** They make an auditable, low-friction MIS proof of concept; Excel suits ad hoc management reviews and SQL makes aggregation reproducible.

**What is the biggest data modeling risk?** Double-counting financial records when joining project rows to tasks/timesheets, and comparing sampled financial flows against lifecycle budgets.

**What makes it original?** Consistent data model, source-to-dashboard reconciliation, documented caveats, decision workflow and real interface interactions.

## Demonstrate without exaggeration
Do not claim the project improved actual customer revenue or was adopted by Celoxis. Do not claim a native Power BI deliverable or Excel PivotTables until opened and verified.
