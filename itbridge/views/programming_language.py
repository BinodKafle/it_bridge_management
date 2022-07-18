from rest_framework.viewsets import ModelViewSet

from ..models import ProgrammingLanguage
from ..serializers import ProgrammingLanguageSerializer


class ProgrammingLanguageViewSet(ModelViewSet):
    serializer_class = ProgrammingLanguageSerializer
    queryset = ProgrammingLanguage.objects.all()
