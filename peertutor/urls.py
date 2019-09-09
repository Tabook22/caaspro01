from django.urls import path
from .views import showfile
app_name="peertutor"
urlpatterns = [ 
    path('',showfile, name="showfile"),
]
