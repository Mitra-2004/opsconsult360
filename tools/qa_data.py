#!/usr/bin/env python3
"""Standard-library verification of SQL, exported CSV, HTML and Excel OOXML."""
import csv, json, sqlite3, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
TABLES=("projects","tasks","financials","employees","timesheets","actions")
with sqlite3.connect(ROOT/"sql"/"opsconsult.db") as db:
    db.row_factory=sqlite3.Row
    items={t:[dict(r) for r in db.execute("SELECT * FROM "+t)] for t in TABLES}
for t in TABLES:
    with (ROOT/"data"/(t+".csv")).open(encoding="utf-8",newline="") as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==len(items[t]), f"Incorrect count for {t}"
    key=list(items[t][0])[0]
    assert {str(r[key]) for r in items[t]}=={r[key] for r in rows}, f"Invalid keys {t}"
ids={p["project_id"] for p in items["projects"]}
assert len(ids)==60
assert len(items["tasks"])==360 and len(items["financials"])==240
assert len(items["employees"])==48 and len(items["timesheets"])==240
for t in ("tasks","financials","timesheets","actions"):
    assert all(r["project_id"] in ids for r in items[t]), f"Broken project reference in {t}"
employees={e["employee_id"] for e in items["employees"]}
assert all(t["employee_id"] in employees for t in items["timesheets"])
assert sum(p["status"]=="Completed" for p in items["projects"])==15
assert sum(p["status"]=="Delayed" for p in items["projects"])==15
variance=sum(f["actual_cost_inr"]-f["planned_cost_inr"] for f in items["financials"])
assert abs(variance-2679054.29)<0.02
data=json.loads((ROOT/"dashboard"/"data.json").read_text(encoding="utf-8"))
assert len(data["projects"])==60 and len(data["financials"])==240
assert "const DB=" in (ROOT/"dashboard"/"index.html").read_text(encoding="utf-8")
with zipfile.ZipFile(ROOT/"excel"/"OpsConsult_360_Excel_Final_Review.xlsx") as z:
    files=z.namelist()
    ns={"x":"http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    book=ET.fromstring(z.read("xl/workbook.xml"))
    sheets=[r.attrib["name"] for r in book.findall(".//x:sheet",ns)]
    assert len(sheets)>=19
    errors=[]; count=0
    for name in files:
        if name.startswith("xl/worksheets/sheet") and name.endswith(".xml"):
            root=ET.fromstring(z.read(name))
            count+=len(root.findall(".//x:f",ns))
            errors.extend((name,c.attrib["r"]) for c in root.findall(".//x:c",ns) if c.attrib.get("t")=="e")
    assert not errors,errors
    has_pivot=any(n.startswith("xl/pivotTables/") for n in files)
report=f"""# Automated OpsConsult 360 QA — 23 November 2026

**PASS**: relational data, six CSV exports, core KPIs, HTML data payload and workbook structure.

- 60 projects (15 completed, 15 delayed); 360 tasks; 240 financial records; 48 employees; 240 timesheets; {len(items['actions'])} actions.
- Primary IDs match across SQLite and CSV; foreign keys resolve.
- Recorded-period unfavorable cost variance: ₹{variance:,.2f}.
- Excel: {len(sheets)} worksheets, {count} formulas, zero cached worksheet formula-error cells.
- Native Excel PivotTables found: **{"Yes" if has_pivot else "No"}**.

**Not proven by this test:** live Excel recalculation and PivotTable interactions, full browser accessibility, or a native Power BI report. The GitHub HTML is regenerated from SQLite and may look different from the previously tested local dashboard.
"""
(ROOT/"docs"/"AUTOMATED_QA.md").write_text(report,encoding="utf-8")
print(report)
