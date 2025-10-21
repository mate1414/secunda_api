from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import buildings, organizations, activities
from app.database import engine
from app.models import base

base.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="REST API для справочника организаций",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)