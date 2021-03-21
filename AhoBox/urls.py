from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('test', views.test, name='test'),
    path('AnimeDetails', views.animeDetails, name='animeDetails')
]