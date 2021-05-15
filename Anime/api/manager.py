from Anime.models import AnimeCard, Anime
from Genres.manager import insertGenre
from decimal import *
from Genres.models import Genre
from Studio.models import Studio


def generateCardStructure(values_dict):
    animeList = []
    for animeDict in values_dict:
        anime = AnimeCard()
        anime.title = animeDict.get('title')
        anime.mal_id = animeDict.get('mal_id')
        anime.synopsis = animeDict.get('synopsis')
        anime.image_url = animeDict.get('image_url')
        animeList.append(anime)
    return animeList


def insertAnime(values_dict):
    titles = {}
    for key in values_dict:
        if 'title' in key:
            titles[key] = values_dict.get(key)

    a = Anime.objects.update_or_create(mal_id=values_dict.get('mal_id'))[0]
    a.mal_id = values_dict.get('mal_id')
    a.name = values_dict.get('title')
    if not values_dict.get('image_url') is None:
        a.image_url = values_dict.get('image_url')
    if not values_dict.get('trailer_url') is None:
        a.trailer_url = values_dict.get('trailer_url')
    a.titles = titles
    a.type = 'AN'
    a.score = Decimal(values_dict.get('score'))
    a.scored_by = values_dict.get('scored_by')
    a.rank = values_dict.get('rank')
    a.episodes = values_dict.get('episodes')
    a.publication_status = values_dict.get('status')
    if not values_dict.get('broadcast') is None:
        a.broadcast = values_dict.get('broadcast')
    a.save()
    print(values_dict.get('genres'))
    for value in values_dict.get('genres'):
        gen = Genre.objects.get_or_create(
            name=value.get('name'),
            mal_id=value.get('mal_id'),
            type=value.get('type')
        )
        a.genres.add(gen[0])
    for value in values_dict.get('studios'):
        studio = Studio.objects.get_or_create(
            mal_id=value.get('mal_id'),
            name=value.get('name'),
            type=value.get('type')
        )
        a.studios.add(studio[0])
    if not values_dict.get('synopsis') is None:
        a.synopsis = values_dict.get('synopsis')
    a.save()
