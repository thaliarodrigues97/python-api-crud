from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yaml
from src.infrastructure.api.product_controller import router

def run_app():
    yaml_path = Path("src/infrastructure/openapi/openapi.yaml")
    with open(yaml_path, "r", encoding="utf-8") as f:
        openapi_schema = yaml.safe_load(f)

    app = FastAPI(
        title="Hexagonal FastAPI Example",
        description="Exemplo de API em Python",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    app.openapi = lambda: openapi_schema

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router, prefix="/api", tags=["Products"])
    return app