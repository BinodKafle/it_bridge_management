from rest_framework.viewsets import ModelViewSet

from ..models import Teacher
from ..serializers import TeacherSerializer


class TeacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()