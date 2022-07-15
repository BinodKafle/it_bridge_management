from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    deleted_at = models.DateTimeField(editable=False, null=True)
