from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models import BooleanField, CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from app_modules.core_apps.base.models import BaseModel

# Create your models here.
class User(AbstractUser, BaseModel):
    def __str__(self):
        return self.email
