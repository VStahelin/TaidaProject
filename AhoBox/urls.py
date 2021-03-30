from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('test', views.test, name='test'),
    path('AnimeDetails', views.animeDetails, name='animeDetails'),
    path('Search', views.search, name='search'),
    path('CreateList', views.createList, name='createList'),
    path('Lists', views.lists, name='lists'),
    path('ListDetails', views.listDetails, name='listDetails'),
]