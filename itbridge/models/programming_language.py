from django.db import models

from shared.models import Base


class ProgrammingLanguage(Base):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name
