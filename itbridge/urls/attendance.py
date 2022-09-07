from rest_framework.routers import DefaultRouter
from ..views import CheckInView

router = DefaultRouter(trailing_slash=False)

router.register("attendance/check-in", CheckInView, basename="check-in")

urlpatterns = router.urls
