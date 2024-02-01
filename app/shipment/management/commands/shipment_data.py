import json
import os

from django.core.management.base import BaseCommand

from shipment.models import Shipment
from dashboard.models import (
    Carrier,
    Sender,
    Receiver,
)
from article.models import Article
from shipment.utils import create_address_obj


class Command(BaseCommand):
    help = 'Import shipment data from JSON file'

    def handle(self, *args, **options):
        file_path = os.getcwd() + '/shipment/data.json'

        with open(file_path, 'r') as jsonfile:
            data = json.load(jsonfile)
            for item in data:
                sender_address_obj = create_address_obj(item["sender_address"])
                receiver_address_obj = create_address_obj(item["receiver_address"])

                carrier = Carrier.objects.create(name=item["carrier"])
                sender = Sender.objects.create(address=sender_address_obj)
                receiver = Receiver.objects.create(address=receiver_address_obj)
                article = Article.objects.create(
                    name=item["article_name"],
                    sku=item["SKU"],
                    price=item["article_price"],
                    quantity=item["article_quantity"],
                )

                status_mapping = {
                    "in-transit": Shipment.IN_TRANSIT,
                    "transit": Shipment.TRANSIT,
                    "inbounded-scan": Shipment.IN_BOUNDED_SCAN,
                    "scanned": Shipment.SCANNED,
                    "in-delivery": Shipment.IN_DELIVERY,
                    "delivery": Shipment.DELIVERY,
                }

                Shipment.objects.create(
                    tracking_number=item['tracking_number'],
                    carrier=carrier,
                    receiver=receiver,
                    sender=sender,
                    article=article,
                    status=status_mapping.get(item["status"], Shipment.IN_TRANSIT),     # Default to IN_TRANSIT
                )

        self.stdout.write(self.style.SUCCESS('Data import completed successfully.'))
