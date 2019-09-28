"""caas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [ 
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('peertoturs/',include('peertotur.urls')),
    path('attendance/', include('attendance.urls')),
    path('', include("django.contrib.auth.urls")),
]
# the idea here is to be able to display media file in the development environment, usuallyu in the 
# propduciton environement ngix will handle displying the media files
#this means if the settings is in the DEBUG mode, which means we are in the development
# this is only for development purpose we shouldn't use it in the production environment
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
