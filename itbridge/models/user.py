import time
from django.db import models

from shared.models import Base


def get_upload_path(user, filename):
    return f"profile-pic/{int(time.time())}/{filename}"


class User(Base):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, null=True)
    image = models.ImageField(null=True, upload_to=get_upload_path)

    def __str__(self):
        return self.email
