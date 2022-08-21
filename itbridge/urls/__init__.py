from .programming_language import urlpatterns as programming_language_urls
from .teacher import urlpatterns as teacher_urls
from .user import urlpatterns as user_urls
from .student import urlpatterns as student_urls
from .holiday import urlpatterns as holiday_urls

urlpatterns = []

urlpatterns += programming_language_urls
urlpatterns += teacher_urls
urlpatterns += user_urls
urlpatterns += student_urls
urlpatterns += holiday_urls
