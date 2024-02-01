from rest_framework import serializers

from .models import Shipment
from article.models import Article


class TrackSerializer(serializers.Serializer):
    tracking_number = serializers.CharField(max_length=10)

    class Meta:
        fields = ('tracking_number',)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("name", "sku", "price", "quantity")


class ShipmentSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.address')
    receiver = serializers.CharField(source='receiver.address')
    carrier = serializers.CharField(source='carrier.name')
    article = ArticleSerializer(read_only=True)
    status = serializers.SerializerMethodField("get_status")

    class Meta:
        model = Shipment
        fields = ('tracking_number', 'sender', 'receiver', 'carrier', 'article', 'status', 'created_at', 'updated_at',)

    def get_status(self, obj):
        return obj.get_status_display()
