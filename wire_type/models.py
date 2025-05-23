import uuid
from django.db import models

# Create your models here.
class wireType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Beads Type")

    def __str__(self):
        return self.name