from django.contrib import admin
from django.urls import path,include
from .views import (peer_reg, peer_reg_list)

app_name="attendance"


urlpatterns = [ 
    path('', peer_reg.as_view(),name='peer_reg'),
    path('peer_reg_list', peer_reg_list.as_view(), name='peer_reg_list')
   
]