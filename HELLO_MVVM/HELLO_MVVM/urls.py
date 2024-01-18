"""
URL configuration for HELLO_MVVM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from HELLO_MVVM import views

urlpatterns = [
    path('ajax', views.ajax),
    path('select_list', views.select_list),
    path('select_one', views.select_one),
    path('insert', views.insert),
    path('update', views.update),
    path('delete', views.delete),
]
