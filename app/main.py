"""Main application entry point."""

import uvicorn
from fastapi import FastAPI

from app import routers

app = FastAPI(
    title="ss-sample-python-api test",
    description="Sample Python API test Test.",
    version="v1",
)

app.include_router(routers.main.router)


if __name__ == "__main__":
    # Debug-only configuration
    uvicorn.run(app)
