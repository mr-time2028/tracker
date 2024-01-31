from django.db import models

from dashboard.models import (
    Sender,
    Receiver,
    Carrier,
)
from article.models import Article


class Shipment(models.Model):
    IN_TRANSIT = 'it'
    TRANSIT = 't'
    IN_BOUNDED_SCAN = 'is'
    SCANNED = 's'
    IN_DELIVERY = 'id'
    DELIVERY = 'd'

    STATUS_CHOICES = (
        (IN_TRANSIT, 'in-transit'),
        (TRANSIT, 'transit'),
        (IN_BOUNDED_SCAN, 'inbounded-scan'),
        (SCANNED, 'scanned'),
        (IN_DELIVERY, 'in-delivery'),
        (DELIVERY, 'delivery'),
    )

    tracking_number = models.CharField(max_length=10, unique=True)
    sender = models.OneToOneField(Sender, on_delete=models.CASCADE, related_name="shipment_sender")
    receiver = models.OneToOneField(Receiver, on_delete=models.CASCADE, related_name="shipment_receiver")
    carrier = models.OneToOneField(Carrier, on_delete=models.CASCADE, related_name="shipment_carrier")
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name="shipment_article")
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tracking_number} > {self.sender} --> {self.receiver} | {self.carrier}"
