from django.urls import path
from .views import upload

app_name="peertotur"
urlpatterns = [ 
    path('',upload, name="upload"),
]
