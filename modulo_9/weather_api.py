# weather_api.py

import requests # type: ignore
from config import OPENWEATHER_API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str):
    """Faz requisição à API do OpenWeatherMap para obter dados do clima."""
    try:
        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "lang": "pt_br",
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()  # gera erro se status != 200

        data = response.json()

        weather_info = {
            "cidade": data["name"],
            "temperatura": data["main"]["temp"],
            "condicoes": data["weather"][0]["description"],
            "sensacao": data["main"]["feels_like"]
        }

        return weather_info

    except requests.exceptions.Timeout:
        return {"erro": "A requisição demorou muito tempo e foi cancelada."}

    except requests.exceptions.ConnectionError:
        return {"erro": "Falha na conexão. Verifique sua internet."}

    except requests.exceptions.HTTPError:
        return {"erro": f"Erro HTTP: {response.status_code} - {response.reason}"}

    except Exception as e:
        return {"erro": f"Ocorreu um erro inesperado: {e}"}
