from django.contrib import admin

from .models import (
    Sender,
    Receiver,
    Carrier,
)


@admin.register(Sender)
class SenderAdmin(admin.ModelAdmin):
    pass


@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
    pass


@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    pass
