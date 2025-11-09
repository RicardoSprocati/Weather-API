from datetime import datetime, timezone
from sqlalchemy.orm import Session
from .models import WeatherReading


def create_reading(db:Session, city, payload: dict) -> WeatherReading:
    main = (payload or {}).get("main") or {}

    sys  = (payload or {}).get("sys")  or {} 

    dt_epoch = (payload or {}).get("dt")

    observed_at = datetime.fromtimestamp(dt_epoch, tz=timezone.utc) if dt_epoch else None

    reading = WeatherReading(
        city = payload.get("name") or city,
        country  = sys.get("country"),
        temp = main.get("temp"),
        temp_min = main.get("temp_min"),
        temp_max = main.get("temp_max"),
        observed_at = observed_at,   
    )

    db.add(reading)
    db.commit()
    db.refresh(reading)
    return reading

def List_readings(db: Session, city: str | None = None, limit: int = 20):
    q = db.query(WeatherReading).order_by(WeatherReading.id.desc())

    if city:
        q = q.filter(WeatherReading.city.ilike(f"%{city}%"))

    return q.limit(limit).all()

def get_latest_reading(db: Session, city: str | None = None):
    q = db.query(WeatherReading).order_by(WeatherReading.id.desc())
    if city:
        city_only = city.split(",")[0].strip()
        q = q.filter(WeatherReading.city.ilike(f"%{city_only}%"))
    return q.first()