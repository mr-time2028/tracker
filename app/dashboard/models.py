import uuid

from django.db import models


# class Address(models.Model):
#     country = models.CharField(max_length=90)
#     city = models.CharField(max_length=189)
#     street = models.TextField()
#     house_no = models.CharField(max_length=10)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.country}, {self.city} {self.street}, {self.house_no}"


class Sender(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    # user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='sender_user')
    # address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, related_name="sender_address")
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.address}"


class Receiver(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    # user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='receiver_user')
    # address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, related_name="receiver_address")
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.address}"


class Carrier(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    # user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='carrier_user')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
