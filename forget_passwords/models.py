# models.py
from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils import timezone
import random
import string

class PasswordResetRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    reset_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def generate_reset_code(self):
        """ Generate a 6-digit reset code. """
        self.reset_code = ''.join(random.choices(string.digits, k=6))
        self.expires_at = timezone.now() + timezone.timedelta(minutes=10)  # 10 minutes expiry

    def save(self, *args, **kwargs):
        """ Override save method to generate reset code. """
        if not self.reset_code:
            self.generate_reset_code()
        super().save(*args, **kwargs)
