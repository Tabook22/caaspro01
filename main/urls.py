from django.urls import path
from .views import (
    home,
    create,
     index
     )
app_name="main"
urlpatterns = [
    path('',home, name=('home')),
    path("create/", create, name="index"),
    path("<int:id>", index, name="index"),
]
