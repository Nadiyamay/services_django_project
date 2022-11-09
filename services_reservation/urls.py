"""services_reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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


from django.urls import path, re_path
from django.urls.conf import include
from rest_framework.urlpatterns import format_suffix_patterns
from service_app import views



urlpatterns = [
    path('clients/', views.clients_list),
    path('clients/<int:pk>', views.clients_detail),
    path('services/', views.services_list),
    path('services/<int:pk>', views.services_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)