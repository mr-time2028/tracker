from django.urls import reverse

from rest_framework.test import (
    APITestCase,
    APIClient,
)

from dashboard.models import (
    Sender,
    Receiver,
    Carrier,
)
from shipment.models import Shipment
from article.models import Article
from .utils import create_address_obj


class TrackShipmentAPITest(APITestCase):
    def setUp(self) -> None:
        self.track_shipment_path = reverse("shipment:shipments-track")
        self.client = APIClient()

        self.sender_address = create_address_obj("Street 1, 10115 Berlin, Germany")
        self.receiver_address = create_address_obj("Street 10, 75001 Paris, France")

        self.carrier = Carrier.objects.create(name="DHL")
        self.sender = Sender.objects.create(address=self.sender_address)
        self.receiver = Receiver.objects.create(address=self.receiver_address)
        self.article = Article.objects.create(
            name="Laptop",
            sku="LP123",
            price=800,
            quantity=1,
        )

        self.tracking_number = "TN12345678"
        self.shipment = Shipment.objects.create(
            tracking_number=self.tracking_number,
            carrier=self.carrier,
            receiver=self.receiver,
            sender=self.sender,
            article=self.article,
            status="it",
        ),

    def test_valid_tracking_number(self):
        data = {"tracking_number": self.tracking_number}
        response = self.client.post(path=self.track_shipment_path, data=data)

        self.assertEqual(response.status_code, 200)

    def test_bad_length_tracking_number(self):
        data = {"tracking_number": self.tracking_number+"somethingwrong"}
        response = self.client.post(path=self.track_shipment_path, data=data)

        self.assertEqual(response.status_code, 400)

    def test_invalid_tracking_number(self):
        data = {"tracking_number": "wrongtrack"}
        response = self.client.post(path=self.track_shipment_path, data=data)

        self.assertEqual(response.status_code, 404)
