from contextlib import asynccontextmanager
import os
from pathlib import Path

from fastapi import FastAPI, Request, Query, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app.services.openweather import fetch_weather

from .db import Base, engine, get_db
from .routers import weather
from . import repositories as repo
from . import models

BASE_DIR = Path(__file__).parent                 
TEMPLATES_DIR = BASE_DIR / "templates"          
ASSETS_DIR = TEMPLATES_DIR / "assets"           

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title="Weather Minimal API",
    description="Consome apenas temp, temp_min e temp_max da OpenWeather.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(weather.router)

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/assets", StaticFiles(directory=str(ASSETS_DIR)), name="assets")

@app.get("/", include_in_schema=False)
def home(
    request: Request,
    city: str | None = Query(None, description="Ex.: Florianopolis,BR"),
    db: Session = Depends(get_db),
):
    target_city = city or os.getenv("DEFAULT_CITY", "Florianopolis,BR")

    try:
        payload = fetch_weather(target_city)
    except Exception as e:
        return templates.TemplateResponse(
            "home.html",
            {"request": request, "reading": None, "api_url": None, "error": f"Falha na OpenWeather: {e}"},
            status_code=502,
        )

    saved = repo.create_reading(db, city=target_city, payload=payload)

    base = str(request.base_url).rstrip("/")
    api_url = f"{base}/weather"

    return templates.TemplateResponse(
        "home.html",
        {"request": request, "reading": saved, "api_url": api_url, "error": None},
    )
