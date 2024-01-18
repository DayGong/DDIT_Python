"""
URL configuration for HELLO_MVC project.

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
from django.urls import path
from HELLO_MVC import views

urlpatterns = [
    path('', views.emp_list),
    path('emp_list', views.emp_list),
    path('emp_detail', views.emp_detail),
    path('emp_add', views.emp_add),
    path('emp_add_act', views.emp_add_act),
    path('emp_mod', views.emp_mod),
    path('emp_mod_act', views.emp_mod_act),
    path('emp_del_act', views.emp_del_act),
]
