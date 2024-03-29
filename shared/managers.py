from django.db import models
from django.utils import timezone
from django.db.models.query import QuerySet


class BaseQuerySet(QuerySet):
    def delete(self):
        return super(BaseQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        return super(BaseQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)


class BaseManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop("alive_only", True)
        self._get_queryset_class = BaseQuerySet
        super(BaseManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        qs = super(BaseManager, self).get_queryset()
        if self.alive_only:
            return qs.filter(deleted_at=None)
        return qs

