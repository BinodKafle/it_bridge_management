from rest_framework import mixins, viewsets
from ..serializers import AttendanceSerializer


class CheckInView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = AttendanceSerializer

