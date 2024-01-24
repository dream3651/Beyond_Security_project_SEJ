from django.conf import settings
from django.template.context_processors import static
from django.urls import path, re_path
from django.conf.urls.static import static  # 추가된 import 문
from videos.views import index1, next_page1, upload_video1, news, reference

urlpatterns = [
    path('', index1, name='index1'),
    path('reference/', reference, name='reference'),
    path('news/', news, name='news'),
    path('next1/', next_page1, name='next_page1'),
    path('upload1/', upload_video1, name='upload_video1'),
    path('next1/<path:video_url>/', next_page1, name='next_page1')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)