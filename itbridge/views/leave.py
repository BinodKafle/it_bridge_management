from rest_framework.viewsets import ModelViewSet

from ..models import Leave
from ..serializers import LeaveSerializer


class LeaveViewSet(ModelViewSet):
    serializer_class = LeaveSerializer
    queryset = Leave.objects.all()
