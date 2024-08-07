"""
URL configuration for anshprivate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from feedback import views

urlpatterns = [
    path('a/', admin.site.urls),
    path('',views.index,name="index"),
    path('aboutus/',views.about,name="about"),
    path('booking/',views.booking,name="booking"),
    path('gallary/',views.gallary,name="gallary"),
    path('reviews/',views.review,name="review"),
    path('room/',views.room,name="room"),
    path('services/',views.services,name="services"),
]

