import uuid
from django.db import models
from materials.models import Material

class PurchaseMaterial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material = models.CharField(verbose_name="Material", max_length=255, default="")
    quantity = models.IntegerField(verbose_name="Quantity", default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    color = models.CharField(verbose_name="Color", max_length=255)
    size = models.CharField(verbose_name="Size", max_length=255)
    type = models.CharField(verbose_name="Type", max_length=255, default="")
    date = models.DateField(auto_now_add=True, verbose_name="Date")

    def __str__(self):
        return f"{self.material.name} - {self.color} - {self.size}"
