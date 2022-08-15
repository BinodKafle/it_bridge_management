from rest_framework.routers import DefaultRouter

from ..views.student import StudentViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r"students", StudentViewSet, basename="student")

urlpatterns = router.urls

