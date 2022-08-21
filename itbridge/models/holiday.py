from django.db import models

from shared.models import Base


class Holiday(Base):
    name = models.CharField(max_length=100)
    from_date = models.DateField(null=False)
    to_date = models.DateField(null=False)

    def __str__(self):
        return self.name
