import requests

def get_weather(lat,lon):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    try:
        response = requests.get(url, params = params, timeout = 10)
        response.raise_for_status()
        data = response.json()
        return data["current_weather"]
    except Exception as e:
        return {"error": str(e)}
