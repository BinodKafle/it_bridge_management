from rest_framework.routers import DefaultRouter

from ..views.holiday import HolidayViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r"holiday", HolidayViewSet, basename="holiday")

urlpatterns = router.urls

