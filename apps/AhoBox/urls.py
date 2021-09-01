from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Search', views.search, name='search'),
]