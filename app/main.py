from fastapi import FastAPI
from .routes import router

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="devops-app", version="1.1.0")
app.include_router(router)

# Expose /metrics + default HTTP metrics
Instrumentator().instrument(app).expose(app, endpoint="/metrics")
