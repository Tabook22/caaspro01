from django.urls import path
from .views import (upload, upload_list,upload_file, uploadfilelst)
from django.conf import settings
from django.conf.urls.static import static

app_name="peertotur"
urlpatterns = [ 
    path('upload/',upload, name="upload"),
    path('upload_list/',upload_list, name="upload_list"),
    path('class/filelst/', uploadfilelst.as_view(),name='filelsts'),
    path('upload_file/',upload_file, name="upload_file"),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)