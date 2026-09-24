from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.config import settings
import os

app = FastAPI(title="Proyek Chatme Cevin", openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.include_router(api_router, prefix=settings.API_V1_STR)