from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..schemas import TempsOut
from ..services.openweather import fetch_weather
from .. import repositories

router = APIRouter(prefix="/weather", tags=["weather"])

@router.post("/ingest", response_model=TempsOut)

def  ingest(
    city: str = Query(..., description="Ex.: 'Florianopolis,BR'"),
    db: Session = Depends(get_db)
):
    try:
        payload = fetch_weather(city)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Falha na OpenWeather: {e}")
    reading = repositories.create_reading(db, city=city, payload=payload)
    return reading

@router.get("", response_model=list[TempsOut])
def list_items(
    city: str | None = Query(None),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return repositories.List_readings(db, city=city, limit=limit)
