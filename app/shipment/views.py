from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework import (
    viewsets,
    status,
    response,
)

from .models import Shipment
from .serializers import (
    TrackSerializer,
    ShipmentSerializer,
)


class ShipmentModelViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    def list(self, request):
        raise MethodNotAllowed("get", code=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, methods=['post'])
    def track(self, request):
        track_serializer = TrackSerializer(data=request.data, context={"request": request})
        if track_serializer.is_valid(raise_exception=True):
            tracking_number = track_serializer.validated_data["tracking_number"]
            try:
                shipment = self.queryset.get(tracking_number=tracking_number)
                shipment_serializer = ShipmentSerializer(instance=shipment, context={"request": request})
                return response.Response({
                    "error": False,
                    "data": shipment_serializer.data,
                }, status=status.HTTP_200_OK)
            except Shipment.DoesNotExist:
                return response.Response({
                    "error": True,
                    "detail": "There is no shipment with this tracking number!"
                }, status=status.HTTP_404_NOT_FOUND)
        return response.Response({
            "error": True,
            "detail": track_serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)
