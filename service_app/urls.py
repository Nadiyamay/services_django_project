from django.apps import AppConfig
from django.urls import re_path
from .views import ListView
urlpatterns = [
  re_path(r'^\/(?P<api_name>[a-z]+)\/$', ListView, name=None),
]


# from django.apps import AppConfig
# from django.urls import path
# from .views import ListView
# urlpatterns = [
#   path(r'^(?P<api_name>[a-z]+)', ListView, name=None),
#   path(r'^(?P<api_name>[a-z]+)', ListView, name=None),
#   path(r'^(?P<api_name>[a-z]+)', ListView, name=None),
# ]
