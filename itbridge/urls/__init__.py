from .programming_language import urlpatterns as programming_language_urls

from .user import urlpatterns as user_urls

urlpatterns = []

urlpatterns += programming_language_urls
urlpatterns += user_urls
