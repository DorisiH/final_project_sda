from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_nr = models.CharField(max_length=20, null=False, blank=False)
    addres = models.CharField(max_length=50, null=False, blank=False)
    addres2 = models.CharField(max_length=50, null=True, blank=True)
    addres3 = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.username