from django.urls import path
from .views import (upload, upload_list,upload_file)

app_name="peertotur"
urlpatterns = [ 
    path('upload/',upload, name="upload"),
    path('upload_list/',upload_list, name="upload_list"),
    path('upload_file/',upload_file, name="upload_file"),
]
