from django.contrib import admin
from django.urls import path,include
from .views import peer_reg
urlpatterns = [ 
    path('', peer_reg.as_view(),name='peer_reg')
   
]