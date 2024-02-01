from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    ShipmentModelViewSet,
)

router = DefaultRouter(trailing_slash=False)
router.register('shipments', ShipmentModelViewSet, basename='shipments')


app_name = "shipment"
urlpatterns = [
    path('', include(router.urls))
]
