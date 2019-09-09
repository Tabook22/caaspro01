from django.urls import path
from .views import (
    home,
    create,
     index,
     view
     )
app_name="main"
urlpatterns = [
    path("<int:id>", index, name="index"),
    path('',home, name=('home')),
    path("home/", home, name="home"),
    path("create/", create, name="create"),
    path("view/", view, name="view"), 
]
