from rest_framework import (
    serializers,
    response,
    status,
)

from .utils import get_weather
from .models import (
    Sender,
    Receiver,
    Address,
)


class AddressSerializer(serializers.ModelSerializer):
    weather = serializers.SerializerMethodField("get_weather")

    class Meta:
        model = Address
        fields = ("country", "city", "street", "postal_code", "weather")

    def get_weather(self, address):
        return get_weather(address)


class SenderSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Sender
        fields = ("id", "address",)


class ReceiverSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Receiver
        fields = ("id", "address",)
