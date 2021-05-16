from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Search', views.search, name='search'),
    path('CreateList', views.createList, name='createList'),
    path('Lists', views.lists, name='lists'),
    path('ListDetails', views.listDetails, name='listDetails'),
]