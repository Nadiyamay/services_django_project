
from django.urls import re_path, path, include
from . import views


urlpatterns = [
    re_path(r'^clients/$', views.clients_list),
    re_path(r'^clients/(?P<pk>[0-9]+)/$', views.clients_detail),
]

