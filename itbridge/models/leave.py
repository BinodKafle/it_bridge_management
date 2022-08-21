from django.db import models

from .user import User

from shared.models import Base


class Leave(Base):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Cancelled', 'Cancelled')
    )
    TYPES = (
        ("Festival", "Festival"),
        ("Sick", "Sick"),
        ("Marriage", "Marriage"),
        ("Mourning", "Mourning")
    )

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="user_leave")
    from_date = models.DateTimeField(null=False)
    to_date = models.DateTimeField(null=False)
    status = models.CharField(max_length=50, null=False, choices=STATUS, default='Pending')
    type = models.CharField(max_length=100, null=False, choices=TYPES)
    reason_text = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.user.name




