import json

from fastapi import APIRouter

from schemas import Report


report_router = APIRouter(prefix='/report')
report_router.tags = ["Report"]

REPORTS_FILE = "reports.json"


def save(report: Report):
    with open(REPORTS_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(report.json(), ensure_ascii=False, indent=5) + "\n")


@report_router.post("/", response_model=dict[str, str])
def save_report(report: Report):
    save(report)
    return {"message": "Report saved successfully"}
