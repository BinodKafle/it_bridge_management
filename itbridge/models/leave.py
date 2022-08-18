from django.db import models

from .user import User

from shared.models import Base


class Leave(Base):

            users = models.ForeignKey(User, Null=False, on_delete=models.CASCADE, related_name="user_leave")
            from_date = models.DateTimeField()
            to_date = models.DateTimeField()
            stat = (('Pending', 'Pending'), ('Approved', 'Approved'), ('Cancelled', 'Cancelled'))
            status = models.CharField(max_length=50, choices=stat, default='Pending', null=True)
            type = models.CharField(max_length=100)
            reason_text = models.CharField(max_length=100)

            def __str__(self):
                return self.email




