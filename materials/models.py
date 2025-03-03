import uuid
from django.db import models

from colors.models import ColorType
from sizes.models import SizeType

class Material(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Material Name")
    color = models.ForeignKey(ColorType, on_delete=models.CASCADE, related_name="color")
    size = models.ForeignKey(SizeType, on_delete=models.CASCADE, related_name="size")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
