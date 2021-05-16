from django.urls import path

from . import views

urlpatterns = [
    path('CreateList', views.createList, name='createList'),
    path('Lists', views.lists, name='lists'),
    path('ListDetails', views.listDetails, name='listDetails')
]
