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
                    peertotur_exp_list,
                    peertoturexp_update,
                    peertoturexp_delete,
                    document_detail)
from django.conf import settings
from django.conf.urls.static import static

app_name = "peertotur"
urlpatterns = [
    path('upload/', upload, name="upload"),
    path('upload_list/', upload_list, name="upload_list"),
    path('addpeertotur/', add_peertotur.as_view(), name="add_peertotur"),
    path('document_detail', document_detail.as_view(), name="document_detail"),
    path('peertotur_experties', peertotur_experties.as_view(),
         name='peertotur_experties'),
    path('peertotur_exp_list/', peertotur_exp_list.as_view(),
         name="peertotur_exp_list"),
    path('peertotur_list', peertotur_list.as_view(), name="peertotur_list"),
    path('peertotur_detail/<int:id>/',
         peertotur_detail.as_view(), name="peertotur_detail"),
    path('peertotur_delete/<int:pk>',
         peertotur_delete.as_view(), name="peertotur_delete"),
    path('peertoturexp_delete/<int:pk>',
         peertoturexp_delete.as_view(), name="peertoturexp_delete"),
    path('peertotur_update/<int:id>/',
         peertotur_update.as_view(), name='peertotur_update'),
    path('peertoturexp_update/<int:id>/',
         peertoturexp_update.as_view(), name='peertoturexp_update'),
    path('upload_delete/<int:pk>', upload_delete, name="upload_delete"),
    path('class/filelst/', uploadfilelst.as_view(), name='filelsts'),
    path('class/fileupload/', uploadfiles.as_view(), name='class_fileupload'),
    path('upload_file/', upload_file, name="upload_file"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
