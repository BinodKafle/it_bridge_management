from rest_framework.routers import DefaultRouter

from ..views import ProgrammingLanguageViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r"programming-language", ProgrammingLanguageViewSet, basename="programming-language")

urlpatterns = router.urls
