from pydantic import BaseModel, ConfigDict

class TempsOut(BaseModel):
    temp: float | None = None
    temp_min: float | None = None
    temp_max: float | None = None
    model_config = ConfigDict(from_attributes=True)
