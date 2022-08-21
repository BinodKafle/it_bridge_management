from rest_framework.viewsets import ModelViewSet

from ..models import holiday
from ..serializers import HolidaySerializer


class HolidayViewSet(ModelViewSet):
    serializer_class = HolidaySerializer
    queryset = holiday.objects.all()
