from .programming_language import urlpatterns as programming_language_urls
from .teacher import urlpatterns as teacher_urls
from .user import urlpatterns as user_urls

urlpatterns = []

urlpatterns += programming_language_urls
urlpatterns += teacher_urls
urlpatterns += user_urls
