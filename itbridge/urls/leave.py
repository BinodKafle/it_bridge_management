from rest_framework.routers import DefaultRouter

from ..views import LeaveViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r"leaves", LeaveViewSet, basename="leave")

urlpatterns = router.urls
