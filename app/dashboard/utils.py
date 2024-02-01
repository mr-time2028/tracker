import json
import requests
from requests.exceptions import RequestException

from django.conf import settings
from django.core.cache import cache

from dashboard.models import Address


# get_weather function receive address objects and fetch the weather condition using OpenWeatherMap API
# https://openweathermap.org/current
def get_weather(address: Address) -> dict:
    cached_weather = cache.get(address.id)

    if not cached_weather:
        try:
            response = requests.get(
                url=f"https://api.openweathermap.org/data/2.5/weather?q={address.city}&appid={settings.OPEN_WEATHER_MAP_API_KEY}"
            )
            weather = response.json()
            cache.set(address.id, json.dumps(weather), timeout=settings.WEATHER_DATA_CACHE_TIME)
        except RequestException as e:
            print(e)
            return {}
    else:
        weather = json.loads(cached_weather)

    try:
        weather_info = weather["weather"]
        temp_info = weather["main"]

        result = {
            "main": weather_info[0]["main"],
            "description": weather_info[0]["description"],
            "temperature": f'{temp_info["temp"]} Kelvin',
        }

        return result

    except Exception as e:
        print(e)
        return {}
