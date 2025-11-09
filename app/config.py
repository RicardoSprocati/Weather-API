import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")

OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@localhost:5432/weather"
)

if not OPENWEATHER_API_KEY:
    print("[AVISO] OPENWEATHER_API_KEY não definida.")