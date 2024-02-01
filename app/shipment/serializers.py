from rest_framework import serializers

from .models import Shipment
from article.serializers import ArticleSerializer
from dashboard.serializers import (
    SenderSerializer,
    ReceiverSerializer,
)


class TraceSerializer(serializers.Serializer):
    tracking_number = serializers.CharField(max_length=10)


class ShipmentSerializer(serializers.ModelSerializer):
    sender = SenderSerializer()
    receiver = ReceiverSerializer()
    carrier = serializers.CharField(source='carrier.name')
    article = ArticleSerializer()
    status = serializers.SerializerMethodField("get_status")

    class Meta:
        model = Shipment
        fields = ('tracking_number', 'sender', 'receiver', 'carrier', 'article', 'status', 'created_at', 'updated_at',)

    def get_status(self, obj):
        return obj.get_status_display()
