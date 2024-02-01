import requests

from django.conf import settings

from dashboard.models import Address


# get_weather function receive address objects and fetch the weather condition using OpenWeatherMap API
# https://openweathermap.org/current
def get_weather(address: Address) -> dict:
    response = requests.get(
        url=f"https://api.openweathermap.org/data/2.5/weather?q={address.city}&appid={settings.OPEN_WEATHER_MAP_API_KEY}"
    )
    parsed_response = response.json()

    try:
        weather_info = parsed_response["weather"]
        temp_info = parsed_response["main"]

        result = {
            "main": weather_info[0]["main"],
            "description": weather_info[0]["description"],
            "temperature": f'{temp_info["temp"]} Kelvin',
        }

        return result

    except Exception as e:
        print(e)
        return {}
