import uuid
from django.db import models

class SizeType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Size Name")

    def __str__(self):
        return self.name