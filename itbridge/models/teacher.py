from django.db import models

from .user import User
from .programming_language import ProgrammingLanguage
from .leave import Leave
from shared.models import Base


class Teacher(Base):
    users = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="user_teacher")
    programming_language = models.ForeignKey(
        ProgrammingLanguage, null=False, on_delete=models.CASCADE, related_name="teacher_programming_language")
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def __str__(self):
        return self.users.email
