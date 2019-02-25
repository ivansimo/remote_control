from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='grupos'),
    path('<int:grupo_id>', views.grupo, name='grupo'),
    path('search', views.search, name='search'),
]