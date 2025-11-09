from sqlalchemy import Column, Integer, Float, DateTime, String, func
from .db import Base

class WeatherReading(Base):

    __tablename__ = "weather_readings"

    id = Column(Integer, primary_key=True)

    city = Column(String(80), index=True, nullable=False)

    country = Column(String(10), index=True, nullable=True)

    temp = Column(Float, nullable=True)

    temp_min = Column(Float, nullable=True)

    temp_max = Column(Float, nullable=True)

    observed_at = Column(DateTime(timezone=True), nullable=True)

    collected_at = Column(DateTime(timezone=True), server_default=func.now())