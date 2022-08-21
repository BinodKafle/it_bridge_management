from django.db import models
from django.utils import timezone
from .managers import BaseManager

class Base(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    deleted_at = models.DateTimeField(editable=False, null=True)

    objects = BaseManager()
    all_objects = BaseManager(alive_only=False)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(Base, self).delete()
