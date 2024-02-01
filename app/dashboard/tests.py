import json

from django.test import TestCase
from django.core.cache import cache
from django.conf import settings

from dashboard.models import Address
from .utils import get_weather


class TestUtils(TestCase):
    def test_get_weather_with_cached_data(self):
        address = Address(city='Berlin')  # Create an instance of Address with required data
        cached_weather = {
            'weather': [{'main': 'Clear', 'description': 'Clear sky'}],
            'main': {'temp': 290.15}  # Replace with your actual temperature data
        }
        cache.set(address.id, json.dumps(cached_weather), timeout=settings.WEATHER_DATA_CACHE_TIME)

        result = get_weather(address)

        self.assertEqual(result, {
            "main": "Clear",
            "description": "Clear sky",
            "temperature": "290.15 Kelvin",
        })
