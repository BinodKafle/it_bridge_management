from django.db import models

from itbridge.models import User
from shared.models import Base


class Attendance(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendance", null=False)
    check_in = models.DateTimeField(null=True)
    check_out = models.DateTimeField(null=True)
    status = models.CharField(max_length=45, null=True)

    def __str__(self):
        return f"{self.user}, check-in: {self.check_in}"
