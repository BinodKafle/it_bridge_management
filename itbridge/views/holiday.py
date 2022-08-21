from rest_framework.viewsets import ModelViewSet

from ..models import Holiday
from ..serializers import HolidaySerializer


class HolidayViewSet(ModelViewSet):
    serializer_class = HolidaySerializer
    queryset = Holiday.objects.all()
