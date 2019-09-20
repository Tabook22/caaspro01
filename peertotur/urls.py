from django.urls import path
from .views import (upload, 
                    upload_delete, 
                    upload_list, 
                    upload_file,
                    uploadfilelst, 
                    uploadfiles, 
                    add_peertotur,
                    peertotur_list,
                    peertotur_delete,
                    peertotur_update,
                    peertotur_detail,
                    peertotur_experties,
                    peertotur_exp_list)
from django.conf import settings
from django.conf.urls.static import static

app_name = "peertotur"
urlpatterns = [
    path('upload/', upload, name="upload"),
    path('upload_list/', upload_list, name="upload_list"),
    path('addpeertotur/', add_peertotur.as_view(), name="add_peertotur"),
    path('peertotur_experties', peertotur_experties.as_view(), name='peertotur_experties'),
    path('peertotur_exp_list/', peertotur_exp_list.as_view(), name="peertotur_exp_list"),
    path('peertotur_list', peertotur_list.as_view(), name="peertotur_list"),
    path('peertotur_detail/<int:id>/', peertotur_detail.as_view(), name="peertotur_detail"),
    path('peertotur_delete/<int:pk>', peertotur_delete.as_view(), name="peertotur_delete"),
    path('peertotur_update/<int:id>/', peertotur_update.as_view(), name='peertotur_update'),
    path('upload_delete/<int:pk>', upload_delete, name="upload_delete"),
    path('class/filelst/', uploadfilelst.as_view(), name='filelsts'),
    path('class/fileupload/', uploadfiles.as_view(), name='class_fileupload'),
    path('upload_file/', upload_file, name="upload_file"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
