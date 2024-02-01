from rest_framework.decorators import action
from rest_framework import (
    viewsets,
    status,
    response,
)

from .models import Shipment
from .serializers import (
    TraceSerializer,
    ShipmentSerializer,
)


class ShipmentModelViewSet(viewsets.ViewSet):
    queryset = Shipment.objects.all()

    def get_serializer_class(self):
        if self.action == 'track':
            return TraceSerializer
        return ShipmentSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    @action(detail=False, methods=['post'])
    def track(self, request):
        track_serializer = self.get_serializer(data=request.data, context={"request": request})
        if track_serializer.is_valid(raise_exception=True):
            tracking_number = track_serializer.validated_data["tracking_number"]
            try:
                shipment = self.queryset.get(tracking_number=tracking_number)     # tracking_number is unique
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
