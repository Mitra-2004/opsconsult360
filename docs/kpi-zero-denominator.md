# Undefined KPI ratios

A percentage with a zero denominator is undefined, not necessarily zero. For example, recorded hours of zero against zero available hours do not establish zero utilization. In a reconciliation, distinguish missing or undefined values from measured zeros, and apply the same convention across Excel, SQL and Power BI. DAX DIVIDE can return BLANK for a zero denominator; SQLite can use NULLIF on the denominator. This guidance does not change the existing measures.
