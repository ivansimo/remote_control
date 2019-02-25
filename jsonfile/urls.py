from django.urls import path

from . import views

urlpatterns = [
    path('jsonfile', views.jsonfile, name='jsonfile'),
]