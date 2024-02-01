from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=10, unique=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.sku}"
