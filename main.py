from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import run_app
import yaml
from src.infrastructure.api.product_controller import router
yaml_path = Path("src/infrastructure/openapi/openapi.yaml")

app = run_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )