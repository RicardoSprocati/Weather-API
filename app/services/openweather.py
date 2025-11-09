import requests
from ..config import OPENWEATHER_API_KEY, OPENWEATHER_BASE_URL

def fetch_weather(city:str) -> dict:

    if not OPENWEATHER_API_KEY:
        raise RuntimeError("OPENWEATHER_API_KEY ausente")
    
    params = {
        "q": city,             
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",      
        "lang": "pt_br",       
    }

    resp = requests.get(OPENWEATHER_BASE_URL, params=params, timeout=15)

    resp.raise_for_status()

    return resp.json()