from django.db import models

from shared.models import Base


class User(Base):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, null=True)
    image = models.ImageField(max_length=255, null=True)

    def __str__(self):
        return self.email
