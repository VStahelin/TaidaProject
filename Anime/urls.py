from django.urls import path

from . import views

urlpatterns = [
    path('AnimeDetails/<int:mal_id>', views.animeDetails, name='animeDetails'),
]