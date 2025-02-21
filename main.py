import uvicorn
from fastapi import FastAPI

from endpoints import report_router

app = FastAPI(openapi_prefix="/api/v1")

app.include_router(report_router)


if __name__ == "__main__":
    uvicorn.run(app, port=9000)
