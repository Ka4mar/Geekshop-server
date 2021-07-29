from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta, datetime
import pytz


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def is_activation_key_expired(self):
        if datetime.now(pytz.timezone(settings.TIME_ZONE)) < (self.activation_key_created + timedelta(hours=48)):
            return False
        return True


def safe_delete(self):
        self.is_active = False
        self.save()
