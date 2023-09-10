from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    CHOICE_ROLES = (
        (1, 'admin'),
        (2, 'user')
    )
    role = models.PositiveSmallIntegerField(default=2, choices=CHOICE_ROLES)
    phone = models.CharField(default='', max_length=15)
