from .programming_language import urlpatterns as programming_language_urls

from .student import urlpatterns as student_urls

urlpatterns = []

urlpatterns += programming_language_urls

urlpatterns += student_urls
