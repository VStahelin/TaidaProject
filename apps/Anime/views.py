import ast

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from jikanpy import Jikan

from Anime.api.manager import insertAnime
from Anime.models import Anime


@login_required(login_url='login')
def animeDetails(request, mal_id):
    if not Anime.objects.filter(mal_id=mal_id).exists():
        jikan = Jikan()
        anime = jikan.anime(mal_id)
        insertAnime(anime)

    anime = Anime.objects.get(mal_id=mal_id)
    studios = ''
    anime.titles = ast.literal_eval(anime.titles)

    for a in anime.studios.all():
        studios = a.name

    genres = []
    for b in anime.genres.all():
        genres.append(b.__dict__)
    print(genres)
    return render(request, 'anime/AnimeDetails.html', {'anime': anime, 'studios': studios, 'genres': genres})
