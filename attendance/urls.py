from django.contrib import admin
from django.urls import path,include
from .views import (
    attendance_add, attendance_list,
    attendance_detail,
    attendance_delete)

app_name="attendance"


urlpatterns = [ 
    path('attendance_add/', attendance_add.as_view(),name='attendance_add'),
    path('attendance_list/', attendance_list.as_view(), name='attendance_list'),
    path('attendance_detail/<int:id>/', attendance_detail.as_view(),name='attendance_detail'),
    path('attendance_delete/<int:pk>/', attendance_delete.as_view(),name='attendance_delete')
   
]